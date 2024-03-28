from pydantic_core import Url
from pyrdfrules.engine.engine import Engine

class HttpEngine(Engine):
    """
    Represents a remote RDFRules instance running at a specific URL.
    """
    
    """
    URL of the instance.
    """
    url: Url