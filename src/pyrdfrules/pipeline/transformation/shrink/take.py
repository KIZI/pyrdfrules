from pyrdfrules.pipeline.transformation.shrink.strategy import Strategy


class Take(Strategy):
    """
    Takes first N records.

    Args:
        take: number of records to take.
    """
    
    """
    Number of records to take.
    """
    take: int