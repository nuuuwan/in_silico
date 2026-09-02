from in_silico.records import ScientificRecord
from in_silico.validation import RecordValidator


class Workflow:
    def __init__(self, validator: RecordValidator) -> None:
        self.validator = validator

    def run(self, record: ScientificRecord) -> ScientificRecord:
        result = self.validator.validate(record)
        if not result.is_valid:
            raise ValueError("; ".join(result.errors))
        return record
