# Sourcefold baseline debt and continuation audit — decision packet (v3)

- Goal: `20261012-sourcefold-baseline-debt-audit`
- Baseline: `98c2404ca894546326fc2f5b03d6db932e8d92bf` (`main` = `origin/main`)
- Date: 2026-10-12
- Version: v3.
  - v2 addressed R1 (`handoffs/R1-critic-review.md`; v1 wrongly gave the
    scope as 31 paths).
  - v3 addresses R1b (`handoffs/R1b-critic-rereview.md`): the reverse CRLF
    class of 268 TSV files, the OBR-002 logs, and refinements to T1.
- Status: candidate for re-review. It is not accepted and not released.
- Language: English, following the repository's goal-document convention. The
  summary for the user is in Russian, in chat.
- Boundary: read-only toward the repository. All runs and experiments were done
  only in an isolated scratch clone.
  - No OCR, `tesseract.exe` execution, render, PDF parsing, translation,
    proofreading, or network installs.
  - Evidence, tests, scripts, and acceptance state are unchanged.

## 1. Summary

| # | Finding | State |
|---|---|---|
| F1 | The recorded result (989 passed / 27 skipped / 13 failed) reproduces exactly on a clean clone. | verified |
| F2 | All 12 lineage failures belong to one class: **byte/line-ending identity**. The sealed hash is SHA-256 of the same content with CRLF line endings, but Git stores and checks out LF. The content itself has not changed. | verified |
| F3 | The problem is wider than the tests. Of the 3996 tracked blobs, the CR-free text blobs were checked (§3.3; CR blobs are in §3.6): **186** of them have a CRLF identity sealed elsewhere. Path attribution assigns **182** of them to CRLF and **4** to LF. Of 616 attributed references, **611** do not match the current working bytes. The tests reach only part of this set. | verified |
| F4 | Experiment: `text eol=crlf` for exactly those 182 paths in `Sourcefold/.gitattributes`. Blob IDs stay unchanged. Attributed-reference mismatches drop from 611 to **1**: the expected LF hash in the prose of the export R1 review. Full suite: **1 failed / 1001 passed / 27 skipped**. | verified (scratch only) |
| F5 | The Tesseract failure is a layering defect. A static pin test calls `verify_inputs()`, which requires the executable to exist. The test's static input hashes match 10 of 10. | verified |
| F6 | The NRI `.tools` copy on this machine matches the historical records for `tesseract.exe`, `eng.traineddata`, and `osd.traineddata` (hashes only, no execution). | verified |
| F7 | The import root and the Python environment are not declared. The only third-party dependencies are Pillow and pytest. | verified |
| F8 | A reverse class introduced by the standalone export: **268** tracked `.tsv` blobs in 13 OCR run folders are CRLF, while their seals and the NRI blobs (`22fafc14`) are LF. The export copied the NRI working tree under `core.autocrlf=true`, and NRI has no `eol` rule for `*.tsv`. No test catches this. | verified |
| F9 | In `ocr_benchmark_OBR-G1-VIRAL-002/ocr_output_manifest.md:60-64`, none of the 5 `Log SHA-256` values matches the log content in raw, LF, or CRLF form. Each log has a single NRI commit (`684a640019`). This is a content-level mismatch, not line endings, and its cause is not established. | verified, cause unknown |

## 2. Reproducing the test suite

- **Environment:**
  - CPython 3.12.14 (AMD64 build, running under Windows 11 ARM64 emulation)
    from NRI `.tools/python`;
  - pytest 9.1.1, installed offline with `uv 0.12.13` from the local uv cache;
  - Pillow 12.2.0, a local copy of the cp312-win_amd64 build from the NRI
    MinerU venv;
  - no network use.
- **Import root:** without `PYTHONPATH=<repo root>`, collection stops on
  `tests/test_page_review_crop_contracts.py` (`No module named 'Sourcefold'`).
- **First run:** `13 failed, 977 passed, 27 skipped, 12 errors`. The 12 errors
  are `PermissionError` on the sandboxed `Temp\pytest-of-user`. Rerunning
  those 12 with `--basetemp=<scratch>` gives 12 passed.
- **Reconciled total:** **989 passed / 27 skipped / 13 failed**, which matches
  the recorded result.
- Details: `evidence/pytest_summary.md`.

## 3. Lineage failures

### 3.1 Failing nodes, consumers, and authority

All 12 nodes are in `Sourcefold/tests/`. "Consumer" is the sealed record whose
pin fails. "Authority" is the `authorization_id` of that record. "Next sealed
consumer" is the record that consumed this consumer in turn. At the global
level, the scope of all these records is now covered by the bounded
`G1WGADR-G1-VIRAL-001` (pages 001–020). That decision does not supersede the
records themselves.

