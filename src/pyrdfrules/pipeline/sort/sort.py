from pyrdfrules.pipeline.pipeline_item import PipelineItem
from typing import List

from pyrdfrules.pipeline.sort.measure.sort_measure import SortMeasure
from pyrdfrules.pipeline.transformation.entity.prefix import Prefix

class Sort(PipelineItem):
    """
    Sort predicted triples by their rules.
    """
    
    """
    Here, you can define your own prefixes manually.
    """
    sort_by: List[SortMeasure]