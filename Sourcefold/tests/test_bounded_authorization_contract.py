import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.bounded_authorization_contract import (  # noqa: E402
    AGGRESSIVE_BATCH_AUTHORIZATION_SCHEMA_VERSION,
    BOUNDED_AUTHORIZATION_SCHEMA_VERSION,
    assert_aggressive_page_builder_uses_authorization_preflight,
    materialize_aggressive_batch_authorization,
    validate_bounded_authorization,
)


def test_bounded_authorization_accepts_ledger_bound_scope():
    result = validate_bounded_authorization(
        artifact={
            "authorization_id": "BA-G1-VIRAL-PAGE-010-TEXT-EXTRACTION-001",
            "scope": "page_010_text_extraction_review_only_no_semantic_map_no_pcrp_no_acceptance",
        },
        expected_authorization_id="BA-G1-VIRAL-PAGE-010-TEXT-EXTRACTION-001",
        ledger_text="## BA-G1-VIRAL-PAGE-010-TEXT-EXTRACTION-001\n",
        allowed_scope_markers=["text_extraction_review_only"],
        created_capabilities={"semantic_map_created": False, "pcrp_created": False, "page_complete_acceptance_created": False},
    )

    assert result["schema_version"] == BOUNDED_AUTHORIZATION_SCHEMA_VERSION
    assert result["status"] == "passed"


def test_bounded_authorization_blocks_wrong_id_missing_ledger_scope_and_leakage():
    result = validate_bounded_authorization(
        artifact={"authorization_id": "WRONG", "scope": "page_complete_acceptance"},
        expected_authorization_id="BA-G1-VIRAL-PAGE-010-TEXT-EXTRACTION-001",
        ledger_text="",
        allowed_scope_markers=["text_extraction_review_only"],
        created_capabilities={"pcrp_created": True, "page_complete_acceptance_created": True},
    )

    finding_ids = {finding["finding_id"] for finding in result["findings"]}
    assert result["status"] == "blocked"
    assert "bounded_authorization_id_mismatch" in finding_ids
    assert "bounded_authorization_missing_from_ledger" in finding_ids
    assert "bounded_authorization_scope_not_allowed" in finding_ids
    assert "bounded_authorization_leaked_authority" in finding_ids


def test_aggressive_batch_authorization_preflight_materializes_idempotently(tmp_path):
    ledger = tmp_path / "bounded_trial_authorizations.md"
    artifact = materialize_aggressive_batch_authorization(
        ledger_path=ledger,
        authorization_id="BA-G1-VIRAL-PAGE-015-AGGRESSIVE-BATCH-001",
        page="015",
        lane_id="P015BATCH-G1-VIRAL-001",
        authority="Bogdan Telegram message: start page 015 aggressive batch",
        exact_action=["Create page 015 aggressive delegated-review batch artifacts."],
        admitted_inputs=[
            {"name": "post_p014_status_route_packet", "sha256": "A" * 64},
            {"name": "page_015_image", "sha256": "B" * 64},
        ],
        allowed_outputs=[
            "scripts/build_page_015_aggressive_batch.py",
            "fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_015_triage_G1_VIRAL_001/*",
        ],
        limits=[
            "Do not process page 016 or later.",
            "Do not accept whole Gate 1, admit fixtures, mutate source/OCR/render/PDF/raw, translate, proofread, implement, push, or create final batch review.",
        ],
    )
    materialize_aggressive_batch_authorization(
        ledger_path=ledger,
        authorization_id="BA-G1-VIRAL-PAGE-015-AGGRESSIVE-BATCH-001",
        page="015",
        lane_id="P015BATCH-G1-VIRAL-001",
        authority="Bogdan Telegram message: start page 015 aggressive batch",
        exact_action=["Create page 015 aggressive delegated-review batch artifacts."],
        admitted_inputs=[
            {"name": "post_p014_status_route_packet", "sha256": "A" * 64},
            {"name": "page_015_image", "sha256": "B" * 64},
        ],
        allowed_outputs=["scripts/build_page_015_aggressive_batch.py"],
        limits=["Do not process page 016 or later."],
    )

    ledger_text = ledger.read_text(encoding="utf-8")
    assert artifact["schema_version"] == AGGRESSIVE_BATCH_AUTHORIZATION_SCHEMA_VERSION
    assert artifact["guardrails"]["whole_gate_1_acceptance"] is False
    assert artifact["guardrails"]["page_016_plus_processing"] is False
    assert ledger_text.count("## BA-G1-VIRAL-PAGE-015-AGGRESSIVE-BATCH-001") == 1
    assert "P015BATCH-G1-VIRAL-001" in ledger_text
    assert "page_015_image" in ledger_text
    assert "Do not create final human batch-review acceptance" in ledger_text


def test_aggressive_batch_authorization_preflight_rejects_mismatched_page_or_lane(tmp_path):
    kwargs = {
        "ledger_path": tmp_path / "bounded_trial_authorizations.md",
        "authorization_id": "BA-G1-VIRAL-PAGE-015-AGGRESSIVE-BATCH-001",
        "page": "015",
        "lane_id": "P014BATCH-G1-VIRAL-001",
        "authority": "Bogdan Telegram message: start page 015 aggressive batch",
        "exact_action": ["Create page 015 aggressive delegated-review batch artifacts."],
        "admitted_inputs": [{"name": "page_015_image", "sha256": "B" * 64}],
        "allowed_outputs": ["scripts/build_page_015_aggressive_batch.py"],
        "limits": ["Do not process page 016 or later."],
    }
    try:
        materialize_aggressive_batch_authorization(**kwargs)
    except ValueError as exc:
        assert "P015BATCH" in str(exc)
    else:
        raise AssertionError("expected mismatched lane to fail closed")


def test_aggressive_batch_builder_scanner_requires_authorization_preflight(tmp_path):
    legacy = tmp_path / "build_page_015_aggressive_batch.py"
    legacy.write_text("def build():\n    pass\n", encoding="utf-8")
    try:
        assert_aggressive_page_builder_uses_authorization_preflight(legacy)
    except ValueError as exc:
        assert "authorization preflight" in str(exc)
    else:
        raise AssertionError("expected missing preflight to fail closed")

    current = tmp_path / "build_page_015_aggressive_batch.py"
    current.write_text(
        """
from bounded_authorization_contract import materialize_aggressive_batch_authorization


def build():
    materialize_aggressive_batch_authorization(
        authority="aggressive_batch_authorization_preflight",
    )
""".lstrip(),
        encoding="utf-8",
    )
    assert_aggressive_page_builder_uses_authorization_preflight(current)


def test_all_aggressive_batch_builders_use_authorization_preflight():
    scripts_root = ROOT / "scripts"
    builders = sorted(scripts_root.glob("build_page_*_aggressive_batch.py"))

    assert builders, "expected at least one aggressive page builder"
    for builder in builders:
        assert_aggressive_page_builder_uses_authorization_preflight(builder)
