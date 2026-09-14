# Reality Compression

[![Validate](https://github.com/FrancyJGLisboa/reality-compression/actions/workflows/validate.yml/badge.svg)](https://github.com/FrancyJGLisboa/reality-compression/actions/workflows/validate.yml)

Reality Compression is a portable Agent Skill that reconstructs a complex topic, identifies the smallest truthful causal model, stress-tests it, and produces two coordinated outputs:

1. a rigorous written explanation;
2. an educational comic derived from the same validated model.

It is not a generic summarizer. A complete run must reconstruct reality before simplifying it, separate facts from inference, preserve consequential uncertainty, test a concrete case and a falsifier, pass G1–G10, and render the comic when the runtime exposes image generation.

## Install in one command

Install for both Codex/ChatGPT Desktop and Claude Code:

```bash
curl -fsSL https://raw.githubusercontent.com/FrancyJGLisboa/reality-compression/main/skills/reality-compression/scripts/install.py | python3 - --runtime all
```

Install for only one runtime:

```bash
# Codex and ChatGPT Desktop
curl -fsSL https://raw.githubusercontent.com/FrancyJGLisboa/reality-compression/main/skills/reality-compression/scripts/install.py | python3 - --runtime codex

# Claude Code
curl -fsSL https://raw.githubusercontent.com/FrancyJGLisboa/reality-compression/main/skills/reality-compression/scripts/install.py | python3 - --runtime claude
```

The installer uses the official personal skill locations:

- Codex and ChatGPT Desktop: `~/.agents/skills/reality-compression`
- Claude Code: `~/.claude/skills/reality-compression`

It refuses to overwrite an existing installation. To update intentionally, add `--force`; replacement is staged and validated before the current copy is changed.

If you prefer to inspect code before running it, clone the repository and use:

```bash
python3 skills/reality-compression/scripts/install.py --runtime all
```

## Invoke

Codex or ChatGPT Desktop:

```text
$reality-compression --expert Git and CI/CD
```

Claude Code after the local installation:

```text
/reality-compression --expert Git and CI/CD
```

Also supported by the skill contract:

```text
Reality Compression: lossy compression
/reality-compression --decision Should we turn this prototype into a shared service?
/reality-compression --from-source [paste source]
```

Modes: `--balanced` (default), `--eli5`, `--expert`, `--decision`, `--from-source`, and `--high-assurance`.

## Native plugin installation

### Claude Code marketplace

This repository is also a Claude Code marketplace. Register it and install the namespaced plugin:

```bash
claude plugin marketplace add FrancyJGLisboa/reality-compression
claude plugin install reality-compression@francyjglisboa-skills
```

The plugin invocation is:

```text
/reality-compression:reality-compression
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
│   └── reality-compression/
│       ├── SKILL.md
│       ├── agents/openai.yaml
│       ├── references/
│       └── scripts/
├── tests/
└── LICENSE
```

`skills/reality-compression/SKILL.md` is the canonical behavioral contract. Both plugin manifests point to the same skill; there are no divergent Claude and OpenAI prompt copies.

## Validate

```bash
python3 skills/reality-compression/scripts/validate_contract.py skills/reality-compression
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
