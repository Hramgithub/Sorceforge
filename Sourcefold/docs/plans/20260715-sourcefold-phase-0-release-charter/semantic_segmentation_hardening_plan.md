# Semantic Segmentation Hardening Plan

Status: `implemented_for_current_aggressive_builders_and_validator`

## Problem

The P016-P020 aggressive review exposed a pipeline-wide gap: semantic validation
checks heading depth, schema shape, crop bounds, and guardrails, but it does not
fail closed when a callout or Keeper's Notes segment consumes ordinary body text
that follows the callout.

The issue is not limited to aggressive mode. Any builder that maps mixed source
text blocks with ad hoc string splitting can accidentally treat `everything
after Keeper's Notes` as Keeper body.

## Required Contract

Mixed text blocks must be represented as bounded semantic segments:

- `body_before`
- `callout_heading`
- `callout_body`
- `body_after`
- `next_heading`
- continuation markers when source text continues across pages

Callout body segmentation must declare one of:

- explicit callout body end marker
- next segment start marker
- crop or source region boundary
- reviewed continuation boundary

If no boundary is declared, the builder must fail closed rather than assigning the
remaining text block to the callout unit.

## Implemented Scope

- Added `scripts/semantic_segmentation_contract.py` as the shared bounded
  callout contract module. It provides fail-closed splitting plus validation for
  semantic units that represent callout/sidebar/card/Keeper body segments.
- Added fail-closed semantic validation in `page_review_semantic_units.py`:
  any callout/sidebar/card/Keeper body unit must carry a
  `semantic_split_contract` with a registered boundary kind and marker.
- Updated current aggressive builders for P012, P014, and P016-P020 to emit and
  validate `semantic_split_contract` before writing semantic map outputs.
- Rebuilt P012, P014, and P016-P020 downstream semantic maps, complete-review
  bundles, delegated acceptance reports, status packets, and aggressive batch
  reports so the artifacts carry the new split validation state.
- Corrected the P016/P018 human-review findings: P016 history text is no longer
  inside `SU-P016-KEEPER-005`, and P018 piazza/village body text is no longer
  inside `SU-P018-KEEPER-002`.

## Pipeline Hardening Follow-Up

Remaining follow-up beyond the current aggressive lane:

- `build_page_complete_review.py`
- fixture-wide audit over older existing semantic maps with callout/sidebar/Keeper
  units generated before this contract existed
- new-page builder template enforcement so every future mixed text block declares
  its segment boundary before semantic map output

The durable rule is: a semantic unit must prove its segment boundary; it must not
inherit the rest of a text block merely because it follows a callout heading.
