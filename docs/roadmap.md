# Roadmap for `in_silico`

## L1 Plan

1. Build the `in_silico` foundation. Establish the package architecture, scientific record types, provenance rules, validation framework, workflow conventions, and biological vocabulary on which every later capability will depend.
2. Add molecular-representation and descriptor capabilities. Expose chemical structures, identifiers, stereochemistry, fingerprints, and calculated properties through stable library APIs suitable for automated downstream analysis.
3. Add dengue-dataset capabilities. Ingest public compound and bioactivity data while preserving assay context, source provenance, data-quality information, and the biological meaning of each measurement.
4. Add molecular-similarity capabilities. Enable users to generate fingerprints, find structurally similar compounds, inspect nearest neighbors, and assess when structural similarity does or does not correspond to similar activity.
5. Add prediction and evaluation capabilities. Provide reproducible model-training workflows with scientifically meaningful validation, uncertainty estimates, data-leakage controls, and applicability-domain checks.
6. Add candidate-ranking and reporting capabilities. Combine evidence quality, similarity, predictions, and uncertainty into transparent rankings that inform research decisions without overstating the strength of computational evidence.

Each L1 stage has a concrete library goal and should leave the package more capable than in the preceding stage. Only L1 stage 1 is specified at L2 and L3 below. Later stages remain outcome-level milestones until preceding work clarifies their exact scope and data requirements.

# L2 and L3 Plan

## 1 Build the `in_silico` foundation

Provide a stable foundation for representing scientific records, running deterministic workflows, validating inputs, tracking provenance, and interpreting the biological context of dengue drug discovery.

The output of 1.1 is a usable, versioned `in_silico` package accompanied by research notes that provide the biological context required for later features.

### 1.1 Establish the package structure and reproducible execution baseline

- [x] 1.1.1. [Python] Define the initial `in_silico` package layout under `src/in_silico/`, separating configuration, records, provenance, validation, and workflow execution behind a clear public API.
- [x] 1.1.2. [Research] Write `research/in-silico-drug-discovery-overview.md`, giving later implementation work a shared account of the drug-discovery process and its evidence standards.
- [x] 1.1.3. [Research] Explain target identification, hit discovery, hit-to-lead work, preclinical evaluation, and clinical evaluation so that each project capability can be placed in the wider pipeline.
- [x] 1.1.4. [Python] Create an `environment_check` command-line entry point that verifies whether the package can perform its minimum supported workflow.
- [x] 1.1.5. [Python] Record the Python version, operating-system details, and versions of all required scientific libraries so that a run can be reproduced and diagnosed.

- [x] 1.1.6. [Research] Distinguish computational hypotheses, in vitro results, in vivo results, and clinical evidence to prevent claims from exceeding the evidence supporting them.
- [x] 1.1.7. [Python] Make `environment_check` run a deterministic smoke test through the public API by constructing a scientific record, calculating one property, and writing an output file.
- [x] 1.1.8. [Research] Explain where cheminformatics, molecular docking, molecular dynamics, and machine learning fit in the pipeline, including what each method can and cannot establish about clinical efficacy.
- [x] 1.1.9. [Python] Add tests that identify missing dependencies or capabilities with actionable failure messages instead of allowing obscure downstream errors.
- [x] 1.1.10. [Python] Define package-level configuration for `data/`, `research/`, `results/`, and `tests/` so that paths remain explicit and reproducible across environments.

- [ ] 1.1.11. [Research] Add a glossary and a References section using open, public, authoritative sources, with a source and access date for every important claim.
- [ ] 1.1.12. [Python] Document the public API boundary and the commands required to reproduce package behavior, while treating package installation as supporting setup rather than a learning objective.

### 1.2 Build a biological vocabulary for dengue and antiviral discovery

- [ ] 1.2.1. [Research] Write `research/dengue-biology.md`, establishing the biological vocabulary and disease context required to interpret dengue-focused data and models.
- [ ] 1.2.2. [Research] Describe dengue virus classification, genome organization, structural and non-structural proteins, replication, host-cell entry, and disease course as a foundation for later target selection.
- [ ] 1.2.3. [Python] Add typed glossary and biological-entity models with fields such as `term`, `definition`, `entity_type`, `source`, and `related_terms`, allowing biological knowledge to be stored consistently.
- [ ] 1.2.4. [Research] Explain serotypes, primary and secondary infection, antibody-dependent enhancement, and the biological factors that complicate disease severity and antiviral efficacy.
- [ ] 1.2.5. [Research] Describe the roles of viral proteins examined in antiviral research, clearly separating established biological functions from proposed therapeutic targets.

