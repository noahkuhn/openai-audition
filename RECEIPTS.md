# Receipts

Receipts are the evidence trail.

They should show:

- What Noah asked.
- What Codex recommended.
- What was built.
- What was rejected.
- What changed because of human judgment.
- What shipped.

## Receipt 000 - Planning Chat

Date: 2026-05-01

Type: Codex planning session

Summary:

- Noah asked Codex how to get hired by OpenAI through a viral project.
- Codex proposed several directions, including public agent systems, real-world Codex task benchmarks, and proof-of-work applications.
- Noah sharpened the premise: the valuable marketing angle is that a human asks Codex to get him hired by OpenAI, and the process itself becomes the proof.
- The final direction became a new repo and public artifact, not a continuation of any existing app.

Human intervention:

- Rejected over-anchoring on Argus or crypto.
- Reframed the goal around public attention and hiring signal.
- Clarified that this chat is the planning lane and the new repo starts with work already in motion.

Artifact created:

- This repo scaffold.

Public artifact:

- [evidence/decision-record-001-public-audition.md](evidence/decision-record-001-public-audition.md)

## Receipt 001 - Initial Repo Scaffold

Date: 2026-05-01

Type: Git commit

Claim:

- Codex helped create the public audition repo as the first concrete artifact.

Why it matters:

- The project needed to become inspectable instead of remaining a private planning chat.

Evidence:

- Commit `4ec87e2` - `Initial public audition scaffold`
- Files created: `README.md`, `MISSION.md`, `SCORECARD.md`, `CANDIDATES.md`, `BUILD_LOG.md`, `RECEIPTS.md`, `APPLICATION.md`, `site/index.html`

Human role:

- Noah set the premise and corrected that existing projects should not become the default angle.

Codex role:

- Codex structured the initial repo and drafted the first public artifacts.

Outcome:

- A clean Labs repo existed with the public premise and first static site.

Public artifact:

- [README.md](README.md)
- [index.html](index.html)

## Receipt 002 - Lifecycle-First Evidence Architecture

Date: 2026-05-01

Type: Git commit

Claim:

- The repo was corrected from transcript capture toward a lifecycle-first public evidence model.

Why it matters:

- The project does not win by dumping chat logs. It wins by moving from viral hook to clean OpenAI due diligence.

Evidence:

- Commit `46ab3ed` - `Add lifecycle-first evidence architecture`
- Files created in that pass included `CASE_FILE.md`, lifecycle/evidence planning docs, `launch/x-thread-draft.md`, and `launch/video-outline.md`.
- Later pruning removed the extra planning docs from the public launch path.

Human role:

- Noah rejected the low-level transcript-storage framing and clarified the project lifecycle.

Codex role:

- Codex reorganized the repo around attention, case file, evidence, and private source material.

Outcome:

- The repo now separates public story, OpenAI case file, proof artifacts, and raw private source material.

Public artifact:

- [CASE_FILE.md](CASE_FILE.md)
- [evidence/decision-record-001-public-audition.md](evidence/decision-record-001-public-audition.md)

## Receipt 003 - Public Launch Package

Date: 2026-05-02

Type: Site and launch artifact update

Claim:

- The repo moved from scaffold to a launch-ready public draft.

Why it matters:

- The attention layer needs to be coherent before any deeper proof object is selected.

Evidence:

- Homepage updated to route readers through hook, case file, lifecycle, and evidence.
- Case file updated with current status and evidence links.
- Launch assets tightened around X thread and short-video flow.
- First curated decision record added under `evidence/`.

Human role:

- Noah pushed for the actual lifecycle: OpenAI knows nothing, the project must become interesting, and historical artifacts must be useful once OpenAI inspects.

Codex role:

- Codex translated that correction into the public artifact structure and launch path.

Outcome:

- The project now has a usable first-click surface plus a due-diligence path.

Public artifact:

