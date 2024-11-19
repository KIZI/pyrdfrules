from typing import Awaitable
from pyrdfrules.common.base_actions import BaseActions
from pyrdfrules.rdfgraph import RDFGraph

class PredictionTasksActions(BaseActions):
    
    def get(self) -> Awaitable[RDFGraph]:
        """Get and show prediction tasks with candidates.
        
        Returns:
            Awaitable[Self]: Get and show all triples.
        """
        pass
    
    def evaluate(self) -> Awaitable[RDFGraph]:
        """Evaluate all prediction tasks. It returns ranking metrics (such as hits@k, mean reciprocal rank), and completeness/quality metrics with confusion matrix (such as precision, recall).
        
        Returns:
            Awaitable[Self]: Export.
        """
        pass
    