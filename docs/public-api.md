# Public API and Reproducible Commands

## Supported boundary

The supported Python API consists of the names exported directly from
`in_silico`. Code using the package should import these names from the package
root:

```python
from in_silico import CalculatedProperty
from in_silico import Configuration
from in_silico import EnvironmentCheck
from in_silico import EnvironmentReport
from in_silico import LibraryVersion
from in_silico import Provenance
from in_silico import RecordPropertyCalculator
from in_silico import RecordValidator
from in_silico import ScientificRecord
from in_silico import ValidationResult
from in_silico import Workflow
```

The `environment_check` command is also public. Modules below the package root,
class file locations, and names absent from this list are implementation details.
They may change without preserving direct submodule imports.

## Public responsibilities

| Name | Responsibility |
| --- | --- |
| `CalculatedProperty` | Stores a named calculated value |
| `Configuration` | Derives standard project paths from an explicit root |
| `EnvironmentCheck` | Runs the smoke test and captures environment information |
| `EnvironmentReport` | Stores and serializes the environment report |
| `LibraryVersion` | Records whether a required library and version are available |
| `Provenance` | Identifies the source of a scientific record |
| `RecordPropertyCalculator` | Calculates the foundation smoke-test property |
| `RecordValidator` | Validates required scientific-record fields |
| `ScientificRecord` | Stores an identifier, values, and optional provenance |
| `ValidationResult` | Reports validation errors and validity |
| `Workflow` | Runs record validation as a workflow step |

## Supporting setup

Installation only makes the package and command available. It is supporting
setup, not a project learning objective:

```bash
python3 -m pip install -e .
```

Python 3.11 or newer is required. Runtime dependencies are declared in
`pyproject.toml`; the current foundation has no external runtime dependencies.

## Reproduce package behavior

From the repository root, run the public smoke test:

```bash
environment_check
```

The command validates a `ScientificRecord`, calculates its
`record_value_count`, writes `environment_check_smoke_test.json`, and prints a
JSON environment report. The artifact is deterministic for the fixed smoke-test
input. The report contains machine-specific Python, operating-system, package,
and library versions for diagnosis.

Run the complete behavior test suite:

```bash
python3 -m unittest discover -s tests -p 'Test*.py' -v
```

The command exits with a nonzero status when a test fails. Together, the smoke
test and test suite reproduce and verify the package behavior established by the
foundation milestone.

## Public API example

```python
from pathlib import Path

from in_silico import Configuration
from in_silico import RecordPropertyCalculator
from in_silico import RecordValidator
from in_silico import ScientificRecord
from in_silico import Workflow

configuration = Configuration(Path("/path/to/project"))
record = ScientificRecord("example", {"status": "ready"})
validated = Workflow(RecordValidator(("status",))).run(record)
calculated = RecordPropertyCalculator.calculate(validated)

assert configuration.results_path == Path("/path/to/project/results")
assert calculated.name == "record_value_count"
assert calculated.value == 1
```
