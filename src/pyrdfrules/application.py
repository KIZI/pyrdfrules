from pydantic import BaseModel
from pyrdfrules.common.http.url import Url

from pyrdfrules.common.logging.logger import configure_logging, log
from pyrdfrules.config import Config
from pyrdfrules.engine.http_engine import HttpEngine
from pyrdfrules.engine.local_http_engine import LocalHttpEngine
from pyrdfrules.engine.remote_http_engine import RemoteHttpEngine
from pyrdfrules.rdfrules.rdfrules import RDFRules

class Application(BaseModel):
    """
    The Application class provides methods to start and stop local or remote instances of RDFRules.
    """
    
    __rdfrules: RDFRules|None = None
        
    def start_local(self, config: Config|None = None, **kwargs) -> RDFRules:
        """Starts a local instance of RDFRules.
        
        Args:
            config: The configuration to use.
            **kwargs: Additional arguments.
            
        Returns:
            The RDFRules instance.
        
        """
        
        log().info("Starting local RDFRules")
        
        config = Config() if config is None else config
        
        # todo - add optional path to RDFRules
        # todo - add JVM path
        
        self.__rdfrules = RDFRules(
            engine=LocalHttpEngine(
                config=config,
                **kwargs
            ),
            config=config
        )
        
        self.__rdfrules.engine.start()
        
        log().info("Local instance of RDFRules started")
        
        return self.__rdfrules
    
    def start_remote(self, url: Url|str, config: Config|None = None) -> RDFRules:
        """Starts a remote instance of RDFRules.
        """
        
        log().info("Connecting to remote instance of RDFRules at %s", url)
        
        config = Config() if config is None else config
        
        self.__rdfrules = RDFRules(
            engine=RemoteHttpEngine(
                config=config,
                url=url
            ),
            config=config
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