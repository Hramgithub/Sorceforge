# Core 0.1 P009 OCR Smoke Remediation Matrix

Matrix id: `C01TESRM-G1-VIRAL-001`

Status: `candidate_only_p009_remediation_matrix_completed`

Boundary: P009-only remediation matrix over read-only text-evidence crop PNGs.

Baseline similarity: `0.460269`.
Best candidate: `trim_mask_psm4`.
Best similarity: `0.9993`.
Improvement over baseline: `0.539031`.
Recommendation: `candidate_only_remediation_improves_control_stand_continue_same_scope`.

Preserved limits:

- No page 009 source/review/reference/accepted-text overwrite.
- No page 021+ processing or authorization.
- No PDF parsing/text-layer extraction.
- No render execution.
- No source/OCR/render/PDF/raw mutation.
- No runtime implementation/start.
- No translation/proofreading/push.

Top variants:

| Rank | Candidate | Similarity | Token recall |
|---:|---|---:|---:|
| 1 | `trim_mask_psm4` | `0.9993` | `0.996324` |
| 2 | `grayscale_psm4` | `0.9993` | `0.996324` |
| 3 | `denoise_sharpen_psm4` | `0.999124` | `0.992647` |
| 4 | `split_denoise_sharpen_psm4` | `0.999124` | `0.992647` |
| 5 | `trim_mask_psm11` | `0.998775` | `0.996324` |
| 6 | `grayscale_psm11` | `0.998775` | `0.996324` |
| 7 | `full_original_psm11` | `0.9986` | `0.996324` |
| 8 | `denoise_sharpen_psm11` | `0.9986` | `0.992647` |
