from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "build_gate_1_source_profile_decision_packet.py"
TEST_PATH = ROOT / "tests" / "test_gate_1_source_profile_decision_packet.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
PREP_ROOT = TRIAL_ROOT / "gate_1_source_profile_review_parking_decision_prep_G1_VIRAL_001"
REVIEW_ROOT = TRIAL_ROOT / "gate_1_source_profile_review_parking_decision_prep_review_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "gate_1_source_profile_decision_packet_G1_VIRAL_001"
LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"

AUTHORIZATION_ID = "BA-G1-VIRAL-SOURCE-PROFILE-DECISION-PACKET-001"
PACKET_ID = "G1SPDP-G1-VIRAL-001"

INPUT_HASHES = {
    "G1SPRPDREV-G1-VIRAL-001.review": (
        REVIEW_ROOT / "gate_1_source_profile_review_parking_decision_prep_review.json",
        "118241D5A8CFB01FBD0DFBB4C1D0424E97B52E976A52F4EA10045A452C4F8CE8",
    ),
    "G1SPRPDREV-G1-VIRAL-001.summary": (
        REVIEW_ROOT / "gate_1_source_profile_review_parking_decision_prep_review_summary.md",
        "AB6CEB2E5D3BD8A68F10C173D2700FA7413466082B8CAC91ACEB5D71B701541F",
    ),
    "G1SPRPDREV-G1-VIRAL-001.manifest": (
        REVIEW_ROOT / "gate_1_source_profile_review_parking_decision_prep_review_manifest.md",
        "FAD4F428CAA277D1F7E6537CC6BE9230EBF4865B69731CD7CC8AD350E78888D5",
    ),
    "G1SPRPD-G1-VIRAL-001.packet": (
        PREP_ROOT / "gate_1_source_profile_review_parking_decision_prep.json",
        "3572FBB2A2A23DD9B4B3A2D9C518849F91AF60367A5165CA72AECE6E1AB7A06C",
    ),
    "G1SPRPD-G1-VIRAL-001.report": (
        PREP_ROOT / "gate_1_source_profile_review_parking_decision_prep_report.json",
        "E31CFE5960F876EF483C5AEE8A65A8F4C5BD364D27201CC3ECC59E2E4DD94E44",
    ),
    "G1SPRPD-G1-VIRAL-001.summary": (
        PREP_ROOT / "gate_1_source_profile_review_parking_decision_prep_summary.md",
        "F9FEE23C6B5341E289C3776C590DA6918B82167AA9266942F4C47C8ED017C0B0",
    ),
    "G1SPRPD-G1-VIRAL-001.manifest": (
        PREP_ROOT / "gate_1_source_profile_review_parking_decision_prep_manifest.md",
        "E310CC116A9DA41BE833770F69C3FC92FE2E7B3C53B3EFF3C0CAB9ABC1BF84A7",
    ),
}

NEGATIVE_CAPABILITIES = [
    "source_profile_acceptance",
    "creates_parking_decision",
    "whole_gate_1_acceptance",
    "fixture_admission",
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


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8", newline="\n")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def check_authorization(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Build Gate 1 source-profile decision options packet.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("Gate 1 source-profile decision packet is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"Gate 1 source-profile decision packet requires {AUTHORIZATION_ID}")


def verify_inputs() -> tuple[dict[str, dict[str, str]], dict, dict]:
    ledger = LEDGER.read_text(encoding="utf-8-sig")
    if f"## {AUTHORIZATION_ID}" not in ledger:
        raise SystemExit(f"{AUTHORIZATION_ID} missing from ledger")

    verified: dict[str, dict[str, str]] = {}
    for key, (path, expected) in INPUT_HASHES.items():
        actual = sha256_file(path)
        if actual != expected:
            raise SystemExit(f"{key} hash mismatch: {actual}")
        verified[key] = {"path": path.relative_to(ROOT).as_posix(), "sha256": actual}
    review = read_json(INPUT_HASHES["G1SPRPDREV-G1-VIRAL-001.review"][0])
    prep = read_json(INPUT_HASHES["G1SPRPD-G1-VIRAL-001.packet"][0])
    if review["review_id"] != "G1SPRPDREV-G1-VIRAL-001" or not review["authorizes_next_packet_prep"]:
        raise SystemExit("G1SPRPDREV is not an accepted next-packet prep review")
    for key in ["accepts_source_profile", "creates_parking_decision", "accepts_whole_gate_1", "admits_fixture"]:
        if review[key] or prep[key]:
            raise SystemExit(f"{key} unexpectedly true")
    if prep["processes_page_021_plus"]:
        raise SystemExit("prep unexpectedly processes page 021+")
    return verified, review, prep


def option(option_id: str, source_rows: list[str], title: str, prompt: str) -> dict:
    return {
        "option_id": option_id,
        "source_rows": source_rows,
        "title": title,
        "human_prompt": prompt,
        "requires_future_explicit_decision": True,
        "creates_acceptance": False,
        "creates_parking_decision": False,
    }


