from pyrdfrules.pipeline.exception.invalid_pipeline_item import InvalidPipelineItem
from pydantic import BaseModel

class PipelineItem(BaseModel):
    """
    Base class interface providing common APIs for pipeline items.
    """
    
    def json(self) -> str:
        """
        Serializes a pipeline item to JSON.
        
        Parameters
        ----------
        
        Returns
        -------
        json (str): A JSON representation of the arbitrary pipeline item.
        
        Raises
        ------
        InvalidPipelineItem: If the pipeline item is not defined in this library, this error will be raised.
        
        """
        raise InvalidPipelineItem()