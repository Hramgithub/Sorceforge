# pytest run summary (scratch clone at 98c2404, 2026-10-12)

Interpreter: CPython 3.12.14 (AMD64 build) under Windows 11 ARM64 emulation; pytest 9.1.1; Pillow 12.2.0.
Command (from Sourcefold/ of the clone): python -B -m pytest -p no:cacheprovider -q -rfs --tb=line
Environment: PYTHONPATH=<clone root>; PYTHONDONTWRITEBYTECODE=1.

Full run result line:
13 failed, 977 passed, 27 skipped, 12 errors in 90.84s (0:01:30)

The 12 errors were PermissionError on the sandboxed system temp dir (tmp_path). Rerun of exactly those 12 with --basetemp=<scratch>: 12 passed.
Reconciled total: 989 passed, 27 skipped, 13 failed (equals the recorded export result).

Failed node IDs:
FAILED tests/test_core_0_1_text_extraction_012_016_020_method_family.py::test_012_016_020_pre_output_scope_and_pins
FAILED tests/test_gate_1_review_decision.py::test_gate_1_review_decision_preserves_brief_lineage
FAILED tests/test_gate_1_review_decision_brief.py::test_gate_1_review_decision_brief_preserves_packet_lineage_and_boundaries
FAILED tests/test_gate_1_review_packet.py::test_gate_1_review_packet_preserves_lineage_and_boundaries
FAILED tests/test_gate_1_source_recon_evidence_rollup.py::test_gate_1_source_recon_rollup_preserves_decision_lineage
FAILED tests/test_gate_1_status_packet.py::test_gate_1_status_packet_preserves_rollup_lineage
FAILED tests/test_ocr_remediation_review_package.py::test_review_package_binds_exact_predecessors_and_hashes
FAILED tests/test_source_reconstruction_fixture_admission.py::test_fixture_admission_preserves_lineage_and_boundaries
FAILED tests/test_source_reconstruction_human_package.py::test_human_package_preserves_boundary_and_lineage
FAILED tests/test_source_reconstruction_human_review.py::test_human_review_preserves_lineage_and_boundaries
FAILED tests/test_source_reconstruction_next_slice.py::test_next_slice_preserves_status_packet_and_region_lineage
FAILED tests/test_source_reconstruction_next_slice_004.py::test_page_004_next_slice_consumes_p003a_and_region_lineage
FAILED tests/test_source_reconstruction_qa.py::test_source_reconstruction_qa_preserves_lineage_and_boundaries

## T1 scratch experiment (182 paths, eol=crlf in Sourcefold/.gitattributes)

1 failed, 1001 passed, 27 skipped in 82.53s (0:01:22)
Only failure: tests/test_core_0_1_text_extraction_012_016_020_method_family.py::test_012_016_020_pre_output_scope_and_pins (missing D:\NRI tesseract).
