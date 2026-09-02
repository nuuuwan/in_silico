# Roadmap for `in_silico`

## L1 Plan

1. Learn how evidence moves through drug discovery. Use Pydantic, pandas, SciPy, statsmodels, NetworkX, and RDFLib to build the first reusable evidence models, assay calculations, uncertainty experiments, and scientific relationship graphs.
2. Learn how computers represent molecules. Use RDKit to explore atoms, bonds, stereochemistry, protonation, identifiers, fingerprints, and molecular descriptors by changing structures and observing how their representations and calculated properties change.
3. Learn dengue biology through data. Use pandas, Biopython, and public scientific formats to connect the viral lifecycle, proteins, host systems, assays, and disease context to real records while learning why provenance and experimental context matter.
4. Learn molecular similarity and its limits. Use RDKit fingerprints and scientific Python tools to inspect nearest neighbors, vary similarity metrics, and discover activity cliffs where structurally similar molecules behave differently.
5. Learn prediction through controlled experiments. Use scikit-learn to train simple models, introduce realistic leakage and bias, compare validation strategies, inspect uncertainty, and learn when a prediction should not be trusted.
6. Learn evidence-based candidate prioritization. Compose the reusable records, descriptors, similarity functions, models, and uncertainty estimates into transparent rankings, then test how different scientific assumptions change the result.

Each L1 stage is a learning milestone expressed through runnable scientific experiments built with the same open-source libraries used by the later system. Early tools should expose small, understandable interfaces while contributing reusable schemas, calculations, parsers, and visualizations to `in_silico`. Package engineering supports the learning goal but is not itself the objective. Only stage 1 is currently expanded to L2, and only section 1.1 is expanded to L3.

# L2 and L3 Plan

## Meta-goals for all L2 and L3 planning

These constraints apply to every L2 section and every current or future L3 task in this roadmap.

- **Use real scientific sources.** Domain data should come from appropriate third-party sources such as ChEMBL, PubChem, UniProt, RCSB PDB, Gene Ontology, or other open authoritative databases. The roadmap must identify the source relevant to each task rather than inventing a local substitute.
- **Never hard-code domain knowledge.** Dengue targets, protein functions, assay definitions, activity values, evidence levels, discovery-stage rules, and terminology must be loaded from retrieved records or versioned, cited data files. Executables may contain algorithms and validation logic, but not hidden scientific facts.
- **Make every output reusable.** Each task must produce at least one artifact consumed by a named later task: an importable function, validated schema, normalized dataset, fitted model, vocabulary, evidence graph, source adapter, or durable test fixture. A tutorial-only program, quiz, static learning page, or one-off report does not qualify.
- **Build on the real library stack.** Use the same third-party libraries intended for later work—such as RDKit, pandas, NumPy, SciPy, statsmodels, scikit-learn, Pydantic, Pandera, Pint, Biopython, NetworkX, and RDFLib—rather than replacing their behavior with simplified teaching implementations.
- **Keep interfaces thin and logic importable.** Files under `tools/` should parse parameters and call code under `src/in_silico/`. Scientific transformations, fitting, validation, graph construction, and decision logic must be available through the package API and independently testable.
- **Preserve provenance.** Retrieved and derived data must retain source identifiers, URLs or database names, licensing or access terms, retrieval timestamps, source versions where available, transformation histories, and checksums. Raw snapshots are immutable; processed outputs never overwrite them.
- **Separate retrieval from analysis.** Networked source adapters create versioned local snapshots. Every analysis tool must be able to rerun from those snapshots without a network connection, so later results do not silently change when a public database updates.
- **Prefer data-driven learning.** Learning should come from interrogating real records, changing explicit parameters, and comparing computed results. Explanatory text supports the tool but is not the deliverable.
- **Expose uncertainty and incompatibility.** Tools must preserve missing values, censoring, conflicting records, assay differences, estimation uncertainty, and model limitations instead of silently resolving them or presenting false precision.
- **Test the scientific contract.** Each reusable component must include tests using small, provenance-preserving slices of public data plus synthetic edge cases where necessary. Tests should cover scientific invariants, units, failure modes, determinism, and round-trip serialization—not only code execution.

## 1 Learn the drug-discovery process and its evidence

Build enough biological and pharmacological understanding to interpret later computations correctly. Learn by changing parameters and observing consequences, but implement each experiment with real scientific libraries and retain its core logic for later data, modeling, and ranking workflows.

### 1.1 Explore the discovery pipeline, assays, and strength of evidence

By the end of 1.1, the learner should be able to place a result in the drug-discovery pipeline, interpret basic potency and toxicity measurements, distinguish evidence levels, recognize an unsupported claim, and choose a sensible next experiment. The code produced should also establish the first reusable scientific models and numerical functions in `src/in_silico/`.

