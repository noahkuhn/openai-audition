# Memory

## 2026-05-01 - OpenAI Audition Scaffold

- Decisions: Create a fresh Labs repo for the public audition instead of extending Argus, Brain, or another existing project.
- Decisions: The campaign title is "I Asked Codex To Get Me Hired At OpenAI."
- Decisions: The process is the product; the repo should preserve planning, scoring, rejected ideas, prompts, build logs, receipts, and the final application.
- Learnings: Existing projects can be proof-object candidates, but the main angle must stay legible to normal people and OpenAI builders.
- Refactor backlog: Add a lightweight generator only after the static public artifact is useful.
- Reliability backlog: Keep claims evidence-backed; do not fake autonomy, metrics, OpenAI endorsement, or outcomes.
- Next session: Move from scaffold to public launch assets: homepage copy, X launch thread, and first video outline.

## 2026-05-01 - Lifecycle-First Evidence Architecture

- Decisions: Center the repo around `CASE_FILE.md`, `PROJECT_LIFECYCLE.md`, and `ARTIFACT_LEDGER.md` instead of raw transcript storage.
- Decisions: Capture raw Codex sessions from `~/.codex/sessions` into ignored `source-material/private/` markdown exports.
- Decisions: Use `evidence/` only for reviewed excerpts and proof artifacts that strengthen the public audition.
- Decisions: Add `make capture-source` and `make capture-public` as operator commands.
- Learnings: The attention asset is the public story; transcripts and commits are supporting proof.
- Learnings: OpenAI due diligence needs a clean case file, not a dump of chats.
- Refactor backlog: Add a summarizer later if raw transcripts become too long to review manually.
- Reliability backlog: Review every public evidence artifact for secrets, personal data, noisy tool output, and unrelated private context before committing.
- Next session: Fill the case file, launch thread, and video outline.

## 2026-05-02 - Public Launch Package

- Decisions: Upgrade the root homepage from scaffold to the first-click attention surface.
- Decisions: Make `CASE_FILE.md` the OpenAI due-diligence entry point and update it with current proof.
- Decisions: Add receipts for the initial scaffold, lifecycle evidence architecture, and launch-package pass.
- Decisions: Add the first curated public decision record under `evidence/`.
- Learnings: The launch path is layered: X gets the story, the site gets the click, the case file gets OpenAI, and evidence gets serious readers.
- Refactor backlog: Add a deploy target once hosting is chosen.
- Reliability backlog: Add one more curated excerpt from the repo-setup/build session before public launch.
- Next session: Deploy the static site and create the first launch video asset.
