# OCR Benchmark Result Report - OBR-G1-VIRAL-002

Report id: `OBR-G1-VIRAL-002`

Status: `valid_for_review`

Verdict: `remediation_recommended_before_gate_review`

Created: 2026-07-18

Actor: OpenClaw / Codex

Authorization id: `BA-G1-VIRAL-OCRBENCH-001`

Output manifest: `OOM-G1-VIRAL-001`

Purpose: compare the bounded five-sample OCR output against
`GSM-G1-VIRAL-001` and record benchmark findings.

Boundary: this report is benchmark evidence only. It is not QA, fixture
creation, source-profile acceptance, translation, proofreading,
renderer/profile acceptance, implementation, or Gate 1 advancement.

## Inputs

| Input | ID | SHA-256 |
|---|---|---|
| Pre-OCR map bundle | `POMB-G1-VIRAL-001` | `B000FB2212D538212097BD71B695024CA5208988927616397B9F215C4FCC2B9F` |
| Gold sample manifest | `GSM-G1-VIRAL-001` | `A7EA3157815D8F3311AFA91B0EF70F97AE9E6C0C7F4D76203983C1B0341B7D62` |
| OCR candidate manifest | `OCM-G1-VIRAL-001` | `6FBDC9463A670968D335DFB8F841819CEB55CDC24B2CFC1C32EF9AA9BD323842` |
| OCR run boundary | `ORB-G1-VIRAL-001` | `CFA4B8ACDF0BA5AED70DFE5E730E442D8B3D3671E17FEE8300AB5BE4AE95B10C` |
| OCR output manifest | `OOM-G1-VIRAL-001` | `BF8ABFF3F9E54DCAA0E2C944A437EC46D1A0C066C051798F012B0FC1AFEFD849` |

## Method

- Cropped five sample regions from existing rendered PNG pages.
- Ran `D:\NRI\.tools\tesseract\tesseract.exe` with `-l eng --oem 1 --psm 6`
  and `txt tsv` output.
- Compared raw text outputs to the gold strings in `GSM-G1-VIRAL-001`.
- No OCR was run outside the admitted five crop files.
- No OCR outputs were manually edited.
- The PDF was not opened, parsed, rehashed, recounted, or inspected.

## Sample Findings

| Sample id | Gold target summary | OCR outcome summary | Finding |
|---|---|---|---|
| `GS-G1-VIRAL-001` | cover title | OCR did not recover the target phrase. | fail |
| `GS-G1-VIRAL-002` | contents heading | OCR did not recover the heading. | fail |
| `GS-G1-VIRAL-003` | contents entries | OCR recovered contents-like material but not the selected gold entries. | fail; crop/selection mismatch suspected |
| `GS-G1-VIRAL-004` | section heading | OCR did not recover the heading. | fail; crop/config unsuitable |
| `GS-G1-VIRAL-005` | short quote | OCR captured most quote words but punctuation/layout diverged and surrounding text was included. | partial |

## Aggregate Result

| Metric | Result |
|---|---:|
| Samples attempted | 5 |
| Tesseract exit-code success | 5 |
| Exact text matches | 0 |
| Strong partial matches | 1 |
| Weak partial matches | 0 |
| Failed matches | 4 |

## Interpretation

The local Tesseract executable is usable, but the first candidate config is not
good enough for Gate 1 source-profile review. The strongest signal is that
large body text can be partially recovered, while title/heading and contents
snippets are weak under the current crop boxes and `--psm 6` configuration.

Likely remediation areas:

- tighten gold-sample crop boxes for headings and contents entries;
- evaluate alternate Tesseract page segmentation modes for headings and
  table-like contents regions;
- consider a bounded preprocessing trial for contrast/scale only after
  separate authorization;
- split table/list regions into smaller line-level crops before scoring.

## Recommendation

`G1-VIRAL-REMEDIATE-001` should be requested before any Gate 1 advancement
package. The benchmark is useful evidence, but it does not support advancement
as-is. Suggested remediation scope: refine sample crop boxes, test a small
matrix of Tesseract `--psm` modes on the same admitted samples, and consider a
separately authorized scale/contrast preprocessing trial with hashes.

## Limits Preserved

- No PDF opening, parsing, rehashing, recounting, or inspection.
- No OCR outside the five admitted sample crops.
- No manual edits to OCR outputs.
- No source text acceptance.
- No QA, fixture creation, source-profile acceptance, translation,
  proofreading, renderer/profile acceptance, implementation, or Gate 1
  advancement.

## Invalidation

This report stales if protocol revision/blob changes, authorization changes,
POMB/GSM/OCM/ORB/OOM hashes change, crop boxes change, OCR output changes,
scoring rules change, reviewer/authority changes, or predecessor remediation
or supersession occurs.
