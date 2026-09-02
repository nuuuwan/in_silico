import warnings

import requests

with warnings.catch_warnings():
    warnings.filterwarnings(
        "ignore",
        message="pkg_resources is deprecated as an API.*",
        category=UserWarning,
    )
    from chembl_webresource_client.new_client import new_client
    from chembl_webresource_client.settings import Settings

from in_silico.sources.ChEMBLSource.ChEMBLSourceMixin import (
    ChEMBLSourceMixin,
)
from in_silico.sources.SourceRecords import SourceRecords


class ChEMBLSource(ChEMBLSourceMixin):
    NAME = "chembl"
    BASE_URL = "https://www.ebi.ac.uk/chembl/api/data"

    def __init__(self, client=new_client, session=None) -> None:
        Settings.Instance().NEW_CLIENT_TIMEOUT = 60
        self.client = client
        self.session = session or requests.Session()

    def fetch(
        self, query: str, activity_types: tuple[str, ...], limit: int
    ) -> SourceRecords:
        targets = list(self.client.target.search(query)[:limit])
        target_ids = self.ids(targets, "target_chembl_id")
        assays = self.related(
            self.client.assay, "target_chembl_id", target_ids, limit
        )
        assay_ids = self.ids(assays, "assay_chembl_id")
        activities = self.activities(assay_ids, activity_types, limit)
        molecule_ids = self.ids(activities, "molecule_chembl_id")
        molecules = self.related(
            self.client.molecule,
            "molecule_chembl_id",
            molecule_ids,
            limit,
        )
        activity_ids = self.ids(activities, "activity_id")
        records = {
            "targets": targets,
            "assays": assays,
            "molecules": molecules,
            "activities": activities,
            "dose_responses": self.details(activity_ids, limit),
        }
        return SourceRecords(
            self.NAME,
            records,
            self.request_urls(query, activity_types),
            self.source_version(),
        )
