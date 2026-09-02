import hashlib
import json
from pathlib import Path

from in_silico.sources.SnapshotWriter.SnapshotManifestMixin import (
    SnapshotManifestMixin,
)
from in_silico.sources.SourceRecords import SourceRecords


class SnapshotWriter(SnapshotManifestMixin):
    def ensure_available(self, output_dir: Path, manifest: Path) -> None:
        if manifest.exists():
            raise FileExistsError(f"manifest already exists: {manifest}")

    def write(
        self,
        results: list[SourceRecords],
        output_dir: Path,
        manifest: Path,
        query: str,
        activity_types: tuple[str, ...],
        retrieved_at: str,
    ) -> dict:
        self.ensure_available(output_dir, manifest)
        self.ensure_snapshot_paths(results, output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        snapshots = []
        for result in results:
            snapshots.extend(self.write_source(result, output_dir))
        document = self.document(
            results,
            snapshots,
            query,
            activity_types,
            retrieved_at,
        )
        manifest.parent.mkdir(parents=True, exist_ok=True)
        manifest.write_text(
            json.dumps(document, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        return document

    def ensure_snapshot_paths(self, results, output_dir) -> None:
        for result in results:
            for entity in result.records:
                path = output_dir / f"{result.source}_{entity}.jsonl"
                if path.exists():
                    raise FileExistsError(
                        f"raw snapshot already exists: {path}"
                    )

    def write_source(self, result, output_dir) -> list[dict]:
        snapshots = []
        for entity, records in result.records.items():
            content = "".join(
                json.dumps(record, sort_keys=True) + "\n"
                for record in records
            ).encode()
            path = output_dir / f"{result.source}_{entity}.jsonl"
            with path.open("xb") as output:
                output.write(content)
            snapshots.append(
                {
                    "source": result.source,
                    "entity": entity,
                    "path": str(path),
                    "records": len(records),
                    "sha256": hashlib.sha256(content).hexdigest(),
                }
            )
        return snapshots
