import json
from typing import Awaitable
from pydantic import BaseModel

from pyrdfrules.engine.result.pipeline import PipelineRunResult
from pyrdfrules.pipeline.pipeline import Pipeline

def ensure_started(func):
    def wrapper(*args):
        args[0].__start()
        return func(*args)
    return wrapper

class Engine(BaseModel):
    """
    Base class for RDFRules engine backends. This class contains shared methods and all its descendants represent different methods to communicate with the RDFRules engine.
    """
    
    started: bool = False
    
    async def start(self) -> Awaitable:
        """
        Starts the engine.

        Returns:
            Awaitable: Returns a future.
        """
        pass
    
    def __start(self) -> None:
        """
        Starts the engine in a blocking synchronous way if the engine isn't already running.
        
        Used internally when there isa chance the engine might have crashed in the meantime, as we cannot assume it's always running.
        """
        pass
    
    @ensure_started
    async def check(self) -> Awaitable:
        """Returns without an exception if the instance is still running.

        Returns:
            Awaitable: Non-blocking future.
        """
        pass

    @ensure_started    
    async def stop(self) -> Awaitable:
        """
        Stops the engine.
        """
        pass
    
    @ensure_started
    async def launch_pipeline(self, pipeline: Pipeline) -> Awaitable[PipelineRunResult]:
        """
        Launches the pipeline on this specific engine.

        Args:
            pipeline (Pipeline): Pipeline specification to run.

        Returns:
            Awaitable[PipelineRunResult]: Returns a non-blocking future.
            
        Throws:    
        
        """
        pass
    
    
    
    @ensure_started
    async def run_task(self, task: str|dict) -> Awaitable[None]:
        """
        Runs a task on the engine.

        Args:
            task (str|dict): Task to run, either string-serialized JSON or JSON represented as a dict.

        Returns:
            Awaitable[None]: Returns a non-blocking future.
        """
        
        # todo custom exception
        if not isinstance(task, dict):
            task = json.loads(task)
            
        
        
        pass