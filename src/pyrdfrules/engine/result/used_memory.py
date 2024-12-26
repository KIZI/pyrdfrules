from pydantic import BaseModel

class UsedMemory(BaseModel):
    """
    Represents used memory of the RDFRules instance.
    """
    
    """
    Currently used memory in bytes.
    """
    used: int
    
    """
    Total memory in bytes.
    """
    total: int
    