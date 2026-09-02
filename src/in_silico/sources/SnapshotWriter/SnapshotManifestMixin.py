class SnapshotManifestMixin:
    TERMS = {
        "chembl": {
            "name": "ChEMBL",
            "url": "https://www.ebi.ac.uk/chembl/",
            "access_terms": "https://www.ebi.ac.uk/chembl/about",
        },
        "pubchem": {
            "name": "PubChem",
            "url": "https://pubchem.ncbi.nlm.nih.gov/",
            "access_terms": "https://www.ncbi.nlm.nih.gov/home/about/policies/",
        },
    }

    def document(
        self, results, snapshots, query, types, retrieved_at
    ) -> dict:
        sources = []
        for result in results:
            source = dict(self.TERMS[result.source])
            source.update(
                {"version": result.version, "requests": list(result.requests)}
            )
            sources.append(source)
        return {
            "schema_version": 1,
            "retrieved_at": retrieved_at,
            "query": query,
            "activity_types": list(types),
            "transformations": [],
            "sources": sources,
            "snapshots": snapshots,
        }
