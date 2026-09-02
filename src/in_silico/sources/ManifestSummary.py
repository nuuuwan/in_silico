from pathlib import Path


class ManifestSummary:
    ENTITY_NAMES = {
        "targets": ("target", "targets"),
        "assays": ("assay", "assays"),
        "molecules": ("molecule", "molecules"),
        "activities": ("activity", "activities"),
        "dose_responses": ("dose response", "dose responses"),
    }

    def __init__(
        self, manifest: dict, path: Path, sources: tuple[str, ...]
    ) -> None:
        self.manifest = manifest
        self.path = path
        self.sources = sources

    def render(self) -> str:
        grouped = self.grouped_snapshots()
        lines = [
            f"Bioactivity search: {self.manifest['query']}",
            "Activity types: " + ", ".join(self.manifest["activity_types"]),
            f"Retrieved: {self.manifest['retrieved_at']}",
            "",
        ]
        for source, snapshots in grouped.items():
            lines.extend(self.source_lines(source, snapshots))
        count = sum(
            item["records"]
            for snapshots in grouped.values()
            for item in snapshots
        )
        lines.append(f"Wrote {count} records and {self.path}")
        return "\n".join(lines)

    def grouped_snapshots(self) -> dict[str, list[dict]]:
        grouped = {}
        for snapshot in self.manifest["snapshots"]:
            if snapshot["source"] not in self.sources:
                continue
            grouped.setdefault(snapshot["source"], []).append(snapshot)
        return grouped

    def source_lines(self, source: str, snapshots: list[dict]) -> list[str]:
        name = self.source_names().get(source, source.title())
        details = ", ".join(self.record_count(item) for item in snapshots)
        total = sum(item["records"] for item in snapshots)
        return [f"{name}: {total} records", f"  {details}", ""]

    def record_count(self, snapshot: dict) -> str:
        count = snapshot["records"]
        names = self.ENTITY_NAMES[snapshot["entity"]]
        return f"{count} {names[count != 1]}"

    def source_names(self) -> dict[str, str]:
        return {
            source["name"].lower(): source["name"]
            for source in self.manifest["sources"]
        }
