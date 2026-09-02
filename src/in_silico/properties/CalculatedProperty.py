from dataclasses import dataclass


@dataclass(frozen=True)
class CalculatedProperty:
    name: str
    value: int
