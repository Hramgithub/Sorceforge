# Core 0.1 P002 Fresh OCR Scoring Decision Plan

Lane: `C01TEP002FRESHDECIDE-G1-VIRAL-001`

Status: `completed`

## Scope

- Consume committed `C01TEP002FRESHSCOREAUD-G1-VIRAL-001` report/summary/manifest by exact hash.
- Consume page `002` PSM `4` and PSM `6` candidate texts by exact hash.
- Consume the human-verified P002 assisted-draft report/summary/manifest as comparison evidence.
- Select the best current candidate and decide whether it can clear fresh OCR success.

## Boundaries

- No OCR/Tesseract execution.
- No fresh OCR success or bridge removal.
- No accepted text, semantic map, page-status, source, or raw mutation.
- No fixture admission, production assembly, page `021+`, push, promotion, acceptance, or downstream execution.

## Result

- Best candidate: `psm4`.
- PSM `4` metrics: sequence similarity `0.996182`, token recall `0.985507`.
- PSM `6` metrics: sequence similarity `0.307332`, token recall `0.978261`.
- Strict threshold: `0.997` for both sequence similarity and token recall.
- Decision: `remediation_required_before_fresh_ocr_success`.
- Fresh OCR success pages: `[]`.
- Bridge removed pages: `[]`.
- Promotable pages: `[]`.
- Next action: `bounded_p002_candidate_remediation_from_best_candidate_and_visual_verified_diffs`.

## Output Hashes

- `p002_fresh_ocr_scoring_decision_report.json`: `C745B2EBF02001D0F4ACD4AD836DFC534C59B799911A2FAB96785CBB3F50471B`
- `p002_fresh_ocr_scoring_decision_summary.md`: `7B72F72E6480BDDDD6FF61947F2425F8BB0E5DF8446AF1EEA56F3EDF02CD3D50`
- `p002_fresh_ocr_scoring_decision_manifest.md`: `0283F681EE24683AA6BBC6EA1F2818F7DC9680E6DCB8D56B1D91FCE476260713`
