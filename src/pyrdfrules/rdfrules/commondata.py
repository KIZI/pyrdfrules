from __future__ import annotations

from typing import List, Optional, Union
from pydantic import AnyUrl, BaseModel, model_serializer
from enum import Enum

class DataItemModel(BaseModel):

    @model_serializer()
    def serialize_model(self):
        
        parameters = {}
        
        for key, value in vars(self).items():
            if value is not None:
                parameters[key] = value

        return parameters
    pass


class TripleItem(BaseModel):
    pass


class TripleItemUri(BaseModel):
    prefix: Optional[str]
    nameSpace: Optional[str]
    localName: Optional[str]


class URL(BaseModel):
    url: AnyUrl


class Compression(str, Enum):
    GZ = "gz"
    BZ2 = "bz2"


class QuadMatcher(BaseModel):
    subject: Optional[str] = None
    predicate: Optional[str] = None
    object: Optional[str] = None
    graph: Optional[str] = None


class TripleMatcher(BaseModel):
    subject: Optional[str] = None
    predicate: Optional[str] = None
    object: Optional[str] = None


class QuadMapper(BaseModel):
    subject: Optional[str] = None
    predicate: Optional[str] = None
    object: Optional[str] = None
    graph: Optional[str] = None


class DiscretizationTaskMode(str, Enum):
    IN_MEMORY = "inmemory"
    EXTERNAL = "external"


class DiscretizationTask(BaseModel):
    name: str
    bins: Optional[int] = None
    buffer: Optional[int] = 15000000
    mode: Optional[DiscretizationTaskMode] = None
    support: Optional[float] = None


class RDFFormat(str, Enum):
    NTRIPLES_UTF8 = "nt"
    NQUADS_UTF8 = "nq"
    TURTLE_FLAT = "ttl"
    TRIG_BLOCKS = "trig"
    TRIX = "trix"


class Threshold(DataItemModel):
    name: str
    value: Optional[Union[int, float]] = None
    me: Optional[float] = None
    dme: Optional[bool] = None


class AtomItemPatternType(str, Enum):
    ANY = "Any"
    ANY_CONSTANT = "AnyConstant"
    ANY_VARIABLE = "AnyVariable"
    CONSTANT = "Constant"
    VARIABLE = "Variable"
    ONE_OF = "OneOf"
    NONE_OF = "NoneOf"


class AtomItemPattern(BaseModel):
    name: AtomItemPatternType
    value: Optional[Union[TripleItem, str, List[TripleItem]]] = None


class AtomPattern(BaseModel):
    subject: AtomItemPattern
    predicate: AtomItemPattern
    object: AtomItemPattern
    graph: AtomItemPattern


class RulePattern(BaseModel):
    body: List[AtomPattern]
    head: Optional[AtomPattern] = None
    exact: Optional[bool] = False
    orderless: Optional[bool] = False


class ConstantsPosition(str, Enum):
    NOWHERE = "Nowhere"
    OBJECT = "Object"
    SUBJECT = "Subject"
    LOWER_CARDINALITY_SIDE = "LowerCardinalitySide"
    LOWER_CARDINALITY_SIDE_HEAD = "LowerCardinalitySideHead"


class RuleConstraint(BaseModel):
    name: str
    values: Optional[List[TripleItemUri]] = None
    predicate: Optional[TripleItemUri] = None
    position: Optional[ConstantsPosition] = None
    injectiveMapping: Optional[bool] = None


class ConstantsForPredicatePosition(str, Enum):
    SUBJECT = "Subject"
    OBJECT = "Object"
    LOWER_CARDINALITY_SIDE = "LowerCardinalitySide"
    BOTH = "Both"


class RulesMining(BaseModel):
    thresholds: Optional[List[Threshold]] = None
    patterns: Optional[List[RulePattern]] = None
    constraints: Optional[List[RuleConstraint]] = None
    parallelism: Optional[int] = None


class RuleConsumerType(str, Enum):
    IN_MEMORY = "inMemory"
    ON_DISK = "onDisk"
    TOP_K = "topK"


class RuleConsumer(DataItemModel):
    name: RuleConsumerType
    file: Optional[str] = None
    format: Optional[str] = None
    k: Optional[int] = None
    allowOverflow: Optional[bool] = None


class MeasureType(str, Enum):
    HEAD_SIZE = "HeadSize"
    SUPPORT = "Support"
    HEAD_SUPPORT = "HeadSupport"
    HEAD_COVERAGE = "HeadCoverage"
    BODY_SIZE = "BodySize"
    CONFIDENCE = "Confidence"
    PCA_CONFIDENCE = "PcaConfidence"
    PCA_BODY_SIZE = "PcaBodySize"
    QPCA_CONFIDENCE = "QpcaConfidence"
    QPCA_BODY_SIZE = "QpcaBodySize"
    LIFT = "Lift"
    CLUSTER = "Cluster"


