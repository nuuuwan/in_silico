# In Silico Drug Discovery (`in_silico`)

[![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![RDKit](https://img.shields.io/badge/RDKit-Cheminformatics-2C8EBB)](https://www.rdkit.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Author: nuuuwan](https://img.shields.io/badge/Author-nuuuwan-181717?logo=github&logoColor=white)](https://github.com/nuuuwan)

This project builds `in_silico`, a Python library for exploring early-stage drug-discovery hypotheses: using computers to organize chemical and biological evidence, compare compounds, and prioritize candidates before laboratory testing.

The library will use chemical data, molecular structures, and simple machine-learning methods to identify compounds that may be worth investigating for diseases relevant to Sri Lanka, beginning with dengue. It will grow incrementally from foundational molecular representations to a transparent ranked list of promising compounds.

The intended learner is an experienced programmer and computer scientist who is new to biology and pharmacology. The project therefore emphasizes biological concepts, scientific terminology, experimental evidence, and the assumptions behind computational methods. Programming work is organized as production-quality library design, APIs, data models, workflows, validation, testing, and documentation rather than general programming instruction.

This is an educational research project. Computational results do not prove that a compound is safe or effective. They generate hypotheses for future laboratory research and must be confirmed through appropriate experiments.

## Public API

The supported API is exported from `in_silico`:

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

Implementations are separated into `configuration`, `provenance`, `records`,
`validation`, `workflows`, and `environment` packages under `src/in_silico/`.

## Environment check

Install the package, then run its minimum supported workflow and print a JSON
environment report:

```bash
python3 -m pip install -e .
environment_check
```

The report records the package and Python versions, Python implementation,
operating system and release, machine architecture, and versions of all required
runtime libraries. The current foundation has no required scientific libraries,
so `libraries` is empty until those dependencies are introduced.

The command also writes `environment_check_smoke_test.json`. This deterministic
artifact proves that the public API can construct and validate a scientific
record, calculate its `record_value_count` property, and write a result file.

Before running the smoke test, the command checks required libraries and output
capabilities. Failures identify what is missing and how to recover.

## Project paths

`Configuration` derives stable paths from an explicit project root:

```python
from pathlib import Path

from in_silico import Configuration

configuration = Configuration(Path("/path/to/project"))
configuration.data_path
configuration.research_path
configuration.results_path
configuration.tests_path
```

These properties always refer to `data/`, `research/`, `results/`, and `tests/`
under the chosen root. They do not depend on the process's working directory.

## Documents

- [Roadmap](docs/roadmap.md)
