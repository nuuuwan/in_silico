from datetime import datetime, timezone
from pathlib import Path

from in_silico.sources.ChEMBLSource import ChEMBLSource
from in_silico.sources.PubChemSource.PubChemSource import PubChemSource
from in_silico.sources.SnapshotWriter.SnapshotWriter import SnapshotWriter


class BioactivityFetcher:
    def __init__(self, adapters=None, writer=None) -> None:
        self.adapters = adapters or {
            "chembl": ChEMBLSource(),
            "pubchem": PubChemSource(),
        }
        self.writer = writer or SnapshotWriter()

    def fetch(
        self,
        sources: tuple[str, ...],
        query: str,
        activity_types: tuple[str, ...],
        output_dir: Path,
        manifest: Path,
        limit: int,
    ) -> dict:
        self.validate(sources, query, activity_types, limit)
        activity_types = tuple(name.upper() for name in activity_types)
        self.writer.ensure_available(output_dir, manifest)
        results = [
            self.adapters[source].fetch(query, activity_types, limit)
            for source in sources
        ]
        retrieved_at = datetime.now(timezone.utc).isoformat()
        return self.writer.write(
            results,
            output_dir,
            manifest,
            query,
            activity_types,
            retrieved_at,
        )

    def validate(self, sources, query, activity_types, limit) -> None:
        unknown = set(sources) - set(self.adapters)
        if not sources or unknown:
            names = ", ".join(sorted(unknown)) or "none selected"
            raise ValueError(f"unsupported sources: {names}")
        if not query.strip():
            raise ValueError("query must not be empty")
        if not activity_types:
            raise ValueError("at least one activity type is required")
        if limit < 1:
            raise ValueError("limit must be positive")
