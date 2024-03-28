from pathlib import Path
from pydantic import BaseModel

from pyrdfrules.common.file.workspace_file import WorkspaceFile

class Workspace(BaseModel):
    """
    Path in which RDFRules can find datasets and store results.
    """
    
    """
    Base path to the workspace root directory.
    """
    base_path: Path
    
    def open(self, path: str) -> WorkspaceFile:
        """Creates a file reference if the specified path exists.

        Args:
            path (str): Relative path from the workspace root.

        Returns:
            WorkspaceFile: Workspace file abstraction.
        """
        
        # todo - check if the file exists
        return WorkspaceFile(path, self)