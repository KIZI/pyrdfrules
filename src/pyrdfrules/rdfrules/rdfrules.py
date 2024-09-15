from typing import Any, Awaitable

from pyrdfrules.api.workspace.workspace_api import WorkspaceApi
from pyrdfrules.common.file.workspace import Workspace
from pyrdfrules.common.task.task_runner import TaskRunner
from pyrdfrules.engine.engine import Engine

class RDFRules():
    
    engine: Engine
    
    workspace: Workspace
    
    task: TaskRunner
    
    def __init__(self, engine: Engine) -> None:
        self.engine = engine
        pass
    
    def __getattr__(self, name: str) -> Any:
        if name == 'workspace':
            # should not be cached, because it can change
            return Workspace(self.engine.api.workspace)
        
        if name == 'task':
            # todo this can be cached
            return TaskRunner(self.engine.api.task)
        
        pass
    
    async def start(self) -> Awaitable:
        """
        Starts the engine.
        """
        
        await self.engine.start()
        
        pass