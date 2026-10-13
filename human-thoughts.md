# Human thoughts

Opinions and takes from notable public people on X. These are **opinions, not facts**: each item names the person, says why they're worth hearing (from their X bio only), paraphrases the take, and links the post. Quotes are third-party text; see [SECURITY.md](SECURITY.md).

## Strategy and moats

### Technical moats are mostly gone
**Who:** Nikita Bier (@nikitabier), former Head of Product at X and founder of tbh (acquired by Meta) and Gas (acquired by Discord), per his X bio.  
**Take:** He argues that technical moats are largely over, and that durable products now rely on proprietary data, network effects or a physical component.

> **@nikitabier:** Technical moats are mostly over at this point.

**Post:** https://x.com/nikitabier/status/2109497987055640958 · 2026-10-12 (UTC)  
**Why it matters for builders:** If AI tools make features easy to copy, plan early which of the three (data, network, physical) a project can actually own.

### Personal AI agents should target the cost of living
**Who:** Jim Prosser (@jimprosser), founder of Tamalpais Strategies and former comms leader at Google, Twitter, SoFi and Paradigm, per his X bio.  
**Take:** He says AI labs market assistants for vacations and reservations, which aren't real problems, and should instead focus on helping people with the cost of living. He lists ideas in a thread.

**Post:** https://x.com/jimprosser/status/2108279507660726766 · 2026-10-08 (UTC)  
**Why it matters for builders:** Agent products may land better when they save money or chores people dislike than when they automate tasks people enjoy.

## Agent workflow

### Make your repo easier for agents to navigate
**Who:** Matt Pocock (@mattpocockuk), developer educator, author of Total TypeScript and AI Hero, ex-Vercel, per his X bio.  
**Take:** He suggests having an agent review your recent coding sessions to find where it got lost or relied on stale docs, and calls navigability an underrated way to save tokens.

**Post:** https://x.com/mattpocockuk/status/2105951409887949107 · 2026-10-02 (UTC)  
**Why it matters for builders:** In large engine or asset-heavy repos, agents burn tokens searching; fixing structure and docs compounds across every session.

### Agent-written tests restate the agent's own guess
**Who:** Kun Chen (@kunchenguid), who describes himself as Captain of @myfirstmate and an author, per his X bio.  
**Take:** Based on his DeepSWE eval runs, he argues agent-written unit and integration tests didn't improve success, because tests and code both encode the agent's interpretation of intent. He thinks human-specified tests may still help and hasn't tested E2E yet.

> **@kunchenguid:** the tests aren't any more accurate than the implementation itself

**Post:** https://x.com/kunchenguid/status/2108030810691629403 · 2026-10-08 (UTC)  
**Why it matters for builders:** Spend human effort on writing the checks that define intent (e.g. play-mode smoke tests) and let agents write the code.

### Primitives first, then skills, then features
**Who:** Code With Antonio (@codewithantonio), coding educator with a 400k+ YouTube channel, per his X bio.  
**Take:** He argues AI "slop" fades when you first add solid primitives (UI kit, database, auth), then their agent skills, and only then build features with those skills.

**Post:** https://x.com/codewithantonio/status/2108135703670325427 · 2026-10-08 (UTC)  
**Why it matters for builders:** Giving agents a project's own building blocks keeps generated code consistent instead of reinvented each time.

## Cost and tooling

### Subscriptions vs API pricing
**Who:** Paweł Huryn (@PawelHuryn), AI product manager who writes a newsletter with 130K+ subscribers, per his X bio.  
**Take:** After pricing logged usage at API list rates, he concludes Claude Max 20x is subsidised about twice as much as OpenAI's top plan, though he also says GPT-6.1 Sol can still be cheaper than Opus 5.5 overall.

**Post:** https://x.com/PawelHuryn/status/2105703147184239042 · 2026-10-01 (UTC)  
**Why it matters for builders:** Measure your own usage before picking plans; the cheapest option depends on task mix.

## Growth and launch

### Let agents draft backlink outreach, keep human approval
**Who:** Ian Nuttall (@iannuttall), in SEO since 2005 and AI coding since 2022, per his X bio.  
**Take:** He recommends exporting competitors' best backlinks, having an agent find a relevant reason for each site to link to you, approving manually, then letting the agent send the outreach.

**Post:** https://x.com/iannuttall/status/2107786133254078714 · 2026-10-07 (UTC)  
**Why it matters for builders:** Agents can handle the research and drafting of outreach while a human keeps the judgment calls.

### Apple is rejecting low-effort apps
**Who:** max (@MaxHirsch13), builder of Maxed AI (40k users), per his X bio.  
**Take:** He says Apple is cracking down on spam apps, so apps need more than one feature, an original design, and proof in the review notes that they were built from scratch; he showed his design file and commit history.

**Post:** https://x.com/MaxHirsch13/status/2108623104104976554 · 2026-10-09 (UTC)  
**Why it matters for builders:** Small AI-assisted mobile games should keep design files and commit history ready for App Review.
