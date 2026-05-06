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

## 2026-05-02 - Launch Readiness Hardening

- Decisions: Use `launch/x-thread-draft.md` as the canonical launch thread and keep `auditions/openai/launch-thread.md` as a pointer to avoid drift.
- Decisions: Route homepage proof links to GitHub-rendered documents instead of raw Markdown served by GitHub Pages.
- Decisions: Add curated evidence for the overbuilding correction, subagent launch review, and launch-surface hardening.
- Learnings: The stronger framing is a user-side Codex evaluation under real pressure, not a generic public audition category.
- Learnings: Evidence claims need concrete public artifacts; summary-only receipts are not enough for serious readers.
- Refactor backlog: Add a short launch video or screenshot-based proof artifact next.
- Reliability backlog: Re-run public link and Pages checks after pushing these hardening changes.
- Next session: Launch distribution and direct routing to OpenAI/Codex people.

## 2026-05-03 - Public Repo Pruning

- Decisions: Remove duplicated `auditions/openai` lane, lifecycle/artifact/protocol scaffolding, source-capture tooling, and extra prompt templates from the public repo.
- Decisions: Keep the public path focused on homepage, README, case file, OpenAI fit, application, build log, receipts, evidence, and launch/outreach copy.
- Learnings: "Process is the point" does not mean every internal process artifact belongs in the public first impression.
- Learnings: The repo should feel like a sharp public case file, not a miniature project-management system.
- Refactor backlog: Reassess whether `MEMORY.md` should stay tracked after launch if it starts adding noise.
- Reliability backlog: Verify no live links point to removed files before pushing.
- Next session: Launch distribution using the canonical thread.

## 2026-05-03 - OG Image And Review Packet Redesign

- Decisions: The initial pass used a generated desk/case-file bitmap for the hero and Open Graph asset; this was superseded by the real Codex image correction below.
- Decisions: Use deterministic text composition for the Open Graph card so X shares have crisp readable copy.
- Decisions: Save the five subagent design directions in `evidence/design-directions-2026-05-03.md`.
- Decisions: Redesign the homepage around the shared case-file/review-packet direction and move the human correction moment above general OpenAI fit copy.
- Learnings: The design directions independently converged on the same point: the page must show objective, drift, correction, and receipts immediately.
- Refactor backlog: If the homepage gets another pass, consider adding real cropped screenshots of receipts or build-log excerpts as evidence thumbnails.
- Reliability backlog: Verify GitHub Pages serves the PNG and the `summary_large_image` metadata after push.
- Next session: Launch and route the redesigned page to targeted Codex/OpenAI people.

## 2026-05-03 - Real Codex Image Correction

- Decisions: Replace the generated desk/laptop imagery with Noah's actual Codex Desktop screenshot.
- Decisions: Use new cache-busting asset names: `codex-instance-base.png` for the hero and `openai-audition-og-codex.png` for Open Graph/Twitter.
- Decisions: Remove the old generated OG and base images so the repo no longer carries the fake visual source.
- Learnings: For this audition, actual process evidence beats polished synthetic imagery.
- Refactor backlog: Consider using real screenshot thumbnails elsewhere if they strengthen evidence without making the page noisy.
- Reliability backlog: Verify the new live image URL returns 200 after GitHub Pages rebuilds.
- Next session: Launch with the actual-Codex image, not the generated one.

## 2026-05-05 - Live Evidence Audit

- Decisions: Treat launch verification as public evidence and add `evidence/live-launch-verification-2026-05-05.md`.
- Decisions: Update `CASE_FILE.md` so OpenAI due-diligence readers see the current public repo/site status, latest meaningful commits, and full receipt sequence.
- Decisions: Fix duplicate `Receipt 007` numbering and add a live verification receipt before distribution.
- Learnings: The repo was live, the OG image returned 200 as PNG, the public repo returned 200, and the primary OpenAI Codex role page was still live with an apply link on 2026-05-05.
- Refactor backlog: None for this pass; avoid adding more scaffolding before outreach.
- Reliability backlog: Re-check OpenAI Careers immediately before submitting the actual application because role pages can change.
- Next session: Publish the X thread, apply, and send targeted direct notes using `launch/openai-outreach.md`.

## 2026-05-05 - Post-Application State Correction

- Decisions: Treat application and first-wave distribution as already started based on Noah's update.
- Decisions: Add `launch/follow-up-tracker.md` and `evidence/post-application-distribution-2026-05-05.md` so next work starts from response tracking.
- Learnings: Noah reported he already applied, sent two DMs, published one LinkedIn post, and posted an X thread for the original project.
- Refactor backlog: Replace this user-reported state with exact links/timestamps if Noah supplies them.
- Reliability backlog: Do not claim public verification for the application, DMs, LinkedIn post, or X thread until receipts are captured.
- Next session: Check replies/signals and decide whether to send a targeted second wave or produce one follow-up artifact.

## 2026-05-05 - Narrow Signal Check

