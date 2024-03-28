from pyrdfrules.pipeline.pipeline_item import PipelineItem
from typing import List

from pyrdfrules.pipeline.transformation.shrink.strategy import Strategy

class Shrink(PipelineItem):
    """Shrink the dataset (set of quads) with a specified window.

    Args:
        strategy (Strategy): Shrink strategy to use.
    """
    strategy: Strategy