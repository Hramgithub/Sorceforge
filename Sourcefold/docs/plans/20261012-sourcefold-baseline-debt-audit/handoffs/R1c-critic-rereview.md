# R1c independent critic re-review: baseline debt audit packet v3

- Goal ID: `20261012-sourcefold-baseline-debt-audit`
- Step ID: `R1c`, re-review after R1b
- Role: independent critic. The critic did not design or write the packet or
  its fixes.
- Model: Claude Opus 5.5 (`claude-opus-5-5`, as reported by the platform)
- Effort: unavailable. The task requested high effort, but the agent cannot
  see the actual setting.
- Assignment state: `user-overridden`. The policy critic is `gpt-6-astra`;
  the user overrode this to a Claude Opus 5.5 subagent for this goal only.
- Timestamp: 2026-10-12T01:17+03:00
- Baseline: `98c2404ca894546326fc2f5b03d6db932e8d92bf`. NRI export source:
  `22fafc14942e925b2e5f088f3c7ab1cd8efe3003`.
- Previous receipts: `handoffs/R1-critic-review.md` and
  `handoffs/R1b-critic-rereview.md`. Both are unchanged.
- Recommendation: **OK** as a decision packet. No P1 or P2 findings remain;
  there are 4 P3 nits.

## Scope

This is a read-only re-review of:

- `audit.md` v3, `plan.md`, and `context.md`;
- `evidence/cr_blob_scan.py`, `evidence/cr_blob_scan_98c2404.json`, and
  `evidence/tsv_and_log_check.py`.

It was checked against the same rules as R1 and R1b.

Nothing was executed or changed:

- no OCR, `tesseract.exe`, render, or network install;
- no commit;
- no file written in either repository except this receipt.

The critic's own scripts and outputs are in the session scratchpad under
`r1critic/`; they are not tracked.

## Independent verifications and results

1. **CR-containing blobs (F8 / §3.6).** I wrote my own script, separate from
   the packet's. It reads all HEAD blobs through `git cat-file`, the NRI
   blobs at `22fafc14`, and every 64-hex token in tracked files.
   - It finds **315** non-NUL blobs that contain CR:
     - 36 are sealed by their raw bytes, and their NRI blob is identical;
     - **268** are sealed by their LF form while the Sourcefold blob is CRLF;
     - 6 are unreferenced and differ from NRI;
     - 5 are unreferenced and identical to NRI.
   - These match the §3.6 table exactly.
2. **The 268 LF-sealed files.**
   - All 268 are `.tsv`.
   - For all 268, the NRI blob equals the Sourcefold blob with CRLF→LF,
     so the content is unchanged and only line endings differ.
   - For all 268, SHA-256 of the NRI blob equals the LF seal.
   - The per-folder counts (72/46/46/30/28/12/8/8/5/5/4/2/2) sum to 268 and
     match my R1b counts.
   - The 182 T1 paths and the 268 T1b paths are disjoint. The T1 paths
     contain no CR; the T1b paths do.
3. **The 6 unreferenced files that differ from NRI.** One is evidence:
   `core_0_1_text_extraction_geometry_probe_012_013_016_017_018_020_G1_VIRAL_001/raw_ocr/full_page_triage_boxes_expanded_psm4/p012/01_p012_b001_tes.tsv`.
   Five are active tooling or configuration:
   - `Sourcefold/.gitignore`
   - `docs/roadmap/roadmap_viewer.html`
   - `scripts/documentation_checkpoint.ps1`
   - `scripts/validate_roadmap.ps1`
   - `tools/roadmap-validator/validate-roadmap.mjs`

   All six have LF NRI blobs.
4. **Sourcefold blobs vs NRI `22fafc14`.**
   - 280 differ under `Sourcefold/`.
   - 274 of them are CR-containing: 268 + 6.
   - The other 6 are the intended guidance edits:
     - `AGENTS.md`, `PROJECT_STATUS.md`, `README.md`, and `SETUP.md`;
     - `docs/architecture/role_model.md` and `docs/plans/README.md`.
   - This is consistent with §3.6.
