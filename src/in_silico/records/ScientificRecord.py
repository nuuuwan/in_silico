from dataclasses import dataclass, field
from typing import Any

from in_silico.provenance import Provenance


@dataclass(frozen=True)
class ScientificRecord:
    identifier: str
    values: dict[str, Any] = field(default_factory=dict)
    provenance: Provenance | None = None
