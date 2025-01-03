from pydantic import BaseModel


class Subject(BaseModel):
    
    type: str
    
    value: str