from pathlib import Path
from pydantic import BaseModel

class WorkspaceItem(BaseModel):
    """Represents a directory in the workspace.
    """
    
    name: str
    """Name of the workspace diretory.
    """
    
    path: Path
    """Full path to the file.
    """