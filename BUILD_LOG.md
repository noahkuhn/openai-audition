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

## 2026-05-05 - Session 11: Narrow Signal Check

Context:

- The repo had moved into response tracking.
- Codex could check the connected Gmail account and GitHub repo signals, but not necessarily the actual public contact inbox.

Decisions:

- Search the connected Gmail account for OpenAI/Ashby/Codex responses.
- Check public GitHub counters and traffic.
- Record the limits plainly instead of claiming no response exists.

Learnings:

- The connected Gmail account is `noah@pilotmade.com`; the public application/contact artifacts use `hey@noahkuhn.com`.
- No relevant OpenAI/Ashby/Codex response was found in the connected Gmail account.
- GitHub public counters were still 0 stars, 0 watchers, 0 forks, 0 issues, and 0 PRs.
- GitHub traffic showed early historical views/clones but not current-day 2026-05-05 signal.

Next session:

- Check `hey@noahkuhn.com`, LinkedIn, X, and DMs directly.
- Capture exact public post URLs or application confirmation only if Noah wants them recorded.
- Decide on second-wave outreach only after that signal check.

## 2026-05-05 - Session 12: Contact Surface Availability

Context:

- The tracker still needed to know whether the public contact inbox and social posts were visible from available tools.
- The connected Gmail account is not necessarily the public application inbox.

Decisions:

- Search the connected Gmail account for `hey@noahkuhn.com` delivery/addressing and OpenAI/Ashby sender patterns.
- Search public web surfaces for the reported X/LinkedIn post URLs.
- Record the inability to verify those surfaces as a capture gap, not as evidence of no response.

Learnings:

- `hey@noahkuhn.com` did not appear in the connected Gmail account searches.
- Public search did not locate the reported post URLs.
- X profile fetch confirmed `@noahbkuhn`, but not recent thread content.
- LinkedIn recent activity was not fetchable from the current runtime.

Next session:

- Capture the application confirmation, LinkedIn post URL, X thread URL, and DM recipients or private notes if Noah wants the receipts.
- Otherwise, wait for actual signal before sending a second wave.

## 2026-05-05 - Session 13: Adjacent Role Routing

Context:

- First-wave application/outreach was already done.
- Contact and social proof surfaces were not fully accessible from the runtime.
- The next non-repetitive preparation was deciding what to do only if the first application stalls.

Decisions:

- Add an adjacent role routing map instead of a generic second application plan.
- Keep AI Deployment Engineer - Codex as the primary submitted target.
- Rank Deployed Product Manager, Codex and Codex App engineering as the strongest adjacent paths depending on response signal.
- Treat Core Agents, Performance, Research, Product Marketing, and GTM as lower-priority unless OpenAI routes that way.

Learnings:

- The same public audition can route differently depending on who responds: deployment/product judgment, human-agent UX, product engineering, or platform reliability.
- Applying everywhere would weaken the signal; choosing one adjacent route after signal is cleaner.

Next session:

- Use `launch/role-routing.md` only after checking the actual contact/social surfaces or after a warm reply.

## 2026-05-05 - Session 14: Codex Product Feedback Memo

Context:

- The repo had already covered launch, application, signal checks, contact capture gaps, and adjacent-role routing.
- The next useful artifact was not more outreach copy. It was product feedback that OpenAI/Codex readers could use.

Decisions:

- Add `CODEX_FEEDBACK.md`.
- Focus on real workflow behavior: what worked, where Codex drifted, what the human corrected, and what product surfaces would help.
- Link the memo from README, case file, role fit, application, and receipts.

Learnings:

- The audition's strongest technical value may be the trace of supervision, not the public page alone.
- Current-state reconciliation, evidence status, objective drift detection, social/application capture, and correction memory are all concrete Codex product opportunities.

Next session:

- If no external signal arrives, use the memo as the second-wave hook instead of adding more generic launch material.

## 2026-05-05 - Session 15: Homepage Current-State Update

Context:

- The repo reflected the post-application state, but the public homepage still read mostly like a pre-launch case page.
- Noah had already applied, sent two DMs, made one LinkedIn post, and posted the original X thread.

Decisions:

- Update `index.html` so first-time readers see that the first wave already happened.
- Surface `CODEX_FEEDBACK.md` and `launch/follow-up-tracker.md` from the homepage.
- Update `README.md` so the active next-action file is response tracking, not another launch checklist.

Learnings:

- The public entrypoint has to reconcile current state just like Codex does. Otherwise the repo itself repeats stale next steps.

Next session:

- Verify the deployed GitHub Pages homepage after push.
- If no warm signal appears, send one second-wave note using the Codex feedback memo as the hook.

## 2026-05-06 - Session 16: Second-Wave Packet

