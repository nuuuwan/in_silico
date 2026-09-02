from pathlib import Path
from unittest import TestCase

from in_silico import Configuration


class TestConfiguration(TestCase):
    def test_project_paths_are_explicit(self) -> None:
        configuration = Configuration(Path("/project"))

        self.assertEqual(configuration.data_path, Path("/project/data"))
        self.assertEqual(
            configuration.research_path,
            Path("/project/research"),
        )
        self.assertEqual(configuration.results_path, Path("/project/results"))
        self.assertEqual(configuration.tests_path, Path("/project/tests"))
