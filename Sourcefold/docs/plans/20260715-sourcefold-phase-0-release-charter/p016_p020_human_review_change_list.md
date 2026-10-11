# P016-P020 Human Review Change List

Status: `corrections_rebuilt_pending_final_recheck`

This list records Bogdan review findings for the P016-P020 aggressive sequential
run before any corrective rebuild is authorized.

## P016-CHANGE-001

- Page: `016`
- Reported by: Bogdan Telegram message `2090`
- Status: `corrected_pending_final_recheck`
- Artifact observed: `P016SEM-G1-VIRAL-001`
- Current issue: the two late-history paragraphs beginning `In 1961, the island
  was deemed off limits...` and `Throughout the 1970s and 80s...` are currently
  included in `SU-P016-KEEPER-005`.
- Expected correction: keep `SU-P016-KEEPER-005` scoped to the Keeper's Notes
  body ending with `The Keeper can decide if the investigators can glean anything
  relevant to their investigation from the book.`, then emit the two late-history
  paragraphs as a separate history semantic unit after the Keeper's Notes block.
- Correction result: `SU-P016-KEEPER-005` is bounded by an explicit
  `semantic_split_contract`, and the late-history text now appears as
  `SU-P016-HIST-003`.
- Verification: focused P016-P020 aggressive batch lane passed after rebuilding
  the full P016-P020 sequence.

## P017-REVIEW-001

- Page: `017`
- Reported by: Bogdan Telegram message `2093`
- Status: `reviewed_ok_no_correction_requested`
- Artifact observed: `P017SEM-G1-VIRAL-001`
- Human note: `17 ok`
- Deferred implementation notes: no P017 semantic/source correction is requested
  from this review note.

## P018-CHANGE-001

- Page: `018`
- Reported by: Bogdan Telegram message `2096`
- Status: `corrected_pending_final_recheck`
- Artifact observed: `P018SEM-G1-VIRAL-001`
- Current issue: `SU-P018-KEEPER-002` includes ordinary body text after the
  Keeper's Notes paragraph. The Keeper's Notes unit currently consumes the
  piazza/village description beginning `The hotel is located right on the town
  piazza...` and continuing through `A number of streets lead away from the
  piazza...`.
- Expected correction: keep `SU-P018-KEEPER-002` scoped only to the short
  Keeper's Notes body about Italian speakers and young helpers carrying gear into
  the hotel lobby, then emit the piazza/village description as ordinary body text
  after the Keeper's Notes block.
- Correction result: `SU-P018-KEEPER-002` is bounded by an explicit
  `semantic_split_contract`, and the piazza/village description now appears as
  `SU-P018-WELCOME-004`.
- Verification: focused P016-P020 aggressive batch lane passed after rebuilding
  the full P016-P020 sequence.

## P019-REVIEW-001

- Page: `019`
- Reported by: Bogdan Telegram message `2099`
- Status: `reviewed_ok_no_correction_requested`
- Artifact observed: `P019SEM-G1-VIRAL-001`
- Human note: `19 ok`
- Deferred implementation notes: no P019 semantic/source correction is requested
  from this review note.

## P020-REVIEW-001

- Page: `020`
- Reported by: Bogdan Telegram message `2102`
- Status: `reviewed_ok_no_correction_requested`
- Artifact observed: `P020SEM-G1-VIRAL-001`
- Human note: `20 ok`
- Deferred implementation notes: no P020 semantic/source correction is requested
  from this review note.
