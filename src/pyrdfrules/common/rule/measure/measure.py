from pydantic import BaseModel

class RuleMeasure(BaseModel):
    
    name: str
    
    value: float