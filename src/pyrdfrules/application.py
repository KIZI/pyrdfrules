from pydantic import BaseModel
from pydantic_core import Url

from pyrdfrules.engine.http_engine import HttpEngine
from pyrdfrules.engine.local_http_engine import LocalHttpEngine
from pyrdfrules.engine.remote_http_engine import RemoteHttpEngine
from pyrdfrules.rdfrules.rdfrules import RDFRules

class Application(BaseModel):
    
    __rdfrules: RDFRules
        
    async def start_local(self, **kwargs) -> RDFRules:
        """Starts a local instance of RDFRules.
        """
        
        self.__rdfrules = RDFRules(
            engine=LocalHttpEngine(
                kwargs
            )
        )
        
        await self.__rdfrules.engine.start()
        
        return self.__rdfrules
    
    async def start_remote(self, url: Url|str) -> RDFRules:
        """Starts a remote instance of RDFRules.
        """
        
        self.__rdfrules = RDFRules(
            engine=RemoteHttpEngine(
                url=url
            )
        )
        
        await self.__rdfrules.engine.start()
        
        return self.__rdfrules
    
    async def stop(self) -> None:
        """Stops the application.
        """
        
        await self.__rdfrules.engine.stop()

    def check(self):
        """Checks the liveliness state of the application.
        """