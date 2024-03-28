from pydantic_core import Url

from pyrdfrules.common.graph.graph import Graph

class RemoteGraph(Graph):
    
    """
    A URL to a remote file to be loaded. If this is specified then the workspace file is ommited.
    """
    url: Url