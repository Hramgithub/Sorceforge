# Context: Sourcefold baseline debt and continuation audit

- Goal ID: `20261012-sourcefold-baseline-debt-audit`
- State: `paused` (2026-10-13: user switched to an idea-vs-implementation audit; packet v3 kept as reference)
- Baseline: `98c2404ca894546326fc2f5b03d6db932e8d92bf` on `main`.
- Predecessor: completed goal `20261011-sourcefold-model-handoff`, whose next
  action was this audit.

## Accepted constraints

- Read-only with respect to evidence, tests, scripts, and acceptance state.
- Phase 0 and global Gate 1 remain active; `G1WGADR-G1-VIRAL-001` is bounded to
  pages 001-020 and the admitted G1FADAR fixture groups.
- The recorded suite result is 989 passed, 27 skipped, 13 failed.

## Preflight evidence

- Working tree clean at baseline; `origin/main` equal to `HEAD`.
- Every active OCR producer names `D:\NRI\.tools\tesseract\tesseract.exe`
  directly or via `overview.TESSERACT`; `D:\NRI` does not exist on this machine,
  so a test run cannot start Tesseract.
- Local tool candidates (not tracked, not portable): NRI checkout `.tools` with
  CPython 3.12.14 x86_64, pytest 9.1.1, Pillow 12.2.0 (MinerU venv), uv 0.12.13,
  Tesseract.
- Root `.gitattributes` sets `* -text`; a local clone reproduces working-tree
  bytes except files explicitly marked `text eol=lf`.

## Completed evidence

- S2: scratch clone at baseline reproduces 989 passed / 27 skipped / 13 failed
  after reconciling 12 sandbox temp-dir errors; the import root requires
  `PYTHONPATH=<repo root>`.
- S3: all 12 lineage failures are byte/line-ending identity: sealed hashes equal
  the CRLF form of unchanged LF blobs; 31 paths reachable from failing tests
  (superseded as a scope claim by the v2 full scan: 182 CRLF / 4 LF);
  scratch experiment with `text eol=crlf` on exactly those paths in
  `Sourcefold/.gitattributes` gives 1 failed / 1001 passed / 27 skipped.
- S4: method-family failure is a static/runtime layering defect; static inputs
  10/10 match; local NRI Tesseract exe/eng/osd hashes equal historical records.
- S5: third-party imports are only Pillow and pytest; proposal follows KB
  Creator D6.
- S6: packet `audit.md` recommends T1 line-ending identity restoration.

- R1 (critic, Claude Opus 5.5): NOT OK on v1 — P1-1 scope of CRLF identities
  was 31 test-reachable paths, real scope 186; plus P2-1..P2-4, P3-1..P3-5.
  Receipt `handoffs/R1-critic-review.md`.
- v2 fixes: full scan of 3996 blobs with path attribution → 182 CRLF / 4 LF;
  scratch experiment with 182 paths: 1 failed / 1001 passed / 27 skipped and
  attributed-reference mismatches 611 → 1 (allow-listed R1 prose); node IDs,
  authority, and next-consumer columns; self-pin count 10/12; 18 producer
  scripts; risk statements for existing checkouts, `-text` override, blob vs
  working identity.

- Evidence rename (v2): `evidence/crlf_identity_registry_candidate.json`, cited
  by the R1 receipt, was renamed to
  `evidence/superseded_first_layers_31_paths.json` (content unchanged; the
  file was never committed). The full set is `evidence/t1_candidate_set.json`.
- R1b (same critic): NOT OK on v2 — P1-A reverse class: 268 `.tsv` blobs are
  CRLF in Sourcefold while seals and NRI `22fafc14` blobs are LF (export copied
  the NRI autocrlf working tree); P2-A OBR-002 log hashes match no form;
  P3-A..D. Receipt `handoffs/R1b-critic-rereview.md`.
- v3 fixes: §3.6 reverse class verified (268/268 NRI blobs equal LF seals;
  plus 6 unreferenced differing blobs); F9 recorded as content-level, cause
  unknown; T1b proposed as a separate decision; consistency check scope and
  allowlist explicit; materialization script dirty-path refusal and index
  restore; folder counts corrected.

- R1c (same critic): OK on v3, no P1/P2; P3-E..H applied (six non-NRI blobs
  named with tooling split from T1b; F9 moved from allowlist to known
  residual; F3 scope wording; plan deliverables). Receipt
  `handoffs/R1c-critic-rereview.md`.

## Current step

Packet complete (v3, critic OK). Awaiting user decisions in `audit.md` §10.

## Next action

User decides on T1, T1b, F9 investigation, T2 network, and the §6 rule. No
commit, no evidence change, and no OCR until the user decides.
