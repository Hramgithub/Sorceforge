# Source Reconstruction Candidate Remediation - SRCR-G1-VIRAL-001

Status: `remediation_triage_only`

Boundary: no OCR, PDF parsing, raw-output edits, source acceptance, QA acceptance, fixtures, translation, proofreading, implementation, or Gate 1 advancement.

## Summary

- Candidate records: `5`
- Ready for later human review: `1`
- Needs overlay verify: `2`
- Needs crop remediation: `2`
- Visual-QC-only records: `2`

## Record Triage

| Region admission | Status | Next action |
|---|---|---|
| `SRA-G1-VIRAL-001-R001` | `blocked_visual_component` | `visual_crop_remediation` |
| `SRA-G1-VIRAL-001-R002` | `cleanup_candidate_needs_overlay_verify` | `overlay_verify_after_cleanup` |
| `SRA-G1-VIRAL-001-R003` | `blocked_overbroad_crop` | `narrow_contents_crop_remediation` |
| `SRA-G1-VIRAL-001-R004` | `text_clean_needs_overlay_verify` | `overlay_verify` |
| `SRA-G1-VIRAL-001-R005` | `candidate_ready_for_later_human_review` | `carry_forward` |

## Next

Create a separate bounded crop/overlay remediation authorization before any new OCR or human source review.
