from pyrdfrules.common.base_transformations import BaseTransformations
from pyrdfrules.rdfgraph import RDFGraph

class RDFGraphTransformations(BaseTransformations):
    
    def map_quads(self) -> RDFGraph:
        """Return a new RDFGraph object with updated triples.
        
        Returns:
            Self: RDFGraph object with updated triples.
        """
        pass
    
    def filter(self) -> RDFGraph:
        """Return a new shrinked RDFGraph object.

        Returns:
            Self: Shrinked RDFGraph object.
        """
        pass
    
    def shrink(self) -> RDFGraph:
        """Return a new shrinked RDFGraph object.

        Returns:
            Self: Shrinked RDFGraph object.
        """
        pass
    
    def split(self) -> RDFGraph:
        """Split the loaded KG into several parts with sampling.

        Returns:
            Self: Shrinked RDFGraph object.
        """
        pass
    
    def discretize(self) -> RDFGraph:
        """Return a new RDFGraph object with discretized numeric literals by a predefined task and filter.

        Returns:
            Self: Shrinked RDFGraph object.
        """
        pass
    
    def merge(self) -> RDFGraph:
        """Merge all loaded graphs into one RDFDataset.

        Returns:
            Self: Shrinked RDFGraph object.
        """
        pass