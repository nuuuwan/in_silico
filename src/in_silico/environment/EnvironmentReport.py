import json
import platform
from dataclasses import asdict, dataclass
from importlib.metadata import PackageNotFoundError, version

from in_silico.environment.LibraryVersion import LibraryVersion


@dataclass(frozen=True)
class EnvironmentReport:
    package_version: str
    python_version: str
    python_implementation: str
    operating_system: str
    operating_system_release: str
    machine: str
    smoke_test_output: str
    libraries: tuple[LibraryVersion, ...]

    @classmethod
    def capture(
        cls,
        libraries: tuple[LibraryVersion, ...],
        smoke_test_output: str,
    ) -> "EnvironmentReport":
        try:
            package_version = version("in-silico")
        except PackageNotFoundError:
            package_version = "not installed"
        return cls(
            package_version,
            platform.python_version(),
            platform.python_implementation(),
            platform.system(),
            platform.release(),
            platform.machine(),
            smoke_test_output,
            libraries,
        )

    def to_json(self) -> str:
        return json.dumps(asdict(self), indent=2, sort_keys=True)
