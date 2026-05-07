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

## 2026-05-06 - Role Surface Recheck

- Decisions: Add `evidence/role-surface-recheck-2026-05-06.md` after checking the official OpenAI Codex careers search and primary AI Deployment Engineer - Codex page.
- Decisions: Update `OPENAI_FIT.md` and `launch/role-routing.md` to current-as-of 2026-05-06.
- Learnings: Official OpenAI search still showed 23 Codex-related jobs and the primary submitted role still had an apply link.
- Refactor backlog: Re-check role pages again only before sending a role-specific adjacent application or if OpenAI changes the careers surface.
- Reliability backlog: Do not treat role availability as hiring progress; it only validates routing.
- Next session: Execute warm-intro or second-wave outreach only after real inbox/social checks; otherwise wait for user-provided signal.

## 2026-05-06 - Application Confirmation Mail Check

- Decisions: Use local Apple Mail search as the fallback evidence source because the Gmail connector still returned an expired-token error and no connector re-auth command was exposed in the current tool surface.
- Decisions: Add `evidence/application-confirmation-2026-05-06.md` and update the tracker, case file, application, receipts, README, evidence index, build log, and memory.
- Learnings: Local Mail verified one OpenAI application receipt from `OpenAI Hiring Team` in `noahkuhn@gmail.com`, dated 2026-05-03, subject `Thank you for applying to OpenAI`.
- Refactor backlog: Reconnect Gmail connector auth if connector-based mailbox access is needed again.
- Reliability backlog: Do not treat the application receipt as recruiter interest, warm signal, interview progress, or an offer.
- Next session: Check LinkedIn, X, and DMs directly before executing second-wave outreach; use warm-intro routing first if a credible route appears.

## 2026-05-06 - Signal Sweep

- Decisions: Record the fresh signal sweep inside `launch/follow-up-tracker.md` instead of creating another standalone evidence file.
- Decisions: Treat GitHub clone/referrer movement as measurable attention, not hiring progress.
- Learnings: Local Mail still showed no visible OpenAI recruiter reply beyond the 2026-05-03 application receipt; public search still did not locate owned X/LinkedIn post URLs; GitHub clones rose to 164 total and 67 unique cloners, with 81 clones from 30 uniques on 2026-05-05.
- Refactor backlog: Add exact X/LinkedIn URLs and DM notes when they are available from logged-in surfaces.
- Reliability backlog: Do not infer OpenAI interest from `t.co` or clone traffic without identity or reply evidence.
- Next session: If no warm route or reply is found on direct social/DM checks, use the warm-intro brief before the gated second-wave packet.

## 2026-05-06 - X Launch Post Capture

- Decisions: Add `evidence/x-launch-post-2026-05-06.md` and link the captured X post from the tracker, case file, application, README, receipts, evidence index, build log, and memory.
- Decisions: Treat the X post as a verified distribution receipt, but not as verified OpenAI readership or hiring progress.
- Learnings: Public X payload exposed pinned tweet `2050930949928452494`, created 2026-05-03 13:30:17 UTC, linking the repo and GitHub Pages site with counters of 2 replies, 0 reposts, 0 quotes, 2 likes, and 3 bookmarks.
- Refactor backlog: Capture LinkedIn post URL and DM notes from logged-in surfaces.
- Reliability backlog: Do not overread `t.co` traffic or X counters as OpenAI-specific signal.
- Next session: Use warm-intro routing before broader second-wave notes if no direct reply is found.

## 2026-05-06 - Public Attention Path Check

- Decisions: Record the X reply visibility and GitHub popular-path check inside `launch/follow-up-tracker.md`.
- Decisions: Treat path traffic as public attention only, not OpenAI-specific signal.
- Learnings: Logged-out X payload did not expose the two replies as separate reply text or authors; GitHub popular paths showed `APPLICATION.md` with 19 views from 3 uniques and `launch/x-thread-draft.md` with 16 views from 3 uniques.
- Refactor backlog: Capture reply authors, LinkedIn post URL, and DM notes only from logged-in surfaces with explicit approval.
- Reliability backlog: Do not infer identity or hiring interest from GitHub path traffic.
- Next session: If no logged-in social/DM signal is available, use the warm-intro brief before broader second-wave notes.

## 2026-05-06 - Current Codex Hook Refresh

- Decisions: Update `launch/warm-intro-brief.md`, `launch/second-wave-packet.md`, and `launch/follow-up-tracker.md` around OpenAI's current Codex positioning.
- Decisions: Use the 2026-04-16 `Codex for (almost) everything` release as the public timing hook, while avoiding any claim of OpenAI endorsement or hiring progress.
- Learnings: The audition's friction maps directly to the current Codex surface: connected tools, computer use, memory, proactive continuation, current-state tracking, and longer-running workflow follow-through.
- Refactor backlog: If OpenAI publishes a newer Codex release or role-surface change, refresh the hook before sending a second wave.
- Reliability backlog: Keep the hook grounded in observed workflow evidence and official public OpenAI language.
- Next session: Use this hook only after direct reply checks or when a credible warm route asks what to forward.

