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

## Receipt 014 - Adjacent Role Routing Map

Date: 2026-05-05

Type: Post-application routing plan

Claim:

- If the first Codex Deployment application stalls, the next move should be a deliberate adjacent route, not a broad application spray.

Why it matters:

- The objective is to start the right OpenAI conversation. Adjacent applications should strengthen that path, not dilute it.

Evidence:

- OpenAI Careers still showed multiple Codex surfaces on 2026-05-05.
- The first submitted target remains AI Deployment Engineer - Codex.
- The strongest adjacent routes are Deployed Product Manager, Codex and Codex App engineering, depending on whether the response signal is product/deployment or human-agent UX/product engineering.

Human role:

- Noah supplied the current state: first application and first-wave distribution are already done.

Codex role:

- Codex mapped the current official role surfaces into a constrained second-wave routing decision.

Outcome:

- `launch/role-routing.md` now gives a one-role-at-a-time decision rule before applying elsewhere.

Public artifact:

- [launch/role-routing.md](launch/role-routing.md)

## Receipt 015 - Codex Product Feedback Memo

Date: 2026-05-05

Type: Product feedback artifact

Claim:

- The audition now includes explicit Codex product/deployment feedback, not only campaign artifacts.

Why it matters:

- AI Deployment Engineer - Codex and adjacent Codex product roles value workflow adoption, public guidance, demos, high-fidelity feedback, and translating real usage into product insight.

Evidence:

- The memo distills the actual workflow: ambiguous objective, planning, drift, correction, evidence, application/outreach, signal checks, and capture gaps.
- It identifies product opportunities around evidence ledgers, current-state reconciliation, objective drift detection, social/application capture, and correction memory.

Human role:

- Noah supplied the real objective, corrections, distribution state, and taste pressure.

Codex role:

- Codex converted the workflow into a concise product-feedback memo linked from the public case file.

Outcome:

- OpenAI readers now have a direct product-insight artifact to inspect in addition to the launch story.

Public artifact:

- [CODEX_FEEDBACK.md](CODEX_FEEDBACK.md)

## Receipt 016 - Homepage Current-State Update

Date: 2026-05-05

Type: Public entrypoint correction

Claim:

- The public homepage and README now reflect that the first application and distribution wave already happened.

Why it matters:

- The project loses credibility if the public entry point keeps asking Noah to do completed launch work.
- OpenAI readers should land on the current state: post-application signal tracking, Codex product feedback, and follow-up routing.

Evidence:

- `index.html` now surfaces the post-application state, links `CODEX_FEEDBACK.md`, and points to `launch/follow-up-tracker.md`.
- `README.md` now lists the completed application/outreach state and makes the follow-up tracker the active next-action file.

Human role:

- Noah corrected the stale assumption that application, DMs, LinkedIn, and X posting were still pending.

Codex role:

- Codex updated the public entrypoint to preserve that correction and route readers to the current artifacts.

Outcome:

- The public site is no longer only a launch artifact. It now reflects the active post-launch hiring conversion state.

Public artifacts:

- [index.html](index.html)
- [README.md](README.md)

## Receipt 017 - Second-Wave Packet

Date: 2026-05-06

Type: Follow-up routing artifact

Claim:

- The repo now has a send-ready second-wave packet that does not repeat the completed application or launch steps.

Why it matters:

- If the first wave stays cold, the next move should be a constrained Codex-feedback follow-up, not more generic outreach or another broad application push.

Evidence:

- `launch/second-wave-packet.md` defines the send gate, target order, short DM, OpenAI product/engineer note, recruiter note, public follow-up post, reply handling, and stop rule.
- `launch/follow-up-tracker.md` now points second-wave execution to the packet.

Human role:

- Noah supplied the current-state correction: application, two DMs, LinkedIn, and original X thread were already done.

Codex role:

- Codex converted the current state and product-feedback memo into a bounded follow-up packet.

Outcome:

- The next distribution move is ready if signal remains weak, while still requiring an inbox/social check before sending.

Public artifact:

- [launch/second-wave-packet.md](launch/second-wave-packet.md)

## Receipt 018 - Warm Intro Brief

Date: 2026-05-06

Type: Warm-routing artifact

Claim:

- The repo now includes a forwardable warm-intro brief for OpenAI/Codex routing.

Why it matters:

- A warm route has higher leverage than another cold post when the first application/outreach wave is already done.
- The brief lets someone forward the case without inventing context or overstating the state.

Evidence:

- `launch/warm-intro-brief.md` includes the ask, one-line frame, forwardable note, short forward, mutual-contact ask, reply handling, boundaries, and stop rule.
- `launch/follow-up-tracker.md` now treats warm-intro offers as a signal and asks up to three credible warm contacts before broader second-wave notes.

Human role:

- Noah supplied the real objective and the current state that first-wave application/outreach is already complete.

Codex role:

- Codex converted the public case and product-feedback memo into a forwardable routing asset with explicit boundaries.

Outcome:

- The next conversion path can move through warm routing without requiring a new public launch or another application.

Public artifact:

- [launch/warm-intro-brief.md](launch/warm-intro-brief.md)

## Receipt 019 - Role Surface Recheck

Date: 2026-05-06

Type: Official role-surface verification

Claim:

- The primary OpenAI/Codex role surface is still live enough to support warm-intro and second-wave routing.

Why it matters:

- Role pages can change. The public case should not route people toward stale OpenAI claims or adjacent-role choices.

Evidence:

- Official OpenAI Careers search still showed 23 Codex-related roles on 2026-05-06.
- The primary `AI Deployment Engineer- Codex` page still returned with an apply link, `Technical Success - Remote - US`, and compensation shown.
- `OPENAI_FIT.md` and `launch/role-routing.md` now reference the 2026-05-06 recheck.

Human role:

- Noah had already submitted the primary application and started distribution.

Codex role:

- Codex rechecked the official OpenAI role surfaces and recorded the current routing evidence.

Outcome:

- Warm-intro and second-wave routing can keep AI Deployment Engineer - Codex as the primary target while using adjacent roles only deliberately.

Public artifact:

- [evidence/role-surface-recheck-2026-05-06.md](evidence/role-surface-recheck-2026-05-06.md)

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
