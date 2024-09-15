from typing import Awaitable

from pyrdfrules.engine.engine import Engine

class RDFRules():
    
    engine: Engine
    
    def __init__(self, engine: Engine) -> None:
        self.engine = engine
        pass
    
    async def start(self) -> Awaitable:
        """
        Starts the engine.
        """
        
        await self.engine.start()
        
        pass