| ID | Node | Consumer (ID) | Authority | Next sealed consumer |
|---|---|---|---|---|
| N01 | `test_gate_1_review_decision.py::test_gate_1_review_decision_preserves_brief_lineage` | G1RD-G1-VIRAL-001 | BA-G1-VIRAL-GATE-1-REVIEW-DECISION-001 | G1SRER-G1-VIRAL-001 |
| N02 | `test_gate_1_review_decision_brief.py::test_gate_1_review_decision_brief_preserves_packet_lineage_and_boundaries` | G1RDB-G1-VIRAL-001 | BA-G1-VIRAL-GATE-1-REVIEW-DECISION-BRIEF-001 | G1RD-G1-VIRAL-001 |
| N03 | `test_gate_1_review_packet.py::test_gate_1_review_packet_preserves_lineage_and_boundaries` | G1RP-G1-VIRAL-001 | BA-G1-VIRAL-GATE-1-REVIEW-PACKET-001 | G1RDB-G1-VIRAL-001 |
| N04 | `test_gate_1_source_recon_evidence_rollup.py::test_gate_1_source_recon_rollup_preserves_decision_lineage` | G1SRER-G1-VIRAL-001 | BA-G1-VIRAL-GATE-1-SOURCE-RECON-EVIDENCE-ROLLUP-001 | G1SP-G1-VIRAL-001 |
| N05 | `test_gate_1_status_packet.py::test_gate_1_status_packet_preserves_rollup_lineage` | G1SP-G1-VIRAL-001 | BA-G1-VIRAL-GATE-1-STATUS-PACKET-001 | SRNS-G1-VIRAL-002 |
| N06 | `test_source_reconstruction_fixture_admission.py::test_fixture_admission_preserves_lineage_and_boundaries` | SRFA-G1-VIRAL-001 | BA-G1-VIRAL-SOURCE-RECON-FIXTURE-ADMISSION-001 | G1RP-G1-VIRAL-001 |
| N07 | `test_source_reconstruction_human_package.py::test_human_package_preserves_boundary_and_lineage` | SRHP-G1-VIRAL-001 | BA-G1-VIRAL-SOURCE-RECON-HUMAN-PACKAGE-001 | SRHR-G1-VIRAL-001 |
| N08 | `test_source_reconstruction_human_review.py::test_human_review_preserves_lineage_and_boundaries` | SRHR-G1-VIRAL-001 | BA-G1-VIRAL-SOURCE-RECON-HUMAN-REVIEW-001 | SRQA-G1-VIRAL-001 |
| N09 | `test_source_reconstruction_next_slice.py::test_next_slice_preserves_status_packet_and_region_lineage` | SRNS-G1-VIRAL-002 | BA-G1-VIRAL-SOURCE-RECON-NEXT-SLICE-001 | later page slices |
| N10 | `test_source_reconstruction_next_slice_004.py::test_page_004_next_slice_consumes_p003a_and_region_lineage` | SRCR-G1-VIRAL-004 | BA-G1-VIRAL-SOURCE-RECON-NEXT-SLICE-004 | later page slices |
| N11 | `test_source_reconstruction_qa.py::test_source_reconstruction_qa_preserves_lineage_and_boundaries` | SRQA-G1-VIRAL-001 | BA-G1-VIRAL-SOURCE-RECON-QA-001 | SRFA-G1-VIRAL-001 |
| N12 | `test_ocr_remediation_review_package.py::test_review_package_binds_exact_predecessors_and_hashes` | ORR-G1-VIRAL-001 | BA-G1-VIRAL-REMEDIATION-REVIEW-001 | G1 readiness/parking matrix (`gate_1_source_profile_readiness_parking_matrix.json:167`) |

### 3.2 First failing pin of each node

- Predecessor paths are relative to
  `Sourcefold/fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/`.
- The "Sealed" value is read from the consumer record field named in
  `evidence/lineage_trace.json`. It equals SHA-256 of the LF→CRLF transform of
  the current bytes.
- "NRI commit" is the only NRI commit of the predecessor, checked with
  `git log --all`.

