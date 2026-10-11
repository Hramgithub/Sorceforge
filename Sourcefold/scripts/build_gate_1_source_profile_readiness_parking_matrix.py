from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "build_gate_1_source_profile_readiness_parking_matrix.py"
TEST_PATH = ROOT / "tests" / "test_gate_1_source_profile_readiness_parking_matrix.py"
AUTHORIZATION_LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "gate_1_source_profile_readiness_parking_matrix_G1_VIRAL_001"

AUTHORIZATION_ID = "BA-G1-VIRAL-SOURCE-PROFILE-READINESS-PARKING-MATRIX-001"
MATRIX_ID = "G1SPRM-G1-VIRAL-001"

ALLOWED_DISPOSITIONS = [
    "ready_for_gate_review",
    "parked_for_0.1",
    "parked_pending_ocr_hardening",
    "blocked_needs_decision",
    "evidence_only_not_accepting",
]

INPUT_HASHES = {
    "G1SP-G1-VIRAL-016.packet": (
        TRIAL_ROOT / "gate_1_status_packet_G1_VIRAL_016" / "gate_1_status_packet.json",
        "C69701A098CC33486B89C6F0D7F8D1A890B05C288DC8F814A430D44ABF47F88F",
    ),
    "G1SP-G1-VIRAL-016.report": (
        TRIAL_ROOT / "gate_1_status_packet_G1_VIRAL_016" / "gate_1_status_report.json",
        "3C051D65A15CB4DE0FA5649D6FE6C5C81AC75B3A752EC80E126EA81E50713F05",
    ),
    "G1SP-G1-VIRAL-015.packet": (
        TRIAL_ROOT / "gate_1_status_packet_G1_VIRAL_015" / "gate_1_status_packet.json",
        "B016D09B91A5C1DA9B3E6026C9E5CF777CE290773864C786A51903FA1FCD62F8",
    ),
    "ORM-G1-VIRAL-001.report": (
        TRIAL_ROOT / "ocr_remediation_matrix_G1_VIRAL_001" / "ocr_remediation_matrix_report.json",
        "3A454433ABA46E237D091F5BB4DA6EB8B73FCEE400935AF10BB0DC5731F212F5",
    ),
    "ORR-G1-VIRAL-001.report": (
        TRIAL_ROOT / "ocr_remediation_review_G1_VIRAL_001" / "ocr_remediation_review_report.json",
        "B3491A1F3E942C430AE246A62DCAFB066F95BEA56390CF510D27635EBFEE6725",
    ),
    "ONC-G1-VIRAL-001.report": (
        TRIAL_ROOT / "ocr_remediation_review_G1_VIRAL_001" / "negative_check_report.json",
        "2205564DB2BCD9EEF73D8EB02034EA28D7292D1A6970E3056F3BD9F5887E8F61",
    ),
    "gate_01_qualification_protocol.current": (
        ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "gate_01_qualification_protocol.md",
        "95A562A783BB85B795E75734202AA807D09112A15AE0CFF2426D4D5CF78BA813",
    ),
    "phase_gate_component_hierarchy.current": (
        ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "phase_gate_component_hierarchy.md",
        "25CE8497153E413483E97A896CD30B6A179A5E979D6BDC91C1109B81BC54CDFE",
    ),
    "release_charter.current": (
        ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "release_charter.md",
        "8728377545FAC6082360DA95D23ADE2EADF4286FF9DC704ABB1765ECCE61FBBE",
    ),
}

NEGATIVE_CAPABILITIES = [
    "fixture_admission",
    "source_mutation",
    "new_source_acceptance",
    "source_profile_acceptance",
    "ocr_execution",
    "ocr_remediation_execution",
    "render_execution",
    "pdf_parsing_or_text_layer_extraction",
    "raw_mutation",
    "translation",
    "proofreading",
    "renderer_profile_acceptance",
    "implementation",
    "push",
    "page_021_plus_processing",
    "whole_gate_1_acceptance",
]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def write_json(path: Path, payload: object) -> None:
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8", newline="\n")


def check_authorization(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Build Gate 1 source-profile readiness/parking matrix.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("Gate 1 source-profile readiness/parking matrix is fail-closed; pass --execute with exact authorization id")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"Gate 1 source-profile readiness/parking matrix requires {AUTHORIZATION_ID}")


def verify_authorization_ledger() -> None:
    ledger = AUTHORIZATION_LEDGER.read_text(encoding="utf-8-sig")
    if f"## {AUTHORIZATION_ID}" not in ledger:
        raise SystemExit(f"{AUTHORIZATION_ID} is missing from bounded trial authorization ledger")


