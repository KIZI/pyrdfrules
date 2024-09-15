from pathlib import Path
from typing import Optional

from pyrdfrules.common.file.workspace_item import WorkspaceItem

class WorkspaceDirectory(WorkspaceItem):
    """Represents a directory in the workspace.
    """
    
    name: str
    """Name of the workspace diretory.
    """
    
    size: int
    """Size of the directory in bytes.
    """
    
    path: Optional[Path]
    """Full path to the file.
    """
    
    writable: bool
    """If the file is writable.
    """
    
    files: list[WorkspaceItem] = []
    
    def add(self, item: WorkspaceItem) -> None:
        """Adds a file or directory to the directory.
        
        Args:
            item (WorkspaceItem): File or directory to add.
        """
        
        self.files.append(item)
        pass
    