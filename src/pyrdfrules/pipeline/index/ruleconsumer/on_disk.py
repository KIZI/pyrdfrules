from pyrdfrules.pipeline.index.ruleconsumer.ruleconsumer import RuleConsumer
from pyrdfrules.pipeline.pipeline_item import PipelineItem
from annotated_types import Gt
from typing import Annotated, Literal

class OnDisk(RuleConsumer):
    """
    All mined rules are gradually saving on disk instead of memory.
    """
    
    """
    A relative path to a file where the rules will be continuously saved in a pretty printed format.
    """
    export_path: str
    
    """
    Export rules format. Available types are text and (streaming) ndjson.
    """
    export_format: Literal['text', 'ndjson']