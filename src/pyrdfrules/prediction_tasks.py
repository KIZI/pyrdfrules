from pyrdfrules.base_rdfrules_object import BaseRDFRulesObject
from pyrdfrules.common.predictontasks.predictiontasks_actions import PredictionTasksActions
from pyrdfrules.common.predictontasks.predictiontasks_transformations import PredictionTasksTransformations

class PredictionTasks(BaseRDFRulesObject):
    """The PredictionTasks object is a special container of all predicted triples divided into generated prediction tasks. Each prediction task (e.g. <Alice> <wasBornIn> ?) has a list of sorted candidates by their score. This structure allows to select candidates by a chosen selection strategy, and construct a dataset from predicted candidates.

    Args:
        BaseRDFRulesObject (_type_): _description_
    """
    
    actions: PredictionTasksActions
    
    transformations: PredictionTasksTransformations
    
    def __init__(self):
        self.actions = PredictionTasksActions(self)
        self.transformations = PredictionTasksTransformations(self)