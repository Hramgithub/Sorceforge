# Core 0.1 Implementation Planning Prep - C01IPP-G1-VIRAL-001

Status: `core_0_1_implementation_planning_prep_ready_for_review`

This packet prepares the Core 0.1 implementation planning transition after `G1WGADR-G1-VIRAL-001`.

It does not authorize or create runtime implementation.

## Accepted Input Scope

- Whole Gate 1 acceptance decision: `G1WGADR-G1-VIRAL-001`.
- Page range: `001`-`020`.
- Fixture admission decision: `G1FADAR-G1-VIRAL-001`.
- Positive fixture groups: `1`.
- Negative fixture groups: `4`.
- Page 021+ included: `false`.
- Source-profile acceptance beyond G1WGADR: `false`.

## Work Packages

- `C01WP-01-phase-1-scaffold-contracts`: Phase 1 scaffold and contract inventory (`candidate_first_slice`); authorized now: `false`.
- `C01WP-02-core-artifact-schema-contracts`: Core artifact schema contract planning (`candidate_after_scaffold`); authorized now: `false`.
- `C01WP-03-reconstruct-dry-contracts`: Reconstruct lane dry contract planning (`candidate_future_slice`); authorized now: `false`.
- `C01WP-04-ocr-profile-execution-authorization-prep`: OCR/profile execution authorization prep (`blocked_until_separate_authorization`); authorized now: `false`.
- `C01WP-05-translation-proofreading-future-lanes`: Translation and proofreading future-lane planning (`blocked_downstream`); authorized now: `false`.

## Boundary

- Runtime implementation: `false`.
- Implementation authorization receipt: `false`.
- OCR/render/PDF/raw/source mutation: `false`.
- Translation/proofreading: `false`.
- Page 021+ processing/authorization: `false`.
- Source-profile acceptance beyond G1WGADR: `false`.
- New or broader fixture admission: `false`.
- Push: `false`.

## Required Before Runtime Implementation

- `implementation_authorization_receipt_with_separate_human_authorization`
- `single_core_0_1_source_profile_lock_or_explicitly_parked_equivalent`
- `acceptance_matrix_claim_to_evidence_mapping_for_first_slice`
- `sol_architecture_review_for_first_slice`
- `terra_critique_for_first_slice`
- `roadmap_validation_for_first_slice`

## Remaining Blockers

- `runtime_implementation_requires_separate_authorization`
- `ocr_render_pdf_raw_mutation_requires_separate_authorization`
- `translation_proofreading_requires_separate_authorization`
- `page_021_plus_remains_separate_bounded_lane_if_selected`
- `source_profile_acceptance_beyond_g1wgadr_requires_separate_authorization`
- `push_requires_separate_authorization`
