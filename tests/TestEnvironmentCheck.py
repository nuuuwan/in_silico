import json
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase

from in_silico import (
    EnvironmentCheck,
    RecordPropertyCalculator,
    ScientificRecord,
)


class TestEnvironmentCheck(TestCase):
    def test_run_records_environment_and_verifies_workflow(self) -> None:
        with TemporaryDirectory() as directory:
            output_path = Path(directory) / "smoke-test.json"
            report = EnvironmentCheck.run(output_path)

        self.assertTrue(report.package_version)
        self.assertTrue(report.python_version)
        self.assertTrue(report.python_implementation)
        self.assertTrue(report.operating_system)
        self.assertTrue(report.operating_system_release)
        self.assertTrue(report.machine)
        self.assertEqual(report.smoke_test_output, str(output_path.resolve()))
        self.assertEqual(report.libraries, ())

    def test_main_prints_json_report(self) -> None:
        output = StringIO()

        with TemporaryDirectory() as directory:
            original_path = EnvironmentCheck.DEFAULT_OUTPUT_PATH
            EnvironmentCheck.DEFAULT_OUTPUT_PATH = (
                Path(directory) / "result.json"
            )
            try:
                with redirect_stdout(output):
                    exit_code = EnvironmentCheck.main()
            finally:
                EnvironmentCheck.DEFAULT_OUTPUT_PATH = original_path

        report = json.loads(output.getvalue())
        self.assertEqual(exit_code, 0)
        self.assertEqual(report["libraries"], [])
        self.assertIn("python_version", report)

    def test_smoke_test_output_is_deterministic(self) -> None:
        with TemporaryDirectory() as directory:
            first_path = Path(directory) / "first.json"
            second_path = Path(directory) / "second.json"
            EnvironmentCheck.run(first_path)
            EnvironmentCheck.run(second_path)

            self.assertEqual(first_path.read_bytes(), second_path.read_bytes())

    def test_public_property_calculator_counts_record_values(self) -> None:
        record = ScientificRecord("example", {"first": 1, "second": 2})

        result = RecordPropertyCalculator.calculate(record)

        self.assertEqual(result.name, "record_value_count")
        self.assertEqual(result.value, 2)
