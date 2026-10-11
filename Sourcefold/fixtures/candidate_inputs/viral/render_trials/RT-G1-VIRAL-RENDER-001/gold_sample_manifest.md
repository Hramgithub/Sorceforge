# Gold Sample Manifest - GSM-G1-VIRAL-001

Manifest id: `GSM-G1-VIRAL-001`

Status: `valid_for_review`

Created: 2026-07-18

Actor: OpenClaw / Codex

Authorization id: `BA-G1-VIRAL-GOLDSAMPLE-001`

Baseline commit: `40dc8ba8aafd6a3d70ddedfc3f6d6bae8b28aad5`

Purpose: provide a small controlled gold-sample set for future OCR benchmark
authorization.

Boundary: this is not accepted source text, OCR output, benchmark result, QA,
fixture, source-profile acceptance, translation, proofreading,
renderer/profile acceptance, implementation, or Gate 1 advancement.

Method: manually read small snippets from already rendered PNG pages. The PDF
was not opened, parsed, rehashed, recounted, or inspected. No OCR was run. No
PDF text-layer content was inspected or used.

## Inputs

| Evidence | ID | SHA-256 |
|---|---|---|
| Pre-OCR map bundle | `POMB-G1-VIRAL-001` | `B000FB2212D538212097BD71B695024CA5208988927616397B9F215C4FCC2B9F` |
| OCR prep package | `OPR-G1-VIRAL-001` | `8920E42A10EBBF64557A3C971F73D783FB9F00A86D90777F22BEA7941F38C62F` |

## Gold Samples

| Sample id | Page/region reference | Sample type | Gold text | Notes |
|---|---|---|---|---|
| `GS-G1-VIRAL-001` | `PG-G1-VIRAL-P001` / `RG-G1-VIRAL-P001-R002` | cover title | `VIRAL UNREDACTED` | large cover title; line break normalized to space |
| `GS-G1-VIRAL-002` | `PG-G1-VIRAL-P005` / `RG-G1-VIRAL-P005-R001` | contents heading | `Contents` | page heading only |
| `GS-G1-VIRAL-003` | `PG-G1-VIRAL-P005` / `RG-G1-VIRAL-P005-R002` | contents entries | `Introduction 6; Summary 6; Overview 6` | selected top-left contents entries only |
| `GS-G1-VIRAL-004` | `PG-G1-VIRAL-P006` / `RG-G1-VIRAL-P006-R002` | section heading | `Introduction` | large section heading |
| `GS-G1-VIRAL-005` | `PG-G1-VIRAL-P006` / `RG-G1-VIRAL-P006-R003` | short quote | `"We are the Spektral Krew and we go places and do things you would never do." - Marco Proudfoot` | quote punctuation normalized to ASCII |

## Gold Sample Rules

- These snippets are benchmark references only.
- They must not be promoted to accepted source text by this manifest.
- Any correction to a gold string stales this manifest and any dependent OCR
  benchmark.
- Future benchmark scoring must reference exact sample IDs and this manifest
  hash.

## Invalidation

This manifest is stale if protocol revision/blob changes, baseline commit is
superseded, authorization changes, POMB changes, OPR changes, rendered page
image/hash changes, sample selection changes, gold text changes,
reviewer/authority changes, or predecessor remediation/supersession occurs.
