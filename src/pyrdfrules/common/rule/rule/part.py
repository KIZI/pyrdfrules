from typing import List
from pydantic import BaseModel

class RulePart(BaseModel):
        
    graphs: List[dict]
    
    subject: dict
    
    predicate: dict
    
    object: dict