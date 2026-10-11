from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"

AUTHORIZATION_ID = "BA-G1-VIRAL-PAGE-015-AGGRESSIVE-BATCH-001"
REVIEW_ID = "P015BATCHREV-G1-VIRAL-001"
HUMAN_DECISION = "p015 aggressive batch ok"

BATCH_REPORT = TRIAL_ROOT / "page_015_aggressive_batch_G1_VIRAL_001" / "page_015_aggressive_batch_report.json"
STATUS_PACKET = TRIAL_ROOT / "gate_1_status_packet_G1_VIRAL_010" / "gate_1_status_packet.json"
OUTPUT_ROOT = TRIAL_ROOT / "page_015_aggressive_batch_final_review_G1_VIRAL_001"

BATCH_REPORT_SHA256 = "B3FFBC67FDB16DFFF11D76D253697F80378D9753D195C6275A7A095FC4990550"
STATUS_PACKET_SHA256 = "D340D6D2FEAF561B60EC6ED9329104D5700D262C55AA8DB03EACBDA3B17D05D3"


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
    parser = argparse.ArgumentParser(description="Accept page 015 aggressive batch final human review.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("page 015 aggressive batch final review is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"page 015 aggressive batch final review requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit(f"page 015 aggressive batch final review requires decision: {HUMAN_DECISION}")


def verify_predecessors() -> tuple[dict, dict]:
    if sha256_file(BATCH_REPORT) != BATCH_REPORT_SHA256:
        raise SystemExit("P015 aggressive batch report hash mismatch")
    if sha256_file(STATUS_PACKET) != STATUS_PACKET_SHA256:
        raise SystemExit("G1SP-G1-VIRAL-010 status packet hash mismatch")

    batch = read_json(BATCH_REPORT)
    status = read_json(STATUS_PACKET)
    if batch["status"] != "ready_for_bogdan_final_batch_review":
        raise SystemExit("P015 aggressive batch is not ready for final review")
    if status["status"] != "gate_1_status_route_packet_ready_for_final_human_batch_review":
        raise SystemExit("G1SP-G1-VIRAL-010 is not ready for final batch review")
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
        "page_016_plus_processing": False,
    }


def write_manifest() -> None:
    lines = ["# Page 015 Aggressive Batch Final Review Manifest", "", "| Output | SHA-256 |", "|---|---|"]
    for path in sorted(OUTPUT_ROOT.rglob("*")):
        if path.is_file() and path.name != "page_015_aggressive_batch_final_review_manifest.md":
            lines.append(f"| `{path.relative_to(OUTPUT_ROOT).as_posix()}` | `{sha256_file(path)}` |")
    lines.append("")
    write_text(OUTPUT_ROOT / "page_015_aggressive_batch_final_review_manifest.md", "\n".join(lines))


def build() -> None:
    batch, status = verify_predecessors()
    if OUTPUT_ROOT.exists():
        shutil.rmtree(OUTPUT_ROOT)
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)

    record = {
        "review_id": REVIEW_ID,
        "authorization_id": AUTHORIZATION_ID,
        "decision": HUMAN_DECISION,
        "status": "page_015_aggressive_batch_final_human_review_accepted",
        "human_review_scope": "final_bundle_and_post_p015_status_only",
        "internal_stage_human_review_state": "human_review_skipped_by_explicit_authorization",
        "predecessors": [
            {"package_id": batch["package_id"], "sha256": BATCH_REPORT_SHA256},
            {"status_packet_id": status["status_packet_id"], "sha256": STATUS_PACKET_SHA256},
        ],
        "accepted_page_complete_pages_current": status["page_complete_accepted_pages"],
        "remaining_page_complete_pages_unstarted": status["remaining_page_complete_pages_unstarted"],
        "recommended_next_candidate": status["recommended_next_candidate"],
        "continuation": batch["continuation"],
        "guardrails": guardrails(),
    }
    write_json(OUTPUT_ROOT / "page_015_aggressive_batch_final_review_report.json", record)
    write_text(
        OUTPUT_ROOT / "page_015_aggressive_batch_final_review_summary.md",
        "# Page 015 Aggressive Batch Final Review - P015BATCHREV-G1-VIRAL-001\n\n"
        "Bogdan accepted the final page 015 aggressive batch review target with `p015 aggressive batch ok`.\n\n"
        "This accepts the final bundle plus `G1SP-G1-VIRAL-010` only. It does not rewrite internal P015TR/P015TXT/P015SEM/PCRP/P015PCA stages as direct human-approved stages.\n\n"
        "Pages `001-015` are page-complete accepted only. Pages `016-020` remain unstarted. Page 016 triage/readiness remains a recommended next candidate, not authorized by this record.\n",
    )
    write_manifest()


if __name__ == "__main__":
    check_authorization()
    build()
