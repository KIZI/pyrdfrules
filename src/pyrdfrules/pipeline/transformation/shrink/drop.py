from pyrdfrules.pipeline.transformation.shrink.strategy import Strategy


class Drop(Strategy):
    """
    Drops first N records.

    Args:
        drop: number of records to drop.
    """
    
    """
    Number of records to drop.
    """
    drop: int