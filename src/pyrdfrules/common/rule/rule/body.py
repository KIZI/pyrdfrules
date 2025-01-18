from typing import List
from pydantic import BaseModel

from pyrdfrules.common.rule.rule.object import Object
from pyrdfrules.common.rule.rule.predicate import Predicate
from pyrdfrules.common.rule.rule.subject import Subject

class RuleBody(BaseModel):
    graphs: List[str]
    
    object: Object
    
    predicate: Predicate|str|dict
    
    subject: Subject
    
    def get_predicate_text(self) -> str:
        if isinstance(self.predicate, Predicate):
            return self.predicate.localName
        else:
            return str(self.predicate)
    
    def as_text(self) -> str:
        return "(" + self.subject.value + ' <' + self.get_predicate_text() + '> ' + self.object.value + ")"