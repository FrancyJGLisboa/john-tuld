# Runtime-neutral installation

The canonical skill folder contains `SKILL.md`, OpenAI UI metadata under `agents/`, and conditional guidance under `references/`. The GitHub repository wraps this same folder in both OpenAI and Claude plugin manifests. No API key or runtime-specific prompt fork is required.

## ChatGPT / OpenAI skill-capable environments

For local Codex and ChatGPT Desktop discovery, install the folder at:

```text
~/.agents/skills/reality-compression/
```

Keep `agents/openai.yaml` inside the package. Invoke with `$reality-compression` or `Reality Compression: …`.

For the reference experience, the runtime must expose native image generation to the agent. The package does not emulate ImageGen and does not promise equivalent comic quality elsewhere.

## Codex-style runtimes

Copy the complete folder into the official user-level skills directory:

```text
~/.agents/skills/reality-compression/
```

Or run from the unpacked package directory:

```bash
python3 scripts/install.py --runtime codex
```

Restart or refresh skill discovery if the runtime does not detect new skills dynamically.

## Claude-style runtimes

Copy the complete folder into Claude Code's personal skills directory:

```text
~/.claude/skills/reality-compression/
```

Or run:

```bash
python3 scripts/install.py --runtime claude
```

Use `--target-claude /absolute/path/to/skills` to override the destination. Without an image generator, the required terminal state is `RENDER_PENDING`, accompanied by the complete comic brief.

The GitHub repository also includes a Claude marketplace manifest. Plugin installations use the namespaced invocation `/reality-compression:reality-compression`.

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
quick_validate.py /path/to/reality-compression
```
