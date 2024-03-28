from annotated_types import Gt
from typing import Annotated

from pyrdfrules.pipeline.index.thresholds.threshold import Threshold

class MaxRuleLength(Threshold):
    """
    MaxRuleLength
    """
    
    """
    The minimal value is 1.
    """
    value: Annotated[float, Gt(1)]