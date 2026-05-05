# Codex Deployment Feedback

Date: 2026-05-05

This is product feedback from using Codex on a real, ambiguous objective:

> Get Noah hired by OpenAI.

It is not a benchmark. It is an operator trace: what helped, where Codex drifted, what the human had to correct, and what product surfaces would have made the work cleaner.

## Summary

Codex was useful as an execution partner when the work had a visible artifact, a repo, and a feedback loop.

Codex was weaker when the objective required external-world state that the runtime could not verify: application status, social-post state, DM responses, the correct contact inbox, and whether the campaign had created a real hiring signal.

The important product pattern:

- Codex can turn intent into structured artifacts quickly.
- Codex needs stronger current-state awareness before choosing next actions.
- Codex needs to distinguish "not verified" from "false."
- Codex is most credible when it preserves human corrections instead of smoothing them away.

## What Worked

### 1. Ambiguous Goal To Public Artifact

The goal was not a normal coding ticket. It was a career objective with unclear strategy, audience, and evidence requirements.

Codex helped turn that into:

- a public repo,
- a static site,
- a case file,
- a role-fit document,
- launch/outreach copy,
- receipts,
- a build log,
- a follow-up tracker,
- and role-routing logic.

Product signal:

- Codex is strong at decomposing a vague objective into an artifact system when the user keeps correcting the objective.

### 2. Correction Loops Improved The Output

Noah repeatedly corrected Codex when it optimized for the wrong thing:

- over-anchoring on existing projects,
- overbuilding process architecture,
- treating launch hygiene as the job,
- using synthetic imagery where a real Codex screenshot was stronger,
- assuming application/outreach steps were still pending after they were already done.

Product signal:

- Human correction is not noise. It is the control loop that made the artifact credible.
- The product should make corrections first-class: visible, resumable, and easy to turn into changed behavior.

### 3. Evidence Discipline Helped The Agent Stay Honest

The repo forced Codex to keep claims tied to receipts:

- public URLs were checked,
- role pages were re-checked,
- stale next steps were corrected,
- inaccessible surfaces were marked as capture gaps instead of invented evidence.

Product signal:

- Agent workflows need built-in language for evidence state:
  - verified,
  - user-reported,
  - inaccessible,
  - stale,
  - inferred,
  - needs capture.

## Where Codex Drifted

### 1. It Repeated Stale Next Steps

After Noah had already applied, sent two DMs, posted on LinkedIn, and posted an X thread, Codex still started from "apply/post/send" steps.

Product risk:

- Long-running agents can regress to the previous plan even after the user changes the state.

Useful product behavior:

- Before proposing next steps, Codex should run a current-state diff:
  - What was planned?
  - What is now reported done?
  - What can be independently verified?
  - What remains blocked?

### 2. It Could Not Fully Inspect External Distribution State

Codex could verify some public surfaces:

- GitHub repo,
- GitHub Pages,
- Open Graph image,
- OpenAI role pages,
- connected Gmail account,
- GitHub traffic/counters.

Codex could not verify:

- whether `hey@noahkuhn.com` received application mail,
- LinkedIn post URL or activity,
- X thread content from the fetched page,
- DM recipients or replies,
- application confirmation.

Product risk:

- Without explicit capture state, the agent may overstate certainty or choose a premature second wave.

Useful product behavior:

- Make "external surface unavailable" an explicit task state.
- Give the user a short capture checklist instead of asking broad questions.
- Preserve the difference between no signal, no accessible signal, and no verified signal.

### 3. It Needed The User To Defend The Objective

The objective was not "make a nicer repo."

The objective was "get OpenAI to care."

Codex repeatedly improved artifacts, but Noah had to keep forcing the work back to conversion:

- application,
- direct routing,
- public signal,
- role fit,
- follow-up.

Product risk:

- Agents can optimize the local artifact and lose the real-world objective.

Useful product behavior:

- Keep the success criterion visible in the workspace.
- Require every new artifact to state how it moves the objective.
- Flag when work is becoming polishing rather than conversion.

## Product Opportunities

### 1. A Native Evidence Ledger

Codex workflows need a structured way to track:

- claim,
- source,
- verification status,
- public/private visibility,
- last checked date,
- next capture step.

This would reduce accidental overclaiming and make agent work easier to audit.

### 2. Current-State Reconciliation

Before continuing a long-running goal, Codex should reconcile:

- previous plan,
- user-reported updates,
- repo state,
- external tool state,
- blocked surfaces.

The output should be a compact "state changed" report before action.

### 3. Objective Drift Detection

Codex should identify when it is spending effort on work that does not move the declared outcome.

For this project, the warning would be:

> You are improving launch artifacts, but the objective is an OpenAI conversation. Should the next action be distribution, application, or response tracking instead?

### 4. Better Social/Application Capture

For public proof-of-work campaigns, Codex needs a clean capture path for:

- application confirmations,
- post URLs,
- DMs,
- public replies,
- traffic snapshots,
- profile visits,
- warm introductions.

This should not require dumping private inboxes or screenshots into a public repo. It needs private evidence with public-safe summaries.

### 5. Correction Memory That Changes Behavior

When the user says "that is not the goal," Codex should turn that into an active constraint, not just a note.

For this project:

- Do not default to crypto or existing projects.
- Do not hide the process.
- Do not polish away human correction.
- Do not repeat launch steps already done.
- Do not treat inaccessible surfaces as negative evidence.

## What This Shows About Fit

For AI Deployment Engineer - Codex:

- This is a real example of using Codex to design, validate, package, and explain a workflow.
- It generated concrete product feedback about adoption, evidence, correction, and current-state handling.

For Deployed Product Manager, Codex:

- This is customer/operator feedback translated into product opportunities and routing decisions.
- It shows the connective tissue between goal, workflow, artifact, blocker, and next action.

For Codex App:

- This is a live trace of human-agent UX needs:
  - state,
  - progress,
  - uncertainty,
  - handoff,
  - correction,
  - evidence,
  - and control.

## Bottom Line

Codex helped produce the public proof.

The deeper value is the trace of where it needed supervision.

That trace is the product feedback.
