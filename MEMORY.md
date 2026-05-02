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

## 2026-05-02 - Recentered On OpenAI Conversation

- Decisions: Add `OPENAI_FIT.md` so the campaign targets current Codex role surfaces instead of vague OpenAI attention.
- Decisions: Add `launch/openai-outreach.md` to convert the public artifact into applications, direct pings, and a 48-hour checkpoint.
- Decisions: Keep proof-object work deferred until public or OpenAI feedback demands deeper technical evidence.
- Learnings: Repo polish is only useful when it increases attention, credibility, or conversion to an OpenAI conversation.
- Learnings: Noah's correction that Codex was overbuilding is itself useful process evidence.
- Refactor backlog: Replace launch placeholders once public site, repo, X, LinkedIn, and primary role URLs are chosen.
- Reliability backlog: Re-check OpenAI Careers before publishing any role-specific public claims.
- Next session: Publish, apply to the strongest Codex role, and send direct outreach.

## 2026-05-02 - Contact And Primary Role Inputs

- Decisions: Treat AI Deployment Engineer - Codex as the first application target after verifying the live OpenAI Careers page.
- Decisions: Use `https://noahkuhn.com/openai/` as prior OpenAI application context, not as the new public audition URL.
- Decisions: Fill known identity/contact inputs: X `@noahbkuhn`, LinkedIn `https://www.linkedin.com/in/noahkuhn`, email `hey@noahkuhn.com`.
- Learnings: The deployment role maps strongly because it asks for Codex power usage, workflow adoption, demos, technical enablement, public guidance, and product feedback.
- Refactor backlog: Replace deployed audition URL and public GitHub repo URL once hosting/repo are created.
- Reliability backlog: Do not push or publish the repo with contact details until Noah confirms the public destination.
- Next session: Create/push the GitHub repo and deploy the static site after explicit confirmation.
