from typing import Awaitable
from pyrdfrules.common.base_transformations import BaseTransformations
from pyrdfrules.prediction import Prediction
from pyrdfrules.prediction_tasks import PredictionTasks
from pyrdfrules.rdfgraph import RDFGraph

class PredictionTasksTransformations(BaseTransformations):
    
    def filter(self) -> Awaitable[PredictionTasks]:
        """Return a new PredictionTasks object with filtered prediction tasks.
        
        Returns:
            Awaitable[Self]: RDFGraph object with updated triples.
        """
        pass
    
    def shrink(self) -> Awaitable[PredictionTasks]:
        """Return a new RDFGraph object with updated triples.
        
        Returns:
            Awaitable[Self]: RDFGraph object with updated triples.
        """
        pass
    
    def select_candidates(self) -> Awaitable[RDFGraph]:
        """Select candidates from each prediction task by a selection strategy.
        
        Returns:
            Awaitable[Self]: RDFGraph object with updated triples.
        """
        pass
    
    def to_prediction(self) -> Awaitable[Prediction]:
        """Convert this object back to the Prediction object.
        
        Returns:
            Awaitable[Self]: RDFGraph object with updated triples.
        """
        pass

    def to_dataset(self) -> Awaitable[RDFGraph]:
        """Return a new RDFGraph object with updated triples.
        
        Returns:
            Awaitable[Self]: RDFGraph object with updated triples.
        """
        pass