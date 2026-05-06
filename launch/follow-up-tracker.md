# Follow-Up Tracker

This file starts after the first application/distribution wave.

## Current State

As of Noah's 2026-05-05 update plus the 2026-05-06 local Mail check:

- Application: submitted; receipt verified in local Mail on 2026-05-06.
- DMs: two sent.
- LinkedIn: one post published.
- X: launch post captured on 2026-05-06.

Treat the application receipt and X launch post as verified. Treat the DMs and LinkedIn post as user-reported until links, screenshots, or private notes are captured.

## Signal Checks

### 2026-05-05

Gmail:

- Checked the connected Gmail account: `noah@pilotmade.com`.
- Searches for `openai newer_than:30d`, `(openai OR ashby OR codex) newer_than:7d`, and `ashby` found no relevant OpenAI/Ashby/Codex application response.
- Limitation: the public application/contact artifacts use `hey@noahkuhn.com`, so this Gmail check is not comprehensive unless that mailbox forwards into `noah@pilotmade.com`.

GitHub:

- Repo status via GitHub API: 0 stars, 0 watchers, 0 forks, 0 issues, 0 PRs.
- Traffic API available window: 48 views from 5 unique visitors; 83 clones from 42 unique cloners.
- Visible traffic was concentrated on 2026-05-02 and 2026-05-03; the API did not show current-day 2026-05-05 traffic yet.

Interpretation:

- No verified warm signal captured yet.
- Do not treat this as proof that there are no email, LinkedIn, X, or DM responses.
- Next highest-leverage check is the actual application/contact inbox and the public post URLs.

### 2026-05-05 Contact Surface Availability

Gmail alias checks:

- `deliveredto:hey@noahkuhn.com newer_than:30d`: no results in the connected Gmail account.
- `to:hey@noahkuhn.com newer_than:30d`: no results in the connected Gmail account.
- `(openai OR ashby OR codex) (to:hey@noahkuhn.com OR deliveredto:hey@noahkuhn.com)`: no results in the connected Gmail account.
- `from:(openai.com OR jobs.ashbyhq.com OR ashbyhq.com) newer_than:30d`: no results in the connected Gmail account.

Public post checks:

- Public search did not find a matching `openai-audition`, `I asked Codex`, or `noahkuhn.github.io/openai-audition` post URL.
- Direct fetch confirmed the public X profile exists at <https://x.com/noahbkuhn>, but the fetched page did not expose recent post/thread content.
- LinkedIn recent activity was not fetchable from the current runtime.

Interpretation:

- At that point, the accessible tools still could not verify the application confirmation, the LinkedIn post, the X thread, or DMs.
- This is a capture gap, not a failure signal.

Fast capture checklist:

- LinkedIn post URL.
- Names or categories for the two DMs, kept private if needed.
- Any replies, reactions, profile visits, intro offers, or recruiter messages.

### 2026-05-06 Application Confirmation Check

Gmail connector status:

- The Gmail connector still returned an expired-token error from the available tool surface.
- The current CLI/plugin surface did not expose a connector re-auth command.
- Codex used local Apple Mail search across All Inboxes as the fallback evidence source.

Local Mail findings:

- `"OpenAI Hiring Team"` surfaced one visible application receipt.
- Sender: `OpenAI Hiring Team`.
- Mailbox: `noahkuhn@gmail.com`.
- Date: 2026-05-03.
- Subject: `Thank you for applying to OpenAI`.
- Summary shown in Mail: application received; recruiting team will review; the message points to OpenAI hiring philosophy and interview-process information.
- `ashby OpenAI` returned no visible results.
- `OpenAI recruiter` returned multiple results, but the only current relevant OpenAI hiring item visible was the application receipt.

Interpretation:

- The application receipt is now verified.
- No recruiter response, warm intro, interview, or offer is verified.
- At that point, LinkedIn, X, and DM receipts remained uncaptured. The X launch post was captured later in this tracker.

Evidence:

- [Application confirmation mail check](../evidence/application-confirmation-2026-05-06.md)

### 2026-05-06 Signal Sweep

Public web/social checks:

- Public web search still did not locate a user-owned `openai-audition`, `I asked Codex`, or `noahkuhn.github.io/openai-audition` post URL.
- Direct public fetch of <https://x.com/noahbkuhn> returned the profile shell and follower count, but did not expose recent post/thread content.
- LinkedIn profile and recent-activity fetches were not accessible from the current runtime.

Local Mail:

- `OpenAI Ashby`: no visible results.
- `OpenAI recruiter`: 15 visible results; the only current relevant OpenAI hiring item visible was the 2026-05-03 application receipt.
- `OpenAI Hiring Team`: top visible result remained the 2026-05-03 application receipt; no visible recruiter reply after it.

GitHub:

- Repo status via GitHub API: 0 stars, 0 watchers, 0 forks, 0 issues, 0 PRs.
- Views: 48 total, 5 unique; nonzero days were 2026-05-02 and 2026-05-03.
- Clones: 164 total, 67 unique; 2026-05-05 showed 81 clones from 30 unique cloners.
- Referrers: `noahkuhn.github.io` with 46 views from 3 uniques; `t.co` with 2 views from 2 uniques.

