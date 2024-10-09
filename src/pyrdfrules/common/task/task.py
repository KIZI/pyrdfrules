import datetime
from typing import Awaitable
from pydantic import BaseModel

class Task(BaseModel):
    
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
    
    # TODO add events
    
    def is_finished(self) -> bool:
        """Checks if the task is finished.
        """
        
        return self.status == 'finished'
    
    def update_from_dict(self, data: dict) -> None:
        """Updates the task from a dictionary.
        """
        
        self.logs = data['logs']
        
        if "finished" in data:
            self.status = 'finished'
            self.finished = datetime.datetime.fromisoformat(data['finished'])
            
        if "result" in data:
            self.result = data['result']
        
        self.last_updated = datetime.datetime.now()