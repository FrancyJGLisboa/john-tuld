---
name: john-tuld
description: "Help analysts and technical specialists explain complex findings to executives and other nontechnical decision-makers. Turn a topic or supplied source into a plain-language executive brief and matching educational comic, preserving the mechanism, stakes, and uncertainty. Use for leadership briefings, communicating technical work upward, or explicit /john-tuld and $john-tuld requests. Do not use for ordinary summaries or image-only requests."
---

# John Tuld

Help the person who understands the technical work explain it to the person who must make decisions and communicate them onward. Reconstruct a topic, question, or supplied source into the smallest truthful model, then deliver a plain-language executive brief and an educational comic derived from that same model.

The name refers to John Tuld, played by Jeremy Irons in *Margin Call* (2011), and his request for a golden-retriever-level explanation. Apply that demand for clarity: assume no technical prerequisites, respect the reader's intelligence, and keep every qualification that could change the decision.

## Invocation contract

Accept any of these forms:

```text
/john-tuld {topic or pasted content}
$john-tuld {topic or pasted content}
John Tuld: {topic or pasted content}
```

Optional modes:

- `--balanced` (default): a compact executive briefing with plain language, stakes, and enough mechanism to judge the conclusion.
- `--eli5`: minimize prerequisites without inventing certainty.
- `--expert`: preserve technical vocabulary, equations, and edge cases that affect correctness.
- `--decision`: organize compression around a stated decision and what would change it.
- `--from-source`: stay within supplied material; identify missing evidence rather than filling gaps from memory.
- `--high-assurance`: show the gate audit and source consequential factual claims when retrieval is available.

## Audience and language

The target audience is English-speaking and, by default, consists of executives, board members, or other senior stakeholders who do not work in the subject's technical details. The skill serves the analyst, engineer, researcher, or specialist preparing that communication. Adapt to a different audience when the user specifies one; `--expert` retains technical depth for specialist readers.

Produce the written explanation, section headings, comic brief, captions, labels, and all other instructional content in clear natural English, even when the request or supplied source is in another language. Preserve non-English proper names and quote source-language terms only when they are necessary to the explanation; translate or explain them in English. Use another output language only when the user explicitly requests it.

Do not infer the output language from the language of the prompt. Ask a question only when ambiguity would materially change the model and cannot be handled with explicit branches.

## Communicating upward

- Lead with the finding and its consequence. Connect to money, time, risk, customers, or operational capacity only when the evidence supports that connection; do not invent a business case or urgency.
- Explain what changes what in ordinary words before naming the technical concept. Spell out necessary acronyms and explain numbers with their units, baseline, and time period when available.
- Make the brief speakable in a meeting and usable without the comic. Put detailed derivations in a technical appendix when requested or when `--expert` or `--high-assurance` makes them useful.
- State the decision or question for leadership when one exists. Separate the evidence from any recommendation, and say what missing information or changed assumption would alter the answer.
- End with a sentence the stakeholder can repeat accurately to someone else. Use the film reference to guide clarity; roleplay, finance jargon, and a golden retriever character are not required in the output.

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

1. **Frame the target.** Identify the phenomenon, desired mode, supplied evidence, time sensitivity, audience, and any decision the model must support. Assume an English-speaking nontechnical senior decision-maker unless the user specifies a different audience or explicitly requests another output language. If the decision or stakes are unknown, state that limitation without inventing them.
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
JOHN TULD BRIEF — {TOPIC}

1. What you need to know — the finding and why it matters
2. How it works — the smallest useful model, causal chain, and crucial distinctions
3. One concrete example — the model in operation
4. What could change this — evidence, inference, uncertainty, limits, and material omissions
5. The decision and the sentence to repeat — the leadership question, if any, and a truthful takeaway

JOHN TULD COMIC
Status: COMPLETE | RENDER_PENDING | BLOCKED
[rendered comic, or the render brief when rendering is unavailable]
```

Rules:

- Keep the opening brief enough to say aloud in about one minute. Expand only where the audience or decision needs it; avoid a technical preamble.
- When the source does not justify a decision or recommendation, say so. An explanatory request can end with the takeaway alone.
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
