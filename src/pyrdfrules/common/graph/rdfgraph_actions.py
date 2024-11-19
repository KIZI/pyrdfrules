from typing import Awaitable
from pyrdfrules.common.base_actions import BaseActions
from pyrdfrules.rdfgraph import RDFGraph

class RDFGraphActions(BaseActions):
    
    def get(self) -> Awaitable[RDFGraph]:
        """Get and show all triples.
        
        Returns:
            Awaitable[Self]: Get and show all triples.
        """
        pass
    
    def histogram(self) -> Awaitable[RDFGraph]:
        """Return histogram by chosen aggregated triple items.
        
        Returns:
            Awaitable[Self]: Histogram.
        """
        pass
    
    def properties(self) -> Awaitable[RDFGraph]:
        """Return information and stats about all properties.
        
        Returns:
            Awaitable[Self]: Histogram.
        """
        pass
    
    def export(self) -> Awaitable[RDFGraph]:
        """Export this graph into a file in some familiar RDF format.
        
        Returns:
            Awaitable[Self]: Export.
        """
        pass
    