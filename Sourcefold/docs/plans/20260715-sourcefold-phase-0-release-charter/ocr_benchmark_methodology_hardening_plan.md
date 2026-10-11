# OCR Benchmark Methodology Hardening Plan

Status: `implemented_verified`

Scope: `ocr_benchmark_methodology_hardening_no_new_ocr_no_acceptance`

Authority: Bogdan Telegram message `2189`: "делай оба шага"

## Boundary

- Consume `G1SPRMREV-G1-VIRAL-001` plus existing OCR benchmark/remediation
  evidence.
- Harden the OCR methodology rules that were parked pending OCR hardening:
  engine/config/threshold handling, benchmark pass/fail policy, no
  acceptance-by-score, visual-QC routing, overlay/order QC interpretation, and
  raw payload containment.
- Create no new OCR outputs and do not rerun OCR.

## Outputs

- `BA-G1-VIRAL-OCR-BENCHMARK-METHODOLOGY-HARDENING-001`
- `OCRHM-G1-VIRAL-001`
- `ocr_benchmark_methodology_hardening.json`
- `ocr_benchmark_methodology_hardening_report.json`
- `ocr_benchmark_methodology_hardening_summary.md`
- `ocr_benchmark_methodology_hardening_manifest.md`

## Guardrails

- This is methodology hardening and decision-prep evidence only.
- It does not accept OCR engine/config/thresholds as a source profile.
- It does not create source-profile acceptance, parking decisions, fixture
  admission, whole Gate 1 acceptance, page `021+` processing, source/OCR/render
  /PDF/raw mutation, translation, proofreading, implementation, push, or any
  broader Gate action.
