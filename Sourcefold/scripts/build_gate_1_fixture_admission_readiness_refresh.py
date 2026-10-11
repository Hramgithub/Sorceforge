from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "build_gate_1_fixture_admission_readiness_refresh.py"
TEST_PATH = ROOT / "tests" / "test_gate_1_fixture_admission_readiness_refresh.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
STATUS_ROOT = TRIAL_ROOT / "gate_1_status_packet_G1_VIRAL_017"
POLICY_ROOT = TRIAL_ROOT / "gate_1_unsupported_negative_fixture_policy_acceptance_G1_VIRAL_001"
STRATEGY_ROOT = TRIAL_ROOT / "gate_1_fixture_strategy_fit_acceptance_G1_VIRAL_001"
PREVIOUS_READINESS_ROOT = TRIAL_ROOT / "gate_1_fixture_admission_readiness_prep_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "gate_1_fixture_admission_readiness_refresh_G1_VIRAL_001"
LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"

AUTHORIZATION_ID = "BA-G1-VIRAL-FIXTURE-ADMISSION-READINESS-REFRESH-001"
REFRESH_ID = "G1FARR-G1-VIRAL-001"
HUMAN_DECISION = (
    "proceed with fixture_admission_readiness_refresh; no fixture admission, "
    "no fixture manifest, no whole Gate 1 acceptance, no page 021+, no push"
)

