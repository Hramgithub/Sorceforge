# NRI OCR and Layout Preservation Rules

These rules apply to every NRI project that extracts, translates, rewrites, or rebuilds material from PDFs, scans, OCR, or page renders.

## Preserve Structure

- Preserve source heading hierarchy. Do not promote or demote section, scene, subsection, table, or card headings without a documented reason.
- Normalize reader-facing headings before production output: remove OCR/service headings, remove all-caps styling when it is not semantically required, and use consistent capitalization for equivalent heading levels.
- If a reader-facing Markdown/HTML output has no table of contents, add one. For Markdown outputs, use a compact TOC built from `##` headings by default; for HTML, `###` headings may also receive anchors or appear in navigation when the document needs deeper browsing. Use stable anchors/hyperlinks, and keep page markers hidden when they are needed only for audit.
- Preserve page markers when source-to-output traceability matters.
- Keep tables as tables whenever they carry rules, stats, choices, references, or structured data.
- Keep cards/stat blocks structurally separate from prose.
- For source-faithful rebuilds, work page by page: one source PDF page render, one source Markdown page file, one translated Markdown page file. Do not translate, concatenate, or redesign until the source page structure is approved.
- Do not create a table unless the source page has an actual table. If the source uses prose, labels, or lists, preserve that structure.
- For mixed pages, keep text, image/sidebar/callout anchors, and source order visible in the source Markdown. Layout decisions such as moving sidebars belong to a later reader/production stage.
- A source-visible quote, sidebar/callout, handout, list, table, or stat block must receive semantic Markdown during reconstruction and, when the structural review profile is used, an identity-bound typed sidecar. `MASTER_EN` preserves or explicitly transforms accepted structure; it must not be the first stage that rediscovers a boundary flattened by reconstruction. HTML/DOCX/PDF may style the structure but must not create it from untyped prose or a raster-only crop.
- Semantic kind and transport syntax are separate authorities. A stat block is not a quotation: accepted reconstruction and MASTER Markdown must keep its title and rows as ordinary Markdown while an identity-bound typed sidecar seals the exact neutral span. A publication adapter may add paired machine-only markers around that exact span and render a neutral statblock container, but it must never use `>` or a quotation/callout as statblock transport. Ordinary source quotations, handouts, and callouts retain their reviewed blockquote syntax and must not receive statblock styling.
- A role-specific reviewed section must be complete, not merely internally valid. When a profile declares an appendix of stat blocks or character records, validation must require the complete title/record/leaf topology and lossless reviewed partitions for any source block that fuses two roles. Downstream stages must not guess missing headings from capitalization, repeated labels, or scenario vocabulary.
- A source-visible compact sequence of labelled or measured lines must remain one reviewed line group during reconstruction. Represent its internal line boundaries with Markdown hard breaks, keep the visually reviewed order, and retain an ordinary paragraph boundary after the group. The structural review profile must bind the group to ordered source blocks and reject internal blank paragraphs, missing hard breaks, reordered lines, or an unnecessary hard break on the final line. Do not infer such groups from punctuation or field names alone.
- A source-confirmed OCR correction must be recorded as an exact reviewed source-to-reader replacement with a reason. The immutable extracted unit keeps its original identity; the correction is valid only when its source form occurs exactly once in selected page evidence and its replacement is present in reviewed Markdown. Structural span validation and OCR-equivalence auditing must consume the same correction ledger.
- When selected structural title evidence disagrees across OCR views, reconstruction must fail closed until visual review binds the exact source view/index to one exact reader heading. A changed heading also requires the exact source-to-reader correction ledger entry; an unchanged confirmation is permitted for visual line wraps or punctuation that must remain lexical. Never split or join title words from a dictionary, casing, or token-length heuristic.
- Reviewed reconstruction Markdown uses one empty root line between adjacent semantic blocks. Repeated empty root lines must be rejected by Stage 05/06; a reviewed author may reduce them only through exact, uniquely matching before/after line declarations with the observed count. Blockquote blank markers and hard-break line groups are content and must not be collapsed by this rule.

## Preserve Emphasis

- Preserve meaningful bold, italic, quote, list, and table formatting from the source.
- If OCR loses bold/italic/quote formatting, restore it from the page render when feasible.
- If formatting cannot be verified, record it in a QA table instead of silently flattening it.

## Reader-Safe Output

- Service/OCR artifacts must not leak into final reader files unless explicitly kept for QA.
- Do not leave raw OCR markers such as stray `@`, broken columns, or file captions in production text.
- Keeper/reader documents should be readable without opening the original PDF, while still retaining enough page markers for audit.

## QA Requirement

When a formatting decision may affect meaning, create or update a local QA table with:

| Original/source signal | Proposed output | Evidence | Decision |
|---|---|---|---|
| TBD | TBD | TBD | TBD |
