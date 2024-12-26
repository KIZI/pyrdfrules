from pyrdfrules.common.base_actions import BaseActions
from pyrdfrules.rdfgraph import RDFGraph

class RulesetActions(BaseActions):
    
    def get(self) -> RDFGraph:
        """Get and show all mined rules.
        
        Returns:
            Self: Get and show all triples.
        """
        pass
    
    
    def export(self) -> RDFGraph:
        """Export this Ruleset object into a file in some selected output format.
        
        Returns:
            Self: Get and show all triples.
        """
        pass