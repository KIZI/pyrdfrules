from pyrdfrules.common.base_actions import BaseActions
from pyrdfrules.rdfgraph import RDFGraph

class PredictionActions(BaseActions):
    
    def get(self) -> RDFGraph:
        """Get and show predicted triples with bound rules.
        
        Returns:
            Self: Get and show all triples.
        """
        pass
    
    def export(self) -> RDFGraph:
        """Export this graph into a file in some familiar RDF format.
        
        Returns:
            Self: Export.
        """
        pass
    