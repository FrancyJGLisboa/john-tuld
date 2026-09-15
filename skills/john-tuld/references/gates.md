# G1–G10 quality gates

Run these gates after constructing the candidate model and again after the comic is rendered. A gate passes because the artifact meets its test, not because a heading exists.

## Analytical gates

### G1 — Reality reconstructed

**Pass:** The artifact identifies the actual phenomenon or source claim, its scope, actors or components, constraints, and relevant context. It preserves the analyst as speaker and the intended executive as recipient. It does not answer a nearby but different question.

**Fail signals:** Keyword summary; treating a disputed claim as reality; ignoring the user's decision or source boundaries; presenting John Tuld as the explaining persona instead of the listener.

**Repair:** Restate the target in one sentence. Branch explicitly if two interpretations remain viable.

### G2 — Core mechanism identified

**Pass:** The explanation says what changes what, through which intermediate step, under which conditions.

**Fail signals:** Definitions without process; lists of features; metaphor standing in for mechanism.

**Repair:** Write `A changes B because C; this produces D unless E` and validate each link.

### G3 — Crucial distinctions preserved

**Pass:** Concepts that would lead to different predictions or actions are not conflated.

**Fail signals:** Correlation treated as causation; capability confused with outcome; tool confused with workflow; average confused with distribution.

**Repair:** Add only distinctions that materially change interpretation.

### G4 — Truth status separated

**Pass:** The reader can tell the difference among supplied claims, independently established facts, inference, hypothesis, assumption, and unknown.

**Fail signals:** An inference written as fact; a source's assertion presented as verified; invented precision.

**Repair:** Label consequential statements inline or in a compact evidence table.

### G5 — Uncertainty preserved

**Pass:** Material uncertainty, disagreement, missing evidence, and confidence limits survive compression.

**Fail signals:** A neat single story despite competing mechanisms; certainty added for narrative smoothness.

**Repair:** State what is uncertain and whether it changes the kernel, only the parameters, or the conclusion.

### G6 — Causal chain coherent

**Pass:** Each arrow has a defensible mechanism and correct direction. Feedback loops and timing are included when they change behavior.

**Fail signals:** Hidden step; reversed cause; sequence mistaken for causality; omitted incentive or constraint.

**Repair:** Challenge each arrow with “by what mechanism?” and “what else could produce this?”

### G7 — Compression faithful

**Pass:** A reasonable reader using the compressed model would make the same normal-case predictions or decisions as with the fuller model.

**Fail signals:** Exception presented as rule; important qualifier omitted; analogy predicts something the real mechanism does not.

**Repair:** Restore the smallest missing qualifier, variable, or branch.

### G8 — Concrete test passed

**Pass:** A specific example can be walked through using the model without adding an unmentioned mechanism.

**Fail signals:** Example merely repeats the definition; unexplained exception appears.

**Repair:** Choose a representative case with an observable start, transition, and result.

### G9 — Limits exposed

**Pass:** At least one boundary condition, counterexample, failure mode, or falsifying observation is explicit.

**Fail signals:** Universal wording; no way to know when the model stops being useful.

**Repair:** State `This model breaks or needs expansion when …` and `Evidence that would overturn it is …` when applicable.

## Visual gate

### G10 — Comic parity

**Pass:** The comic preserves the same entities, causal direction, distinctions, uncertainty, takeaway, and speaker/recipient roles as the validated text. The analyst or neutral captions explain; the executive receives the explanation. John Tuld, if present, listens or asks questions. It is legible and understandable without inventing claims.

**Fail signals:** Decorative poster; text-heavy infographic; metaphor contradicts mechanism; omitted uncertainty changes meaning; illegible labels; explanatory speech assigned to John Tuld; a title, byline, or caption that credits him as author or teacher.

**Repair:** Simplify the panels, not the truth. Correct speaker assignments and bubble-tail targets in the render brief when roles are reversed. Regenerate once when a correctable rendering error materially damages the teaching goal. If the tool still fails, return `RENDER_PENDING` with the exact corrected brief.

## Completion rule

- `COMPLETE`: G1–G10 pass and the rendered comic is present.
- `RENDER_PENDING`: G1–G9 pass, but no acceptable rendered comic can be delivered in the current runtime.
- `BLOCKED`: Any of G1, G2, G4, G5, or G7 cannot be repaired with available information, or the requested work cannot be performed responsibly.

Do not average gate scores. One critical failure is not canceled by strength elsewhere.
