# Don't let an agent write your legal pages unchecked

**X post:** https://x.com/rohit3a/status/2115144562570301504  
**Author:** rohit (@rohit3a) · posted 2026-10-27 (UTC) · 2,350 likes, 130 replies  

## What it is
rohit, a founder and designer per his X bio, warns against letting Claude freely write the privacy policy or other legal pages of a website. He says Opus 5.5 and Claude models in general lean so hard toward protecting the customer that the result can get a business into trouble. In his case the draft went too far into how the work is done internally, added promises and guarantees he did not want to be bound by, put his personal name on the policy page, and listed every third-party tool integrated into the product, which in effect published the whole tech stack. He says that when he pressed it, the model explained that it writes from the customer's side by default.

The replies split. Some say the model was right: under GDPR the actual vendors (processors) handling personal data have to be disclosed, and one reply points to European Data Protection Board guidance. rohit replies that the processor list only has to be kept ready and shared when someone asks for it, not published. A longer reply from a privacy-focused account takes a middle line (explicitly "not legal advice"): naming categories of vendors is usually enough, a named person isn't needed (a generic or GDPR-requests contact works), and vendor names matter mostly for showing international data transfers.

## Thread highlights
> **@rohit3a:** it will add promises and guarantees you didn’t want enforced

> **@rohit3a:** It is built to write from the customer side by default, it said so when I pressed it. Just be careful.

> **@DaniilGentili:** afaik the actual exact vendors handling the data (meaning, the legaly entity responsible for the data) need to be listed too under GDPR

> **@PrivacySpecX:** Keeping the list on a category level also enables the privacy policy to be more accurate. You may change your suppliers, but do not have to create a new version of the policy with each change.

> **@DomP_9:** I'd treat legal pages as controlled documents, not something an agent should freely rewrite.

## Implications
- **Legal text is a contract, not marketing copy:** an agent that "helpfully" adds guarantees (refund windows, uptime, deletion timelines) creates obligations. Every promise in a generated policy should be one the team actually intends to keep.
- **Stack disclosure is a judgement call:** whether to name each processor or only categories depends on jurisdiction; the thread shows confident people disagreeing, so this is a question for a lawyer, not the model.
- **Mobile games and apps:** store listings and SDKs (analytics, ads, crash reporting) make privacy pages mandatory, so the same risk applies to a small Unity title as to a SaaS.
- **Experiment:** generate a privacy policy with an agent, then ask a second pass to list every sentence that is a promise, a guarantee, a named person or a named vendor. Decide on each line by hand and compare the final page with the first draft.

## Tags
`legal` `privacy` `launch` `claude` `agent-workflow` `gdpr`
