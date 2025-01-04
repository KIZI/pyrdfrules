from typing import Generator
from pyrdfrules.api.task.task_api import TaskApi
from pyrdfrules.common.logging.logger import log
from pyrdfrules.common.task.task import Task
from pyrdfrules.common.task.task_updater import TaskUpdater
from pyrdfrules.config import Config
from pyrdfrules.rdfrules.pipeline import Pipeline


class TaskRunner():
    """
    The TaskRunner class is responsible for running tasks on the RDFRules engine.
    """
    
    api: TaskApi
    
    task_updater: TaskUpdater
    
    config: Config
    
    def __init__(self, api: TaskApi, config: Config) -> None:
        self.api = api
        self.task_updater = TaskUpdater(api, config)
        self.config = config
        
        pass
    
    def create_task(self, pipeline: Pipeline) -> Task:
        """Creates a task.
        """
        
        task = self.api.create_task(pipeline)
        
        self.add_task_log_message_listener(task)
        
        return task
    
    def add_task_log_message_listener(self, task: Task) -> None:
        """Adds a listener to the task log messages.
        """
        
        task.on_log_message += lambda message: log().info(message)
        task.on_finished += lambda message: log().info('Task finished')
        
    
    def create_task_from_string(self, task: str) -> Task:
        """Creates a task.
        """
        
        task = self.api.create_task(task)
        
        self.add_task_log_message_listener(task)
        
        return task
    
    def run_task(self, task: Task) -> Generator[Task, None, None]:
        """Runs a task step.
        """
        
        yield from self.task_updater.run(task)
    
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
        
        self.task_updater.stop(task)