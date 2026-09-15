# Invocation examples

These examples test behavior, not exact phrasing.

## Role direction — applies to every example

The analyst or specialist explains the mechanism to the stated recipient. John Tuld is the audience model, never the narrator. Titles identify who the explanation is **for**; no title, byline, first-person identity, speech bubble, or caption credits him with producing the analysis.

For an unnamed audience, use `REALITY COMPRESSION FOR NONTECHNICAL LEADERSHIP`. For the COO below, use `REALITY COMPRESSION FOR THE COO`. The comic uses `VISUAL EXPLANATION FOR` the same recipient.

## Explicit John Tuld boardroom scene

```text
$john-tuld --from-source Explain this to John Tuld and show the analyst briefing him in the comic:
Our support team receives 120 requests per day and finishes 100 per day. Both rates have stayed constant. No other process removes requests from the queue.
```

Expected behavior:

- Uses `REALITY COMPRESSION FOR JOHN TULD` and speaks from the analyst's perspective; it does not introduce the narrator as John Tuld.
- The analyst explains the 20-request daily gap and qualifies the continuing increase with the stated constant-rate assumption.
- The render brief assigns every speech bubble to its speaker and points its tail at that speaker.
- John Tuld asks for clarity or acknowledges the explanation. He does not teach the queue mechanism or deliver an expert lecture.
- The final takeaway belongs to the analyst or a neutral caption addressed to the recipient.

Example dialogue, with the roles preserved:

```text
Analyst: We receive 120 requests a day and finish 100. Twenty stay in the queue.
John Tuld: So the queue keeps growing?
Analyst: Yes, by 20 a day while those rates stay unchanged.
```

If a generated image puts the analyst's explanatory lines into John Tuld's speech bubbles, it fails G10 even when the numbers are correct.

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
- `VISUAL EXPLANATION FOR NONTECHNICAL LEADERSHIP — Status: RENDER_PENDING` is explicit when no more specific recipient was supplied.
- A complete panel-by-panel render brief follows.
- The model never says the skill completed successfully and never labels Mermaid, ASCII, or a prompt as the comic.
