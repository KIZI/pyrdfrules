from typing import Annotated, Dict, List, Literal, Tuple
from pyrdfrules.pipeline.pipeline_item import PipelineItem

class Prefix(PipelineItem):

    """
    A short name for the namespace.
    """
    prefix: str  
    
    """
    A namespace URI to be shortened. It should end with the slash or hash symbol, e.g., http://dbpedia.org/property/.
    """
    namespace: str