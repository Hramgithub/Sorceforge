# Review Asset Deduplication Plan

Scope: answer and implementation plan for duplicate crops found in `PCRP-G1-VIRAL-P010-001`.

## Problem

The P010 page-complete review packet carried duplicate crop files:

- `1_P010-upper-left-continuation-gear-human-context.png` duplicated `1b_P010-upper-left-continuation-gear-text-evidence.png`.
- `2_P010-upper-right-continuation-appearance-gear-human-context.png` duplicated `2b_P010-upper-right-continuation-appearance-gear-text-evidence.png`.
- `5_P010-lower-left-hyeon-profile-human-context.png` duplicated `5b_P010-lower-left-hyeon-profile-text-evidence.png`.
- `6_P010-lower-right-maya-profile-human-context.png` duplicated `6b_P010-lower-right-maya-profile-text-evidence.png`.

The duplicated pairs had identical SHA-256 hashes, so they were not distinct review surfaces. They were the same physical crop materialized twice under different role names.

## 1. Why We Collected The Same Crop Twice

The package model separated crop roles logically but did not deduplicate physical assets.

Relevant roles:

- `human_review_crop`: a crop intended to help a human understand or review the region.
- `text_evidence_crop`: the OCR/source evidence surface for text verification.

For P010 text blocks, the human-review crop geometry and the text-evidence crop geometry were identical. The builder did not check whether two role outputs resolved to the same crop bytes. It materialized both roles as separate files, producing different attachment names with identical image hashes.

This was originally conservative after the P009 crop-role correction: every role had to be explicit. The refined rule should be: every role must be explicit in metadata, but roles do not require separate physical files when their source image, crop box, transform, and bytes are identical.

## 2. How To Stop Collecting It Twice

Add package-level review asset deduplication.

The builder should compute a canonical asset key from:

- source image id/path;
- crop box;
- crop transform/rendering options;
- output bytes hash.

If two roles produce the same canonical key or identical output hash, the package should:

- write one physical asset file;
- bind multiple roles to that asset via `role_bindings` or `aliases`;
- record the duplicate as deduplicated, not as a second independent file;
- preserve the role semantics so `human_review_crop` cannot silently replace `text_evidence_crop`.

Example shape:

```json
{
  "asset_id": "P010-B001-TEXT-EVIDENCE",
  "package_path": "review_assets/1b_P010-upper-left-continuation-gear-text-evidence.png",
  "sha256": "C5B10AF894F47363FE406A6676803EA79378BDAF20251BF0C80D5BA2AB31C10A",
  "role_bindings": [
    {
      "role": "text_evidence_crop",
      "block_id": "P010-B001"
    },
    {
      "role": "human_review_crop",
      "block_id": "P010-B001",
      "deduplicated_with": "P010-B001-TEXT-EVIDENCE"
    }
  ]
}
```

Chat delivery should use a separate `delivery_assets` list rather than sending every package asset. For page-complete review, the default delivery list should include:

- the full page image;
- visual anchor crops;
- text-evidence crops;
- required human-readable review/text/semantic files;
- human-context crops only when they differ from text-evidence crops and add review value.

## 3. How To Make It A Universal Pipeline Rule

Add a reusable validator/contract:

`sourcefold_review_asset_deduplication.v1`

Required behavior:

- Block byte-identical crop files with different names unless they are represented as aliases or role bindings.
- Allow multiple logical roles to point to one physical asset.
- Require role semantics to remain explicit even when physical files are deduplicated.
- Require `human_review_crop` to remain distinct in meaning from `text_evidence_crop`, even if both roles bind to the same asset.
- Require package reports/manifests to show deduplication decisions.
- Require a separate `delivery_assets` list for chat-facing review packets.
- Block package readiness when duplicate hashes exist without a declared deduplication rationale.

Regression coverage should include the P010 case:

- `1 == 1b`
- `2 == 2b`
- `5 == 5b`
- `6 == 6b`

Expected result: those become role aliases or bindings to one physical asset, not duplicated PNG files.

## Recommended Next Step

Before page 010 acceptance, implement bounded hardening:

`BA-G1-VIRAL-REVIEW-ASSET-DEDUPLICATION-001`

Then regenerate or supersede `PCRP-G1-VIRAL-P010-001` so the package and chat delivery carry only necessary physical assets.

Boundaries:

- no page acceptance;
- no whole Gate 1 acceptance;
- no source/OCR acceptance;
- no page 011 processing;
- no push unless separately authorized.

## Sol/Terra Implementation Design

Sol conclusion: the deduplication fix must not be limited to chat delivery. The
pipeline needs a reusable distinction between physical package assets, logical
role bindings, and chat-facing delivery assets.

Terra conclusion: the fix must not delete crop-role metadata or deduplicate every
same-hash file blindly. Deduplication is safe only when applied to declared
review crop/image assets with explicit alias or role-binding metadata.

### Target Model

The page-complete review package should expose three separate concepts:

