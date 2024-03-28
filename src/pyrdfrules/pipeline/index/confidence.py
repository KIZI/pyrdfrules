from pyrdfrules.pipeline.index.confidencemetric.confidence_metric import ConfidenceMetric
from pyrdfrules.pipeline.pipeline_item import PipelineItem


class ComputeConfidence(PipelineItem):
    """
    Computes confidence.
    """
    
    confidence_metric: ConfidenceMetric