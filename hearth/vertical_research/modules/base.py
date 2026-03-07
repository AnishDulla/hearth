from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any

from pydantic import BaseModel


@dataclass
class ModuleRunResult:
    name: str
    output: BaseModel
    raw_text: str
    tool_calls: int
    notes: list[str]


class BaseModule(ABC):
    name: str
    display_name: str

    @property
    @abstractmethod
    def instructions(self) -> str:
        raise NotImplementedError

    @property
    @abstractmethod
    def output_schema(self) -> type[BaseModel]:
        raise NotImplementedError

    @abstractmethod
    def build_input(self, vertical: str, icp: str, context: dict[str, Any] | None = None) -> str:
        raise NotImplementedError
