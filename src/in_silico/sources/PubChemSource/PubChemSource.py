from time import monotonic, sleep

import requests

from in_silico.sources.PubChemSource.PubChemPayloadMixin import (
    PubChemPayloadMixin,
)
from in_silico.sources.PubChemSource.PubChemSearchMixin import (
    PubChemSearchMixin,
)
from in_silico.sources.SourceRecords import SourceRecords


class PubChemSource(PubChemSearchMixin, PubChemPayloadMixin):
    NAME = "pubchem"
    BASE_URL = "https://pubchem.ncbi.nlm.nih.gov/rest/pug"

    def __init__(self, session=None, delay: float = 0.2) -> None:
        self.session = session or requests.Session()
        self.delay = delay
        self.requests = []
        self.last_request = 0.0

    def fetch(
        self, query: str, activity_types: tuple[str, ...], limit: int
    ) -> SourceRecords:
        targets = self.taxonomies(query, limit)
        linked_aids = self.assay_ids(targets)
        aids = self.matching_assay_ids(linked_aids, activity_types, limit)
        assays = self.payloads(aids, "summary")
        activities = self.matching(
            self.payloads(aids, "concise"), activity_types
        )
        matching_aids = tuple(record["AID"] for record in activities)
        dose_responses = self.payloads(
            matching_aids, "doseresponse", optional=True
        )
        cids = self.compound_ids(activities, limit)
        records = {
            "targets": targets,
            "assays": assays,
            "molecules": self.compounds(cids),
            "activities": activities,
            "dose_responses": dose_responses,
        }
        return SourceRecords(
            self.NAME,
            records,
            tuple(self.requests),
            "PUG REST",
        )

    def get(self, path: str, optional: bool = False):
        elapsed = monotonic() - self.last_request
        if elapsed < self.delay:
            sleep(self.delay - elapsed)
        response = self.session.get(f"{self.BASE_URL}/{path}", timeout=60)
        self.last_request = monotonic()
        self.requests.append(response.url)
        if optional and response.status_code == 404:
            return None
        response.raise_for_status()
        return response.json()
