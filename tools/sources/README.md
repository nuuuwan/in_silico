# Explore Real Dengue Experiments

ChEMBL and PubChem are public collections of results reported by scientists.
They connect several kinds of record: a **target** is the part of a virus or
cell a treatment may affect, an **assay** is a laboratory test, a **compound**
is a chemical tested in that assay, and an **activity measurement** records what
happened at a particular amount of that chemical.

The fetch tool preserves copies of those records before later tools interpret
them. Start from the repository root:

```bash
tools/sources/fetch_bioactivity.py \
  --sources chembl,pubchem \
  --query "dengue virus" \
  --activity-types IC50,EC50,CC50
```

The terminal summarizes the search and shows how many targets, assays,
molecules, activities, and dose responses came from each source.

The reported manifest path identifies a request-specific folder under
`data/raw`. It contains JSON Lines files. Each line is one record written as
JavaScript Object Notation (JSON), a structured text format. Open a target
file, choose an identifier, and search for that identifier in an assay file.
Then follow an assay identifier into activities and a compound identifier into
molecules. How many steps separate the disease search from a measured chemical?

## Ask Two Libraries the Same Question

Run the command once with `--sources chembl`, then with `--sources pubchem`.
Each request automatically gets its own folder. ChEMBL organizes published
drug-discovery data; PubChem collects chemical and biological test records from
many depositors. Compare the fields and number of links rather than assuming
one answer is complete. Which details appear in only one source?

## Change What Counts as Activity

Repeat the PubChem experiment with `--activity-types IC50`, then with
`--activity-types EC50`. IC50 is the concentration that reduces a measured
process by half. EC50 is the concentration that produces half of the assay's
largest measured effect. They can describe different experiments and should not
be treated as interchangeable numbers. Do the same compounds and assays remain?

Try `CC50`, the concentration that kills half of the tested cells. Why would a
compound that affects dengue at a low concentration but kills cells at nearly
the same concentration be a poor lead?

## Audit the Snapshot

Open the manifest after each run. It records when retrieval happened, which web
addresses were requested, source versions, access terms, record counts, and a
SHA-256 checksum. A checksum is a digital fingerprint: if a snapshot changes,
its fingerprint changes too. Re-run the same command without changing paths;
it reports the existing result without downloading or overwriting anything.
This preserves the exact records used by later analyses.

Use `tools/sources/fetch_bioactivity.py --help` to discover smaller limits or
different source combinations. Public services change and can be temporarily
unavailable, so keep successful raw snapshots unchanged for offline analysis.

Learn more from the official [ChEMBL web-service guide](https://chembl.gitbook.io/chembl-interface-documentation/web-services/chembl-data-web-services)
and [PubChem PUG REST tutorial](https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest-tutorial).
