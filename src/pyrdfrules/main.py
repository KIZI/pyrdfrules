import jdk
from multiprocessing import Process

import jpype
import jpype.imports
from jpype.types import *
import os

# this is a sample file - proper structuring and classes will be added later

def test():
    print("Hello from pyrdfrules!")
    
def setup():
    if not os.path.isdir(jdk._JRE_DIR):
        jdk.install("11", jre=True, operating_system=jdk.OS, arch=jdk.ARCH)
    
    java_home = "%s/%s" % (jdk._JRE_DIR, os.listdir(jdk._JRE_DIR)[0])
    
    # todo - why is this necessary? probably not gonna be needed on Linux and Windows...
    java_home += "/Contents/Home"
    
    os.environ["JAVA_HOME"] = java_home
    os.environ["PATH"] = "%s/bin:%s" % (java_home, os.environ["PATH"])
    os.environ["RDFRULES_STOPPING_TOKEN"] = "stoppingtoken"
    
def start_server():
    path = os.path.abspath('../src/rdfrules')

    jpype.startJVM(
        "-Dprog.version=1.7.2"
        "-Dprog.revision=3ea05ae9ef9d9258c005a1971721225663d57f98",
        "-Dprog.home=%s" % path,
        "-Drdfrules.writable.path=."
        classpath=["%s/lib/*" % path]
    )
    
    jpype.JClass("com.github.propi.rdfrules.http.Main").main([])
    
def start():
    proc = Process(target=start_server) 
    proc.start()