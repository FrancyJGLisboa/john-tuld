---
name: reality-compression
description: "Reconstruct and compress a complex topic or supplied source into the smallest truthful causal model, then produce a coordinated written explanation and educational comic. Use when the user invokes /reality-compression, $reality-compression, Reality Compression, or explicitly asks for the General/AI Reality Compression Radar method. Do not use for ordinary summaries or image-only requests."
---

# Reality Compression

Turn a topic, question, or pasted source into a compact model that remains useful for explanation, prediction, or decision. Complete both deliverables: rigorous text and a comic derived from the same model.

## Invocation contract

Accept any of these forms:

```text
/reality-compression {topic or pasted content}
$reality-compression {topic or pasted content}
Reality Compression: {topic or pasted content}
```

Optional modes:

- `--balanced` (default): compact, accessible, and rigorous.
- `--eli5`: minimize prerequisites without inventing certainty.
- `--expert`: preserve technical vocabulary, equations, and edge cases that affect correctness.
- `--decision`: organize compression around a stated decision and what would change it.
- `--from-source`: stay within supplied material; identify missing evidence rather than filling gaps from memory.
- `--high-assurance`: show the gate audit and source consequential factual claims when retrieval is available.

Infer language from the user and keep text inside the comic in that language. Ask a question only when ambiguity would materially change the model and cannot be handled with explicit branches.

## Hard invariants

1. Reconstruct before compressing. Do not simplify a phenomenon not yet understood.
2. Mechanism before metaphor. Use analogy only after identifying what causes what.
3. Preserve decision-relevant detail, disagreement, boundary conditions, and uncertainty.
4. Separate source fact, established fact, inference, assumption, hypothesis, and unknown when the distinction matters.
5. Prefer causal structure over a glossary or encyclopedic survey.
6. Test the proposed mental model with at least one concrete example and one boundary, counterexample, or falsifier.
7. State what was intentionally omitted.
8. Derive the written explanation and comic from one shared model.
9. The comic must teach the mechanism; decoration or a topic-themed poster does not qualify.
10. Never sacrifice truth for elegance. Cleverness without mechanism, surprise without evidence, and evidence without consequence are failures.
11. Do not end with a plan, outline, or comic prompt when a rendered comic is technically available.
12. Do not claim a complete run unless both text and a rendered comic were delivered.

## End-to-end workflow

Perform these stages in order. They may remain internal unless a visible audit helps the user.

1. **Frame the target.** Identify the phenomenon, intended audience, desired mode, supplied evidence, time sensitivity, and any decision the model must support.
2. **Reconstruct reality.** Determine the operative entities, constraints, incentives, sequence, feedback loops, and measurable outcomes. For supplied content, reconstruct the author's actual claim before evaluating it.
3. **Resolve truth status.** Distinguish what the input says, what is externally established, what is inferred, and what remains uncertain. Retrieve current evidence when required and allowed. In `--from-source`, do not introduce unsupported outside claims.
4. **Find the compression kernel.** Express the smallest causal model that still predicts the important behavior. Delete detail only if removing it does not change the model's conclusions in normal use.
5. **Stress-test it.** Apply a concrete example; test an alternative explanation, counterexample, or failure condition; restore any nuance the test shows is necessary.
6. **Run G1–G10.** Repair failures before drafting. Use [references/gates.md](references/gates.md) for exact pass criteria.
7. **Write the text.** Follow the output contract below. Adapt length to the topic; never pad sections.
8. **Build the comic brief.** Translate the validated model—not the original topic—into a short visual narrative. Read [references/comic-protocol.md](references/comic-protocol.md).
9. **Render the comic.** On ChatGPT with ImageGen, generation is mandatory in the same run. On another runtime, use a capable native image generator if available. If none exists or rendering fails after one reasonable retry, provide the complete render brief and mark the run `RENDER_PENDING`.
10. **Verify alignment.** Check that every comic claim is supported by the text, the causal order is intact, uncertainty is not erased, and no visual label reverses a relationship.

## Gates

All gates must pass for `COMPLETE`. Critical failures block a clean compression; explain the limitation instead of manufacturing closure.

| Gate | Required result |
| --- | --- |
| G1 Reality | Topic/source reconstructed accurately |
| G2 Mechanism | Operative causal mechanism identified |
| G3 Distinctions | Commonly conflated concepts separated |
| G4 Truth status | Facts, source claims, inferences, and unknowns kept distinct |
| G5 Uncertainty | Material uncertainty and disagreement preserved |
| G6 Causality | Chain is coherent, directional, and free of hidden leaps |
| G7 Fidelity | Compression does not distort normal predictions or decisions |
| G8 Concrete test | Example demonstrates the model in operation |
| G9 Limits | Boundary, counterexample, or falsifier is stated |
| G10 Visual parity | Comic faithfully teaches the validated written model |

For detailed pass/fail tests and repair actions, read [references/gates.md](references/gates.md).

## Written output contract

Use this stable order, merging adjacent sections only when the content would otherwise be repetitive:

```text
REALITY COMPRESSION — {TOPIC}

1. The apparent complexity
2. What is actually happening
3. The smallest useful model
4. The causal chain
5. Crucial distinctions
6. Evidence, inference, and uncertainty
7. Concrete test
8. Where the compression breaks
9. Why it matters
10. Compressed takeaway

REALITY COMPRESSION COMIC
Status: COMPLETE | RENDER_PENDING | BLOCKED
[rendered comic, or the render brief when rendering is unavailable]
```

Rules:

- The smallest useful model should normally fit in one short paragraph or a compact causal chain.
- Use a table only when exact comparison or truth-status mapping is clearer than prose.
- Cite fresh or contested external claims when retrieval was used. Do not add citations to purely conceptual reasoning.
- In `--high-assurance`, append a compact G1–G10 audit after the takeaway and before the comic.
- `BLOCKED` is reserved for input that cannot be responsibly reconstructed, prohibited retrieval, or a critical contradiction that the user must resolve.
- `RENDER_PENDING` means the analytical artifact and production brief are complete, but an actual comic is not. Never label a prompt, ASCII diagram, or panel list as a rendered comic.

## Runtime behavior

- **ChatGPT with ImageGen:** generate and display the actual comic. This is the reference implementation and the only environment in which this package promises the intended comic quality.
- **Codex/Claude-style runtime with a capable image tool:** render the comic and verify it if the tool permits inspection; quality may differ from ChatGPT.
- **Runtime without image generation:** complete the text and production-ready brief, return `RENDER_PENDING`, and give the exact brief to a renderer. Do not substitute Mermaid, ASCII art, SVG boxes, or stock imagery for the required comic.

See [references/runtime-installation.md](references/runtime-installation.md) for packaging and installation, and [references/examples.md](references/examples.md) when testing invocation behavior or unfamiliar modes.
