# Live Launch Verification - 2026-05-05

Purpose: confirm the public audition is still inspectable before the next distribution push.

## Checks

- Public site: `curl -I https://noahkuhn.github.io/openai-audition/`
  - Result: `HTTP/2 200`
  - Content type: `text/html; charset=utf-8`
  - Last modified: `Sun, 03 May 2026 13:17:39 GMT`
- Open Graph image: `curl -I https://noahkuhn.github.io/openai-audition/assets/og/openai-audition-og-codex.png`
  - Result: `HTTP/2 200`
  - Content type: `image/png`
  - Content length: `282406`
- Public repo: `curl -I https://github.com/noahkuhn/openai-audition`
  - Result: `HTTP/2 200`
- Official OpenAI role page: <https://openai.com/careers/ai-deployment-engineer-codex-remote-us/>
  - Result: page is live and includes an apply link.
  - Current title: `AI Deployment Engineer- Codex`
  - Team/location: `Technical Success - Remote - US`
- Official OpenAI Codex search: <https://openai.com/careers/search/?q=codex>
  - Result: showed 23 Codex-related jobs on 2026-05-05.

## Findings

- The live site, share image, and public repo are reachable.
- The primary role target is still current enough to keep in the application path.
- The audit found two local credibility issues: `CASE_FILE.md` stopped its evidence list at older commits, and `RECEIPTS.md` had duplicate `Receipt 007` headings.
- This pass fixes those local evidence issues and records the verification as public evidence.

## Next Action

- Superseded by Noah's later 2026-05-05 update: application submitted, two DMs sent, one LinkedIn post published, and an X thread for the original project already posted.
- Track response signal in [../launch/follow-up-tracker.md](../launch/follow-up-tracker.md).
- Add a follow-up artifact only if the first distribution wave gets no signal or asks for deeper proof.
