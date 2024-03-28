from pathlib import Path
from pydantic import BaseModel

from pyrdfrules.common.file.workspace import Workspace

class WorkspaceFile(BaseModel):
    """
    Represents a file in the workspace.
    """
    
    """
    Path relative to the workspace root.
    """
    path: str
    
    """
    Workspace the file is in.
    """
    workspace: Workspace
    
    def get_absolute_path(self) -> str:
        return ''