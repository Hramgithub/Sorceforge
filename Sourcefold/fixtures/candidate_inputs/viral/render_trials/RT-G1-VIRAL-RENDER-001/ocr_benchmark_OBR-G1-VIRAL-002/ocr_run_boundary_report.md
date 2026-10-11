# OCR Run Boundary Report - ORB-G1-VIRAL-001

Report id: `ORB-G1-VIRAL-001`

Status: `valid_for_bounded_execution`

Created: 2026-07-18

Actor: OpenClaw / Codex

Authorization id: `BA-G1-VIRAL-OCRBENCH-001`

Baseline commit: `30025b4b9cebff5de4701b44e3b9d2aa4c1f80dc`

Purpose: define the exact OCR benchmark execution boundary before creating
any OCR outputs.

Boundary: this report records the execution boundary under
`BA-G1-VIRAL-OCRBENCH-001` for a small benchmark run over five admitted region
crops. It is not QA, fixture creation, source-profile acceptance, translation,
proofreading, renderer/profile acceptance, implementation, or Gate 1
advancement.

## Admitted Inputs

| Input | ID | SHA-256 |
|---|---|---|
| Pre-OCR map bundle | `POMB-G1-VIRAL-001` | `B000FB2212D538212097BD71B695024CA5208988927616397B9F215C4FCC2B9F` |
| Gold sample manifest | `GSM-G1-VIRAL-001` | `A7EA3157815D8F3311AFA91B0EF70F97AE9E6C0C7F4D76203983C1B0341B7D62` |
| OCR candidate manifest | `OCM-G1-VIRAL-001` | `6FBDC9463A670968D335DFB8F841819CEB55CDC24B2CFC1C32EF9AA9BD323842` |

## Engine

| Field | Value |
|---|---|
| Executable | `D:\NRI\.tools\tesseract\tesseract.exe` |
| Version | `tesseract v5.4.0.20240606` |
| Executable SHA-256 | `BABB405F4366B480D02CD8FF2BAC8D497170F6C1711CE6F3D5D8BF0FB7FA6ED9` |
| Language | `eng` |
| Language data SHA-256 | `7D4322BD2A7749724879683FC3912CB542F19906C83BCC1A52132556427170B2` |
| OEM | `1` |
| PSM | `6` |
| Output formats | text and TSV |
| Preprocessing | none |

## Admitted Sample Crops

| Sample id | Page/region | Source image | Crop box | Crop output |
|---|---|---|---|---|
| `GS-G1-VIRAL-001` | `PG-G1-VIRAL-P001` / `RG-G1-VIRAL-P001-R002` | `images/page_001.png` | `[760,260,1050,760]` | `input_crops/GS-G1-VIRAL-001.png` |
| `GS-G1-VIRAL-002` | `PG-G1-VIRAL-P005` / `RG-G1-VIRAL-P005-R001` | `images/page_005.png` | `[920,260,750,280]` | `input_crops/GS-G1-VIRAL-002.png` |
| `GS-G1-VIRAL-003` | `PG-G1-VIRAL-P005` / `RG-G1-VIRAL-P005-R002` | `images/page_005.png` | `[260,600,2050,2300]` | `input_crops/GS-G1-VIRAL-003.png` |
| `GS-G1-VIRAL-004` | `PG-G1-VIRAL-P006` / `RG-G1-VIRAL-P006-R002` | `images/page_006.png` | `[200,320,950,360]` | `input_crops/GS-G1-VIRAL-004.png` |
| `GS-G1-VIRAL-005` | `PG-G1-VIRAL-P006` / `RG-G1-VIRAL-P006-R003` | `images/page_006.png` | `[220,1550,2100,1400]` | `input_crops/GS-G1-VIRAL-005.png` |

## Commands

Each crop is executed with the same bounded Tesseract pattern:

```powershell
& D:\NRI\.tools\tesseract\tesseract.exe <crop_png> <raw_output_base> -l eng --oem 1 --psm 6 txt tsv
```

## Output Paths

- Crop images: `input_crops/`
- Raw OCR text/TSV/logs: `raw_outputs/`
- Output manifest: `ocr_output_manifest.md`
- Benchmark result report: `ocr_benchmark_result_report.md`

## Limits

- No PDF opening, parsing, rehashing, recounting, or inspection.
- No OCR outside the five admitted sample crops.
- No manual edits to OCR outputs.
- No copied OCR text promoted into accepted source text.
- No QA, fixture creation, source-profile acceptance, translation,
  proofreading, renderer/profile acceptance, implementation, or Gate 1
  advancement.

## Invalidation

This boundary stales if protocol revision/blob changes, baseline commit is
superseded, authorization changes, POMB/GSM/OCM hash changes, rendered page
image hash changes, crop boxes change, Tesseract executable/language data/config
changes, output format changes, reviewer/authority changes, or predecessor
remediation/supersession occurs.
