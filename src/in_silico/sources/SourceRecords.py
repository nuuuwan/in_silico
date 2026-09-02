from dataclasses import dataclass


@dataclass(frozen=True)
class SourceRecords:
    source: str
    records: dict[str, list[dict]]
    requests: tuple[str, ...]
    version: str
