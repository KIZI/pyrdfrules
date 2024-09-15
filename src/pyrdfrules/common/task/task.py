import datetime
from pydantic import BaseModel


class Task(BaseModel):
    
    id: str
    """UUID of the task.
    """
    
    started: datetime.datetime
    """Time when the task was started.
    """