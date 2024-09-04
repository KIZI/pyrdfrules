from typing import Awaitable
from pydantic import BaseModel

from pyrdfrules.engine.engine import Engine

class RDFRules(BaseModel):
    
    engine: Engine
    
    async def start(self) -> Awaitable:
        """
        Starts the engine.
        """
        
        await self.engine.start()
        
        pass