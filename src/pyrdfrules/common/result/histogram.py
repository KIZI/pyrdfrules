from typing import List, Optional
from pydantic import BaseModel, PositiveInt

from pyrdfrules.common.result.resultobject import ResultObject

class HistogramSingleResult(ResultObject):
    """
    Histogram single result.
    """
    
    amount: PositiveInt
    """Histogram amount.
    """
    
    object: Optional[str|dict|None] = None
    """RDF object, if available.
    """
    
    predicate: Optional[str|dict|None] = None
    """RDF predicate, if available.
    """
    
    subject: Optional[str|dict|None] = None
    """RDF subject, if available.
    """
    
    def get_histogram_name(self) -> str:
        """Returns the name of the histogram item.
        
        Returns:
            str: Name of the histogram item.
        """
        
        parts = []
        
        if self.subject is not None:
            parts.append(self.subject)
        
        if self.predicate is not None:
            parts.append(self.predicate)
        
        if self.object is not None:
            parts.append(self.object)

        if len(parts) == 0:
            return "Unknown"

        return " - ".join(parts)
    
    pass

class HistogramResult(BaseModel):
    """
    Histogram result collection.
    
    Attributes:
        subject (bool): If True, the histogram is created for subjects.
        predicate (bool): If True, the histogram is created for predicates.
        object (bool): If True, the histogram is created for objects.
    """
    
    list: List[HistogramSingleResult] = []
    
    def get_sorted(self, reverse = True) -> List[HistogramSingleResult]:
        """Returns the histogram list sorted by amount.
        
        Args:
            reverse (bool): If True, the list is sorted in descending order (most frequent first).
        
        Returns:
            list[HistogramSingleResult]: Sorted histogram list.
        """
        
        return sorted(self.list, key=lambda x: x.amount, reverse=reverse)
    
    def get_top(self, n: int) -> List[HistogramSingleResult]:
        """Returns the top n elements from the histogram.
        
        Args:
            n (int): Number of elements to return.
        
        Returns:
            list[HistogramSingleResult]: Top n elements.
        """
        
        return self.get_sorted()[:n]
    
    def get_bottom(self, n: int) -> List[HistogramSingleResult]:
        """Returns the bottom n elements from the histogram.
        
        Args:
            n (int): Number of elements to return.
        
        Returns:
            list[HistogramSingleResult]: Bottom n elements.
        """
        
        return self.get_sorted(reverse=False)[:n]
    
    def print(self, top_n: int = 10):
        """Prints the histogram.
        
        Args:
            top_n (int): Number of top elements to print.      
        """
        
        from pyrdfrules.common.format.histogram import draw_histogram
        
        top = self.get_top(top_n)
        
        mapping = {}
        
        for item in top:
            mapping[item.get_histogram_name()] = item.amount
        
        draw_histogram(mapping)
    
    pass
