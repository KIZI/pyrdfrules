from typing import Awaitable
from pyrdfrules.api.rdfrules_api_context import RDFRulesApiContext
from pyrdfrules.common.pipeline.pipeline import Pipeline
from pyrdfrules.common.task.task import Task


class TaskApi():
    
    context: RDFRulesApiContext
    
    def __init__(self, context: RDFRulesApiContext) -> None:
        self.context = context
        pass
    
    async def create_task(self, task: Pipeline|dict|str) -> Awaitable[Task]:
        """Creates a task.

        Args:
            task (Pipeline | dict | str): Task to create.

        Returns:
            Awaitable[Task]: Created task.
        """
        
        pass
    
    async def get_task_status(self, task_id: str):
        """Get the status of a task.
        """
        pass
    
    async def interrupt_task(self, task_id: str):
        """Interrupt a task.
        """
        pass