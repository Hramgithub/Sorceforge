# Viral Forward 10 Step Plan

Status: active forward plan; not an authorization by itself

Created: 2026-07-18

Baseline commit: `c3bda8a8b32a87f92f23e434b9ffd5999637bedf`

This plan starts after `MBR-G1-VIRAL-001`, which blocks a real
`pre_ocr_map_bundle` freeze from SPM/RT/VSR/PIR/PMR/PRM alone. Each step below
requires its own bounded authorization, exact inputs, allowed outputs, limits,
expiry, invalidation behavior, validation, and checkpoint/commit approval.

## Reviewed Direction

Sol review: OK with revisions. Required explicit non-accepting schema status,
canonical hashing/serialization, ID namespaces, coordinate basis, baseline
commit lineage, source input hashes for map-layer steps, no OCR/text payload
leakage, validation before remediation, exact map hashes for bundle freezing,
and a map-consumption admission record before OCR.

Terra review: conditional OK. Tightened commit/remediation authority, forbids
promoting PRM provisional IDs/boxes into canonical identity, limits
text-in-art to flags/zones only, keeps bundle freeze separate from Gate 1
acceptance, prevents gold text/sample creation during OCR prep, and prevents an
OCR benchmark from self-advancing Gate 1.

## Ten Steps

1. `BA-G1-VIRAL-MAPSCHEMA-001`
   Authorize only a version-bound provisional map schema plus shared
   page/region identity and coordinate model. This does not accept the
   candidate, freeze a bundle, create map payload, or authorize OCR.

2. `MSID-G1-VIRAL-001`
   Create a schema/identity packet for `common_map`, `doc_map`, `content_map`,
   `art_map`, and `pre_ocr_map_bundle`. It must define canonical
   serialization/hashing, ID namespaces, coordinate basis, schema versions,
   baseline commit lineage, invalidation, and payload-leakage rules.

3. MSID review
   Send `MSID-G1-VIRAL-001` to Sol/Terra. Any remediation and commit require
   explicit separate approval. No map payload can be produced from an unreviewed
   or stale MSID.

4. `BA-G1-VIRAL-DOCMAP-001`
   Create a non-accepting trial `doc_map` from current SPM/RT/VSR/PIR/PMR/PRM
   lineage using MSID-defined trial IDs. Do not promote PRM provisional IDs or
   boxes into canonical identity. No OCR, copied text, or accepted reading
   order.

5. `BA-G1-VIRAL-CONTENTMAP-001`
   Create a non-accepting trial `content_map` referencing `doc_map`/MSID IDs.
   It may contain structural candidates only. It must not contain copied text,
   OCR semantics, accepted OCR routing, PDF text-layer content, or source truth.

6. `BA-G1-VIRAL-ARTMAP-001`
   Create a non-accepting trial `art_map` referencing `doc_map`/MSID IDs. It
   may contain visual/mixed/text-in-art flags or zones only. It must not
   transcribe text, OCR, or make semantic text claims.

7. `BA-G1-VIRAL-MAPCONSISTENCY-001`
   Validate cross-map references, missing/duplicate regions, stale
   predecessors, schema conformance, coordinate basis, and payload leakage.
   Remediation requires a separate bounded authorization.

8. `BA-G1-VIRAL-MAPBUNDLE-001`
   Freeze `pre_ocr_map_bundle` only from exact passing map revisions, current
   map hashes, and current schema hash. The bundle is a lineage freeze only,
   not Gate 1 acceptance, source-profile acceptance, OCR readiness, or
   downstream consumption permission.

9. `BA-G1-VIRAL-OCRPREP-001`
   Prepare an OCR candidate manifest, scoring plan, gold-sample creation plan,
   and map-consumption admission record. Do not run OCR. Do not create gold
   text or sample answers.

10. `BA-G1-VIRAL-OCRBENCH-001`
    After separate authorization for gold sample creation and admitted OCR run,
    execute a bounded OCR benchmark, record findings, and request or recommend
    Gate 1 advance/remediation. The benchmark cannot advance Gate 1 by itself.

## Global Limits

- No PDF opening, parsing, rehashing, recounting, or new PDF inspection unless
  a later bounded authorization names that exact action.
- No OCR, transcription, copied source text, PDF text-layer payload, gold text,
  QA execution, fixture creation, source acceptance, translation,
  proofreading, renderer/profile acceptance, or implementation unless a later
  step explicitly authorizes that exact action.
- Roadmap YAML and status rollups may carry only IDs, links, status, blockers,
  and concise comments. Region rows, coordinates, map payload, and copied text
  belong only in dedicated evidence artifacts when authorized.
