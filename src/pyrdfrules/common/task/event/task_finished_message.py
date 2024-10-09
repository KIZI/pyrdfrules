
import datetime
from pydantic import BaseModel
from pyrdfrules.common.event.event_dispatcher import EventDispatcher

class TaskFinishedMessage(BaseModel):

    id: str

    time_start: datetime.datetime
    
    time_end: datetime.datetime