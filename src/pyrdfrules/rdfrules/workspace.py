from __future__ import annotations

from typing import List, Optional, Union
from pydantic import AnyUrl, BaseModel
from enum import Enum


class FileTreeFile(BaseModel):
    name: str
    size: int


class FileTreeDirectory(BaseModel):
    name: str
    writable: bool
    subfiles: List[Union[FileTreeFile, FileTreeDirectory]]


class FileTree(BaseModel):
    file: Optional[FileTreeFile] = None
    directory: Optional[FileTreeDirectory] = None