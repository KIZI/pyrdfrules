from typing import List
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
    
    __rdfrules: List[RDFRules] = []
        
    def start_local(self, config: Config|None = None, **kwargs) -> RDFRules:
        """Starts a local instance of RDFRules.
        
        Args:
            config: The configuration to use.
            install_jvm: True if JVM should be installed.
            install_rdfrules: True if RDFRules should be installed.
            rdfrules_path:  Path where RDFRules is installed, or where it should be downloaded to.
            jvm_path: Path where JVM is installed, or where it should be downloaded to.
            port: Port to use, if not specified, will default to 8851 + the number of instances already started.
            **kwargs: Additional arguments.
            
        Returns:
            The RDFRules instance.
        
        """
        
        if "port" not in kwargs and len(self.__rdfrules) > 0:
            kwargs["port"] = 8851 + len(self.__rdfrules)
        
        log().info("Starting local RDFRules")
        
        config = Config() if config is None else config
        
        rdfrules = RDFRules(
            engine=LocalHttpEngine(
                config=config,
                **kwargs
            ),
            config=config
        )
        
        rdfrules.engine.start()
        
        self.__rdfrules.append(rdfrules)
        configure_logging(rdfrules.config)
        
        log().info("Local instance of RDFRules started")
        
        return rdfrules
    
    def start_remote(self, url: Url|str, config: Config|None = None) -> RDFRules:
        """Starts a remote instance of RDFRules.
        """
        
        log().info("Connecting to remote instance of RDFRules at %s", url)
        
        config = Config() if config is None else config
        
        rdfrules = RDFRules(
            engine=RemoteHttpEngine(
                config=config,
                url=url
            ),
            config=config
        )
        
        self.__rdfrules.append(rdfrules)
        
        configure_logging(rdfrules.config)
        
        rdfrules.engine.start()
        
        log().info("Connected to remote instance of RDFRules at %s", url)
        
        return rdfrules
    
    def stop(self) -> None:
        """Stops the application.
        """
        
        log().info(f"Stopping {len(self.__rdfrules)} instance(s) of RDFRules")
        
        count = len(self.__rdfrules)
        it = 0
        
        for rdfrules in self.__rdfrules:
            it += 1
            log().info(f"Stopping RDFRules instance {it} of {count}")
            rdfrules.engine.stop()
            log().info(f"Stopped RDFRules instance {it} of {count}")