import hashlib
import json
import re
from pathlib import Path


class BioactivityPaths:
    ROOT = Path("data/raw")

    def __init__(
        self,
        query: str,
        sources: tuple[str, ...],
        activity_types: tuple[str, ...],
        limit: int,
    ) -> None:
        request = {
            "query": query.strip().casefold(),
            "sources": sorted(source.casefold() for source in sources),
            "activity_types": sorted(name.upper() for name in activity_types),
            "limit": limit,
        }
        encoded = json.dumps(request, sort_keys=True).encode()
        digest = hashlib.sha256(encoded).hexdigest()[:12]
        slug = re.sub(r"[^a-z0-9]+", "-", request["query"]).strip("-")
        self.output_dir = self.ROOT / f"{slug or 'search'}-{digest}"
        self.manifest = self.output_dir / "bioactivity.manifest.json"