## 2026-05-06 - Warm Routing Shortlist

- Decisions: Add `launch/warm-routing-shortlist.md` and link it from README, warm-intro brief, second-wave packet, and follow-up tracker.
- Decisions: Base the routing map on official OpenAI Codex release, Academy, and careers surfaces checked on 2026-05-06.
- Learnings: Official Codex careers search showed 22 Codex roles; the best routing lanes are Codex Technical Success, Codex App workflow UX, Codex Core Agent feedback loops, data/product measurement, and plugins/skills/ecosystem.
- Refactor backlog: Refresh this shortlist if OpenAI role surfaces or Codex public positioning changes before outreach.
- Reliability backlog: Use this as a lane map, not as proof of OpenAI interest or permission to spray unrelated employees.
- Next session: Ask for a specific warm route using this map only after direct reply checks or explicit approval.

## 2026-05-07 - Gmail Auth Boundary And Mail Correction

- Decisions: Treat Gmail connector auth as a user-side reconnect blocker because the available Gmail tools still return `token_expired` and expose no OAuth reconnect command.
- Decisions: Record the auth boundary and local Mail fallback findings in `launch/follow-up-tracker.md`.
- Learnings: Apple Mail automation confirmed the current 2026-05-03 application receipt from `OpenAI Hiring Team <no-reply@openai.com>`.
- Learnings: `OpenAI Application Update for Noah Kuhn` from 2026-01-07 was an old rejection for `Software Engineer, Full Stack (People Innovation)`, not a decision on the current Codex application.
- Refactor backlog: Reconnect Gmail from the user-side connector UI before relying on Gmail tools again.
- Reliability backlog: Do not conflate old OpenAI application updates with the current Codex application state.
- Next session: Continue from the real current state: application received, X post captured, LinkedIn/DM details uncaptured, no verified recruiter/warm/interview/offer signal.

## 2026-05-07 - Follow-Up Post Draft

- Decisions: Add `launch/follow-up-post-draft.md` as the standalone public follow-up asset and link it from README, the follow-up tracker, and the second-wave packet.
- Decisions: Gate the post on logged-in response checks, a warm-route request, or Noah explicitly choosing to post before full private surface capture.
- Learnings: The strongest follow-up frame is that Codex handled file-backed artifact work but drifted when application, social, DM, inbox, and response state changed.
- Refactor backlog: If the post is published, add the final public URL and counters to the follow-up tracker.
- Reliability backlog: Do not present the draft as sent, and do not imply OpenAI has seen it.
- Next session: Publish or adapt the draft only if no warmer direct route appears first.

## 2026-05-07 - Public GitHub Signal Check

- Decisions: Record the fresh GitHub traffic check in `launch/follow-up-tracker.md` without treating it as hiring movement.
- Learnings: Repo status stayed at 0 stars, 0 watchers, 0 forks, and 0 open issues; views stayed 48 total from 5 uniques; clones rose to 361 total from 135 unique cloners, including 197 clones from 72 unique cloners on 2026-05-06.
- Learnings: Referrers stayed `noahkuhn.github.io` and `t.co`, and popular paths stayed concentrated on `APPLICATION.md`, `launch/x-thread-draft.md`, `RECEIPTS.md`, `/launch`, and repo overview.
- Refactor backlog: If GitHub identity, stars, issues, or external replies appear, capture them separately from aggregate traffic.
- Reliability backlog: Do not infer OpenAI interest from aggregate clone growth.
- Next session: Continue only with real response-surface evidence, a specific warm route, or approval to publish/send the prepared follow-up.

## 2026-05-07 - Homepage Current-Action Update

- Decisions: Update `index.html` so the current-state proof stack links to `launch/follow-up-post-draft.html` and labels it prepared, not published or sent.
- Decisions: Change the homepage case-panel next step to warm route or follow-up.
- Learnings: The live homepage had fallen slightly behind the README/tracker path; it still surfaced older follow-up material but not the new draft.
- Refactor backlog: If the follow-up draft is published, replace prepared-state language with the final public URL and counters.
- Reliability backlog: Keep the homepage from implying outreach happened before Noah approves or performs it.
- Next session: Use the homepage as the public front door only after verifying it still matches the live tracker state.

## 2026-05-07 - Role Surface Refresh

- Decisions: Add `evidence/role-surface-refresh-2026-05-07.md` and update role/routing docs to current official OpenAI Careers state.
- Decisions: Keep AI Deployment Engineer - Codex as the live primary routing lane and Codex App as the strongest adjacent workflow-UX lane.
- Learnings: Official OpenAI Careers search showed 23 Codex jobs out of 659 total jobs; AI Deployment Engineer - Codex and Frontend Software Engineer, Codex App both still had apply links.
- Refactor backlog: Refresh role surfaces again only before applying to a new adjacent role or publishing role-specific claims.
- Reliability backlog: Do not treat role availability as OpenAI interest or hiring progress.
- Next session: Use the refreshed facts only for warm routing or an approved follow-up.