- [ ] 1.2.6. [Python] Add validation and serialization for glossary records, exporting a stable table to `research/glossary.csv` or `data/glossary.csv` for reuse by people and software.
- [ ] 1.2.7. [Research] Distinguish biological targets, binding sites, mechanisms of action, and measurable phenotypes so that these concepts are not conflated in records or analyses.
- [ ] 1.2.8. [Python] Add a public search and filtering API that retrieves terms by entity type, including viruses, proteins, cells, assays, compounds, and clinical concepts.
- [ ] 1.2.9. [Research] Support the note with open, public sources from health agencies, public databases, reviews, and accessible primary research so that its claims are traceable.
- [ ] 1.2.10. [Python] Test duplicate terms, missing definitions, invalid entity types, serialization, and search behavior to enforce the glossary contract.

### 1.3 Represent molecules and biological entities as data

- [ ] 1.3.1. [Research] Write `research/chemical-and-biological-representation.md`, defining how the project will represent molecular identity and biological entities without hiding important ambiguity.
- [ ] 1.3.2. [Research] Explain atoms, bonds, formal charge, stereochemistry, tautomers, protonation states, salts, mixtures, and molecular identity at the level needed to interpret cheminformatics records.
- [ ] 1.3.3. [Python] Add a molecular-record module that parses SMILES with RDKit and returns clear, structured errors for invalid input.
- [ ] 1.3.4. [Research] Explain SMILES, InChI, compound and protein identifiers, amino-acid sequences, and three-dimensional structures so that each representation’s purpose is explicit.
- [ ] 1.3.5. [Python] Convert between SMILES and RDKit molecular objects, render structure images, and preserve both original and canonical representations when they serve different provenance needs.

- [ ] 1.3.6. [Research] Explain why different textual representations can denote the same chemical entity and why structurally similar molecules can exhibit different biological behavior.
- [ ] 1.3.7. [Python] Add data models for compounds, proteins or targets, assays, and sources so that related chemical and biological evidence can be represented together.
- [ ] 1.3.8. [Python] Represent identifiers, provenance, missing values, and one-to-many relationships explicitly instead of reducing each chemical record to an isolated string.
- [ ] 1.3.9. [Research] Document the limits of using static molecular records to represent dynamic biological systems, providing interpretive cautions for later analyses.
- [ ] 1.3.10. [Python] Validate invalid SMILES, disconnected structures, duplicate canonical SMILES, and inconsistent identifiers so that unsuitable records are detected before analysis.

### 1.4 Acquire, inspect, and document public scientific data

- [ ] 1.4.1. [Research] Write `research/public-data-sources.md`, describing public sources for compounds, bioactivity, proteins, structures, disease information, and dengue literature that the project could use.
- [ ] 1.4.2. [Research] Compare candidate sources by scientific relevance and practical usability so that later dataset choices are explicit rather than opportunistic.
- [ ] 1.4.3. [Python] Add a data-ingestion workflow that reads a source export or openly licensed fixture, normalizes columns, validates required fields, and records each raw-to-processed transformation.
- [ ] 1.4.4. [Research] Record each source’s scope, identifiers, license or access terms, update behavior, assay context, and known limitations to support reproducible source selection.
- [ ] 1.4.5. [Python] Use pandas to profile schema, data types, missingness, duplicates, units, and categorical values, producing an inspectable summary of the input data.

- [ ] 1.4.6. [Research] Explain why activity values require assay conditions, endpoint definitions, units, organism or cell system, and experimental context before they can be compared.
- [ ] 1.4.7. [Python] Preserve source identifiers, provenance fields, and conflicting values so that normalization never erases uncertainty or source-specific evidence.
- [ ] 1.4.8. [Research] Define inclusion and exclusion rules for public data before assembling the dengue dataset, making selection decisions consistent and auditable.
- [ ] 1.4.9. [Python] Produce a machine-readable data-quality report with row counts, validation failures, and transformation summaries so that every run can be reviewed.
- [ ] 1.4.10. [Python] Make ingestion deterministic and rerunnable from a documented input, yielding equivalent processed data and quality reports on repeated runs.

### 1.5 Calculate and interpret basic molecular properties