- [index.html](index.html)
- [launch/x-thread-draft.md](launch/x-thread-draft.md)
- [launch/video-outline.md](launch/video-outline.md)
- [evidence/decision-record-001-public-audition.md](evidence/decision-record-001-public-audition.md)

## Receipt 004 - Recentered On Getting The OpenAI Conversation

Date: 2026-05-02

Type: Strategy correction and repo update

Claim:

- The project was corrected from launch-readiness nitpicking back to the real objective: get Noah a job conversation at OpenAI.

Why it matters:

- The public audition only matters if it routes attention into a hiring conversation.

Evidence:

- Noah explicitly asked whether Codex was getting him the job or overbuilding.
- Codex then created a direct role-fit and outreach layer instead of adding more abstract process documentation.
- Current Codex role surfaces were checked against OpenAI Careers before adding role-specific positioning.

Human role:

- Noah forced the priority correction and restated the objective.

Codex role:

- Codex translated the correction into `OPENAI_FIT.md`, `launch/openai-outreach.md`, and updated public-facing artifacts.

Outcome:

- The repo now has a clear conversion path: public hook -> case file -> role fit -> direct outreach -> OpenAI conversation.

Public artifact:

- [OPENAI_FIT.md](OPENAI_FIT.md)
- [launch/openai-outreach.md](launch/openai-outreach.md)
- [evidence/correction-002-overbuilding.md](evidence/correction-002-overbuilding.md)

## Receipt 005 - Primary Role And Contact Inputs

Date: 2026-05-02

Type: Launch input update

Claim:

- The audition now has a concrete first role target and contact layer.

Why it matters:

- The campaign cannot convert without a specific role, public contact path, and route from attention to application.

Evidence:

- Noah provided X, LinkedIn, email, a previous OpenAI application page, and the AI Deployment Engineer - Codex role link.
- Codex verified the role page on OpenAI Careers before treating it as the primary target.

Human role:

- Noah supplied the public identity and likely role target.

Codex role:

- Codex mapped the role to the campaign and updated the case file, application, fit document, outreach plan, launch copy, and public homepage.

Outcome:

- The role and contact inputs were filled; public repo and deployed audition URLs were added later in Receipt 006.

Public artifact:

- [OPENAI_FIT.md](OPENAI_FIT.md)
- [APPLICATION.md](APPLICATION.md)
- [launch/openai-outreach.md](launch/openai-outreach.md)

## Receipt 006 - Public Repo And Site Published

Date: 2026-05-02

Type: Public launch infrastructure

Claim:

- The audition moved from local repo to public artifact.

Why it matters:

- The campaign only works if OpenAI people and builders can inspect it without private access.

Evidence:

- Public GitHub repo: <https://github.com/noahkuhn/openai-audition>
- Public GitHub Pages site: <https://noahkuhn.github.io/openai-audition/>
- GitHub Pages built successfully from `main`.
- Commit history was authored as `Noah Kuhn <1133909+noahkuhn@users.noreply.github.com>` before first push.

Human role:

- Noah specified that the repo must be separate and use the `noahkuhn` GitHub identity.

Codex role:

- Codex authenticated the `noahkuhn` GitHub account, rewrote unpublished local authorship, created the public repo, pushed `main`, enabled Pages, and verified the site returned HTTP 200.

Outcome:

- The repo and site are live public surfaces for launch and outreach.

## Receipt 007 - Launch Readiness Review Integrated

Date: 2026-05-02

Type: Public readiness review

Claim:

- The repo was reviewed and hardened for eyebrow-raising public launch, not just basic correctness.

Why it matters:

- The project depends on first-impression credibility. Stale placeholders, raw Markdown links, duplicate launch copy, and summary-only evidence would weaken the signal.

Evidence:

- Narrative review recommended leading with "career-changing objective" and "real pressure."
- Readiness review identified raw Markdown links, stale publish language, duplicate launch-thread files, and shallow evidence depth.
- Codex integrated those findings into the homepage, README, case file, application, launch thread, outreach copy, and evidence folder.

Human role:

- Noah asked Codex not to stop until the project was strong enough to raise an eyebrow.

