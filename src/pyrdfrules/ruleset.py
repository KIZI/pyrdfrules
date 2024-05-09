from pyrdfrules.base_rdfrules_object import BaseRDFRulesObject
from pyrdfrules.common.ruleset.ruleset_actions import RulesetActions
from pyrdfrules.common.ruleset.ruleset_transformations import RulesetTransformations

class Ruleset(BaseRDFRulesObject):
    
    actions: RulesetActions
    
    transformations: RulesetTransformations
    
    def __init__(self):
        self.actions = RulesetActions(self)
        self.transformations = RulesetTransformations(self)