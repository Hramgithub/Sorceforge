# R1b independent critic re-review: baseline debt audit packet v2

- Goal ID: `20261012-sourcefold-baseline-debt-audit`
- Step ID: `R1b` (re-review after the R1 findings)
- Role: independent critic. I did not design or write the packet or its fixes.
- Model: Claude Opus 5.5 (`claude-opus-5-5`, as reported by the platform)
- Effort: unavailable. High was requested, but the effort level is not
  visible to the agent.
- Assignment state: `user-overridden`. The policy critic is `gpt-6-astra`.
  The user's override, scoped to this goal only, names a Claude Opus 5.5
  subagent instead.
- Timestamp: 2026-10-12T01:10+03:00
- Baseline: `98c2404ca894546326fc2f5b03d6db932e8d92bf`
- Previous receipt: `handoffs/R1-critic-review.md` (unchanged)
- Recommendation: **NOT OK** as a decision packet. There is 1 new blocker and
  1 must-fix item. All R1 findings are resolved.

## Scope

This is a read-only re-review of `audit.md` v2, `context.md`, `plan.md`, and
the new evidence files. It was checked against the same rules as R1:

- root `AGENTS.md`;
- `Sourcefold/AGENTS.md`;
- `docs/governance/nri_goal_governance.md`;
- `MODEL_HANDOFF_SPEC.md` §4, §10, and §14.

I did not run OCR, `tesseract.exe`, rendering, or network installs, and I made
no commit. This receipt is the only file I wrote in either repository. My
scripts and outputs are in the session scratchpad under `r1critic/`, which is
not tracked.

## Files checked

- **Packet:**
  - `audit.md` (v2) and `context.md`;
  - `plan.md` (unchanged since v1);
  - `evidence/t1_candidate_set.json`, `identity_scan.py`,
    `identity_scan_98c2404.json`, and `identity_attribute.py`;
  - `identity_attribution_98c2404.json` and
    `identity_attribution_after_t1_experiment.json`;
  - `eol_apply_set.py` and `superseded_first_layers_31_paths.json`.
- **Repository:**
  - the HEAD blobs (3996), and the import commit `c557381` compared with NRI
    `22fafc14`;
  - `ocr_benchmark_OBR-G1-VIRAL-002/ocr_output_manifest.md` and its
    `raw_outputs`;
  - `012_016_020_method_family_manifest.md` and the TSV hashing in its
    producer;
  - the consumer reports for N01, N05, N07, N10, and N12.
- **Scratch clone:** the 182-path experiment in `Sourcefold/.gitattributes`.

## Independent verifications and results

1. **Candidate set.** `t1_candidate_set.json` holds 182 `selected_crlf`
   paths, 4 `kept_lf` paths, and 0 unresolved.
   - Their union is exactly the 186 files my own R1 scan found.
   - The 31 v1 paths are all among the 182 selected ones.
2. **Sealing references.** I checked every `sealing_refs` file:line for all
   182 paths against HEAD. Each line contains that path's CRLF hash: 0 bad
   references, and no path is without a reference.
   - No LF hash of a selected path is referenced with its basename within ±6
     lines.
   - The 4 kept-LF stderr files are named next to their LF references in their
     own manifests. Their CRLF references do not name them, so they are
     content collisions, as the packet says.
3. **OBR-002.** `ocr_output_manifest.md:60-64` are rows keyed by sample ID.
   The `Stderr SHA-256` column holds `7EB70257…`, which is SHA-256 of `\r\n`.
   Each blob is 1 byte (`\n`). The packet's decision is confirmed.
4. **Scratch clone.**
   - All 182 paths have `text: set` and `eol: crlf`. 129 of them keep
     `diff: unset`, that is 128 in the matrix folder and 1 in the prep folder.
   - The working bytes of all 182 paths equal their CRLF identity. The 4 kept
     paths are still LF.
   - In the real repository, all 182 paths have `text: unset`.
   - These results confirm the packet's statements.
5. **pytest rerun** in the scratch clone (with `PYTHONPATH=clone` and
   `--basetemp` under the scratchpad): `1 failed, 1001 passed, 27 skipped`.
   The only failure is the Tesseract node. F4 is confirmed.
6. **Attribution summaries.** The baseline attribution checks 616 references
   and finds 611 mismatched. After the experiment, 1 is mismatched. These are
   the packet's own outputs. Their logic matches my independent results in
   items 1 and 2.
7. **R1 fixes.**
   - **P2-1:** §3.5 now matches my R1 result: 10 of 12 test files pinned, by
     these mechanisms.
   - **P2-2:** node IDs are present. I spot-checked the authority column
     against the `authorization_id` fields of the N01, N05, N07, N10, and N12
     consumers, and all match. N05 → SRNS-G1-VIRAL-002 is confirmed through
     `input_status_packet_id`.
   - **P2-3:** the guard now reads the hash from the cited sealing record.
   - **P2-4 (a)–(d):** addressed.
   - **P3-1 to P3-5:** addressed (18 scripts; the DLL is marked as a new
     identity; the KB Creator repository and commit are named; the pre-edit
     blob ID requirement is added; the language is declared).
