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
from pyrdfrules.rdfrules.release import JVM_VERSION, RDFRULES_DOWNLOAD_URI

started = False
result_process = None
server_url = None

_jvm_path = None
_rdfrules_path = None

_workspace_path = None

def get_base_dir():
    return os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "..", ".."))

def get_workspace_dir():
    global _workspace_path
    return _workspace_path

def setup(rdf_rules_path: str = '', jvm_path: str = '', workspace_path: str|Path|None = '') -> None:
    if not workspace_path:
        workspace_path = os.path.join(get_base_dir(), "workspace")
    
    if not rdf_rules_path:
        rdf_rules_path = os.path.join(get_base_dir(), "rdfrules")
        
    if not jvm_path:
        jvm_path = os.path.join(get_base_dir(), "jvm")
    
    global _rdfrules_path
    _rdfrules_path = rdf_rules_path
    
    global _jvm_path
    _jvm_path = jvm_path
    
    global _workspace_path
    _workspace_path = str(workspace_path)
    
    pass

def get_jvm_path() -> str:
    return _jvm_path

def get_rdfrules_path() -> str:
    return _rdfrules_path

def is_jvm_installed() -> bool:
    return os.path.isdir(jdk._JRE_DIR)

def install_jvm():
    if not is_jvm_installed():
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
    java_home = "%s/%s" % (jdk._JRE_DIR, os.listdir(jdk._JRE_DIR)[0])
    
    if platform.system() == "Darwin":
        # todo - why is this necessary? probably not gonna be needed on Linux and Windows...
        java_home += "/Contents/Home"
    
    os.environ["JAVA_HOME"] = java_home
    os.environ["PATH"] = "%s/bin:%s" % (java_home, os.environ["PATH"])
    os.environ["RDFRULES_STOPPING_TOKEN"] = "stoppingtoken"
    os.environ["RDFRULES_WORKSPACE"] = get_workspace_dir()
    
    log().debug(f"JAVA_HOME: {os.environ['JAVA_HOME']}")
    log().debug(f"PATH: {os.environ['PATH']}")
    log().debug(f"RDFRULES_STOPPING_TOKEN: {os.environ['RDFRULES_STOPPING_TOKEN']}")
    log().info(f"RDFRULES_WORKSPACE: {os.environ['RDFRULES_WORKSPACE']}")

def install_rdfrules() -> bool:
    # download compiled version
    path = get_rdfrules_path()
        
    if not os.path.exists(path):
        os.makedirs(path)
    
    target = os.path.join(path, 'rdfrules.zip')
    
    url = RDFRULES_DOWNLOAD_URI
    r = requests.get(url, allow_redirects=True)
    open(target, 'wb').write(r.content)
    
    # unzip
    
    import zipfile
    with zipfile.ZipFile(target, 'r') as zip_ref:
        zip_ref.extractall(path)
    
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
    path = os.path.abspath('../src/rdfrules')
    workspace = get_workspace_dir()

    log().info(f"Starting RDFRules at {path}")
    log().info(f"Workspace at {workspace}")
    
    command = [
        "java",
        "-Dprog.version=1.7.2",
        "-Dprog.revision=3ea05ae9ef9d9258c005a1971721225663d57f98",
        f"-Dprog.home={path}",
        f"-Drdfrules.writable.path={workspace}",
        "-cp", f"{path}/lib/*",
        "com.github.propi.rdfrules.http.Main"
    ]
    
    process = subprocess.Popen(
        command, 
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        preexec_fn=os.setsid
    )
    
    # TODO - rework this
    global result_process
    
    result_process = process.pid
    
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
    
    return proc

def get_server_url():
    return server_url + "/api/"

def stop_rdfrules_process():
    log().info("Stopping RDFRules process")
    os.killpg(os.getpgid(result_process), 15)