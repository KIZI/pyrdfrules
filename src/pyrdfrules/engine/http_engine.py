from pyrdfrules.common.http.url import Url
from pyrdfrules.api.http_rdfrules_api import HTTPRDFRulesApi
from pyrdfrules.api.rdfrules_api import RDFRulesApi
from pyrdfrules.engine.engine import Engine, ensure_started

class HttpEngine(Engine):
    """
    Represents a remote RDFRules instance running at a specific URL.
    """
    
    api: HTTPRDFRulesApi
    
    def check(self) -> None:
        """Returns without an exception if the instance is still running.
        """
        
        self.api.workspace.get_all_files()
        
        pass