Interpretation:

- No recruiter response, warm intro, interview, offer, or OpenAI-adjacent reply is verified.
- GitHub clone traffic increased materially on 2026-05-05, and `t.co` referrer traffic suggests some X-driven traffic, but neither proves OpenAI interest.
- The next non-repetitive move is still direct capture of LinkedIn/X/DM surfaces or warm-intro routing, not another application.

### 2026-05-06 X Launch Post Capture

Public X payload:

- X post: <https://x.com/noahbkuhn/status/2050930949928452494>
- Profile: `Noah Kuhn` / `@noahbkuhn`
- Followers shown: 74
- Pinned tweet id: `2050930949928452494`
- Post created at: 2026-05-03 13:30:17 UTC
- Expanded links:
  - <https://github.com/noahkuhn/openai-audition>
  - <https://noahkuhn.github.io/openai-audition/>
- Public counters in the payload: 2 replies, 0 reposts, 0 quotes, 2 likes, 3 bookmarks.

Interpretation:

- The X launch post URL is now captured.
- This helps explain the `t.co` referrer in GitHub traffic, but it does not prove OpenAI readership.
- LinkedIn post URL and two DM details remain uncaptured.

Evidence:

- [X launch post capture](../evidence/x-launch-post-2026-05-06.md)

### 2026-05-06 Public Attention Path Check

X public payload:

- The public post payload still exposed the original X post and aggregate counters.
- It did not expose the two replies as separate reply text or reply authors in the logged-out payload.
- Treat the reply count as an attention hint, not a usable routing signal.

GitHub popular paths:

- `/blob/main/APPLICATION.md`: 19 views from 3 unique visitors.
- `/blob/main/launch/x-thread-draft.md`: 16 views from 3 unique visitors.
- `/blob/main/RECEIPTS.md`: 6 views from 3 unique visitors.
- `/tree/main/launch`: 5 views from 3 unique visitors.
- Repo overview: 2 views from 2 unique visitors.

Interpretation:

- The application and X-thread draft are the most-inspected repo paths visible through GitHub traffic.
- This suggests the public pitch and social copy are doing some work.
- It still does not prove OpenAI readership, recruiter interest, a warm intro, interview, or offer.

## What To Watch

- OpenAI recruiter reply.
- OpenAI/Codex engineer or product reply.
- Builder amplifier reply, quote, repost, or intro offer.
- Warm-intro offer from anyone who can forward [warm-intro-brief.md](warm-intro-brief.md).
- LinkedIn comments or inbound profile views from OpenAI-adjacent people.
- X replies, reposts, DMs, bookmarks, or visible traffic to the case file.
- GitHub traffic or stars from relevant people.

## Current Follow-Up Hook

OpenAI's 2026-04-16 `Codex for (almost) everything` release makes the strongest follow-up hook more specific than the original launch story.

Use this framing for warm intros or second-wave notes:

- OpenAI is positioning Codex beyond coding into connected tools, computer use, memory, proactive continuation, and ongoing work.
- This public audition is a live user-side case study of those exact surfaces under pressure.
- The value is not "AI made me a page"; it is concrete feedback about current-state reconciliation, evidence status, social/application capture, objective drift, and correction memory.

Reference:

- <https://openai.com/index/codex-for-almost-everything/>

## If A Warm Reply Comes In

Use the shortest useful response:

```text
Appreciate you taking a look. The cleanest starting point is the case file:
https://github.com/noahkuhn/openai-audition/blob/main/CASE_FILE.md

If there is a better person for Codex deployment, product, or agent-workflow feedback, I would be grateful for the right route.
```

If they ask what role:

```text
The first target is AI Deployment Engineer - Codex, but the broader fit is any Codex lane where hands-on agent workflow, deployment judgment, demos, technical guidance, and product feedback matter.
```

If they ask what is actually different:

```text
The useful part is the correction trail. Codex did not simply write a page; it drifted, got corrected, and turned the objective into public artifacts, evidence, and role-specific positioning.
```

## If There Is No Signal After 48 Hours

Do not build a large new app.

Run a second wave:

- Ask up to three credible warm contacts to forward [warm-intro-brief.md](warm-intro-brief.md).
- Capture the LinkedIn post link and private DM notes.
- Send 6-8 more targeted notes using [second-wave-packet.md](second-wave-packet.md), not a generic blast.
- Publish one tighter follow-up around what Codex got wrong while trying to get Noah hired.
- Add one stronger proof artifact only if it creates a sharper reply hook.
- Use [role-routing.md](role-routing.md) before applying to any adjacent role.

## Second-Wave Note

```text
I applied to Codex and built the application as a public Codex case study.

The interesting bit is not "AI made me a portfolio." It is the operator loop: I gave Codex an ambiguous career objective, it drifted into overbuilding, I corrected it, and the repo preserves what changed.

If you work on Codex deployment, product, or agent workflows, I think this is useful signal:
https://noahkuhn.github.io/openai-audition/
```
