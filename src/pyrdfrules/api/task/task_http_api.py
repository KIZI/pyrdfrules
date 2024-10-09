from datetime import datetime
import json
from typing import Awaitable
from pyrdfrules.api.http_api_urls import TASK_CREATE_URL, TASK_READ_URL
from pyrdfrules.api.http_rdfrules_api_context import HTTPRDFRulesApiContext
from pyrdfrules.api.rdfrules_api_context import RDFRulesApiContext
from pyrdfrules.api.task.exception.task_not_found_exception import TaskNotFoundException
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
        
        data = response.json()
        
        print(data)
        
        return Task(
            id=data['id'],
            started=datetime.fromisoformat(data['started']),
            api=self
        )
    
    async def get_task(self, task_id: str = None, task: Task = None) -> Awaitable[Task]:
        await super().get_task(task_id, task)
        
        task_id = task_id or task.id
        
        data = await self.get_task_response(task_id)
        
        return Task(
            id=data['id'],
            started=datetime.fromisoformat(data['started']),
            api=self
        )
        
    async def get_task_response(self, task_id: str) -> Awaitable[dict]:
        response = await self.context.get_http_client().get(
            TASK_READ_URL.format(task_id = task_id)
        )
        
        print(response.status_code)
        
        # response codes - 202 - in progress
        # response codes - 200 - finished
        
        if response.status_code >= 400:
            raise TaskNotFoundException(task_id)
        
        return response.json()
    
    async def interrupt_task(self, task_id: str):
        """Interrupt a task.
        """
        pass