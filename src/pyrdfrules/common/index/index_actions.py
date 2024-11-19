from typing import Awaitable
from pyrdfrules.common.base_actions import BaseActions
from pyrdfrules.common.base_transformations import BaseTransformations
from pyrdfrules.common.rule.ruleset import Ruleset
from pyrdfrules.index import Index

class IndexActions(BaseActions):
    
    def properties_cardinality(self) -> Awaitable[Ruleset]:
        """Get cardinalities from selected properties (such as size, domain, range).
        
        Returns:
            Awaitable[Ruleset]: Properties cardinality.
        """
        pass