class Measure(BaseModel):
    name: MeasureType
    value: Optional[Union[int, float]] = None


class WeightedSimilarityCounting(BaseModel):
    name: str
    weight: float


class SimilarityCounting(BaseModel):
    features: List[WeightedSimilarityCounting]


class Clustering(BaseModel):
    minNeighbours: int
    minSimilarity: float
    features: SimilarityCounting


class PredictionSource(str, Enum):
    NDJSON = "ndjson"
    JSON = "json"
    CACHE = "cache"


class RulesetSource(str, Enum):
    TEXT = "txt"
    JSON = "json"
    NDJSON = "ndjson"
    CACHE = "cache"


class ShrinkSetup(BaseModel):
    take: Optional[int] = None
    drop: Optional[int] = None
    start: Optional[int] = None
    end: Optional[int] = None


class PruningStrategyType(str, Enum):
    DATA_COVERAGE_PRUNING = "DataCoveragePruning"
    MAXIMAL = "Maximal"
    CLOSED = "Closed"
    SKYLINE_PRUNING = "SkylinePruning"
    WITHOUT_QUASI_BINDING = "WithoutQuasiBinding"


class PruningStrategy(BaseModel):
    strategy: PruningStrategyType
    measure: Optional[str] = None
    injectiveMapping: Optional[bool] = None


class ConfidenceType(str, Enum):
    STANDARD_CONFIDENCE = "StandardConfidence"
    PCA_CONFIDENCE = "PcaConfidence"
    QPCA_CONFIDENCE = "QpcaConfidence"
    LIFT = "Lift"


class SupportType(str, Enum):
    SUPPORT = "Support"
    HEAD_COVERAGE = "HeadCoverage"


class SampleablePart(BaseModel):
    ratio: Optional[float] = None
    max: Optional[int] = None


class DefaultConfidence(str, Enum):
    CWA = "cwa"
    PCA = "pca"
    QPCA = "qpca"


class ScoreFactoryType(str, Enum):
    MAXIMUM = "maximum"
    NOISY_OR = "noisyOr"


class ScoreFactory(BaseModel):
    type: ScoreFactoryType
    scoreAfterAggregation: Optional[bool] = None


class RulesFactoryType(str, Enum):
    TOP_K = "topK"
    NON_REDUNDANT_TOP_K = "nonRedundantTopK"


class RulesFactory(BaseModel):
    type: RulesFactoryType
    topK: Optional[int] = None


class PredictionTaskPattern(BaseModel):
    p: Optional[TripleItemUri] = None
    targetVariable: Optional[str] = None


class PredictionTasksBuilderType(str, Enum):
    TEST_ALL = "testAll"
    TEST_CARDINALITIES = "testCardinalities"
    TEST_PATTERNS = "testPatterns"
    TEST_CUSTOM = "testCustom"
    PREDICTION_CARDINALITIES = "predictionCardinalities"
    PREDICTION_PATTERNS = "predictionPatterns"


class PredictionTasksBuilder(BaseModel):
    type: PredictionTasksBuilderType
    patterns: Optional[List[PredictionTaskPattern]] = None
    tasks: Optional[List[str]] = None


class SelectionStrategyType(str, Enum):
    PCA = "pca"
    QPCA = "qpca"
    TOP_K = "topK"


class SelectionStrategy(BaseModel):
    type: SelectionStrategyType
    k: Optional[int] = None


class RankingStrategyType(str, Enum):
    TEST = "test"
    PREDICTION = "prediction"


class RankingStrategy(BaseModel):
    type: RankingStrategyType


class RdfSourceSettingsType(str, Enum):
    TSV_RAW = "tsvRaw"
    TSV_PARSED_URIS = "tsvParsedUris"
    TSV_PARSED_LITERALS = "tsvParsedLiterals"
    NO_SETTINGS = "noSettings"


class RdfSourceSettings(BaseModel):
    settings: RdfSourceSettingsType


class AutoDiscretizationTask(BaseModel):
    minSupportLowerBoundOn: bool
    minSupportUpperBoundOn: bool
    minHeadSize: int
    minHeadCoverage: float
    maxRuleLength: int
    predicates: List[AnyUrl]


class HeadVariablePreMappingType(str, Enum):
    NO_MAPPING = "noMapping"
    FROM_TEST_SET_AT_HIGHER_CARDINALITY_SITE = "fromTestSetAtHigherCardinalitySite"
    FROM_TEST_SET_AT_CUSTOM_POSITION = "fromTestSetAtCustomPosition"


class HeadVariablePreMapping(BaseModel):
    type: HeadVariablePreMappingType
    target: Optional[str] = None
    
class Constraint(BaseModel):
    
    name: str
    
    pass    