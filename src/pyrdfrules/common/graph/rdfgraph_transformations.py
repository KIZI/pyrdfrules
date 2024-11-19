from typing import Awaitable
from pyrdfrules.common.base_transformations import BaseTransformations
from pyrdfrules.rdfgraph import RDFGraph

class RDFGraphTransformations(BaseTransformations):
    
    def map_quads(self) -> Awaitable[RDFGraph]:
        """Return a new RDFGraph object with updated triples.
        
        Returns:
            Awaitable[Self]: RDFGraph object with updated triples.
        """
        pass
    
    def filter(self) -> Awaitable[RDFGraph]:
        """Return a new shrinked RDFGraph object.

        Returns:
            Awaitable[Self]: Shrinked RDFGraph object.
        """
        pass
    
    def shrink(self) -> Awaitable[RDFGraph]:
        """Return a new shrinked RDFGraph object.

        Returns:
            Awaitable[Self]: Shrinked RDFGraph object.
        """
        pass
    
    def split(self) -> Awaitable[RDFGraph]:
        """Split the loaded KG into several parts with sampling.

        Returns:
            Awaitable[Self]: Shrinked RDFGraph object.
        """
        pass
    
    def discretize(self) -> Awaitable[RDFGraph]:
        """Return a new RDFGraph object with discretized numeric literals by a predefined task and filter.

        Returns:
            Awaitable[Self]: Shrinked RDFGraph object.
        """
        pass
    
    def merge(self) -> Awaitable[RDFGraph]:
        """Merge all loaded graphs into one RDFDataset.

        Returns:
            Awaitable[Self]: Shrinked RDFGraph object.
        """
        pass