# Source Reconstruction Protocol - SRP-G1-VIRAL-001

Protocol id: `SRP-G1-VIRAL-001`

Status: `source_reconstruction_prep_only`

Authorization: `BA-G1-VIRAL-SOURCE-RECON-PREP-001`

Baseline commit: `02a0c643a6f0d83fb8b3dd35f428b9269c800f69`

Boundary: this protocol prepares a future human-readable source reconstruction
review package. It does not run OCR, create candidate source text, accept source
text, run QA, create fixtures, translate, proofread, implement modules, or
advance Gate 1.

## Scope

This prep package is limited to the currently admitted Viral review subset from
existing evidence:

- `POMB-G1-VIRAL-001` map-bundle lineage;
- `GSM-G1-VIRAL-001` controlled gold-sample references;
- `OCM-G1-VIRAL-001` frozen-for-review OCR candidate;
- `ORR-G1-VIRAL-001` remediation review;
- `OAC-G1-VIRAL-001` remediation admission candidate as configuration hints
  only;
- `GER-G1-VIRAL-001` evidence rollup;
- `ONC-G1-VIRAL-001` negative checks.

The admitted manifest is `SRA-G1-VIRAL-001`. No region outside that manifest is
in scope for this prep step.

## Output Schema

A future run package, under a separate run authorization, must contain:

- one candidate text record per admitted OCR-capable region;
- source page image and region reference for every candidate text record;
- selected OCR/config lineage for every OCR-derived text record;
- route decisions for visual-only or unresolved regions;
- overlay/order QC summary;
- uncertainty list;
- command/config/version/hash manifest;
- clear human review options.

This prep step may create only `SRD-G1-VIRAL-001` dry-run/precheck evidence.

## Fail-Closed Execution Rule

`scripts/build_source_reconstruction_review_package.py` must not run OCR by
default. It may create only a dry-run report unless all of the following are
true in a future separate execution:

- authorization id is exactly `BA-G1-VIRAL-SOURCE-RECON-RUN-001`;
- admitted manifest hash matches the expected value named by that run
  authorization;
- predecessor hashes match the run authorization;
- explicit execution flag is supplied;
- output directory is named by the run authorization.

If any condition is missing or mismatched, the script must fail closed before
creating candidate text or raw OCR outputs.

## Route Classes

- `ocr_candidate`: may later produce candidate text only through the future
  authorized script run.
- `visual_qc_only`: must not produce candidate text; it must be carried as a
  visual review item.
- `blocked_or_unresolved`: must stop the future run until a remediation
  authorization updates the manifest.

## Human Review Boundary

Bogdan is not needed for this prep package. Bogdan should review only a future
`G1-VIRAL-SOURCE-RECONSTRUCTION-REVIEW-001` package that contains readable
candidate text aligned to source page images/regions and an explicit
uncertainty list.

## Disallowed Outputs

- OCR outputs;
- candidate source text;
- accepted source text;
- PDF text-layer content;
- QA acceptance;
- fixtures;
- translation or proofreading outputs;
- implementation artifacts;
- Gate 1 advancement.

## Invalidation

This protocol stales if any predecessor hash, admitted manifest, route class,
run authorization rule, script/test contract, OCR candidate identity, map-bundle
lineage, gold sample content, reviewer authority, or protocol boundary changes.
