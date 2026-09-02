from in_silico.properties.CalculatedProperty import CalculatedProperty
from in_silico.records import ScientificRecord


class RecordPropertyCalculator:
    @staticmethod
    def calculate(record: ScientificRecord) -> CalculatedProperty:
        return CalculatedProperty("record_value_count", len(record.values))
