# OCR Candidate Manifest - OCM-G1-VIRAL-001

Manifest id: `OCM-G1-VIRAL-001`

Status: `candidate_config_frozen_for_review`

Created: 2026-07-18

Actor: OpenClaw / Codex

Authorization id: `BA-G1-VIRAL-OCRCANDIDATE-002`

Baseline commit: `a35c9702c04b33705a24d7c6c5ca536d0d60c8ea`

Purpose: record the first OCR candidate configuration attempt for future
bounded OCR benchmark execution.

Boundary: this is not OCR execution, OCR output, benchmark result, QA, fixture,
source evidence, source-profile acceptance, translation, proofreading,
renderer/profile acceptance, implementation, or Gate 1 advancement.

Method: bound the discovered local Tesseract executable and language data to a
candidate configuration. No OCR tool was installed. No OCR was run.

## Environment Check

| Check | Result |
|---|---|
| `D:\NRI\.tools\tesseract\tesseract.exe --version` | `tesseract v5.4.0.20240606` |
| Tesseract executable SHA-256 | `BABB405F4366B480D02CD8FF2BAC8D497170F6C1711CE6F3D5D8BF0FB7FA6ED9` |
| `eng.traineddata` | `D:\NRI\.tools\tesseract\tessdata\eng.traineddata`; SHA-256 `7D4322BD2A7749724879683FC3912CB542F19906C83BCC1A52132556427170B2` |
| `osd.traineddata` | `D:\NRI\.tools\tesseract\tessdata\osd.traineddata`; SHA-256 `9CF5D576FCC47564F11265841E5CA839001E7E6F38FF7F7AACF46D15A96B00FF` |

## Candidate

Candidate id: `OCR-G1-VIRAL-TESSERACT-ENG-PSM6-001`

Status: `candidate_config_frozen_for_review`

Engine/config intended for future freeze:

- Engine: Tesseract OCR
- Version: `5.4.0.20240606`
- Executable path: `D:\NRI\.tools\tesseract\tesseract.exe`
- Executable SHA-256:
  `BABB405F4366B480D02CD8FF2BAC8D497170F6C1711CE6F3D5D8BF0FB7FA6ED9`
- Language: `eng`
- Language data path: `D:\NRI\.tools\tesseract\tessdata\eng.traineddata`
- Language data SHA-256:
  `7D4322BD2A7749724879683FC3912CB542F19906C83BCC1A52132556427170B2`
- OEM: `1`
- PSM: `6`
- Input: rendered PNG pages/regions admitted by `POMB-G1-VIRAL-001`
- Output format: TSV plus plain text, if future authorization permits
- Preprocessing: none
- Coordinate reporting: TSV coordinates if available

This candidate config is now frozen for review, but OCR execution still
requires a separate bounded OCR benchmark authorization naming exact inputs,
outputs, limits, expiry, and invalidation behavior.

## Blockers

- No OCR benchmark execution authorization exists.
- No OCR output manifest exists.
- No benchmark result exists.
- Gate 1 advancement authority remains separate.

## Invalidation

This manifest is stale if protocol revision/blob changes, baseline commit is
superseded, authorization changes, executable path/hash changes, Tesseract
version changes, language data path/hash changes, OCR config changes, command
path changes, output format changes, preprocessing policy changes,
reviewer/authority changes, or predecessor remediation/supersession occurs.
