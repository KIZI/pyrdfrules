from pathlib import Path

from pyrdfrules.api.workspace.workspace_api import WorkspaceApi
from pyrdfrules.common.file.workspace_tree import WorkspaceTree

class Workspace():
    """
    Path in which RDFRules can find datasets and store results.
    """
    
    api: WorkspaceApi
    
    def __init__(self, api: WorkspaceApi) -> None:
        self.api = api
        pass
    
    async def get_files(self) -> WorkspaceTree:
        """Returns a list of all files in the workspace.

        Returns:
            WorkspaceTree: List of workspace files.
        """
        
        tree = WorkspaceTree()
        tree.create_from_dict(await self.api.get_all_files())
        
        return tree