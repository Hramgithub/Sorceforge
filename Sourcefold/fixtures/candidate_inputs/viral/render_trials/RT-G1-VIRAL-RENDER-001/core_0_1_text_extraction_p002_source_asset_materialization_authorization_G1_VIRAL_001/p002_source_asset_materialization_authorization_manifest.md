# C01TEP002ASSETMATAUTH-G1-VIRAL-001 Manifest

- Authorization: `BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-P002-SOURCE-ASSET-MATERIALIZATION-AUTHORIZATION-001`
- Status: `p002_source_asset_materialization_authorization_recorded_future_lane_only_no_materialization_no_mutation`
- Page: `002`
- Output policy: report/summary/manifest only; no materialization, OCR, acceptance, production, or downstream execution.

## Inputs

- `C01TEP002ASSETREC-G1-VIRAL-001.report`: `A1D88F383DDF5F8654DBBEFEEEBEE391F955EB4C61C01C490009533430B9E140`
- `C01TEP002ASSETREC-G1-VIRAL-001.summary`: `B34EB8461DD931C2E18341905C056AADC5EDE78D510D249FB2B771EF8838235F`
- `C01TEP002ASSETREC-G1-VIRAL-001.manifest`: `061FE0C03A176953E585FCCF80962DB6CAA9F338E7CDF0299A9F14A8923AFDAB`

## Outputs

- `p002_source_asset_materialization_authorization_report.json`: `37D85ADA6E3AB6CAAA7D8F82F488F53281AE740A8BDD8D4D82AE83264FB6811B`
- `p002_source_asset_materialization_authorization_summary.md`: `6FAB886C6FEC44ADDCC6F06749143369779402D958AC397CAAE01EA605CE45F8`

## Manifest Self-Hash

- This manifest does not embed its own post-write SHA-256 because doing so
  would change the digest. The manifest file SHA-256 is sealed after
  materialization in `PROJECT_STATUS.md`, `roadmap.yaml`, and
  `bounded_trial_authorizations.md`.
