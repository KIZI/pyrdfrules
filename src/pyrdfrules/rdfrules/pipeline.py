from __future__ import annotations

from typing import List, Literal, Optional, Union
from pydantic import AnyUrl, BaseModel, model_serializer
from enum import Enum

from pyrdfrules.rdfrules.commondata import ConfidenceType, Constraint, RuleConsumer, SupportType, Threshold
from pyrdfrules.rdfrules.jsonformats import PrefixFull


class Pipeline(BaseModel):
    """Pipeline is a sequence of tasks to be executed.
    """
    tasks: List[RDFRulesTaskModel]
    
    @model_serializer()
    def serialize_model(self):
        return self.tasks
    
    pass

class RDFRulesTaskModel(BaseModel):

    @model_serializer()
    def serialize_model(self):
        
        parameters = {}
        
        for key, value in vars(self).items():
            if key != 'name' and value is not None:
                parameters[key] = value

        return {'name': self.name, 'parameters': parameters}
    pass

class LoadGraph(RDFRulesTaskModel):
    name: Literal["LoadGraph"] = "LoadGraph"
    
    graphName: Optional[str] = None
    path: Optional[str] = None
    url: Optional[AnyUrl] = None
    settings: Optional[str] = None


class LoadDataset(RDFRulesTaskModel):
    name: Literal["LoadDataset"] = "LoadDataset"
    
    path: Optional[str] = None
    url: Optional[AnyUrl] = None


class LoadRulesetWithoutIndex(RDFRulesTaskModel):
    name: Literal["LoadRulesetWithoutIndex"] = "LoadRulesetWithoutIndex"
    
    path: str
    format: str
    parallelism: Optional[int] = None


class LoadPredictionWithoutIndex(RDFRulesTaskModel):
    name: Literal["LoadPredictionWithoutIndex"] = "LoadPredictionWithoutIndex"
    
    path: str
    format: str


class MergeDatasets(RDFRulesTaskModel):
    name: Literal["MergeDatasets"] = "MergeDatasets"
    
    pass


class MapQuads(RDFRulesTaskModel):
    name: Literal["MapQuads"] = "MapQuads"
    
    search: str
    replacement: str
    inverse: bool


class FilterQuads(RDFRulesTaskModel):
    name: Literal["FilterQuads"] = "FilterQuads"
    
    or_: List[dict]


class Shrink(RDFRulesTaskModel):
    name: Literal["Shrink"] = "Shrink"
    
    setup: str


class Split(RDFRulesTaskModel):
    name: Literal["Split"] = "Split"
    
    train: dict
    test: dict


class AddPrefixes(RDFRulesTaskModel):
    name: Literal["AddPrefixes"] = "AddPrefixes"
    
    path: Optional[str] = None
    url: Optional[AnyUrl] = None
    prefixes: List[PrefixFull]


class Prefixes(RDFRulesTaskModel):
    name: Literal["Prefixes"] = "Prefixes"
    pass


class Discretize(RDFRulesTaskModel):
    name: Literal["Discretize"] = "Discretize"
    
    matcher: str
    inverse: bool
    task: str


class DiscretizeInBulk(RDFRulesTaskModel):
    name: Literal["DiscretizeInBulk"]
    
    predicates: List[str]
    task: str


class Cache(RDFRulesTaskModel):
    name: Literal["Cache"] = "Cache"
    
    path: str
    inMemory: bool
    revalidate: bool


class Index(RDFRulesTaskModel):
    name: Literal["Index"] = "Index"
    
    train: List[str]
    test: List[str]


class ExportQuads(RDFRulesTaskModel):
    name: Literal["ExportQuads"] = "ExportQuads"
    
    path: str


class ExportIndex(RDFRulesTaskModel):
    name: Literal["ExportIndex"] = "ExportIndex"
    
    path: str


class ExportPrediction(RDFRulesTaskModel):
    name: Literal["ExportPrediction"] = "ExportPrediction"
    
    path: str
    format: str


class GetQuads(RDFRulesTaskModel):
    name: Literal["GetQuads"] = "GetQuads"
    
    pass


