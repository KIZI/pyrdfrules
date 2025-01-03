from pydantic import BaseModel


class Object(BaseModel):
    
    type: str
    
    value: str