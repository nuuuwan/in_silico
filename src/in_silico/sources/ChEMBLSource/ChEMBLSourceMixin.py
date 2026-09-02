from importlib.metadata import version


class ChEMBLSourceMixin:
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

    def details(self, identifiers, limit) -> list[dict]:
        records = []
        resource = "activity_supplementary_data_by_activity"
        for identifier in identifiers[:limit]:
            url = f"{self.BASE_URL}/{resource}/{identifier}.json"
            response = self.session.get(url, timeout=60)
            if response.status_code == 404:
                continue
            response.raise_for_status()
            records.append(response.json())
        return records

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
            f"{self.BASE_URL}/activity_supplementary_data_by_activity/"
            "<activity-id>.json",
        )
