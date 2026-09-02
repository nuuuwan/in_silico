import argparse
from pathlib import Path

from in_silico import BioactivityFetcher


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
        parser.add_argument("--output-dir", type=Path, required=True)
        parser.add_argument("--manifest", type=Path, required=True)
        parser.add_argument("--limit", type=int, default=25)
        return parser

    @classmethod
    def main(cls) -> int:
        parser = cls.parser()
        arguments = parser.parse_args()
        sources = cls.split(arguments.sources)
        activity_types = cls.split(arguments.activity_types)
        try:
            manifest = BioactivityFetcher().fetch(
                sources,
                arguments.query,
                activity_types,
                arguments.output_dir,
                arguments.manifest,
                arguments.limit,
            )
        except (FileExistsError, ValueError) as error:
            parser.error(str(error))
        count = sum(item["records"] for item in manifest["snapshots"])
        print(f"Wrote {count} records and {arguments.manifest}")
        return 0

    @classmethod
    def split(cls, value: str) -> tuple[str, ...]:
        return tuple(item.strip() for item in value.split(",") if item.strip())
