from typing import Awaitable
from typing import Self

from pyrdfrules.base_rdfrules_object import BaseRDFRulesObject
from pyrdfrules.common.graph.rdfgraph_actions import RDFGraphActions
from pyrdfrules.common.graph.rdfgraph_transformations import RDFGraphTransformations

class RDFGraph(BaseRDFRulesObject):
    
    actions: RDFGraphActions
    
    transformations: RDFGraphTransformations
    
    def __init__(self):
        self.actions = RDFGraphActions(self)
        self.transformations = RDFGraphTransformations(self)
        
        
    def load(self):
        """_summary_
        """
        pass