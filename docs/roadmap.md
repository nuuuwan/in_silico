# Roadmap for `in_silico`

## L1 Plan

1. Learn how evidence moves through drug discovery. Build interactive tools that teach the stages from target identification to clinical evaluation, the meaning of common assay results, and the difference between a computational hypothesis and experimental evidence.
2. Learn how computers represent molecules. Explore atoms, bonds, stereochemistry, protonation, identifiers, fingerprints, and molecular descriptors by changing structures and observing how their representations and calculated properties change.
3. Learn dengue biology through data. Connect the viral lifecycle, proteins, host systems, assays, and disease context to real public records while learning why provenance and experimental context matter.
4. Learn molecular similarity and its limits. Generate fingerprints, inspect nearest neighbors, vary similarity metrics, and discover activity cliffs where structurally similar molecules behave differently.
5. Learn prediction through controlled experiments. Train simple models, introduce realistic leakage and bias, compare validation strategies, inspect uncertainty, and learn when a prediction should not be trusted.
6. Learn evidence-based candidate prioritization. Combine experimental evidence, similarity, predictions, uncertainty, and applicability into transparent rankings, then test how different assumptions change the result.

Each L1 stage is a learning milestone expressed through runnable scientific experiments. The software exists to make important concepts observable and testable; package engineering supports that goal but is not itself the learning objective. Only stage 1 is currently expanded to L2, and only section 1.1 is expanded to L3.

# L2 and L3 Plan

## 1 Learn the drug-discovery process and its evidence

Build enough biological and pharmacological understanding to interpret later computations correctly. The emphasis is on learning by changing parameters, observing consequences, and explaining why the result changed—not on production infrastructure.

### 1.1 Explore the discovery pipeline, assays, and strength of evidence

By the end of 1.1, the learner should be able to place a result in the drug-discovery pipeline, interpret basic potency and toxicity measurements, distinguish evidence levels, recognize an unsupported claim, and choose a sensible next experiment.

- [x] 1.1.1. [Research + Python] Learn the purpose, inputs, outputs, and failure modes of target identification, hit discovery, hit-to-lead, preclinical evaluation, and clinical evaluation.

  Build a candidate-journey explorer that moves a hypothetical dengue compound through the selected stages and shows the scientific question, evidence produced, and common reason for failure at each step.

  ```bash
  tools/learning/candidate_journey.py --start target-identification --end clinical-evaluation --failure-mode low-selectivity
  ```

- [ ] 1.1.2. [Research + Python] Learn how a biological target, binding event, mechanism of action, cellular phenotype, and clinical outcome differ.

  Build a causal-chain explorer that lets the learner connect these concepts, deliberately break a link, and observe which downstream conclusions are no longer justified.

  ```bash
  tools/learning/causal_chain.py --target DENV2-NS5 --binding inhibited --mechanism polymerase-inhibition --phenotype reduced-replication --break-at phenotype
  ```

- [ ] 1.1.3. [Research + Python] Learn the difference between computational hypotheses, biochemical results, cellular results, animal studies, and clinical evidence.

  Build an evidence-ladder explorer that accepts a result and displays what it directly measures, what it only suggests, and which stronger claims remain unsupported.

  ```bash
  tools/learning/evidence_ladder.py --method docking --result predicted-binding --target DENV2-NS5
  ```

- [ ] 1.1.4. [Research + Python] Learn how scientific claims must be calibrated to the evidence behind them.

  Build a claim sandbox that compares a proposed statement with a chosen evidence level, explains any overreach, and shows how the wording changes as biochemical, cellular, animal, or clinical evidence is added.

  ```bash
  tools/learning/claim_sandbox.py --claim "compound X treats dengue" --evidence docking,in-vitro
  ```

- [ ] 1.1.5. [Research + Python] Learn the anatomy of a dengue antiviral assay: endpoint, virus and serotype, host system, exposure time, controls, replicates, concentration range, and units.

  Build an assay explorer that removes or changes one field at a time and shows how that change affects interpretation and comparability with another assay.

  ```bash
  tools/learning/assay_anatomy.py --preset cellular-antiviral --virus DENV-2 --cell-line Huh7 --remove controls
  ```

- [ ] 1.1.6. [Research + Python] Learn what IC50, EC50, CC50, and selectivity index measure and why they are not interchangeable.

  Build an endpoint calculator that plots antiviral activity and cytotoxicity curves, computes the selected endpoints, and updates them when the learner changes curve shape, concentration range, or noise.

  ```bash
  tools/learning/endpoint_lab.py --ec50 2 --cc50 80 --hill 1.2 --noise 0.05 --concentrations 0.01,0.1,1,10,100
  ```

- [ ] 1.1.7. [Research + Python] Learn how dose–response curves, replicate variability, and incomplete concentration coverage affect potency estimates.

  Build a dose–response simulator that generates replicate measurements, fits a curve, displays confidence intervals, and exposes failure cases such as a missing plateau or excessive noise.

  ```bash
  tools/learning/dose_response.py --true-ec50 2 --replicates 3 --noise 0.15 --max-concentration 10 --seed 42
  ```

- [ ] 1.1.8. [Research + Python] Learn what cheminformatics, molecular docking, molecular dynamics, machine learning, biochemical assays, and cellular assays can and cannot answer.

  Build a method-matching sandbox that ranks methods for a selected research question, shows the inputs each requires, and distinguishes the evidence generated from the conclusion the learner hopes to reach.

  ```bash
  tools/learning/method_matcher.py --question target-binding --available structures,sequences,bioactivity --budget low
  ```

- [ ] 1.1.9. [Research + Python] Learn why controls, biological replicates, technical replicates, uncertainty, and reproducibility matter.

  Build a replication simulator that lets the learner vary effect size, measurement noise, batch effects, and replicate counts, then compare how stable the estimated effect is across repeated experiments.

  ```bash
  tools/learning/replication_lab.py --effect 0.4 --biological-replicates 3 --technical-replicates 2 --batch-effect 0.15 --runs 100 --seed 42
  ```

- [ ] 1.1.10. [Research + Python] Learn why two apparently similar activity measurements may disagree or be impossible to combine.

  Build an assay-comparison sandbox that varies endpoint, units, serotype, cell line, exposure time, and censoring, then identifies which differences can be normalized and which change the biological meaning.

  ```bash
  tools/learning/compare_assays.py --left data/demo/assay_a.json --right data/demo/assay_b.json --vary cell-line,time,endpoint
  ```

- [ ] 1.1.11. [Research + Python] Learn the core vocabulary needed to read dengue drug-discovery papers and datasets without conflating related concepts.

  Build a contextual term explorer that takes a term such as `target`, `hit`, `potency`, or `efficacy`, shows it inside an assay or pipeline example, and contrasts it with commonly confused terms using source-backed definitions.

  ```bash
  tools/learning/term_in_context.py --term efficacy --contrast potency,activity --context antiviral-assay
  ```

- [ ] 1.1.12. [Research + Python] Apply the section’s concepts to a small, source-backed dengue case study.

  Build a case-study sandbox in which the learner changes assay results and available evidence for a hypothetical NS5 inhibitor, then observes how the supported claim, uncertainty, pipeline position, and recommended next experiment change.

  ```bash
  tools/learning/dengue_case_study.py --target DENV2-NS5 --ec50 2 --cc50 80 --evidence docking,cellular --replicates 3
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