- `package_assets`: the physical files stored in the package.
- `role_bindings`: the logical roles attached to each physical asset.
- `delivery_assets`: the subset of package assets intended for chat delivery.

If a crop is byte-identical and role-identical by source/box/transform, the
package should store one physical file and bind multiple logical roles to it.
If a human context crop is wider, padded, or otherwise materially different from
the text evidence crop, it remains a separate physical asset.

### Shared Contract

Implement:

`Sourcefold/scripts/review_asset_deduplication.py`

Schema:

`sourcefold_review_asset_deduplication.v1`

Expected reusable functions:

- `build_review_asset_index(attachments)`
- `validate_review_asset_deduplication(attachments)`
- `build_delivery_assets(attachments, policy="page_complete_review")`
- `require_passed_review_asset_deduplication(packet_or_report)`

### Contract Rules

- Duplicate image/crop asset hashes inside one review package are blocked unless
  represented as aliases or role bindings.
- Multiple logical roles may point to one physical asset.
- `human_review_crop` remains semantically distinct from `text_evidence_crop`
  even when both bind to one physical file.
- Text and JSON duplicate hashes are outside the initial rule unless explicitly
  declared as review assets.
- A package ready for human review must include `delivery_assets`.
- `delivery_assets` must not include alias-only duplicate crops.
- The report/manifest must record deduplication decisions and rationale.

### Page-Complete Builder Integration

Update `Sourcefold/scripts/build_page_complete_review.py` so packaging does not
copy every logical attachment blindly.

Implementation steps:

1. Build each logical attachment record as today.
2. Before copying, compute a canonical asset key using source path/id, crop box,
   transform/rendering options, and output hash.
3. If an equivalent physical asset already exists, do not copy another file.
4. Record the later logical attachment as a `role_binding` or `alias` to the
   canonical asset.
5. Keep text evidence roles explicit and required.
6. Generate `package_assets`, `review_asset_deduplication`, and
   `delivery_assets` in the report.
7. Emit only physical files in the manifest hash table; emit aliases in a
   separate manifest section.

### Delivery Policy

Default `page_complete_review` delivery should include:

- source page image;
- visual anchor crops;
- text evidence crops in logical review order;
- review packet, summary, manifest, report, text map, and semantic map files;
- human context crops only when not deduplicated with text evidence crops.

For the P010 PCRP case, delivery should include:

- `page_010.png`
- `3_P010-left-hyeon-portrait-image-area-human-context.png`
- `4_P010-right-maya-portrait-image-area-human-context.png`
- `1b_P010-upper-left-continuation-gear-text-evidence.png`
- `5b_P010-lower-left-hyeon-profile-text-evidence.png`
- `2b_P010-upper-right-continuation-appearance-gear-text-evidence.png`
- `6b_P010-lower-right-maya-profile-text-evidence.png`
- the review/text/semantic markdown/json files needed for the decision.

The duplicate human-context filenames for text blocks should not be delivered as
separate images when they are aliases of text-evidence assets.

### Tests

Add:

`Sourcefold/tests/test_review_asset_deduplication.py`

Required coverage:

- P010 duplicate crop pairs become aliases or role bindings.
- Duplicate image hash without alias metadata blocks readiness.
- Distinct human context crop remains a separate asset.
- Text evidence role remains mandatory.
- `delivery_assets` excludes alias-only duplicate crops.
- Manifest/report show deduplication rationale.

Update:

`Sourcefold/tests/test_page_complete_review.py`

Required P010 assertions:

- `PCRP-G1-VIRAL-P010-001` has no separate physical PNG files for the four
  duplicate text-block human-context crops.
- Logical human-review roles still exist through role bindings.
- Physical package assets include the four text-evidence crops, two portrait
  anchors, the full page, and required text/semantic documents.
- Chat delivery assets match the review-facing subset.

### P010 Refresh Strategy

Because current `PCRP-G1-VIRAL-P010-001` work is still uncommitted, prefer
refreshing that package in place under the new contract rather than creating
`PCRP-G1-VIRAL-P010-002`.

The refresh should:

- remove physical duplicate PNGs from the package;
- add `review_asset_deduplication` results;
- add `package_assets`;
- add `delivery_assets`;
- update manifest/report/summary/packet hashes;
- preserve package scope: page-complete review packet only, no acceptance.

### Bounded Authorization

Recommended implementation authorization:

`BA-G1-VIRAL-REVIEW-ASSET-DEDUPLICATION-001`

Allowed scope:

- shared deduplication validator;
- page-complete review builder integration;
- tests and regression coverage;
- P010 PCRP refresh;
- docs/roadmap/ledger sync.

Forbidden scope:

- page-complete acceptance;
- whole Gate 1 acceptance;
- source/OCR acceptance;
- page 011 processing;
- push.

### Sol/Terra Verdict

Sol: OK. The design preserves crop roles and removes redundant physical files.

Terra: OK only if deduplication is explicit, limited to review crop/image
assets, and `delivery_assets` becomes the source of truth for chat attachments.
