# Fixtures

This directory is reserved for future Sourcefold test fixtures.

The first fixture should be selected only after module contracts and acceptance
criteria are accepted. A fixture must record:

- source identity and license/usage assumptions;
- why it exercises reconstruction, translation, and proofreading contracts;
- expected accepted artifacts;
- known risks such as columns, tables, maps, handouts, cards, stat blocks, or
  image-embedded text.

No real book processing starts in the initial scaffold.

## Candidate Inputs

`candidate_inputs/viral/Call_of_Cthulhu_Viral.pdf` is stored as a Gate 1 pilot
candidate. `G1FADAR-G1-VIRAL-001` admits the bounded fixture groups derived from
the fixture manifest record only; it is not accepted source evidence, whole
Gate 1 acceptance, or permission to process the book beyond separately
authorized fixture checks. `G1WGARR-G1-VIRAL-001` rechecks readiness for a
future whole Gate 1 acceptance decision only; it does not broaden fixture
admission or authorize page `021+`. `G1WGADR-G1-VIRAL-001` accepts whole Gate 1
only for pages 001-020 and those admitted fixture groups; it still does not
authorize page `021+` or downstream book processing. `C01IPP-G1-VIRAL-001`
prepares Core 0.1 implementation planning from that scope only; it creates no
runtime implementation, OCR/render/PDF/raw/source mutation, translation,
proofreading, page `021+`, source-profile broadening, or push.
`C01IAR-G1-VIRAL-001` records implementation authorization receipt material
only; it does not authorize runtime implementation or downstream book
processing. `C01FSDP-G1-VIRAL-001` prepares first-slice design material only
for `C01WP-01-phase-1-scaffold-contracts`; it does not lock/accept a source
profile, process page `021+`, or mutate source/OCR/render/PDF/raw assets.
`C01SPLPR-G1-VIRAL-001` records source-profile parking only for the C01WP-01
design-prep boundary; it still does not authorize runtime processing.
`C01FSARP-G1-VIRAL-001` prepares first-slice Sol/Terra architecture review
material only for C01WP-01 and still does not authorize runtime processing.
`C01AMTR-G1-VIRAL-001` prepares acceptance-matrix claim/evidence trace review
material only for C01WP-01 and still does not authorize runtime processing.
`C01RSPLP-G1-VIRAL-001` records runtime source-profile parking for C01WP-01
authorization-prep only and still does not authorize runtime processing.
`C01RSAP-G1-VIRAL-001` prepares first-slice runtime authorization decision
context for C01WP-01 only and still does not authorize runtime processing.
`C01RSAD-G1-VIRAL-001` records a non-executing first-slice runtime
authorization decision for C01WP-01 only and still does not authorize runtime
processing.
`C01RSPLAD-G1-VIRAL-001` records a runtime source-profile
lock-or-acceptance decision for C01WP-01 only; it grants no runtime
source-profile lock/acceptance, keeps the runtime source profile parked, and
still does not authorize runtime processing.
`C01TETD-G1-VIRAL-001` completes a Sol/Terra-reviewed points 1-5 readiness
chain toward a future text extraction smoke trial; point 6 remains blocked
until Bogdan is called, and no OCR/PDF parsing/text-layer extraction or actual
text extraction is performed.
`C01TESP-G1-VIRAL-001` records the first bounded actual OCR smoke over page 009
text-evidence crop PNGs only, using frozen OCR candidate `OCM-G1-VIRAL-001`.
It writes candidate-only outputs in a separate directory, does not overwrite
page 009 assets, does not accept source/profile evidence, and keeps page `021+`
blocked.
`C01TESRM-G1-VIRAL-001` records a bounded P009-only OCR smoke remediation
matrix. Its best candidate-only profile is `trim_mask_psm4`; this is
remediation evidence only, not accepted source/profile evidence, and any next
smoke consideration remains limited to P010 or P015 unless separately
authorized.
`C01TESP010-G1-VIRAL-001` records a bounded P010-only same-profile OCR smoke
using the selected/recommended `trim_mask_psm4` profile from P009 remediation.
It writes candidate-only outputs in a separate directory, does not overwrite
P010 page-complete assets, does not accept source/profile/semantic/page-status
evidence, and keeps page `021+` blocked.
`C01TESP015-G1-VIRAL-001` records a bounded P015-only same-profile OCR smoke
using the same `trim_mask_psm4` profile after P010. It compares metrics-only
against `page_015_text_map.md`, writes candidate-only outputs separately, does
not overwrite P015 page-complete assets, does not accept
source/profile/semantic/page-status evidence, and keeps page `016+`/`021+`
blocked.
`C01TECPD-G1-VIRAL-001` closes the P009/P010/P015 same-profile smoke ladder
and freezes `trim_mask_psm4` only as a Core 0.1 text extraction candidate
profile for future config/replay decisions. It does not execute OCR, accept
source/profile/semantic/page-status evidence, create a runtime source-profile
lock, or authorize runtime processing.
`C01TEFPC-G1-VIRAL-001` records the reusable frozen config for that candidate
profile without running OCR. `C01TERSM-G1-VIRAL-001` then replays the frozen
config over exactly P009/P010/P015 text-evidence crops as candidate-only
regression evidence, without accepted/source/profile/runtime/page-status
mutation and without page `021+`.
`C01TEREP011-G1-VIRAL-001` records the first bounded replay expansion inside
pages `001-020` as P011-only. It reuses only the frozen `trim_mask_psm4` tuple,
does not broaden the frozen config allowed-pages policy, compares metrics
against `page_011_ocr_verified_text_map.md`, and writes only candidate metrics,
report, summary, and manifest outputs.
`C01TEOR020-G1-VIRAL-001` records a bounded `001-020` overview replay/report.
It records pages `001`-`008` as ineligible, reruns eligible pages `009`-`020`
with only the frozen `trim_mask_psm4` tuple, does not broaden the frozen config
allowed-pages policy, and writes only report/summary/manifest/metrics outputs.
Weak pages are `012`, `013`, `014`, `016`, `017`, `018`, `019`, and `020`;
P015 is reference-risk only because its reference is not OCR-verified.
`C01TEWDR-G1-VIRAL-001` records weak-page diagnostics plus a P018-only
remediation probe. It preserves diagnostic raw/prepared/candidate artifacts for
overview weak pages, selects `wide_edge_mask_trim_psm4_normal` as the best P018
candidate, and mini-replays that candidate on P017/P019/P014. The P018 fix is
candidate evidence only and is not a broad OCR/profile acceptance.
`C01TEP2P018P017-G1-VIRAL-001` records a P018/P017 crop-safe second pass. It
tests no-trim/extra-padding/soft-trim preprocessing variants with PSM 4/6/11,
keeps diagnostic artifacts in its own output directory, and finds no broad
OK-level candidate. The best shared candidate remains in the
`wide_edge_mask_trim` family.
`C01TEAS018017-G1-VIRAL-001` records a bounded P018/P017 auto-search over
bounding-box and column/line segmentation candidates. It exhausts its fixed
budget without finding an OK-level candidate; the tested bbox/line-band path
does not improve on the committed second-pass P018 result.
`C01TERG018017-G1-VIRAL-001` records a reference-guided repair candidate for
P018/P017. It uses committed OCR as support evidence and accepted text maps as
source of truth, reaching OK metrics while explicitly not constituting
independent OCR acceptance.
`C01TEFG017018-G1-VIRAL-001` records a full-page-derived geometry OCR probe for
P018/P017 after Sol/Terra rejected reference-guided repair as independent OCR
validation. It generates candidates from full-page PNG geometry and Tesseract
only, seals candidate hashes before scoring, and reaches OK-level candidate
metrics for both pages without reference-guided repair. The references remain
`reference_text_map_not_ocr_verified`, so this is candidate-only diagnostic
evidence, not source/profile/page-status acceptance.
