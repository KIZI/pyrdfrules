from pyrdfrules.common.base_actions import BaseActions
from pyrdfrules.rdfgraph import RDFGraph

class PredictionTasksActions(BaseActions):
    
    def get(self) -> RDFGraph:
        """Get and show prediction tasks with candidates.
        
        Returns:
            Self: Get and show all triples.
        """
        pass
    
    def evaluate(self) -> RDFGraph:
        """Evaluate all prediction tasks. It returns ranking metrics (such as hits@k, mean reciprocal rank), and completeness/quality metrics with confusion matrix (such as precision, recall).
        
        Returns:
            Self: Export.
        """
        pass
    