# In Silico Drug Discovery Overview

Published 2026-09-02 by @nuuuwan.

## What drug discovery means

Drug discovery is the search for substances that may prevent, control, or cure
a disease. A substance being studied for this purpose is often called a
*compound*.

Finding an interesting compound is only the beginning. Researchers must learn
what it does, how much is needed, how the body handles it, and whether it causes
harm. They must then test whether it helps people. This takes many rounds of
research, and most early ideas do not become medicines.

`in_silico` means "performed on a computer." Computer methods can sort large
amounts of information, find patterns, and suggest which compounds deserve
closer study. They cannot prove that a compound is safe or that it treats a
disease. Only suitable experiments can provide that evidence.

## The journey from an idea to a medicine

Drug discovery is often described as a series of stages. Real projects may move
back and forth between them when new results raise new questions.

### 1. Target identification: What should we change?

A disease changes how the body, a cell, or an infectious organism works.
Researchers first look for something involved in that change. This is called a
*target*. A target might be a protein used by a virus or a process inside a
human cell. A protein is a tiny biological machine that performs a job in a
living system.

Researchers ask whether changing the target is likely to help with the disease
and whether it can be changed without causing unacceptable harm. Computers can
bring together published research, genetic information, protein structures, and
known interactions. This supports a target hypothesis: a reasoned proposal about
what to study. It does not prove that changing the target will help a patient.

### 2. Hit discovery: What might affect the target or disease?

Researchers look for compounds that produce a useful signal. They may test many
compounds in the laboratory or use computers to rank likely candidates. The FDA
notes that thousands may be considered before a small number are selected for
more study [1].

An early promising compound is called a *hit*. A computer-ranked hit is only a
suggestion for laboratory testing. A laboratory hit is also uncertain. The
result might come from a measurement problem, contamination, or an unexpected
reaction with the test itself. Researchers therefore repeat the test and use
different tests to check that the signal is real [2].

### 3. Hit-to-lead work: Can a hit become a good candidate?

A real hit may still be a poor medicine. It might break down too quickly, fail
to reach the right part of the body, affect healthy cells, or be difficult to
make. Researchers compare related compounds and chemists alter their structures.
Each version is tested again.

The aim is to find a *lead*: a compound with a useful balance of desired
activity, limited unwanted effects, suitable behavior in the body, and practical
production. Improving one feature can make another worse, so there is rarely one
simple "best score" [1, 2].

### 4. Preclinical evaluation: Is human testing reasonable?

Before testing a candidate in people, researchers study what it does and what
harm it might cause. Some studies use isolated chemicals, proteins, or cells.
These are called *in vitro* studies, meaning studies outside a living body.
Other studies use a whole living organism. These are called *in vivo* studies.

Researchers examine the candidate's effects, how it moves through and leaves
the body, and how dose relates to both exposure and harm. Regulated preclinical
studies follow standards for plans, equipment, records, staff, reports, and
quality checks [3]. The results help decide whether and how to begin human
trials. They cannot guarantee safety or benefit in people [4].

### 5. Clinical evaluation: What happens in people?

A clinical trial is a planned study involving people. Its written plan states
who may take part, what treatment they receive, what will be measured, and how
the results will be analyzed [4].

Clinical trials usually proceed through phases:

- **Phase 1** mainly studies safety and dosage in a small group.
- **Phase 2** begins to study whether the treatment helps people with the
  condition and continues to watch for side effects.
- **Phase 3** tests benefits and harmful effects in a larger group, often by
  comparing the treatment with another treatment or a control group.

Regulators review all the available evidence, including laboratory studies,
clinical trials, manufacturing, and quality information [5]. The exact process
depends on the country. The FDA sources used here describe the United States and
serve as a clear public example, not a worldwide rulebook.

Approval is not the end of learning. Rare or delayed problems may appear only
after many more people use a medicine, so safety monitoring continues [6].

## Where this project fits

`in_silico` supports the early stages of discovery. Its planned capabilities fit
into the wider process as follows:

