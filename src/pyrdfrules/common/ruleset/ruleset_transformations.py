from typing import Awaitable
from pyrdfrules.common.base_transformations import BaseTransformations
from pyrdfrules.rdfgraph import RDFGraph

class RulesetTransformations(BaseTransformations):
    
    async def filter(self) -> Awaitable[RDFGraph]:
        """Return a new RDFGraph object with updated triples.
        
        Returns:
            Awaitable[Self]: RDFGraph object with updated triples.
        """
        pass
    
    async def shrink(self) -> Awaitable[RDFGraph]:
        """Return a new RDFGraph object with updated triples.
        
        Returns:
            Awaitable[Self]: RDFGraph object with updated triples.
        """
        pass
    
    async def sort(self) -> Awaitable[RDFGraph]:
        """Return a new RDFGraph object with updated triples.
        
        Returns:
            Awaitable[Self]: RDFGraph object with updated triples.
        """
        pass
    
    async def compute_difference(self) -> Awaitable[RDFGraph]:
        """Return a new RDFGraph object with updated triples.
        
        Returns:
            Awaitable[Self]: RDFGraph object with updated triples.
        """
        pass

    async def make_clusters(self) -> Awaitable[RDFGraph]:
        """Return a new RDFGraph object with updated triples.
        
        Returns:
            Awaitable[Self]: RDFGraph object with updated triples.
        """
        pass

    async def prune(self) -> Awaitable[RDFGraph]:
        """Return a new RDFGraph object with updated triples.
        
        Returns:
            Awaitable[Self]: RDFGraph object with updated triples.
        """
        pass

    async def predict(self) -> Awaitable[RDFGraph]:
        """Return a new RDFGraph object with updated triples.
        
        Returns:
            Awaitable[Self]: RDFGraph object with updated triples.
        """
        pass