# R1 independent critic review: baseline debt audit packet

- Goal ID: `20261012-sourcefold-baseline-debt-audit`
- Step ID: `R1`
- Role: independent critic (did not design or write the packet)
- Model: Claude Opus 5.5 (`claude-opus-5-5`, as reported by the platform)
- Effort: unavailable (requested: high; not visible to the agent)
- Assignment state: `user-overridden` (policy critic `gpt-6-astra`; scoped user
  override to a Claude Opus 5.5 subagent for this goal only)
- Timestamp: 2026-10-12T00:54+03:00
- Baseline: `98c2404ca894546326fc2f5b03d6db932e8d92bf`
- Recommendation: **NOT OK** as a decision packet (1 blocker, 4 must-fix).

## Scope

Read-only review of `audit.md`, `plan.md`, `context.md`, `evidence/*`, and
the added `PROJECT_STATUS.md` row. The review checked them against root
`AGENTS.md`, `Sourcefold/AGENTS.md`, `docs/governance/nri_goal_governance.md`,
and `Sourcefold/docs/handoff/MODEL_HANDOFF_SPEC.md` §4, §10 and §14.

The review did not run OCR, `tesseract.exe`, rendering or network installs,
and made no commit. The only file written in either repository is this
receipt. Critic scripts and outputs are in the session scratchpad under
`r1critic/`. They are not tracked.

## Files checked

- Packet: `audit.md`, `plan.md`, `context.md`, `evidence/pytest_summary.md`,
  `evidence/crlf_identity_registry_candidate.json`, `evidence/trace_lineage.py`,
  `evidence/eol_iterate.py`, `evidence/eol_apply_final.py`,
  `evidence/self_pins.py`.
- Repository (HEAD): `.gitattributes`, `Sourcefold/.gitattributes`, all 3996
  tracked blobs (hash scan), the 13 failing test files,
  `scripts/build_core_0_1_text_extraction_012_016_020_method_family.py`, the
  21 Tesseract-naming scripts, `run_ocr_remediation_matrix.py`,
  `run_source_reconstruction_refined_ocr.py`,
  `docs/plans/20261011-sourcefold-standalone-export/release.md` and
  `handoffs/R1-release-review.md`,
  `first_pass_runtime_selector_run_001_020_report.json`, and
  `p002_fresh_ocr_pass_decision_report.json`.
- NRI (read-only): Git history of the sampled predecessors and of the root and
  `Sourcefold/.gitattributes`; `.tools/tesseract` (hashed only, not executed);
  `.tools/tool-manifest.json`.
- KB Creator (read-only):
  `C:\_Hobby\_work\kb_creator\kb_creator\docs\plans\20261011-standalone-hardening\decisions.md`
  (D4, D4b, D6).

## Independent verifications and results

1. **First-layer hashes, own recompute.** Hashes were computed with
   PowerShell `Get-FileHash` and with Python `hashlib` over Git blobs, using
   the transform `\n -> \r\n`. Rows checked: L01, L06, L10, L12, and L14. All
   LF and CRLF values equal the §3.1 table. None of these blobs contains CR.
   For L01, L06, L12, and L14, the sealed value read directly from the
   consumer record equals the CRLF hash. L10's CRLF hash `A37F734D…` appears
   in 26 tracked files, including producer constants.
2. **NRI history.** For L01 (`8d172bae`), L10 (`4a51b975`), L12 and L14
   (`f90d170b`), L06 (`1d6b5a81`), and the status packet (`a9971239`):
   - each path has exactly one NRI commit;
   - the NRI blob at that commit and at NRI HEAD equals the Sourcefold blob
     byte for byte (same blob IDs).

   Across all 31 registry paths, `git log --all` gives exactly one NRI commit
   each.
3. **Registry recompute.** All 31 LF and CRLF values in
   `crlf_identity_registry_candidate.json` recompute correctly. The 31 CRLF
   hashes have exactly 244 references in other tracked files. LF references
   exist only for the brief report, in
   `20261011-sourcefold-standalone-export/handoffs/R1-release-review.md`.
   This confirms §3.2 as far as it goes.
4. **NRI attributes.** `fb1bfa1d` (2026-06-16) added `* text=auto` with
   `*.json`/`*.md`/`*.txt text eol=lf`. This is confirmed. The 4 named
   producers and 12 more call `write_text` without `newline=`. This is
   confirmed.
5. **Scratch pytest rerun** with the eol=crlf experiment for the 31 paths.
   The command ran from `scratch\repo\Sourcefold` with
   `PYTHONPATH=scratch\repo` and `--basetemp` under the scratchpad. Result:
   `1 failed, 1001 passed, 27 skipped`. The only failure is the Tesseract
   node at `...method_family.py:143`. The clone shows only
   `Sourcefold/.gitattributes` modified. F4 is confirmed.
