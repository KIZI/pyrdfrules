from multiprocessing import Process

from pyrdfrules.common.http.url import Url
from pyrdfrules.api.http_rdfrules_api import HTTPRDFRulesApi
from pyrdfrules.api.http_rdfrules_api_context import HTTPRDFRulesApiContext
from pyrdfrules.api.rdfrules_api_context import RDFRulesApiContext
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
    

    __ready: bool = False
    """
    Set to true after all startup checks have passed.
    """
    
    def __init__(self, config : Config, install_jvm: bool = False, install_rdfrules: bool = False, rdfrules_path: str = '', jvm_path: str = '') -> None:
        super().__init__(config=config)
        self.install_jvm = install_jvm
        self.install_rdfrules = install_rdfrules
        self.rdfrules_path = rdfrules_path
        self.jvm_path = jvm_path
        
        setup(rdfrules_path, jvm_path, workspace_path=config.workspace_path)
    
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
            self.__process = start_rdfrules_process()
        except FailedToStartException as e:
            exit(1)

    
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
                Url(get_server_url()),
                self.config
            )
        )
        
        pass
    
    def stop(self) -> None:
        """
        Stops the engine.
        """
        
        stop_rdfrules_process()
        
        pass