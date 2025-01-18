from typing import List
from pydantic import BaseModel

from pyrdfrules.common.rule.rule.object import Object
from pyrdfrules.common.rule.rule.predicate import Predicate
from pyrdfrules.common.rule.rule.subject import Subject

class RuleHead(BaseModel):
    
    graphs: List[str]
    
    object: Object
    
    predicate: str|dict
    
    subject: Subject
    
    def as_text(self) -> str:
        return "(" + self.subject.value + ' <' + str(self.predicate) + '> ' + self.object.value + ")"