| ID | Node | Predecessor | Sealed (CRLF) | Git LF | NRI commit |
|---|---|---|---|---|---|
| L01 | N01 | `gate_1_review_decision_brief_G1_VIRAL_001/gate_1_review_decision_brief_report.json` | `E577B18D7E8945C39FA5286D83FD9D8607B45636ABD82243ED4A9F002B306FE8` | `210CEC9E840D255E66012E8F65161BDE181A8A689C9BB94195ECAD1B18395775` | `8d172bae31` 2026-07-18 |
| L02 | N02 | `gate_1_review_packet_G1_VIRAL_001/gate_1_review_packet_report.json` | `AE3695954BE26DB60EB541CD9819532CE5CA98F961D0F0B21F06C0BE5F96D990` | `C31D5C7C41495FC50BC051211814969464744C95CBEA48F9006B6D484FB6FA10` | `514b9286c2` 2026-07-18 |
| L03 | N03 | `source_reconstruction_fixture_admission_G1_VIRAL_001/source_reconstruction_fixture_admission_report.json` | `485ECEAAC7CC1CC3FBE95341ED7A0F5E68345EF59CCC8CEB7F8F57706A541A1C` | `EC7E9E67B8C5354D0F28EB7540A513EDE9E89CD54B131BB00422B5BDF47EF992` | `7ca497a34e` 2026-07-18 |
| L04 | N04 | `gate_1_review_decision_G1_VIRAL_001/gate_1_review_decision_report.json` | `8F1FD747C95B758B2227C6483B09D34DB37A786B7988DA68EEB721A7942547C3` | `7030C9071843E84665CC0875803C76483AEF752032425088B87577EECF6F0C5B` | `3369b6c627` 2026-07-18 |
| L05 | N05 | `gate_1_source_recon_evidence_rollup_G1_VIRAL_001/gate_1_source_recon_evidence_rollup_report.json` | `CDF75D022DC29D0594CA441F02EDA2DC50CE9C0C4BA81F5C51523745318A4AEB` | `51C921F5A7C309A7FD2F49D4F7E2C29E0CF8B3CE3647A593B9722C44A8E90189` | `bd9e3e596f` 2026-07-18 |
| L06 | N06 | `source_reconstruction_qa_G1_VIRAL_001/source_reconstruction_qa_report.json` | `A98811F3368FD468618A111D9F7A85BFFBD72CE9387CCF11DA011875C80553E0` | `4DE4C1D1C1C6B628FC9B2126575BC3991A8115622ECE980FCFE648A887420841` | `1d6b5a81f9` 2026-07-18 |
| L07 | N07 | `source_reconstruction_visual_overlay_review_G1_VIRAL_001/source_reconstruction_visual_overlay_review_report.json` | `54ABBA9FA01B8AFECB2C2B4FD12EE4FCFD2EDA5B0B2948FB4A2D4C17238E2BF8` | `6FB393283FE89AB95B91675A49EF56CA292F6E7CEDBAEB7C666789B1E301141B` | `b001cbdf1d` 2026-07-18 |
| L08 | N08 | `source_reconstruction_human_package_G1_VIRAL_001/source_reconstruction_human_package_report.json` | `2A5A475737BF6442B11DFB26CE6E62724978B9F797E37A8BAB843BF2534017CC` | `3436CD54C19ECA3FAA9E0736D7198F4EC40EB0785934F6E7AAB3CC27B1C35175` | `8d53e8ad35` 2026-07-18 |
| L09 | N09 | `gate_1_status_packet_G1_VIRAL_001/gate_1_status_packet_report.json` | `4F0AD3C7553863636B6FD15E329815EE26E62329D668C9FA8AC756CE04B24644` | `66BC6288459AA5F7131FF7878F37314B9A04D4FB44F0F61E803887C2A528A934` | `a9971239d3` 2026-07-18 |
| L10 | N10 | `provisional_region_map_report.md` | `A37F734D9D1B9DA1456FE7C3D5804D70FE352DB7197495843561B40D7A4DD35C` | `5F7394F6A230A2944B851C2C8E363862A67A1F61081453B4082B02F744370862` | `4a51b975a6` 2026-07-18 |
| L11 | N11 | `source_reconstruction_human_review_G1_VIRAL_001/source_reconstruction_human_review_report.json` | `FF7C9778E711D67964584CD00870762FD7ADE47E4368EA71DD3C373AB5EB4980` | `12A3BFCA1A0B705DB7E93A4D9B385126D278D778359ED5537128A7637EA14320` | `aa218f9b8b` 2026-07-18 |
| L12 | N12 | `ocr_remediation_matrix_G1_VIRAL_001/ocr_remediation_matrix_report.json` | `3A454433ABA46E237D091F5BB4DA6EB8B73FCEE400935AF10BB0DC5731F212F5` | `16418A1BA27C36D7F14F89545B89297002022117C507448EFCEA82BA74758AB3` | `f90d170ba2` 2026-07-18 |
| L13 | N12 | `ocr_remediation_matrix_G1_VIRAL_001/ocr_remediation_matrix_rows.json` | `B0077249E070E6673E12F4A8B83C542DFD400A8200C558ACED4A0C47C284FD66` | `00682A35933E0256BFBBBC2B22340993372288B16EE850FDEFA189A1FA4F556C` | `f90d170ba2` 2026-07-18 |
| L14 | N12 | `ocr_remediation_matrix_G1_VIRAL_001/ocr_remediation_output_manifest.md` | `135751E4C7DE4BE6582AD91387CAEA6E20415865D183A67874F950935AF117F7` | `396B3FE6B5126FF67432AEA1B84DE9A500449EFF6C7DAA35127C41E788C8E066` | `f90d170ba2` 2026-07-18 |
| L15 | N12 | `ocr_remediation_matrix_G1_VIRAL_001/ocr_remediation_plan.json` | `A56165FE767A5752B150E72E687BF2D115571906A6E77D81ECDCC0734A75DC47` | `87741F8CF719662A781E181CDAA4C22A294599C8797FE2064AF4A7A2A9DCEF15` | `f90d170ba2` 2026-07-18 |