6. **Tesseract.** Files were hashed and not executed. These match the
   historical records:
   - `tesseract.exe`: `BABB405F…6ED9`
   - `eng.traineddata`: `7D4322BD…70B2`
   - `osd.traineddata`: `9CF5D576…00FF`

   `tool-manifest.json` contains `tesseract v5.4.0.20240606`.
   `libtesseract-5.dll`: `279488C4…AC1A`, 101 MB, with 0 historical records
   in the repo. `verify_inputs()` at lines 138-158 checks `TESSERACT.exists()`
   at line 142 before the hash loop. This is confirmed.
7. **Scripts.**
   - 21 scripts name `D:\NRI` Tesseract directly or through `TESSERACT`.
   - `build_core_0_1_text_extraction_frozen_profile_config.py` is pinned
     once and `build_p002_completion_and_next_review.py` 4 times (LF). The
     method-family script is pinned 0 times.
   - The only third-party imports are PIL and pytest.

   All of this is confirmed.
8. **Lane map.** The first-pass report fields match:
   - `fresh_ocr_execution_pages` = 009, 010, 011, 015;
   - `candidate_materialized_pages` = 012, 013, 016, 017, 018, 020;
   - `bridge_lineage_pages` = 001–008, 014, 019;
   - `all_pages_fresh_ocr_success` and `production_ready` are false.

   P002 decision: `fresh_ocr_success_pages`, `bridge_removed_for_pages`, and
   `promotable_pages` = 002; `acceptance_performed` and `production_ready`
   are false. This is confirmed.
9. **Vocabulary.** Nothing is called green, released, or fixed. Gate 1 and
   G1WGADR are described as bounded. The 13 failures are described as
   present in the real repository. `git status` shows changes only inside
   the goal folder and the status row. This is confirmed.
10. **Full CRLF-identity scan (new).** For every tracked LF blob at HEAD
    (3996 blobs), the critic computed SHA-256 of the CRLF transform. It then
    searched all other tracked files for that value as a 64-hex token. See
    finding P1-1.

## Findings

### P1 (blocker)

**P1-1. The "31 paths in total" claim is false, so T1 is under-scoped.**
This affects F3, §3.2, §9 T1, and the registry. 186 tracked LF files have
their CRLF identity sealed elsewhere in the repository. That is 155 more than
the registry lists:

- 147 of the extra files are CRLF-only (0 LF references).
- 8 are tiny stderr files with identical content, referenced as both LF and
  CRLF. They are ambiguous and need a per-file decision.

Examples:

- `ocr_remediation_review_G1_VIRAL_001/ocr_remediation_review_report.json`.
  This is the consumer of L12–L15 itself. Its CRLF hash `B3491A1F…` is
  referenced 9 times, including `expected_sha256` in
  `source_reconstruction_review_G1_VIRAL_001/source_reconstruction_precheck.json:52`
  and `bounded_trial_authorizations.md:8803`.
- `render_output_manifest.md`. Its CRLF hash `622C0D91…` has 13 references,
  including `decision_log.md:231` and `roadmap.yaml`.
- `gate_1_status_packet_G1_VIRAL_002/*`.
- Sibling manifests and summaries of the 31 paths, for example
  `gate_1_review_decision_manifest.md` and
  `gate_1_status_packet_manifest.md`.
- About 130 `ocr_remediation_matrix_G1_VIRAL_001/raw_outputs/*.log.txt` and
  `*.stderr.txt` files, sealed by `ocr_remediation_matrix_rows.json` and
  `ocr_remediation_output_manifest.md`.

The 31-path list is only the set reachable from failing test assertions. It
is not the set of sealed CRLF identities. If T1 is applied as written:

- the guard and the successor record would make an incomplete registry
  canonical;
- the same directories would stay internally inconsistent. For example,
  `ocr_remediation_matrix_rows.json` would return to its sealed CRLF form
  while its own row hashes of `raw_outputs` still mismatch the working bytes;
- the Definition of Done (12 tests pass) cannot detect any of this.

Required fix, either of:

- re-scope F3, §3.2, and T1 to "identities exercised by the failing tests",
  and list the residual set as known remaining debt; or
- extend the classification to all 186 files, with an explicit decision for
  the 8 ambiguous files.

The 244-reference cross-check should be repeated for the new set.

### P2 (must fix before acceptance)

