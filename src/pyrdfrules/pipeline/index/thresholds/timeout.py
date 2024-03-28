from pyrdfrules.pipeline.index.thresholds.threshold import Threshold
from annotated_types import Gt
from typing import Annotated

class Timeout(Threshold):
    """
    Timeout.
    """
    
    """
    The minimal value is 1.
    """
    value: Annotated[float, Gt(1)]