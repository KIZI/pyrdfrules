from pyrdfrules.api.http_api_urls import WORKSPACE_URL
from pyrdfrules.api.http_rdfrules_api_context import HTTPRDFRulesApiContext
from pyrdfrules.api.workspace.exception.workspace_file_not_found_exception import WorkspaceFileNotFoundException
from pyrdfrules.api.workspace.workspace_api import WorkspaceApi


class WorkspaceHttpApi(WorkspaceApi):
    
    context: HTTPRDFRulesApiContext
    
    def __init__(self, context: HTTPRDFRulesApiContext) -> None:
        super().__init__(context)
        pass
    
    def get_all_files(self) -> dict:
        """Get all files and directories recursively from the workspace directory.
        """
        
        response = self.context.get_http_client().get(WORKSPACE_URL)
        
        return response.json()
    
    def get_file(self, path: str) -> bytes:
        """Get the file content.
        """
        
        response = self.context.get_http_client().get(WORKSPACE_URL + path)
        
        if response.status_code == 404:
            raise WorkspaceFileNotFoundException(path)
        
        return response.content
    
    def delete_file(self, path: str) -> None:
        """Delete a file.
        """
        
        response = self.context.get_http_client().delete(WORKSPACE_URL + path)
        
        if response.status_code == 404:
            raise WorkspaceFileNotFoundException(path)
        
        pass
    
    def upload_file(self, path: str, content: bytes):
        """Upload a file.
        """
        
        if path == '/':
            raise Exception('Cannot upload to root directory')
        
        if path.endswith('/'):
            raise Exception('Cannot upload to a directory')
        
        response = self.context.get_http_client().post(
            WORKSPACE_URL + path,
            data=content
        )
        
        return response.json()