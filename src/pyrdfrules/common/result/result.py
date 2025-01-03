
from pyrdfrules.common.rule.resultrule import ResultRule
from pyrdfrules.common.rule.rule.body import RuleBody
from pyrdfrules.common.rule.rule.head import RuleHead
from pyrdfrules.common.rule.ruleset import Ruleset


class Result():
    
    ruleset: Ruleset = None
    """Ruleset generated by RDFRules.
    """
    
    def __init__(self, data: dict) -> None:
        self.id = id
        self.data = data
        
        self._parse_data()
        
        pass
    
    def _parse_data(self):
        
        rules = []
        
        for item in self.data:                
            match item:
                case {'body': _, 'head': __, 'measures': ___}:
                    # Item is a rule
                    
                    rule = ResultRule.model_construct(item)
                    
                    print(rule)
                    
                    pass
                case _: 
                    pass
    
    def get_ruleset(self) -> Ruleset:
        pass