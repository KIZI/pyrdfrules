from pyrdfrules.pipeline.pipeline_item import PipelineItem

class SortMeasure(PipelineItem):
    """
    Base SortMeasuer class.
    """
    
    """
    Sort in reverse order.
    """
    reversed: bool = False