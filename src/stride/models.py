from dataclasses import dataclass
from typing import List


@dataclass
class Threat:
    category: str
    title: str
    description: str
    mitigation: str
    severity: str


@dataclass
class ComponentAnalysis:
    component: str
    threats: List[Threat]