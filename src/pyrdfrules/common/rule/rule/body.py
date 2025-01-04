from typing import List
from pydantic import BaseModel

from pyrdfrules.common.rule.rule.object import Object
from pyrdfrules.common.rule.rule.predicate import Predicate
from pyrdfrules.common.rule.rule.subject import Subject

class RuleBody(BaseModel):
    graphs: List[str]
    
    object: Object
    
    predicate: Predicate
    
    subject: Subject
    
    def as_text(self) -> str:
        return "(" + self.subject.value + ' <' + self.predicate.localName + '> ' + self.object.value + ")"