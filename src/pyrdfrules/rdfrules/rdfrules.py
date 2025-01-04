from typing import Any

from pyrdfrules.api.workspace.workspace_api import WorkspaceApi
from pyrdfrules.common.file.workspace import Workspace
from pyrdfrules.common.task.task_runner import TaskRunner
from pyrdfrules.config import Config
from pyrdfrules.engine.engine import Engine

class RDFRules():
    """Represents the RDFRules engine.
    """
    
    engine: Engine
    """RDFRules engine.
    """
    
    workspace: Workspace
    """Workspace classes.
    """
    
    task: TaskRunner
    """Task runner.
    """
    
    config: Config
    """Configuration.
    """
    
    def __init__(self, engine: Engine, config: Config) -> None:
        self.engine = engine
        self.config = config
        self.engine.config = config
        pass
    
    def __getattr__(self, name: str) -> Any:
        if name == 'workspace':
            # should not be cached, because it can change
            return Workspace(self.engine.api.workspace)
        
        if name == 'task':
            # todo this can be cached
            return TaskRunner(self.engine.api.task, self.config)
        
        pass
    
    def start(self) -> None:
        """
        Starts the engine.
        """
        
        self.engine.start()
        
        pass