import json

from pyrdfrules.api.rdfrules_api import RDFRulesApi
from pyrdfrules.config import Config
from pyrdfrules.engine.result.pipeline import PipelineRunResult

def ensure_started(func):
    def wrapper(*args):
        args[0].__start()
        return func(*args)
    return wrapper

class Engine():
    """
    Base class for RDFRules engine backends. This class contains shared methods and all its descendants represent different methods to communicate with the RDFRules engine.
    """
    
    started: bool = False
    
    api: RDFRulesApi
    
    config: Config
    """
    Configuration of the engine."""
    
    def __init__(self, config: Config) -> None:
        """
        Initializes the engine with the given configuration.

        Args:
            config (Config): Configuration of the engine.
        """
        self.config = config
        pass
    
    def start(self) -> None:
        """
        Starts the engine.
        """
        pass
    
    def __start(self) -> None:
        """
        Starts the engine in a blocking synchronous way if the engine isn't already running.
        
        Used internally when there isa chance the engine might have crashed in the meantime, as we cannot assume it's always running.
        """
        pass
    
    @ensure_started
    def check(self) -> None:
        """Returns without an exception if the instance is still running.
        """
        pass

    @ensure_started    
    def stop(self) -> None:
        """
        Stops the engine.
        """
        pass
    
    @ensure_started
    def launch_pipeline(self) -> PipelineRunResult:
        """
        Launches the pipeline on this specific engine.

        Args:
            pipeline (Pipeline): Pipeline specification to run.

        Returns:
            PipelineRunResult: Returns a non-blocking future.
            
        Throws:    
        
        """
        pass
    
    @ensure_started
    def run_task(self, task: str|dict) -> None:
        """
        Runs a task on the engine.

        Args:
            task (str|dict): Task to run, either string-serialized JSON or JSON represented as a dict.
        """
        
        # todo custom exception
        if not isinstance(task, dict):
            task = json.loads(task)
            
        
        
        pass