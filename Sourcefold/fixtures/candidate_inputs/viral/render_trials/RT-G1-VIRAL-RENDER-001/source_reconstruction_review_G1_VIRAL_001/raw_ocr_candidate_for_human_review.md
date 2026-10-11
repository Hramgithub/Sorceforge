# Viral Source Reconstruction Review Package - G1-VIRAL-SOURCE-RECONSTRUCTION-REVIEW-001

Status: `candidate_review_blocked_for_remediation`

Authorization: `BA-G1-VIRAL-SOURCE-RECON-RUN-001`

Boundary: this package is not accepted source text, QA acceptance, fixture acceptance, translation, proofreading, implementation, or Gate 1 advancement.

Human review status: `blocked_for_remediation`. Visual-QC and overlay-QC findings must be remediated before asking Bogdan to approve source reconstruction.

## Candidate Text Records

### SRA-G1-VIRAL-001-R001 / PG-G1-VIRAL-P001 / z02

- Source image: `fixtures\candidate_inputs\viral\render_trials\RT-G1-VIRAL-RENDER-001\images\page_001.png`
- Input crop: `fixtures\candidate_inputs\viral\render_trials\RT-G1-VIRAL-RENDER-001\ocr_remediation_matrix_G1_VIRAL_001\input_crops\GS-G1-VIRAL-001__z02.png`
- Region: `RG-G1-VIRAL-P001-R002`
- Predecessor crop SHA-256: `6D34BF801BED6A81890DA573C92514C063566A428F371C0F45F6125E170B59EB`
- Selected config: `white_mask_x4__psm4`
- OCR text SHA-256: `D5BDEC0C1DB3C98CBCF6F32648FB9B7775AB613A157ABC0ABAE4F78FE6885D6D`
- Overlay QC: `bad_geometry`
- Order QC: `auto_qc_pass`

```text
UNREDACTED -
```

### SRA-G1-VIRAL-001-R002 / PG-G1-VIRAL-P005 / z01

- Source image: `fixtures\candidate_inputs\viral\render_trials\RT-G1-VIRAL-RENDER-001\images\page_005.png`
- Input crop: `fixtures\candidate_inputs\viral\render_trials\RT-G1-VIRAL-RENDER-001\ocr_remediation_matrix_G1_VIRAL_001\input_crops\GS-G1-VIRAL-002__z01.png`
- Region: `RG-G1-VIRAL-P005-R001`
- Predecessor crop SHA-256: `8A3A979381FB476C3B6D9831D7665E50F3171C4D4300EB7C3373E4216738CF24`
- Selected config: `original__psm11`
- OCR text SHA-256: `66725B0AA1EE5F38CBD242128278CBEB1659B96AE77F1FA88B22F6AFBABF66AE`
- Overlay QC: `needs_visual_review`
- Order QC: `auto_qc_pass`

```text
bd

Contents
```

### SRA-G1-VIRAL-001-R003 / PG-G1-VIRAL-P005 / z01

- Source image: `fixtures\candidate_inputs\viral\render_trials\RT-G1-VIRAL-RENDER-001\images\page_005.png`
- Input crop: `fixtures\candidate_inputs\viral\render_trials\RT-G1-VIRAL-RENDER-001\ocr_remediation_matrix_G1_VIRAL_001\input_crops\GS-G1-VIRAL-003__z01.png`
- Region: `RG-G1-VIRAL-P005-R002`
- Predecessor crop SHA-256: `54E0E3B0A956EA0BA215987D25B242EED3A803100AD87C2E8949E3EA4592F66A`
- Selected config: `binary_x3__psm11`
- OCR text SHA-256: `09B06CBDAC2B3013245A9439CD0D05B8DD2027070EA770528969815FFA30E9BB`
- Overlay QC: `likely_visual_page`
- Order QC: `auto_qc_pass`

```text
Introduction

Summary

Overview

The Spektral Krew
```

### SRA-G1-VIRAL-001-R004 / PG-G1-VIRAL-P006 / z01

- Source image: `fixtures\candidate_inputs\viral\render_trials\RT-G1-VIRAL-RENDER-001\images\page_006.png`
- Input crop: `fixtures\candidate_inputs\viral\render_trials\RT-G1-VIRAL-RENDER-001\ocr_remediation_matrix_G1_VIRAL_001\input_crops\GS-G1-VIRAL-004__z01.png`
- Region: `RG-G1-VIRAL-P006-R002`
- Predecessor crop SHA-256: `B07232F8A6CC6673E1B848221E31B33BE67AC31743A93E6924F65493B0AC835A`
- Selected config: `original__psm11`
- OCR text SHA-256: `3FA53FC0DAB8EF96D05D8FD4C7E41B490182803725C67B86A531E09EFFC5FA77`
- Overlay QC: `bad_geometry`
- Order QC: `auto_qc_pass`

```text
Introduction
```

### SRA-G1-VIRAL-001-R005 / PG-G1-VIRAL-P006 / z01

- Source image: `fixtures\candidate_inputs\viral\render_trials\RT-G1-VIRAL-RENDER-001\images\page_006.png`
- Input crop: `fixtures\candidate_inputs\viral\render_trials\RT-G1-VIRAL-RENDER-001\ocr_remediation_matrix_G1_VIRAL_001\input_crops\GS-G1-VIRAL-005__z01.png`
- Region: `RG-G1-VIRAL-P006-R003`
- Predecessor crop SHA-256: `C8D19E8904F77CCEFF0EABF300FA24AD740124BF038762A233FC77FC7C3A2B3D`
- Selected config: `enhanced_x2__psm1`
- OCR text SHA-256: `583BB36EDDE0E76E022896E78B2BDB455B9BBF93A27BDD616F9019D271BD49B9`
- Overlay QC: `ok`
- Order QC: `auto_qc_pass`

```text
“We are the Spektral Krew, and we go places and do things you

would never do.” — Marco Proudfoot
```

## Visual-QC Queue

- `SRA-G1-VIRAL-001-R006` / `PG-G1-VIRAL-P001` / `z01` / crop `B43A959D758409D58379483725C51D829A5C37ED377FA0F3DF75CEDA3BF7E54C`: `decorative_visual_component`; no candidate text created.
- `SRA-G1-VIRAL-001-R007` / `PG-G1-VIRAL-P005` / `z02` / crop `44F23D879C08FC0E1FC6C5DED9EC894FA2E78C1D2B98B90C6A547CA31AEC08F4`: `page_number_or_layout_component`; no candidate text created.

## Review Options

- Do not request source approval from Bogdan yet.
- Remediate exact records by `region_admission_id` and predecessor crop hash.
- Route visual-QC-only records to a separate visual correction/remediation artifact before human acceptance review.
