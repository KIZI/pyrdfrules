from typing import Awaitable
from pyrdfrules.common.base_transformations import BaseTransformations
from pyrdfrules.rdfgraph import RDFGraph

class RulesetTransformations(BaseTransformations):
    
    def filter(self) -> Awaitable[RDFGraph]:
        """Return a new RDFGraph object with updated triples.
        
        Returns:
            Awaitable[Self]: RDFGraph object with updated triples.
        """
        pass
    
    def shrink(self) -> Awaitable[RDFGraph]:
        """Return a new RDFGraph object with updated triples.
        
        Returns:
            Awaitable[Self]: RDFGraph object with updated triples.
        """
        pass
    
    def sort(self) -> Awaitable[RDFGraph]:
        """Return a new RDFGraph object with updated triples.
        
        Returns:
            Awaitable[Self]: RDFGraph object with updated triples.
        """
        pass
    
    def compute_difference(self) -> Awaitable[RDFGraph]:
        """Return a new RDFGraph object with updated triples.
        
        Returns:
            Awaitable[Self]: RDFGraph object with updated triples.
        """
        pass

    def make_clusters(self) -> Awaitable[RDFGraph]:
        """Return a new RDFGraph object with updated triples.
        
        Returns:
            Awaitable[Self]: RDFGraph object with updated triples.
        """
        pass

    def prune(self) -> Awaitable[RDFGraph]:
        """Return a new RDFGraph object with updated triples.
        
        Returns:
            Awaitable[Self]: RDFGraph object with updated triples.
        """
        pass

    def predict(self) -> Awaitable[RDFGraph]:
        """Return a new RDFGraph object with updated triples.
        
        Returns:
            Awaitable[Self]: RDFGraph object with updated triples.
        """
        pass