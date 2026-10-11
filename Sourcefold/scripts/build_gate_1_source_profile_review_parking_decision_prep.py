from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "build_gate_1_source_profile_review_parking_decision_prep.py"
TEST_PATH = ROOT / "tests" / "test_gate_1_source_profile_review_parking_decision_prep.py"
AUTHORIZATION_LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "gate_1_source_profile_review_parking_decision_prep_G1_VIRAL_001"

AUTHORIZATION_ID = "BA-G1-VIRAL-SOURCE-PROFILE-REVIEW-PARKING-DECISION-PREP-001"
PACKET_ID = "G1SPRPD-G1-VIRAL-001"

INPUT_HASHES = {
    "G1SP-G1-VIRAL-017.packet": (
        TRIAL_ROOT / "gate_1_status_packet_G1_VIRAL_017" / "gate_1_status_packet.json",
        "DA9B421CD8A5BC503FCCEE24F6043FBCEC9F86262AF3E9E9018C460D871E4ED6",
    ),
    "G1SP-G1-VIRAL-017.report": (
        TRIAL_ROOT / "gate_1_status_packet_G1_VIRAL_017" / "gate_1_status_report.json",
        "007F7F1F6FC73FC4F9B9268CB3969F895517D20B054FCC1D787851E4609D2F68",
    ),
    "G1SP-G1-VIRAL-017.summary": (
        TRIAL_ROOT / "gate_1_status_packet_G1_VIRAL_017" / "gate_1_status_summary.md",
        "FF3F3D7F9F3EA0352C95448124821DE2C2255E63DCFEB9D6879A6EA722166CF3",
    ),
    "G1SP-G1-VIRAL-017.manifest": (
        TRIAL_ROOT / "gate_1_status_packet_G1_VIRAL_017" / "gate_1_status_manifest.md",
        "4A7DDDC454034FC8CFC75C184856B66D27B17ECEA0E5E8447C331B07CCD381A9",
    ),
    "G1SPRM-G1-VIRAL-001.matrix": (
        TRIAL_ROOT
        / "gate_1_source_profile_readiness_parking_matrix_G1_VIRAL_001"
        / "gate_1_source_profile_readiness_parking_matrix.json",
        "49EFEF00F19ACA3D583EA5A2DB221023C54F9EA32C83609A0DD95988F9612466",
    ),
    "G1SPRM-G1-VIRAL-001.report": (
        TRIAL_ROOT
        / "gate_1_source_profile_readiness_parking_matrix_G1_VIRAL_001"
        / "gate_1_source_profile_readiness_parking_matrix_report.json",
        "1E5F1A6CEA99B4BB4C67D9126727FBBC5C855CDDCF3B0F98CA0AD9F1C6710577",
    ),
    "G1SPRM-G1-VIRAL-001.summary": (
        TRIAL_ROOT
        / "gate_1_source_profile_readiness_parking_matrix_G1_VIRAL_001"
        / "gate_1_source_profile_readiness_parking_matrix_summary.md",
        "663A31D6E5D22CB6F0E093DF4BE5B122B42F5C4E4402E825D995195D6CBB8E9B",
    ),
    "G1SPRMREV-G1-VIRAL-001.review": (
        TRIAL_ROOT
        / "gate_1_source_profile_readiness_parking_matrix_review_G1_VIRAL_001"
        / "gate_1_source_profile_readiness_parking_matrix_review.json",
        "76D0B43FCE9B614424A47FEBDE61666E42B372E671396E876E1F59B38FCEC640",
    ),
    "G1SPRMREV-G1-VIRAL-001.summary": (
        TRIAL_ROOT
        / "gate_1_source_profile_readiness_parking_matrix_review_G1_VIRAL_001"
        / "gate_1_source_profile_readiness_parking_matrix_review_summary.md",
        "E25C0611E91186E20C1970966367DB8797E7D71F1069E2B230AC751F16E20EE7",
    ),
    "OCRHM-G1-VIRAL-001.packet": (
        TRIAL_ROOT / "ocr_benchmark_methodology_hardening_G1_VIRAL_001" / "ocr_benchmark_methodology_hardening.json",
        "AF62629E87F757929CC609C13198DB2594E4837F1296E1D9EF242E7E21B11C36",
    ),
    "OCRHM-G1-VIRAL-001.report": (
        TRIAL_ROOT / "ocr_benchmark_methodology_hardening_G1_VIRAL_001" / "ocr_benchmark_methodology_hardening_report.json",
        "08A913FED762D70FE603FEAD390804C067695071B580DEE00F50C22D68E991A5",
    ),
    "OCRHM-G1-VIRAL-001.summary": (
        TRIAL_ROOT / "ocr_benchmark_methodology_hardening_G1_VIRAL_001" / "ocr_benchmark_methodology_hardening_summary.md",
        "F110555A257C322F2A36ECDFF98B75491557A2ABAB31A016ADD0882600E8A044",
    ),
}

