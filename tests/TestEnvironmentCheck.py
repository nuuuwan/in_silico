import json
from contextlib import redirect_stdout
from io import StringIO
from unittest import TestCase

from in_silico import EnvironmentCheck


class TestEnvironmentCheck(TestCase):
    def test_run_records_environment_and_verifies_workflow(self) -> None:
        report = EnvironmentCheck.run()

        self.assertTrue(report.package_version)
        self.assertTrue(report.python_version)
        self.assertTrue(report.python_implementation)
        self.assertTrue(report.operating_system)
        self.assertTrue(report.operating_system_release)
        self.assertTrue(report.machine)
        self.assertEqual(report.libraries, ())

    def test_main_prints_json_report(self) -> None:
        output = StringIO()

        with redirect_stdout(output):
            exit_code = EnvironmentCheck.main()

        report = json.loads(output.getvalue())
        self.assertEqual(exit_code, 0)
        self.assertEqual(report["libraries"], [])
        self.assertIn("python_version", report)
