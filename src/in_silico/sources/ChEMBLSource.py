from importlib.metadata import version

from chembl_webresource_client.new_client import new_client
from chembl_webresource_client.settings import Settings

from in_silico.sources.SourceRecords import SourceRecords


class ChEMBLSource:
    NAME = "chembl"
    BASE_URL = "https://www.ebi.ac.uk/chembl/api/data"

    def __init__(self, client=new_client) -> None:
        Settings.Instance().NEW_CLIENT_TIMEOUT = 60
        self.client = client

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
        dose_responses = self.related(
            self.client.activity_supplementary_data_by_activity,
            "activity_id",
            activity_ids,
            limit,
        )
        records = {
            "targets": targets,
            "assays": assays,
            "molecules": molecules,
            "activities": activities,
            "dose_responses": dose_responses,
        }
        return SourceRecords(
            self.NAME,
            records,
            self.request_urls(query, activity_types),
            self.source_version(),
        )

    def source_version(self) -> str:
        releases = list(self.client.chembl_release.all()[:1])
        release = releases[0] if releases else {}
        database = release.get("chembl_release") or "unknown"
        client = version("chembl_webresource_client")
        return f"database {database}; client {client}"

    def activities(self, assay_ids, activity_types, limit) -> list[dict]:
        if not assay_ids:
            return []
        query = self.client.activity.filter(
            assay_chembl_id__in=assay_ids,
            standard_type__in=activity_types,
        )
        return list(query[:limit])

    def related(self, resource, field, identifiers, limit) -> list[dict]:
        if not identifiers:
            return []
        return list(resource.filter(**{f"{field}__in": identifiers})[:limit])

    def ids(self, records: list[dict], field: str) -> tuple[str, ...]:
        return tuple(
            dict.fromkeys(
                record[field] for record in records if record.get(field)
            )
        )

    def request_urls(self, query, activity_types) -> tuple[str, ...]:
        kinds = ",".join(activity_types)
        return (
            f"{self.BASE_URL}/target/search.json?q={query}",
            f"{self.BASE_URL}/assay?target_chembl_id__in=<searched-targets>",
            f"{self.BASE_URL}/activity?standard_type__in={kinds}",
            f"{self.BASE_URL}/molecule?molecule_chembl_id__in=<activities>",
        )
