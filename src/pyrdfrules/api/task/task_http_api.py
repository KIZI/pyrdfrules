from datetime import datetime
import json
from pyrdfrules.api.http_api_urls import TASK_CREATE_URL, TASK_READ_URL, TASK_INTERRUPT_URL
from pyrdfrules.api.http_rdfrules_api_context import HTTPRDFRulesApiContext
from pyrdfrules.api.rdfrules_api_context import RDFRulesApiContext
from pyrdfrules.api.task.exception.task_not_found_exception import TaskNotFoundException
from pyrdfrules.api.task.task_api import TaskApi
from pyrdfrules.common.logging.logger import log
from pyrdfrules.common.task.task import Task
from pyrdfrules.rdfrules.pipeline import Pipeline


class TaskHttpApi(TaskApi):
    
    __doc__ = TaskApi.__doc__
    
    context: HTTPRDFRulesApiContext
    
    def __init__(self, context: HTTPRDFRulesApiContext) -> None:
        super().__init__(context)
        pass

    def create_task(self, task: Pipeline|dict|str) -> Task:
        """Creates a task.

        Args:
            task (Pipeline | dict | str): Task to create.

        Returns:
            Task: Created task.
        """
        
        if isinstance(task, Pipeline):
            task = task.model_dump()
            pass
        elif isinstance(task, dict):
            pass
        elif isinstance(task, str):
            task = json.loads(task)
            
        response = self.context.get_http_client().post(
            TASK_CREATE_URL,
            json=task
        )
        
        data = response.json()
        
        log().debug(data)
        
        return Task(
            id=data['id'],
            started=datetime.fromisoformat(data['started'])
        )
    
    def get_task(self, task_id: str = None, task: Task = None) -> Task:
        super().get_task(task_id, task)
        
        task_id = task_id or task.id
        
        data = self.get_task_response(task_id)
        
        log().debug(data)
        
        return Task(
            id=data['id'],
            started=datetime.fromisoformat(data['started'])
        )
        
    def get_task_response(self, task_id: str) -> dict:
        response = self.context.get_http_client().get(
            TASK_READ_URL.format(task_id = task_id)
        )
        
        # response codes - 202 - in progress
        # response codes - 200 - finished
        
        if response.status_code >= 400:
            log().error(response.text)
            raise TaskNotFoundException(task_id)
        
        result = response.json()
        
        log().debug(result)
        
        return result
    
    def interrupt_task(self, task_id: str) -> dict:
        """Interrupt a task.
        """
        
        response = self.context.get_http_client().delete(
            TASK_INTERRUPT_URL.format(task_id = task_id)
        )
        
        if response.status_code != 202:
            log().error(response.text)
            raise TaskNotFoundException(task_id)
        
        log().debug(response.text)
        
        return response.json()