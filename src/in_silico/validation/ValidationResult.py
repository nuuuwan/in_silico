from dataclasses import dataclass


@dataclass(frozen=True)
class ValidationResult:
    errors: tuple[str, ...] = ()

    @property
    def is_valid(self) -> bool:
        return not self.errors