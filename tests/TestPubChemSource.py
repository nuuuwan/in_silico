from unittest import TestCase
from unittest.mock import Mock

from in_silico import PubChemSource


class TestPubChemSource(TestCase):
    def test_search_filters_activity_and_preserves_links(self) -> None:
        session, compounds = self.session()

        result = PubChemSource(session, delay=0).fetch(
            "dengue virus", ("IC50",), 10
        )

        rows = result.records["activities"][0]["payload"]["Table"]["Row"]
        self.assertEqual(rows, [{"Cell": [11, "IC50"]}])
        self.assertEqual(
            result.records["molecules"], compounds["PC_Compounds"]
        )
        self.assertEqual(result.records["dose_responses"][0]["AID"], 7)
        first_url = session.get.call_args_list[0].args[0]
        last_url = session.get.call_args_list[-1].args[0]
        self.assertIn("taxonomy/synonym/dengue%20virus", first_url)
        self.assertIn("compound/cid/11/record", last_url)

    def session(self) -> tuple[Mock, dict]:
        taxonomy = {
            "TaxonomySummaries": {"TaxonomySummary": [{"TaxonomyID": 12637}]}
        }
        aids = {
            "InformationList": {
                "Information": [{"TaxonomyID": 12637, "AID": [7]}]
            }
        }
        endpoint_aids = {"IdentifierList": {"AID": [7, 8]}}
        summary = {"AssaySummaries": [{"AID": 7}]}
        concise = {
            "Table": {
                "Columns": {"Column": ["CID", "Activity Name"]},
                "Row": [
                    {"Cell": [11, "IC50"]},
                    {"Cell": [12, "Ki"]},
                ],
            }
        }
        dose = {"Table": {"Row": [{"Cell": [11, 0.1, 20]}]}}
        compounds = {"PC_Compounds": [{"id": {"id": {"cid": 11}}}]}
        payloads = [
            taxonomy,
            aids,
            endpoint_aids,
            summary,
            concise,
            dose,
            compounds,
        ]
        responses = [
            self.response(payload, index)
            for index, payload in enumerate(payloads)
        ]
        session = Mock()
        session.get.side_effect = responses
        return session, compounds

    @staticmethod
    def response(payload: dict, index: int) -> Mock:
        response = Mock()
        response.url = f"https://pubchem.example/{index}"
        response.status_code = 200
        response.json.return_value = payload
        return response