Each node pins several files (report, JSON, Markdown, manifest), and the first
mismatch hides the ones after it. Going down the failing tests to a fixed point
reaches 31 paths (`evidence/eol_iterate_observations.json`). v1 wrongly called
this the full scope. That list is now kept as
`evidence/superseded_first_layers_31_paths.json`.

### 3.3 Full scope: every sealed CRLF identity

Method (`evidence/identity_scan.py`, `evidence/identity_attribute.py`):

1. For each tracked text blob at `98c2404` that has LF and no CR, compute the
   LF identity (blob bytes) and the CRLF identity (LF→CRLF).
2. Find every 64-hex token in the other tracked files.
3. Attribute a reference to a path when either:
   - the content is unique (only one tracked path has that blob); or
   - for duplicated content, the path's base name appears within ±6 lines of
     the token.

Results (`evidence/identity_scan_98c2404.json`,
`evidence/identity_attribution_98c2404.json`):

| Category | Files | Decision |
|---|---:|---|
| CRLF identity attributed by path | 176 | CRLF |
| Both: `gate_1_review_decision_brief_report.json`. The LF reference is the prose at `20261011-sourcefold-standalone-export/handoffs/R1-release-review.md:76`, which describes this mismatch and does not seal anything. | 1 | CRLF (reviewed) |
| Not attributed automatically: `ocr_benchmark_OBR-G1-VIRAL-002/raw_outputs/GS-G1-VIRAL-00{1..5}.stderr.txt`. The rows of `ocr_output_manifest.md:60-64` are keyed by sample ID, and their `Stderr SHA-256` column is the CRLF identity. | 5 | CRLF (reviewed) |
| LF identity attributed by path: 4 stderr files in `core_0_1_text_extraction_geometry_probe_..._G1_VIRAL_002` and `..._weak_page_diagnostics_p018_remediation_G1_VIRAL_001`, sealed as LF by their own manifests. Identical content in the matrix run is sealed as CRLF (a content collision, not a contradiction). | 4 | leave LF |
| **Total** with a CRLF identity referenced anywhere | **186** | 182 CRLF / 4 LF |

Other numbers:

- **Baseline working tree:** 616 attributed references, **611 mismatched**.
- **After the scratch experiment** (182 paths with `eol=crlf`):
  **1 mismatched**, which is the R1 prose reference above
  (`evidence/identity_attribution_after_t1_experiment.json`).
- **Candidate list:** `evidence/t1_candidate_set.json`. For every path it
  records the basis and the sealing references (file:line). These references
  are the authority for T1; a derived hash is not.

Limitation of §3.3: the scan covered only blobs without CR. Blobs that
contain CR are analysed in §3.6. The consistency check covers only line-ending
identities. Content-level mismatches (F9) are outside its scope.

### 3.4 Classification and earliest failing layer

| Class | Applies? | Justification |
|---|---|---|
| historical supersession | no | Every one of the 31 failing-chain predecessors has exactly one NRI commit (`git log --all`). |
| byte/line-ending identity | **yes, all 12** | The sealed value equals SHA-256(LF→CRLF(blob)) for all of them, and the LF blobs contain no CR. |
| stale sealed evidence | no | The record correctly describes the bytes it was sealed against. |
| implementation defect | yes, historical, in the producer layer | See below. |

**Earliest failing layer:** the byte-identity contract between the producers
and the repository attributes, 2026-07-18.

1. **Producers wrote CRLF.** Producers of that period call `Path.write_text()`
   without `newline=`, which writes CRLF on Windows. Downstream producers then
   hashed the CRLF working bytes and sealed those hashes.
2. **Git stored LF.**
   - For JSON and Markdown outside `-text` folders, the cause is the NRI rule
     `*.json text eol=lf` / `*.md text eol=lf`, present since `fb1bfa1d`
     (2026-06-16). Git normalized those files to LF.
   - For `ocr_remediation_matrix_G1_VIRAL_001/**`, NRI `f90d170b` added
     `-text -diff` in the same commit as the files, yet none of the 324
     text-like files contains CR. Normalization therefore happened before that
     attribute took effect. **The exact mechanism for this folder is not
     established.** Only the result is observed: the blobs are LF and the seals
     are CRLF.
