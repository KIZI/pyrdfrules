from pyrdfrules.pipeline.pipeline_item import PipelineItem
from typing import List

from pyrdfrules.pipeline.transformation.entity.prefix import Prefix

class AddPrefixes(PipelineItem):
    """
    Add prefixes to datasets to shorten URIs.
    """
    
    """
    It is possible to load a file with prefixes in the Turtle (.ttl) format from the workspace on the server side (just click onto a file name), or you can load any remote prefix file from URL (see below).
    """
    file: str
    
    """
    URL: A URL to a remote file with prefixes in the Turtle (.ttl) format to be loaded. If this is specified then the workspace file is ommited.
    """
    url: str
    
    """
    Here, you can define your own prefixes manually.
    """
    prefixes: List[Prefix]