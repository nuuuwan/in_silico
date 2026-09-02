import json
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase
from unittest.mock import patch

from in_silico.sources.BioactivityPaths import BioactivityPaths
from tools.sources.FetchBioactivity import FetchBioactivity


class TestFetchBioactivity(TestCase):
    def test_existing_manifest_prints_output(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            paths = BioactivityPaths(
                "dengue virus", ("chembl",), ("IC50", "EC50", "CC50"), 25
            )
            manifest = root / paths.output_dir.name / paths.manifest.name
            manifest.parent.mkdir()
            manifest.write_text(
                json.dumps(self.manifest()),
                encoding="utf-8",
            )
            arguments = [
                "fetch_bioactivity.py",
                "--sources",
                "chembl",
                "--query",
                "dengue virus",
                "--activity-types",
                "IC50,EC50,CC50",
            ]

            with (
                patch.object(BioactivityPaths, "ROOT", root),
                patch("sys.argv", arguments),
                patch("builtins.print") as output,
            ):
                result = FetchBioactivity.main()

            self.assertEqual(result, 0)
            output.assert_called_once_with(self.expected_output(manifest))

    def test_inputs_select_distinct_default_directories(self) -> None:
        baseline = self.paths("dengue virus", ("IC50",))
        query = self.paths("zika virus", ("IC50",))
        activity = self.paths("dengue virus", ("EC50",))
        source = BioactivityPaths("dengue virus", ("pubchem",), ("IC50",), 25)
        limit = BioactivityPaths("dengue virus", ("chembl",), ("IC50",), 10)

        self.assertNotEqual(baseline.output_dir, query.output_dir)
        self.assertNotEqual(baseline.output_dir, activity.output_dir)
        self.assertNotEqual(baseline.output_dir, source.output_dir)
        self.assertNotEqual(baseline.output_dir, limit.output_dir)

    def paths(self, query: str, activity_types: tuple[str, ...]):
        return BioactivityPaths(query, ("chembl",), activity_types, 25)

    def manifest(self) -> dict:
        return {
            "query": "dengue virus",
            "activity_types": ["IC50", "EC50", "CC50"],
            "retrieved_at": "2026-09-02T08:05:01+00:00",
            "sources": [{"name": "ChEMBL"}, {"name": "PubChem"}],
            "snapshots": [
                {"source": "chembl", "entity": "targets", "records": 25},
                {"source": "chembl", "entity": "activities", "records": 25},
                {"source": "pubchem", "entity": "targets", "records": 1},
            ],
        }

    def expected_output(self, path: Path) -> str:
        return (
            "Bioactivity search: dengue virus\n"
            "Activity types: IC50, EC50, CC50\n"
            "Retrieved: 2026-09-02T08:05:01+00:00\n\n"
            "ChEMBL: 50 records\n"
            "  25 targets, 25 activities\n\n"
            f"Wrote 50 records and {path}"
        )
