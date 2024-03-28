from typing import Annotated, Optional

from annotated_types import Gt, Le
from pyrdfrules.pipeline.pipeline_item import PipelineItem

class PCAConfidence(PipelineItem):
    """
    A minimal PCA (Partial Completeness Assumption) confidence threshold.
    """
    
    """
    This operation counts the PCA confidence for all rules and filter them by this minimal threshold. The value range is between 0.001 and 1 included. Default value is set to 0.5.
    """
    min_confidence: Annotated[float, Gt(0.001), Le(1)]
    
    """
    Get top-k rules with highest confidence.
    """
    top_k: Optional[int]