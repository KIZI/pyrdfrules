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
    
    def as_text(self) -> str:
        
        body_segments = []
        
        for body in self.body:
            body_segments.append(body.as_text())
            
        body_text = ' ^ '.join(body_segments)
        
        return body_text + ' -> ' + self.head.as_text()
    
    def as_json(self) -> str:
        return self.json()