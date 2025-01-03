from typing import Optional
from pydantic import BaseModel


class Predicate(BaseModel):
    
    localName: str
    
    nameSpace: str
    
    prefix: Optional[str]