- [x] 1.1.1. [Research + Python] Learn what dengue targets, assays, compounds, and activity measurements look like in real public drug-discovery databases.

  Build source adapters using the official ChEMBL web-resource client and PubChem PUG REST. They search rather than assuming target, compound, or assay identifiers; retrieve matching target, assay, molecule, activity, and available dose–response records; preserve source relationships; and write immutable raw snapshots with retrieval manifests. These adapters become ingestion components for later dataset stages.

  ```bash
  tools/sources/fetch_bioactivity.py --sources chembl,pubchem --query "dengue virus" --activity-types IC50,EC50,CC50
  ```

- [ ] 1.1.2. [Research + Python] Learn how a biological target, binding event, mechanism of action, cellular phenotype, and clinical outcome differ in public scientific records.

  Build source adapters that follow identifiers in the ChEMBL snapshot to UniProt, Gene Ontology, and RCSB PDB, then use RDFLib and NetworkX to assemble the retrieved relationships into a typed evidence graph. Missing links remain missing rather than being filled with built-in biological assertions. The graph becomes the relationship layer used by later target and evidence features.

  ```bash
  tools/evidence/build_graph.py --activities data/raw/chembl_dengue.jsonl --resolve uniprot,quickgo,rcsb --cache-dir data/raw/resolved --manifest data/raw/resolved.manifest.json --output data/processed/dengue_evidence.jsonld
  ```

- [ ] 1.1.3. [Research + Python] Learn the difference between computational hypotheses, biochemical results, cellular results, animal studies, and clinical evidence, and how each relates to discovery-stage progression.

  Create cited, versioned `evidence_levels.yml` and `discovery_stages.yml` data files whose individual definitions retain sources and access dates. Build an evidence classifier backed by Pydantic discriminated unions that loads those files, classifies retrieved records, and returns machine-readable evidence levels, applicable stages, and supported or unsupported claims for later ranking logic.

  ```bash
  tools/evidence/classify.py --input data/processed/dengue_evidence.jsonld --evidence-rules data/reference/evidence_levels.yml --stage-rules data/reference/discovery_stages.yml --output data/processed/classified_evidence.jsonl
  ```

- [ ] 1.1.4. [Research + Python] Learn how scientific claims must be calibrated to the evidence behind them.

  Build a claim checker whose rules operate on the classified public records from 1.1.3. It compares a user-supplied statement with the linked evidence, explains any overreach, and emits structured claim–evidence links that later candidate ranking explanations can reuse.

  ```bash
  tools/evidence/check_claim.py --claim "the selected compound treats dengue" --evidence data/processed/classified_evidence.jsonl --rules data/reference/evidence_levels.yml
  ```

- [ ] 1.1.5. [Research + Python] Learn the anatomy of a dengue antiviral assay: endpoint, virus and serotype, host system, exposure time, controls, replicates, concentration range, and units.

  Build an assay-context extractor using Pydantic for record validation, pandas for tabular inspection, and Pandera for dataset-level checks. It reads the retrieved ChEMBL assay records, measures context completeness, and establishes the assay schema later ingestion code will use. Parameterized omission is applied to copies in memory so the learner can see why each real source field matters without modifying the raw snapshot.

  ```bash
  tools/assays/explore_context.py --input data/raw/chembl_dengue.jsonl --sample-size 20 --omit cell_line --output data/processed/assay_context.parquet
  ```

- [ ] 1.1.6. [Research + Python] Learn what IC50, EC50, CC50, and selectivity index measure and why they are not interchangeable.

  Build an endpoint calculator with NumPy, SciPy, and Matplotlib that reads concentration–response measurements retrieved from a declared public assay source, fits four-parameter logistic models, calculates EC50, CC50, and selectivity index where the input supports them, and returns both figures and reusable numerical results.

  ```bash
  tools/assays/calculate_endpoints.py --input data/raw/pubchem_dose_response.csv --group-by compound_id,endpoint --output data/processed/endpoints.parquet
  ```

- [ ] 1.1.7. [Research + Python] Learn how dose–response curves, replicate variability, and incomplete concentration coverage affect potency estimates.

  Build a dose–response fitting tool with NumPy and SciPy that uses real replicate measurements, fits a four-parameter logistic curve, estimates bootstrap confidence intervals, and diagnoses failure cases such as a missing plateau or excessive noise. Keep fitting, resampling, and diagnostics as importable library functions used by later bioactivity processing.

  ```bash
  tools/assays/fit_dose_response.py --input data/raw/pubchem_dose_response.csv --compound-id-from-row 0 --bootstrap 1000 --seed 42 --output results/dose_response.json
  ```

