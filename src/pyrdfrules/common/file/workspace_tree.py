from pathlib import Path
from typing import List
from pydantic import BaseModel

from pyrdfrules.common.file.workspace_directory import WorkspaceDirectory
from pyrdfrules.common.file.workspace_file import WorkspaceFile

class WorkspaceTree(BaseModel):
    """
    The WorkspaceTree class represents the structure of the workspace directory, including files and subdirectories.
    """
        
    root: WorkspaceDirectory|None = None
    
    def create_from_dict(self, data: dict) -> None:
        """Creates a workspace tree from a dictionary response.
        
        Args:
            data (dict): Dictionary with workspace items.
        """
        
        def create_folder(subdata: dict, base_path: Path) -> WorkspaceDirectory:

            directory = WorkspaceDirectory(
                name=subdata['name'],
                path=base_path,
                size=0,
                writable=subdata['writable']
            )
            
            if 'subfiles' in subdata:
                for file in subdata['subfiles']:
                    if "subfiles" in file:
                        directory.add(
                            create_folder(file, base_path / Path(file['name']))
                        )
                    else:
                        directory.add(
                            WorkspaceFile(
                                name=file['name'],
                                path=base_path / Path(file['name']),
                                size=file['size']
                            )
                        )
            
            return directory
        
        
        self.root = create_folder(data, Path('/'))
        pass
    
    
    def get_root(self) -> WorkspaceDirectory:
        """Returns the root directory of the workspace tree.
        
        Returns:
            WorkspaceDirectory: Root directory.
        """
        
        return self.root