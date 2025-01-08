from pyrdfrules.api.http_api_urls import WORKSPACE_URL
from pyrdfrules.api.http_rdfrules_api_context import HTTPRDFRulesApiContext
from pyrdfrules.api.workspace.exception.workspace_file_not_found_exception import WorkspaceFileNotFoundException
from pyrdfrules.api.workspace.workspace_api import WorkspaceApi
from pyrdfrules.common.logging.logger import log


class WorkspaceHttpApi(WorkspaceApi):
    
    __doc__ = WorkspaceApi.__doc__
    
    context: HTTPRDFRulesApiContext
    
    def __init__(self, context: HTTPRDFRulesApiContext) -> None:
        super().__init__(context)
        pass
    
    def normalize_path(self, path: str) -> str:
        """Normalize the path.
        """
        
        if not path.startswith('/'):
            path = '/' + path
        
        return path
    
    def get_all_files(self) -> dict:
        """Get all files and directories recursively from the workspace directory.
        """
        
        response = self.context.get_http_client().get(WORKSPACE_URL)
        
        log().info(response.request.url)
        log().info(response.request.headers)
        log().info(response.request.body)
        
        log().info(response.status_code)
        log().info(response.request.headers)
        log().info(response.text)        
        return response.json()
    
    def get_file(self, path: str) -> bytes:
        """Get the file content.
        """
        
        response = self.context.get_http_client().get(WORKSPACE_URL + self.normalize_path(path))
        
        if response.status_code == 404:
            raise WorkspaceFileNotFoundException(path)
        
        return response.content
    
    def delete_file(self, path: str) -> None:
        """Delete a file.
        """
        
        response = self.context.get_http_client().delete(WORKSPACE_URL + self.normalize_path(path))
        
        if response.status_code == 404:
            raise WorkspaceFileNotFoundException(path)
        
        pass
    
    def upload_file(self, path: str, file: bytes):
        """Upload a file.
        """
        
        if path == '/':
            raise Exception('Cannot upload to root directory')
        
        if path.endswith('/'):
            raise Exception('Cannot upload to a directory')
        
        name = path.split('/')[-1]
        directory = path[:-(len(name) + 1)]
                
        response = self.context.get_http_client().post(
            WORKSPACE_URL + self.normalize_path(path),
            data={"directory": directory},
            files={"file": file},
        )
        
        print(response.request.headers)
        print(response.request.body)
        print(response.request.url)
        print(response.text)
        
        if response.status_code not in [200, 201]:
            raise WorkspaceFileNotFoundException(path)
        
        if response.text != "uploaded":
            raise Exception("Upload failed")

        return