3. **Later checkouts produce LF.** Every later checkout writes LF, so the seals
   no longer match.

**Defect class still present:** 18 of 184 scripts in `scripts/` contain at
least one `write_text` call without `newline=` (AST scan
`evidence/write_text_scan.py`). This includes `run_ocr_remediation_matrix.py`
(lines 178, 179, 296, 493) and `run_source_reconstruction_refined_ocr.py`.

### 3.5 Test files are pinned and must not be edited

The current LF hash of **10 of the 12** failing test files is pinned elsewhere
in the repository:

- **8 through their own consumer.** The `test_contract_sha256` field of the
  consumer record pins them.
- **`test_gate_1_status_packet.py`** through
  `gate_1_status_packet_G1_VIRAL_002/gate_1_status_report.json`, plus
  `roadmap.yaml` and `bounded_trial_authorizations.md`. Its own consumer
  G1SP-G1-VIRAL-001 pins an older version: `263C5815…` is the LF hash of
  `a9971239d3`, while the test changed in `b8322bffbb` (2026-07-25). That test
  checks only that the field is not empty, at line 78.
- **`test_source_reconstruction_next_slice.py`** through
  `source_reconstruction_next_slice_G1_VIRAL_002` (`test_sha256`, its
  manifest), `roadmap.yaml`, and `bounded_trial_authorizations.md`.
- **Not pinned:** `test_ocr_remediation_review_package.py` and
  `test_source_reconstruction_next_slice_004.py`.

Conclusion: the fix must not edit the tests.

### 3.6 Reverse class: CRLF blobs introduced by the export

Method: `evidence/cr_blob_scan.py` and `evidence/tsv_and_log_check.py`. The
scan covers all 315 tracked text blobs that contain CR at `98c2404`. It
compares the raw identity and the CRLF→LF identity with references in the
repository, and it compares each blob with the NRI blob at the export source,
`22fafc14942e925b2e5f088f3c7ab1cd8efe3003`.

| Category | Blobs | NRI blob |
|---|---:|---|
| Sealed by raw (CRLF) bytes, as intended (`-text` folders from the start) | 36 | identical |
| Sealed by the **LF** form while the tracked blob is CRLF | **268** | LF, and equal to the seal in all 268 cases |
| Not referenced, and the blob differs from NRI (LF there) | 6 | LF |
| Not referenced, blob identical to NRI | 5 | identical |

- **What the 268 are:** all `.tsv` files (Tesseract TSV) in 13 OCR run
  folders: second_pass 72, smoke_p009 remediation matrix 46,
  weak_page_diagnostics 46, geometry_probe_G1_VIRAL_002 30, auto_search 28,
  full_page_geometry_probe 12, method_family 8, replay_regression_smoke 8,
  p013_noexp 5, OBR-002 5, smoke_p010 4, smoke_p009 2, smoke_p015 2.
- **Cause:** the NRI working tree held CRLF for `*.tsv` (`* text=auto` with
  `core.autocrlf=true`, and no `eol` rule for TSV). The standalone import
  copied working-tree bytes and committed them as blobs under the root
  `* -text`.
- **The export receipt is accurate as written.** `release.md:15` says "byte
  identical to the source working tree", and that is literally true. These are
  not the NRI blob bytes, and they are not the bytes the TSV seals were made
  from. (The v2 wording "i.e. LF" was wrong.)
- **Who is affected:** no test reads these seals, which is why the suite does
  not catch the problem.
- **What a fix requires:** new blobs. An attribute rule cannot convert
  CRLF→LF on checkout. The fix is to commit the NRI blob bytes from
  `22fafc14` for the 268 paths. This needs its own user decision (T1b).
- **The 6 unreferenced blobs that differ from NRI** split into two groups:
  - **Evidence:** 1 file,
    `core_0_1_text_extraction_geometry_probe_..._G1_VIRAL_001/raw_ocr/full_page_triage_boxes_expanded_psm4/p012/01_p012_b001_tes.tsv`.
    It has the same autocrlf mechanism and is decided together with T1b.
  - **Tooling:** 5 files, decided **separately** from T1b:
    - `Sourcefold/.gitignore`
    - `docs/roadmap/roadmap_viewer.html`
    - `tools/roadmap-validator/validate-roadmap.mjs`
    - `scripts/documentation_checkpoint.ps1`
    - `scripts/validate_roadmap.ps1`

    The two `.ps1` files got CRLF from NRI's `*.ps1 text eol=crlf` rule, not
    from autocrlf.

## 4. Tesseract-dependent failure