5. **F9 (OBR-002 logs).**
   - None of the 5 `Log SHA-256` values in `ocr_output_manifest.md` matches
     the raw, LF, or CRLF form of its log.
   - Each log blob is identical in NRI and has exactly one NRI commit.
   - The TSV seals in the same rows equal the NRI LF blob hashes.
   - F9 and its "cause unknown" label are confirmed.
6. **R1b fixes.**
   - **P1-A:** resolved by §3.6, F8, T1b, and decision 2 in §10. The v2
     wording "i.e. LF" is gone. The `release.md:15` claim is now correctly
     framed as "literally true for the working tree".
   - **P2-A:** resolved. The §3.3 limitation now says the consistency check
     covers line-ending identities only, F9 is recorded, and the T1 guard has
     an explicit allowlist.
   - **P3-A:** resolved; the counts are 128 / 5 / 47 in 13 folders / 2 root
     files.
   - **P3-B:** steps in `plan.md` are updated.
   - **P3-C:** the rename is recorded in `context.md`.
   - **P3-D:** the materialization script now refuses dirty paths and restores
     the index on failure.
7. **Carried forward from R1b.** These were not re-run this round:
   - all 182 sealing references are valid, and the set equals my 186-file
     scan;
   - the scratch suite with the 182-path experiment gives 1 failed / 1001
     passed / 27 skipped, and the only failure is the Tesseract node;
   - the authorization IDs, node IDs, and self-pins (10 of 12) are correct.

   The v3 changes do not touch these sections.
8. **Vocabulary and boundary.**
   - Nothing is called green, accepted, or released.
   - Gate 1, G1WGADR, and P002 are stated in their bounded form.
   - The 13 failures are still described as present.
   - `git status` shows changes only in the goal folder and the status row.
   - T1, T1b, and network access each require a separate user decision.
     T1b is clearly marked as creating new blobs.

## Findings

### P1 (blocker)

None.

### P2 (must fix before acceptance)

None.

### P3 (nits, fix when convenient)

- **P3-E.** §3.6 calls the 6 unreferenced files that differ from NRI evidence
  "of the same mechanism" and defers their decision "with T1b". Five of them
  are active tooling or configuration, not evidence (see item 3). The two
  `.ps1` files were CRLF in the NRI working tree because of NRI's
  `*.ps1 text eol=crlf` rule, not because of `core.autocrlf`. Name the six
  files and keep the tooling decision separate from the evidence restoration.
  For `.ps1`, an attribute may be the right fix instead of new blobs.
- **P3-F.** The T1 guard puts the 5 F9 log rows on the allowlist of a
  line-ending check. That check can never attribute those rows, so the
  allowlist entry has no effect. Record F9 as a known residual in the BIR
  record instead, or say that the guard also checks manifest rows that are
  unresolved.
- **P3-G.** F3 says "across all 3996 tracked blobs, 186 text files have a
  CRLF identity sealed elsewhere". It does not count the 36 CR-containing
  blobs whose raw CRLF identity is sealed and correct. The §3.3 limitation
  note covers this, but the F3 wording should say "among blobs without CR".
- **P3-H.** The Deliverables section of `plan.md` still lists only the R1
  receipt. Add the R1b and R1c receipts. In `context.md`, the S3 bullet
  ("31 paths in total") is history, but it should point to the v2 correction.

## Recommendation

**OK** as a decision packet for the user, at the scope of v3. Every factual
claim that I spot-checked or fully re-checked (the hashes, the counts, the
NRI identity, the scratch suite result, the authority IDs, and the self-pins)
is correct.

The packet does not change any evidence, test, script, or acceptance state.
It routes every change of governed bytes (T1, T1b) and the network
permission (T2) to explicit, separate user decisions. Its runtime proposal is
fail-closed.

The P3 nits do not block presenting the packet to the user.
