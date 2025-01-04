from pydantic import BaseModel
from pyrdfrules.common.http.url import Url

from pyrdfrules.api.rdfrules_api_context import RDFRulesApiContext
from pyrdfrules.common.http.get_http_client import get_http_client_instance
from pyrdfrules.common.http.http_client import HttpClient
from pyrdfrules.config import Config

class HTTPRDFRulesApiContext(RDFRulesApiContext):
    """
    Context class for the RDFRules API, passed around for HTTP API clients.
    """
    
    url: Url
    """URL of the RDFRules API server.
    """
    
    client: HttpClient
    """HTTP client instance.
    """
    
    config: Config
    """Configuration.
    """
    
    def __init__(self, url: Url, config: Config) -> None:
        super().__init__()
        self.url = url
        self.client = get_http_client_instance(
            url,
            config
        )
        
    def get_url(self) -> Url:
        """Gets the URL of the RDFRules API server.
        
        Returns:
            Url: URL of the RDFRules API server.
        """
        return self.url
    
    def get_http_client(self) -> HttpClient:
        """Gets the HTTP client instance.

        Returns:
            HttpClient: HTTP client instance.
        """
        return self.client