- **Node:** `tests/test_core_0_1_text_extraction_012_016_020_method_family.py::test_012_016_020_pre_output_scope_and_pins`.
- **Cause:** `verify_inputs()`
  (`scripts/build_core_0_1_text_extraction_012_016_020_method_family.py:138-158`)
  checks `TESSERACT.exists()` (line 142) before running the static checks.
  `TESSERACT = overview.TESSERACT = D:\NRI\.tools\tesseract\tesseract.exe`.
- **Static inputs:** the 10 entries of `INPUT_HASHES`, checked without the
  executable (`evidence/static_pins.py`), give 10 match, 0 mismatch.
- **Classification:** a layering defect (a static test depends on runtime
  presence) plus runtime portability debt. It is not an evidence mismatch.
- **Pins:** neither the script nor its test is pinned by hash in any tracked
  file (0 references).

### 4.1 Tesseract identity on this machine

| Object | Historical record | `C:\_Hobby\_work\NRI\.tools\tesseract` |
|---|---|---|
| `tesseract.exe` | `BABB405F4366B480D02CD8FF2BAC8D497170F6C1711CE6F3D5D8BF0FB7FA6ED9` (`source_reconstruction_refined_ocr_report.json`) | same |
| `tessdata/eng.traineddata` | `7D4322BD2A7749724879683FC3912CB542F19906C83BCC1A52132556427170B2` (`ocr_candidate_manifest.md:31`) | same |
| `tessdata/osd.traineddata` | `9CF5D576FCC47564F11265841E5CA839001E7E6F38FF7F7AACF46D15A96B00FF` (`ocr_candidate_manifest.md:32`) | same |
| version | `tesseract v5.4.0.20240606` | NRI `tool-manifest.json` (2026-07-08) records the same version; the executable was not run |
| `libtesseract-5.dll` | **no historical record** | `279488C41BD341EDAA03DCD097FAA33604BA330E6254AC97BCAF2229D8D7AC1A`. This is a new identity, not a historical one. |

The historical identity can be reproduced only for the recorded objects.
Pinning the DLL would add a new identity.

## 5. Proposal: portable OCR runtime binding

This proposal adopts KB Creator decision D4. Source: the separate KB Creator
repository, local checkout `C:\_Hobby\_work\kb_creator`, file
`kb_creator/docs/plans/20261011-standalone-hardening/decisions.md` at commit
`f6cf348`. That decision is accepted for KB Creator only and does not transfer
automatically. For Sourcefold, its use rests on the user's decision of
2026-10-12 (plan.md, item 6).

1. **Tracked pin** `Sourcefold/runtime/ocr_runtime.pin.json`, schema
   `sourcefold_ocr_runtime_pin.v1`.
   - It records the engine, the version string, and relative paths with
     SHA-256 for `tesseract.exe`, `eng.traineddata`, and `osd.traineddata`.
     These are historical identities.
   - It records `libtesseract-5.dll`, explicitly marked as a new identity.
   - It contains no absolute paths and no machine name.
2. **Local binding** (not tracked): `Sourcefold/runtime.local.json`,
   `--tools-root`, or `SOURCEFOLD_TOOLS_ROOT`, with precedence CLI > env >
   file. There is no `PATH` search and no default.
3. **`scripts/ocr_runtime_binding.py`:**
   - `resolve_static()` checks the root, rejects reparse points and anything
     outside the root, and hashes every pinned file. It executes nothing. It
     fails closed before any output root is created.
   - `resolve_for_authorized_run()` runs `--version` and sets
     `TESSDATA_PREFIX` explicitly. It is called only inside an action that has
     its own bounded authorization.
   - The run records its runtime identity.
4. **Static and runtime checks stay separate.** Static tests do not require
   the executable.
5. **Historical scripts and receipts are not rewritten.** `D:\NRI` stays in
   them as provenance (see §6).

## 6. Recommendation on question 5: editing scripts that name `D:\NRI`

**Facts:**

- 21 scripts name `D:\NRI\...\tesseract.exe`, either directly or through
  `overview.TESSERACT`.
- 2 of them are pinned by hash:
  - `build_core_0_1_text_extraction_frozen_profile_config.py` (1 reference);
  - `build_p002_completion_and_next_review.py` (4 references).
- The other 19 have no hash pins, but they are referenced by path as
  provenance.
- Many of these producers refuse to overwrite an existing output root. This
  was checked for some of them, **not all 21**.

**Recommendation:**

- **Do not rewrite historical producers en masse.** A new OCR run gets a
  successor producer with `ocr_runtime_binding`, a new authorization, and a
  new output root.
- **Allow a narrow exception** for scripts without hash pins, and only to
  separate the static check from the runtime check. Example:
  `build_..._012_016_020_method_family.py`, where the `exists()` check moves
  from `verify_inputs()` onto the execution path.
  - Before the edit, record the script's blob ID (`git ls-files -s`) and
    SHA-256 in the successor record, because the path is cited as provenance.
  - Check again that the script has no hash references.
  - Keep `--execute` fail-closed.
