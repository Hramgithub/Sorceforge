from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path

from display_structure_labels import normalize_draft_structure_lines


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "build_structure_display_migration.py"
TEST_PATH = ROOT / "tests" / "test_structure_display_migration.py"
AUTHORIZATION_LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"

AUTHORIZATION_ID = "BA-G1-VIRAL-STRUCTURE-DISPLAY-NORMALIZATION-001"
PACKAGE_ID = "SDN-G1-VIRAL-001"
OUT_ROOT = TRIAL_ROOT / "structure_display_normalization_G1_VIRAL_001"
NORMALIZED_ROOT = OUT_ROOT / "normalized_human_facing_packets"

SOURCE_PACKETS = [
    (
        TRIAL_ROOT
        / "source_reconstruction_p002_completion_and_next_review_G1_VIRAL_001"
        / "next_review_packet_for_bogdan.md",
        "p002_next_review_packet.md",
    ),
    (
        TRIAL_ROOT
        / "page_complete_review_p003_G1_VIRAL_001"
        / "review_assets"
        / "page_003_ocr_block_text.md",
        "p003_ocr_block_text.md",
    ),
    (
        TRIAL_ROOT
        / "source_reconstruction_next_slice_G1_VIRAL_004"
        / "human_review_packet.md",
        "p004_human_review_packet.md",
    ),
]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def write_json(path: Path, payload: object) -> None:
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8", newline="\n")


def check_authorization(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build human-facing structure display normalization package.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("structure display normalization is fail-closed; pass --execute with exact authorization id")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"structure display normalization requires {AUTHORIZATION_ID}")
    return args


def verify_authorization_ledger() -> None:
    ledger = AUTHORIZATION_LEDGER.read_text(encoding="utf-8-sig")
    if f"## {AUTHORIZATION_ID}" not in ledger:
        raise SystemExit(f"{AUTHORIZATION_ID} is missing from bounded trial authorization ledger")


def normalize_packet(source: Path, normalized_name: str) -> dict[str, str | int | bool]:
    source_text = source.read_text(encoding="utf-8-sig")
    normalized = normalize_draft_structure_lines(source_text)
    dest = NORMALIZED_ROOT / normalized_name
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(normalized, encoding="utf-8", newline="\n")
    return {
        "source_path": source.relative_to(ROOT).as_posix(),
        "normalized_path": dest.relative_to(ROOT).as_posix(),
        "source_sha256": sha256_file(source),
        "normalized_sha256": sha256_file(dest),
        "source_mutated": False,
        "normalizations_applied": source_text != normalized,
        "text_body_occurrences": normalized.count("/ `text_body`"),
    }


def build_report(normalized_packets: list[dict[str, str | int | bool]]) -> dict[str, object]:
    return {
        "package_id": PACKAGE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "human_facing_structure_display_normalized",
        "scope": "display_only_normalized_copies_for_prior_and_future_review_packets",
        "generator": {
            "script": SCRIPT_PATH.relative_to(ROOT).as_posix(),
            "script_sha256": sha256_file(SCRIPT_PATH),
            "test": TEST_PATH.relative_to(ROOT).as_posix(),
            "test_sha256": sha256_file(TEST_PATH) if TEST_PATH.exists() else None,
        },
        "display_rule": {
            "rule_id": "SDR-G1-VIRAL-TEXT-BODY-001",
            "when": "human-facing Draft structure/semantics line has a body/text-only semantic role and raw heading_level none",
            "display_as": "text_body",
            "raw_predecessor_evidence_mutated": False,
            "future_display_aware_generators_use_helper": "scripts/display_structure_labels.py",
            "updated_generators": [
                "scripts/build_p002_completion_and_next_review.py",
                "scripts/build_source_reconstruction_next_slice_004.py",
                "scripts/build_page_004_context_decision.py",
            ],
        },
        "normalized_packets": normalized_packets,
        "guardrails": {
            "source_acceptance_created_or_mutated": False,
            "page_complete_acceptance_created": False,
            "accepted_pages_as_complete": [],
            "whole_gate_1_acceptance_created": False,
            "fixture_admission": False,
            "ocr_executed": False,
            "pdf_opened_or_parsed": False,
            "pdf_text_layer_used": False,
            "render_executed": False,
            "raw_artifacts_modified": False,
            "translation_authorized": False,
            "proofreading_authorized": False,
            "renderer_profile_acceptance": False,
            "implementation_authorized": False,
            "push_authorized": False,
        },
    }


def build_summary(report: dict[str, object]) -> str:
    packet_count = len(report["normalized_packets"])  # type: ignore[arg-type]
    return "\n".join(
        [
            "# Structure Display Normalization Summary",
            "",
            f"Package: `{report['package_id']}`",
            "",
            f"- Normalized human-facing packet copies: {packet_count}.",
            "- Body/text-only `Draft structure/semantics` lines display `text_body` instead of ambiguous `none`.",
            "- Original predecessor evidence files are not mutated.",
            "- Future display-aware generators use the same display helper; historical predecessor artifacts are not regenerated in this package.",
            "- No source acceptance, page-complete acceptance, whole Gate acceptance, fixture admission, OCR, render, PDF parsing/text-layer extraction, raw mutation, translation, proofreading, implementation, or push was created.",
            "",
        ]
    )


def build_manifest(package_id: str, out_root: Path) -> str:
    lines = [
        "# Structure Display Normalization Manifest",
        "",
        f"Package: `{package_id}`",
        "",
        "## Output Hashes",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for path in sorted(out_root.rglob("*")):
        if path.is_file() and path.name != "structure_display_normalization_manifest.md":
            lines.append(f"| `{path.relative_to(out_root).as_posix()}` | `{sha256_file(path)}` |")
    lines.append("")
    return "\n".join(lines)


def build() -> None:
    verify_authorization_ledger()
    if OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    normalized_packets = [normalize_packet(path, normalized_name) for path, normalized_name in SOURCE_PACKETS]
    report = build_report(normalized_packets)
    write_json(OUT_ROOT / "structure_display_normalization_report.json", report)
    (OUT_ROOT / "structure_display_normalization_summary.md").write_text(build_summary(report), encoding="utf-8", newline="\n")
    (OUT_ROOT / "structure_display_normalization_manifest.md").write_text(
        build_manifest(report["package_id"], OUT_ROOT), encoding="utf-8", newline="\n"
    )


if __name__ == "__main__":
    parsed = check_authorization()
    build()
