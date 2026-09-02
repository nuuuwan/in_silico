# In Silico Drug Discovery Overview

*2026-09-02 by @nuuuwan*

## Purpose and scope

Drug discovery is an iterative process for turning knowledge about disease into
interventions whose quality, safety, and efficacy can be tested. Computational
methods can organize evidence, generate hypotheses, and prioritize experiments.
They do not by themselves demonstrate that a compound is safe or effective in
people.

This note provides the shared model used by `in_silico`. It describes where
computational work contributes, what evidence later stages require, and how the
project must qualify its conclusions. The stages overlap and often feed back into
one another; they are a decision framework, not a guaranteed linear sequence.

## Discovery and development

### Disease understanding and target selection

Research first defines the unmet need and the biological process to influence.
A target may be a viral protein, host protein, pathway, or measurable phenotype.
Evidence should connect the target to disease biology and show that changing it
could produce a useful effect without unacceptable harm.

Computational analyses can integrate literature, sequences, structures, and
known interactions. Their output is a target hypothesis. Target relevance and
tractability remain separate questions, and neither proves that modulation will
benefit a patient.

### Hit discovery

Researchers search for compounds that produce a desired signal in biochemical,
cellular, or phenotypic assays. Searches may use experimental screening,
structure-based methods, ligand similarity, machine learning, or combinations of
these approaches. FDA's overview notes that early discovery may examine thousands
of compounds before a small number are selected for further study [1].

A computational hit is a prioritized candidate, not an experimentally confirmed
hit. An experimental screening signal is also provisional until identity,
concentration-response behavior, assay artifacts, and orthogonal or secondary
assays have been considered. The NCATS Assay Guidance Manual treats assay
optimization, interference, statistical validation, secondary assays, and data
reporting as integral to reliable screening [2].

### Hit confirmation and lead optimization

Confirmed hits are investigated for potency, selectivity, mechanism, chemical
identity, and reproducibility. Medicinal chemistry and repeated testing seek a
lead series with an acceptable balance of biological activity and developability.
Relevant properties include absorption, distribution, metabolism, excretion,
toxicity, route of administration, dose, and interactions with other treatments
[1]. A stronger score on one property cannot compensate automatically for weak or
missing evidence elsewhere.

### Preclinical evaluation

Preclinical work combines in vitro and in vivo studies to characterize
pharmacology, exposure, and toxicity before human testing. FDA describes good
laboratory practice requirements covering study conduct, personnel, facilities,
equipment, protocols, procedures, reports, and quality assurance [3]. Preclinical
results support decisions about whether and how to proceed; they do not substitute
for evidence from humans [4].

### Clinical evaluation and review

Clinical trials answer defined questions in people under a protocol. Typical
phases progress from initial safety and dosage studies, through preliminary
efficacy and side-effect studies, to larger controlled studies of efficacy and
adverse reactions [4]. Regulatory review considers the full body of evidence,
including preclinical and clinical data, manufacturing information, analyses,
and proposed use [5]. Exact pathways and legal standards depend on jurisdiction;
the FDA material cited here is a clear public example, not a universal rulebook.

Approval does not make knowledge complete. Rare, delayed, or population-specific
effects may emerge only after wider use, so safety evidence continues to evolve
through post-market monitoring [6].

## Evidence hierarchy

Evidence categories answer different questions and must remain distinct:

| Evidence | What it can support | What it cannot establish alone |
| --- | --- | --- |
| Computational | Plausibility, similarity, predicted binding or activity, and priorities for testing | Physical binding, biological activity, safety, or clinical benefit |
| In vitro | Activity or toxicity in a defined biochemical or cellular system | Whole-organism exposure, safety, or clinical efficacy |
| In vivo | Effects in a specified organism and experimental model | Equivalent effects or acceptable risk in humans |
| Clinical | Safety or efficacy for the studied people, intervention, comparator, dose, and endpoints | Universal benefit outside the studied context or complete long-term safety |
| Post-market | Performance and uncommon risks across broader real-world use | Absence of all bias, confounding, or unobserved risk |

