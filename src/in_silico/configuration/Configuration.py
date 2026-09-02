from dataclasses import dataclass
from pathlib import Path
from typing import ClassVar


@dataclass(frozen=True)
class Configuration:
    DATA_DIRECTORY: ClassVar[str] = "data"
    RESEARCH_DIRECTORY: ClassVar[str] = "research"
    RESULTS_DIRECTORY: ClassVar[str] = "results"
    TESTS_DIRECTORY: ClassVar[str] = "tests"

    project_root: Path

    def resolve(self, path: str | Path) -> Path:
        return self.project_root / path

    @property
    def data_path(self) -> Path:
        return self.resolve(self.DATA_DIRECTORY)

    @property
    def research_path(self) -> Path:
        return self.resolve(self.RESEARCH_DIRECTORY)

    @property
    def results_path(self) -> Path:
        return self.resolve(self.RESULTS_DIRECTORY)

    @property
    def tests_path(self) -> Path:
        return self.resolve(self.TESTS_DIRECTORY)
