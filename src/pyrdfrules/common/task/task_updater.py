import time
from typing import Awaitable
from pyrdfrules.api.task.task_api import TaskApi
from pyrdfrules.common.task.task import Task


class TaskUpdater():
    
    api: TaskApi
    """API used to interact with the RDFRules instance.
    """
    
    task_update_interval_ms: int = 1000
    """Update interval for the task status.
    """
    
    def __init__(self, api: TaskApi) -> None:
        self.api = api
        pass
    
    async def run(self, task: Task) -> Awaitable[None]:
        """Runs the task.
        """
        
        time.sleep(self.task_update_interval_ms / 1000)
        
        while not task.is_finished():
            response = await self.api.get_task_response(task.id)
            print(response)
            await self.update_task(task, response)
            time.sleep(self.task_update_interval_ms / 1000)
        
        pass
    
    async def update_task(self, task: Task, response: dict) -> Awaitable[Task]:
        """Updates a task.
        """
        
        task.update_from_dict(response)
        
        return task