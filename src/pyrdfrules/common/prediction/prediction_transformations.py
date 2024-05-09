from typing import Awaitable
from pyrdfrules.common.base_transformations import BaseTransformations
from pyrdfrules.prediction import Prediction
from pyrdfrules.rdfgraph import RDFGraph

class PredictionTransformations(BaseTransformations):

    async def filter(self) -> Awaitable[Prediction]:
        """Returns a new Prediction object with filtered predicted triples by measures of significance, rule patterns, triple filters and other options.

        Returns:
            Awaitable[Self]: Shrinked RDFGraph object.
        """
        pass
    
    async def shrink(self) -> Awaitable[Prediction]:
        """Returns a new shrinked Prediction object.

        Returns:
            Awaitable[Self]: Shrinked RDFGraph object.
        """
        pass
    
    async def sort(self) -> Awaitable[Prediction]:
        """Returns a new Prediction object with sorted predicted triples by their rules and their measures of significance.

        Returns:
            Awaitable[Self]: Shrinked RDFGraph object.
        """
        pass
    
    async def group(self) -> Awaitable[Prediction]:
        """Aggregates and scores triples predicted by many rules.

        Returns:
            Awaitable[Self]: Shrinked RDFGraph object.
        """
        pass
    
    async def to_prediction_tasks(self) -> Awaitable[RDFGraph]:
        """Generate prediction tasks by a user-defined strategy.

        Returns:
            Awaitable[Self]: Shrinked RDFGraph object.
        """
        pass
    
    async def to_dataset(self) -> Awaitable[RDFGraph]:
        """Transform all predicted triples into the RDFGraph object.

        Returns:
            Awaitable[Self]: Shrinked RDFGraph object.
        """
        pass