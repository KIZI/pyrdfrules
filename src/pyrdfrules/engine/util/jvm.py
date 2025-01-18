
from pathlib import Path
import subprocess
from threading import Thread
from time import sleep
import jdk
from multiprocessing import Process, Pipe

import jpype.imports
from jpype.types import *
import os
import requests
import platform

from pyrdfrules.common.logging.logger import log
from pyrdfrules.engine.exception.failed_to_start_exception import FailedToStartException
from pyrdfrules.rdfrules.release import JVM_VERSION, RDFRULES_DOWNLOAD_URI, RDFRULES_VERSION, RDFRULES_REVISION

from tqdm import tqdm
import zipfile

started = False
result_process = None
result_processes = []
server_url = None

_jvm_path = None
_rdfrules_path = None

_workspace_path = None
_port = None

def get_base_dir():
    return os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "..", ".."))

def get_workspace_dir():
    global _workspace_path
    return _workspace_path

def setup(rdf_rules_path: str = '', jvm_path: str = '', workspace_path: str|Path|None = '', port = None) -> None:
    if not workspace_path:
        workspace_path = os.path.join(get_base_dir(), "workspace")
    
    if not rdf_rules_path:
        rdf_rules_path = os.path.join(get_base_dir(), "rdfrules")
    
    global _rdfrules_path
    _rdfrules_path = rdf_rules_path
    
    global _jvm_path
    _jvm_path = jvm_path
    
    global _workspace_path
    _workspace_path = str(workspace_path)
    
    global _port
    if port is not None:
        if not isinstance(port, int):
            raise ValueError("Port must be an integer")
        
        if int(port) < 0 or int(port) > 65535:
            raise ValueError("Port must be between 0 and 65535")

    _port = port
    
    if not os.path.exists(_workspace_path):
        os.makedirs(_workspace_path, exist_ok=True)
        
    if not os.path.exists(_rdfrules_path):
        os.makedirs(_rdfrules_path, exist_ok=True)
    
    if _jvm_path and not os.path.exists(_jvm_path):
        os.makedirs(_jvm_path, exist_ok=True)
    
    pass

def get_jvm_path() -> str:
    if not _jvm_path:
        return jdk._JRE_DIR

    return _jvm_path

def get_jvm_home() -> str:
    parts = [
        get_jvm_path(),
        os.listdir(get_jvm_path())[0]
    ]
        
    if platform.system() == "Darwin":
        # todo - why is this necessary? probably not gonna be needed on Linux and Windows...
        parts.append("Contents")
        parts.append("Home")
    
    return os.path.join(*parts)

def get_rdfrules_path() -> str:
    return _rdfrules_path

def is_jvm_installed() -> bool:
    return os.path.isdir(get_jvm_path()) and len(os.listdir(get_jvm_path())) > 0

def install_jvm():
    if not is_jvm_installed():
        log().info(f"JVM not installed, installing at {get_jvm_path()}")
        log().info(f"JVM version: {JVM_VERSION}")
        log().info(f"This may take a while...")
        jdk.install(JVM_VERSION, jre=True, operating_system=jdk.OS, arch=jdk.ARCH, path=get_jvm_path())
    
def is_rdfrules_installed() -> bool:
    path = get_rdfrules_path()
    
    # check if the directory exists
    shapes = [
        'lib',
        'bin',
        'bin/main',
    ]
    
    return all([os.path.exists(os.path.join(path, shape)) for shape in shapes])

def set_jvm_env() -> None:
    java_home = get_jvm_home()
    
    os.environ["JAVA_HOME"] = java_home
    os.environ["PATH"] = os.path.join(java_home, "bin") + ":%s" % (os.environ["PATH"])
    os.environ["RDFRULES_STOPPING_TOKEN"] = "stoppingtoken"
    os.environ["RDFRULES_WORKSPACE"] = get_workspace_dir()
    
    global _port
    
    if _port is not None:
        os.environ["RDFRULES_PORT"] = str(_port)
    
    log().debug(f"JAVA_HOME: {os.environ['JAVA_HOME']}")
    log().debug(f"PATH: {os.environ['PATH']}")
    log().debug(f"RDFRULES_STOPPING_TOKEN: {os.environ['RDFRULES_STOPPING_TOKEN']}")
    log().info(f"RDFRULES_WORKSPACE: {os.environ['RDFRULES_WORKSPACE']}")

