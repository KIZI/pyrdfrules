from pyrdfrules.pipeline.index.ruleconsumer.ruleconsumer import RuleConsumer
from pyrdfrules.pipeline.pipeline_item import PipelineItem
from annotated_types import Gt
from typing import Annotated

class TopK(RuleConsumer):
    """
    This activates the top-k approach, where top k rules with the highest support are mined. This approach can rapidly speed up the mining time. 
    """
    k_value: Annotated[int, Gt(1)]
    
    """
    If there are multiple rules with the lowest head coverage in the priority queue, then all of them may not be saved into the queue since the k value can not be exceeded. For this case the ordering of such rules is not deterministic and same task can return different results due to the long tail of rules with a same head coverage. If you check this, the overflowed long tail will be also returned but you can get much more rules on the output than the k value.
    """
    allow_overflow: bool