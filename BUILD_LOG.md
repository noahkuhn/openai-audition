# Build Log

This is the chronological record of the audition.

The rule: if it materially shaped the campaign, record it.

## 2026-05-01 - Session 0: The Audition Starts Before The Repo

Context:

- Noah asked Codex a thought experiment: if Codex were Noah and wanted to get hired by OpenAI after a project went viral, what would it build?
- Noah explicitly pushed for subagents and long thinking.
- The initial candidate was a live public agent investigation system.
- Noah rejected anchoring too hard on existing crypto/onchain work.
- The frame sharpened into a meta-campaign: "I asked Codex to get me hired at OpenAI."

Decisions:

- The public campaign is the product.
- The repo starts after the planning has already begun; this is a feature, not a problem.
- Existing projects are only raw material and must win through the scorecard.
- The first artifact should make the process legible before building a deep app.
- The audience is OpenAI plus builders on X.

Learnings:

- A clever app is weaker than a clean public proof-of-work narrative.
- The built thing must still have substance, or the campaign becomes a stunt.
- The best angle is "Codex turns intent into proof."

Next session:

- Create the repo under Labs.
- Publish the initial mission, scorecard, candidates, and static site.
- Decide whether the first public launch is the process itself or a process plus one proof object.

## 2026-05-01 - Session 1: Storage Model Corrected For The Project Lifecycle

Context:

- Noah asked how useful Codex discussions could be stored without manually recording every screen.
- The first answer over-indexed on transcript export.
- Noah corrected the framing: the lifecycle is unknown audience -> viral attention -> OpenAI due diligence -> clean historical artifacts.

Decisions:

- Add `CASE_FILE.md` as the first file an OpenAI person should read.
- Add `PROJECT_LIFECYCLE.md` to define what each phase needs.
- Add `ARTIFACT_LEDGER.md` so every public and proof artifact has a role.
- Add `EVIDENCE_PROTOCOL.md`.
- Treat raw Codex session export as private source material, not the public product.
- Put curated evidence in `evidence/` only after review.

Learnings:

- Git commits prove work changed, but conversation captures explain why.
- The public needs selected evidence, not a raw conversation dump.
- The repo needs an artifact hierarchy, not a pile of logs.

Next session:

- Fill the case file and launch assets before adding product depth.
- Use raw capture only to preserve source material.
- Promote only the strongest excerpts into evidence.

## 2026-05-02 - Session 2: Public Launch Package

Context:

- Noah said to proceed with the plan.
- The project needed to move from repo scaffold to a public surface that can actually carry attention.

Decisions:

- Make the homepage serve the first-click audience instead of acting as a placeholder.
- Make `CASE_FILE.md` the OpenAI due-diligence entry point.
- Add explicit receipts for the first scaffold commit and the evidence-architecture correction.
- Keep raw captures private and make curated evidence the public path.
- Add the first curated public decision record.

Learnings:

- The launch sequence needs a strong first screen, not a comprehensive archive.
- The repo should be navigable by audience: public, OpenAI, builders, private source material.
- Each artifact needs a single job.

Next session:

- Deploy the static site or choose the public host.
- Create the next curated transcript excerpt from the repo-setup session.
- Record or assemble the 60-90 second launch video.

## 2026-05-02 - Session 3: Recentered On Getting The Job

Context:

- Noah called out the failure mode directly: Codex was drifting into repo polish instead of the objective.
- The objective is not a perfect repository. The objective is to get Noah an OpenAI conversation.
- Codex checked current OpenAI Codex role surfaces before adding role-specific claims.

Decisions:

- Add `OPENAI_FIT.md` to anchor the campaign to real Codex role surfaces.
- Add `launch/openai-outreach.md` as the conversion layer from public attention to direct OpenAI contact.
- Update the homepage, application, case file, launch thread, and artifact ledger around the direct ask.
- Keep proof-object work deferred until attention or OpenAI feedback demands deeper technical proof.

Learnings:

- Broken links matter only if they block distribution.
- The repo exists to support attention, credibility, and direct outreach.
- The strongest story includes the correction: human judgment forced Codex back to the real goal.

Next session:

- Fill final public URLs.
- Verify the public repo and site.
- Apply to the strongest Codex role.
- Send direct outreach using `launch/openai-outreach.md`.

## 2026-05-02 - Session 4: Contact And Primary Role Filled

Context:

- Noah provided X, LinkedIn, email, a prior OpenAI application page, and a likely primary role.
- Codex verified the AI Deployment Engineer - Codex role on OpenAI Careers.
- The previous OpenAI page is useful as supporting background, but the new audition remains the attention object.

Decisions:

- Treat AI Deployment Engineer - Codex as the first application target.
- Treat `https://noahkuhn.com/openai/` as prior application context, not the new campaign URL.
- Fill known launch/contact inputs while leaving only deployed audition URL and public GitHub repo URL unresolved.

Learnings:

- The deployment role is especially strong because it asks for Codex power usage, customer-facing workflow design, demos, technical guidance, and product feedback.
- Noah's prior page supports the baseline story: full-stack product engineering, internal tools, Python/SQL/data workflows, LLM integrations, and durable products.

Next session:

- Create or choose the public GitHub repo URL.
- Deploy the audition page.
- Replace final URL placeholders.
- Apply to AI Deployment Engineer - Codex.

## 2026-05-02 - Session 5: Public Launch Readiness Hardening

Context:

- Noah asked whether the project was actually ready to get noticed and told Codex not to stop until it could raise an eyebrow.
- Narrative and readiness subagents reviewed the launch package.
- The reviews identified abstraction-heavy copy, raw Markdown links from the public site, stale publish language, duplicate launch threads, and insufficient public evidence.

Decisions:

