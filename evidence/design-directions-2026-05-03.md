# Evidence 005: Design Direction Review

Date: 2026-05-03

Context:

- Noah said the public site felt serviceable but generic.
- Noah asked Codex to use five subagents for design directions, save the directions in the repo, and redesign only if a direction was good enough.
- The objective stayed unchanged: make the audition more likely to get noticed by OpenAI/Codex people.

Decision:

- Adopt the shared direction: an active case file / marked-up review packet.
- The strongest repeated idea was to put the human correction moment above generic role-fit copy.
- This direction fits the repo because the public artifact is not a portfolio; it is inspectable evidence of human-agent work under a real objective.

## Direction 1: Under Oath

Make the landing page feel like a public case file, not a startup homepage. Codex is not being worshipped; it is being examined. Noah's claim is on trial in public, and the evidence is visible immediately.

First viewport:

- Huge three-line headline: `I asked Codex / to get me hired / at OpenAI.`
- One sharp subhead: `Not a demo. A public record of human-agent work.`
- A case panel with current objective, latest receipt, last human correction, and current verdict.
- A bottom strip of artifact tabs: `Mission`, `Scorecard`, `Build Log`, `Receipts`, `Application`.

Why it could raise an eyebrow:

- It turns process, correction, and receipts into the product instead of hiding them behind a pitch veneer.

## Direction 2: The Review Packet

Treat the landing page like an opened case file on a desk, not a polished personal microsite.

First viewport:

- Left side: the premise in huge type.
- Right side: a pinned intake card with `Objective`, `Candidate`, `Agent`, `Current status`, and the twist: `Codex drifted. Noah corrected it.`
- Bottom strip: three evidence tabs only: `Case File`, `Correction`, `Direct Ask`.

Why it could raise an eyebrow:

- It stops looking like "smart engineer makes a site" and starts looking like a live human-agent evaluation artifact.

## Direction 3: The Correction Board

Push the page toward an editorial incident board: less landing page, more live case under review.

First viewport:

- Left 60%: `I asked Codex to get me hired at OpenAI.` huge and direct.
- Right 40%: an evidence rail with `The Prompt`, `The Drift`, and `The Correction`.
- The correction should be the dramatic hook because it is the proof of judgment.

Why it could raise an eyebrow:

- It frames the project as an agent-evaluation artifact. The signal is not that Noah used AI; it is that he can direct and correct an agent under ambiguity.

## Direction 4: The Annotated Case File

Make the landing page feel like the first page of an internal dossier: warm paper, dense black headline, monospace metadata, red editorial markup, green evidence links, thin rule lines, margin notes, and stamped labels.

First viewport:

- Left 70%: giant premise plus short thesis.
- Right 30%: case panel with `Target`, `Candidate`, `Agent`, `Status`, plus a redlined human correction excerpt.
- Primary CTA: `Open Case File`.
- Secondary CTA: `See The Receipts`.

Why it could raise an eyebrow:

- It refuses normal portfolio grammar and says: inspect the human-agent loop under real stakes.

## Direction 5: The Marked-Up Brief

Make the page look like an important document under active review, not a fake product UI.

First viewport:

- One oversized brief page dominates the screen.
- The raw objective appears in a monospace strip.
- Margin callouts identify `Objective`, `Drift`, and `Human correction`.
- Bottom tabs route to `Case File`, `Correction`, and `Receipts`.

Why it could raise an eyebrow:

- It communicates the non-obvious signal: Noah used Codex on an ambiguous, high-stakes objective, caught drift, corrected it, and kept the trail public.

## Implemented Direction

The site now uses the shared review-packet direction:

- Replaced the generated image concept with a real screenshot of an active Codex instance.
- Added a deterministic 1200x630 Open Graph image for X shares using the actual Codex UI as the source.
- Rebuilt the first viewport around a case panel, raw objective strip, and three evidence tabs.
- Moved the correction moment ahead of general OpenAI fit copy.
- Preserved stable GitHub links for readers who want to inspect the underlying case file, receipts, fit, and application.
