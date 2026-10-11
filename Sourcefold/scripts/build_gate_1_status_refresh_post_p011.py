from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "build_gate_1_status_refresh_post_p011.py"
TEST_PATH = ROOT / "tests" / "test_gate_1_status_refresh_post_p011.py"
AUTHORIZATION_LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "gate_1_status_packet_G1_VIRAL_006"

AUTHORIZATION_ID = "BA-G1-VIRAL-GATE-1-STATUS-REFRESH-006"
STATUS_PACKET_ID = "G1SP-G1-VIRAL-006"

PAGE_ACCEPTANCE_REPORT_HASHES = {
    "001": ("P001PCA-G1-VIRAL-001", "page_complete_acceptance_p001_G1_VIRAL_001", "0ED79F4FE7A9E239E6992CEDA9C9A73CDD3B39E6BD71BBDEC68DBCFDF6C9BF0B"),
    "002": ("P002PCA-G1-VIRAL-001", "page_complete_acceptance_p002_G1_VIRAL_001", "B136282C441D1E48DE9CE064356B3B06F6D45A500C1984901D53908335D8547C"),
    "003": ("P003PCA-G1-VIRAL-001", "page_complete_acceptance_p003_G1_VIRAL_001", "9D74A9B73D657A0669AD0025B40936E1873A9643F1F03F31279B87FCFAFA5F79"),
    "004": ("P004PCA-G1-VIRAL-001", "page_complete_acceptance_p004_G1_VIRAL_001", "57D4E5B3665129732308E042B4CECEEDD170907B2DCB852468DBBF885C222035"),
    "005": ("P005PCA-G1-VIRAL-001", "page_complete_acceptance_p005_G1_VIRAL_001", "2065A5C139E42514AD92EFB897151CE87CEEEF42208B9A7F99482B7A7F923022"),
    "006": ("P006PCA-G1-VIRAL-001", "page_complete_acceptance_p006_G1_VIRAL_001", "9D0643332F24AF2B5FF3D14518B9FF83B70B331FA1E165577A6C5245532692B5"),
    "007": ("P007PCA-G1-VIRAL-001", "page_complete_acceptance_p007_G1_VIRAL_001", "8A1B163709D47D9268602C8F2EEF5F5E880E450807468DC9EB360BE8C7CC80F5"),
    "008": ("P008PCA-G1-VIRAL-001", "page_complete_acceptance_p008_G1_VIRAL_001", "44F126668C6A6F148579787917D93199D0413F51DE0E8C3C6143AAA4047B0F64"),
    "009": ("P009PCA-G1-VIRAL-001", "page_complete_acceptance_p009_G1_VIRAL_001", "87F11A29136C46E4ED20E70054F8B3ADF2C1AE869458F8A37A82D9A593DF8051"),
    "010": ("P010PCA-G1-VIRAL-001", "page_complete_acceptance_p010_G1_VIRAL_001", "4EA737E0AD3A902479275563F1361BE89DF72E4C8825FC8D617134FB20A1C58E"),
    "011": ("P011PCA-G1-VIRAL-001", "page_complete_acceptance_p011_G1_VIRAL_001", "973E19C9E58EEEF3CABEAC16FD9C887948B7AF81F18916738E8867913E09B0A3"),
}

G1SP_005 = {
    "package_id": "G1SP-G1-VIRAL-005",
    "root": "gate_1_status_packet_G1_VIRAL_005",
    "packet_sha256": "E696DE1651E43539A07ECA958B948678DE7FFAAE61EB426F2CE46C478C5310E2",
}

