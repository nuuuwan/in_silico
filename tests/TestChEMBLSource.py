from types import SimpleNamespace
from unittest import TestCase
from unittest.mock import Mock

from in_silico import ChEMBLSource


class TestChEMBLSource(TestCase):
    def test_search_follows_source_relationships(self) -> None:
        client, expected = self.client()

        result = ChEMBLSource(client).fetch("dengue virus", ("IC50",), 10)

        for entity, records in expected.items():
            self.assertEqual(result.records[entity], records)
        self.assertIn("database 36", result.version)
        client.assay.filter.assert_called_once_with(
            target_chembl_id__in=("CHEMBLT1",)
        )
        client.activity.filter.assert_called_once_with(
            assay_chembl_id__in=("CHEMBLA1",),
            standard_type__in=("IC50",),
        )

    def client(self) -> tuple[SimpleNamespace, dict]:
        target = {"target_chembl_id": "CHEMBLT1", "pref_name": "Dengue"}
        assay = {
            "assay_chembl_id": "CHEMBLA1",
            "target_chembl_id": "CHEMBLT1",
        }
        activity = {
            "assay_chembl_id": "CHEMBLA1",
            "molecule_chembl_id": "CHEMBLM1",
            "activity_id": 17,
            "standard_type": "IC50",
            "standard_value": "3.0",
        }
        molecule = {"molecule_chembl_id": "CHEMBLM1"}
        dose_response = {"activity_id": 17, "type": "Hill slope"}
        client = SimpleNamespace(
            target=Mock(),
            assay=Mock(),
            activity=Mock(),
            molecule=Mock(),
            chembl_release=Mock(),
            activity_supplementary_data_by_activity=Mock(),
        )
        client.target.search.return_value = [target]
        client.assay.filter.return_value = [assay]
        client.activity.filter.return_value = [activity]
        client.molecule.filter.return_value = [molecule]
        supplementary = client.activity_supplementary_data_by_activity
        supplementary.filter.return_value = [dose_response]
        client.chembl_release.all.return_value = [{"chembl_release": "36"}]
        expected = {
            "targets": [target],
            "assays": [assay],
            "activities": [activity],
            "molecules": [molecule],
            "dose_responses": [dose_response],
        }
        return client, expected