- **Forbid edits to the two pinned scripts.**

## 7. Proposal: Python dependency declaration

This adopts KB Creator decision D6 (same source and same caveat as §5):
`pyproject.toml` + `uv.lock` on Python 3.12.x.

- **`Sourcefold/pyproject.toml`** goes next to `package.json`:
  - `requires-python = ">=3.12,<3.13"`;
  - `dependencies = ["pillow==12.2.0"]`;
  - dependency group `test` = `pytest==9.1.1`;
  - `[tool.pytest.ini_options]`: `testpaths = ["tests"]`,
    `pythonpath = [".."]` (declares the import root),
    `addopts = "-p no:cacheprovider"`.
- **`Sourcefold/uv.lock`** is a universal lock with hashes. Creating it
  requires network access, which needs separate permission.
- **The venv and `uv` are not tracked.**
- **Interpreter matrix:** verified on CPython 3.12.14 AMD64 under ARM64
  emulation. Native ARM64 is not verified. Python 3.14 is outside the
  supported range.
- **Update `SETUP.md`.**

## 8. Map of the 001–020 lanes (do not mix)

| Layer | Record | Content |
|---|---|---|
| Original first pass | `core_0_1_text_extraction_first_pass_runtime_selector_run_001_020_G1_VIRAL_001/first_pass_runtime_selector_run_001_020_report.json` | Fresh OCR executed: `009`, `010`, `011`, `015`. Selected candidates materialized: `012`, `013`, `016`, `017`, `018`, `020`. Bridge lineage: `001`–`008`, `014`, `019`. `all_pages_fresh_ocr_success=false`, `production_ready=false`. |
| Bounded Gate decision | `G1WGADR-G1-VIRAL-001` | Whole Gate 1 accepted only for pages 001–020 and the `G1FADAR-G1-VIRAL-001` fixture groups. The global roadmap Gate 1 is `active`. |
| P002 successor | `C01TEP002FRESHPASS-G1-VIRAL-001` | `fresh_ocr_success_pages=["002"]`, `bridge_removed_for_pages=["002"]`, `promotable_pages=["002"]` after bounded human-backed remediation. No acceptance and no production. |

## 9. Recommended next bounded task

### T1 — Restore the sealed byte identity of evidence (`BIR-G1-VIRAL-001`)

**Changes:**

1. **`Sourcefold/.gitattributes`.** Append `text eol=crlf` for exactly the 182
   paths in `evidence/t1_candidate_set.json`, at the **end** of the file.
   - The rules must go in this file and not the root one: the deeper file
     overrides the root, and the later line wins.
   - All 182 paths currently have `text: unset`, from the root `* -text`
     ("preserve imported evidence bytes").
   - Of these, 128 are in `ocr_remediation_matrix_G1_VIRAL_001/` and 1 is in
     `source_reconstruction_prep_G1_VIRAL_001/`. Both folders carry an
     explicit `-text -diff` rule, and the matrix rule's comment says "Preserve
     generated OCR remediation evidence exactly".
   - T1 overrides these rules only for paths that have a cited CRLF seal.
     Distribution: 128 in the matrix folder, 5 in OBR-002, 47 across 13 other
     folders, and 2 files at the render-trial root
     (`provisional_region_map_report.md`, `render_output_manifest.md`). See
     `evidence/t1_candidate_set.json`.
   - Justification: the "preserved" bytes are the ones the records sealed.
     The LF blobs had already been normalized before `-text` took effect: none
     of the 324 text-like files in the matrix folder contains CR (§3.4).
   - The 4 LF paths (§3.3) are not included.
