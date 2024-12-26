from pydantic import BaseModel
from pydantic_core import Url

from pyrdfrules.common.logging.logger import configure_logging, log
from pyrdfrules.config import Config
from pyrdfrules.engine.http_engine import HttpEngine
from pyrdfrules.engine.local_http_engine import LocalHttpEngine
from pyrdfrules.engine.remote_http_engine import RemoteHttpEngine
from pyrdfrules.rdfrules.rdfrules import RDFRules

class Application(BaseModel):
    
    __rdfrules: RDFRules
        
    def start_local(self, **kwargs) -> RDFRules:
        """Starts a local instance of RDFRules.
        """
        
        log().info("Starting local RDFRules")
        
        # todo - add optional path to RDFRules
        # todo - add JVM path
        
        self.__rdfrules = RDFRules(
            engine=LocalHttpEngine(
                kwargs
            ),
            config=Config()
        )
        
        self.__rdfrules.engine.start()
        
        log().info("Local instance of RDFRules started")
        
        return self.__rdfrules
    
    def start_remote(self, url: Url|str, config: Config|None = None) -> RDFRules:
        """Starts a remote instance of RDFRules.
        """
        
        log().info("Connecting to remote instance of RDFRules at %s", url)
        
        self.__rdfrules = RDFRules(
            engine=RemoteHttpEngine(
                url=url
            ),
            config=Config() if config is None else config
        )
        
        configure_logging(self.__rdfrules.config)
        
        self.__rdfrules.engine.start()
        
        log().info("Connected to remote instance of RDFRules at %s", url)
        
        return self.__rdfrules
    
    def stop(self) -> None:
        """Stops the application.
        """
        
        log().info("Stopping RDFRules")
        
        self.__rdfrules.engine.stop()