- [ ] 1.1.8. [Research + Python] Learn what cheminformatics, molecular docking, molecular dynamics, machine learning, biochemical assays, and cellular assays can and cannot answer.

  Build a method-matching sandbox that inspects actual inputs with RDKit for chemical structures, Biopython for sequences or PDB structures, and pandas for bioactivity tables. It ranks only methods whose required data are present and distinguishes their possible outputs from the conclusion the learner hopes to reach.

  ```bash
  tools/methods/select.py --question target-binding --source-manifest data/raw/resolved.manifest.json --bioactivity data/processed/endpoints.parquet --budget low
  ```

- [ ] 1.1.9. [Research + Python] Learn why controls, biological replicates, technical replicates, uncertainty, and reproducibility matter.

  Build a replication analyzer with NumPy and statsmodels that resamples real replicate measurements, estimates effect uncertainty and power, and then lets the learner add explicit batch effects or change sample size. Retain the resampling and power functions for later model evaluation and experimental-design checks.

  ```bash
  tools/statistics/analyze_replicates.py --input data/raw/pubchem_dose_response.csv --group-by compound_id,concentration --bootstrap 1000 --add-batch-effect 0.15 --seed 42
  ```

- [ ] 1.1.10. [Research + Python] Learn why two apparently similar activity measurements may disagree or be impossible to combine.

  Build an assay-comparison tool with pandas and Pint that reads retrieved records, normalizes units and censored values while preserving endpoint, serotype, cell line, and exposure time, and identifies which differences are computationally harmonizable versus biologically meaningful. The harmonizer becomes part of later data ingestion.

  ```bash
  tools/assays/compare.py --input data/raw/chembl_dengue.jsonl --left-id-from-row 0 --right-id-from-row 1 --output results/assay_comparison.json
  ```

- [ ] 1.1.11. [Research + Python] Learn the core vocabulary needed to read dengue drug-discovery papers and datasets without conflating related concepts.

  Build an ontology adapter that retrieves selected terms and relationships from declared public vocabularies such as BAO, EFO, ChEBI, and Gene Ontology through a versioned source manifest. RDFLib resolves and traverses those records; the resulting vocabulary service is used later by validation and search features.

  ```bash
  tools/vocabulary/build.py --sources data/sources/ontologies.yml --terms target,hit,potency,efficacy,activity --output data/reference/drug_discovery_terms.jsonld
  ```

- [ ] 1.1.12. [Research + Python] Apply the section’s concepts to a reproducible slice of the retrieved dengue evidence.

  Build an evidence-evaluation tool that composes the Pydantic evidence models, pandas assay tables, SciPy dose–response fitting, statsmodels uncertainty estimates, and NetworkX evidence graph created earlier. The compound and target are selected from the retrieved snapshot at runtime; changing the chosen records recomputes the supported claim, uncertainty, pipeline position, and next experiment through importable `in_silico` APIs.

  ```bash
  tools/hypotheses/evaluate.py --evidence data/processed/classified_evidence.jsonl --stage-rules data/reference/discovery_stages.yml --candidate-id-from-row 0 --output results/hypothesis_evaluation.json
  ```

### 1.2 Learn the biological vocabulary of dengue and antiviral discovery

Learn the viral lifecycle, genome, proteins, host interactions, disease course, and vocabulary needed to interpret dengue-focused data and models. **L3 planning is intentionally deferred until 1.1 is complete.**

### 1.3 Learn how molecules and biological entities are represented

Explore how molecular identity, proteins, targets, assays, identifiers, relationships, ambiguity, and provenance appear in scientific software and datasets. **L3 planning is intentionally deferred until 1.1 is complete.**

### 1.4 Learn to acquire and critically inspect public scientific data

Learn how source scope, licensing, provenance, assay context, missingness, normalization, and selection rules shape a scientific dataset. **L3 planning is intentionally deferred until 1.1 is complete.**

### 1.5 Learn to calculate and interpret basic molecular properties

Explore what common molecular descriptors measure, how they are calculated, what changes them, and why they are not direct evidence of biological activity. **L3 planning is intentionally deferred until 1.1 is complete.**

### 1.6 Learn exploratory analysis through reproducible visual experiments

Learn how distributions, transformations, missingness, outliers, confounding, and sampling bias change visual patterns and their defensible interpretation. **L3 planning is intentionally deferred until 1.1 is complete.**

### 1.7 Consolidate and demonstrate the first learning milestone

Combine the scientific concepts and runnable experiments into one reproducible demonstration, with the learner able to explain the evidence, assumptions, limitations, and unresolved questions. **L3 planning is intentionally deferred until 1.1 is complete.**
