from typing import Awaitable
from pydantic import BaseModel

from pyrdfrules.common.file.workspace import Workspace
from pyrdfrules.common.rule.ruleset import Ruleset
from pyrdfrules.engine.engine import Engine
from pyrdfrules.engine.local_http_engine import LocalHttpEngine
from pyrdfrules.pipeline.pipeline import Pipeline

class RDFRules(BaseModel):
    
    engine: Engine = LocalHttpEngine()
    
    workspace: Workspace
    
    async def launch(self, pipeline: Pipeline) -> Awaitable[Ruleset]:
        """
        Launches the pipeline and returns the ruleset.
        """
        
        self.engine.launch_pipeline(pipeline)
        
        pass