2. **Successor record `BIR-G1-VIRAL-001`.** Machine JSON plus a short MD, in a
   new folder under the render-trial root. For each path it records:
   - the Git blob, the LF and CRLF SHA-256, and the NRI commit;
   - the **cited sealing records (file:line)** and the reviewed decision, where
     one was needed.

   It also states which identity is canonical for which use:
   - for working-tree bytes and sealed records, the CRLF identity;
   - for Git storage (blob ID, `git show`, any reader of raw blob bytes), the
     LF identity stays, and both remain valid.
   - Whether `git archive` honours `eol` must be checked in T1 and recorded.

   It also records that the export statement in `release.md:15` ("byte
   identical to the source working tree") remains a true historical claim
   about the export. The NRI working tree did not equal the NRI blobs at
   either end: CRLF for these 182 files at sealing time, and for `*.tsv` see
   §3.6.
3. **Materialization script for existing checkouts:**
   `scripts/materialize_sealed_eol.py`.
   - Changing attributes does not rewrite files in an existing checkout.
   - The script, for the registry paths only, runs `git rm --cached` and then
     `git checkout HEAD --`, and verifies the hashes. This method was checked in
     the scratch clone.
   - **It refuses to start if any registry path is dirty**, in the working
     tree or in the index.
   - **On failure it restores the index**, so no staged deletions are left.
   - `SETUP.md` must document the step.
4. **Guard test (new file):**
   - For every registry path, the working bytes equal the hash **read from the
     cited sealing record**, not the hash computed by the registry.
   - `git check-attr text eol` returns `set` / `crlf` for every registry path.
     This also checks that the ordering against `-text` is correct.
   - The generic line-ending consistency check covers both directions: the
     §3.3 logic plus the §3.6 logic, turned into a test or tool. It reports
     zero unexpected mismatches. The allowlist is explicit and finite:
     - the R1 prose reference;
     - the 268 TSV files of §3.6, until T1b.

     The 5 OBR-002 log rows (F9) do not belong on this allowlist. This check
     cannot detect them, so they are recorded in the BIR record as a known
     residual content-level mismatch.
   - It fails closed if a path is missing or the attribute drifts.

**Unchanged:** Git blob IDs, the content of all evidence, existing tests,
expected hashes, reports, and manifests.

**Definition of Done**, checked on both a fresh clone and an existing checkout
after the materialization script:

- full suite: `1 failed (Tesseract) / 1001 passed / 27 skipped`, plus the new
  guard test;
- generic consistency check: 0 unexpected mismatches;
- the diff contains only `.gitattributes`, the BIR record, the materialization
  script, the guard test, `SETUP.md`, and the goal/status documents.

**Authorization:** a separate decision by the user is required. T1 changes the
working-tree bytes of 182 governed evidence files back to their sealed form;
the blobs stay the same.

### T1b: restore the NRI blobs for the 268 TSV files (separate decision)

- **Change:** commit the bytes of the NRI blobs from
  `22fafc14942e925b2e5f088f3c7ab1cd8efe3003` for the 268 paths in §3.6. All
  268 are LF and equal their seals. The 6 unreferenced blobs that differ from
  NRI need a decision of their own.
- **Content:** these are new blobs in Sourcefold. Only the line endings
  change. The record `BIR-G1-VIRAL-002` cites, for each path, the NRI blob,
  both hashes, and the sealing references.
- **Authority:** it directly changes committed bytes of governed evidence, so
  it needs a separate explicit user decision. It may be combined with T1 into
  one commit only on the user's explicit instruction.

### Follow-ups, in order (each a separate task)

- **T2:** the Python declaration (§7) and `SETUP.md`. Needs network for
  `uv lock`.
- **T3:** `ocr_runtime_binding` and the pin (§5), plus separating the static
  and runtime checks in the method-family script under the §6 rule. This
  removes the 13th failure without running OCR.
- **T4:** a shared LF writer for new producers, and a scanner test with an
  allowlist of the 18 legacy scripts (§3.4), which are not modified.

## 10. Decisions for the user

1. Approve T1 as the next task (182 paths; blobs unchanged).
2. Decide on T1b: restore 268 TSV blobs from NRI `22fafc14`. This creates new
   blobs; the content is unchanged and only line endings differ.
3. Decide whether to investigate F9 (the OBR-002 logs) as a separate task.
4. Allow network access for `uv lock` in T2.
5. Confirm the §6 rule: successor producers for OCR runs; narrow edits only to
   scripts without hash pins, recording their blob ID.

## 11. Evidence

| File | What it holds |
|---|---|
| `evidence/pytest_summary.md` | Runs and reconciliation, including the 182-path experiment |
| `evidence/lineage_trace.json`, `trace_lineage.py` | First layer and NRI history |
| `evidence/eol_iterate_observations.json`, `eol_iterate.py`, `eol_experiment.py`, `eol_apply_final.py` | Failing-chain layers (31 paths, superseded scope) |
| `evidence/superseded_first_layers_31_paths.json` | The v1 list, kept as superseded |
| `evidence/identity_scan_98c2404.json`, `identity_scan.py` | Full scan of 3996 blobs |
| `evidence/identity_attribution_98c2404.json`, `identity_attribution_after_t1_experiment.json`, `identity_attribute.py` | Path attribution and the consistency check before and after the experiment |
| `evidence/t1_candidate_set.json`, `eol_apply_set.py` | The 182/4 set with sealing references, and the experiment |
| `evidence/cr_blob_scan_98c2404.json`, `cr_blob_scan.py`, `tsv_and_log_check.py` | Reverse class (§3.6) and the OBR-002 logs (F9) |
| `evidence/static_pins.py`, `self_pins.py`, `file_history_match.py`, `write_text_scan.py` | Supporting checks |

The scripts are audit evidence, not project tools. They use this machine's
layout through their arguments. The `eol_*` scripts refuse to run outside a
scratch clone.
