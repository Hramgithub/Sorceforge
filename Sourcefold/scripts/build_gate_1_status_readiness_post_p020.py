from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "build_gate_1_status_readiness_post_p020.py"
TEST_PATH = ROOT / "tests" / "test_gate_1_status_readiness_post_p020.py"
AUTHORIZATION_LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "gate_1_status_packet_G1_VIRAL_016"

AUTHORIZATION_ID = "BA-G1-VIRAL-POST-P020-STATUS-READINESS-001"
STATUS_PACKET_ID = "G1SP-G1-VIRAL-016"

G1SP_015 = {
    "package_id": "G1SP-G1-VIRAL-015",
    "root": "gate_1_status_packet_G1_VIRAL_015",
    "packet_sha256": "B016D09B91A5C1DA9B3E6026C9E5CF777CE290773864C786A51903FA1FCD62F8",
}

FINAL_REVIEW_REPORT_HASHES = {
    "016": ("P016BATCHREV-G1-VIRAL-001", "page_016_aggressive_batch_final_review_G1_VIRAL_001", "A99DFF6580DB07F3F66303B856EA5FB7A94E215864B4112F59C71B964682FD70"),
    "017": ("P017BATCHREV-G1-VIRAL-001", "page_017_aggressive_batch_final_review_G1_VIRAL_001", "2A0ADB59F9FCA08D1DD6542842CC7C030660A2BF64512CC1C2CC386BEE6C9534"),
    "018": ("P018BATCHREV-G1-VIRAL-001", "page_018_aggressive_batch_final_review_G1_VIRAL_001", "0A563CAED4F29EF055437E952562E84AF35A4F5A894E77FA917B48BE39F7DFC8"),
    "019": ("P019BATCHREV-G1-VIRAL-001", "page_019_aggressive_batch_final_review_G1_VIRAL_001", "B4EFBECC07D519ABB51CC6197C0AF9521CBCAD269A853727542A3C91A0E63C45"),
    "020": ("P020BATCHREV-G1-VIRAL-001", "page_020_aggressive_batch_final_review_G1_VIRAL_001", "B7E024DC1C30FED09539C048182E9369354D0081C9ECA5F4A47A210D957178FB"),
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
    "page_021_plus_processing_authorized",
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
    parser = argparse.ArgumentParser(description="Build post-P020 Gate 1 status/readiness packet.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("post-P020 Gate 1 status/readiness is fail-closed; pass --execute with exact authorization id")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"post-P020 Gate 1 status/readiness requires {AUTHORIZATION_ID}")


def verify_authorization_ledger() -> None:
    ledger = AUTHORIZATION_LEDGER.read_text(encoding="utf-8-sig")
    if f"## {AUTHORIZATION_ID}" not in ledger:
        raise SystemExit(f"{AUTHORIZATION_ID} is missing from bounded trial authorization ledger")


def verify_hashes() -> None:
    verify_authorization_ledger()
    actual_g1sp = sha256_file(TRIAL_ROOT / G1SP_015["root"] / "gate_1_status_packet.json")
    if actual_g1sp != G1SP_015["packet_sha256"]:
        raise SystemExit(f"G1SP-015 packet hash mismatch: {actual_g1sp}")
    for page, (_package_id, root, expected) in FINAL_REVIEW_REPORT_HASHES.items():
        actual = sha256_file(TRIAL_ROOT / root / f"page_{page}_aggressive_batch_final_review_report.json")
        if actual != expected:
            raise SystemExit(f"P{page} final review report hash mismatch: {actual}")


def build_packet() -> dict[str, object]:
    accepted_pages = [f"{page:03d}" for page in range(1, 21)]
    return {
        "status_packet_id": STATUS_PACKET_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "gate_1_status_readiness_packet_post_p020_ready_for_route_decision",
        "purpose": "post_P020_gate_1_status_readiness_decision_prep_no_acceptance",
        "creates_acceptance": False,
        "baseline": {
            "page_complete_accepted_pages": accepted_pages,
            "page_complete_acceptance_scope": "individual_pages_only",
            "p016_p020_final_review_state": "accepted",
            "page_021_plus_state": "unprocessed_not_authorized",
            "whole_gate_1_acceptance": False,
        },
        "blocker_flags": {
            "pages_001_020_complete": True,
            "page_021_plus_unauthorized": True,
            "whole_gate_1_acceptance": False,
            "fixture_admission": False,
            "source_profile_parameters_unaccepted_or_unparked": True,
            "ocr_benchmark_remediation_unresolved": True,
            "gate_1_status_only_no_acceptance": True,
            "stale_current_next_wording_requires_cleanup": True,
        },
        "negative_capability_matrix": {name: False for name in FORBIDDEN_CAPABILITIES},
        "predecessor_bindings": {
            "status_predecessor": G1SP_015,
            "final_human_reviews": {
                page: {
                    "package_id": package_id,
                    "state": "final_human_review_accepted",
                    "scope": f"page_{page}_aggressive_batch_bundle_and_status_only",
                    "root": root,
                    "report_sha256": report_sha256,
                }
                for page, (package_id, root, report_sha256) in FINAL_REVIEW_REPORT_HASHES.items()
            },
        },
        "routing_matrix": [
            {
                "option": "gate_1_source_profile_readiness_or_parking_matrix",
                "status": "recommended_next_candidate_not_authorized_by_this_packet",
                "why": "pages 001-020 are page-complete accepted only, but whole Gate 1 inputs still need accepted or parked dispositions",
            },
            {
                "option": "stale_doc_sync_cleanup",
                "status": "prerequisite_cleanup_not_acceptance",
                "why": "old current/next wording must not route later work back to page 011/015/016 or imply page 021 authorization",
            },
            {
                "option": "page_021_or_p021_p025_aggressive",
                "status": "separate_exact_authorization_required",
                "why": "page 021+ does not inherit the P016-P020 sequential aggressive authorization",
            },
            {
                "option": "ocr_benchmark_remediation",
                "status": "separate_branch_not_authorized",
                "why": "benchmark methodology debt remains unresolved before whole-Gate maturity",
            },
            {
                "option": "whole_gate_1_acceptance",
                "status": "not_ready",
                "why": "page-complete acceptance through 020 is not whole Gate 1 acceptance and does not admit fixtures or source/profile parameters",
            },
        ],
        "recommended_next_candidate": "gate_1_source_profile_readiness_or_parking_matrix",
    }


def write_summary(packet: dict[str, object]) -> None:
    accepted = "`, `".join(packet["baseline"]["page_complete_accepted_pages"])
    lines = [
        "# Gate 1 Status Readiness Packet - G1SP-G1-VIRAL-016",
        "",
        "Status: `gate_1_status_readiness_packet_post_p020_ready_for_route_decision`",
        "",
        "Purpose: post-P020 Gate 1 status/readiness decision prep. This packet creates no acceptance and authorizes no next processing lane.",
        "",
        "## Baseline",
        "",
        f"- Page-complete accepted only: `{accepted}`.",
        "- P016-P020 final human review: `accepted`.",
        "- Page `021+`: `unprocessed_not_authorized`.",
        "- Whole Gate 1 acceptance: `false`.",
        "",
        "## First-Class Blockers",
        "",
        "- `pages_001_020_complete=true`",
        "- `page_021_plus_unauthorized=true`",
        "- `whole_gate_1_acceptance=false`",
        "- `fixture_admission=false`",
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
    lines.extend(
        [
            "",
            "Recommended next candidate: `gate_1_source_profile_readiness_or_parking_matrix`.",
            "",
            "Decision after review: `status readiness packet ok` or `hold status readiness packet: <reason>`.",
            "",
        ]
    )
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
            "page_021_plus_processing_authorized": False,
            "whole_gate_1_acceptance": False,
            "negative_capability_matrix": packet["negative_capability_matrix"],
            "blocker_flags": packet["blocker_flags"],
            "recommended_next_candidate": packet["recommended_next_candidate"],
        },
    )


def write_manifest() -> None:
    lines = [
        "# Gate 1 Status Readiness Manifest - G1SP-G1-VIRAL-016",
        "",
        "Status: `gate_1_status_readiness_packet_post_p020_ready_for_route_decision`",
        "",
        "Boundary: this status/readiness packet creates no acceptance, no page 021+ authorization, no source mutation, no OCR/render/PDF/raw mutation, and no next-layer authorization.",
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
