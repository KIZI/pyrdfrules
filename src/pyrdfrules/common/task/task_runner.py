from pyrdfrules.api.task.task_api import TaskApi
from pyrdfrules.common.task.task import Task


class TaskRunner():
    
    api: TaskApi
    
    def __init__(self, api: TaskApi) -> None:
        self.api = api
        pass
    
    async def create_task_from_string(self, task: str) -> Task:
        """Creates a task.
        """
        
        return await self.api.create_task(task)
    
    async def get_task_by_id(self, task_id: str) -> Task:
        """Get a task, or update status of an existing task.
        """
        
        return await self.api.get_task(task_id)
    
    async def update_task(self, task: Task) -> Task:
        """Updates a task.
        """
        
        return await self.api.get_task(task = task)