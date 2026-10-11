# Page 002 QA and Structure Evaluation Packet

Status: `ready_for_bogdan_plan_review`

Scope: this packet plans the next bounded steps after `SRADV-G1-VIRAL-002`.
It does not accept source text, page 002 as complete, whole Gate 1, QA,
fixtures, translation, proofreading, renderer/profile behavior,
implementation, or push.

## Current Evidence

- Last committed verification layer: `SRADV-G1-VIRAL-002`.
- Commit: `552a3fdc2`.
- Verified page-002 records: 2.
- Bogdan decision source: Telegram message `377`.
- Human decision recorded: `1 ok`, `2 ok`, headings ignored for the text
  verification decision, text OK.
- Page-complete acceptance: `false`.
- Source acceptance: `false`.
- QA acceptance: `false`.
- Fixture admission: `false`.
- Gate 1 advancement: `false`.

## Recommended Path

1. Run `BA-G1-VIRAL-SOURCE-RECON-P002-ASSISTED-DRAFT-QA-001`.
2. Run `BA-G1-VIRAL-SOURCE-RECON-P002-STRUCTURE-SEMANTICS-001`.
3. Present a compact structure digest to Bogdan.
4. Run a structure QA layer.
5. Only then ask for source acceptance for the two page-002 records.

Rationale: page 002 is mostly credits, labels, and legal/footer text. Accepting
flat text before structure would leave ambiguity about heading levels, labels,
and footer roles.

## Step 1 - Verified Draft QA

Target id: `SRADQ-G1-VIRAL-002`

Authorization: `BA-G1-VIRAL-SOURCE-RECON-P002-ASSISTED-DRAFT-QA-001`

QA checks:

- `SRADV-G1-VIRAL-002` consumes exact `SRAD-G1-VIRAL-002` hashes.
- Bogdan Telegram message `377` is recorded exactly.
- Both records have `verified_text_matches_crop=true`.
- Heading handling is recorded as ignored for text verification.
- Records count is exactly 2.
- Verified text hashes match the assisted draft text hashes.
- Corrected crop hashes are preserved.
- `source_acceptance=false`.
- `page_complete_acceptance=false`.
- `whole_gate_1_acceptance=false`.

Outputs:

- QA report.
- QA manifest.
- QA summary.
- Fail-closed generator script and pytest.

## Step 2 - Structure/Semantics Pass

Target id: `SRSS-G1-VIRAL-002`

Authorization: `BA-G1-VIRAL-SOURCE-RECON-P002-STRUCTURE-SEMANTICS-001`

The structure pass does not change text. It assigns roles and presentation
observations to already verified text spans.

### Schema

Each span should carry:

- `text`: exact verified text span.
- `semantic_role`: source role such as `credits_title`, `credit_role_label`,
  `credit_value`, `legal_notice`, or `url`.
- `heading_level`: `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `none`, or `unknown`.
- `bold`: `true`, `false`, or `unknown`.
- `italic`: `true`, `false`, or `unknown`.
- `underline`: `true`, `false`, or `unknown`.
- `centered`: `true`, `false`, or `unknown`.
- `small_caps`: `true`, `false`, or `unknown`.
- `font_scale`: `large`, `normal`, `small`, or `unknown`.
- `confidence`: `high`, `medium`, or `low`.
- `requires_bogdan_review`: boolean.

Rule: do not infer `h1` through `h6` from bold styling alone. Heading level is
semantic hierarchy, while bold/italic/underline are presentation observations.

### Proposed Record 1 Structure

| Text span | Semantic role | Heading level | Presentation notes | Review note |
|---|---|---|---|---|
| `Credits` | `credits_title` | `h1` | centered likely; bold likely | Confirm as page/section title |
| `Writing` | `credit_role_label` | `none` | bold likely | Label, not heading |
| `Alex Guillotte, Buds RPG Review` | `credit_value` | `none` | unknown | Value for Writing |
| `Illustrations, Design & Layout` | `credit_role_label` | `none` | bold likely | Label, not heading |
| `Alex Guillotte` | `credit_value` | `none` | unknown | Value |
| `Editing` | `credit_role_label` | `none` | bold likely | Label |
| `Matthew Pook` | `credit_value` | `none` | unknown | Value |
| `Additional Editing` | `credit_role_label` | `none` | bold likely | Label |
| `Keith Mageau` | `credit_value` | `none` | unknown | Value |
| `Language Consultant` | `credit_role_label` | `none` | bold likely | Label |
| `Luca Alexander Volpino` | `credit_value` | `none` | unknown | Value |
| `Play Testers` | `credit_role_label` | `none` | bold likely | Label |
| Play tester names | `credit_value_list` | `none` | unknown | Multi-line value list |

### Proposed Record 2 Structure

| Text span | Semantic role | Heading level | Presentation notes | Review note |
|---|---|---|---|---|
| `Special Thanks to Seth Skorkowsky.` | `special_thanks_line` | `none_or_h2_candidate` | unknown | Needs Bogdan decision: sentence or heading-like line |
| `In creating this unredacted version...` | `special_thanks_body` | `none` | unknown | Body paragraph |
| `(C) Copyright 2022 - Alex Guillotte, Buds RPG Review` | `copyright_notice` | `none` | unknown | Legal/footer notice |
| `Call of Cthulhu is a Trademark of Chaosium Inc.` | `trademark_notice` | `none` | unknown | Legal/footer notice |
| `OBS Community Content program` | `license_program_reference` | `none` | unknown | Part of license notice |
| `www.Chaosium.com` | `publisher_url` | `none` | unknown | URL |
| `The Miskatonic Repository Logo is used under license.` | `logo_license_notice` | `none` | unknown | Legal/footer notice |

## Bogdan Evaluation Questions

Use this answer shape when reviewing the structure pass:

```text
1 - structure ok
2 - structure ok
```

or:

```text
1 - правка: <what to change>
2 - blocker: <what is unclear>
```

Specific question for record 2:

- Should `Special Thanks to Seth Skorkowsky.` be `heading_level=none` as a
  sentence/line, or a heading-like `h2` candidate?

## Step 3 - Structure QA

Target id: `SRSSQ-G1-VIRAL-002`

QA checks:

- Structure spans reference exact `SRADV-G1-VIRAL-002` text hashes.
- No text is changed during structure marking.
- Every role has `confidence` and `requires_bogdan_review`.
- Heading levels are separated from presentation flags.
- Renderer/profile acceptance remains false.
- Source acceptance remains false.

## Step 4 - Source Acceptance Candidate

Only after QA and structure review, create a separate bounded decision packet:

`BA-G1-VIRAL-SOURCE-RECON-P002-SOURCE-ACCEPTANCE-001`

Possible decision wording:

```text
Accept the two page-002 source reconstruction records with verified text and
reviewed structure metadata; page 002 is not accepted as complete.
```

Still blocked after that:

- Page 002 complete acceptance.
- Whole Gate 1 acceptance.
- Translation.
- Proofreading.
- Renderer/profile acceptance.
- Implementation.
- Push.
