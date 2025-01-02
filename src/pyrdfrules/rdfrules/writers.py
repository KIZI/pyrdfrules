from __future__ import annotations

from typing import List, Optional, Union
from pydantic import AnyUrl, BaseModel
from enum import Enum


class Quad(BaseModel):
    subject: str
    predicate: str
    object: str
    graph: str


class Triple(BaseModel):
    subject: str
    predicate: str
    object: str


class TripleItemType(str, Enum):
    URI = "Uri"
    TEXT = "Text"
    BOOLEAN = "Boolean"
    NUMBER = "Number"
    INTERVAL = "Interval"


class HistogramKey(BaseModel):
    subject: Optional[str] = None
    predicate: Optional[str] = None
    object: Optional[str] = None


class ResolvedPredictedTriple(BaseModel):
    triple: Triple
    predictedResult: str
    score: float
    rules: List[str]


class ResolvedInstantiatedAtom(BaseModel):
    subject: str
    predicate: str
    object: str


class ResolvedInstantiatedRule(BaseModel):
    head: ResolvedInstantiatedAtom
    body: List[ResolvedInstantiatedAtom]
    source: str
    predictedResult: str


class PropertyStats(BaseModel):
    name: str
    amount: int


class TaskResponseInProgress(BaseModel):
    id: str
    started: str
    logs: List[dict]


class TaskResponseResult(BaseModel):
    id: str
    started: str
    finished: str
    logs: List[dict]