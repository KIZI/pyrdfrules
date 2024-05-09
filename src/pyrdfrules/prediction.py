from pyrdfrules.base_rdfrules_object import BaseRDFRulesObject
from pyrdfrules.common.prediction.prediction_actions import PredictionActions
from pyrdfrules.common.prediction.prediction_transformations import PredictionTransformations

class Prediction(BaseRDFRulesObject):
    
    actions: PredictionActions
    
    transformations: PredictionTransformations
    
    def __init__(self):
        self.actions = PredictionActions(self)
        self.transformations = PredictionTransformations(self)