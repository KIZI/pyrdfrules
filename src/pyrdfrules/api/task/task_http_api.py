import json
from typing import Awaitable
from pyrdfrules.api.http_api_urls import TASK_CREATE_URL
from pyrdfrules.api.http_rdfrules_api_context import HTTPRDFRulesApiContext
from pyrdfrules.api.rdfrules_api_context import RDFRulesApiContext
from pyrdfrules.api.task.task_api import TaskApi
from pyrdfrules.common.pipeline.pipeline import Pipeline
from pyrdfrules.common.task.task import Task


class TaskHttpApi(TaskApi):
    
    context: HTTPRDFRulesApiContext
    
    def __init__(self, context: HTTPRDFRulesApiContext) -> None:
        super().__init__(context)
        pass

    async def create_task(self, task: Pipeline|dict|str) -> Awaitable[Task]:
        """Creates a task.

        Args:
            task (Pipeline | dict | str): Task to create.

        Returns:
            Awaitable[Task]: Created task.
        """
        
        if isinstance(task, Pipeline):
            pass
        elif isinstance(task, dict):
            pass
        elif isinstance(task, str):
            task = json.loads(task)
            
        response = await self.context.get_http_client().post(
            TASK_CREATE_URL,
            json=task
        )
        
        print(response.json())
        
        pass
    
    async def get_task_status(self, task_id: str):
        """Get the status of a task.
        """
        pass
    
    async def interrupt_task(self, task_id: str):
        """Interrupt a task.
        """
        pass