from typing import List
from pydantic import BaseModel

from pyrdfrules.common.graph.graph import Graph
from pyrdfrules.common.rule.measure.measure import RuleMeasure
from pyrdfrules.common.rule.rule.body import RuleBody
from pyrdfrules.common.rule.rule.head import RuleHead

class ResultRule(BaseModel):
    """
    Rule mined by RDFRules.
    """
    
    """
    Represents the list of the parts of the rule in its body.
    """
    body: List[RuleBody]
    
    """
    Head of the rule.
    """
    head: RuleHead
    
    """
    Measures of the rule.
    """
    measures: List[RuleMeasure]