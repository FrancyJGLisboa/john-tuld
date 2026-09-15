# Runtime-neutral installation

The canonical skill folder contains `SKILL.md`, OpenAI UI metadata under `agents/`, and conditional guidance under `references/`. The GitHub repository wraps this same folder in both OpenAI and Claude plugin manifests. No API key or runtime-specific prompt fork is required.

## Downloadable skill bundle

Download [skills.zip](https://github.com/FrancyJGLisboa/john-tuld/raw/refs/heads/main/skills.zip) for the standalone skill, including its license and version. The archive contains one top-level `john-tuld/` folder and preserves all relative reference paths.

Use the ZIP directly in a dedicated standalone skill importer when one is available, or extract that folder into a local runtime's personal skills directory. ChatGPT web ZIP import is not verified for this package; OpenAI's [current documentation](https://learn.chatgpt.com/docs/build-skills) describes web distribution through plugins. A standalone skill ZIP and a plugin package use different layouts.

## ChatGPT / OpenAI skill-capable environments

For local Codex and ChatGPT Desktop discovery, install the folder at:

```text
~/.agents/skills/john-tuld/
```

Keep `agents/openai.yaml` inside the package. Invoke with `$john-tuld` or `Explain to John Tuld: …`. The skill name identifies the listener; the analyst remains the explanatory speaker.

For the reference experience, the runtime must expose native image generation to the agent. The package does not emulate ImageGen and does not promise equivalent comic quality elsewhere.

## Codex-style runtimes

Copy the complete folder into the official user-level skills directory:

```text
~/.agents/skills/john-tuld/
```

Or run from the unpacked package directory:

```bash
python3 scripts/install.py --runtime codex
```

Restart or refresh skill discovery if the runtime does not detect new skills dynamically.

## Claude-style runtimes

Copy the complete folder into Claude Code's personal skills directory:

```text
~/.claude/skills/john-tuld/
```

Or run:

```bash
python3 scripts/install.py --runtime claude
```

Use `--target-claude /absolute/path/to/skills` to override the destination. Without an image generator, the required terminal state is `RENDER_PENDING`, accompanied by the complete comic brief.

The GitHub repository also includes a Claude marketplace manifest. Plugin installations use the namespaced invocation `/john-tuld:john-tuld`.

## Portable/manual use

If a runtime does not implement skill discovery, add `SKILL.md` as project instructions and retain the relative `references/` paths. The invocation and completion contract remain unchanged.

ChatGPT on the web installs reusable public skills through the plugin directory rather than directly from an arbitrary GitHub URL. The repository's `.codex-plugin/plugin.json` is the package manifest for that publication path.

## Validation

From the package root:

```bash
python3 scripts/validate_contract.py .
```

When the OpenAI skill validator is available, also run:

```bash
quick_validate.py /path/to/john-tuld
```