def verify_input_hashes() -> dict[str, dict[str, str]]:
    verify_authorization_ledger()
    verified: dict[str, dict[str, str]] = {}
    for key, (path, expected) in INPUT_HASHES.items():
        actual = sha256_file(path)
        if actual != expected:
            raise SystemExit(f"{key} hash mismatch: {actual}")
        verified[key] = {
            "path": path.relative_to(ROOT).as_posix(),
            "sha256": actual,
        }
    return verified


def matrix_rows() -> list[dict[str, object]]:
    return [
        {
            "id": "candidate_source_identity_and_selected_page_scope",
            "category": "candidate_source_identity",
            "disposition": "ready_for_gate_review",
            "basis": "Viral candidate input and selected pages 001-020 have stable project evidence, but fixture/source-profile acceptance remains separate.",
            "requires_human_decision_before_acceptance": True,
        },
        {
            "id": "render_profile_and_render_trial_evidence",
            "category": "render_profile",
            "disposition": "evidence_only_not_accepting",
            "basis": "Render-trial evidence exists and supports review workflows, but renderer/profile acceptance remains false.",
            "requires_human_decision_before_acceptance": True,
        },
        {
            "id": "pages_001_020_page_complete_evidence",
            "category": "page_complete_evidence",
            "disposition": "ready_for_gate_review",
            "basis": "Pages 001-020 are page-complete accepted only according to G1SP-G1-VIRAL-016.",
            "requires_human_decision_before_acceptance": True,
        },
        {
            "id": "page_021_plus_disposition",
            "category": "page_scope",
            "disposition": "blocked_needs_decision",
            "basis": "Page 021+ is unprocessed and not authorized; it is not part of the current route.",
            "requires_human_decision_before_acceptance": True,
        },
        {
            "id": "pre_ocr_map_model_and_bundle_lineage",
            "category": "pre_ocr_map_model",
            "disposition": "ready_for_gate_review",
            "basis": "Map model and bundle lineage evidence exists for Gate 1 decision prep, not acceptance.",
            "requires_human_decision_before_acceptance": True,
        },
        {
            "id": "ocr_engine_config_thresholds",
            "category": "ocr_methodology",
            "disposition": "parked_pending_ocr_hardening",
            "basis": "OCR engine/config/thresholds remain evidence-gated and are selected for the next remediation/hardening branch.",
            "requires_human_decision_before_acceptance": True,
        },
        {
            "id": "ocr_benchmark_remediation_debt",
            "category": "ocr_methodology",
            "disposition": "parked_pending_ocr_hardening",
            "basis": "Existing ORR/ORM/ONC evidence is cited as unresolved/later input; no OCR remediation is started here.",
            "requires_human_decision_before_acceptance": True,
        },
        {
            "id": "source_reconstruction_source_review_qa_fixture_evidence",
            "category": "source_reconstruction",
            "disposition": "evidence_only_not_accepting",
            "basis": "Narrow source reconstruction and QA evidence exists, but fixture admission and source-profile acceptance remain false.",
            "requires_human_decision_before_acceptance": True,
        },
        {
            "id": "semantic_crop_projection_inventory_gates",
            "category": "semantic_and_page_review_pipeline",
            "disposition": "ready_for_gate_review",
            "basis": "Current page pipeline evidence includes crop provenance, semantic split contracts, projection validation, inventory reconciliation, and page-complete gates.",
            "requires_human_decision_before_acceptance": True,
        },
        {
            "id": "acceptance_authority_and_delegated_review_boundaries",
            "category": "authority",
            "disposition": "ready_for_gate_review",
            "basis": "Human/delegated review boundaries are explicit for current pages; direct per-stage Bogdan approval is not retroactively recorded.",
            "requires_human_decision_before_acceptance": True,
        },
        {
            "id": "unsupported_profiles_and_negative_fixtures",
            "category": "unsupported_profiles",
            "disposition": "blocked_needs_decision",
            "basis": "Unsupported profile and negative fixture obligations remain missing for Core 0.1 source-profile acceptance.",
            "requires_human_decision_before_acceptance": True,
        },
        {
            "id": "whole_gate_1_acceptance",
            "category": "gate_acceptance",
            "disposition": "blocked_needs_decision",
            "basis": "Page-complete acceptance through 020 is not whole Gate 1 acceptance.",
            "requires_human_decision_before_acceptance": True,
        },
    ]


