from pyrdfrules.pipeline.index.thresholds.threshold import Threshold
from annotated_types import Gt, Le
from typing import Annotated

class MinHeadCoverage(Threshold):
    """
    MinHeadCoverage
    """
    
    """
    The minimal value is 0.001 and maximal value is 1.
    """
    value: Annotated[float, Gt(0.001), Le(1)]