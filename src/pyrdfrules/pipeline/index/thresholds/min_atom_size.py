from pyrdfrules.pipeline.index.thresholds.threshold import Threshold

class MinAtomSize(Threshold):
    """
    MinAtomSize.
    """
    
    """
    If negative value, the minimal atom size is same as the current minimal support threshold.
    """
    value: float