Codex role:

- Codex delegated narrative and readiness review, integrated findings, and verified the resulting public surfaces.

Outcome:

- The launch package now has a sharper first-click story, canonical launch thread, rendered-document links, and additional curated evidence artifacts.

Public artifact:

- [evidence/subagent-review-2026-05-02.md](evidence/subagent-review-2026-05-02.md)
- [evidence/launch-surface-2026-05-02.md](evidence/launch-surface-2026-05-02.md)

## Receipt 008 - Share Image And Review-Packet Redesign

Date: 2026-05-03

Type: Design direction and public site update

Claim:

- The public site was redesigned away from a generic landing page and toward an active case file.

Why it matters:

- The first click has to make an OpenAI/Codex person pause before they read the deeper repo. The design now foregrounds objective, drift, correction, and receipts.

Evidence:

- Five subagent directions were saved in [evidence/design-directions-2026-05-03.md](evidence/design-directions-2026-05-03.md).
- The real Codex screenshot base image is saved at [assets/og/codex-instance-base.png](assets/og/codex-instance-base.png).
- The final Open Graph image is saved at [assets/og/openai-audition-og-codex.png](assets/og/openai-audition-og-codex.png).
- The homepage now declares `summary_large_image` metadata and routes Open Graph/Twitter previews to the 1200x630 PNG.

Human role:

- Noah identified that the previous page looked too generic and asked for a stronger share image and design pass.

Codex role:

- Codex created the first image asset, collected the design directions, chose the convergent review-packet direction, updated the homepage, and preserved the decision trail. Receipt 009 records Noah's correction that the final image needed to show a real Codex instance.

Outcome:

- The public site now presents the audition as inspectable human-agent work instead of a standard portfolio page.

## Receipt 009 - Synthetic Image Replaced With Actual Codex Instance

Date: 2026-05-03

Type: Human correction and public asset update

Claim:

- The share image and hero background now use a real Codex instance instead of a generated scene.

Why it matters:

- The audition depends on inspectable reality. A synthetic laptop/case-file image looked polished, but it weakened the claim by making the public surface feel staged.

Evidence:

- Noah provided an actual Codex Desktop screenshot from the running audition session.
- The homepage hero background now uses [assets/og/codex-instance-base.png](assets/og/codex-instance-base.png).
- Open Graph and Twitter metadata now point to [assets/og/openai-audition-og-codex.png](assets/og/openai-audition-og-codex.png).
- The earlier generated image assets were removed from the repo.

Human role:

- Noah caught the mismatch and required the image to show an actual Codex instance.

Codex role:

- Codex cropped and composed the real screenshot into the hero and OG assets, updated metadata, and removed the synthetic image files.

Outcome:

- The public share image is now aligned with the premise: this is a live Codex audition, not a staged AI-themed graphic.

Public artifact:

- <https://github.com/noahkuhn/openai-audition>
- <https://noahkuhn.github.io/openai-audition/>

## Receipt 010 - Live Launch Surface And Role Verification

Date: 2026-05-05

Type: Launch verification and evidence hygiene

Claim:

- The public audition surfaces and primary OpenAI Codex role target were re-checked before further launch/outreach.

Why it matters:

- The project cannot route attention into a hiring conversation if public links, share metadata, or role-specific claims are stale.

Evidence:

- GitHub Pages returned HTTP 200 for <https://noahkuhn.github.io/openai-audition/>.
- The Open Graph PNG returned HTTP 200 with `content-type: image/png`.
- The public GitHub repo returned HTTP 200.
- OpenAI Careers still listed AI Deployment Engineer - Codex as an applyable role and showed multiple current Codex role surfaces.
- The audit found and fixed stale case-file commit coverage and duplicate receipt numbering.

Human role:

- Noah's standing instruction is that the process is the point, but claims must stay honest and verifiable.

Codex role:

- Codex verified the live public surfaces, checked the official OpenAI role pages, updated the case file and receipts, and added a concise public verification artifact.