**P2-1. The self-pin count is inaccurate and contradicts §3.4.** The packet's
own `self_pins.py` reports 8 LF matches plus 1 `NO MATCH` (the superseded
status-packet pin). Independently, the current LF hashes of 10 of the 12
failing lineage test files are pinned:

- 8 through their own consumer's `test_contract_sha256`.
- `test_gate_1_status_packet.py` through
  `gate_1_status_packet_G1_VIRAL_002/gate_1_status_report.json`
  (`test_contract_sha256`), `roadmap.yaml:696`, and
  `bounded_trial_authorizations.md:2127`.
- `test_source_reconstruction_next_slice.py` through
  `source_reconstruction_next_slice_G1_VIRAL_002` report `test_sha256`, its
  manifest, `roadmap.yaml:379`, and `bounded_trial_authorizations.md:4897`.

Unpinned: `test_ocr_remediation_review_package.py` and
`test_source_reconstruction_next_slice_004.py`. The conclusion "do not edit
tests" stands and is stronger. Correct the number and the mechanism.

**P2-2. §14 Result 1 and the plan's Definition of Done are not met.** The
§3.1 table lists test files instead of node IDs; node IDs appear only in
`evidence/pytest_summary.md`. It has no "authority" column (the bounded
authorization or decision under which each consumer record was sealed) and
no "current successor" column. MODEL_HANDOFF_SPEC §14 requires all of these.

**P2-3. Registry labels overclaim, and the guard design is self-referential.**

- `sealed_crlf_sha256` is computed (`eol_apply_final.py:49`), not read from a
  sealed record.
- `nri_first_commit` takes the newest `git log` line (`eol_apply_final.py:44`).

The values are correct today (verifications 2 and 3), but:

- the T1 successor record must cite, for each path, the sealing record path
  and the field or line;
- the guard test must check working bytes against that cited sealed value,
  not against the registry's own derived hash.

**P2-4. The T1 risk statement is incomplete.**

- (a) Existing clones do not re-materialize CRLF after pulling an attribute
  change. Tests and the guard stay red until a documented re-checkout or
  renormalize step is run. That step is not in the plan or in the `SETUP.md`
  update, and the Definition of Done was verified only on a fresh clone.
- (b) 4 T1 paths are under `ocr_remediation_matrix_G1_VIRAL_001/** -text
  -diff`, whose comment says "Preserve generated OCR remediation evidence
  exactly". T1 overrides this with `text`, because the later line in the
  same file wins. This needs an explicit justification and an ordering rule
  that the guard checks.
- (c) The §3.3 causal chain is not verified for the matrix directory. NRI
  `f90d170b` added `-text -diff` in the same commit as the matrix files, yet
  0 of the 324 text-like matrix files contain CR. Normalization evidently
  happened before that attribute applied. Say this instead of attributing
  everything to `*.json text eol=lf`.
- (d) After T1, blob-level readers and `git archive` consumers still see LF
  while the working tree has CRLF. The successor record must state which
  identity is canonical for which use.

### P3 (nits)

- **P3-1.** "16 of 184" counts scripts with no `newline=` anywhere. 18
  scripts have at least one `write_text` call without it. The missing two
  include `run_ocr_remediation_matrix.py` (lines 178, 179, 296, 493), which
  produced L12–L15 and the CRLF raw outputs, and
  `run_source_reconstruction_refined_ocr.py`. The T4 allowlist would be
  incomplete.
- **P3-2.** "Historical identity can be reproduced by hash" (§4.1) holds only
  for the recorded objects (exe, eng, osd, version). The proposed
  `libtesseract-5.dll` pin is a new identity, not a historical one. Say so.
- **P3-3.** The KB Creator decisions path is given without its repository
  (it is not in NRI; it is a separate `kb_creator` checkout) and without a
  commit. Acceptance there does not transfer to Sourcefold
  (non-transitive). Name the user decision that adopts it.
- **P3-4.** §6 narrow edit: the method-family script is referenced by path
  as provenance, so require the pre-edit blob ID in the successor or commit
  record. "All 21 refuse to overwrite" is evidenced here only for 7 of 21 by
  grep; either verify all 21 or soften the wording.
- **P3-5.** The task packet calls `audit.md` Russian; the file is English.
  Align the wording.

## Recommendation

**NOT OK** for the packet as a decision packet. The following are correct and
reproducible:

- F1, F2 (for the 12 failures), F4, F5, F6 (scoped as in P3-2), and F7;
- the lane map;
- the vocabulary;
- the read-only boundary.

P1-1 changes the scope and the Definition of Done of the recommended T1, so
the user should not be asked to approve T1 as written. Fix P1-1 and P2-1 to
P2-4, then send the packet for re-review.
