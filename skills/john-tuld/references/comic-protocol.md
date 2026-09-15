# Comic generation protocol

Use this protocol only after G1–G9 pass. The comic is the final compression layer.

Default to a nontechnical senior stakeholder. Make the mechanism, consequence, and material uncertainty understandable through ordinary language and concrete visuals. A reader should not need the analyst present to decode the comic. Depict the subject being explained; the John Tuld name does not require film characters, a boardroom, or a golden retriever.

## Speaker and recipient

The comic is an explanation **from the analyst to the executive**. John Tuld represents the person receiving reality compression. He is never its expert presenter, author, teacher, or narrator.

When people appear, assign the explanatory speech to the analyst or specialist. The executive can ask questions, react, or confirm understanding. Neutral captions can explain the mechanism in a character-free comic. If John Tuld is depicted, keep him in the listening or questioning role and do not attribute neutral captions to him.

For every dialogue panel, specify the speaker, exact words, and speech-bubble tail target in the render brief. Give this role mapping to the image generator explicitly; a name or suit alone is insufficient to establish who explains. Check the final panel as carefully as the opening: the analyst supplies the takeaway to the recipient.

## 1. Extract the visual truth set

Create a private list of no more than seven propositions the comic must preserve:

- the initial problem or misleading surface appearance;
- the central actors or components;
- the causal transformation;
- the feedback, constraint, or gate if essential;
- the observable outcome;
- one crucial distinction or boundary;
- the compressed takeaway.

Every panel must serve at least one proposition. Remove decorative panels that do not teach.

## 2. Select a visual grammar

Prefer a concrete recurring metaphor only if its relationships map correctly to the real mechanism. Otherwise depict the mechanism directly.

Use 5–8 panels. A reliable arc is:

1. apparent complexity or failure;
2. hidden structure appears;
3. mechanism starts;
4. key transformation;
5. consequence or feedback;
6. boundary or common confusion;
7. resolved mental model;
8. takeaway, if needed.

Avoid separate legends when a short in-panel label works. Keep prose outside the image; inside, use short captions, arrows, names, and one final line.

## 3. Build the render brief

The brief must include:

- exact topic and audience;
- speaker/recipient mapping, including that John Tuld is the listener if depicted;
- educational objective in one sentence;
- aspect ratio and panel count;
- consistent characters or objects;
- panel-by-panel action and minimal exact text, with a named speaker or neutral narrator for every line;
- visual mapping for the causal arrows;
- facts or distinctions that must not be altered;
- desired style: polished editorial educational comic, strong visual hierarchy, legible lettering, restrained palette, no corporate stock-art look;
- exclusions: no extra claims, no fake citations, no random equations, no logos unless necessary, no decorative jargon, no unreadable microtext.

Use English for all visible text, including captions, speech, arrows, and labels, even when the request or source is in another language. Preserve a source-language term only when it is itself instructional, and explain it in English. Use another output language only when the user explicitly requests it. Quote exact labels. Keep each label short enough for reliable rendering.

## 4. Render by runtime

### ChatGPT reference path

Use the native image generation tool in the same run. Supply the render brief and explicitly require a coherent multi-panel educational comic that preserves the analyst-to-executive direction of explanation. After generation, display the image under `VISUAL EXPLANATION FOR {AUDIENCE}`, using the same recipient as the written explanation.

Inspect the rendered result when inspection is available. Regenerate once if any of these materially fail:

- a causal arrow is reversed;
- a required distinction disappears;
- visible text changes the claim;
- a speech bubble, caption, title, or final takeaway makes John Tuld the explaining expert;
- panels are missing or out of order;
- labels are unusably illegible.

Do not regenerate merely for subjective style preferences.

### Other runtimes

Use a native image tool only if it can plausibly follow the panel brief. If no such tool exists, output the full brief verbatim beneath `Status: RENDER_PENDING`. The brief is a handoff artifact, not the comic itself.

## 5. Alignment check

Before `COMPLETE`, answer internally:

1. Does the image teach the smallest useful model?
2. Does every arrow point in the same direction as the written causal chain?
3. Are conditional claims and the metaphor's limits preserved without adding behavior absent from the real system?
4. Does the analyst or neutral caption explain the mechanism, with the executive receiving it and John Tuld never presented as the expert narrator?
5. Can the final panel be traced directly to the analyst's written takeaway for the recipient?

Any consequential “no” fails G10.