| Project capability | Where it helps | What it contributes |
| --- | --- | --- |
| Biological terms and target records | Target identification | Keeps a clear account of a target and why it may matter |
| Public compound and activity data | Target identification and hit discovery | Collects existing evidence and possible starting compounds |
| Molecular representations and properties | Hit discovery and hit-to-lead work | Describes compounds consistently and highlights features to investigate |
| Similarity search | Hit discovery and hit-to-lead work | Finds related compounds for comparison |
| Prediction and model evaluation | Hit discovery and hit-to-lead work | Ranks ideas for testing and reports uncertainty |
| Candidate ranking and reports | Hit discovery and hit-to-lead work | Shows why one hypothesis was ranked above another |

The intended result is a transparent list of compounds that may be worth
testing. The software does not confirm hits, perform preclinical studies, run
clinical trials, approve medicines, or monitor safety. A highly ranked compound
remains a hypothesis until experiments provide stronger evidence.

## Different kinds of evidence

Each kind of research answers a different question. One should not be presented
as if it answered them all.

| Evidence | What it may show | What it cannot show by itself |
| --- | --- | --- |
| Computer result | A compound or target is worth investigating | The compound physically works, is safe, or helps people |
| In vitro result | An effect occurs in a particular laboratory test | The same effect occurs in a whole body |
| In vivo result | An effect occurs in a particular living model | The same benefit and risk will occur in humans |
| Clinical result | What happened to the people studied under stated conditions | What will happen to every person or over unlimited time |
| After-approval data | How a medicine performs during wider use | That every possible risk has been found |

Evidence becomes stronger by combining well-designed studies, not merely by
moving down the table. Results may disagree. Those disagreements must be kept
and investigated rather than hidden or averaged away.

It is more accurate to say, "The compound reduced this measurement in these
cells under these conditions," than to say, "The compound works." The first
statement tells the reader what was actually observed.

### Match each claim to its evidence

The wording of a claim must reveal what was actually done:

| Evidence available | Defensible claim | Claim that goes too far |
| --- | --- | --- |
| Computer calculation | "The model predicts that this compound may bind." | "This compound binds to the target." |
| In vitro experiment | "The compound reduced viral activity in these cells." | "The compound treats infection in a body." |
| In vivo experiment | "The compound reduced this outcome in this animal model." | "The compound will work safely in humans." |
| Clinical study | "The treatment improved this outcome in the people studied." | "The treatment works for everyone and has no unknown risks." |

A computer result is a *hypothesis*: an idea that can guide a test. An in vitro
result is a physical observation, but only in the stated laboratory system. An
in vivo result includes the complexity of a living organism, but a model organism
is not a human. Clinical evidence comes from people, yet it still applies only to
the studied treatment, dose, participants, comparison, outcome, and time period.

None of these labels guarantees that a study was well designed. Sample size,
controls, measurement quality, bias, and uncertainty still matter. Later-stage
evidence answers broader questions, but it does not turn an earlier prediction
into an observation or erase conflicting results.

## What the main computer methods do

These methods often work together near the beginning of drug discovery. They
help researchers decide what to test, but they answer different questions.

### Cheminformatics

Cheminformatics uses computers to store, clean, search, compare, and calculate
information about chemical structures. It can identify duplicate records, find
similar compounds, and calculate descriptors: numbers that summarize structural
features. RDKit, which this project plans to use, provides two- and
three-dimensional molecular operations and descriptor generation [8].

Cheminformatics can show that two recorded structures are similar or that a
calculated property differs. It cannot show that a compound binds to a target,
changes a cell, is safe in a body, or helps a patient.

### Molecular docking

Molecular docking tries possible positions of a compound in a three-dimensional
model of a target and scores how well each pose appears to fit. It can suggest a
possible binding pose and help prioritize compounds for physical tests [9].

The result depends on the target structure, compound form, scoring method, and
other assumptions. A good docking score is not proof of binding. Docking alone
cannot establish activity in cells, safety, or clinical benefit.

### Molecular dynamics