class Size(RDFRulesTaskModel):
    name: Literal["Size"] = "Size"
    
    pass


class Properties(RDFRulesTaskModel):
    name: Literal["Properties"] = "Properties"
    pass


class Histogram(RDFRulesTaskModel):
    name: Literal["Histogram"] = "Histogram"
    subject: bool
    predicate: bool
    object: bool


class LoadIndex(RDFRulesTaskModel):
    name: Literal["LoadIndex"] = "LoadIndex"
    
    path: str
    partially: bool


class CacheIndex(RDFRulesTaskModel):
    name: Literal["CacheIndex"] = "CacheIndex"
    
    path: str
    inMemory: bool
    revalidate: bool


class ToDataset(RDFRulesTaskModel):
    name: Literal["ToDataset"] = "ToDataset"
    
    pass


class ToDatasetWithIntervals(RDFRulesTaskModel):
    name: Literal["ToDatasetWithIntervals"] = "ToDatasetWithIntervals"
    
    pass


class ToDatasetPrediction(RDFRulesTaskModel):
    name: Literal["ToDatasetPrediction"] = "ToDatasetPrediction"
    
    pass


class ToDatasetPredictionTasks(RDFRulesTaskModel):
    name: Literal["ToDatasetPredictionTasks"] = "ToDatasetPredictionTasks"
    
    pass


class ToPredictions(RDFRulesTaskModel):
    name: Literal["ToPredictions"] = "ToPredictions"
    
    pass


class ToPredictionTasks(RDFRulesTaskModel):
    name: Literal["ToPredictionTasks"] = "ToPredictionTasks"
    
    generator: str
    limit: int
    topK: int


class DiscretizeTask(RDFRulesTaskModel):
    name: Literal["DiscretizeTask"] = "DiscretizeTask"
    
    task: str


class Mine(RDFRulesTaskModel):
    name: Literal["Mine"] = "Mine"
    
    mining: Optional[dict] = None
    ruleConsumers: List[RuleConsumer] = []
    thresholds: List[Threshold] = []
    patterns: Optional[List] = None
    
    constraints: List[Constraint] = []
    
    parallelism: Optional[int] = None


class LoadRuleset(RDFRulesTaskModel):
    name: Literal["LoadRuleset"] = "LoadRuleset"
    
    rules: Optional[List[str]] = None
    parallelism: Optional[int] = None


class LoadPrediction(RDFRulesTaskModel):
    name: Literal["LoadPrediction"] = "LoadPrediction"
    
    path: str
    format: str


class Predict(RDFRulesTaskModel):
    name: Literal["Predict"] = "Predict"
    
    testPath: Optional[str] = None
    mergeTestAndTrainForPrediction: bool
    onlyTestCoveredPredictions: bool
    predictedResults: List[str]
    injectiveMapping: bool
    headVariablePreMapping: str


class Prune(RDFRulesTaskModel):
    name: Literal["Prune"] = "Prune"
    
    strategy: str


class FilterRules(RDFRulesTaskModel):
    name: Literal["FilterRules"] = "FilterRules"
    
    measures: List[dict]
    patterns: List[str]
    tripleMatchers: List[dict]
    indices: List[int]


class FilterPrediction(RDFRulesTaskModel):
    name: Literal["FilterPrediction"] = "FilterPrediction"
    
    predictedResults: List[str]
    tripleMatchers: List[dict]
    measures: List[dict]
    patterns: List[str]
    distinctPredictions: bool
    withoutTrainTriples: bool
    onlyCoveredTestPredictionTasks: bool
    indices: List[int]


class FilterPredictionTasks(RDFRulesTaskModel):
    name: Literal["FilterPredictionTasks"] = "FilterPredictionTasks"
    
    predictedResults: List[str]
    tripleMatchers: List[str]
    nonEmptyPredictions: bool


class SelectPredictions(RDFRulesTaskModel):
    name: Literal["SelectPredictions"] = "SelectPredictions"
    
    strategy: Optional[str] = None
    minScore: float
    predictedResults: List[str]


class WithModes(RDFRulesTaskModel):
    name: Literal["WithModes"] = "WithModes"
    
    pass


