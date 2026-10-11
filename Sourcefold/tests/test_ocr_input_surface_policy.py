import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.ocr_input_surface_policy import (  # noqa: E402
    OCR_INPUT_SURFACE_POLICY_SCHEMA_VERSION,
    route_ocr_input_surface,
    validate_ocr_input_surface,
)

OVERVIEW_001_020_REPORT = (
    ROOT
    / "fixtures"
    / "candidate_inputs"
    / "viral"
    / "render_trials"
    / "RT-G1-VIRAL-RENDER-001"
    / "core_0_1_text_extraction_overview_replay_001_020_trim_mask_psm4_G1_VIRAL_001"
    / "overview_replay_report.json"
)


def artifact(**overrides):
    base = {"path": "fixtures/static/page_018.png", "sha256": "abc123", "hash_status": "matched"}
    base.update(overrides)
    return base


def ocr_candidate_surface(page_id="P010", **overrides):
    base = {
        "surface_class": "ocr_candidate_crop",
        "artifact_role": "OCR-candidate",
        "ocr_allowed": True,
        "source_artifact": artifact(),
        "page_id": page_id,
        "regions": [{"box_px": [10, 20, 300, 400]}],
        "preprocessing_profile": "trim_mask_psm4",
        "ocr_engine_profile": "tesseract_psm4",
        "allowed_purpose": "candidate_scoring_evidence",
        "reference_policy": "scorer_only_after_hash",
    }
    base.update(overrides)
    return base


def full_page_surface(page_id="P018", **overrides):
    base = ocr_candidate_surface(page_id=page_id)
    base.update(
        {
            "surface_class": "full_page_region",
            "artifact_role": "full-page-region",
            "preprocessing_profile": "expanded_overlap_columns_psm4",
            "authorization": {
                "full_page_region_authorization_id": "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-FULL-PAGE-GEOMETRY-P018-P017-001",
                "page_family": "two_column_tight_page",
                "region_policy": "full_page_derived_page_space_regions",
                "negative_reason_not_baseline": "high_recall_low_sequence_similarity_from_crop_input",
            },
        }
    )
    base.update(overrides)
    return base


def test_ocr_candidate_baseline_can_pass_without_full_page_routing():
    result = route_ocr_input_surface(
        surface=ocr_candidate_surface("P010"),
        metrics={"sequence_similarity_ratio": 0.998867, "token_recall": 0.995825},
    )

    assert result["schema_version"] == OCR_INPUT_SURFACE_POLICY_SCHEMA_VERSION
    assert result["route_decision"] == "baseline_ok"
    assert result["acceptance_effect"] == "none"
    assert result["policy_promotion_effect"] == "none"


def test_p009_p010_p015_do_not_auto_route_full_page_for_imperfect_baseline():
    for page_id in ("P009", "P010", "P015"):
        result = route_ocr_input_surface(
            surface=ocr_candidate_surface(page_id),
            metrics={"sequence_similarity_ratio": 0.9969, "token_recall": 0.9929},
        )

        assert result["route_decision"] == "park_candidate_policy"


def test_high_recall_low_similarity_geometry_failure_routes_to_probe_requirement():
    result = route_ocr_input_surface(
        surface=ocr_candidate_surface("P018"),
        metrics={"sequence_similarity_ratio": 0.81659, "token_recall": 0.993},
        diagnostic_flags=["text_near_crop_boundary", "column_order_drift"],
    )

    assert result["route_decision"] == "geometry_probe_required"
    assert result["status"] == "blocked"


def test_full_page_region_requires_explicit_authorization():
    result = route_ocr_input_surface(
        surface=full_page_surface(authorization=None),
        metrics={"sequence_similarity_ratio": 0.999466, "token_recall": 0.996067},
    )

    assert result["route_decision"] == "blocked_unsafe_surface"
    assert any(finding["finding_id"] == "full_page_region_missing_authorization" for finding in result["findings"])


def test_full_page_region_candidate_is_review_ready_but_not_accepted():
    result = route_ocr_input_surface(
        surface=full_page_surface(),
        metrics={"sequence_similarity_ratio": 0.999466, "token_recall": 0.996067},
    )

    assert result["route_decision"] == "candidate_policy_ready_for_review"
    assert result["acceptance_effect"] == "none"
    assert result["policy_promotion_effect"] == "none"
    control = result["observed_control_measurement_evaluation"]
    assert control["sequence_similarity_delta"] == 0
    assert control["token_recall_delta"] == 0
    assert control["auto_pass"] is False
    assert control["auto_accept"] is False


def test_p018_measurement_is_not_a_hidden_hard_threshold():
    below = route_ocr_input_surface(
        surface=full_page_surface(page_id="P017", preprocessing_profile="bright_title_body_psm7_4_4"),
        metrics={"sequence_similarity_ratio": 0.99923, "token_recall": 0.997859},
    )
    above = route_ocr_input_surface(
        surface=full_page_surface(),
        metrics={"sequence_similarity_ratio": 0.9999, "token_recall": 0.999},
    )

    assert below["route_decision"] == "candidate_policy_ready_for_review"
    assert above["route_decision"] == "candidate_policy_ready_for_review"
    for result in (below, above):
        control = result["observed_control_measurement_evaluation"]
        assert control["auto_pass"] is False
        assert control["auto_fail"] is False
        assert control["auto_promote"] is False
        assert control["auto_accept"] is False


