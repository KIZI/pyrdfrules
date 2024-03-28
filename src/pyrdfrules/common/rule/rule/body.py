from typing import List
from pydantic import BaseModel

class RuleBody(BaseModel):
    
    
    items: List[any]