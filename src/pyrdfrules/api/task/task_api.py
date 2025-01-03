from pyrdfrules.api.rdfrules_api_context import RDFRulesApiContext
from pyrdfrules.common.task.task import Task
from pyrdfrules.rdfrules.pipeline import Pipeline


class TaskApi():
    
    context: RDFRulesApiContext
    
    def __init__(self, context: RDFRulesApiContext) -> None:
        self.context = context
        pass
    
    def create_task(self, task: Pipeline|dict|str) -> Task:
        """Creates a task.

        Args:
            task (Pipeline | dict | str): Task to create.

        Returns:
            Task: Created task.
        """
        
        pass
    
    def get_task(self, task_id: str = None, task: Task = None) -> Task:
        """Get a task, or update status of an existing task.

        Args:
            task_id (str, optional): ID of the task. Defaults to None.
            task (Task, optional): Task object. Defaults to None.

        Raises:
            ValueError: If task_id or task is not provided.

        Returns:
            Task: Retrieved task.
        """
        
        if task_id is None and task is None:
            raise ValueError('task_id or task must be provided')
        
        pass
    
    def interrupt_task(self, task_id: str):
        """Interrupt a task.
        """
        pass