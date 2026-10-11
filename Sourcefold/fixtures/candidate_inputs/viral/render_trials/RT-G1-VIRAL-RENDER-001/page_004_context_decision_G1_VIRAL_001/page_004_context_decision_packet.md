# Page 004 Context-Only Decision Packet

Package: `P004CDP-G1-VIRAL-001`

Status: `ready_for_bogdan_page_004_context_only_decision`

Boundary: this is a context-only decision packet. It does not accept page 004 as complete, does not advance Gate 1, and does not admit fixtures.

## Proposed Context Decision

- Region: `PRM-G1-VIRAL-001-P004-R01`
- Proposed status: `context_only_not_peer_crop_record`
- Reason: Full tilted inset contains the title/body regions and would overlap peer crops under the global crop layout guardrail.
- Full tilted inset: yes.
- Accepted peer text records remain the title/body records below.

## Accepted Peer Records

### PRM-G1-VIRAL-001-P004-R02 - warning_title

- Review id: `SRCR-G1-VIRAL-004-R01`
- Crop: `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_next_slice_G1_VIRAL_004/region_refs/1_SRCR-G1-VIRAL-004-R01__PRM-G1-VIRAL-001-P004-R02.png`
- Crop SHA-256: `ADD3C344100356249BF38C85A7C89D2A2DB9FF23B48141509A47F86C6A32C219`
- Accepted text SHA-256: `86F56FE8221F029DB2C9755CC998669A7D873C32BFA83BC9431BAFE0BB814400`

### PRM-G1-VIRAL-001-P004-R03 - safety_warning_body

- Review id: `SRCR-G1-VIRAL-004-R02`
- Crop: `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_next_slice_G1_VIRAL_004/region_refs/2_SRCR-G1-VIRAL-004-R02__PRM-G1-VIRAL-001-P004-R03.png`
- Crop SHA-256: `EFB82E2F8ECE14585CFD83F71C301B7024C437680703B18765A259A7E3B234C8`
- Accepted text SHA-256: `430246F1327C4554B2D16C8D5BFE11704EE515B4B5C3DB298A7B3492716E14A2`

## Review Attachments

- `review_assets/page_004.png` - source_page_image, SHA-256 `45A61639C922FD6CCD085BA259BA114DD92FBCB96E86A17D216F5387DCCA9B88`
- `review_assets/1_SRCR-G1-VIRAL-004-R01__PRM-G1-VIRAL-001-P004-R02.png` - block_crop, SHA-256 `ADD3C344100356249BF38C85A7C89D2A2DB9FF23B48141509A47F86C6A32C219`
- `review_assets/2_SRCR-G1-VIRAL-004-R02__PRM-G1-VIRAL-001-P004-R03.png` - block_crop, SHA-256 `EFB82E2F8ECE14585CFD83F71C301B7024C437680703B18765A259A7E3B234C8`
- `review_assets/page_004_ocr_block_text.md` - ocr_block_text_markdown, SHA-256 `7994F6D597C0041052361533BDDBCC63511B784F1BC24D6E7A089588BAAD3DDB`

## Decision Needed

Bogdan can now decide whether the full tilted inset should remain context-only before page-map readiness for page 004.

Reply shape:

```text
page 004 context-only ok
```

or:

```text
hold page 004 context-only: <reason>
```

This packet itself creates no page-complete acceptance.
