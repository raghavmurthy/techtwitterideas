# The ~150-item checklist a vibe-coded app needs before paying customers

**X post:** https://x.com/mardehaym/status/2110705357492203564  
**Author:** Mark Ajzenstadt (@mardehaym) · posted 2026-10-15 (UTC) · 8736 likes, 702 replies  

## What it is
Mark Ajzenstadt, founder of LimestoneHQ (which embeds AI engineers into PE-backed companies, per his X bio), answers people who say they vibe-coded an app over a weekend and no longer need developers. He lists roughly 150 things the app needs before it touches a paying customer, grouped here:
- **Data:** a designed schema, migrations that roll forward and back without locking tables, indexes, connection pooling, nightly backups with tested restores, point-in-time recovery, soft deletes, money stored as integers, correct timezones, pagination, imports and exports.
- **Auth and security:** robust login and password reset, MFA with recovery, session timeouts and kill-switches, SSO/SAML/SCIM for enterprise, real roles and per-record access checks, tenant isolation, rate limits and lockouts, OWASP protections, secrets kept out of the code and the AI chat history, rotating keys the AI pasted into config, checking that every package the AI installed is real, and dependency scanning.
- **Compliance:** SOC 2, HIPAA and BAAs, PCI scope, GDPR deletion that reaches backups and logs, data residency, audit trails and access reviews.
- **Ops:** matching environments, infrastructure as code, CI that runs tests, one-click rollback, zero-downtime deploys, feature flags, queues with retries and dead-letter queues, email deliverability, cost alerts (he says a runaway agent loop cost them $1,382.59), disaster recovery, logs, error tracking, alerts, on-call and runbooks.
- **Testing:** unit, integration, end-to-end, load and regression tests, plus testing on old hardware and for accessibility.
- **Billing and API:** proration, dunning, tax, refunds, metering, signed and retried webhooks, a versioned API, and handling third-party API changes.
- **AI-specific:** prompt-injection protection, keeping customer data out of prompts, per-customer model spend caps, evals for model updates, provider fallback and deprecation plans, and human approval for anything irreversible.
- **UX and code health:** empty, loading and error states, undo, localisation, code review, dependency upgrades, deleting the AI's dead code, splitting giant files, written architecture decisions, and a bus factor above one.

He closes by listing the people still needed, from a senior engineer reading every line the AI wrote to someone who remembers why it was built that way a year later.

## Thread highlights
> **@hamzaalibasra:** users forgive janky UI but never lost data or broken login. The boring checklist IS the product.

> **@Xkosa8:** the agent that built it shouldn't still have prod credentials and open internet. Scope what it can reach before it ships, not after.

> **@LynnBuildsdn:** A restore test belongs on that list too: can you recover the data after a bad migration? A demo running successfully doesn't answer that.

## Implications
- Use it as a pre-launch audit: have an agent go through the list against your repo and mark each item done, not needed, or missing, with evidence.
- For games with online features (accounts, saves, leaderboards, purchases), the data, auth, billing and ops sections apply almost unchanged: think cloud-save restores, idempotent purchases and per-player cost caps on AI features.
- The AI-specific items (spend caps, evals, provider fallback, approval for irreversible actions) are the newest and the easiest to skip.
- **Experiment:** paste the section headings into an agent session for an existing project, ask it to audit only the "Data" and "AI-specific" sections with file and line evidence, then fix the top three gaps.

## Tags
`checklist` `launch` `security` `vibe-coding` `ops` `testing`
