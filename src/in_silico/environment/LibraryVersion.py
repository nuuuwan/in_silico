from dataclasses import dataclass
from importlib.metadata import PackageNotFoundError, version


@dataclass(frozen=True)
class LibraryVersion:
    name: str
    version: str | None

    @property
    def is_available(self) -> bool:
        return self.version is not None

    @classmethod
    def capture(cls, name: str) -> "LibraryVersion":
        try:
            library_version = version(name)
        except PackageNotFoundError:
            library_version = None
        return cls(name, library_version)
