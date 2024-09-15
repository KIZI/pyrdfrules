from typing import Any, Awaitable

from pyrdfrules.api.workspace.workspace_api import WorkspaceApi
from pyrdfrules.common.file.workspace import Workspace
from pyrdfrules.engine.engine import Engine

class RDFRules():
    
    engine: Engine
    
    workspace: Workspace
    
    def __init__(self, engine: Engine) -> None:
        self.engine = engine
        pass
    
    def __getattr__(self, name: str) -> Any:
        if name == 'workspace':
            return Workspace(self.engine.api.workspace)
        
        pass
    
    async def start(self) -> Awaitable:
        """
        Starts the engine.
        """
        
        await self.engine.start()
        
        pass