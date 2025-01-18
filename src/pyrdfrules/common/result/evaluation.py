
from typing import List, Optional
from pyrdfrules.common.format.confusion_matrix import confusion_matrix
from pyrdfrules.common.logging.logger import log
from pyrdfrules.common.result.resultobject import ResultObject

class Evaluation(ResultObject):
    
    accuracy: Optional[float] = None
    """
    Accuracy of the evaluation.
    """
    
    fn: Optional[int] = None
    """
    Number of false negatives.
    """
    
    fp: Optional[int] = None
    """
    Number of false positives.
    """
    
    fscore: Optional[float] = None
    """
    F-score of the evaluation.
    """
    
    precision: Optional[float] = None
    """
    Precision of the evaluation.
    """
    
    recall: Optional[float] = None
    """
    Recall of the evaluation.
    """
    
    tn: Optional[int] = None
    """
    Number of true negatives.
    """
    
    tp: Optional[int] = None
    """
    Number of true positives.
    """
    
    n: Optional[int] = None
    """
    Number of items in the evaluation.
    """
    
    hits: Optional[List[dict]] = None
    """
    List of hits.
    """
    
    mr: Optional[float] = None
    
    mrr: Optional[float] = None
    
    total: Optional[int] = None
    
    totalCorrect: Optional[int] = None
    
    type: Optional[str] = None
    
    def print(self):    
        if self.type == "completeness":
            confusion_matrix(self.tp, self.fp, self.tn, self.fn)
        else:            
            log().debug(f"Could not print evaluation, unknown type {self.type}")