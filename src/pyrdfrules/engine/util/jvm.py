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

from pyrdfrules.engine.exception.failed_to_start_exception import FailedToStartException

started = False

class TeeOut(StringIO):
    def __init__(self, pipe, std=sys.__stdout__):
        self.pipe = pipe

    def write(self, s):
        self.pipe.send(s.strip())

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
    print("Reading output")
    
    for line in iter(process.stdout.readline, b''):
        pipe.send(line.strip())
        
    process.stdout.close()
    
def read_output_stderr(pipe, process):
    for line in iter(process.stderr.readline, ''):
        pipe.send(line.strip())
        
    process.stderr.close()
    
def start_rdfrules(pipe):
    path = os.path.abspath('../src/rdfrules')
    
    print(f"Starting RDFRules at {path}")
    
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
        text=True
    )
    
    Thread(target=read_output_stdout, args=(pipe, process)).start()
    Thread(target=read_output_stderr, args=(pipe, process)).start()

    process.wait()

def wait_for_pipe(pipe):
    global started
    
    while True:
        try:
            recv = pipe.recv().strip()
            
            if recv.startswith("Server online"):
                started = True
                break
            
        # TODO logs
            
        except EOFError:
            break
    
def start_rdfrules_process():
    parent_pipe, child_pipe = Pipe()
    
    pipe_thread = Thread(target=wait_for_pipe, args=(parent_pipe,))
    pipe_thread.start()
    
    proc = Process(target=start_rdfrules, args=(child_pipe, ), daemon=True)
    proc.start()
    
    pipe_thread.join(10)
    
    if not started:
        raise FailedToStartException("RDFRules process did not start")
    
    print("Started RDFRules process")
    
    return proc