FORBIDDEN_CAPABILITIES = [
    "fixture_admission",
    "source_mutation",
    "new_source_acceptance",
    "ocr_execution",
    "render_execution",
    "pdf_parsing_or_text_layer_extraction",
    "raw_mutation",
    "translation",
    "proofreading",
    "renderer_profile_acceptance",
    "implementation",
    "push",
    "page_012_processing_authorized",
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
    parser = argparse.ArgumentParser(description="Build post-P011 Gate 1 status refresh packet.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("post-P011 Gate 1 status refresh is fail-closed; pass --execute with exact authorization id")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"post-P011 Gate 1 status refresh requires {AUTHORIZATION_ID}")


def verify_authorization_ledger() -> None:
    ledger = AUTHORIZATION_LEDGER.read_text(encoding="utf-8-sig")
    if f"## {AUTHORIZATION_ID}" not in ledger:
        raise SystemExit(f"{AUTHORIZATION_ID} is missing from bounded trial authorization ledger")


def verify_hashes() -> None:
    verify_authorization_ledger()
    for page, (_package_id, root, expected) in PAGE_ACCEPTANCE_REPORT_HASHES.items():
        actual = sha256_file(TRIAL_ROOT / root / "page_complete_acceptance_report.json")
        if actual != expected:
            raise SystemExit(f"page {page} acceptance report hash mismatch: {actual}")
    actual_g1sp = sha256_file(TRIAL_ROOT / G1SP_005["root"] / "gate_1_status_packet.json")
    if actual_g1sp != G1SP_005["packet_sha256"]:
        raise SystemExit(f"G1SP-005 packet hash mismatch: {actual_g1sp}")


def build_packet() -> dict[str, object]:
    accepted_pages = sorted(PAGE_ACCEPTANCE_REPORT_HASHES)
    return {
        "status_packet_id": STATUS_PACKET_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "gate_1_status_route_packet_ready_no_acceptance",
        "purpose": "post_P011_status_refresh_to_route_page_012_triage_or_other_bounded_branches",
        "creates_acceptance": False,
        "baseline": {
            "page_complete_accepted_pages": accepted_pages,
            "page_complete_acceptance_scope": "individual_pages_only",
            "source_reconstruction_current_canonical_narrow_state": "13_accepted_records",
            "new_source_acceptance_rollup_created": False,
            "g1sp_005_state": "stale_only_for_page_011_not_yet_accepted_after_P011PCA",
        },
        "blocker_flags": {
            "pages_001_011_complete": True,
            "pages_012_020_unstarted": True,
            "whole_gate_1_acceptance": False,
            "source_profile_parameters_unaccepted_or_unparked": True,
            "ocr_benchmark_remediation_unresolved": True,
            "gate_1_status_only_no_acceptance": True,
        },
        "negative_capability_matrix": {name: False for name in FORBIDDEN_CAPABILITIES},
        "predecessor_bindings": {
            "page_complete_acceptances": {
                page: {
                    "package_id": package_id,
                    "state": "page_complete_accepted",
                    "scope": f"page_{page}_only",
                    "root": root,
                    "report_sha256": report_sha256,
                }
                for page, (package_id, root, report_sha256) in PAGE_ACCEPTANCE_REPORT_HASHES.items()
            },
            "status_predecessor": G1SP_005,
        },
        "routing_matrix": [
            {
                "option": "page_012_triage_readiness",
                "status": "recommended_next_candidate_not_authorized_by_this_packet",
                "why": "smallest next page slice after pages 001-011 page-complete coverage",
            },
            {
                "option": "ocr_benchmark_remediation",
                "status": "separate_branch_not_authorized",
                "why": "methodology debt remains unresolved before whole-Gate maturity",
            },
            {
                "option": "source_profile_or_gate_1_parameter_parking_or_acceptance_review",
                "status": "separate_branch_not_authorized",
                "why": "requires explicit parameter scope and accepted/parked disposition",
            },
            {
                "option": "whole_gate_1_acceptance",
                "status": "not_ready",
                "why": "not ready while pages_012_020_unstarted, source_profile_parameters_unaccepted_or_unparked, and ocr_benchmark_remediation_unresolved remain blockers",
            },
        ],
        "recommended_next_candidate": "page_012_triage_readiness",
    }


def write_summary(packet: dict[str, object]) -> None:
    lines = [
        "# Gate 1 Status Route Packet - G1SP-G1-VIRAL-006",
        "",
        "Status: `gate_1_status_route_packet_ready_no_acceptance`",
        "",
        "Purpose: post-P011 status refresh. This packet updates the route after page 011 became page-complete accepted; it does not authorize the next layer.",
        "",
        "## Baseline",
        "",
        "- Page-complete accepted only: `001`, `002`, `003`, `004`, `005`, `006`, `007`, `008`, `009`, `010`, `011`.",
        "- Source reconstruction current canonical narrow state: `13 accepted records`.",
        "- `G1SP-G1-VIRAL-005`: stale only for the old page 011 not-yet-accepted route state.",
        "- New source-acceptance rollup created here: `false`.",
        "",
        "## First-Class Blockers",
        "",
        "- `pages_001_011_complete=true`",
        "- `pages_012_020_unstarted=true`",
        "- `whole_gate_1_acceptance=false`",
        "- `source_profile_parameters_unaccepted_or_unparked=true`",
        "- `ocr_benchmark_remediation_unresolved=true`",
        "- `gate_1_status_only_no_acceptance=true`",
        "",
        "## Routing Matrix",
        "",
        "| Option | Status |",
        "|---|---|",
    ]
    for option in packet["routing_matrix"]:
        lines.append(f"| `{option['option']}` | `{option['status']}` |")
    lines.extend(["", "Recommended next candidate: `page_012_triage_readiness`.", "", "Decision after review: `status packet ok` or `hold status packet: <reason>`.", ""])
    (OUT_ROOT / "gate_1_status_summary.md").write_text("\n".join(lines), encoding="utf-8", newline="\n")


def write_report(packet: dict[str, object]) -> None:
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
            "new_source_acceptance_rollup_created": False,
            "whole_gate_1_acceptance": False,
            "negative_capability_matrix": packet["negative_capability_matrix"],
            "blocker_flags": packet["blocker_flags"],
            "recommended_next_candidate": packet["recommended_next_candidate"],
        },
    )


def write_manifest() -> None:
    lines = [
        "# Gate 1 Status Route Manifest - G1SP-G1-VIRAL-006",
        "",
        "Status: `gate_1_status_route_packet_ready_no_acceptance`",
        "",
        "Boundary: this status route packet creates no acceptance, no source mutation, no OCR/render/PDF/raw mutation, and no next-layer authorization.",
        "",
        "## Output Hashes",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for path in sorted(OUT_ROOT.rglob("*")):
        if path.is_file() and path.name != "gate_1_status_manifest.md":
            lines.append(f"| `{path.relative_to(OUT_ROOT).as_posix()}` | `{sha256_file(path)}` |")
    lines.append("")
    (OUT_ROOT / "gate_1_status_manifest.md").write_text("\n".join(lines), encoding="utf-8", newline="\n")


def build() -> None:
    verify_hashes()
    if OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    packet = build_packet()
    write_json(OUT_ROOT / "gate_1_status_packet.json", packet)
    write_summary(packet)
    write_report(packet)
    write_manifest()


if __name__ == "__main__":
    check_authorization()
    build()
