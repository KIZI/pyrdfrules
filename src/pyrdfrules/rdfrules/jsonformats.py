from __future__ import annotations

from typing import List, Optional, Union
from pydantic import AnyUrl, BaseModel
from enum import Enum


class PrefixFull(BaseModel):
    prefix: str
    nameSpace: str


class PrefixNamespace(BaseModel):
    nameSpace: str


class Prefix(BaseModel):
    full: Optional[PrefixFull] = None
    namespace: Optional[PrefixNamespace] = None


class PredictedResult(str, Enum):
    POSITIVE = "Positive"
    NEGATIVE = "Negative"
    PCA_POSITIVE = "PcaPositive"


class PruningStrategyDataCoveragePruning(BaseModel):
    measure: str
    injectiveMapping: bool
    minCoverage: float


class TripleItem(BaseModel):
    pass


class TripleItemPosition(BaseModel):
    subject: Optional[TripleItem] = None
    object: Optional[TripleItem] = None


class PredictionTaskResolved(BaseModel):
    task: str
    result: str


class PredictionTaskResultResolved(BaseModel):
    task: str
    result: str
