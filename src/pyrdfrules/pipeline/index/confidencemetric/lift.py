from typing import Annotated, Optional

from annotated_types import Gt, Le
from pyrdfrules.pipeline.pipeline_item import PipelineItem

class Lift(PipelineItem):
    """
    A minimal confidence threshold. This operation first counts the standard confidence for all rules and filter them by this minimal threshold, then it counts the lift measure by the computed cofindence. The value range is between 0.001 and 1 included. Default value is set to 0.5.
    """