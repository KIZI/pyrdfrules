from typing import Awaitable
from pydantic_core import Url
from pyrdfrules.api.http_rdfrules_api import HTTPRDFRulesApi
from pyrdfrules.api.rdfrules_api import RDFRulesApi
from pyrdfrules.engine.engine import Engine, ensure_started

class HttpEngine(Engine):
    """
    Represents a remote RDFRules instance running at a specific URL.
    """
    
    api: HTTPRDFRulesApi
    
    async def check(self) -> Awaitable:
        """Returns without an exception if the instance is still running.

        Returns:
            Awaitable: Non-blocking future.
        """
        
        await self.api.workspace.get_all_files()
        
        pass