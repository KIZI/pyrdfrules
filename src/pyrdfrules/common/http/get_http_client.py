from pydantic_core import Url
from pyrdfrules.common.http.http_client import HttpClient

__http_client: HttpClient = None

def get_http_client_instance(url: Url) -> HttpClient:
    """Gets the HTTP client.

    Returns:
        HttpClient: HTTP client.
    """
    
    global __http_client
    
    if __http_client is None:
        __http_client = HttpClient()
    
    __http_client.set_base_url(url)
        
    return __http_client