import jdk
from multiprocessing import Process

import jpype
import jpype.imports
from jpype.types import *
import os

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
    
def start_rdfrules():
    path = os.path.abspath('../src/rdfrules')

    jpype.startJVM(
        "-Dprog.version=1.7.2",
        "-Dprog.revision=3ea05ae9ef9d9258c005a1971721225663d57f98",
        "-Dprog.home=%s" % path,
        "-Drdfrules.writable.path=.",
        classpath=["%s/lib/*" % path]
    )
    
    jpype.JClass("com.github.propi.rdfrules.http.Main").main([])
    
def start_rdfrules_process():
    proc = Process(target=start_rdfrules) 
    proc.start()
    return proc