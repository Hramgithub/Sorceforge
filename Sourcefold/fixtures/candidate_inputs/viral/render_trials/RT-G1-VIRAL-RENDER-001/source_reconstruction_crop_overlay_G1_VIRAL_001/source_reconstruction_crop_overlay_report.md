# Source Reconstruction Crop/Overlay Remediation - SRCO-G1-VIRAL-001

Status: `crop_overlay_remediation_evidence_only`

Boundary: no OCR, PDF parsing, raw OCR output edits, source acceptance, QA acceptance, fixtures, translation, proofreading, implementation, or Gate 1 advancement.

Human review remains blocked. This package prepares exact crop/overlay references and one refined crop for a later bounded OCR run.

## Summary

- Candidate records: `5`
- Visual-QC records: `2`
- Ready for later human review: `1`
- Overlay references ready: `2`
- Refined OCR rerun required: `1`

## Record Remediation

| Region admission | Status | Next action | Artifact |
|---|---|---|---|
| `SRA-G1-VIRAL-001-R001` | `visual_component_demoted_from_text_review` | `keep_visual_qc_only_until_manual_visual_decision` | `fixtures\candidate_inputs\viral\render_trials\RT-G1-VIRAL-RENDER-001\source_reconstruction_crop_overlay_G1_VIRAL_001\crop_overlay_refs\SRA-G1-VIRAL-001-R001__visual_reference.png` |
| `SRA-G1-VIRAL-001-R002` | `noise_stripped_overlay_reference_ready` | `include_in_later_human_package_after_overlay_review` | `fixtures\candidate_inputs\viral\render_trials\RT-G1-VIRAL-RENDER-001\source_reconstruction_crop_overlay_G1_VIRAL_001\crop_overlay_refs\SRA-G1-VIRAL-001-R002__overlay_reference.png` |
| `SRA-G1-VIRAL-001-R003` | `narrow_subcrop_prepared_for_later_ocr_rerun` | `run_bounded_ocr_on_refined_crop_after_separate_authorization` | `fixtures\candidate_inputs\viral\render_trials\RT-G1-VIRAL-RENDER-001\source_reconstruction_crop_overlay_G1_VIRAL_001\crop_overlay_refs\SRA-G1-VIRAL-001-R003__narrow_contents_candidate.png` |
| `SRA-G1-VIRAL-001-R004` | `clean_text_overlay_reference_ready` | `include_in_later_human_package_after_overlay_review` | `fixtures\candidate_inputs\viral\render_trials\RT-G1-VIRAL-RENDER-001\source_reconstruction_crop_overlay_G1_VIRAL_001\crop_overlay_refs\SRA-G1-VIRAL-001-R004__overlay_reference.png` |
| `SRA-G1-VIRAL-001-R005` | `carried_forward_candidate` | `carry_forward_to_later_human_package` | `fixtures\candidate_inputs\viral\render_trials\RT-G1-VIRAL-RENDER-001\source_reconstruction_crop_overlay_G1_VIRAL_001\crop_overlay_refs\SRA-G1-VIRAL-001-R005__carry_forward_reference.png` |
| `SRA-G1-VIRAL-001-R006` | `visual_qc_reference_ready` | `keep_visual_qc_only_until_manual_visual_decision` | `fixtures\candidate_inputs\viral\render_trials\RT-G1-VIRAL-RENDER-001\source_reconstruction_crop_overlay_G1_VIRAL_001\crop_overlay_refs\SRA-G1-VIRAL-001-R006__visual_qc_reference.png` |
| `SRA-G1-VIRAL-001-R007` | `visual_qc_reference_ready` | `keep_visual_qc_only_until_manual_visual_decision` | `fixtures\candidate_inputs\viral\render_trials\RT-G1-VIRAL-RENDER-001\source_reconstruction_crop_overlay_G1_VIRAL_001\crop_overlay_refs\SRA-G1-VIRAL-001-R007__visual_qc_reference.png` |

## Next

Create a separate bounded refined OCR authorization for only the prepared refined crop(s), then rebuild the human review candidate package if evidence improves.
