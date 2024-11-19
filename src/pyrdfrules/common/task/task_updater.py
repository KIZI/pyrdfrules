import time
from typing import Awaitable
from pyrdfrules.api.task.task_api import TaskApi
from pyrdfrules.common.task.task import Task
from pyrdfrules.config import Config


class TaskUpdater():
    
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
    
    def run(self, task: Task) -> Awaitable[None]:
        """Runs the task.
        """
        
        while not task.is_finished():
            time.sleep(int(self.config.task_update_interval_ms) / 1000)
            
            response = self.api.get_task_response(task.id)
            self.update_task(task, response)
            
        pass
    
    def update_task(self, task: Task, response: dict) -> Awaitable[Task]:
        """Updates a task.
        """
        
        task.update_from_dict(response)
        
        return task