def build_matrix(verified_inputs: dict[str, dict[str, str]]) -> dict[str, object]:
    rows = matrix_rows()
    for row in rows:
        if row["disposition"] not in ALLOWED_DISPOSITIONS:
            raise SystemExit(f"invalid disposition for {row['id']}: {row['disposition']}")
    return {
        "matrix_id": MATRIX_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "source_profile_readiness_parking_matrix_ready_for_human_route_review",
        "purpose": "gate_1_source_profile_readiness_parking_matrix_decision_prep_no_acceptance",
        "creates_acceptance": False,
        "creates_parking_decision": False,
        "starts_ocr_remediation": False,
        "baseline": {
            "status_packet": "G1SP-G1-VIRAL-016",
            "page_complete_accepted_pages": [f"{page:03d}" for page in range(1, 21)],
            "page_complete_acceptance_scope": "individual_pages_only",
            "page_021_plus_state": "unprocessed_not_authorized",
            "whole_gate_1_acceptance": False,
        },
        "allowed_dispositions": ALLOWED_DISPOSITIONS,
        "rows": rows,
        "negative_capability_matrix": {name: False for name in NEGATIVE_CAPABILITIES},
        "verified_inputs": verified_inputs,
        "selected_route_sequence": [
            "gate_1_source_profile_readiness_parking_matrix",
            "ocr_benchmark_remediation_methodology_hardening",
        ],
        "next_branch_after_this_matrix": {
            "branch": "ocr_benchmark_remediation_methodology_hardening",
            "status": "selected_next_branch_not_started_not_authorized_by_this_matrix",
        },
    }


def write_summary(matrix: dict[str, object]) -> None:
    counts = {status: 0 for status in ALLOWED_DISPOSITIONS}
    for row in matrix["rows"]:
        counts[row["disposition"]] += 1
    lines = [
        "# Gate 1 Source Profile Readiness Parking Matrix - G1SPRM-G1-VIRAL-001",
        "",
        "Status: `source_profile_readiness_parking_matrix_ready_for_human_route_review`",
        "",
        "Purpose: decision prep for Gate 1 source-profile readiness and parking candidates. This packet creates no acceptance and starts no OCR remediation.",
        "",
        "## Baseline",
        "",
        "- Pages `001` through `020`: page-complete accepted only.",
        "- Page `021+`: `unprocessed_not_authorized`.",
        "- Whole Gate 1 acceptance: `false`.",
        "- Next selected branch after this matrix: `ocr_benchmark_remediation_methodology_hardening`.",
        "",
        "## Disposition Counts",
        "",
    ]
    for status in ALLOWED_DISPOSITIONS:
        lines.append(f"- `{status}`: {counts[status]}")
    lines.extend(["", "## Matrix Rows", "", "| Row | Disposition |", "|---|---|"])
    for row in matrix["rows"]:
        lines.append(f"| `{row['id']}` | `{row['disposition']}` |")
    lines.extend(
        [
            "",
            "Decision after review: `source-profile readiness matrix ok` or `hold source-profile readiness matrix: <reason>`.",
            "",
        ]
    )
    (OUT_ROOT / "gate_1_source_profile_readiness_parking_matrix_summary.md").write_text("\n".join(lines), encoding="utf-8", newline="\n")


def write_report(matrix: dict[str, object]) -> None:
    write_json(
        OUT_ROOT / "gate_1_source_profile_readiness_parking_matrix_report.json",
        {
            "matrix_id": MATRIX_ID,
            "authorization_id": AUTHORIZATION_ID,
            "status": matrix["status"],
            "generator_script": SCRIPT_PATH.relative_to(ROOT).as_posix(),
            "generator_script_sha256": sha256_file(SCRIPT_PATH),
            "test_contract": TEST_PATH.relative_to(ROOT).as_posix(),
            "test_contract_sha256": sha256_file(TEST_PATH) if TEST_PATH.exists() else None,
            "creates_acceptance": False,
            "creates_parking_decision": False,
            "starts_ocr_remediation": False,
            "negative_capability_matrix": matrix["negative_capability_matrix"],
            "row_count": len(matrix["rows"]),
            "next_branch_after_this_matrix": matrix["next_branch_after_this_matrix"],
        },
    )


def write_manifest() -> None:
    lines = [
        "# Gate 1 Source Profile Readiness Parking Matrix Manifest - G1SPRM-G1-VIRAL-001",
        "",
        "Status: `source_profile_readiness_parking_matrix_ready_for_human_route_review`",
        "",
        "Boundary: this matrix creates no acceptance, no parking decision, no OCR remediation execution, no page 021+ authorization, and no next-layer execution.",
        "",
        "## Output Hashes",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for path in sorted(OUT_ROOT.rglob("*")):
        if path.is_file() and path.name != "gate_1_source_profile_readiness_parking_matrix_manifest.md":
            lines.append(f"| `{path.relative_to(OUT_ROOT).as_posix()}` | `{sha256_file(path)}` |")
    lines.append("")
    (OUT_ROOT / "gate_1_source_profile_readiness_parking_matrix_manifest.md").write_text("\n".join(lines), encoding="utf-8", newline="\n")


def build() -> None:
    verified_inputs = verify_input_hashes()
    if OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    matrix = build_matrix(verified_inputs)
    write_json(OUT_ROOT / "gate_1_source_profile_readiness_parking_matrix.json", matrix)
    write_summary(matrix)
    write_report(matrix)
    write_manifest()


if __name__ == "__main__":
    check_authorization()
    build()
