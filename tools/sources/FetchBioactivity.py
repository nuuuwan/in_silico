import argparse
import json
from pathlib import Path

from in_silico import BioactivityFetcher
from in_silico.sources.BioactivityPaths import BioactivityPaths
from in_silico.sources.ManifestSummary import ManifestSummary


class FetchBioactivity:
    @classmethod
    def parser(cls) -> argparse.ArgumentParser:
        parser = argparse.ArgumentParser(
            description=(
                "Search ChEMBL and PubChem, then preserve linked raw records."
            )
        )
        parser.add_argument("--sources", default="chembl,pubchem")
        parser.add_argument("--query", required=True)
        parser.add_argument("--activity-types", required=True)
        parser.add_argument("--limit", type=int, default=25)
        return parser

    @classmethod
    def main(cls) -> int:
        parser = cls.parser()
        arguments = parser.parse_args()
        sources = cls.split(arguments.sources)
        activity_types = cls.split(arguments.activity_types)
        paths = BioactivityPaths(
            arguments.query, sources, activity_types, arguments.limit
        )
        if paths.manifest.exists():
            cls.print_output(
                json.loads(paths.manifest.read_text(encoding="utf-8")),
                paths.manifest,
                sources,
            )
            return 0
        try:
            manifest = BioactivityFetcher().fetch(
                sources,
                arguments.query,
                activity_types,
                paths.output_dir,
                paths.manifest,
                arguments.limit,
            )
        except (FileExistsError, ValueError) as error:
            parser.error(str(error))
        cls.print_output(manifest, paths.manifest, sources)
        return 0

    @classmethod
    def split(cls, value: str) -> tuple[str, ...]:
        return tuple(item.strip() for item in value.split(",") if item.strip())

    @classmethod
    def print_output(
        cls, manifest: dict, path: Path, sources: tuple[str, ...]
    ) -> None:
        print(ManifestSummary(manifest, path, sources).render())
