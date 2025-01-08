from pathlib import Path

from pyrdfrules.api.workspace.workspace_api import WorkspaceApi
from pyrdfrules.common.file.workspace_tree import WorkspaceTree
from pyrdfrules.common.logging.logger import log

class Workspace():
    """
    The Workspace class provides methods to interact with the RDFRules workspace, including file management.
    """
    
    api: WorkspaceApi
    
    def __init__(self, api: WorkspaceApi) -> None:
        self.api = api
        pass
    
    def get_files(self) -> WorkspaceTree:
        """Returns a list of all files in the workspace.

        Returns:
            WorkspaceTree: List of workspace files.
        """
        
        log().debug("Getting files from workspace")
        
        tree = WorkspaceTree()
        tree.create_from_dict(self.api.get_all_files())
        
        return tree
    
    def upload_file(self, path: Path | str, file) -> None:
        """Uploads a file to the workspace.

        Args:
            path (Path): Path to the file to upload.
        """
        
        log().debug(f"Uploading file {path}")
        
        self.api.upload_file(str(path), file)
        
    def download_file(self, path: Path | str) -> str:
        """Downloads a file from the workspace.

        Args:
            path (Path): Path to the file to download.

        Returns:
            str: File contents.
        """
        
        return self.api.get_file(str(path))
    
    def delete_file(self, path: Path | str) -> None:
        """Deletes a file from the workspace.

        Args:
            path (Path): Path to the file to delete.
        """
        
        log().debug(f"Deleting file {path}")
        
        self.api.delete_file(str(path))