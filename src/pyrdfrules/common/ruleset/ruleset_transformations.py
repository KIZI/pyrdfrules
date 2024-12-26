from pyrdfrules.common.base_transformations import BaseTransformations
from pyrdfrules.rdfgraph import RDFGraph

class RulesetTransformations(BaseTransformations):
    
    def filter(self) -> RDFGraph:
        """Return a new RDFGraph object with updated triples.
        
        Returns:
            Self: RDFGraph object with updated triples.
        """
        pass
    
    def shrink(self) -> RDFGraph:
        """Return a new RDFGraph object with updated triples.
        
        Returns:
            Self: RDFGraph object with updated triples.
        """
        pass
    
    def sort(self) -> RDFGraph:
        """Return a new RDFGraph object with updated triples.
        
        Returns:
            Self: RDFGraph object with updated triples.
        """
        pass
    
    def compute_difference(self) -> RDFGraph:
        """Return a new RDFGraph object with updated triples.
        
        Returns:
            Self: RDFGraph object with updated triples.
        """
        pass

    def make_clusters(self) -> RDFGraph:
        """Return a new RDFGraph object with updated triples.
        
        Returns:
            Self: RDFGraph object with updated triples.
        """
        pass

    def prune(self) -> RDFGraph:
        """Return a new RDFGraph object with updated triples.
        
        Returns:
            Self: RDFGraph object with updated triples.
        """
        pass

    def predict(self) -> RDFGraph:
        """Return a new RDFGraph object with updated triples.
        
        Returns:
            Self: RDFGraph object with updated triples.
        """
        pass