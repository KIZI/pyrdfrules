from pyrdfrules.pipeline.transformation.shrink.strategy import Strategy


class Drop(Strategy):
    """
    Takes a subset (window) of n to m records.

    Args:
        start: start of the window.
        end: end of the window.
    """
    
    """
    First index of the window.
    """
    start: int
    
    """
    Last index of the window.
    """
    end: int