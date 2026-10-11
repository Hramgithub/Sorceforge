# Source Reconstruction Run Orchestration - SRM-G1-VIRAL-001

- Script: `scripts/build_source_reconstruction_review_package.py`
- Authorization: `BA-G1-VIRAL-SOURCE-RECON-RUN-001`
- Run manifest: `SRM-G1-VIRAL-001`
- Review package: `G1-VIRAL-SOURCE-RECONSTRUCTION-REVIEW-001`
- Evidence precheck: `SRQ-G1-VIRAL-001`
- Status: `candidate_review_blocked_for_remediation`
- OCR executed by this run: `false`
- Candidate text assembled from selected OCR evidence: `true`
- Human review ready: `false`
- Source acceptance: `false`
- Gate 1 advancement: `false`

Reproduce with:

```powershell
python scripts\build_source_reconstruction_review_package.py --execute --authorization-id BA-G1-VIRAL-SOURCE-RECON-RUN-001 --admitted-manifest-sha256 59D146B024EBAEB548D2BD5F03BF3027632C4F289FD2FFAC36F36879501277E9
python -m pytest tests\test_source_reconstruction_review_package.py
scripts\validate_roadmap.ps1
```
