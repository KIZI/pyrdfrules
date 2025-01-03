# generated by datamodel-codegen:
#   filename:  https://raw.githubusercontent.com/propi/rdfrules/refs/heads/master/http/schema/common.json
#   timestamp: 2025-01-02T18:33:57+00:00

from __future__ import annotations

from typing import Any, List, Literal, Optional, Union

from pydantic import BaseModel, Field, RootModel


class Model(RootModel[Any]):
    root: Any


class Measure(BaseModel):
    name: Optional[str] = None
    value: Optional[float] = None


class Variable(BaseModel):
    type: Literal['variable']
    value: str


class TripleItemInterval(BaseModel):
    left: float
    right: float
    leftIsOpen: bool
    rightIsOpen: bool


class TripleItemLongUri(RootModel[str]):
    root: str = Field(..., pattern='<.*>')


class TripleItemPrefixedUri(BaseModel):
    prefix: str
    nameSpace: str
    localName: str


class TripleItemBlankNode(RootModel[str]):
    root: str = Field(..., pattern='_:.*')


class Constant(BaseModel):
    type: Literal['constant']
    value: Union[
        TripleItemInterval, Union[TripleItemLongUri, TripleItemPrefixedUri, TripleItemBlankNode], str, float, bool
    ]


class Atom(BaseModel):
    subject: Union[Variable, Constant]
    predicate: Union[TripleItemLongUri, TripleItemPrefixedUri, TripleItemBlankNode]
    object: Union[Variable, Constant]
    graphs: Optional[List[Union[TripleItemLongUri, TripleItemPrefixedUri, TripleItemBlankNode]]] = None


class Rule(BaseModel):
    head: Atom
    body: List[Atom]
    measures: List[Measure]