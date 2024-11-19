from multiprocessing import Process
from typing import Awaitable

from pydantic_core import Url
from pyrdfrules.api.http_rdfrules_api import HTTPRDFRulesApi
from pyrdfrules.api.http_rdfrules_api_context import HTTPRDFRulesApiContext
from pyrdfrules.api.rdfrules_api_context import RDFRulesApiContext
from pyrdfrules.engine.engine import Engine
from pyrdfrules.engine.http_engine import HttpEngine
from pyrdfrules.engine.util.jvm import get_server_url, install_jvm, install_rdfrules, is_jvm_installed, is_rdfrules_installed, set_jvm_env, start_rdfrules_process, stop_rdfrules_process

class RemoteHttpEngine(HttpEngine):
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
    
    url: str
    
    def __init__(self, url: Url|str):
        super().__init__()
        self.url = str(url)
    
    def install(self) -> Awaitable:
        """Installs RDFRules locally.

        Returns:
            Awaitable: Non-blocking future when the installation process finishes.
        """
        pass
    
    def start(self) -> Awaitable:
        """
        Starts the local HTTP engine.
        Spawns a JVM process in thebackground.

        Returns:
            Awaitable: Returns a non-blocking future.
        """
        
        # todo check if remote server is running
        
        super().start()
        
        self.install()
        
        self.api = HTTPRDFRulesApi(
            HTTPRDFRulesApiContext(
                Url(self.url),
                self.config
            )
        )
        
        pass
    
    def stop(self) -> Awaitable:
        """
        Stops the engine.
        """
        
        pass