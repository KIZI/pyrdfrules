from typing import Awaitable
from pydantic_core import Url
from requests import Response, Session

class HttpClient():
    
    session: Session
    base_url: str
    
    def __init__(self) -> None:
        self.session = Session()
        self.base_url = None
        
    def get_session(self) -> Session:
        """Gets the session object. Use this method to set global configuration, including timeouts.

        Returns:
            Session: Global session object.
        """
        return self.session
    
    def set_base_url(self, url: str | Url) -> None:
        """Sets the base URL for the HTTP client.

        Args:
            url (str|Url): Base URL.
        """
        
        # TODO normalize URL
        
        self.base_url = str(url)
    
    async def get(self, url: str | Url) -> Awaitable[Response]:
        """Sends a GET request.

        Args:
            url (str|Url): URL to send the request to.

        Returns:
            Response: Response object.
        """
        
        url = self.base_url + str(url)
        
        print("GET", url)
        
        return self.session.get(url)

    async def post(self, url: str | Url, **kwargs) -> Awaitable[Response]:
        """Sends a POST request.

        Args:
            url (str|Url): URL to send the request to.

        Returns:
            Response: Response object.
        """
        
        url = self.base_url + str(url)
        
        print("POST", url)
        
        return self.session.post(url, **kwargs)