def install_rdfrules() -> bool:
    # download compiled version
    path = get_rdfrules_path()
        
    if not os.path.exists(path):
        os.makedirs(path)
    
    target = os.path.join(path, 'rdfrules.zip')
    
    with tqdm(unit='B', unit_scale=True, unit_divisor=1024, miniters=1, desc="Downloading RDFRules") as t:
        def update_to(size, totalSize):
            t.total = totalSize
            t.update(size)
        
        url = RDFRULES_DOWNLOAD_URI
        r = requests.get(url, allow_redirects=True, stream=True)
        
        with open(target, 'wb') as f:            
            for data in r.iter_content(chunk_size=8192):
                size = f.write(data)
                update_to(size, int(r.headers.get('content-length')))
    
    # unzip
    
    with tqdm(unit='B', unit_scale=True, unit_divisor=1024, miniters=1, desc="Extracting RDFRules") as t:
        with open(target, 'rb') as f:
            with zipfile.ZipFile(f, 'r') as zip_ref:
                
                t.total = sum([zinfo.file_size for zinfo in zip_ref.filelist])
                
                for file in zip_ref.namelist():
                    zip_ref.extract(file, path)
                    t.update(zip_ref.getinfo(file).file_size)
    
    pass

def read_output_stdout(pipe, process):
    log().debug("Reading output")
    
    try:
        for line in iter(process.stdout.readline, b''):
            pipe.send(line.strip())
        
        process.stdout.close()
    except BrokenPipeError:
        pass
    
def read_output_stderr(pipe, process):
    try:
        for line in iter(process.stderr.readline, b''):
            pipe.send(line.strip())
        
        process.stderr.close()
    except BrokenPipeError:
        pass
    
def start_rdfrules(pipe):
    path = get_rdfrules_path()
    workspace = get_workspace_dir()

    log().info(f"Starting RDFRules at {path}")
    log().info(f"Workspace at {workspace}")
    
    command = [
        os.path.join(get_jvm_home(), "bin", "java"),
        f"-Dprog.version={RDFRULES_VERSION}",
        f"-Dprog.revision={RDFRULES_REVISION}",
        f"-Dprog.home={path}",
        f"-Drdfrules.writable.path={workspace}",
        "-cp", os.path.join(path, "lib", "*"),
        "com.github.propi.rdfrules.http.Main"
    ]

    process = subprocess.Popen(
        command, 
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        preexec_fn=os.setsid if "setsid" in dir(os) else None
    )
    
    # TODO - rework this
    global result_processes
    result_processes.append(process.pid)
    
    Thread(target=read_output_stdout, args=(pipe, process)).start()
    Thread(target=read_output_stderr, args=(pipe, process)).start()

    process.wait()

def wait_for_pipe(pipe):
    global started
    global server_url
    
    while True:
        try:
            recv = pipe.recv().strip()
            log().debug(recv)
            
            if recv.startswith("Server online at"):
                server_url = recv.split(" ")[-1]
                started = True
                break
            
        # TODO logs
            
        except EOFError:
            break
    
def start_rdfrules_process():
    parent_pipe, child_pipe = Pipe()
    
    pipe_thread = Thread(target=wait_for_pipe, args=(parent_pipe,))
    pipe_thread.start()
    
    proc = Thread(target=start_rdfrules, args=(child_pipe, ))
    proc.start()
    
    # TODO -  make this configurable
    pipe_thread.join(10)
    
    # TODO - Parse output for a better error message - port in use etc
    
    if not started:
        log().critical("RDFRules process did not start")
        raise FailedToStartException("RDFRules process did not start")
    
    log().debug("Started RDFRules process")
    
    global result_processes
    proccess_id = result_processes[-1]
    
    return [proc, proccess_id]

def get_server_url():
    if server_url.endswith("/"):
        return server_url + "api/"
    
    return server_url + "/api/"

def stop_rdfrules_process(proccess_id: int):
    log().info("Stopping RDFRules process")
    os.killpg(os.getpgid(proccess_id), 15)