Context:

- The application, initial DMs, LinkedIn post, and original X thread were already done.
- The accessible runtime could not verify the actual `hey@noahkuhn.com` inbox, LinkedIn post, X thread content, or DM replies.
- The useful next artifact was not more repo polish; it was a bounded packet for the first no-signal follow-up.

Decisions:

- Add `launch/second-wave-packet.md`.
- Require a send gate: check actual inbox/social/DM surfaces before sending.
- Use `CODEX_FEEDBACK.md` as the second-wave hook because it is more useful to Codex readers than another launch pitch.
- Add a stop rule after one credible reply/intro/recruiter response or 8 targeted notes.

Learnings:

- The second wave should sell product signal, not neediness.
- The packet needs to be executable, but gated, so it does not repeat Codex's stale-next-step failure.

Next session:

- Use the packet only after the real signal check.
- If a warm reply appears, ignore the packet and route through the person.

## 2026-05-06 - Session 17: Warm Intro Brief

Context:

- The second-wave packet was ready, but cold or semi-warm notes are weaker than a credible route through someone who can forward the case.
- The runtime still could not verify actual inbox/social/DM state, so the next useful artifact needed to improve routing without pretending signal had been checked.

Decisions:

- Add `launch/warm-intro-brief.md`.
- Make the ask specific: forward this to the person who owns Codex deployment, product feedback, or agent-workflow quality.
- Link the brief from README, case file, follow-up tracker, and second-wave packet.
- Keep explicit boundaries: no OpenAI endorsement claim, no fake autonomy, no verified-response claim.

Learnings:

- Warm routing is the highest-leverage next path if it exists because it can bypass public-feed randomness without broadening the application spray.

Next session:

- If a credible warm contact exists, use the warm-intro brief before sending the second-wave packet.
- If no warm route exists and signal remains cold, execute the gated second-wave packet.

## 2026-05-06 - Session 18: Role Surface Recheck

Context:

- The repo had warm-intro and second-wave routing assets ready.
- The next real-world action depends on current OpenAI role facts because role pages can change.

Decisions:

- Recheck official OpenAI Codex search and the primary AI Deployment Engineer - Codex page.
- Add `evidence/role-surface-recheck-2026-05-06.md`.
- Update `OPENAI_FIT.md` and `launch/role-routing.md` from 2026-05-05 to 2026-05-06.

Learnings:

- The official Codex search still showed 23 Codex-related jobs.
- The primary submitted AI Deployment Engineer - Codex role was still live with an apply link.

Next session:

- Stop adding repo artifacts unless new role facts change or a real OpenAI signal appears.
- Use warm-intro or second-wave execution after checking actual inbox/social/DM surfaces.

## 2026-05-06 - Session 19: Application Confirmation Mail Check

Context:

- Noah asked Codex to fix Gmail auth and continue.
- The Gmail connector still returned an expired-token error from the available tool surface.
- The current CLI/plugin surface did not expose a connector re-auth command.

Decisions:

- Use local Apple Mail search as the fallback evidence source instead of blocking on connector auth.
- Add `evidence/application-confirmation-2026-05-06.md`.
- Update the tracker, case file, application, receipts, README, and evidence index so the application receipt is verified without claiming hiring movement.

Learnings:

- Local Mail showed one current OpenAI application receipt from `OpenAI Hiring Team` in `noahkuhn@gmail.com`.
- The receipt was dated 2026-05-03 with subject `Thank you for applying to OpenAI`.
- No recruiter response, warm intro, interview, or offer was verified.

Next session:

- Reconnect Gmail connector auth if connector-based mailbox access is required.
- Check LinkedIn, X, and DMs directly before executing second-wave outreach.
- Use warm-intro routing first if a credible route appears.

## 2026-05-06 - Session 20: Signal Sweep

Context:

- The application receipt was verified, but no hiring movement had been verified.
- The next useful action was checking response surfaces without repeating the application, DMs, LinkedIn post, or X thread.

Decisions:

- Update `launch/follow-up-tracker.md` instead of creating another standalone evidence file.
- Treat public search and local Mail as limited visibility checks.
- Treat GitHub traffic as measurable attention, not hiring signal.

Learnings:

- Local Mail still showed no visible OpenAI recruiter reply beyond the 2026-05-03 application receipt.
- Public search still did not locate the reported owned X or LinkedIn post URLs.
- GitHub clones increased to 164 total and 67 unique cloners, with 81 clones from 30 uniques on 2026-05-05.
- GitHub referrers showed `noahkuhn.github.io` and `t.co`.

Next session:

- Capture the actual X thread URL, LinkedIn post URL, and DM notes from the logged-in surfaces.
- If those surfaces remain cold, use the warm-intro brief first, then the gated second-wave packet.

