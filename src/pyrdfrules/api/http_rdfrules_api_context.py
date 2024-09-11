from pydantic import BaseModel
from pydantic_core import Url

from pyrdfrules.api.rdfrules_api_context import RDFRulesApiContext


class HTTPRDFRulesApiContext(RDFRulesApiContext):
    
    url: Url
    """URL of the RDFRules API server.
    """