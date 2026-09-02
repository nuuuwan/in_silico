from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Configuration:
    project_root: Path

    def resolve(self, path: str | Path) -> Path:
        return self.project_root / path
