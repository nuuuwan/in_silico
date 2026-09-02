from pathlib import Path
from unittest import TestCase

from in_silico import (
    Configuration,
    Provenance,
    RecordValidator,
    ScientificRecord,
    Workflow,
)


class TestPublicApi(TestCase):
    def test_valid_record_runs_through_workflow(self) -> None:
        configuration = Configuration(Path("/project"))
        provenance = Provenance("example", "compound-1")
        record = ScientificRecord(
            "compound-1",
            {"smiles": "CCO"},
            provenance,
        )
        workflow = Workflow(RecordValidator(("smiles",)))

        self.assertEqual(configuration.resolve("data"), Path("/project/data"))
        self.assertIs(workflow.run(record), record)

    def test_invalid_record_is_rejected(self) -> None:
        record = ScientificRecord("", {})
        workflow = Workflow(RecordValidator(("smiles",)))

        with self.assertRaisesRegex(
            ValueError, "identifier must not be empty"
        ):
            workflow.run(record)
