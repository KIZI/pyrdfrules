from typing import List
from pyrdfrules.pipeline.pipeline_item import PipelineItem
from pydantic import BaseModel

class Pipeline(BaseModel):
    """Creates a new RDFRules pipeline. This object holds the individual steps and their parameters and is serialized according to the RDFRules JSON interface.

    Args:
        items: List[PipelineItem] a list of pipeline operations to conduct.
    """
    
    """
    Sequentially defined pipeline items.
    """
    items: List[PipelineItem]
    
    def serialize(self) -> str:
        """
        Returns a JSON serialized string for the RDFRules HTTP api.

        Returns:
            str: JSON representation of the pipeline.
        """
        return ""
    
    
    # todo - frozen flag? to preventr modifications while pipeline is running?
    # check pipeline validity