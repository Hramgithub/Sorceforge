# Core 0.1 Unresolved Pages Method Discovery Plan

Lane: `C01TEUNRES020-G1-VIRAL-001`

Authorization: `BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-UNRESOLVED-PAGES-METHOD-DISCOVERY-001`

## Objective

Create a bounded unresolved-pages method discovery dry-run after
`C01TESEL020-G1-VIRAL-001`. The builder consumes the unresolved page set
`012`/`016`/`017`/`018`/`020`, ranks existing hash-pinned diagnostic evidence,
opens fresh method entries only for pages with threshold-passing evidence, and
creates a static selector replay v2.

This is not a production assembly and not a new OCR run. It is a selector and
registry-evidence dry-run over already generated diagnostic artifacts.

## Boundaries

- No OCR execution.
- No render execution.
- No PDF parsing or text-layer extraction.
- No reference-token insertion.
- No accepted text, semantic map, page-status, source, or raw mutation.
- No selector runtime enablement or runtime selector integration.
- No production assembly or clean production output folder.
- No page `021+`.
- No promotion, acceptance, push, translation/proofreading, or downstream
  execution.

## Expected Discovery

- Input selector replay: `C01TESEL020-G1-VIRAL-001`.
- Input unresolved pages: `012`, `016`, `017`, `018`, `020`.
- Input diagnostic evidence: `C01TEGP012013016017018020-G1-VIRAL-001`
  corrected `_G1_VIRAL_002` geometry-probe report.
- Newly discovered pages: `017`, `018`.
- Still unresolved: `012`, `016`, `020`.
- Selector replay v2 selected pages:
  `009`, `010`, `011`, `013`, `015`, `017`, `018`.
- Production ready: `false`.
- All pages first-pass success: `false`.

## Status

Generated after focused tests and Sol/Terra gate.

- Discovered pages: `017`, `018`.
- Still unresolved: `012`, `016`, `020`.
- Selector replay v2 selected pages:
  `009`, `010`, `011`, `013`, `015`, `017`, `018`.
- Production ready: `false`.
- All pages first-pass success: `false`.
- No OCR, production assembly, accepted text mutation, page-status mutation,
  page `021+`, promotion, acceptance, or downstream execution was created.

Generated output hashes:

- `method_registry_entries/page_017.json`:
  `6EAD1FC9B97F19C005D06B586F90B76A4582DCE7A9BA51ED436710A0A84719A8`
- `method_registry_entries/page_018.json`:
  `03FC0EE1BEE6676510387B1B3DDDE9E58306817917975841AC69640DA4CE46F8`
- `selector_replay_v2/selector_replay_v2_selections.json`:
  `801F6B67141C8CFC15A19FEFA17C94585CF70255FB875FD6DA702E9E4E0066DA`
- `unresolved_pages_method_discovery_report.json`:
  `06FF3C64CA67F5259A1AC063A7FE34C10527280AB58B07C215B848357609DDF5`
- `unresolved_pages_method_discovery_summary.md`:
  `0A28CE5184AA1DA393BDCD2DAAB7C9415BC6B2129CE66A9923B009DC10549C67`
