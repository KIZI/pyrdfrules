from pyrdfrules.api.task.task_api import TaskApi


class TaskRunner():
    
    api: TaskApi
    
    def __init__(self, api: TaskApi) -> None:
        self.api = api
        pass
    
    async def create_task_from_string(self, task: str) -> None:
        """Creates a task.
        """
        
        await self.api.create_task(task)
        
        pass