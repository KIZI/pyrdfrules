from typing import List
from pydantic import BaseModel

from pyrdfrules.common.graph.graph import Graph

class RulePart(BaseModel):
        
    graphs: List[Graph]
    
    subject: any
    
    predicate: any
    
    object: any