- Decisions: Search the connected Gmail account and GitHub public signal surfaces before deciding on second-wave outreach.
- Learnings: Connected Gmail is `noah@pilotmade.com`, while public application/contact docs use `hey@noahkuhn.com`; no OpenAI/Ashby/Codex response was found in the connected mailbox, but that is not comprehensive.
- Learnings: GitHub showed 0 stars/watchers/forks/issues/PRs, with historical traffic concentrated on 2026-05-02 and 2026-05-03.
- Refactor backlog: Add real public post URLs or private recipient notes only if Noah wants them recorded.
- Reliability backlog: Do not interpret the narrow no-hit check as evidence that the outreach failed.
- Next session: Check the actual contact inbox plus LinkedIn/X/DMs before sending a second wave.

## 2026-05-05 - Contact Surface Availability

- Decisions: Treat inaccessible application/social proof as a capture gap, not as a reason to redo launch.
- Learnings: `hey@noahkuhn.com` did not appear in the connected Gmail account searches; public search did not locate the reported X/LinkedIn post URLs; X profile fetch confirmed `@noahbkuhn` but did not expose recent thread content; LinkedIn recent activity was not fetchable.
- Refactor backlog: Add application confirmation, LinkedIn URL, X thread URL, and DM notes only if Noah wants those receipts in the repo.
- Reliability backlog: Do not publish claims about responses or post performance without actual URLs/screenshots/private notes.
- Next session: Use real captured links/signals to decide whether to reply, route, or send a second wave.

## 2026-05-05 - Adjacent Role Routing

- Decisions: Add `launch/role-routing.md` so any second application is deliberate and current-role-aware.
- Decisions: Keep AI Deployment Engineer - Codex as the submitted primary; route next toward Deployed Product Manager, Codex or Codex App only if first-wave signal supports it.
- Learnings: The public audition is strongest for deployment/product/operator evidence first, human-agent UX/product engineering second, and heavier Codex infrastructure/research only if OpenAI asks for deeper technical proof.
- Refactor backlog: Re-check OpenAI Careers before using the role-routing map because listings can change.
- Reliability backlog: Do not apply broadly to every Codex role; pick one adjacent route after checking actual signal.
- Next session: Use captured signal to decide whether to reply, wait, or apply to one adjacent role.

## 2026-05-05 - Codex Product Feedback Memo

- Decisions: Add `CODEX_FEEDBACK.md` as a direct product/deployment feedback artifact, not another launch artifact.
- Decisions: Link the memo from README, case file, OpenAI fit, application, receipts, build log, and memory.
- Learnings: The strongest product signals from the audition are current-state reconciliation, evidence status, objective drift detection, social/application capture, and correction memory.
- Refactor backlog: If OpenAI asks for more depth, turn one feedback item into a concrete demo or implementation sketch.
- Reliability backlog: Keep the memo grounded in observed workflow behavior; do not claim broad benchmark results.
- Next session: Use the memo as the second-wave hook only if external signal remains weak.

## 2026-05-05 - Homepage Current-State Update

- Decisions: Update the public homepage and README to say the first application/outreach wave already happened.
- Decisions: Promote `CODEX_FEEDBACK.md` and `launch/follow-up-tracker.md` from the homepage so OpenAI readers see product feedback and active response tracking.
- Learnings: The public entrypoint can drift just like the agent; it must reconcile current state or it will keep implying stale next steps.
- Refactor backlog: After GitHub Pages deploys, visually verify the homepage on desktop and mobile.
- Reliability backlog: Keep application/social/DM proof labeled user-reported until the exact receipts are captured.
- Next session: Use the Codex feedback memo as the follow-up hook only if the first wave remains cold.

## 2026-05-06 - Second-Wave Packet

- Decisions: Add `launch/second-wave-packet.md` as the bounded no-signal follow-up packet.
- Decisions: Gate the packet on actual inbox, LinkedIn, X, and DM checks so it does not repeat completed launch work.
- Decisions: Use `CODEX_FEEDBACK.md` as the second-wave hook and stop after one credible reply/intro/recruiter response or 8 targeted notes.
- Learnings: The next distribution move should sell Codex product signal, not ask again generically.
- Refactor backlog: If the user captures the real public post URLs, add them to the follow-up tracker before sending.
- Reliability backlog: Do not execute the packet until actual response surfaces are checked.
- Next session: If signal is cold after the real check, send 6-8 targeted notes from the packet; if warm, route through the person.

## 2026-05-06 - Warm Intro Brief

- Decisions: Add `launch/warm-intro-brief.md` as the forwardable routing asset for credible OpenAI/Codex warm intros.
- Decisions: Make warm routing precede cold or semi-warm second-wave notes when a credible route exists.
- Decisions: Keep boundaries explicit: no OpenAI endorsement, no fake autonomy, no verified-response claim, and no claim that uncaptured application/social proof is publicly verified.
- Learnings: A warm forward is a stronger conversion path than another public post when the first wave is already complete.
- Refactor backlog: If a real warm route appears, record the route category and outcome in the follow-up tracker without exposing private details.
- Reliability backlog: Do not name private contacts in the public repo unless the user explicitly approves.
- Next session: Use the warm-intro brief for up to three credible routes before broader second-wave notes.
