from in_silico.records import ScientificRecord
from in_silico.validation.ValidationResult import ValidationResult


class RecordValidator:
    def __init__(self, required_fields: tuple[str, ...] = ()) -> None:
        self.required_fields = required_fields

    def validate(self, record: ScientificRecord) -> ValidationResult:
        errors = []
        if not record.identifier.strip():
            errors.append("identifier must not be empty")
        for field_name in self.required_fields:
            if field_name not in record.values:
                errors.append(f"missing required field: {field_name}")
        return ValidationResult(tuple(errors))