Outcome:

- The public case file now reflects the actual launch state instead of stopping at older commits or carrying duplicate receipt numbers.

Public artifact:

- [evidence/live-launch-verification-2026-05-05.md](evidence/live-launch-verification-2026-05-05.md)

## Receipt 011 - Post-Application Distribution State

Date: 2026-05-05

Type: User-reported distribution update

Claim:

- The project has moved past launch preparation into active application and outreach.

Why it matters:

- Repeating the initial launch checklist would waste the moment. The next useful work is response tracking, warm follow-up, and deciding whether the market wants a deeper proof artifact.

Evidence:

- Noah reported that he already applied.
- Noah reported that he already sent two DMs.
- Noah reported that he already published one LinkedIn post.
- Noah reported that he already posted an X thread for the original project.
- Public URLs, application confirmation, and DM recipient details have not yet been captured in this repo.

Human role:

- Noah executed the actual distribution and corrected Codex when it started from stale next steps.

Codex role:

- Codex updated the repo state and next-step plan so future work starts from the actual post-application status.

Outcome:

- The repo now treats application/outreach as started and shifts the next action to follow-up tracking.

Public artifact:

- [evidence/post-application-distribution-2026-05-05.md](evidence/post-application-distribution-2026-05-05.md)
- [launch/follow-up-tracker.md](launch/follow-up-tracker.md)

## Receipt 012 - Narrow Signal Check

Date: 2026-05-05

Type: Response tracking check

Claim:

- No verified warm signal has been captured in the repo yet, but the check is not comprehensive.

Why it matters:

- The next move should depend on real response signal. A narrow no-hit check should not be mistaken for proof that the application or outreach failed.

Evidence:

- Connected Gmail account `noah@pilotmade.com` had no relevant OpenAI/Ashby/Codex application response in the searches performed.
- The application artifacts list `hey@noahkuhn.com`, so the Gmail check may not cover the actual application inbox.
- GitHub public counters showed 0 stars, 0 watchers, 0 forks, 0 issues, and 0 pull requests.
- GitHub traffic API showed historical traffic in the available window, concentrated on 2026-05-02 and 2026-05-03, but did not yet show current-day 2026-05-05 traffic.

Human role:

- Noah provided the corrected current distribution state.

Codex role:

- Codex checked the accessible inbox and GitHub signal surfaces, then recorded the limits instead of overclaiming.

Outcome:

- The follow-up tracker now distinguishes "no verified signal captured" from "no signal exists."

Public artifact:

- [launch/follow-up-tracker.md](launch/follow-up-tracker.md)

## Receipt 013 - Contact Surface Availability Check

Date: 2026-05-05

Type: Evidence-capture boundary check

Claim:

- The remaining first-wave proof gap is access to the actual application/contact/social surfaces, not another repo launch task.

Why it matters:

- The repo should not claim verified application, LinkedIn, X, or DM evidence until the specific URLs, screenshots, timestamps, or private notes are captured.

Evidence:

- Gmail alias searches for `hey@noahkuhn.com` returned no results in the connected `noah@pilotmade.com` account.
- Public search did not locate the reported X or LinkedIn post URLs.
- Direct X profile fetch confirmed <https://x.com/noahbkuhn>, but did not expose recent thread content.
- LinkedIn recent activity was not fetchable from the current runtime.

Human role:

- Noah controls the actual application confirmation, social posts, and DM surfaces.

Codex role:

- Codex checked the accessible surfaces and converted the unknowns into a capture checklist.

Outcome:

- The next step is to capture real URLs/screenshots/private notes or wait for signal, not to repeat application or launch.

Public artifact:

- [launch/follow-up-tracker.md](launch/follow-up-tracker.md)
- [evidence/post-application-distribution-2026-05-05.md](evidence/post-application-distribution-2026-05-05.md)

## Receipt Template

```text
Receipt:
Date:
Type:

Claim:
Evidence:
Human role:
Codex role:
Outcome:
Link or file:
```
