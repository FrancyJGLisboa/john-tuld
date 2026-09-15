# Invocation examples

These examples test behavior, not exact phrasing.

## Executive briefing — default audience

```text
$john-tuld --from-source Explain this to the COO:
In a two-week internal test, our release checks found 9 of 12 deliberately introduced failures. The previous checks found 5 of the same 12. The new checks add 8 minutes per release. We have not measured customer incidents or tested the larger service yet. The team wants approval for a limited pilot.
```

Expected behavior:

- Opens with the finding and leadership question: the new checks caught more failures in the test but take longer, and the team is asking for a limited pilot.
- Explains the mechanism in ordinary words: automatic checks inspect a change before release; broader checks can catch more problems and take more time.
- Keeps the numbers in context: 9 versus 5 of the same 12 planted failures over two weeks, 8 extra minutes per release, and 3 planted failures still missed.
- Does not claim fewer customer incidents, guaranteed production reliability, annual savings, or that a small test proves the result for the larger service. Any support for a pilot is labeled a recommendation contingent on the missing evidence and cost being acceptable.
- Ends with a sentence a leader can repeat without dropping those limits. The comic shows the same tradeoff; it does not imply the release process is now failure-proof.

## 1. Conceptual topic — balanced

```text
/john-tuld lossy compression
```

Expected behavior:

- Kernel captures selective forgetting under an acceptable-error criterion.
- Distinguishes lossy from lossless compression.
- Concrete test can use JPEG, audio, or a task-oriented map.
- Boundary explains artifacts or unacceptable information loss.
- Comic shows information-rich reality becoming a smaller task-sufficient representation.
- ChatGPT with ImageGen ends `COMPLETE`; a text-only runtime ends `RENDER_PENDING` with the exact brief.

## 2. Technical workflow — expert

```text
/john-tuld --expert Git and CI/CD
```

Expected behavior:

- Does not conflate Git, continuous integration, continuous delivery, and continuous deployment.
- Kernel reflects recorded change history plus automated verification and controlled release.
- Causal chain explains how small changes and fast feedback reduce integration/release risk without claiming they eliminate it.
- Boundary includes poor tests, unsafe deployment automation, or large unreviewable changes.
- Comic preserves those distinctions rather than depicting “Git automatically ships code.”

## 3. Decision mode

```text
/john-tuld --decision Should a research team turn a prototype into a shared internal tool?
```

Expected behavior:

- Frames the decision, stakeholders, permissions, ownership, repeatability, and evidence needed.
- Separates a useful demo from a governed operating service.
- Kernel is predictive: repeated value plus an operable harness determines whether scaling is justified.
- Boundary includes low-frequency use, unclear ownership, or costs exceeding decision value.

## 4. Supplied source

```text
/john-tuld --from-source
[paste paper, transcript, report, or meeting notes]
```

Expected behavior:

- First reconstructs the source's own claim and evidence.
- Does not silently import external facts.
- Labels source claims, inferences, contradictions, and missing evidence.
- Comic depicts the source-supported mechanism and visually preserves uncertainty.

## 5. Gate failure

```text
/john-tuld --from-source
“Everyone knows the new method doubles accuracy.”
```

Expected behavior:

- Does not invent the method, baseline, metric, population, or evidence.
- G1/G4/G7 cannot pass.
- Returns `BLOCKED`, names the missing evidence, and asks for the minimum material needed.
- Does not generate a confident explanatory comic from an unsupported assertion.

## 6. Comic tool unavailable

The text passes G1–G9, but the runtime exposes no image generator.

Expected behavior:

- Full written output is delivered.
- `JOHN TULD COMIC — Status: RENDER_PENDING` is explicit.
- A complete panel-by-panel render brief follows.
- The model never says the skill completed successfully and never labels Mermaid, ASCII, or a prompt as the comic.
