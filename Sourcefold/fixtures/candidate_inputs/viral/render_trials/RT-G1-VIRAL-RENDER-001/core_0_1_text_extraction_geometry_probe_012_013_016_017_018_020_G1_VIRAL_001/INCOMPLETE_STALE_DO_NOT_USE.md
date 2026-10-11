# Incomplete Stale Geometry Probe Output

Status: `incomplete_stale_do_not_use`

This output root was created by the first attempted
`C01TEGP012013016017018020-G1-VIRAL-001` execution and stopped before a
complete scoring/report manifest was produced.

Reason: the initial runner interpreted triage `crop_box_px` as
`x1,y1,x2,y2`, but the source triage metadata uses `x,y,width,height`.

Boundary: these partial prepared/raw OCR artifacts are quarantined and must not
be scored, accepted, promoted, or used as policy evidence. The corrected rerun
uses the new output root
`core_0_1_text_extraction_geometry_probe_012_013_016_017_018_020_G1_VIRAL_002`.
