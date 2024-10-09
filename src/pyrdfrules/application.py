from pydantic import BaseModel
from pydantic_core import Url

from pyrdfrules.common.logging.logger import log
from pyrdfrules.config import Config
from pyrdfrules.engine.http_engine import HttpEngine
from pyrdfrules.engine.local_http_engine import LocalHttpEngine
from pyrdfrules.engine.remote_http_engine import RemoteHttpEngine
from pyrdfrules.rdfrules.rdfrules import RDFRules

class Application(BaseModel):
    
    __rdfrules: RDFRules
        
    async def start_local(self, **kwargs) -> RDFRules:
        """Starts a local instance of RDFRules.
        """
        
        log().info("Starting local RDFRules")
        
        self.__rdfrules = RDFRules(
            engine=LocalHttpEngine(
                kwargs
            ),
            config=Config()
        )
        
        await self.__rdfrules.engine.start()
        
        log().info("Local instance of RDFRules started")
        
        return self.__rdfrules
    
    async def start_remote(self, url: Url|str) -> RDFRules:
        """Starts a remote instance of RDFRules.
        """
        
        log().info("Connecting to remote instance of RDFRules at %s", url)
        
        self.__rdfrules = RDFRules(
            engine=RemoteHttpEngine(
                url=url
            ),
            config=Config()
        )
        
        await self.__rdfrules.engine.start()
        
        return self.__rdfrules
    
    async def stop(self) -> None:
        """Stops the application.
        """
        
        await self.__rdfrules.engine.stop()