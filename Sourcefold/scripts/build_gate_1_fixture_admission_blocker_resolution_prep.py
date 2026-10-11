from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "build_gate_1_fixture_admission_blocker_resolution_prep.py"
TEST_PATH = ROOT / "tests" / "test_gate_1_fixture_admission_blocker_resolution_prep.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
FARP_ROOT = TRIAL_ROOT / "gate_1_fixture_admission_readiness_prep_G1_VIRAL_001"
FARPREV_ROOT = TRIAL_ROOT / "gate_1_fixture_admission_readiness_prep_review_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "gate_1_fixture_admission_blocker_resolution_prep_G1_VIRAL_001"
LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"

AUTHORIZATION_ID = "BA-G1-VIRAL-FIXTURE-ADMISSION-BLOCKER-RESOLUTION-PREP-001"
PACKET_ID = "G1FABRP-G1-VIRAL-001"

NEGATIVE_CAPABILITIES = [
    "fixture_admission",
    "fixture_manifest_creation",
    "whole_gate_1_acceptance",
    "source_profile_acceptance",
    "page_021_plus_processing",
    "ocr_execution",
    "ocr_remediation_execution",
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
    parser = argparse.ArgumentParser(description="Build Gate 1 fixture admission blocker resolution prep.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("Gate 1 fixture admission blocker resolution prep is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"Gate 1 fixture admission blocker resolution prep requires {AUTHORIZATION_ID}")


def verify_inputs() -> tuple[dict[str, dict[str, str]], dict, dict]:
    ledger = LEDGER.read_text(encoding="utf-8-sig")
    if f"## {AUTHORIZATION_ID}" not in ledger:
        raise SystemExit(f"{AUTHORIZATION_ID} missing from ledger")

    input_paths = {
        "G1FARP-G1-VIRAL-001.packet": FARP_ROOT / "gate_1_fixture_admission_readiness_prep.json",
        "G1FARP-G1-VIRAL-001.report": FARP_ROOT / "gate_1_fixture_admission_readiness_prep_report.json",
        "G1FARP-G1-VIRAL-001.summary": FARP_ROOT / "gate_1_fixture_admission_readiness_prep_summary.md",
        "G1FARP-G1-VIRAL-001.manifest": FARP_ROOT / "gate_1_fixture_admission_readiness_prep_manifest.md",
        "G1FARPREV-G1-VIRAL-001.review": FARPREV_ROOT / "gate_1_fixture_admission_readiness_prep_review.json",
        "G1FARPREV-G1-VIRAL-001.summary": FARPREV_ROOT / "gate_1_fixture_admission_readiness_prep_review_summary.md",
        "G1FARPREV-G1-VIRAL-001.manifest": FARPREV_ROOT / "gate_1_fixture_admission_readiness_prep_review_manifest.md",
    }
    verified = {
        key: {"path": path.relative_to(ROOT).as_posix(), "sha256": sha256_file(path)}
        for key, path in input_paths.items()
    }
    farp = read_json(input_paths["G1FARP-G1-VIRAL-001.packet"])
    review = read_json(input_paths["G1FARPREV-G1-VIRAL-001.review"])
    if farp["packet_id"] != "G1FARP-G1-VIRAL-001":
        raise SystemExit("unexpected G1FARP packet")
    if review["review_id"] != "G1FARPREV-G1-VIRAL-001":
        raise SystemExit("unexpected G1FARP review")
    if not review["authorizes_next_packet_prep"]:
        raise SystemExit("G1FARP review does not authorize blocker prep")
    for payload in (farp, review):
        if payload["admits_fixture"] or payload["accepts_whole_gate_1"] or payload["processes_page_021_plus"]:
            raise SystemExit("input payload exceeds blocker-prep boundary")
    return verified, farp, review


def build_packet(verified_inputs: dict[str, dict[str, str]], farp: dict, review: dict) -> dict:
    blockers = [
        {
            "blocker_id": "unsupported_negative_fixture_policy",
            "status": "needs_future_policy_decision",
            "source_readiness_row": "unsupported_negative_fixture_policy",
            "resolution_questions": [
                "which unsupported profiles must be declared out of Core 0.1 scope",
                "which negative fixtures are required before fixture admission",
                "what invalidates a future fixture admission decision",
            ],
            "candidate_next_action": "prepare unsupported/negative fixture policy decision packet",
        },
        {
            "blocker_id": "fixture_strategy_fit_check",
            "status": "needs_future_fixture_strategy_decision",
            "source_readiness_row": "fixture_admission_readiness",
            "resolution_questions": [
                "whether pages 001-020 evidence is sufficient fixture-seed material",
                "whether fixture admission must wait for page 021+ disposition",
                "whether evidence-only render/source rows may support fixture strategy without acceptance",
            ],
            "candidate_next_action": "prepare fixture strategy fit decision packet",
        },
        {
            "blocker_id": "whole_gate_1_dependency",
            "status": "blocked_until_fixture_and_policy_decisions",
            "source_readiness_row": "whole_gate_1_acceptance_readiness",
            "resolution_questions": [
                "whether whole Gate 1 acceptance can be considered only after fixture blocker resolution",
                "which Gate 1 dependencies remain non-waivable",
            ],
            "candidate_next_action": "defer whole Gate 1 readiness decision until fixture blockers are resolved",
        },
        {
            "blocker_id": "page_021_plus_boundary",
            "status": "requires_separate_bounded_authorization_if_needed",
            "source_readiness_row": "page_021_plus_boundary",
            "resolution_questions": [
                "whether page 021+ is needed before fixture admission",
                "whether a separate P021 or P021-P025 lane should be opened",
            ],
            "candidate_next_action": "keep page 021+ outside this packet",
        },
    ]
    return {
        "packet_id": PACKET_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "fixture_admission_blocker_resolution_prep_ready_for_review",
        "purpose": "blocker_resolution_prep_only_no_fixture_admission",
        "source_readiness_packet": farp["packet_id"],
        "source_review": review["review_id"],
        "creates_blocker_resolution": False,
        "admits_fixture": False,
        "creates_fixture_manifest": False,
        "accepts_whole_gate_1": False,
        "accepts_source_profile": False,
        "processes_page_021_plus": False,
        "executes_ocr": False,
        "blockers": blockers,
        "recommended_sequence": [
            "unsupported_negative_fixture_policy_decision_prep",
            "fixture_strategy_fit_decision_prep",
            "fixture_admission_readiness_refresh",
            "whole_gate_1_acceptance_readiness_recheck",
        ],
        "inherited_context": {
            "gate_review_candidate_rows": farp["accepted_gate_review_candidate_rows"],
            "parked_ocr_methodology_rows": [row["source_matrix_row_id"] for row in farp["parked_ocr_methodology_rows"]],
            "evidence_only_rows": farp["evidence_only_rows"],
            "blocked_rows": farp["blocked_rows"],
            "page_021_plus_requires_separate_ba": farp["page_021_plus_boundary"]["requires_separate_bounded_authorization"],
        },
        "negative_capability_matrix": {name: False for name in NEGATIVE_CAPABILITIES},
        "verified_inputs": verified_inputs,
    }


def write_summary(packet: dict) -> None:
    lines = [
        "# Gate 1 Fixture Admission Blocker Resolution Prep - G1FABRP-G1-VIRAL-001",
        "",
        "Status: `fixture_admission_blocker_resolution_prep_ready_for_review`",
        "",
        "Purpose: prep only for resolving blockers before any fixture admission.",
        "",
        "## Blockers",
        "",
    ]
    for blocker in packet["blockers"]:
        lines.append(f"- `{blocker['blocker_id']}`: `{blocker['status']}`")
    lines.extend(
        [
            "",
            "## Recommended Sequence",
            "",
        ]
    )
    for step in packet["recommended_sequence"]:
        lines.append(f"- `{step}`")
    lines.extend(
        [
            "",
            "## Boundaries",
            "",
            "- No fixture admission.",
            "- No fixture manifest creation.",
            "- No whole Gate 1 acceptance.",
            "- No source-profile acceptance.",
            "- No page 021+ processing.",
            "- No OCR execution or remediation rerun.",
            "- No source/OCR/render/PDF/raw mutation.",
            "- No translation, proofreading, implementation, or push.",
            "",
        ]
    )
    write_text(OUT_ROOT / "gate_1_fixture_admission_blocker_resolution_prep_summary.md", "\n".join(lines))


def write_report(packet: dict) -> None:
    write_json(
        OUT_ROOT / "gate_1_fixture_admission_blocker_resolution_prep_report.json",
        {
            "packet_id": PACKET_ID,
            "authorization_id": AUTHORIZATION_ID,
            "status": packet["status"],
            "generator_script": SCRIPT_PATH.relative_to(ROOT).as_posix(),
            "generator_script_sha256": sha256_file(SCRIPT_PATH),
            "test_contract": TEST_PATH.relative_to(ROOT).as_posix(),
            "test_contract_sha256": sha256_file(TEST_PATH) if TEST_PATH.exists() else None,
            "blocker_count": len(packet["blockers"]),
            "creates_blocker_resolution": False,
            "admits_fixture": False,
            "accepts_whole_gate_1": False,
            "processes_page_021_plus": False,
            "negative_capability_matrix": packet["negative_capability_matrix"],
        },
    )


def write_manifest() -> None:
    manifest_name = "gate_1_fixture_admission_blocker_resolution_prep_manifest.md"
    lines = [
        "# Gate 1 Fixture Admission Blocker Resolution Prep Manifest - G1FABRP-G1-VIRAL-001",
        "",
        "Status: `fixture_admission_blocker_resolution_prep_ready_for_review`",
        "",
        "Boundary: blocker-resolution prep only; no fixture admission, no fixture manifest, no page 021+, no push, and no whole Gate 1 acceptance.",
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
    verified_inputs, farp, review = verify_inputs()
    if OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    packet = build_packet(verified_inputs, farp, review)
    write_json(OUT_ROOT / "gate_1_fixture_admission_blocker_resolution_prep.json", packet)
    write_summary(packet)
    write_report(packet)
    write_manifest()


if __name__ == "__main__":
    check_authorization()
    build()
