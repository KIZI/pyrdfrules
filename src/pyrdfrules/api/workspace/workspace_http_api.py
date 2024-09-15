from pyrdfrules.api.http_api_urls import WORKSPACE_URL
from pyrdfrules.api.http_rdfrules_api_context import HTTPRDFRulesApiContext
from pyrdfrules.api.workspace.workspace_api import WorkspaceApi


class WorkspaceHttpApi(WorkspaceApi):
    
    context: HTTPRDFRulesApiContext
    
    def __init__(self, context: HTTPRDFRulesApiContext) -> None:
        super().__init__(context)
        pass
    
    async def get_all_files(self):
        
        response = self.context.get_http_client().get(WORKSPACE_URL)
        
        print(response.text)
        
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