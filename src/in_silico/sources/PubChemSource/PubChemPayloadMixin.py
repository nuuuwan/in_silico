class PubChemPayloadMixin:
    def payloads(self, aids, operation, optional=False) -> list[dict]:
        records = []
        for aid in aids:
            payload = self.get(f"assay/aid/{aid}/{operation}/JSON", optional)
            if payload is not None:
                records.append({"AID": aid, "payload": payload})
        return records

    def matching(self, records, activity_types) -> list[dict]:
        matching = []
        allowed = {name.upper() for name in activity_types}
        for record in records:
            table = record["payload"].get("Table", {})
            columns = table.get("Columns", {}).get("Column", [])
            if "Activity Name" not in columns:
                continue
            index = columns.index("Activity Name")
            rows = [
                row
                for row in table.get("Row", [])
                if self.row_matches(row, index, allowed)
            ]
            if rows:
                payload = dict(record["payload"])
                payload["Table"] = dict(table, Row=rows)
                matching.append({"AID": record["AID"], "payload": payload})
        return matching

    def row_matches(self, row, index, allowed) -> bool:
        cells = row.get("Cell", [])
        return len(cells) > index and str(cells[index]).upper() in allowed

    def compound_ids(
        self, activities: list[dict], limit: int
    ) -> tuple[int, ...]:
        values = []
        for activity in activities:
            table = activity["payload"].get("Table", {})
            columns = table.get("Columns", {}).get("Column", [])
            if "CID" not in columns:
                continue
            index = columns.index("CID")
            for row in table.get("Row", []):
                cells = row.get("Cell", [])
                if len(cells) > index and cells[index] is not None:
                    values.append(cells[index])
        return tuple(dict.fromkeys(values))[:limit]

    def compounds(self, cids) -> list[dict]:
        if not cids:
            return []
        joined = ",".join(str(cid) for cid in cids)
        payload = self.get(f"compound/cid/{joined}/record/JSON")
        return payload.get("PC_Compounds", [])
