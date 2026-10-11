from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
SRFA_ROOT = TRIAL_ROOT / "source_reconstruction_fixture_admission_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "gate_1_review_packet_G1_VIRAL_001"

AUTHORIZATION_ID = "BA-G1-VIRAL-GATE-1-REVIEW-PACKET-001"
PACKET_ID = "G1RP-G1-VIRAL-001"
SRFA_REPORT_SHA256 = "485ECEAAC7CC1CC3FBE95341ED7A0F5E68345EF59CCC8CEB7F8F57706A541A1C"
SRFA_FIXTURES_SHA256 = "1B9DA0A5BF9E219059065F3C1517B4C0E1265060F578F1C6007E9C2AA1611B9F"
SRFA_SUMMARY_SHA256 = "DC76D7677EE76EFBAF7BCBBF7ED7C0BED38727CC0E9EAB63C3F7F26DF2013949"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def read_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json(path: Path, payload: object) -> None:
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def check_authorization(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Build Gate 1 review packet from admitted source reconstruction fixtures.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("Gate 1 review packet build is fail-closed; pass --execute with exact authorization id")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"Gate 1 review packet build requires {AUTHORIZATION_ID}")


def verify_fixture_admission(srfa: dict[str, object], fixtures_payload: dict[str, object]) -> list[dict[str, object]]:
    if srfa["admission_id"] != "SRFA-G1-VIRAL-001":
        raise SystemExit("unexpected SRFA id")
    if srfa["status"] != "source_reconstruction_fixtures_admitted_not_gate":
        raise SystemExit("unexpected SRFA status")
    if srfa["source_acceptance"] is not True or srfa["qa_acceptance"] is not True:
        raise SystemExit("SRFA source/QA flags are not ready for packet")
    if srfa["fixture_admission"] is not True or srfa["gate_1_advancement"] is not False:
        raise SystemExit("SRFA fixture/Gate flags are unsafe for packet")
    for key in [
        "ocr_executed",
        "pdf_opened_or_parsed",
        "raw_ocr_outputs_modified",
        "translation_authorized",
        "proofreading_authorized",
    ]:
        if srfa[key] is not False:
            raise SystemExit(f"unsafe SRFA boundary flag: {key}")
    if srfa["summary"] != {
        "fixtures": 7,
        "positive_source_text_fixtures": 4,
        "negative_visual_exclusion_fixtures": 3,
        "blocked_fixtures": 0,
        "gate_1_advanced_fixtures": 0,
    }:
        raise SystemExit("unexpected SRFA summary")

    fixtures = fixtures_payload["fixtures"]
    if len(fixtures) != 7:
        raise SystemExit("unexpected fixture count")
    for fixture in fixtures:
        if fixture["fixture_admitted"] is not True:
            raise SystemExit(f"fixture is not admitted: {fixture['fixture_id']}")
        if fixture["qa_acceptance"] is not True:
            raise SystemExit(f"fixture is not QA accepted: {fixture['fixture_id']}")
        if fixture["gate_1_advancement"] is not False:
            raise SystemExit(f"fixture already advanced Gate 1: {fixture['fixture_id']}")
    return fixtures


def packet_items(fixtures: list[dict[str, object]]) -> list[dict[str, object]]:
    items = []
    for fixture in fixtures:
        items.append(
            {
                "packet_item_id": f"G1RP-G1-VIRAL-001-{fixture['fixture_id']}",
                "fixture_id": fixture["fixture_id"],
                "fixture_kind": fixture["fixture_kind"],
                "region_admission_id": fixture["region_admission_id"],
                "page_id": fixture["page_id"],
                "region_id": fixture["region_id"],
                "review_class": fixture["review_class"],
                "expected_behavior": fixture["expected_behavior"],
                "source_text_accepted": fixture["source_text_accepted"],
                "visual_exclusion_accepted": fixture["visual_exclusion_accepted"],
                "qa_acceptance": True,
                "fixture_admission": True,
                "included_for_gate_1_review": True,
                "gate_1_advancement": False,
            }
        )
        if "packet_correction_note" in fixture:
            items[-1]["packet_correction_note"] = fixture["packet_correction_note"]
        if "semantic_heading_hint" in fixture:
            items[-1]["semantic_heading_hint"] = fixture["semantic_heading_hint"]
    return items