def test_review_and_text_evidence_crops_are_smoke_only_and_non_promotable():
    for surface_class in ("review_crop", "text_evidence_crop"):
        surface = ocr_candidate_surface(
            surface_class=surface_class,
            artifact_role="human-review",
            ocr_allowed=False,
            allowed_purpose="smoke_non_promotable",
        )

        result = route_ocr_input_surface(
            surface=surface,
            metrics={"sequence_similarity_ratio": 1.0, "token_recall": 1.0},
        )

        assert result["route_decision"] == "smoke_non_promotable"
        assert result["policy_promotion_effect"] == "none"
        assert result["acceptance_effect"] == "none"


def test_review_crop_cannot_be_promoted_or_marked_ocr_safe_by_default():
    result = validate_ocr_input_surface(
        ocr_candidate_surface(
            surface_class="review_crop",
            artifact_role="human-review",
            ocr_allowed=True,
            allowed_purpose="candidate_policy",
        )
    )

    finding_ids = {finding["finding_id"] for finding in result["findings"]}
    assert result["status"] == "blocked"
    assert "review_surface_ocr_allowed_must_default_false" in finding_ids
    assert "review_surface_not_promotable" in finding_ids


def test_fail_closed_negative_fixtures():
    cases = [
        ocr_candidate_surface(surface_class="unknown"),
        ocr_candidate_surface(source_artifact=artifact(sha256="")),
        ocr_candidate_surface(source_artifact=artifact(hash_status="mismatch")),
        ocr_candidate_surface(allowed_purpose="acceptance_evidence"),
        ocr_candidate_surface(reference_loaded_before_candidate_hash=True),
        ocr_candidate_surface(page_id="P021"),
        ocr_candidate_surface(tesseract_invoked=True),
        ocr_candidate_surface(render_invoked=True),
        ocr_candidate_surface(pdf_parsed=True),
        ocr_candidate_surface(pdf_text_layer_read=True),
        ocr_candidate_surface(non_temp_artifact_write=True),
    ]

    for surface in cases:
        result = route_ocr_input_surface(
            surface=surface,
            metrics={"sequence_similarity_ratio": 1.0, "token_recall": 1.0},
        )
        assert result["route_decision"] == "blocked_unsafe_surface"


def test_partial_artifacts_are_quarantined_even_when_surface_is_otherwise_valid():
    result = route_ocr_input_surface(
        surface=ocr_candidate_surface(),
        metrics={"sequence_similarity_ratio": 0.999, "token_recall": 0.999},
        scoring_report_complete=False,
    )

    assert result["route_decision"] == "blocked_incomplete_artifacts"
    assert any(finding["finding_id"] == "partial_artifacts_quarantined" for finding in result["findings"])


def test_references_must_not_load_before_candidate_hash_is_sealed():
    result = route_ocr_input_surface(
        surface=ocr_candidate_surface(),
        metrics={"sequence_similarity_ratio": 0.999, "token_recall": 0.999},
        candidate_text_hash_sealed=False,
    )

    assert result["route_decision"] == "blocked_unsafe_surface"
    assert any(finding["finding_id"] == "candidate_hash_not_sealed" for finding in result["findings"])


def test_static_overview_001_020_routes_existing_metrics_without_running_ocr():
    report = json.loads(OVERVIEW_001_020_REPORT.read_text(encoding="utf-8"))
    decisions: dict[str, str] = {}

    for item in report["page_results"]:
        page_id = f"P{item['page']}"
        if item["status"] != "run_completed":
            decisions[item["page"]] = "not_run_ineligible"
            continue

        weak_flags = set(item.get("weak_flags", []))
        diagnostic_flags = []
        if "weak_similarity" in weak_flags:
            diagnostic_flags.append("column_order_drift")
        if "weak_token_recall" in weak_flags:
            diagnostic_flags.append("text_near_crop_boundary")

        routed = route_ocr_input_surface(
            surface=ocr_candidate_surface(
                page_id=page_id,
                source_artifact={
                    "path": item["review_dir"],
                    "sha256": item["candidate_text_sha256"],
                    "hash_status": "matched",
                },
            ),
            metrics=item["metrics"],
            diagnostic_flags=diagnostic_flags,
        )
        decisions[item["page"]] = routed["route_decision"]

    assert {page for page, decision in decisions.items() if decision == "not_run_ineligible"} == {
        "001",
        "002",
        "003",
        "004",
        "005",
        "006",
        "007",
        "008",
    }
    assert {page for page, decision in decisions.items() if decision == "baseline_ok"} == {
        "009",
        "010",
        "011",
        "015",
    }
    assert {"017", "018"}.issubset(
        {page for page, decision in decisions.items() if decision == "geometry_probe_required"}
    )
