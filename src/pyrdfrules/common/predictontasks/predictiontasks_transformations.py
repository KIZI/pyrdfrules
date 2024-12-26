from pyrdfrules.common.base_transformations import BaseTransformations
from pyrdfrules.prediction import Prediction
from pyrdfrules.prediction_tasks import PredictionTasks
from pyrdfrules.rdfgraph import RDFGraph

class PredictionTasksTransformations(BaseTransformations):
    
    def filter(self) -> PredictionTasks:
        """Return a new PredictionTasks object with filtered prediction tasks.
        
        Returns:
            Self: RDFGraph object with updated triples.
        """
        pass
    
    def shrink(self) -> PredictionTasks:
        """Return a new RDFGraph object with updated triples.
        
        Returns:
            Self: RDFGraph object with updated triples.
        """
        pass
    
    def select_candidates(self) -> RDFGraph:
        """Select candidates from each prediction task by a selection strategy.
        
        Returns:
            Self: RDFGraph object with updated triples.
        """
        pass
    
    def to_prediction(self) -> Prediction:
        """Convert this object back to the Prediction object.
        
        Returns:
            Self: RDFGraph object with updated triples.
        """
        pass

    def to_dataset(self) -> RDFGraph:
        """Return a new RDFGraph object with updated triples.
        
        Returns:
            Self: RDFGraph object with updated triples.
        """
        pass