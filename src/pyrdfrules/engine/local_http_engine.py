from multiprocessing import Process
from typing import Awaitable

from pydantic_core import Url
from pyrdfrules.api.http_rdfrules_api import HTTPRDFRulesApi
from pyrdfrules.api.http_rdfrules_api_context import HTTPRDFRulesApiContext
from pyrdfrules.api.rdfrules_api_context import RDFRulesApiContext
from pyrdfrules.engine.engine import Engine
from pyrdfrules.engine.http_engine import HttpEngine
from pyrdfrules.engine.util.jvm import get_server_url, install_jvm, install_rdfrules, is_jvm_installed, is_rdfrules_installed, set_jvm_env, start_rdfrules_process, stop_rdfrules_process

class LocalHttpEngine(HttpEngine):
    """
    Launches a local instance of RDFRules and uses the HTTP API to communicate.
    """
    
    """
    If set to true, will install JVM if JVM is not detected.
    """
    install_jvm: bool = False
    
    """
    If set to true, will install RDFRules locally into src/rdfrules folder if not already present.
    """
    install_rdfrules: bool = False
    
    """
    RDFRules process instance.
    """
    __process: Process
    
    """
    Set to true after all startup checks have passed.
    """
    __ready: bool = False
    
    def __init__(self, install_jvm: bool = False, install_rdfrules: bool = False):
        super().__init__()
        self.install_jvm = install_jvm
        self.install_rdfrules = install_rdfrules
    
    async def install(self) -> Awaitable:
        """Installs RDFRules locally.

        Returns:
            Awaitable: Non-blocking future when the installation process finishes.
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
        
        self.__process = start_rdfrules_process()
    
    async def start(self) -> Awaitable:
        """
        Starts the local HTTP engine.
        Spawns a JVM process in thebackground.

        Returns:
            Awaitable: Returns a non-blocking future.
        """
        
        await super().start()
        
        await self.install()
        
        set_jvm_env()
        
        self.__launch_process()
        
        self.api = HTTPRDFRulesApi(
            HTTPRDFRulesApiContext(
                Url(get_server_url())
            )
        )
        
        pass
    
    async def stop(self) -> Awaitable:
        """
        Stops the engine.
        """
        
        stop_rdfrules_process()
        
        pass