NEGATIVE_CAPABILITIES = [
    "source_profile_acceptance",
    "creates_parking_decision",
    "whole_gate_1_acceptance",
    "fixture_admission",
    "ocr_output_acceptance",
    "ocr_execution",
    "ocr_remediation_execution",
    "page_021_plus_processing",
    "source_mutation",
    "render_execution",
    "pdf_parsing_or_text_layer_extraction",
    "raw_mutation",
    "translation",
    "proofreading",
    "renderer_profile_acceptance",
    "implementation",
    "push",
]

DECISION_CATEGORIES = [
    "accept_for_gate_review_candidate",
    "park_for_0_1_with_invalidation_conditions",
    "remain_evidence_only_not_accepting",
    "hold_blocked_needs_decision",
    "requires_separate_bounded_authorization",
    "not_accepted_not_parked",
]

ROW_DECISION_MAP = {
    "candidate_source_identity_and_selected_page_scope": "accept_for_gate_review_candidate",
    "pages_001_020_page_complete_evidence": "accept_for_gate_review_candidate",
    "pre_ocr_map_model_and_bundle_lineage": "accept_for_gate_review_candidate",
    "semantic_crop_projection_inventory_gates": "accept_for_gate_review_candidate",
    "acceptance_authority_and_delegated_review_boundaries": "accept_for_gate_review_candidate",
    "ocr_engine_config_thresholds": "park_for_0_1_with_invalidation_conditions",
    "ocr_benchmark_remediation_debt": "park_for_0_1_with_invalidation_conditions",
    "render_profile_and_render_trial_evidence": "remain_evidence_only_not_accepting",
    "source_reconstruction_source_review_qa_fixture_evidence": "remain_evidence_only_not_accepting",
    "page_021_plus_disposition": "requires_separate_bounded_authorization",
    "unsupported_profiles_and_negative_fixtures": "hold_blocked_needs_decision",
    "whole_gate_1_acceptance": "hold_blocked_needs_decision",
}


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json(path: Path, payload: object) -> None:
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8", newline="\n")