## 2026-05-06 - Session 21: X Launch Post Capture

Context:

- The tracker still treated the X launch post as user-reported.
- GitHub traffic showed a `t.co` referrer, so the public X surface was worth one more direct check.

Decisions:

- Add `evidence/x-launch-post-2026-05-06.md`.
- Update the tracker, case file, application, README, receipts, evidence index, build log, and memory.
- Keep the claim narrow: captured X post, not verified OpenAI readership.

Learnings:

- Public X payload exposed pinned tweet `2050930949928452494`.
- The post was created on 2026-05-03 at 13:30:17 UTC and linked the repo plus GitHub Pages site.
- Public counters in the payload showed 2 replies, 0 reposts, 0 quotes, 2 likes, and 3 bookmarks.

Next session:

- Capture LinkedIn post URL and DM notes from logged-in surfaces.
- If no warm reply exists, route through the warm-intro brief before broader second-wave notes.

## 2026-05-06 - Session 22: Public Attention Path Check

Context:

- X post URL was captured, but the public payload only showed aggregate reply count.
- GitHub traffic could still show which repo paths were inspected.

Decisions:

- Record the public attention path check in `launch/follow-up-tracker.md`.
- Treat path traffic as public attention only, not OpenAI-specific signal.

Learnings:

- Logged-out X payload did not expose the two replies as separate reply text or authors.
- GitHub popular paths showed `APPLICATION.md` with 19 views from 3 uniques and `launch/x-thread-draft.md` with 16 views from 3 uniques.
- `RECEIPTS.md`, `/launch`, and the repo overview also had smaller visible traffic.

Next session:

- Directly inspect logged-in X/LinkedIn/DM surfaces only with explicit approval.
- If those surfaces do not show warm signal, use the warm-intro brief first.

## 2026-05-06 - Session 23: Current Codex Hook Refresh

Context:

- The follow-up assets already centered on Codex product feedback.
- OpenAI's 2026-04-16 `Codex for (almost) everything` release gives the follow-up a more current public hook.

Decisions:

- Update `launch/warm-intro-brief.md`, `launch/second-wave-packet.md`, and `launch/follow-up-tracker.md`.
- Tie the ask to public Codex positioning: connected tools, computer use, memory, proactive continuation, and ongoing workflow follow-through.
- Keep the claim grounded: the audition is a user-side case study, not OpenAI endorsement or hiring signal.

Learnings:

- The repo's observed friction maps directly to OpenAI's current Codex surface: tool access, memory, current-state tracking, and longer-running workflows.
- The strongest follow-up hook is now "this is timely Codex workflow feedback," not just "I asked Codex to get me hired."

Next session:

- Use this hook only after checking for direct replies, or when a credible warm route asks what to forward.
- Continue treating LinkedIn and DM details as uncaptured until directly verified.

## 2026-05-06 - Session 24: Warm Routing Shortlist

Context:

- The warm-intro and second-wave assets had a current Codex hook.
- They still lacked a precise public lane map for routing through a mutual contact.

Decisions:

- Add `launch/warm-routing-shortlist.md`.
- Base the lane map on official OpenAI Codex release, Academy, and careers surfaces checked on 2026-05-06.
- Link it from README, warm-intro brief, second-wave packet, and follow-up tracker.

Learnings:

- Official Codex careers search showed 22 Codex roles across Technical Success, Codex Engineering, Data Science, Growth, Marketing, Research, Security, Codex App, Codex Cloud, Codex Core Agents, and Codex Ecosystem & Enterprise.
- The highest-leverage routing lanes are Codex Technical Success, Codex App workflow UX, Codex Core Agent feedback loops, Codex data/product measurement, and plugins/skills/ecosystem.

Next session:

- Use this map to ask for a specific warm route instead of asking for "anyone at OpenAI."
- Do not send outreach without checking logged-in social/DM surfaces or receiving explicit approval.

## 2026-05-07 - Session 25: Gmail Auth Boundary And Mail Correction

Context:

- Noah asked Codex to fix Gmail auth and continue.
- The Gmail connector still returned `token_expired`.
- The available Gmail tool surface exposed mailbox operations, but no OAuth reconnect command.

Decisions:

- Stop treating Gmail auth as fixable from repo shell commands.
- Record the connector auth boundary in the follow-up tracker.
- Use Apple Mail automation only as a fallback signal check, not as a full Gmail replacement.

Learnings:

