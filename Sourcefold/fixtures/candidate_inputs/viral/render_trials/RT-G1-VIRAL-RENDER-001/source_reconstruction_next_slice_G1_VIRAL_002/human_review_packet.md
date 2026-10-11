# Source Reconstruction Next Slice Review Packet - SRNS-G1-VIRAL-002

Status: `ready_for_bogdan_review_not_accepted`

Boundary: this packet contains page 002 visual crop references only. It creates no candidate text, source acceptance, QA acceptance, fixtures, Gate 1 advancement, OCR, PDF parsing, rendering, implementation, or push.

Original page reference:

- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/images/page_002.png`
- SHA-256: `ABC72B84D6CE89FE6C9B28981A39ADA33C5B9488B2864E8B35B41B120D6036C9`

## Numbered Questions

### 1 - PRM-G1-VIRAL-001-P002-R01

- Crop: `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_next_slice_G1_VIRAL_002/region_refs/1_SRNS-G1-VIRAL-002-R01__PRM-G1-VIRAL-001-P002-R01.png`
- Prompt: Transcribe/confirm the centered credits/legal-like text block, or mark blocker.
- Answer shape: `1 - text: <transcription> | 1 - blocker: <reason> | 1 - visual-only`

### 2 - PRM-G1-VIRAL-001-P002-R02

- Crop: `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_next_slice_G1_VIRAL_002/region_refs/2_SRNS-G1-VIRAL-002-R02__PRM-G1-VIRAL-001-P002-R02.png`
- Prompt: Decide whether the boxed/footer legal-like block is source text and transcribe it if yes.
- Answer shape: `2 - text: <transcription> | 2 - visual-only | 2 - blocker: <reason>`
