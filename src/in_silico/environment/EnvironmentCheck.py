import json
import sys
from dataclasses import asdict
from pathlib import Path

from in_silico.environment.EnvironmentReport import EnvironmentReport
from in_silico.environment.LibraryVersion import LibraryVersion
from in_silico.properties import RecordPropertyCalculator
from in_silico.records import ScientificRecord
from in_silico.validation import RecordValidator
from in_silico.workflows import Workflow


class EnvironmentCheck:
    REQUIRED_LIBRARIES: tuple[str, ...] = ()
    DEFAULT_OUTPUT_PATH = Path("environment_check_smoke_test.json")

    @classmethod
    def run(cls, output_path: Path | None = None) -> EnvironmentReport:
        output_path = output_path or cls.DEFAULT_OUTPUT_PATH
        libraries = cls._verify_libraries()
        cls._verify_output_path(output_path)
        smoke_test_output = cls._run_smoke_test(output_path)
        return EnvironmentReport.capture(libraries, smoke_test_output)

    @classmethod
    def _verify_libraries(cls) -> tuple[LibraryVersion, ...]:
        libraries = tuple(
            LibraryVersion.capture(name) for name in cls.REQUIRED_LIBRARIES
        )
        missing = [
            library.name for library in libraries if not library.is_available
        ]
        if missing:
            names = ", ".join(missing)
            message = (
                f"missing required libraries: {names}. "
                "Install project dependencies and rerun environment_check."
            )
            raise RuntimeError(message)
        return libraries

    @staticmethod
    def _verify_output_path(output_path: Path) -> None:
        parent = output_path.parent
        if not parent.exists():
            message = (
                f"smoke-test output directory does not exist: {parent}. "
                "Create it or choose an output path in an existing directory."
            )
            raise RuntimeError(message)
        if not parent.is_dir():
            message = f"smoke-test output parent is not a directory: {parent}"
            raise RuntimeError(message)

    @staticmethod
    def _run_smoke_test(output_path: Path) -> str:
        record = ScientificRecord("environment-check", {"status": "ok"})
        validated_record = Workflow(RecordValidator(("status",))).run(record)
        calculated_property = RecordPropertyCalculator.calculate(
            validated_record
        )
        result = {
            "property": asdict(calculated_property),
            "record": {
                "identifier": validated_record.identifier,
                "values": validated_record.values,
            },
        }
        content = json.dumps(result, indent=2, sort_keys=True) + "\n"
        output_path.write_text(content, encoding="utf-8")
        return str(output_path.resolve())

    @classmethod
    def main(cls) -> int:
        try:
            report = cls.run()
        except Exception as error:
            print(f"environment check failed: {error}", file=sys.stderr)
            return 1
        print(report.to_json())
        return 0