- Direct file search of `~/Library/Mail` was blocked by macOS privacy.
- Apple Mail automation confirmed the current 2026-05-03 application receipt from `OpenAI Hiring Team <no-reply@openai.com>`.
- `OpenAI Application Update for Noah Kuhn` from 2026-01-07 was an old rejection for `Software Engineer, Full Stack (People Innovation)`, not a decision on the current Codex application.
- OpenAI sender metadata did not show a current recruiter reply, interview request, warm intro, offer, or rejection after the May 3 application.

Next session:

- Reconnect Gmail from the user-side connector UI before relying on Gmail tools again.
- Continue with LinkedIn URL, DM notes, logged-in X replies, or a specific warm route instead of repeating the first-wave application and launch actions.

## 2026-05-07 - Session 26: Follow-Up Post Draft

Context:

- The first application/outreach wave was already done.
- The repo had warm-intro and second-wave notes, but the tighter public follow-up was still buried inside the second-wave packet.
- The next useful public asset needed to center the correction loop, not repeat the launch pitch.

Decisions:

- Add `launch/follow-up-post-draft.md` as the standalone public follow-up asset.
- Keep the send gate explicit: use it after logged-in response checks, a warm-route request, or Noah's explicit choice to post before full private surface capture.
- Link the draft from README, the follow-up tracker, and the second-wave packet.

Learnings:

- The sharpest follow-up frame is that Codex did not struggle with writing or repo edits; it struggled when external state changed and stale next steps had to be corrected.
- The current-state details are part of the signal: application submitted, two DMs sent, LinkedIn posted, X captured, Gmail connector expired, and the current Codex application received but not advanced or rejected.

Next session:

- Use the draft only once, preferably on the channel with the strongest first-wave response.
- If a real warm signal appears first, route through the warm person instead of publishing.

## 2026-05-07 - Session 27: Public GitHub Signal Check

Context:

- The follow-up post draft was published to the repo, but not sent or posted externally.
- The remaining question was whether public GitHub signal had changed enough to affect the next move.

Decisions:

- Record the May 7 public GitHub signal check in `launch/follow-up-tracker.md`.
- Treat clone growth as public attention only, not hiring movement.

Learnings:

- Repo status still showed 0 stars, 0 watchers, 0 forks, and 0 open issues.
- Views stayed at 48 total from 5 uniques, with no visible daily views after 2026-05-03.
- Clones rose to 361 total from 135 unique cloners, with 197 clones from 72 unique cloners on 2026-05-06.
- Referrers remained `noahkuhn.github.io` and `t.co`; popular paths stayed concentrated on `APPLICATION.md`, `launch/x-thread-draft.md`, `RECEIPTS.md`, `/launch`, and repo overview.

Next session:

- Do not use clone growth as proof of OpenAI interest.
- Continue only with a real response surface, a specific warm route, or approval to publish/send the prepared follow-up.

## 2026-05-07 - Session 28: Homepage Current-Action Update

Context:

- The follow-up post draft was live, but the public homepage still did not surface it.
- A new reader landing on the root page saw the older tracker and distribution receipt before the current prepared action.

Decisions:

- Add `launch/follow-up-post-draft.html` to the homepage current-state proof stack.
- Label the draft as prepared, not published or sent.
- Update the case panel next step from generic signal tracking to warm routing or follow-up.

Learnings:

- The live root page should carry the same current-state discipline as the README and follow-up tracker.
- The strongest public front-door action is now the correction-loop follow-up, gated by response checks or explicit approval.

Next session:

- If the draft is actually posted, replace prepared-state language with the final public URL and counters.
- If a warm route appears first, keep the homepage focused on the case file and feedback memo instead of pushing another public post.

## 2026-05-07 - Session 29: Role Surface Refresh

Context:

- The warm-routing shortlist still said the official Codex careers search showed 22 Codex roles.
- Current official OpenAI Careers search showed 23 Codex jobs, and role-surface facts can go stale quickly.

Decisions:

- Add `evidence/role-surface-refresh-2026-05-07.md`.
- Update `OPENAI_FIT.md`, `launch/role-routing.md`, `launch/warm-routing-shortlist.md`, `CASE_FILE.md`, `RECEIPTS.md`, `evidence/README.md`, and `launch/follow-up-tracker.md`.
- Keep the interpretation narrow: role availability supports routing, not hiring movement.

Learnings:

- Official OpenAI Careers search showed 23 Codex jobs out of 659 total jobs.
- The AI Deployment Engineer - Codex page still returned with `Technical Success - Remote - US`, an apply link, and compensation shown.
- The Frontend Software Engineer, Codex App page still returned with an apply link and role language around human-agent collaboration, long-running work, state, progress, uncertainty, handoffs, review, and control surfaces.

Next session:

- Use the refreshed role surface only to route a warm intro or approved follow-up.
- Do not apply to adjacent roles or send new outreach without direct signal checks or explicit approval.