- Rewrite top surfaces around a "career-changing objective" and user-side Codex evaluation under real pressure.
- Route homepage artifact links to GitHub-rendered documents instead of raw GitHub Pages Markdown.
- Keep `launch/x-thread-draft.md` as the canonical public thread.
- Remove the duplicate `auditions/openai` launch lane after canonicalizing `launch/x-thread-draft.md`.
- Add curated public evidence artifacts for the overbuilding correction, subagent review, and launch-surface hardening.
- Preserve the useful correction from Session 0 without publishing rough private-chat phrasing as the main public quote.

Learnings:

- "Inspectable proof" needs concrete artifacts, not just confident summaries.
- The eyebrow-raising part is not that Codex made a page. It is that Codex was used and corrected on a real, ambiguous objective.
- First-click links should preserve polish; raw Markdown served from Pages weakens the funnel.

Next session:

- Record or assemble the short launch video.
- Start targeted distribution to Codex/OpenAI people and builder amplifiers.

## 2026-05-03 - Session 6: Repo Pruned To The Public Case File

Context:

- Noah challenged whether every file was necessary and whether the repo still made sense.
- The repo had started to look like a mini operating system instead of a clean public case file.

Decisions:

- Remove duplicated OpenAI audition lane files.
- Remove internal lifecycle, artifact-ledger, evidence-protocol, source-capture, and extra prompt-template scaffolding.
- Keep the public path focused on homepage, case file, role fit, application, build log, receipts, evidence, and launch/outreach copy.
- Update the homepage and README so readers see fewer choices and no dead internal architecture.

Learnings:

- Process is the artifact, but too much process architecture weakens the first impression.
- A public repo for attention should feel like a sharp case file, not a project-management system.

Next session:

- Use the canonical launch thread.
- Route attention to Codex/OpenAI people and builder amplifiers.

## 2026-05-03 - Session 7: Share Image And Case-File Design Pass

Context:

- Noah said the site felt serviceable but generic.
- Noah asked Codex to create a compelling `og:image` for X shares using `imagegen`.
- Noah also asked for five subagent design directions, saved in the repo, before deciding whether to redesign.

Decisions:

- Generate a real bitmap desk/case-file visual and save it as a project asset.
- Compose a deterministic 1200x630 Open Graph image so X shares do not depend on AI-rendered text.
- Save the five design directions in `evidence/design-directions-2026-05-03.md`.
- Adopt the shared direction: a review packet / annotated case file rather than a generic portfolio page.
- Move the correction moment ahead of broad OpenAI fit copy on the homepage.

Learnings:

- The design reviewers converged on the same signal: the public artifact should show objective, drift, correction, and receipts immediately.
- The page should make the human-agent loop legible before asking anyone to read deeper documents.

Next session:

- Verify the live X-card image after GitHub Pages rebuilds.
- Use the redesigned page as the public launch surface for targeted OpenAI/Codex outreach.

## 2026-05-03 - Session 8: Synthetic Image Corrected To Real Codex Instance

Context:

- Noah reviewed the share image and pointed out that the generated laptop scene did not show an actual Codex instance.
- The project premise depends on visible reality: Codex doing the work, not a generic AI-themed scene.

Decisions:

- Use Noah's real Codex Desktop screenshot as the source image for the hero and Open Graph card.
- Create new cache-busting assets: `assets/og/codex-instance-base.png` and `assets/og/openai-audition-og-codex.png`.
- Update homepage metadata to point to the new Open Graph image path.
- Remove the old generated image assets from the repo.

Learnings:

- The public surface should not use synthetic imagery when an actual Codex work artifact exists.
- A less polished real screenshot is stronger than a prettier fake image because the claim is about inspectable process.

Next session:

- Verify the live Pages image URL and metadata after push.
- Use the actual-Codex share card for X launch.

## 2026-05-05 - Session 9: Live Evidence Audit Before Distribution

Context:

- The next useful move was not another concept pass; it was checking whether the public launch surface and role claims still held up.
- The live GitHub Pages site, Open Graph image, public repo, and official OpenAI Codex role pages were checked.
- The audit found two public-proof hygiene issues: `CASE_FILE.md` had stale commit and receipt coverage, and `RECEIPTS.md` carried duplicate `Receipt 007` headings.

Decisions:

- Treat live verification as a public evidence artifact because the repo is supposed to be inspectable.
- Update `CASE_FILE.md` so the due-diligence path reflects the actual published commits and receipts.
- Fix receipt numbering before sending the repo to OpenAI/Codex readers.
- Keep the next action pointed at distribution, application, and direct outreach instead of adding more internal scaffolding.

Learnings:

- Launch-ready is not just "the page renders"; it means the public evidence path is current enough for a serious reader.
- Small evidence mismatches undermine the premise more than missing app depth does.

Next session:

- Publish the canonical X thread.
- Apply through the official AI Deployment Engineer - Codex role page.
- Send targeted notes using `launch/openai-outreach.md`.
- Create the launch video only if it materially improves distribution.

## 2026-05-05 - Session 10: Post-Application State Corrected

Context:

- Noah corrected Codex again: he had already applied, sent two DMs, published one LinkedIn post, and posted an X thread for the original project.
- The docs still treated application and initial distribution as next steps.

Decisions:

- Update the repo state so future sessions start after application/distribution, not before it.
- Add a follow-up tracker for replies, warm routing, second-wave notes, and no-signal handling.
- Preserve the distribution state as user-reported until exact links, screenshots, or recipient details are intentionally captured.

Learnings:

- "Current state" matters more than a tidy launch checklist.
- The next useful work is response handling and evidence capture, not repeating the first-wave launch.

Next session:

- Check for replies or measurable signal.
- Capture the application confirmation and public post links if Noah wants them in the evidence trail.
- Send a second wave only if early signal is weak or absent.
