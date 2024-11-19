from pyrdfrules.api.task.task_api import TaskApi
from pyrdfrules.common.logging.logger import log
from pyrdfrules.common.task.task import Task
from pyrdfrules.common.task.task_updater import TaskUpdater
from pyrdfrules.config import Config


class TaskRunner():
    
    api: TaskApi
    
    task_updater: TaskUpdater
    
    config: Config
    
    def __init__(self, api: TaskApi, config: Config) -> None:
        self.api = api
        self.task_updater = TaskUpdater(api, config)
        self.config = config
        
        pass
    
    def create_task_from_string(self, task: str) -> Task:
        """Creates a task.
        """
        
        task = self.api.create_task(task)
        
        task.on_log_message += lambda message: log().info(message)
        task.on_finished += lambda message: log().info('Task finished')
        
        return task
    
    def run_task(self, task: Task) -> None:
        """Runs the task to completion.
        """
        
        self.task_updater.run(task)
    
    def get_task_by_id(self, task_id: str) -> Task:
        """Get a task, or update status of an existing task.
        """
        
        return self.api.get_task(task_id)
    
    def update_task(self, task: Task) -> Task:
        """Updates a task.
        """
        
        return self.api.get_task(task = task)
    
    def stop_task(self, task: Task) -> None:
        """Stops a task.
        """
        
        self.api.interrupt_task(task_id=task.id)