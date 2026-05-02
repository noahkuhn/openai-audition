# I Asked Codex To Get Me Hired At OpenAI

This repo is a public audition.

The premise is simple:

> A human gave Codex a life-level objective, not a coding task: get me hired at OpenAI.
>
> Codex turned that objective into a public proof-of-work campaign.

This is not a resume generator. It is not a cover letter. It is not a generic AI app.

The process is the point, but the process has to be packaged cleanly.

Strangers should see a simple story. OpenAI people should find a clean case file. Builders should be able to inspect the evidence.

## Current Status

This started before the repo existed.

Session 0 was a planning conversation with Codex on 2026-05-01. The decision from that conversation:

- The viral hook is `I asked Codex to get me hired at OpenAI`.
- The product is the public audition process itself.
- The first repo exists to make that process legible, inspectable, and shareable.
- The proof object can evolve, but the public artifact starts now.

## Why This Exists

OpenAI is pushing Codex toward long-running work, memory, computer use, connected tools, approvals, and agents that operate across a full workflow.

This repo asks a sharper question:

> Can Codex help a person convert ambition into a body of work compelling enough to change their career?

If yes, the application is not a PDF. The application is the trail.

## Repo Map

- [CASE_FILE.md](CASE_FILE.md) - the first file an OpenAI person should read.
- [OPENAI_FIT.md](OPENAI_FIT.md) - the target role fit and current OpenAI Codex role surfaces.
- [PROJECT_LIFECYCLE.md](PROJECT_LIFECYCLE.md) - how the project moves from unknown to viral to due diligence.
- [ARTIFACT_LEDGER.md](ARTIFACT_LEDGER.md) - the index of public surfaces, proof artifacts, and source material.
- [MISSION.md](MISSION.md) - the rules and objective.
- [SCORECARD.md](SCORECARD.md) - how candidate projects are judged.
- [CANDIDATES.md](CANDIDATES.md) - possible proof objects and current scoring.
- [BUILD_LOG.md](BUILD_LOG.md) - chronological public build record.
- [RECEIPTS.md](RECEIPTS.md) - evidence that work happened and what Codex did.
- [EVIDENCE_PROTOCOL.md](EVIDENCE_PROTOCOL.md) - how raw source material becomes clean public proof.
- [APPLICATION.md](APPLICATION.md) - the final OpenAI-facing pitch as it evolves.
- [auditions/openai](auditions/openai) - the OpenAI-specific audition lane.
- [launch](launch) - public launch and outreach assets.
- [evidence](evidence) - curated evidence safe for public readers.
- [source-material](source-material) - raw/private source capture rules.
- [prompts](prompts) - prompt artifacts worth publishing.
- [index.html](index.html) - static public homepage.
- [site](site) - site assets.

## Operating Rule

Every artifact should answer one question:

> Would this make someone at OpenAI think, "This person understands what Codex is becoming"?

If not, cut it.

## Local Preview

The site is static. Open [index.html](index.html) in a browser.

## Launch Inputs

The only missing launch inputs are:

```text
PUBLIC_SITE_URL=https://noahkuhn.github.io/openai-audition/
PUBLIC_REPO_URL=https://github.com/noahkuhn/openai-audition
NOAH_X_HANDLE=@noahbkuhn
NOAH_LINKEDIN_URL=https://www.linkedin.com/in/noahkuhn
NOAH_EMAIL=hey@noahkuhn.com
PRIMARY_ROLE_URL=https://openai.com/careers/ai-deployment-engineer-codex-remote-us/
PRIOR_OPENAI_SITE_URL=https://noahkuhn.com/openai/
```

Everything else should keep moving without waiting.

## Session Capture

Codex Desktop stores raw session logs locally under `~/.codex/sessions`.

Capture the latest session for this repo as private source material:

```bash
make capture-source
```

Create a public transcript draft only after review:

```bash
make capture-public
```