def write_text(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8", newline="\n")


def check_authorization(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Build Gate 1 source-profile review / parking decision prep packet.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("Gate 1 source-profile review / parking decision prep is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"Gate 1 source-profile review / parking decision prep requires {AUTHORIZATION_ID}")


def verify_authorization_ledger() -> None:
    ledger = AUTHORIZATION_LEDGER.read_text(encoding="utf-8-sig")
    if f"## {AUTHORIZATION_ID}" not in ledger:
        raise SystemExit(f"{AUTHORIZATION_ID} is missing from bounded trial authorization ledger")


def verify_inputs() -> tuple[dict[str, dict[str, str]], dict, dict, dict, dict]:
    verify_authorization_ledger()
    verified: dict[str, dict[str, str]] = {}
    for key, (path, expected) in INPUT_HASHES.items():
        actual = sha256_file(path)
        if actual != expected:
            raise SystemExit(f"{key} hash mismatch: {actual}")
        verified[key] = {"path": path.relative_to(ROOT).as_posix(), "sha256": actual}

    g1sp17 = read_json(INPUT_HASHES["G1SP-G1-VIRAL-017.packet"][0])
    matrix = read_json(INPUT_HASHES["G1SPRM-G1-VIRAL-001.matrix"][0])
    matrix_review = read_json(INPUT_HASHES["G1SPRMREV-G1-VIRAL-001.review"][0])
    ocrhm = read_json(INPUT_HASHES["OCRHM-G1-VIRAL-001.packet"][0])

    if g1sp17["creates_acceptance"] or g1sp17["creates_parking_decision"]:
        raise SystemExit("G1SP-017 unexpectedly creates acceptance or parking")
    if matrix["creates_acceptance"] or matrix["creates_parking_decision"]:
        raise SystemExit("G1SPRM unexpectedly creates acceptance or parking")
    if matrix_review["accepts_source_profile"] or matrix_review["creates_parking_decision"]:
        raise SystemExit("G1SPRMREV unexpectedly accepts source profile or creates parking")
    if ocrhm["creates_acceptance"] or ocrhm["creates_parking_decision"] or ocrhm["executes_ocr"]:
        raise SystemExit("OCRHM unexpectedly creates acceptance, parking, or OCR execution")
    return verified, g1sp17, matrix, matrix_review, ocrhm


def classify_rows(matrix: dict) -> list[dict]:
    rows: list[dict] = []
    seen: set[str] = set()
    for row in matrix["rows"]:
        row_id = row["id"]
        if row_id in seen:
            raise SystemExit(f"duplicate matrix row: {row_id}")
        seen.add(row_id)
        category = ROW_DECISION_MAP.get(row_id)
        if category is None:
            raise SystemExit(f"unclassified matrix row: {row_id}")
        rows.append(
            {
                "source_matrix_row_id": row_id,
                "source_matrix_disposition": row["disposition"],
                "decision_prep_category": category,
                "category": row["category"],
                "basis": row["basis"],
                "creates_acceptance": False,
                "creates_parking_decision": False,
                "requires_future_explicit_decision": True,
            }
        )
    expected = set(ROW_DECISION_MAP)
    if seen != expected:
        raise SystemExit(f"matrix row set mismatch: missing={sorted(expected - seen)} extra={sorted(seen - expected)}")
    return rows


def build_packet(verified_inputs: dict[str, dict[str, str]], g1sp17: dict, matrix: dict, matrix_review: dict, ocrhm: dict) -> dict:
    rows = classify_rows(matrix)
    counts = {category: sum(1 for row in rows if row["decision_prep_category"] == category) for category in DECISION_CATEGORIES}
    return {
        "packet_id": PACKET_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "gate_1_source_profile_review_parking_decision_prep_ready_for_human_review",
        "purpose": "decision_prep_no_acceptance_no_parking",
        "creates_acceptance": False,
        "creates_parking_decision": False,
        "accepts_source_profile": False,
        "accepts_whole_gate_1": False,
        "admits_fixture": False,
        "executes_ocr": False,
        "processes_page_021_plus": False,
        "consumed_status_refresh": g1sp17["status_packet_id"],
        "consumed_matrix": matrix["matrix_id"],
        "consumed_matrix_review": matrix_review["review_id"],
        "consumed_ocr_hardening": ocrhm["hardening_id"],
        "page_complete_accepted_pages": g1sp17["page_complete_accepted_pages"],
        "page_complete_acceptance_scope": "individual_pages_only",
        "page_021_plus_state": "unprocessed_not_authorized",
        "decision_categories": DECISION_CATEGORIES,
        "decision_prep_rows": rows,
        "decision_prep_counts": counts,
        "remaining_actual_decisions": [
            "source_profile_acceptance_or_parking",
            "unsupported_profiles_and_negative_fixtures",
            "fixture_admission",
            "page_021_plus_disposition",
            "whole_gate_1_acceptance",
        ],
        "negative_capability_matrix": {name: False for name in NEGATIVE_CAPABILITIES},
        "verified_inputs": verified_inputs,
    }


def write_summary(packet: dict) -> None:
    lines = [
        "# Gate 1 Source-Profile Review / Parking Decision Prep - G1SPRPD-G1-VIRAL-001",
        "",
        "Status: `gate_1_source_profile_review_parking_decision_prep_ready_for_human_review`",
        "",
        "Purpose: decision prep only. This packet creates no source-profile acceptance and no parking decision.",
        "",
        "## Counts",
        "",
    ]
    for category, count in packet["decision_prep_counts"].items():
        lines.append(f"- `{category}`: {count}")
    lines.extend(["", "## Rows", ""])
    for row in packet["decision_prep_rows"]:
        lines.append(f"- `{row['source_matrix_row_id']}` -> `{row['decision_prep_category']}`")
    lines.extend(
        [
            "",
            "## Remaining Actual Decisions",
            "",
        ]
    )
    for decision in packet["remaining_actual_decisions"]:
        lines.append(f"- `{decision}`")
    lines.extend(
        [
            "",
            "## Boundaries",
            "",
            "- No source-profile acceptance.",
            "- No parking decision.",
            "- No fixture admission.",
            "- No whole Gate 1 acceptance.",
            "- No OCR execution or remediation rerun.",
            "- No page 021+ processing.",
            "",
        ]
    )
    write_text(OUT_ROOT / "gate_1_source_profile_review_parking_decision_prep_summary.md", "\n".join(lines))


def write_report(packet: dict) -> None:
    write_json(
        OUT_ROOT / "gate_1_source_profile_review_parking_decision_prep_report.json",
        {
            "packet_id": PACKET_ID,
            "authorization_id": AUTHORIZATION_ID,
            "status": packet["status"],
            "generator_script": SCRIPT_PATH.relative_to(ROOT).as_posix(),
            "generator_script_sha256": sha256_file(SCRIPT_PATH),
            "test_contract": TEST_PATH.relative_to(ROOT).as_posix(),
            "test_contract_sha256": sha256_file(TEST_PATH) if TEST_PATH.exists() else None,
            "creates_acceptance": False,
            "creates_parking_decision": False,
            "accepts_source_profile": False,
            "accepts_whole_gate_1": False,
            "admits_fixture": False,
            "executes_ocr": False,
            "processes_page_021_plus": False,
            "decision_prep_counts": packet["decision_prep_counts"],
            "remaining_actual_decisions": packet["remaining_actual_decisions"],
            "negative_capability_matrix": packet["negative_capability_matrix"],
        },
    )


def write_manifest() -> None:
    manifest_name = "gate_1_source_profile_review_parking_decision_prep_manifest.md"
    lines = [
        "# Gate 1 Source-Profile Review / Parking Decision Prep Manifest - G1SPRPD-G1-VIRAL-001",
        "",
        "Status: `gate_1_source_profile_review_parking_decision_prep_ready_for_human_review`",
        "",
        "Boundary: decision prep only; no acceptance, no parking decision, no OCR execution, no page 021+ authorization, no fixture admission, and no whole Gate 1 acceptance.",
        "",
        "## Output Hashes",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for path in sorted(OUT_ROOT.rglob("*")):
        if path.is_file() and path.name != manifest_name:
            lines.append(f"| `{path.relative_to(OUT_ROOT).as_posix()}` | `{sha256_file(path)}` |")
    lines.append("")
    write_text(OUT_ROOT / manifest_name, "\n".join(lines))


def build() -> None:
    verified_inputs, g1sp17, matrix, matrix_review, ocrhm = verify_inputs()
    if OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    packet = build_packet(verified_inputs, g1sp17, matrix, matrix_review, ocrhm)
    write_json(OUT_ROOT / "gate_1_source_profile_review_parking_decision_prep.json", packet)
    write_summary(packet)
    write_report(packet)
    write_manifest()


if __name__ == "__main__":
    check_authorization()
    build()
