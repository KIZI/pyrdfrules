from pyrdfrules.common.base_transformations import BaseTransformations
from pyrdfrules.prediction import Prediction
from pyrdfrules.rdfgraph import RDFGraph

class PredictionTransformations(BaseTransformations):

    def filter(self) -> Prediction:
        """Returns a new Prediction object with filtered predicted triples by measures of significance, rule patterns, triple filters and other options.

        Returns:
            Self: Shrinked RDFGraph object.
        """
        pass
    
    def shrink(self) -> Prediction:
        """Returns a new shrinked Prediction object.

        Returns:
            Self: Shrinked RDFGraph object.
        """
        pass
    
    def sort(self) -> Prediction:
        """Returns a new Prediction object with sorted predicted triples by their rules and their measures of significance.

        Returns:
            Self: Shrinked RDFGraph object.
        """
        pass
    
    def group(self) -> Prediction:
        """Aggregates and scores triples predicted by many rules.

        Returns:
            Self: Shrinked RDFGraph object.
        """
        pass
    
    def to_prediction_tasks(self) -> RDFGraph:
        """Generate prediction tasks by a user-defined strategy.

        Returns:
            Self: Shrinked RDFGraph object.
        """
        pass
    
    def to_dataset(self) -> RDFGraph:
        """Transform all predicted triples into the RDFGraph object.

        Returns:
            Self: Shrinked RDFGraph object.
        """
        pass