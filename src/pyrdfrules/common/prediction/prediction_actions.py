from typing import Awaitable
from pyrdfrules.common.base_actions import BaseActions
from pyrdfrules.rdfgraph import RDFGraph

class PredictionActions(BaseActions):
    
    def get(self) -> Awaitable[RDFGraph]:
        """Get and show predicted triples with bound rules.
        
        Returns:
            Awaitable[Self]: Get and show all triples.
        """
        pass
    
    def export(self) -> Awaitable[RDFGraph]:
        """Export this graph into a file in some familiar RDF format.
        
        Returns:
            Awaitable[Self]: Export.
        """
        pass
    