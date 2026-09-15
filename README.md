# John Tuld

[![Validate](https://github.com/FrancyJGLisboa/reality-compression/actions/workflows/validate.yml/badge.svg)](https://github.com/FrancyJGLisboa/reality-compression/actions/workflows/validate.yml)

**Explain the technical work so leadership can understand it, decide, and explain it onward.**

John Tuld is a portable Agent Skill for analysts, engineers, researchers, and technical specialists communicating with executives and other senior decision-makers. It turns complex findings into plain language while preserving how things work, what is at stake, and what remains uncertain.

The name comes from John Tuld, played by Jeremy Irons in *Margin Call* (2011), and his request for an explanation as simple as one for a golden retriever. The principle is to assume no technical background and give the listener enough understanding to judge the consequences. [Scene reference](https://www.imdb.com/title/tt1615147/characters/nm0000460/).

The skill reconstructs the topic, identifies the smallest truthful causal model, stress-tests it, and produces two coordinated outputs:

1. a plain-language executive brief;
2. an educational comic derived from the same validated model.

The intended audience is English-speaking. By default, every user-facing artifact—including the written explanation, headings, comic captions, labels, and production brief—is generated in English, even when the prompt or source material is in another language. A different output language is used only when the user explicitly requests it.

It is not a generic summarizer. A complete run must reconstruct reality before simplifying it, separate facts from inference, preserve consequential uncertainty, test a concrete case and a falsifier, pass G1–G10, and render the comic when the runtime exposes image generation.

## Artifacts produced

Every run produces one coordinated content package from a single validated causal model:

1. **John Tuld Brief** — an English executive explanation that leads with the finding and stakes, explains the mechanism through a concrete example, preserves evidence and uncertainty, and closes with the leadership question when one exists and a sentence the listener can repeat accurately.
2. **John Tuld Comic** — an English educational comic that teaches the same mechanism. When image generation is unavailable, the run instead provides a production-ready English render brief and reports `RENDER_PENDING`.

In `--high-assurance` mode, the written artifact also includes sources for consequential factual claims and a compact G1–G10 audit. A run reports `COMPLETE` only when both the written explanation and rendered comic are delivered.

## Install in one command

Install for both Codex/ChatGPT Desktop and Claude Code:

```bash
curl -fsSL https://raw.githubusercontent.com/FrancyJGLisboa/reality-compression/main/skills/john-tuld/scripts/install.py | python3 - --runtime all
```

Install for only one runtime:

```bash
# Codex and ChatGPT Desktop
curl -fsSL https://raw.githubusercontent.com/FrancyJGLisboa/reality-compression/main/skills/john-tuld/scripts/install.py | python3 - --runtime codex

# Claude Code
curl -fsSL https://raw.githubusercontent.com/FrancyJGLisboa/reality-compression/main/skills/john-tuld/scripts/install.py | python3 - --runtime claude
```

The installer uses the official personal skill locations:

- Codex and ChatGPT Desktop: `~/.agents/skills/john-tuld`
- Claude Code: `~/.claude/skills/john-tuld`

It refuses to overwrite an existing installation. To update intentionally, add `--force`; replacement is staged and validated before the current copy is changed.

If you prefer to inspect code before running it, clone the repository and use:

```bash
python3 skills/john-tuld/scripts/install.py --runtime all
```

## Invoke

Codex or ChatGPT Desktop:

```text
$john-tuld Explain our deployment failure analysis to the COO: [paste findings]
```

Claude Code after the local installation:

```text
/john-tuld Explain our deployment failure analysis to the COO: [paste findings]
```

Also supported by the skill contract:

```text
John Tuld: Explain lossy compression to a nontechnical product leader
/john-tuld --decision Should we turn this prototype into a shared service?
/john-tuld --from-source [paste source]
/john-tuld --expert Git and CI/CD
```

Modes: `--balanced` (default), `--eli5`, `--expert`, `--decision`, `--from-source`, and `--high-assurance`.

The default is a briefing for nontechnical leadership. Use `--expert` when the intended reader needs technical vocabulary, equations, or detailed edge cases.

## Moving from Reality Compression

The skill and plugin are now named `john-tuld`. Install using the commands above and replace previous `$reality-compression` or `/reality-compression` invocations with `$john-tuld` or `/john-tuld`. Existing installations under the old name remain separate; the installer does not rename or delete them. After verifying the new skill, retire the old copy through your runtime's skill or plugin management.

## Native plugin installation

### Claude Code marketplace

This repository is also a Claude Code marketplace. Register it and install the namespaced plugin:

```bash
claude plugin marketplace add FrancyJGLisboa/reality-compression
claude plugin install john-tuld@francyjglisboa-skills
```

The plugin invocation is:

```text
/john-tuld:john-tuld
```

### ChatGPT and Codex plugin

`.codex-plugin/plugin.json` packages the same canonical skill for the OpenAI plugin system. The repository is ready for plugin validation and directory submission.

An arbitrary public GitHub repository cannot install itself directly into ChatGPT on the web. After the plugin is published in the ChatGPT/Codex plugin directory, users install it from the product UI. The one-line installer above works immediately for local Codex and ChatGPT Desktop skill discovery.

## Runtime behavior

| Runtime | Written artifact | Comic behavior | Successful terminal state |
| --- | --- | --- | --- |
| ChatGPT with ImageGen | Required | Render in the same run | `COMPLETE` |
| Codex with an image tool | Required | Render and verify | `COMPLETE` |
| Claude Code with an image tool | Required | Render and verify | `COMPLETE` |
| Runtime without image generation | Required | Return the production brief | `RENDER_PENDING` |

A prompt, panel list, Mermaid diagram, or ASCII sketch is never labeled as a rendered comic.

## Repository structure

```text
.
├── .claude-plugin/
│   ├── marketplace.json
│   └── plugin.json
├── .codex-plugin/
│   └── plugin.json
├── skills/
│   └── john-tuld/
│       ├── SKILL.md
│       ├── agents/openai.yaml
│       ├── references/
│       └── scripts/
├── tests/
└── LICENSE
```

`skills/john-tuld/SKILL.md` is the canonical behavioral contract. Both plugin manifests point to the same skill; there are no divergent Claude and OpenAI prompt copies.

## Validate

```bash
python3 skills/john-tuld/scripts/validate_contract.py skills/john-tuld
python3 -m unittest discover -s tests -v
```

OpenAI plugin validation:

```bash
python3 /path/to/plugin-creator/scripts/validate_plugin.py .
```

Claude Code users can additionally run:

```bash
claude plugin validate .
```

## Requirements

- Python 3.9 or newer for the one-line installer
- Internet access only during remote installation
- Native image generation for a `COMPLETE` run with a rendered comic

No API key is required by the skill itself. Tool availability and permissions are supplied by the host runtime.

## License

MIT