class GroupPredictions(RDFRulesTaskModel):
    name: Literal["GroupPredictions"] = "GroupPredictions"
    
    scorer: Optional[str] = None


class Evaluate(RDFRulesTaskModel):
    name: Literal["Evaluate"] = "Evaluate"
    
    ranking: str


class ShrinkRuleset(RDFRulesTaskModel):
    name: Literal["ShrinkRuleset"] = "ShrinkRuleset"
    
    setup: str


class ShrinkPrediction(RDFRulesTaskModel):
    name: Literal["ShrinkPrediction"] = "ShrinkPrediction"
    
    setup: str


class ShrinkPredictionTasks(RDFRulesTaskModel):
    name: Literal["ShrinkPredictionTasks"] = "ShrinkPredictionTasks"
    
    setup: str


class SortRuleset(RDFRulesTaskModel):
    name: Literal["SortRuleset"] = "SortRuleset"
    
    by: List[str]
    
    pass


class SortPrediction(RDFRulesTaskModel):
    name: Literal["SortPrediction"] = "SortPrediction"
    pass


class ComputeConfidence(RDFRulesTaskModel):
    name: Literal["ComputeConfidence"] = "ComputeConfidence"
    
    confidenceType: ConfidenceType
    
    min: Optional[float] = None
    topk: Optional[int] = None
    
    
    @model_serializer()
    def serialize_model(self):
        parameters = {}
        
        for key, value in vars(self).items():
            if key != 'name' and value is not None:
                
                if key == 'confidenceType':
                    parameters["name"] = value
                else:
                    parameters[key] = value

        return {'name': self.name, 'parameters': parameters}


class ComputeSupport(RDFRulesTaskModel):
    name: Literal["ComputeSupport"] = "ComputeSupport"
    
    supportType: SupportType


class MakeClusters(RDFRulesTaskModel):
    name: Literal["MakeClusters"] = "MakeClusters"
    
    clustering: str


class FindSimilar(RDFRulesTaskModel):
    name: Literal["FindSimilar"] = "FindSimilar"
    
    rule: str
    take: int
    dissimilar: bool


class CacheRuleset(RDFRulesTaskModel):
    name: Literal["CacheRuleset"] = "CacheRuleset"
    
    path: str
    inMemory: bool
    revalidate: bool


class CachePrediction(RDFRulesTaskModel):
    name: Literal["CachePrediction"] = "CachePrediction"
    
    path: str
    inMemory: bool
    revalidate: bool


class CachePredictionTasks(RDFRulesTaskModel):
    name: Literal["CachePredictionTasks"] = "CachePredictionTasks"
    
    path: str
    revalidate: bool


class Instantiate(RDFRulesTaskModel):
    name: Literal["Instantiate"] = "Instantiate"
    
    predictedResults: List[str]
    injectiveMapping: bool


class GraphAwareRules(RDFRulesTaskModel):
    name: Literal["GraphAwareRules"] = "GraphAwareRules"
    
    pass


class ExportRules(RDFRulesTaskModel):
    name: Literal["ExportRules"] = "ExportRules"
    
    pass


class PropertiesCardinalities(RDFRulesTaskModel):
    name: Literal["PropertiesCardinalities"] = "PropertiesCardinalities"
    
    filter: List[str]


class GetRules(RDFRulesTaskModel):
    name: Literal["GetRules"] = "GetRules"
    
    pass


class GetPrediction(RDFRulesTaskModel):
    name: Literal["GetPrediction"] = "GetPrediction"
    
    maxRules: int


class GetPredictionTasks(RDFRulesTaskModel):
    name: Literal["GetPredictionTasks"] = "GetPredictionTasks"
    
    maxCandidates: int


class RulesetSize(RDFRulesTaskModel):
    name: Literal["RulesetSize"] = "RulesetSize"
    
    pass


class PredictionSize(RDFRulesTaskModel):
    name: Literal["PredictionSize"] = "PredictionSize"
    
    pass


class PredictionTasksSize(RDFRulesTaskModel):
    name: Literal["PredictionTasksSize"] = "PredictionTasksSize"
    
    pass