Molecular dynamics simulates how atoms move over time according to a physical
model. It can explore how a protein changes shape, how a proposed complex might
move, and which interactions may persist. Reviews describe it as an atom-level
view that can explain mechanisms and motivate further experiments [10].

A simulation covers a chosen model and limited simulated time. Its usefulness
depends on its starting structure and physical assumptions. It is not a living
cell, organism, or clinical trial, and cannot demonstrate clinical efficacy.

### Machine learning

Machine learning finds patterns in examples and uses those patterns to predict
new cases. In drug discovery it can rank compounds, predict measured properties,
or help select the next experiment [11].

Its predictions inherit the strengths, gaps, and biases of the training data.
Performance on a test dataset does not prove that the model will work for new
chemical families or biological settings. Machine learning can prioritize a
hypothesis; it cannot turn a prediction into laboratory or clinical evidence.

### Their shared limit

All four methods can reduce a large search to a smaller, better-documented set of
questions. Agreement between methods may strengthen the reason to run an
experiment, but it does not replace that experiment. None can establish that a
compound is clinically effective without suitable evidence from people.

## How the project will handle evidence

### Keep the source

Every important value should retain where it came from, when it was retrieved,
and what changes were made to it. This history is called *provenance*. Keeping
it allows someone else to inspect or repeat the work. The FAIR Principles also
recommend clear identifiers, descriptions, licenses, provenance, and shared
standards so digital research objects can be reused [7].

### Keep the scientific context

A biological activity number has little meaning on its own. Its meaning depends
on what was measured, the units, the test method, the cells or organism used,
the dose, the timing, the controls, and other conditions. Two values with the
same label should not be compared automatically when they came from different
tests.

### Keep compound identity precise

One compound may be written in several ways, while very similar names may refer
to importantly different forms. The project should preserve both the original
record and any cleaned version. It should not silently combine mixtures,
different three-dimensional forms, salts, or conflicting identifiers.

### Check data instead of hiding problems

The software should look for missing information, invalid chemical structures,
impossible units, duplicates, and conflicting identifiers. A failed check should
remain visible with a useful explanation. Quietly deleting awkward data would
make the final result look more certain than it is.

### Test computer models fairly

A model must be tested using data that was not used to build or choose it.
Nearly identical compounds can accidentally appear in both training and test
data, making performance look better than it really is. Reports should record
the data version, settings, software versions, random choices, test method,
results, uncertainty, and the kinds of compounds for which the model may not be
reliable.

### Make the work repeatable

Where practical, running the same workflow with the same inputs should produce
the same outputs. The project should preserve raw inputs, cleaned data, settings,
software information, outputs, and failures. Reports should clearly separate
source observations, calculated values, computer predictions, and project
assumptions.

## The central limitation

This project can organize evidence and rank hypotheses. It cannot demonstrate
that a compound is a medicine. Experimental confirmation, preclinical research,
clinical trials, regulatory review, and continuing safety monitoring are
separate and essential parts of the journey.

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
8. RDKit contributors. [An overview of the
   RDKit](https://www.rdkit.org/docs/Overview.html). Accessed 2026-09-02.
9. Meng X-Y, Zhang H-X, Mezei M, Cui M. [Molecular docking: a powerful approach
   for structure-based drug
   discovery](https://doi.org/10.2174/157340911795677602). *Current Computer-Aided
   Drug Design*. 2011;7(2):146-157. PMID 21534921. Accessed 2026-09-02.
10. Hollingsworth SA, Dror RO. [Molecular dynamics simulation for
    all](https://doi.org/10.1016/j.neuron.2018.08.011). *Neuron*.
    2018;99(6):1129-1143. PMID 30236283. Accessed 2026-09-02.
11. Vamathevan J, Clark D, Czodrowski P, et al. [Applications of machine
    learning in drug discovery and
    development](https://doi.org/10.1038/s41573-019-0024-5). *Nature Reviews Drug
    Discovery*. 2019;18:463-477. PMID 31043761. Accessed 2026-09-02.
