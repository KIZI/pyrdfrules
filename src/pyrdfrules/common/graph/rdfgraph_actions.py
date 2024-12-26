from pyrdfrules.common.base_actions import BaseActions
from pyrdfrules.rdfgraph import RDFGraph

class RDFGraphActions(BaseActions):
    
    def get(self) -> RDFGraph:
        """Get and show all triples.
        
        Returns:
            Self: Get and show all triples.
        """
        pass
    
    def histogram(self) -> RDFGraph:
        """Return histogram by chosen aggregated triple items.
        
        Returns:
            Self: Histogram.
        """
        pass
    
    def properties(self) -> RDFGraph:
        """Return information and stats about all properties.
        
        Returns:
            Self: Histogram.
        """
        pass
    
    def export(self) -> RDFGraph:
        """Export this graph into a file in some familiar RDF format.
        
        Returns:
            Self: Export.
        """
        pass
    