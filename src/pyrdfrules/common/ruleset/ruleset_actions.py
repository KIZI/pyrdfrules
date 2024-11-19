from typing import Awaitable
from pyrdfrules.common.base_actions import BaseActions
from pyrdfrules.rdfgraph import RDFGraph

class RulesetActions(BaseActions):
    
    def get(self) -> Awaitable[RDFGraph]:
        """Get and show all mined rules.
        
        Returns:
            Awaitable[Self]: Get and show all triples.
        """
        pass
    
    
    def export(self) -> Awaitable[RDFGraph]:
        """Export this Ruleset object into a file in some selected output format.
        
        Returns:
            Awaitable[Self]: Get and show all triples.
        """
        pass