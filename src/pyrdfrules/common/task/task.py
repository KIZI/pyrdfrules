import datetime

from pyrdfrules.common.event.event_dispatcher import EventDispatcher
from pyrdfrules.common.result.result import Result
from pyrdfrules.common.task.event.task_finished_message import TaskFinishedMessage
from pyrdfrules.common.task.event.task_log_message import TaskLogMessage

class Task():
    
    id: str
    """UUID of the task.
    """
    
    started: datetime.datetime
    """Time when the task was started.
    """
    
    finished: datetime.datetime = None
    """Time when the task was finished.
    """
    
    last_updated: datetime.datetime = None
    """Time when the task was last updated.
    """
    
    logs: list[str] = []
    """Logs of the task.
    """
    
    status: str = 'running'
    """Status of the task.
    """
    
    result: dict = {}
    """Result of the task.
    """
    
    on_log_message: EventDispatcher = EventDispatcher()
    
    on_finished: EventDispatcher = EventDispatcher()
    
    def __init__(self, id: str, started: datetime.datetime) -> None:
        self.id = id
        self.started = started
        pass
    
    def is_finished(self) -> bool:
        """Checks if the task is finished.
        """
        
        return self.status == 'finished' or self.status == 'stopped'
    
    def update_from_dict(self, data: dict) -> None:
        """Updates the task from a dictionary.
        """
        
        if "logs" in data:
            for log in data['logs']:
                self.on_log_message.dispatch(
                    TaskLogMessage(
                        id=self.id,
                        message=log["message"],
                        time=datetime.datetime.fromisoformat(log["time"])
                    )
                )
        
            self.logs = data['logs']
        
        if "finished" in data:
            self.status = 'finished'
            self.finished = datetime.datetime.fromisoformat(data['finished'])
            
            self.on_finished.dispatch(
                TaskFinishedMessage(
                    id=self.id,
                    time_start=self.started,
                    time_end=self.finished
                )
            )
            
        if "result" in data:
            self.result = data['result']
        
        self.last_updated = datetime.datetime.now()
        
    def get_result(self) -> Result:
        """Returns formatted result of the task.

        Returns:
            Result: Result of the task.
        """
        
        if not self.is_finished():
            raise Exception("Task is not finished yet.")
        
        return Result(self.result)
        
    def _stop(self) -> None:
        """Stops the task.
        """
        
        self.status = 'stopped'
        pass