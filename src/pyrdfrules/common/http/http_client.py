from requests import Response, Session

from pyrdfrules.common.http.url import Url
from pyrdfrules.common.logging.logger import log
from pyrdfrules.config import Config

class HttpClient():
    
    session: Session
    base_url: str
    config: Config
    
    def __init__(self, config: Config) -> None:
        self.session = Session()
        self.base_url = None
        self.config = config
        
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
    
    def get(self, url: str | Url) -> Response:
        """Sends a GET request.

        Args:
            url (str|Url): URL to send the request to.

        Returns:
            Response: Response object.
        """
        
        url = self.base_url + str(url)
        
        log().debug("GET %s", url)
        
        return self.session.get(url)

    def post(self, url: str | Url, **kwargs) -> Response:
        """Sends a POST request.

        Args:
            url (str|Url): URL to send the request to.

        Returns:
            Response: Response object.
        """
        
        url = self.base_url + str(url)
        
        log().debug("POST %s", url)
        
        return self.session.post(url, **kwargs)
    
    def delete(self, url: str | Url) -> Response:
        """Sends a DELETE request.

        Args:
            url (str|Url): URL to send the request to.

        Returns:
            Response: Response object.
        """
        
        url = self.base_url + str(url)
        
        log().debug("DELETE %s", url)
        
        return self.session.delete(url)