8. **Second class of mismatches.** This is new. See P1-A.
   - `identity_scan.py` skips blobs that contain CR (`counts.blob_contains_cr
     = 315`). The packet does not analyse them.
   - I scanned them myself. 311 text-like HEAD blobs contain CRLF: 269 `.tsv`,
     28 `.txt`, 7 `.json`, 6 `.md`, and 1 `.html`.
   - For **268** of them, the **LF-normalised** hash is referenced in a
     tracked file and the raw (CRLF) hash is not.
     - All 268 are referenced from their own run folder.
     - 263 are attributed by basename within ±6 lines. The other 5 are the
       OBR-002 TSVs, which are keyed by sample ID.
   - Example: `core_0_1_text_extraction_012_016_020_method_family_G1_VIRAL_001/raw_ocr/p012_full_columns_scale2_psm6/p012/01_left_column.tsv`.
     - **Sealed:** `2A663A4A…` in `012_016_020_method_family_manifest.md:25`.
       Its producer hashes the raw file (`sha256_file`, line 239).
     - **NRI blob** `3578e7d4…` (in `aab6ffa7` and NRI HEAD): LF, hash
       `2A663A4A…`, so it **matches the seal**.
     - **Sourcefold blob** `2eff1637…` (from import `c557381`): CRLF, hash
       `67439E9D…`. This equals the NRI **working-tree** bytes on this
       machine, where `core.autocrlf=true` and the attribute is
       `text=auto`.
   - **Blob comparison**, Sourcefold `c557381` against NRI `22fafc14`, over
     3974 common paths: **280 blobs differ**.
     - 6 are the intended guidance edits.
     - 269 are `.tsv`.
     - 5 are tooling files: 2 `.ps1`, `.gitignore`, `.html`, and `.mjs`.
   - **Effect of the standalone export.** The export carried autocrlf-converted
     working-tree bytes into the Sourcefold blobs.
     - It broke 268 sealed LF identities that are intact in the NRI Git
       history.
     - `release.md:15` says "byte-identical to the source working tree". That
       is literally true, but it hides this effect.
9. **OBR-002 log column.** The `Log SHA-256` values for all 5
   `GS-G1-VIRAL-00N.log.txt` files match none of these forms: raw, CRLF, or
   CRLF without the final newline. The TSV column matches the LF form, which
   is the inverse class. The log mismatch is not explained by either
   line-ending class. See P2-A.

## Findings

### P1 (blocker)

**P1-A. An inverse byte-identity class is unanalysed, so the "full scope"
claims and the T1 Definition of Done overclaim.**

- **What the packet misses.** §3.3 and F3 present 186 files as the full scope
  of sealed-identity mismatch, but the scan skipped every blob that contains
  CR.
- **The missed class.** There are 268 more governed evidence files whose
  sealed identity is the LF form while the tracked blob and the working tree
  are CRLF. They are mostly Tesseract TSVs across 13 run folders.
- **Cause.** The 2026-10-11 standalone export took NRI working-tree bytes
  from a checkout with `core.autocrlf=true`. The NRI Git blobs still match
  the seals.
- **Consequences:**
  - The T1 Definition of Done says the "generic consistency check" reports
    "0 unexpected mismatches". As designed, `identity_attribute.py` cannot
    see this class, so the check would report 0 while 268 sealed records
    still mismatch.
  - §9 T1 item 2 says the export was "byte-identical to the NRI working tree
    … i.e. LF". That is false for these files, which are CRLF.
  - The §3.4 statement that "Git stored LF" and "every later checkout produces
    LF" is incomplete. The export itself created CRLF blobs.
  - This class cannot be repaired by an attribute change alone. A CRLF blob
    is not converted to LF on checkout. A repair would mean committing new
    blobs equal to the NRI blobs, a different and heavier authorization than
    T1's "blobs unchanged". The user should see it before choosing the next
    task.
- **Required fixes:**
  - extend the scan to blobs that contain CR, in both directions;
  - report the 268 files (or the corrected count) as a classified, separate
    class;
  - correct the `release.md:15` wording and the §3.4 wording;
  - scope the T1 Definition of Done and the guard to the 182 paths, or make
    the generic check cover both directions with an explicit allow-list for
    the known 268;
  - in §10, add a user decision on whether to fix the inverse class (as a
    follow-up task or together with T1).

### P2 (must fix before acceptance)

**P2-A. Mismatches outside both classes are not acknowledged.** The 5 OBR-002
`Log SHA-256` rows match no LF or CRLF form of the tracked log files (verified
for all 5). The `identity_*` approach only detects hashes that equal an LF or
CRLF transform. It cannot see stale or other-cause mismatches.

The packet should say that its consistency check is limited to line-ending
identities, list this known residual, and avoid any implication that T1, or
T1 plus the inverse fix, restores full seal consistency.

### P3 (nits)

- **P3-A.** "49 across 15 other folders" is 13 folders plus 2 files at the
  root of the render trial: `provisional_region_map_report.md` and
  `render_output_manifest.md`.
- **P3-B.** `plan.md` was not updated. R1 still shows `in progress`, and
  neither R1b nor the v2 deliverables are listed.
- **P3-C.** `evidence/crlf_identity_registry_candidate.json`, which the
  immutable R1 receipt cites, is gone. Its content is now
  `superseded_first_layers_31_paths.json` (17062 bytes, SHA-256
  `1DA01E28…CA3B`). Record the rename in `context.md` so the R1 receipt's
  reference can be resolved.
- **P3-D.** Materialization script: when `git rm --cached` is followed by
  `git checkout HEAD --` in a user's checkout, an interruption leaves staged
  deletions behind. The script should refuse to run on dirty or
  locally-modified registry paths, and it should either restore the index
  when it fails or use a single-step equivalent such as removing the working
  file and then running `git checkout HEAD -- <path>`.

## Recommendation

**NOT OK.** The R1 findings (P1-1, P2-1 to P2-4, P3-1 to P3-5) are resolved
and independently confirmed, and the 182-path T1 experiment reproduces. The
packet still presents an incomplete picture of sealed byte identity: the
inverse class created by the export (P1-A) changes what T1's Definition of
Done can claim, and it adds a decision the user must make. Fix P1-A and P2-A,
then request re-review. The P3 items can be fixed together with them.
