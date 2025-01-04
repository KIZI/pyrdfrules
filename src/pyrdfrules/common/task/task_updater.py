import time
from typing import Generator
from pyrdfrules.api.task.task_api import TaskApi
from pyrdfrules.common.task.task import Task
from pyrdfrules.config import Config

class TaskUpdater():
    """
    The TaskUpdater class handles the updating of tasks.
    """
    
    api: TaskApi
    """API used to interact with the RDFRules instance.
    """
    
    config: Config
    """Configuration.
    """
    
    def __init__(self, api: TaskApi, config: Config) -> None:
        self.api = api
        self.config = config
        pass
    
    def run(self, task: Task) -> Generator[Task, None, None]:
        """Runs the task.
        """
        
        while not task.is_finished():
            time.sleep(int(self.config.task_update_interval_ms) / 1000)
            
            response = self.api.get_task_response(task.id)
            self.update_task(task, response)
            yield task
            
        pass
    
    def stop(self, task: Task) -> None:
        """Stops the task.
        """
        
        self.api.interrupt_task(task_id=task.id)
        task._stop()
        
        pass
    
    def update_task(self, task: Task, response: dict) -> Task:
        """Updates a task.
        """
        
        task.update_from_dict(response)
        
        return task
    
    def run_task_step(self, task: Task) -> None:
        """Runs a task step. Raises exceptions if the task is finished.
        """
        
        response = self.api.get_task_response(task.id)
        self.update_task(task, response)
        
        pass