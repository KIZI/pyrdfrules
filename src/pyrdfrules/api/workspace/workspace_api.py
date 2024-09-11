from pyrdfrules.api.rdfrules_api_context import RDFRulesApiContext


class WorkspaceApi():
    
    context: RDFRulesApiContext
    
    def __init__(self, context: RDFRulesApiContext) -> None:
        self.context = context
        pass
    
    async def get_all_files(self):
        """Get all files and directories recursively from the workspace directory.
        """
        pass
    
    async def get_file(self, path: str):
        """Get the file content.
        """
        pass
    
    async def delete_file(self, path: str):
        """Delete a file.
        """
        pass
    
    async def upload_file(self, path: str, content: bytes):
        """Upload a file.
        """
        pass