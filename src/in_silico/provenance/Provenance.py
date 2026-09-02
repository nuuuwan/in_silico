from dataclasses import dataclass


@dataclass(frozen=True)
class Provenance:
    source: str
    source_identifier: str
