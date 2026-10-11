from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "accept_page_012_aggressive_batch_review.py"
TEST_PATH = ROOT / "tests" / "test_page_012_aggressive_batch_final_review.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"

AUTHORIZATION_ID = "BA-G1-VIRAL-PAGE-012-AGGRESSIVE-BATCH-001"
REVIEW_ID = "P012BATCHREV-G1-VIRAL-001"
HUMAN_DECISION = "p012 aggressive batch ok"

BATCH_REPORT = TRIAL_ROOT / "page_012_aggressive_batch_G1_VIRAL_001" / "page_012_aggressive_batch_report.json"
STATUS_PACKET = TRIAL_ROOT / "gate_1_status_packet_G1_VIRAL_007" / "gate_1_status_packet.json"
OUTPUT_ROOT = TRIAL_ROOT / "page_012_aggressive_batch_final_review_G1_VIRAL_001"

BATCH_REPORT_SHA256 = "6D9E6846A4F3E1189C2B59ACC56CD67406CDE60C10DE14B05861FD1EA16B219A"
STATUS_PACKET_SHA256 = "37651668FD8FF162DC6205A7EB244589548C78789BBB0083E2E5FCD85C224E9B"


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
    parser = argparse.ArgumentParser(description="Accept page 012 aggressive batch final human review.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("page 012 aggressive batch final review is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"page 012 aggressive batch final review requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit(f"page 012 aggressive batch final review requires decision: {HUMAN_DECISION}")


def verify_predecessors() -> tuple[dict, dict]:
    if sha256_file(BATCH_REPORT) != BATCH_REPORT_SHA256:
        raise SystemExit("P012 aggressive batch report hash mismatch")
    if sha256_file(STATUS_PACKET) != STATUS_PACKET_SHA256:
        raise SystemExit("G1SP-G1-VIRAL-007 status packet hash mismatch")

    batch = read_json(BATCH_REPORT)
    status = read_json(STATUS_PACKET)
    if batch["status"] != "ready_for_bogdan_final_batch_review":
        raise SystemExit("P012 aggressive batch is not ready for final review")
    if status["status"] != "gate_1_status_route_packet_ready_for_final_human_batch_review":
        raise SystemExit("G1SP-G1-VIRAL-007 is not ready for final batch review")
    return batch, status


def guardrails() -> dict[str, bool]:
    return {
        "whole_gate_1_acceptance": False,
        "fixture_admission": False,
        "source_acceptance_mutation": False,
        "ocr_execution": False,
        "render_execution": False,
        "pdf_parsing_or_text_layer_extraction": False,
        "raw_mutation": False,
        "translation": False,
        "proofreading": False,
        "renderer_profile_acceptance": False,
        "implementation": False,
        "push": False,
        "page_013_processing": False,
    }


def write_manifest() -> None:
    lines = ["# Page 012 Aggressive Batch Final Review Manifest", "", "| Output | SHA-256 |", "|---|---|"]
    for path in sorted(OUTPUT_ROOT.rglob("*")):
        if path.is_file() and path.name != "page_012_aggressive_batch_final_review_manifest.md":
            lines.append(f"| `{path.relative_to(OUTPUT_ROOT).as_posix()}` | `{sha256_file(path)}` |")
    lines.append("")
    write_text(OUTPUT_ROOT / "page_012_aggressive_batch_final_review_manifest.md", "\n".join(lines))


def build() -> None:
    batch, status = verify_predecessors()
    if OUTPUT_ROOT.exists():
        shutil.rmtree(OUTPUT_ROOT)
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)

    record = {
        "review_id": REVIEW_ID,
        "authorization_id": AUTHORIZATION_ID,
        "decision": HUMAN_DECISION,
        "status": "page_012_aggressive_batch_final_human_review_accepted",
        "human_review_scope": "final_bundle_and_post_p012_status_only",
        "internal_stage_human_review_state": "human_review_skipped_by_explicit_authorization",
        "predecessors": [
            {"package_id": batch["package_id"], "sha256": BATCH_REPORT_SHA256},
            {"status_packet_id": status["status_packet_id"], "sha256": STATUS_PACKET_SHA256},
        ],
        "accepted_page_complete_pages_current": status["page_complete_accepted_pages"],
        "remaining_page_complete_pages_unstarted": status["remaining_page_complete_pages_unstarted"],
        "recommended_next_candidate": status["recommended_next_candidate"],
        "guardrails": guardrails(),
    }
    write_json(OUTPUT_ROOT / "page_012_aggressive_batch_final_review_report.json", record)
    write_text(
        OUTPUT_ROOT / "page_012_aggressive_batch_final_review_summary.md",
        "# Page 012 Aggressive Batch Final Review - P012BATCHREV-G1-VIRAL-001\n\n"
        "Bogdan accepted the final page 012 aggressive batch review target with `p012 aggressive batch ok`.\n\n"
        "This accepts the final bundle plus `G1SP-G1-VIRAL-007` only. It does not rewrite internal P012TR/P012TXT/P012SEM/PCRP/P012PCA stages as direct human-approved stages.\n\n"
        "Pages `001-012` are page-complete accepted only. Pages `013-020` remain unstarted. Page 013 triage/readiness remains a recommended next candidate, not authorized by this record.\n",
    )
    write_manifest()


if __name__ == "__main__":
    check_authorization()
    build()
