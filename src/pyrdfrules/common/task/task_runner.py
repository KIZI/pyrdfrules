from pyrdfrules.api.task.task_api import TaskApi
from pyrdfrules.common.task.task import Task
from pyrdfrules.common.task.task_updater import TaskUpdater


class TaskRunner():
    
    api: TaskApi
    
    task_updater: TaskUpdater
    
    def __init__(self, api: TaskApi) -> None:
        self.api = api
        self.task_updater = TaskUpdater(api)
        pass
    
    async def create_task_from_string(self, task: str) -> Task:
        """Creates a task.
        """
        
        task = await self.api.create_task(task)
        
        task.on_log_message += lambda message: print(message)
        task.on_finished += lambda message: print('Task finished', message)
        
        return task
    
    async def run_task(self, task: Task) -> None:
        """Runs the task to completion.
        """
        
        await self.task_updater.run(task)
    
    async def get_task_by_id(self, task_id: str) -> Task:
        """Get a task, or update status of an existing task.
        """
        
        return await self.api.get_task(task_id)
    
    async def update_task(self, task: Task) -> Task:
        """Updates a task.
        """
        
        return await self.api.get_task(task = task)