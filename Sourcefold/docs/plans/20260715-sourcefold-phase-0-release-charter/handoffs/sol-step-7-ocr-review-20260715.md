# Sol Step 7 OCR Benchmark Review
Verdict: NOT OK
Blocking findings:
- PDF text-layer containment is incomplete. The draft correctly says text-layer content/order is non-canonical and cannot populate gold samples, OCR output, or accepted source evidence, but then permits it as a future comparison signal without prohibiting that content/order from being copied into `ocr_benchmark_report`, `output_manifest`, findings, or other output artifacts. Remediation: permit only a separately authorized comparison operation under a later policy; prohibit text-layer content/order payloads in every gold/OCR/map/source/output artifact; allow only policy-approved derived metrics/findings that carry explicit text-layer provenance and non-canonical status. Acceptance criterion: the boundary and non-waivable failures both reject any text-layer content/order payload in benchmark outputs, not only canonical-source treatment.
- OCR lineage and invalidation are not closed. The scoring plan requires a distinct gold-sample authorization, and optional map use is separately authorized, but the OCR trial record contains neither a gold-sample manifest/revision/hash plus `gold_sample_creation_authorization_id` nor a map-consumption authorization ID. The candidate/scoring-plan references also lack explicit revision/hash bindings in the trial record. Remediation: require exact revision/hash IDs for the OCR candidate manifest and scoring plan; bind a gold-sample manifest with sample IDs, revisions/hashes, predecessor IDs, creation authorization, actor/reviewer, and invalidation rules; add `map_consumption_authorization_id` or an explicit `not_used`; and bind these predecessors in every output row. Acceptance criterion: changing any source/render/map/gold/candidate/scoring/config/authorization predecessor deterministically stales the affected trial and outputs.
Non-blocking notes:
- Step 7 is correctly governance/spec drafting only; it authorizes no OCR execution, PDF text-layer extraction, page-image inspection, gold-sample creation, text comparison, map consumption, or Viral-derived observation.
- Future trial predicates correctly require exact `accepted_protocol`, separately authorized selected-page and render evidence, map evidence only when separately authorized, a frozen OCR candidate manifest, a frozen pre-output gold/scoring plan, and a distinct bounded OCR-benchmark authorization.
- Non-waivable failures correctly cover post-hoc metrics/gold/thresholds, drops, duplicates, reorder, substitution, invention/hallucination, protected-content normalization, and unsupported layout/region coercion.
- Live control surfaces consistently show Step 7 as draft/review-needed and Step 8 as blocked. Viral remains quarantined.
- Assumption: “output artifacts” includes benchmark reports, output manifests, findings payloads, and any persisted comparison evidence, not only OCR text output.
- Receipt: scope `Sourcefold` Step 7 draft only; result `NOT OK`; blockers `2`; next action `apply the two bounded text-contract remediations, then request renewed Sol/Terra review`; elapsed active goal time at receipt creation `86 seconds`; token use at receipt creation `58,812`; timestamp `2026-07-15T18:55:42Z`.
Exact answer:
- NOT OK to commit and NOT OK to proceed to Step 8 draft-only yet. Apply only the two Step 7 remediation items above, keep Step 8 blocked and Viral quarantined, then request renewed Sol/Terra review. This is an architecture verdict, not a release acceptance decision.
Files reviewed:
- `Sourcefold/docs/plans/20260715-sourcefold-phase-0-release-charter/gate_01_qualification_protocol.md`
- `Sourcefold/docs/plans/20260715-sourcefold-phase-0-release-charter/context.md`
- `Sourcefold/docs/plans/20260715-sourcefold-phase-0-release-charter/plan.md`
- `Sourcefold/docs/plans/20260715-sourcefold-phase-0-release-charter/today_20260715_step_plan.md`
- `Sourcefold/docs/roadmap/roadmap.yaml`
- `Sourcefold/PROJECT_STATUS.md`
Verification:
- Review was document-only. No PDF was opened, parsed, rendered, OCRed, hashed, page-counted, inspected, mapped, screenshotted, annotated, or text-layer-extracted; no gold sample, schema, evidence artifact, benchmark artifact, or other project artifact was touched or created. Only this handoff receipt was created; no canonical plan, context, project status, roadmap, release file, or commit was changed.
