from pathlib import Path
from typing import List
from pydantic import BaseModel

from pyrdfrules.common.file.workspace_item import WorkspaceItem

class WorkspaceFile(WorkspaceItem):
    """Represents a file in the workspace.
    """
    
    name: str
    """Name of the workspace file.
    """
    
    size: int
    """Size of the file in bytes.
    """
    
    path: Path
    """Full path to the file.
    """
    