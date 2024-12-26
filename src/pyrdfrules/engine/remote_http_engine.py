from multiprocessing import Process

from pyrdfrules.common.http.url import Url
from pyrdfrules.api.http_rdfrules_api import HTTPRDFRulesApi
from pyrdfrules.api.http_rdfrules_api_context import HTTPRDFRulesApiContext
from pyrdfrules.api.rdfrules_api_context import RDFRulesApiContext
from pyrdfrules.config import Config
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
    
    def __init__(self, config: Config, url: Url|str):
        super().__init__(config=config)
        self.url = str(url)
    
    def install(self) -> None:
        """Installs RDFRules locally.
        """
        pass
    
    def start(self) -> None:
        """
        Starts the local HTTP engine.
        Spawns a JVM process in thebackground.
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
    
    def stop(self) -> None:
        """
        Stops the engine.
        """
        
        pass