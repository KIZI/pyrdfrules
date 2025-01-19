from multiprocessing import Process
import re

from pyrdfrules.common.http.url import Url
from pyrdfrules.api.http_rdfrules_api import HTTPRDFRulesApi
from pyrdfrules.api.http_rdfrules_api_context import HTTPRDFRulesApiContext
from pyrdfrules.api.rdfrules_api_context import RDFRulesApiContext
from pyrdfrules.common.logging.logger import log
from pyrdfrules.config import Config
from pyrdfrules.engine.engine import Engine
from pyrdfrules.engine.exception.failed_to_start_exception import FailedToStartException
from pyrdfrules.engine.http_engine import HttpEngine
from pyrdfrules.engine.util.jvm import get_server_url, install_jvm, install_rdfrules, is_jvm_installed, is_rdfrules_installed, set_jvm_env, start_rdfrules_process, stop_rdfrules_process, setup

class LocalHttpEngine(HttpEngine):
    """
    Launches a local instance of RDFRules and uses the HTTP API to communicate.
    """
    
    install_jvm: bool = False
    """
    If set to true, will install JVM if JVM is not detected.
    """
    
    install_rdfrules: bool = False
    """
    If set to true, will install RDFRules locally into src/rdfrules folder if not already present.
    """
    
    rdfrules_path : str = ''
    """
    Path to the RDFRules installation.
    If not set, will default to src/rdfrules.
    Can be used to specify the PyRDFRules downloaded RDFRules location.
    """
    
    jvm_path: str = ''
    """
    Path to the JVM installation.
    If not set, will try to use the JVM installed on the system.
    Can be used to specify the PyRDFRules downloaded JVM location.
    """
    
    """
    RDFRules process instance.
    """
    __process: Process
    
    __pid: int
    """
    PID of the RDFRules process.
    """

    __ready: bool = False
    """
    Set to true after all startup checks have passed.
    """
    
    __port: int = None
    
    __url: str = None
    """
    URL of the RDFRules server.
    """
    
    def __init__(self, config : Config, install_jvm: bool = False, install_rdfrules: bool = False, rdfrules_path: str = '', jvm_path: str = '', port: int|None = None) -> None:
        super().__init__(config=config)
        self.install_jvm = install_jvm
        self.install_rdfrules = install_rdfrules
        self.rdfrules_path = rdfrules_path
        self.jvm_path = jvm_path
        self.__port = port
        
        setup(rdfrules_path, jvm_path, workspace_path=config.workspace_path, port=port)
    
    def install(self) -> None:
        """Installs RDFRules locally.
        """
        if not is_jvm_installed() and self.install_jvm:
            install_jvm()
            
        if not is_rdfrules_installed() and self.install_rdfrules:
            install_rdfrules()
            
        self.__ready = True
    
    def __launch_process(self) -> None:
        if not self.__ready:
            # throw exception
            pass
        
        try :
            result = start_rdfrules_process()
            self.__process = result[0]
            self.__pid = result[1]
            
            self.__url = get_server_url()
            
            if self.__port is not None:
                # stupid hack
                # this can be solved by waiting for the server and removing the one global variable
                current_port = re.search(r':(\d+)', self.__url).group(1)
                self.__url = self.__url.replace(current_port, str(self.__port))

        except FailedToStartException as e:
            log().error(f"Failed to start RDFRules, check if the port {self.__port} is already in use")
            raise e

    
    def start(self) -> None:
        """
        Starts the local HTTP engine.
        Spawns a JVM process in thebackground.
        """
        
        super().start()
        
        self.install()
        
        set_jvm_env()
        
        self.__launch_process()
        
        self.api = HTTPRDFRulesApi(
            HTTPRDFRulesApiContext(
                Url(self.__url),
                self.config
            )
        )
        
        pass
    
    def stop(self) -> None:
        """
        Stops the engine.
        """
        
        if not self.__ready:
            log().warning("Engine not ready, cannot stop")
            return        
        
        stop_rdfrules_process(self.__pid)
        self.__ready = False
        
        pass