
from __future__ import annotations

from enum import Enum
from typing import List, Literal, Optional, Union, Set

from pydantic import AnyUrl, BaseModel, ConfigDict, Field, RootModel

class BaseObject(BaseModel):
    pass


class CachedTask(BaseObject):
    pass


class ToDatasetWithIntervals(BaseObject):
    pass


class GetRules(BaseObject):
    pass


class ExportRules(BaseObject):
    path: str
    format: RulesetSource


class ComputeSupport(BaseObject):
    supportType: SupportType


class FindSimilar(BaseObject):
    resolvedRule: ResolvedRule
    k: int
    dissimilar: bool


class Instantiate(BaseObject):
    predictedResults: Set[PredictedResult]
    injectiveMapping: bool


class Size(BaseObject):
    pass


class ComputeConfidence(BaseObject):
    confidenceType: ConfidenceType


class Sort(BaseObject):
    measures: List[(Optional[TypedKeyMap.Key[Measure]]
    bool


class GraphAwareRules(BaseObject):
    pass


class MakeClusters(BaseObject):
    clustering: Clustering[FinalRule]


class LoadRulesetWithoutIndex(BaseObject):
    path: str
    format: RulesetSource
    parallelism: Optional[int]


class Prune(BaseObject):
    strategy: PruningStrategy


class LoadRuleset(BaseObject):
    rulesetSource: LoadRuleset.RulesetSource
    parallelism: Optional[int]


class Predict(BaseObject):
    testSet: Optional[str]
    mergeTestAndTrainForPrediction: bool
    onlyTestCoveredPredictions: bool
    predictedResults: Set[PredictedResult]
    injectiveMapping: bool
    headVariablePreMapping: HeadVariablePreMapping


class ExportPrediction(BaseObject):
    path: str
    format: PredictionSource


class LoadPredictionWithoutIndex(BaseObject):
    path: str
    format: PredictionSource


class Size(BaseObject):
    pass


class Sort(BaseObject):
    pass


class LoadPrediction(BaseObject):
    path: str
    format: PredictionSource


class Group(BaseObject):
    scorer: PredictedTriplesAggregator.ScoreFactory
    consumer: PredictedTriplesAggregator.RulesFactory
    limit: int


class ToPredictionTasks(BaseObject):
    predictionTasksBuilder: PredictionTasksBuilder
    limit: int
    topK: int


class ToDataset(BaseObject):
    pass


class GetPrediction(BaseObject):
    maxRules: int


class GetPredictionTasks(BaseObject):
    maxCandidates: int


class Size(BaseObject):
    pass


class Select(BaseObject):
    selectionStrategy: Optional[SelectionStrategy]
    minScore: float
    predictedResults: Set[PredictedResult]


class Evaluate(BaseObject):
    rankingStrategy: RankingStrategy


class ToPredictions(BaseObject):
    pass


class ToDataset(BaseObject):
    pass


class WithModes(BaseObject):
    pass


class Discretize(BaseObject):
    task: AutoDiscretizationTask


class LoadIndex(BaseObject):
    path: str
    partially: bool


class PropertiesCardinalities(BaseObject):
    filter: Set[AnyUrl]


class ExportIndex(BaseObject):
    path: str


class Mine(BaseObject):
    rulesMining: RulesMining
    ruleConsumer: RuleConsumer.Invoker[Ruleset]


class ToDataset(BaseObject):
    


class AddPrefixes(BaseObject):
    path: Optional[str]
    url: Optional[AnyUrl]
    prefixes: List[Prefix]


class Properties(BaseObject):
    pass


class Discretize(BaseObject):
    quadMatcher: QuadMatcher
    inverse: bool
    discretizationTask: DiscretizationTask


class Index(BaseObject):
    train: Set[AnyUrl]
    test: Set[AnyUrl]


class Split(BaseObject):
    train: (AnyUrl
    Sampleable.Part


class Histogram(BaseObject):
    s: bool
    p: bool
    o: bool


class LoadDataset(BaseObject):
    path: Optional[str]
    url: Optional[AnyUrl]


class FilterQuads(BaseObject):
    quadMatchers: List[(QuadMatcher
    bool


class Size(BaseObject):
    pass


class GetQuads(BaseObject):
    pass


class Prefixes(BaseObject):
    pass


class ExportQuads(BaseObject):
    path: str


class DiscretizeInBulk(BaseObject):
    predicates: Set[AnyUrl]
    discretizationTask: DiscretizationTask


class LoadGraph(BaseObject):
    graphName: Optional[AnyUrl]
    path: Optional[str]
    url: Optional[AnyUrl]


class MapQuads(BaseObject):
    quadMatcher: QuadMatcher
    quadMapper: QuadMapper
    inverse: bool

