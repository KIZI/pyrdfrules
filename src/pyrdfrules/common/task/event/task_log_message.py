
import datetime
from pydantic import BaseModel
from pyrdfrules.common.event.event_dispatcher import EventDispatcher

class TaskLogMessage(BaseModel):
    
    id: str
    
    message: str
    
    time: datetime.datetime