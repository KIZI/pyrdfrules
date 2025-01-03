from typing import List
from pydantic import BaseModel

class RuleBody(BaseModel):
    graphs: str
    
    object: str
    
    items: List[dict]