def build_packet(verified_inputs: dict[str, dict[str, str]], review: dict, prep: dict) -> dict:
    rows = prep["decision_prep_rows"]
    return {
        "packet_id": PACKET_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "gate_1_source_profile_decision_packet_ready_for_human_options_review",
        "purpose": "decision_packet_prep_no_acceptance_no_parking",
        "creates_acceptance": False,
        "accepts_source_profile": False,
        "creates_parking_decision": False,
        "accepts_whole_gate_1": False,
        "admits_fixture": False,
        "processes_page_021_plus": False,
        "executes_ocr": False,
        "controlling_review": review["review_id"],
        "source_prep_packet": prep["packet_id"],
        "decision_rows": rows,
        "decision_options": [
            option(
                "accept_selected_source_profile_elements_for_gate_review_candidate_status",
                [row["source_matrix_row_id"] for row in rows if row["decision_prep_category"] == "accept_for_gate_review_candidate"],
                "Accept selected source-profile elements for Gate review candidate status.",
                "Should these five rows advance to a future source-profile acceptance decision packet?",
            ),
            option(
                "park_ocr_methodology_for_core_0_1_with_invalidation_conditions",
                [row["source_matrix_row_id"] for row in rows if row["decision_prep_category"] == "park_for_0_1_with_invalidation_conditions"],
                "Park OCR methodology/remediation debt for Core 0.1 with invalidation conditions.",
                "Should these OCR rows be proposed for future parking rather than acceptance?",
            ),
            option(
                "keep_render_and_source_reconstruction_evidence_only",
                [row["source_matrix_row_id"] for row in rows if row["decision_prep_category"] == "remain_evidence_only_not_accepting"],
                "Keep render/source-reconstruction evidence as evidence-only.",
                "Should these evidence rows remain non-accepting support material?",
            ),
            option(
                "hold_unsupported_profiles_and_whole_gate_1_blocked",
                [row["source_matrix_row_id"] for row in rows if row["decision_prep_category"] == "hold_blocked_needs_decision"],
                "Hold unsupported/negative fixture and whole Gate 1 questions as blocked.",
                "Should these rows remain blocked until a later explicit decision?",
            ),
            option(
                "require_separate_ba_for_page_021_plus",
                [row["source_matrix_row_id"] for row in rows if row["decision_prep_category"] == "requires_separate_bounded_authorization"],
                "Require separate bounded authorization for page 021+.",
                "Should page 021+ remain outside this Gate 1 decision path?",
            ),
        ],
        "remaining_actual_decisions": prep["remaining_actual_decisions"],
        "negative_capability_matrix": {name: False for name in NEGATIVE_CAPABILITIES},
        "verified_inputs": verified_inputs,
    }


def write_summary(packet: dict) -> None:
    lines = [
        "# Gate 1 Source-Profile Decision Packet - G1SPDP-G1-VIRAL-001",
        "",
        "Status: `gate_1_source_profile_decision_packet_ready_for_human_options_review`",
        "",
        "Purpose: human-facing decision-options packet only. No source-profile acceptance and no parking decision yet.",
        "",
        "## Options",
        "",
    ]
    for opt in packet["decision_options"]:
        lines.append(f"- `{opt['option_id']}`: {opt['title']}")
    lines.extend(["", "## Remaining Actual Decisions", ""])
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
            "- No page 021+ processing.",
            "- No OCR execution or remediation rerun.",
            "",
        ]
    )
    write_text(OUT_ROOT / "gate_1_source_profile_decision_packet_summary.md", "\n".join(lines))


def write_report(packet: dict) -> None:
    write_json(
        OUT_ROOT / "gate_1_source_profile_decision_packet_report.json",
        {
            "packet_id": PACKET_ID,
            "authorization_id": AUTHORIZATION_ID,
            "status": packet["status"],
            "generator_script": SCRIPT_PATH.relative_to(ROOT).as_posix(),
            "generator_script_sha256": sha256_file(SCRIPT_PATH),
            "test_contract": TEST_PATH.relative_to(ROOT).as_posix(),
            "test_contract_sha256": sha256_file(TEST_PATH) if TEST_PATH.exists() else None,
            "creates_acceptance": False,
            "accepts_source_profile": False,
            "creates_parking_decision": False,
            "accepts_whole_gate_1": False,
            "admits_fixture": False,
            "processes_page_021_plus": False,
            "executes_ocr": False,
            "decision_option_count": len(packet["decision_options"]),
            "negative_capability_matrix": packet["negative_capability_matrix"],
        },
    )


def write_manifest() -> None:
    manifest_name = "gate_1_source_profile_decision_packet_manifest.md"
    lines = [
        "# Gate 1 Source-Profile Decision Packet Manifest - G1SPDP-G1-VIRAL-001",
        "",
        "Status: `gate_1_source_profile_decision_packet_ready_for_human_options_review`",
        "",
        "Boundary: options packet only; no source-profile acceptance, no parking decision, no page 021+ authorization, no fixture admission, and no whole Gate 1 acceptance.",
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
    verified_inputs, review, prep = verify_inputs()
    if OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    packet = build_packet(verified_inputs, review, prep)
    write_json(OUT_ROOT / "gate_1_source_profile_decision_packet.json", packet)
    write_summary(packet)
    write_report(packet)
    write_manifest()


if __name__ == "__main__":
    check_authorization()
    build()