Higher categories do not erase lower-level uncertainty. Evidence accumulates
across methods, and disagreements are findings to preserve rather than values to
average away. A useful claim names the intervention, system, endpoint, conditions,
and uncertainty instead of saying simply that a compound "works."

## Evidence standards for this project

### Provenance and identity

Every important value must retain its source, source identifier, retrieval date,
and transformation history. Compound identity must distinguish original and
standardized representations and must not silently merge salts, stereoisomers,
tautomers, mixtures, or conflicting identifiers. FAIR guidance emphasizes rich
metadata, persistent identifiers, licenses, provenance, and domain standards to
make digital objects reusable [7].

### Experimental context

Bioactivity values are meaningful only with their endpoint, units, assay format,
biological system, organism or cell line, protocol conditions, controls, and
qualifiers. Values from different contexts must not be treated as directly
comparable merely because they share a label such as `IC50`.

### Validation and quality

Inputs must be checked for invalid structures, missing fields, impossible units,
duplicates, inconsistent identifiers, and unsupported transformations. Assay
records should retain controls, replicate information, variability, detection
limits, and known interference risks when available. Failed validation remains
inspectable; it is not silently discarded.

### Computational evaluation

Models and rankings must record the exact data revision, feature generation,
software versions, parameters, random seeds, split strategy, metrics, and
applicability limits. Evaluation data must be independent of model fitting and
selection. Chemical series, duplicate measurements, and related compounds require
special care because random splitting can overstate performance through leakage.

Performance must be reported with uncertainty and relevant baselines. Predictions
outside the represented chemical or biological domain must be flagged. Rankings
are decision aids for allocating experimental attention, not declarations of
therapeutic value.

### Reproducibility and communication

Workflows should be deterministic where practical and preserve raw inputs,
processed outputs, configuration, environment information, and failure reports.
Reports must separate observed source data, calculated values, model predictions,
and project assumptions. Negative, missing, conflicting, and inconclusive results
must remain visible.

## Implications for `in_silico`

The package should therefore:

- represent compounds, targets, assays, sources, and observations explicitly;
- attach provenance and biological context to evidence rather than isolated
  numbers;
- preserve raw data while creating versioned derived records;
- make validation failures and uncertainty machine-readable;
- prevent data leakage and document applicability limits in model evaluation;
- produce reproducible workflows with inspectable inputs and outputs; and
- use claim language no stronger than the evidence category permits.

The immediate project outcome is a transparent ranked list of hypotheses worth
investigating. Experimental confirmation, preclinical development, clinical
evaluation, regulatory review, and ongoing safety monitoring remain outside what
the software alone can establish.

## References

1. U.S. Food and Drug Administration. [Step 1: Discovery and
   Development](https://www.fda.gov/patients/drug-development-process/step-1-discovery-and-development).
   Content current 2018-01-04. Accessed 2026-09-02.
2. National Center for Advancing Translational Sciences. [Assay Guidance
   Manual](https://www.ncbi.nlm.nih.gov/books/NBK53196/). NCBI Bookshelf ID
   NBK53196. Accessed 2026-09-02.
3. U.S. Food and Drug Administration. [Step 2: Preclinical
   Research](https://www.fda.gov/patients/drug-development-process/step-2-preclinical-research).
   Content current 2018-01-04. Accessed 2026-09-02.
4. U.S. Food and Drug Administration. [Step 3: Clinical
   Research](https://www.fda.gov/patients/drug-development-process/step-3-clinical-research).
   Content current 2018-01-04. Accessed 2026-09-02.
5. U.S. Food and Drug Administration. [Step 4: FDA Drug
   Review](https://www.fda.gov/patients/drug-development-process/step-4-fda-drug-review).
   Content current 2018-01-04. Accessed 2026-09-02.
6. U.S. Food and Drug Administration. [Step 5: FDA Post-Market Drug Safety
   Monitoring](https://www.fda.gov/patients/drug-development-process/step-5-fda-post-market-drug-safety-monitoring).
   Content current 2018-01-04. Accessed 2026-09-02.
7. GO FAIR. [FAIR Principles](https://www.go-fair.org/fair-principles/).
   Accessed 2026-09-02.
