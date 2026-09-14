# Invocation examples

These examples test behavior, not exact phrasing.

## 1. Conceptual topic — balanced

```text
/reality-compression lossy compression
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
/reality-compression --expert Git and CI/CD
```

Expected behavior:

- Does not conflate Git, continuous integration, continuous delivery, and continuous deployment.
- Kernel reflects recorded change history plus automated verification and controlled release.
- Causal chain explains how small changes and fast feedback reduce integration/release risk without claiming they eliminate it.
- Boundary includes poor tests, unsafe deployment automation, or large unreviewable changes.
- Comic preserves those distinctions rather than depicting “Git automatically ships code.”

## 3. Decision mode

```text
/reality-compression --decision Should a research team turn a prototype into a shared internal tool?
```

Expected behavior:

- Frames the decision, stakeholders, permissions, ownership, repeatability, and evidence needed.
- Separates a useful demo from a governed operating service.
- Kernel is predictive: repeated value plus an operable harness determines whether scaling is justified.
- Boundary includes low-frequency use, unclear ownership, or costs exceeding decision value.

## 4. Supplied source

```text
/reality-compression --from-source
[paste paper, transcript, report, or meeting notes]
```

Expected behavior:

- First reconstructs the source's own claim and evidence.
- Does not silently import external facts.
- Labels source claims, inferences, contradictions, and missing evidence.
- Comic depicts the source-supported mechanism and visually preserves uncertainty.

## 5. Gate failure

```text
/reality-compression --from-source
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
- `REALITY COMPRESSION COMIC — Status: RENDER_PENDING` is explicit.
- A complete panel-by-panel render brief follows.
- The model never says the skill completed successfully and never labels Mermaid, ASCII, or a prompt as the comic.
