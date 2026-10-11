# Source Reconstruction Prep Orchestration - SRD-G1-VIRAL-001

- Script: `scripts/build_source_reconstruction_review_package.py`
- Prep authorization: `BA-G1-VIRAL-SOURCE-RECON-PREP-001`
- Protocol: `SRP-G1-VIRAL-001`
- Admitted manifest: `SRA-G1-VIRAL-001`
- Dry-run report: `SRD-G1-VIRAL-001`
- OCR executed: `false`
- Candidate source text created: `false`
- PDF opened/parsed/rendered: `false`
- Human review requested now: `false`

Reproduce with:

```powershell
python scripts\build_source_reconstruction_review_package.py --dry-run
python -m pytest tests\test_source_reconstruction_review_package.py
scripts\validate_roadmap.ps1
```
