from pyrdfrules.common.base_actions import BaseActions
from pyrdfrules.common.base_transformations import BaseTransformations
from pyrdfrules.common.rule.ruleset import Ruleset

class IndexActions(BaseActions):
    
    def properties_cardinality(self) -> Ruleset:
        """Get cardinalities from selected properties (such as size, domain, range).
        
        Returns:
            Ruleset: Properties cardinality.
        """
        pass