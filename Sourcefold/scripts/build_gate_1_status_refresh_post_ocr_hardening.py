from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "build_gate_1_status_refresh_post_ocr_hardening.py"
TEST_PATH = ROOT / "tests" / "test_gate_1_status_refresh_post_ocr_hardening.py"
AUTHORIZATION_LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "gate_1_status_packet_G1_VIRAL_017"

AUTHORIZATION_ID = "BA-G1-VIRAL-POST-OCR-HARDENING-STATUS-READINESS-001"
STATUS_PACKET_ID = "G1SP-G1-VIRAL-017"

INPUT_HASHES = {
    "G1SP-G1-VIRAL-016.packet": (
        TRIAL_ROOT / "gate_1_status_packet_G1_VIRAL_016" / "gate_1_status_packet.json",
        "C69701A098CC33486B89C6F0D7F8D1A890B05C288DC8F814A430D44ABF47F88F",
    ),
    "G1SP-G1-VIRAL-016.report": (
        TRIAL_ROOT / "gate_1_status_packet_G1_VIRAL_016" / "gate_1_status_report.json",
        "3C051D65A15CB4DE0FA5649D6FE6C5C81AC75B3A752EC80E126EA81E50713F05",
    ),
    "G1SPRMREV-G1-VIRAL-001.review": (
        TRIAL_ROOT
        / "gate_1_source_profile_readiness_parking_matrix_review_G1_VIRAL_001"
        / "gate_1_source_profile_readiness_parking_matrix_review.json",
        "76D0B43FCE9B614424A47FEBDE61666E42B372E671396E876E1F59B38FCEC640",
    ),
    "OCRHM-G1-VIRAL-001.packet": (
        TRIAL_ROOT / "ocr_benchmark_methodology_hardening_G1_VIRAL_001" / "ocr_benchmark_methodology_hardening.json",
        "AF62629E87F757929CC609C13198DB2594E4837F1296E1D9EF242E7E21B11C36",
    ),
    "OCRHM-G1-VIRAL-001.report": (
        TRIAL_ROOT / "ocr_benchmark_methodology_hardening_G1_VIRAL_001" / "ocr_benchmark_methodology_hardening_report.json",
        "08A913FED762D70FE603FEAD390804C067695071B580DEE00F50C22D68E991A5",
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


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json(path: Path, payload: object) -> None:
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8", newline="\n")


def write_text(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8", newline="\n")


def check_authorization(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Build post-OCR-hardening Gate 1 status/readiness refresh.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("post-OCR-hardening Gate 1 status/readiness refresh is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"post-OCR-hardening Gate 1 status/readiness refresh requires {AUTHORIZATION_ID}")


def verify_authorization_ledger() -> None:
    ledger = AUTHORIZATION_LEDGER.read_text(encoding="utf-8-sig")
    if f"## {AUTHORIZATION_ID}" not in ledger:
        raise SystemExit(f"{AUTHORIZATION_ID} is missing from bounded trial authorization ledger")


def verify_inputs() -> tuple[dict[str, dict[str, str]], dict, dict, dict]:
    verify_authorization_ledger()
    verified: dict[str, dict[str, str]] = {}
    for key, (path, expected) in INPUT_HASHES.items():
        actual = sha256_file(path)
        if actual != expected:
            raise SystemExit(f"{key} hash mismatch: {actual}")
        verified[key] = {"path": path.relative_to(ROOT).as_posix(), "sha256": actual}
    g1sp16 = read_json(INPUT_HASHES["G1SP-G1-VIRAL-016.packet"][0])
    matrix_review = read_json(INPUT_HASHES["G1SPRMREV-G1-VIRAL-001.review"][0])
    ocrhm = read_json(INPUT_HASHES["OCRHM-G1-VIRAL-001.packet"][0])
    if matrix_review["accepts_source_profile"] is not False:
        raise SystemExit("matrix review unexpectedly accepts source profile")
    if ocrhm["creates_acceptance"] is not False or ocrhm["executes_ocr"] is not False:
        raise SystemExit("OCR hardening unexpectedly creates acceptance or executes OCR")
    return verified, g1sp16, matrix_review, ocrhm


def build_packet(verified_inputs: dict[str, dict[str, str]], g1sp16: dict, matrix_review: dict, ocrhm: dict) -> dict:
    return {
        "status_packet_id": STATUS_PACKET_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "gate_1_status_post_ocr_hardening_ready_for_route_decision",
        "purpose": "post_ocr_hardening_gate_1_readiness_refresh_no_acceptance",
        "creates_acceptance": False,
        "creates_parking_decision": False,
        "executes_ocr": False,
        "page_complete_accepted_pages": g1sp16["baseline"]["page_complete_accepted_pages"],
        "page_complete_acceptance_scope": "individual_pages_only",
        "page_021_plus_state": "unprocessed_not_authorized",
        "whole_gate_1_acceptance": False,
        "consumed_route_review": matrix_review["review_id"],
        "consumed_ocr_hardening": ocrhm["hardening_id"],
        "readiness_flags": {
            "pages_001_020_page_complete_accepted_only": True,
            "source_profile_readiness_matrix_review_accepted": True,
            "ocr_benchmark_methodology_hardened_for_gate_review": True,
            "ocr_benchmark_remediation_unresolved": False,
            "source_profile_accepted": False,
            "parking_decisions_recorded": False,
            "unsupported_profiles_negative_fixtures_decided": False,
            "page_021_plus_authorized": False,
            "whole_gate_1_accepted": False,
        },
        "remaining_blockers": [
            "source_profile_acceptance_or_parking_decisions_not_recorded",
            "unsupported_profiles_and_negative_fixtures_need_decision",
            "page_021_plus_disposition_not_authorized",
            "whole_gate_1_acceptance_not_recorded",
            "fixture_admission_not_recorded",
        ],
        "recommended_next_candidates": [
            {
                "candidate": "gate_1_source_profile_review_or_parking_decision",
                "why": "pages 001-020, matrix review, and OCR methodology hardening are ready as decision-prep evidence",
                "requires_new_bounded_authorization": True,
            },
            {
                "candidate": "page_021_or_p021_p025_aggressive_lane",
                "why": "only if Bogdan chooses to continue page-complete processing instead of Gate 1 decisions",
                "requires_new_bounded_authorization": True,
            },
        ],
        "negative_capability_matrix": {name: False for name in NEGATIVE_CAPABILITIES},
        "verified_inputs": verified_inputs,
    }


def write_summary(packet: dict) -> None:
    lines = [
        "# Gate 1 Status Packet - G1SP-G1-VIRAL-017",
        "",
        "Status: `gate_1_status_post_ocr_hardening_ready_for_route_decision`",
        "",
        "Purpose: post-OCR-hardening Gate 1 readiness refresh. This packet creates no acceptance.",
        "",
        "## Current Ready Evidence",
        "",
        "- Pages `001-020`: page-complete accepted only.",
        "- `G1SPRMREV-G1-VIRAL-001`: source-profile readiness matrix route-review artifact accepted with comments.",
        "- `OCRHM-G1-VIRAL-001`: OCR benchmark methodology hardened for Gate review.",
        "",
        "## Remaining Blockers",
        "",
    ]
    for blocker in packet["remaining_blockers"]:
        lines.append(f"- `{blocker}`")
    lines.extend(
        [
            "",
            "## Recommended Next Candidates",
            "",
        ]
    )
    for candidate in packet["recommended_next_candidates"]:
        lines.append(f"- `{candidate['candidate']}`: {candidate['why']}")
    lines.extend(
        [
            "",
            "## Boundaries",
            "",
            "- No source-profile acceptance.",
            "- No parking decision.",
            "- No whole Gate 1 acceptance.",
            "- No OCR execution or remediation rerun.",
            "- No page 021+ processing.",
            "",
        ]
    )
    write_text(OUT_ROOT / "gate_1_status_summary.md", "\n".join(lines))


def write_report(packet: dict) -> None:
    write_json(
        OUT_ROOT / "gate_1_status_report.json",
        {
            "status_packet_id": STATUS_PACKET_ID,
            "authorization_id": AUTHORIZATION_ID,
            "status": packet["status"],
            "generator_script": SCRIPT_PATH.relative_to(ROOT).as_posix(),
            "generator_script_sha256": sha256_file(SCRIPT_PATH),
            "test_contract": TEST_PATH.relative_to(ROOT).as_posix(),
            "test_contract_sha256": sha256_file(TEST_PATH) if TEST_PATH.exists() else None,
            "creates_acceptance": False,
            "creates_parking_decision": False,
            "executes_ocr": False,
            "remaining_blockers": packet["remaining_blockers"],
            "recommended_next_candidates": packet["recommended_next_candidates"],
            "negative_capability_matrix": packet["negative_capability_matrix"],
        },
    )


def write_manifest() -> None:
    manifest_name = "gate_1_status_manifest.md"
    lines = [
        "# Gate 1 Status Manifest - G1SP-G1-VIRAL-017",
        "",
        "Status: `gate_1_status_post_ocr_hardening_ready_for_route_decision`",
        "",
        "Boundary: status/readiness refresh only; no acceptance, no parking decision, no OCR execution, no page 021+ authorization, and no whole Gate 1 acceptance.",
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
    verified_inputs, g1sp16, matrix_review, ocrhm = verify_inputs()
    if OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    packet = build_packet(verified_inputs, g1sp16, matrix_review, ocrhm)
    write_json(OUT_ROOT / "gate_1_status_packet.json", packet)
    write_summary(packet)
    write_report(packet)
    write_manifest()


if __name__ == "__main__":
    check_authorization()
    build()