def build() -> None:
    srfa_report_path = SRFA_ROOT / "source_reconstruction_fixture_admission_report.json"
    srfa_fixtures_path = SRFA_ROOT / "source_reconstruction_admitted_fixtures.json"
    srfa_summary_path = SRFA_ROOT / "source_reconstruction_fixture_admission_summary.md"
    if sha256_file(srfa_report_path) != SRFA_REPORT_SHA256:
        raise SystemExit("SRFA report hash mismatch")
    if sha256_file(srfa_fixtures_path) != SRFA_FIXTURES_SHA256:
        raise SystemExit("SRFA admitted fixtures hash mismatch")
    if sha256_file(srfa_summary_path) != SRFA_SUMMARY_SHA256:
        raise SystemExit("SRFA summary hash mismatch")

    srfa = read_json(srfa_report_path)
    fixtures_payload = read_json(srfa_fixtures_path)
    fixtures = verify_fixture_admission(srfa, fixtures_payload)
    items = packet_items(fixtures)

    if OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    OUT_ROOT.mkdir(parents=True, exist_ok=True)

    review_packet = {
        "packet_id": PACKET_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "gate_1_review_packet_ready_not_advanced",
        "input_fixture_admission_id": "SRFA-G1-VIRAL-001",
        "input_fixture_admission_report_sha256": SRFA_REPORT_SHA256,
        "input_admitted_fixtures_sha256": SRFA_FIXTURES_SHA256,
        "input_fixture_admission_summary_sha256": SRFA_SUMMARY_SHA256,
        "upstream_qa_report_sha256": srfa["input_qa_report_sha256"],
        "upstream_qa_summary_sha256": srfa["input_qa_summary_sha256"],
        "packet_items": items,
    }
    write_json(OUT_ROOT / "gate_1_review_packet.json", review_packet)

    report = {
        "packet_id": PACKET_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "gate_1_review_packet_ready_not_advanced",
        "input_fixture_admission_id": "SRFA-G1-VIRAL-001",
        "input_fixture_admission_report_sha256": SRFA_REPORT_SHA256,
        "input_admitted_fixtures_sha256": SRFA_FIXTURES_SHA256,
        "input_fixture_admission_summary_sha256": SRFA_SUMMARY_SHA256,
        "generator_script": "scripts/build_gate_1_review_packet.py",
        "generator_script_sha256": sha256_file(Path(__file__).resolve()),
        "test_contract": "tests/test_gate_1_review_packet.py",
        "test_contract_sha256": sha256_file(ROOT / "tests" / "test_gate_1_review_packet.py")
        if (ROOT / "tests" / "test_gate_1_review_packet.py").exists()
        else None,
        "source_acceptance": True,
        "qa_acceptance": True,
        "fixture_admission": True,
        "gate_1_review_packet_ready": True,
        "gate_1_advancement": False,
        "ocr_executed": False,
        "pdf_opened_or_parsed": False,
        "raw_ocr_outputs_modified": False,
        "translation_authorized": False,
        "proofreading_authorized": False,
        "renderer_profile_acceptance": False,
        "implementation_authorized": False,
        "summary": {
            "packet_items": len(items),
            "positive_source_text_items": sum(1 for item in items if item["fixture_kind"] == "positive_source_text"),
            "negative_visual_exclusion_items": sum(
                1 for item in items if item["fixture_kind"] == "negative_visual_exclusion"
            ),
            "blocked_items": 0,
            "gate_1_advanced_items": 0,
        },
        "next_authorization_recommendation": "BA-G1-VIRAL-GATE-1-REVIEW-DECISION-001",
    }
    write_json(OUT_ROOT / "gate_1_review_packet_report.json", report)

    summary_lines = [
        "# Gate 1 Review Packet Summary - G1RP-G1-VIRAL-001",
        "",
        "Status: `gate_1_review_packet_ready_not_advanced`",
        "",
        "Boundary: this packet packages SRFA fixtures for Gate 1 review. It is not Gate 1 advancement, translation, proofreading, renderer/profile acceptance, or implementation.",
        "",
        "## Summary",
        "",
        "- Packet items: `7`",
        "- Positive source-text items: `4`",
        "- Negative visual-exclusion items: `3`",
        "- Blocked items: `0`",
        "- Gate 1 advanced: `false`",
        "",
    ]
    (OUT_ROOT / "gate_1_review_packet_summary.md").write_text("\n".join(summary_lines), encoding="utf-8")

    manifest_lines = [
        "# Gate 1 Review Packet Manifest - G1RP-G1-VIRAL-001",
        "",
        "Status: `gate_1_review_packet_ready_not_advanced`",
        "",
        "Boundary: no OCR, PDF parsing, rendering, raw OCR edits, translation, proofreading, renderer/profile acceptance, implementation, or Gate 1 advancement.",
        "",
        "## Output Hashes",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for path in sorted(OUT_ROOT.rglob("*")):
        if path.is_file() and path.name != "gate_1_review_packet_manifest.md":
            manifest_lines.append(f"| `{path.relative_to(OUT_ROOT).as_posix()}` | `{sha256_file(path)}` |")
    manifest_lines.append("")
    (OUT_ROOT / "gate_1_review_packet_manifest.md").write_text("\n".join(manifest_lines), encoding="utf-8")


if __name__ == "__main__":
    check_authorization()
    build()
