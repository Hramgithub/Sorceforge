# Core 0.1 P013 Method Discovery Plan

Lane: `C01TEP013DISC-G1-VIRAL-001`

Authorization: `BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-P013-METHOD-DISCOVERY-001`

## Objective

Simulate a P013 cold-start method search without using the existing P013 MRS
registry entry. The builder ranks available P013 diagnostic method-family
artifacts (`SDD`, `GNO`, `ELO`, `SSP`, `SAC`), chooses the best
threshold-passing method-registry candidate, records a discovered entry, and
creates a P013 selector dry-run from that discovered entry.

This is not a full raw/PDF/OCR-from-scratch run. It is a bounded discovery
layer over already generated, hash-pinned diagnostic artifacts.

## Boundaries

- No existing P013 MRS registry entry as input.
- No OCR execution.
- No render execution.
- No PDF parsing or text-layer extraction.
- No reference-token insertion.
- No accepted text, semantic map, page-status, source, or raw mutation.
- No selector runtime enablement or runtime selector integration.
- No production assembly or clean production output folder.
- No page `001`-`020` runtime loop.
- No page `021+`.
- No promotion, acceptance, push, translation/proofreading, or downstream
  execution.

## Expected Discovery

- Input lanes: `C01TEP013SDD-G1-VIRAL-001`, `C01TEP013GNO-G1-VIRAL-001`,
  `C01TEP013ELO-G1-VIRAL-001`, `C01TEP013SSP-G1-VIRAL-001`,
  `C01TEP013SAC-G1-VIRAL-001`.
- Ranking rule: threshold-met candidate, method-registry-candidate flag,
  similarity, token recall, `line_join` tie-break, then candidate id.
- Winner: `p013_sac_d_noise_then_declared_seam_fracture`.
- Equivalent not selected: `p013_sac_e_paragraph_join_d`.
- Expected metrics: `0.998915 / 0.993939`.

## Status

Generated after focused tests and Sol/Terra gate.

- Discovered entry: `C01TEP013DISC-G1-VIRAL-001-P013`.
- Diagnostic lanes ranked: `5`.
- Candidates ranked: `18`.
- Winner: `p013_sac_d_noise_then_declared_seam_fracture`.
- Equivalent tie not selected: `p013_sac_e_paragraph_join_d`.
- Metrics: `0.998915 / 0.993939`.
- MRS registry input used: `false`.
- Selector dry-run: P013 only, from the fresh discovered entry.
- Production ready: `false`.
- No OCR, production assembly, accepted text mutation, page-status mutation,
  page `001`-`020` runtime loop, page `021+`, promotion, acceptance, or
  downstream execution was created.

Generated output hashes:

- `method_registry_entries/page_013.json`:
  `9E92035A3411C4FDB32F523D9420CB34A17AB3449CD0EA34F57E30FF6295A494`
- `p013_method_discovery_report.json`:
  `8DC4220677A7338A1BDF988D429CF4D4D1095596EAF334F3465F1E8325CC86F7`
- `p013_method_discovery_summary.md`:
  `D2E527F2A02DF59D174C603AD5ECC067B3F488222C9B1879BFC22AA8BE61F052`
- `selector_dry_run/page_013_selection.json`:
  `6036EC7BF9694E5C7C56F70C7DB994537DCA91155734D68CAB4175E460D28788`
