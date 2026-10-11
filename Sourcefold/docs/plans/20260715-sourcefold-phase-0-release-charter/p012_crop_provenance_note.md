# P012 Crop Provenance Note

Status: `design_note_no_acceptance`

This note records a blocker found during the P012 aggressive batch human spot-check.

## Finding

`P012-R005` / `Keeper's Notes` had correct transcribed body text in the text and semantic artifacts, but the review crop did not fully cover the source text box and captured unrelated neighboring text.

This is a provenance failure: the text can be correct while the evidence crop cannot independently justify the text it is linked to.

## Root Cause

The current aggressive batch lane treats crops as review/provenance assets, not as the technical extraction source. Text extraction is recorded as manual/delegated extraction bound to region and block ids, then semantic mapping consumes that text artifact. The crop is generated from the same intended region metadata, but the text is not mechanically derived from the crop image.

Because of that, a bad crop can pass unless the pipeline explicitly checks crop coverage and neighboring-region exclusion.

## Required Contract Improvement

Future P012 aggressive-batch fixes should make extraction provenance explicit:

- `extraction_method: manual_from_text_evidence_region`
- `ocr_executed: false`
- every in-scope text unit must be bound to a region/block id;
- every text-evidence crop must fully cover its bound text region;
- every text-evidence crop must exclude neighboring text regions unless explicitly marked as context;
- Sol/Terra review must treat mismatched crop coverage as a blocker.

## Resolution

`P012-R005` was corrected, page 012 was rebuilt from scratch with seven
text-evidence crops, and `P012BATCHREV-G1-VIRAL-001` records final human review
of the corrected bundle/status.

The crop coverage rule has also been promoted into a shared aggressive-builder
gate: future `build_page_*_aggressive_batch.py` builders must import and call
the shared crop contract validator and define explicit `crop_contract` /
`context_allowed` metadata for text-evidence blocks.
