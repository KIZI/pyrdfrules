from typing import List
from pyrdfrules.pipeline.pipeline_item import PipelineItem
from pydantic import BaseModel

class Pipeline(BaseModel):
    """Creates a new RDFRules pipeline. This object holds the individual steps and their parameters and is serialized according to the RDFRules JSON interface.

    Args:
        items: List[PipelineItem] a list of pipeline operations to conduct.
    """
    
    items: List[PipelineItem]