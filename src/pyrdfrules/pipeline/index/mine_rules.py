from pyrdfrules.pipeline.index.constraint.constraint import Constraint
from pyrdfrules.pipeline.index.ruleconsumer.ruleconsumer import RuleConsumer
from pyrdfrules.pipeline.index.thresholds.threshold import Threshold
from pyrdfrules.pipeline.pipeline_item import PipelineItem
from typing import List, Optional


class MineRules(PipelineItem):
    """
    Mine rules from the indexed dataset with user-defined threshold, patterns and constraints.
    """
    
    """
    Mining thresholds. For one mining task you can specify several thresholds. All mined rules must reach defined thresholds. This greatly affects the mining time. 
    """
    thresholds: Optional[List[Threshold]]
    
    """
    Settings of the rule consumer to which all mined closed rules are saved. 
    """
    rule_consumer: List[RuleConsumer]
    
    """
    In this property, you can define several rule patterns. During the mining phase, each rule must match at least one of the defined patterns. Rule pattern has the following grammar: (? ? ?) ^ (? ? ?) => (? ? ?), ? is any atom item, ?V is any variable, ?C is any constant, ?a is the particular variable. You can also specify any constant instead of a variable. Symbol * matches any remaining body atoms, e.g, * ^ (? ? ?) => (? ? ?).
    """
    patterns: Optional[List[str]] # todo - make a patter type and verify the grammar / provide object oriented interface
    
    """
    Within constraints you can specify whether to mine rules without constants or you can include only chosen predicates into the mining phase.
    """
    constraints: Optional[List[Constraint]]
    
    """         
    If the value is lower than or equal to 0 and greater than 'all available cores' then the parallelism level is set to 'all available cores'.
    """
    paralelism: Optional[int]