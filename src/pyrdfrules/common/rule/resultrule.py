from typing import List
from pydantic import BaseModel

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
    
    def as_test(self) -> str:
        return ''
    
    def as_json(self) -> str:
        return ''