- [ ] 1.5.1. [Research] Write `research/molecular-properties-and-interpretation.md`, providing the scientific context required to calculate and interpret basic molecular descriptors responsibly.
- [ ] 1.5.2. [Research] Explain what each property represents, how it is estimated, and how it can influence solubility, permeability, distribution, metabolism, or binding.
- [ ] 1.5.3. [Python] Add an RDKit-based API for molecular weight, hydrogen-bond donors and acceptors, estimated lipophilicity, rotatable bonds, formal charge, and ring counts.
- [ ] 1.5.4. [Python] Handle invalid structures and missing values explicitly, retaining an audit field that makes every calculation failure inspectable.
- [ ] 1.5.5. [Research] Introduce drug-likeness and the appropriate use and limitations of heuristics such as Lipinski’s Rule of Five, preventing filters from being treated as efficacy rules.

- [ ] 1.5.6. [Python] Compare calculated values with known reference compounds and test simple molecules so that descriptor implementations have scientifically plausible checks.
- [ ] 1.5.7. [Research] Distinguish molecular descriptors from biological endpoints and correlation from causation so that calculated properties are not mistaken for biological evidence.
- [ ] 1.5.8. [Python] Store calculated properties in a versioned table without overwriting raw inputs, preserving both reproducibility and data lineage.
- [ ] 1.5.9. [Research] Explain how ionization, pH, salt form, stereochemistry, and computational method affect interpretation, defining caveats for property-based comparisons.
- [ ] 1.5.10. [Python] Flag statistical or chemically unusual values for review without automatically classifying them as errors or deleting them.

### 1.6 Explore the data with reproducible visual analysis

- [ ] 1.6.1. [Research] Write `research/reading-chemical-data.md`, establishing the statistical vocabulary and interpretive safeguards needed for exploratory chemical-data analysis.
- [ ] 1.6.2. [Research] Explain distributions, transformations, normalization, outliers, sampling bias, confounding, and uncertainty in chemical and biological datasets.
- [ ] 1.6.3. [Python] Add a visualization workflow that generates reproducible distributions and pairwise plots from the calculated molecular properties.
- [ ] 1.6.4. [Python] Produce molecular-weight and lipophilicity distributions, a property scatter plot, and at least one comparison across categories or source groups.
- [ ] 1.6.5. [Research] Document valid interpretations and common failure modes for each planned figure so that visual patterns are connected to defensible claims.

- [ ] 1.6.6. [Python] Add labels, units, and reproducible styling, then export figures to `results/` with metadata identifying the exact input-data version.
- [ ] 1.6.7. [Research] Explain how outliers, missing data, and sampling bias can distort conclusions, providing a conceptual basis for the demonstration in the workflow.
- [ ] 1.6.8. [Python] Include a concrete example showing how outliers, missing data, or sampling bias changes a visualization and its apparent conclusion.
- [ ] 1.6.9. [Python] Generate a concise Markdown summary and reproduce the same figures from a clean run, explicitly cautioning that trends in a small compound set are not general pharmacological laws.

### 1.7 Consolidate, test, and document the first milestone

- [ ] 1.7.1. [Research] Write `research/week-1-review.md`, consolidating the scientific understanding, implementation choices, evidence, and limitations established during the first milestone.
- [ ] 1.7.2. [Python] Create one reproducible workflow that runs environment checks, data validation, property calculations, and figure generation in a documented order.
- [ ] 1.7.3. [Research] Summarize the biological concepts learned, computational representations used, assumptions made, and unresolved questions that affect L1 stages 2–6.
- [ ] 1.7.4. [Python] Add tests for the core parsing, validation, property-calculation, and data-export functions so that the milestone’s public behavior is protected.
- [ ] 1.7.5. [Research] Inventory every compound, target, assay, and public source in the initial working set, making the project’s scientific scope explicit.

- [ ] 1.7.6. [Python] Run the workflow in a clean environment and verify that it regenerates all expected outputs without manual intervention.
- [ ] 1.7.7. [Research] Add a limitations section covering data quality, biological uncertainty, model risk, and the distinction between ranking hypotheses and demonstrating therapeutic value.
- [ ] 1.7.8. [Python] Generate a compact report containing environment information, dataset counts, validation results, property summaries, and links to figures for milestone review.
- [ ] 1.7.9. [Research] Link every research note to its references and label statements as background knowledge, evidence-based findings, or project assumptions.
- [ ] 1.7.10. [Python] Record package versions and exact input-data revisions in the report so that its results can be reproduced from the documented state.
