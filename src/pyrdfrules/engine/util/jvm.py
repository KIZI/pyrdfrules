import subprocess
from threading import Thread
from time import sleep
import jdk
from multiprocessing import Process, Pipe

import jpype
import jpype.imports
from jpype.types import *
import os
import sys
from io import StringIO

from pyrdfrules.common.logging.logger import log
from pyrdfrules.engine.exception.failed_to_start_exception import FailedToStartException

started = False
result_process = None
server_url = None

def is_jvm_installed() -> bool:
    return os.path.isdir(jdk._JRE_DIR)

def install_jvm():
    if not is_jvm_installed():
        jdk.install("11", jre=True, operating_system=jdk.OS, arch=jdk.ARCH)
    
def is_rdfrules_installed(path: str = '../src/rdfrules') -> bool:
    return os.path.exists(path)

def set_jvm_env() -> None:
    java_home = "%s/%s" % (jdk._JRE_DIR, os.listdir(jdk._JRE_DIR)[0])
    
    # todo - why is this necessary? probably not gonna be needed on Linux and Windows...
    java_home += "/Contents/Home"
    
    os.environ["JAVA_HOME"] = java_home
    os.environ["PATH"] = "%s/bin:%s" % (java_home, os.environ["PATH"])
    os.environ["RDFRULES_STOPPING_TOKEN"] = "stoppingtoken"

def install_rdfrules(path: str = '') -> bool:
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
    
    log().info(f"Starting RDFRules at {path}")
    
    command = [
        "java",
        "-Dprog.version=1.7.2",
        "-Dprog.revision=3ea05ae9ef9d9258c005a1971721225663d57f98",
        f"-Dprog.home={path}",
        "-Drdfrules.writable.path=.",
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
    return server_url

def stop_rdfrules_process():
    log().info("Stopping RDFRules process")
    os.killpg(os.getpgid(result_process), 15)