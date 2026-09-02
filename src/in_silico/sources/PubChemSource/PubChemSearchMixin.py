from urllib.parse import quote


class PubChemSearchMixin:
    def taxonomies(self, query: str, limit: int) -> list[dict]:
        path = f"taxonomy/synonym/{quote(query, safe='')}/summary/JSON"
        payload = self.get(path)
        summaries = payload.get("TaxonomySummaries", {})
        return summaries.get("TaxonomySummary", [])[:limit]

    def assay_ids(self, targets: list[dict]) -> tuple[int, ...]:
        aids = []
        for target in targets:
            tax_id = target.get("TaxonomyID")
            if tax_id:
                payload = self.get(f"taxonomy/taxid/{tax_id}/aids/JSON")
                information = payload.get("InformationList", {}).get(
                    "Information", []
                )
                for item in information:
                    aids.extend(item.get("AID", []))
        return tuple(dict.fromkeys(aids))

    def matching_assay_ids(
        self, aids, activity_types, limit
    ) -> tuple[int, ...]:
        matching = set()
        for name in activity_types:
            payload = self.get(f"assay/activity/{quote(name)}/aids/JSON")
            matching.update(payload.get("IdentifierList", {}).get("AID", []))
        return tuple(aid for aid in aids if aid in matching)[:limit]