INPUT_HASHES = {
    "G1SP-G1-VIRAL-017.packet": (
        STATUS_ROOT / "gate_1_status_packet.json",
        "DA9B421CD8A5BC503FCCEE24F6043FBCEC9F86262AF3E9E9018C460D871E4ED6",
    ),
    "G1SP-G1-VIRAL-017.report": (
        STATUS_ROOT / "gate_1_status_report.json",
        "007F7F1F6FC73FC4F9B9268CB3969F895517D20B054FCC1D787851E4609D2F68",
    ),
    "G1SP-G1-VIRAL-017.summary": (
        STATUS_ROOT / "gate_1_status_summary.md",
        "FF3F3D7F9F3EA0352C95448124821DE2C2255E63DCFEB9D6879A6EA722166CF3",
    ),
    "G1SP-G1-VIRAL-017.manifest": (
        STATUS_ROOT / "gate_1_status_manifest.md",
        "4A7DDDC454034FC8CFC75C184856B66D27B17ECEA0E5E8447C331B07CCD381A9",
    ),
    "G1FARP-G1-VIRAL-001.packet": (
        PREVIOUS_READINESS_ROOT / "gate_1_fixture_admission_readiness_prep.json",
        "A6AB9B1CD40EDAC6D2A83B24306920743D5B6039410B1188FA5D6DB433A52CEC",
    ),
    "G1FARP-G1-VIRAL-001.report": (
        PREVIOUS_READINESS_ROOT / "gate_1_fixture_admission_readiness_prep_report.json",
        "0BBED96C4E0D41054AE1FA8AB1FA27430DD330580DA04A5B74C1EBC39CDE5EC8",
    ),
    "G1FARP-G1-VIRAL-001.summary": (
        PREVIOUS_READINESS_ROOT / "gate_1_fixture_admission_readiness_prep_summary.md",
        "E8962C044123C9ADFA59C58F066C166C5675312D27DBE278FE91D0F30DFF6753",
    ),
    "G1UNFPAR-G1-VIRAL-001.acceptance": (
        POLICY_ROOT / "gate_1_unsupported_negative_fixture_policy_acceptance.json",
        "FD4D704EFE18EEA6BF33C82E6C106AF67268E7AEA5924CD4FFB150A4ACDE408C",
    ),
    "G1UNFPAR-G1-VIRAL-001.report": (
        POLICY_ROOT / "gate_1_unsupported_negative_fixture_policy_acceptance_report.json",
        "9AE4141BC8824BA7B3F494222C2C45C5C32C2151742D5C6B8830EEF09909D232",
    ),
    "G1UNFPAR-G1-VIRAL-001.summary": (
        POLICY_ROOT / "gate_1_unsupported_negative_fixture_policy_acceptance_summary.md",
        "C19E40A907688639C6BE286A149A8DF24CD16AC4F5150F430C7106A3AA874F35",
    ),
    "G1UNFPAR-G1-VIRAL-001.manifest": (
        POLICY_ROOT / "gate_1_unsupported_negative_fixture_policy_acceptance_manifest.md",
        "1A3F8DC8FEBD2721BC0C2FB2330BB12193010BA6866EDD2AC211ECA0E2FCB3B9",
    ),
    "G1FSFAR-G1-VIRAL-001.acceptance": (
        STRATEGY_ROOT / "gate_1_fixture_strategy_fit_acceptance.json",
        "4F6BC8EB37F85256DF62C6F02AC4A1A0FFB081B5D70B5131940B001AFB6C3E7A",
    ),
    "G1FSFAR-G1-VIRAL-001.report": (
        STRATEGY_ROOT / "gate_1_fixture_strategy_fit_acceptance_report.json",
        "27A68FB9EF917BD0D8CEE2FAE51206A965098878241825EA53DDEA6944EE3195",
    ),
    "G1FSFAR-G1-VIRAL-001.summary": (
        STRATEGY_ROOT / "gate_1_fixture_strategy_fit_acceptance_summary.md",
        "37CD1B6EC4499EE8664875B8904FAE0959E28C087DE234676FB6330EC6DED511",
    ),
    "G1FSFAR-G1-VIRAL-001.manifest": (
        STRATEGY_ROOT / "gate_1_fixture_strategy_fit_acceptance_manifest.md",
        "9EF9222F67034E2F6A4D14750A777E82A72C270845BE8C4EBB72158D5108F7A0",
    ),
}

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
    parser = argparse.ArgumentParser(description="Refresh Gate 1 fixture admission readiness.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("Gate 1 fixture admission readiness refresh is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"Gate 1 fixture admission readiness refresh requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("fixture admission readiness refresh requires the exact bounded human decision")


def verify_inputs() -> tuple[dict[str, dict[str, str]], dict, dict, dict, dict]:
    ledger = LEDGER.read_text(encoding="utf-8-sig")
    if f"## {AUTHORIZATION_ID}" not in ledger:
        raise SystemExit(f"{AUTHORIZATION_ID} missing from ledger")

    verified: dict[str, dict[str, str]] = {}
    for key, (path, expected) in INPUT_HASHES.items():
        actual = sha256_file(path)
        if actual != expected:
            raise SystemExit(f"{key} hash mismatch: {actual}")
        verified[key] = {"path": path.relative_to(ROOT).as_posix(), "sha256": actual}

    status_packet = read_json(INPUT_HASHES["G1SP-G1-VIRAL-017.packet"][0])
    previous_readiness = read_json(INPUT_HASHES["G1FARP-G1-VIRAL-001.packet"][0])
    policy_acceptance = read_json(INPUT_HASHES["G1UNFPAR-G1-VIRAL-001.acceptance"][0])
    strategy_acceptance = read_json(INPUT_HASHES["G1FSFAR-G1-VIRAL-001.acceptance"][0])

    if status_packet["status_packet_id"] != "G1SP-G1-VIRAL-017":
        raise SystemExit("unexpected Gate 1 status packet")
    if status_packet["page_021_plus_state"] != "unprocessed_not_authorized":
        raise SystemExit("page 021+ is not blocked")
    if status_packet["whole_gate_1_acceptance"]:
        raise SystemExit("whole Gate 1 is unexpectedly accepted")
    if previous_readiness["packet_id"] != "G1FARP-G1-VIRAL-001":
        raise SystemExit("unexpected previous readiness packet")
    if policy_acceptance["acceptance_id"] != "G1UNFPAR-G1-VIRAL-001":
        raise SystemExit("unexpected unsupported/negative fixture policy acceptance")
    if not policy_acceptance["creates_policy_decision"]:
        raise SystemExit("unsupported/negative fixture policy is not accepted")
    if not policy_acceptance["resolves_unsupported_negative_fixture_policy_blocker"]:
        raise SystemExit("unsupported/negative fixture policy blocker is unresolved")
    if strategy_acceptance["acceptance_id"] != "G1FSFAR-G1-VIRAL-001":
        raise SystemExit("unexpected fixture strategy fit acceptance")
    if not strategy_acceptance["creates_fixture_strategy_fit_decision"]:
        raise SystemExit("fixture strategy fit is not accepted")
    if not strategy_acceptance["resolves_fixture_strategy_fit_blocker"]:
        raise SystemExit("fixture strategy fit blocker is unresolved")
    for payload in (policy_acceptance, strategy_acceptance):
        if payload["admits_fixture"] or payload["creates_fixture_manifest"] or payload["accepts_whole_gate_1"]:
            raise SystemExit("source acceptance is too broad for readiness refresh")
    return verified, status_packet, previous_readiness, policy_acceptance, strategy_acceptance


def build_refresh(
    verified_inputs: dict[str, dict[str, str]],
    status_packet: dict,
    previous_readiness: dict,
    policy_acceptance: dict,
    strategy_acceptance: dict,
) -> dict:
    return {
        "refresh_id": REFRESH_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "fixture_admission_readiness_refresh_recorded",
        "purpose": "fixture_admission_readiness_refresh_only_no_admission",
        "human_decision": HUMAN_DECISION,
        "source_status_packet": status_packet["status_packet_id"],
        "previous_readiness_packet": previous_readiness["packet_id"],
        "source_policy_acceptance": policy_acceptance["acceptance_id"],
        "source_strategy_fit_acceptance": strategy_acceptance["acceptance_id"],
        "page_complete_accepted_pages": status_packet["page_complete_accepted_pages"],
        "page_complete_acceptance_scope": "pages_001_020_individual_page_complete_only",
        "readiness_inputs": {
            "pages_001_020_page_complete_accepted_only": True,
            "unsupported_negative_fixture_policy_decision_accepted": True,
            "fixture_strategy_fit_decision_accepted": True,
            "page_021_plus_unprocessed_not_authorized": True,
        },
        "readiness_rows": [
            {
                "row_id": "positive_fixture_seed_readiness",
                "status": "ready_as_seed_material_for_future_manifest_prep",
                "meaning": "Pages 001-020 may seed future positive fixtures only after separate manifest/admission authorization.",
            },
            {
                "row_id": "negative_fixture_policy_readiness",
                "status": "ready_policy_accepted_negative_fixtures_not_materialized",
                "meaning": "Unsupported/negative fixture policy is accepted, but concrete negative fixture artifacts are still future work.",
            },
            {
                "row_id": "fixture_strategy_fit_readiness",
                "status": "ready_strategy_fit_accepted",
                "meaning": "Fixture strategy fit blocker is resolved for Core 0.1 / Viral-like / page-complete accepted-only evidence.",
            },
            {
                "row_id": "fixture_admission_readiness",
                "status": "not_ready_requires_fixture_manifest_prep_and_admission_decision",
                "meaning": "Readiness is refreshed, but fixture admission itself remains a separate future decision.",
            },
            {
                "row_id": "whole_gate_1_acceptance_readiness",
                "status": "not_ready_requires_future_recheck_after_admission_path",
                "meaning": "Whole Gate 1 cannot be accepted by this refresh and needs its own readiness recheck.",
            },
        ],
        "resolves_fixture_admission_readiness_refresh_blocker": True,
        "resolved_blocker": "fixture_admission_readiness_refresh",
        "admits_fixture": False,
        "creates_fixture_manifest": False,
        "accepts_whole_gate_1": False,
        "accepts_source_profile": False,
        "processes_page_021_plus": False,
        "executes_ocr": False,
        "remaining_blockers": [
            "fixture_manifest_prep",
            "fixture_admission_decision",
            "whole_gate_1_acceptance_readiness_recheck",
            "page_021_plus_separate_bounded_authorization_if_selected",
        ],
        "next_possible_packets": [
            "fixture_manifest_prep",
            "fixture_admission_decision_prep",
            "whole_gate_1_acceptance_readiness_recheck",
        ],
        "negative_capability_matrix": {name: False for name in NEGATIVE_CAPABILITIES},
        "verified_inputs": verified_inputs,
    }


def write_summary(refresh: dict) -> None:
    lines = [
        "# Gate 1 Fixture Admission Readiness Refresh - G1FARR-G1-VIRAL-001",
        "",
        "Status: `fixture_admission_readiness_refresh_recorded`",
        "",
        "Purpose: refresh fixture admission readiness after the accepted unsupported/negative fixture policy and fixture strategy fit decision.",
        "",
        "## Inputs",
        "",
        f"- Source status packet: `{refresh['source_status_packet']}`.",
        f"- Previous readiness packet: `{refresh['previous_readiness_packet']}`.",
        f"- Unsupported/negative fixture policy acceptance: `{refresh['source_policy_acceptance']}`.",
        f"- Fixture strategy fit acceptance: `{refresh['source_strategy_fit_acceptance']}`.",
        "",
        "## Readiness Rows",
        "",
    ]
    for row in refresh["readiness_rows"]:
        lines.append(f"- `{row['row_id']}`: `{row['status']}`")
    lines.extend(
        [
            "",
            "## Boundary",
            "",
            "- Fixture admission readiness refresh blocker resolved: `true`.",
            "- Fixture admission: `false`.",
            "- Fixture manifest creation: `false`.",
            "- Whole Gate 1 acceptance: `false`.",
            "- Source-profile acceptance: `false`.",
            "- Page 021+ processing: `false`.",
            "- OCR/remediation/render/PDF/raw mutation: `false`.",
            "- Translation/proofreading/implementation/push: `false`.",
            "",
            "## Remaining Blockers",
            "",
        ]
    )
    for blocker in refresh["remaining_blockers"]:
        lines.append(f"- `{blocker}`")
    lines.append("")
    write_text(OUT_ROOT / "gate_1_fixture_admission_readiness_refresh_summary.md", "\n".join(lines))


def write_report(refresh: dict) -> None:
    write_json(
        OUT_ROOT / "gate_1_fixture_admission_readiness_refresh_report.json",
        {
            "refresh_id": REFRESH_ID,
            "authorization_id": AUTHORIZATION_ID,
            "status": refresh["status"],
            "generator_script": SCRIPT_PATH.relative_to(ROOT).as_posix(),
            "generator_script_sha256": sha256_file(SCRIPT_PATH),
            "test_contract": TEST_PATH.relative_to(ROOT).as_posix(),
            "test_contract_sha256": sha256_file(TEST_PATH) if TEST_PATH.exists() else None,
            "resolves_fixture_admission_readiness_refresh_blocker": True,
            "admits_fixture": False,
            "creates_fixture_manifest": False,
            "accepts_whole_gate_1": False,
            "accepts_source_profile": False,
            "processes_page_021_plus": False,
            "executes_ocr": False,
            "negative_capability_matrix": refresh["negative_capability_matrix"],
            "remaining_blockers": refresh["remaining_blockers"],
        },
    )


def write_manifest() -> None:
    manifest_name = "gate_1_fixture_admission_readiness_refresh_manifest.md"
    lines = [
        "# Gate 1 Fixture Admission Readiness Refresh Manifest - G1FARR-G1-VIRAL-001",
        "",
        "Status: `fixture_admission_readiness_refresh_recorded`",
        "",
        "Boundary: fixture admission readiness refresh only; no fixture admission, no fixture manifest, no page 021+, no whole Gate 1 acceptance, and no push.",
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
    verified_inputs, status_packet, previous_readiness, policy_acceptance, strategy_acceptance = verify_inputs()
    if OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    refresh = build_refresh(verified_inputs, status_packet, previous_readiness, policy_acceptance, strategy_acceptance)
    write_json(OUT_ROOT / "gate_1_fixture_admission_readiness_refresh.json", refresh)
    write_summary(refresh)
    write_report(refresh)
    write_manifest()


if __name__ == "__main__":
    check_authorization()
    build()
