
import datetime
from pydantic import BaseModel

class TaskLogMessage(BaseModel):
    """Log message for a task.
    """
    
    id: str
    """Task ID.
    """
    
    message: str
    """Log message.
    """
    
    time: datetime.datetime
    """Time when the message was logged.
    """