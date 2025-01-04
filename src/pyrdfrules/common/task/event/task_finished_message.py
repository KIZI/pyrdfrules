
import datetime
from pydantic import BaseModel

class TaskFinishedMessage(BaseModel):
    """Message sent when a task has finished.
    """

    id: str
    """
    ID of the task.
    """

    time_start: datetime.datetime
    """
    Time when the task started.
    """
    
    time_end: datetime.datetime
    """
    Time when the task ended.
    """