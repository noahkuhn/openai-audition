# Evidence Protocol

The storage model is layered because each audience needs a different artifact.

X needs a hook.

OpenAI needs a clean case file.

Builders need proof.

Raw Codex logs are source material, not the public product.

## Layer 1: Attention Surface

Purpose:

- Make a stranger understand the project in five seconds.

Artifacts:

- `index.html`
- `launch/x-thread-draft.md`
- `launch/video-outline.md`

Rules:

- No raw transcripts.
- No long explanations.
- One clean promise: `I asked Codex to get me hired at OpenAI.`

## Layer 2: Case File

Purpose:

- Give OpenAI people a clean path from premise to proof.

Artifacts:

- `CASE_FILE.md`
- `APPLICATION.md`
- `PROJECT_LIFECYCLE.md`

Rules:

- Written for a busy product or engineering leader.
- Shows decisions, taste, constraints, and outcomes.
- Links to evidence instead of dumping evidence inline.

## Layer 3: Evidence Ledger

Purpose:

- Let serious readers verify what happened.

Artifacts:

- `ARTIFACT_LEDGER.md`
- `RECEIPTS.md`
- `evidence/`
- git commits

Rules:

- Every major claim gets a receipt.
- Every receipt states Codex role and human role.
- Evidence should be specific enough to inspect.

## Layer 4: Source Material

Purpose:

- Preserve raw material so useful moments are not lost.

Artifacts:

- `source-material/private/`
- local Codex JSONL logs under `~/.codex/sessions`

Rules:

- Ignored by git.
- Never published raw.
- Reviewed and distilled into `evidence/`, `RECEIPTS.md`, or `BUILD_LOG.md`.

## Capture Commands

Capture latest Codex session for this repo as private source material:

```bash
make capture-source
```

Draft a public transcript only after review:

```bash
make capture-public
```

## Receipt Format

```text
Claim:
Why it matters:
Evidence:
Human role:
Codex role:
Outcome:
Public artifact:
Source material:
```

## What Never Goes Public Raw

- secrets,
- credentials,
- unrelated client work,
- private account data,
- private personal details,
- huge tool dumps,
- system/developer instruction noise,
- anything that makes the project harder to understand.
