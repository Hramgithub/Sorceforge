# OCR Benchmark Prerequisite Review - OBR-G1-VIRAL-001

Review id: `OBR-G1-VIRAL-001`

Status: `blocked_waiting_gold_and_ocr_candidate`

Created: 2026-07-18

Actor: OpenClaw / Codex

Authorization id: `BA-G1-VIRAL-OCRBENCH-PREQ-001`

Baseline commit: `e9ba54dc7aa10ae409192c70883c6ecae307c79f`

Purpose: determine whether bounded OCR benchmark execution can start after
`OPR-G1-VIRAL-001`.

Boundary: this is a prerequisite/blocker review only. It is not OCR execution,
OCR output, gold text, benchmark result, QA, fixture, source evidence,
source-profile acceptance, translation, proofreading, renderer/profile
acceptance, implementation, or Gate 1 advancement.

Method: review `OPR-G1-VIRAL-001` and Gate 1 protocol prerequisites. The PDF
was not opened, parsed, rehashed, recounted, or inspected. No OCR,
transcription, copied text, PDF text-layer extraction, benchmark, QA, fixture,
source acceptance, translation, proofreading, or implementation work was
performed.

## Inputs

| Evidence | ID | SHA-256 |
|---|---|---|
| OCR preparation package | `OPR-G1-VIRAL-001` | `8920E42A10EBBF64557A3C971F73D783FB9F00A86D90777F22BEA7941F38C62F` |

## Verdict

`blocked_waiting_gold_and_ocr_candidate`

OCR benchmark execution cannot start yet.

## Missing Prerequisites

- Exact OCR engine/service identity and version/model are not selected.
- Executable/API identity and local environment are not frozen.
- OCR candidate manifest is a stub, not a frozen executable manifest.
- Gold-sample manifest does not exist.
- Gold text/sample answers do not exist and were not authorized.
- Scoring plan is a stub, not a frozen scoring plan with exact gold manifest
  and OCR candidate manifest hashes.
- OCR benchmark authorization has not named exact OCR candidates, gold samples,
  input page/region IDs, outputs, limits, expiry, and invalidation behavior.
- Gate 1 advancement authority remains separate from benchmark execution.

## Allowed Next Actions

1. Request a bounded gold-sample creation authorization. It must name pages or
   regions, human authority, source of gold text, payload containment rules,
   canonicalization/hashing, and invalidation behavior.
2. Request a bounded OCR candidate manifest authorization. It must freeze exact
   OCR engine/config/environment/output format without running OCR.
3. Request a bounded OCR benchmark execution authorization only after gold
   sample and OCR candidate manifests exist and are current.

## Explicit Non-Actions

- No OCR run.
- No OCR output.
- No gold text or sample answer creation.
- No benchmark scoring.
- No QA.
- No fixtures.
- No source acceptance.
- No Gate 1 advancement.

## Plan Completion Note

This review reaches the end of the ten-step forward plan in the only safe
state currently possible: benchmark execution is blocked until gold samples and
OCR candidate identity/config are separately authorized and frozen.

## Invalidation

This review is stale if protocol revision/blob changes, baseline commit is
superseded, authorization changes, `OPR-G1-VIRAL-001` changes,
`POMB-G1-VIRAL-001` changes, OCR candidate identity/config changes,
gold-sample policy/manifest changes, scoring plan changes, reviewer/authority
changes, or any predecessor remediation/supersession occurs.
