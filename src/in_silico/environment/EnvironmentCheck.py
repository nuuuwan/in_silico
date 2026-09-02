import sys

from in_silico.environment.EnvironmentReport import EnvironmentReport
from in_silico.environment.LibraryVersion import LibraryVersion
from in_silico.records import ScientificRecord
from in_silico.validation import RecordValidator
from in_silico.workflows import Workflow


class EnvironmentCheck:
    REQUIRED_LIBRARIES: tuple[str, ...] = ()

    @classmethod
    def run(cls) -> EnvironmentReport:
        cls._verify_workflow()
        libraries = tuple(
            LibraryVersion.capture(name) for name in cls.REQUIRED_LIBRARIES
        )
        missing = [
            library.name for library in libraries if not library.is_available
        ]
        if missing:
            raise RuntimeError(f"missing required libraries: {
                    ', '.join(missing)}")
        return EnvironmentReport.capture(libraries)

    @staticmethod
    def _verify_workflow() -> None:
        record = ScientificRecord("environment-check", {"status": "ok"})
        Workflow(RecordValidator(("status",))).run(record)

    @classmethod
    def main(cls) -> int:
        try:
            report = cls.run()
        except Exception as error:
            print(f"environment check failed: {error}", file=sys.stderr)
            return 1
        print(report.to_json())
        return 0
