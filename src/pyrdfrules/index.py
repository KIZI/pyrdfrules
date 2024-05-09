from typing import Awaitable, Self
from pyrdfrules.base_rdfrules_object import BaseRDFRulesObject
from pyrdfrules.common.index.index_actions import IndexActions
from pyrdfrules.common.index.index_transformations import IndexTransformations

class Index(BaseRDFRulesObject):
    
    actions: IndexActions
    
    transformations: IndexTransformations
    
    def __init__(self):
        self.actions = IndexActions(self)
        self.transformations = IndexTransformations(self)
        
    
    def load(self) -> Awaitable[Self]:
        """Loads the index from cache.

        Returns:
            Awaitable[Self]: Loaded index object.
        """
        
        pass