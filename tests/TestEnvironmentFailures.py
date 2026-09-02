from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase

from in_silico import EnvironmentCheck


class TestEnvironmentFailures(TestCase):
    def test_missing_dependency_explains_how_to_recover(self) -> None:
        original_libraries = EnvironmentCheck.REQUIRED_LIBRARIES
        EnvironmentCheck.REQUIRED_LIBRARIES = ("in-silico-missing-dependency",)
        message = (
            "missing required libraries: in-silico-missing-dependency. "
            "Install project dependencies and rerun environment_check."
        )
        try:
            with self.assertRaisesRegex(RuntimeError, message):
                EnvironmentCheck.run()
        finally:
            EnvironmentCheck.REQUIRED_LIBRARIES = original_libraries

    def test_missing_output_directory_explains_how_to_recover(self) -> None:
        with TemporaryDirectory() as directory:
            output_path = Path(directory) / "missing" / "result.json"
            message = (
                "smoke-test output directory does not exist: .*missing. "
                "Create it or choose an output path in an existing directory."
            )

            with self.assertRaisesRegex(RuntimeError, message):
                EnvironmentCheck.run(output_path)
