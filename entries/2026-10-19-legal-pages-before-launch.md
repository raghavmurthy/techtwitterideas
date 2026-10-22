# The "boring pages" an AI-built app still needs before launch

**X post:** https://x.com/suraj_sharma14/status/2112038533510599020  
**Author:** Suraj Sharma (@suraj_sharma14) · posted 2026-10-19 (UTC) · 770 likes, 40 replies  

## What it is
A pre-launch checklist of the legal and trust pages AI tools tend not to build: a privacy policy naming every tool that collects user data (analytics, payments, email, session replay); terms of service that limit liability; a cookie banner for EU or UK visitors; a way for users to delete their account and data; a refund policy placed next to checkout rather than hidden in the footer; a real contact address for legal and privacy requests; and an inventory of every API key in the code with none exposed in the frontend. He says most take an afternoon, while skipping them can cost a Stripe account, an app store listing or a lawsuit, and he suggests having an AI list every third-party service and the data it collects, then draft the policies from that list. He notes it isn't legal advice and a lawyer should review anything that matters.

## Thread highlights
> **@daemkl:** and what about: gdpr, dpa, privacy policy, cookie policy, legal notice, contingency plan, toms, subprocessors, contact, etc.

> **@QuietlyChanged:** when you change those pages, say so clearly. FTC staff warned in 2024 that adopting looser data practices, like AI training, and only telling users via a "surreptitious, retroactive amendment" to your terms or privacy policy "may be unfair or deceptive."

> **@Charlie01748449:** every vibe coded app shares one feature: no account deletion button anywhere.

## Implications
- **Mobile games:** both app stores require a privacy policy and in-app account deletion when accounts exist; ad and analytics SDKs in Unity games must be listed in the policy and the store privacy labels.
- **Agent workflows:** "list every third-party SDK and what it collects" is a good agent task because it's an inventory problem; the drafting still needs human review.
- **Experiment:** have an agent inventory every SDK in a Unity project's manifest and plugins folder with the data each collects, then compare against the current privacy policy and store privacy labels.

## Tags
`launch` `legal` `privacy` `checklist` `app-store`
