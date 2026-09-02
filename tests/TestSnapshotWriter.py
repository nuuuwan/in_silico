import hashlib
import json
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase

from in_silico import SnapshotWriter
from in_silico.sources.SourceRecords import SourceRecords


class TestSnapshotWriter(TestCase):
    def test_writes_checksums_and_refuses_overwrite(self) -> None:
        result = SourceRecords(
            "pubchem",
            {"targets": [{"TaxonomyID": 12637}]},
            ("https://pubchem.example/request",),
            "PUG REST",
        )
        with TemporaryDirectory() as directory:
            root = Path(directory)
            output = root / "raw"
            manifest_path = root / "bioactivity.manifest.json"
            writer = SnapshotWriter()
            manifest = writer.write(
                [result],
                output,
                manifest_path,
                "dengue virus",
                ("IC50",),
                "2026-09-02T00:00:00+00:00",
            )
            snapshot = output / "pubchem_targets.jsonl"
            digest = hashlib.sha256(snapshot.read_bytes()).hexdigest()

            self.assertEqual(manifest["snapshots"][0]["sha256"], digest)
            self.assertEqual(json.loads(manifest_path.read_text()), manifest)
            with self.assertRaises(FileExistsError):
                writer.write(
                    [result],
                    output,
                    manifest_path,
                    "dengue virus",
                    ("IC50",),
                    "2026-09-02T00:00:00+00:00",
                )
