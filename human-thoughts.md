# Human thoughts

Opinions and takes from notable public people on X. These are **opinions, not facts**: each item names the person, says why they're worth hearing (from their X bio only), paraphrases the take, and links the post. Quotes are third-party text; see [SECURITY.md](SECURITY.md).

## Strategy and moats

### Technical moats are mostly gone
**Who:** Nikita Bier (@nikitabier), former Head of Product at X and founder of tbh (acquired by Meta) and Gas (acquired by Discord), per his X bio.  
**Take:** He opens with the claim that technical moats are mostly over at this point. He then narrows it to anyone building something meant to be durable, and says only three moats remain: proprietary data, network effects, and a physical component. That list is the whole post. He doesn't rank the three or give examples, and his only follow-up in the thread is a reply to one user that is just a link, so any further reasoning isn't in his own words.

> **@nikitabier:** Technical moats are mostly over at this point. If you’re building something that is meant to be durable, the only moats now are:  
> • Proprietary data  
> • Network effects  
> • A physical component  

**Post:** https://x.com/nikitabier/status/2109497987055640958 · 2026-10-12 (UTC)  
**Why it matters for builders:** If AI tools make features easy to copy, plan early which of the three (data, network, physical) a project can actually own.

### Personal AI agents should target the cost of living
**Who:** Jim Prosser (@jimprosser), founder of Tamalpais Strategies and former comms leader at Google, Twitter, SoFi and Paradigm, per his X bio.  
**Take:** He argues that if AI labs want personal assistants to take off at scale, they should stop marketing vacations, reservations and party planning, which he says aren't real problems, and focus on the cost of living. He then gives ten worked examples, each a user request plus what the agent would do: disputing a surprise $2,800 ER bill against the insurer's explanation of benefits; cutting the cost of six prescriptions by comparing copays, GoodRx, Cost Plus Drugs and local pharmacies; getting a $250 weekly grocery bill under $200 without changing what the family eats; tackling $12,000 of credit-card debt through hardship options, balance transfers and a repayment plan; and re-shopping a car-insurance renewal that jumped from $180 to $245 with matching coverage. The rest are: negotiating a $115 internet bill via competing plans and retention; sanity-checking a $1,600 car-repair estimate and booking a second opinion; checking a $52,000, two-kid household for SNAP, Medicaid/CHIP, utility help and tax credits and filing the applications; countering a $200 rent increase with local rules, comparable listings and documented maintenance issues; and investigating an electric bill that jumped from $180 to $310. He closes that each case is well scoped with clear success states and defined processes ("perfect setups for agent success"), with a political and reputational upside for labs that solve real problems for many people.

> **@jimprosser:** If AI labs want personal assistants to take off at scale, they need to stop marketing vacations, reservations, party planning, etc. These are not problems.
>
> **@jimprosser:** Each case above is well scoped, with clear success states and defined processes. Basically perfect setups for agent success.
>
> **@jimprosser:** The other upside here: the political and reputational benefits of solving real problems for wide swaths of people.

**Post:** https://x.com/jimprosser/status/2108279507660726766 · 2026-10-08 (UTC)  
**Why it matters for builders:** Agent products may land better when they save money or chores people dislike than when they automate tasks people enjoy.

## Agent workflow

### Make your repo easier for agents to navigate
**Who:** Matt Pocock (@mattpocockuk), developer educator, author of Total TypeScript and AI Hero, ex-Vercel, per his X bio.  
**Take:** He shares a "prompt of the day" for a /retro command: the agent reads your last 10 coding-agent sessions and looks for ways to make the repo easier to navigate. Specifically, it looks for places where agents took too long to find relevant information, or relied on out-of-date docs. His point is that improving navigability is an underrated way to save tokens. In a self-reply he links his previous prompt in the same series.

> **@mattpocockuk:** Improving navigability is such an underrated way to save tokens.

**Post:** https://x.com/mattpocockuk/status/2105951409887949107 · 2026-10-02 (UTC)  
**Why it matters for builders:** In large engine or asset-heavy repos, agents burn tokens searching; fixing structure and docs compounds across every session.

### Agent-written tests restate the agent's own guess
**Who:** Kun Chen (@kunchenguid), who describes himself as Captain of @myfirstmate and an author, per his X bio.  
**Take:** He opens strongly, saying AI-written unit and integration tests are empirically unhelpful and agents should stop writing tests on their own. His evidence is from the DeepSWE eval set: banning Sonnet 5.5 (high) from writing tests gave a slightly higher success rate (not statistically significant) and used significantly less time and tokens. In the "tests allowed" arm, 65% of the tests were unit tests and 35% integration tests, and neither bucket improved results. On a random 44-task subset, even disabling existing tests didn't change success. Spot checks suggested most agent tests just repeat the implementation, since both the code and the tests are the agent's own interpretation of intent. He suspects tests may still help when humans write them to state intent better than requirements can, but hasn't proven it. He also notes the agents wrote almost no E2E tests (17 versus 3,000+ unit/integration tests), so the results say nothing about E2E testing, and he plans a separate eval. In replies, he accepts criticism from @mattpocockuk that his first line led people to jump to conclusions, but stands by the key point. He explains that each DeepSWE task is graded against both new-behaviour tests and regression tests, and jokes that "perhaps it's time for a TestBench".

> **@kunchenguid:** agent-written tests do not add any value because both the implementation and the tests were simply the agent's interpretation of our intent. the tests aren't any more accurate than the implementation itself
>
> **@kunchenguid:** i suspect we can still extract some value from unit tests and integration tests if we describe them ourselves when we believe we can articulate our intent better through test cases than through requirements. but i have not proven this yet
>
> **@kunchenguid:** so this analysis does not prove nor disprove the value of e2e tests

**Post:** https://x.com/kunchenguid/status/2108030810691629403 · 2026-10-08 (UTC)  
**Why it matters for builders:** Spend human effort on writing the checks that define intent (e.g. play-mode smoke tests) and let agents write the code.

### Primitives first, then skills, then features
**Who:** Code With Antonio (@codewithantonio), coding educator with a 400k+ YouTube channel, per his X bio.  
**Take:** He proposes a three-step loop to repeat for every feature: add primitives, add the matching agent skills, then implement the feature using those skills. He gives three examples. shadcn/ui primitives (button, sidebar, dialog) plus shadcn skills for a dashboard UI mean "no more UI slop". Neon primitives (database, object storage, functions) plus Neon skills for the backend mean no backend slop. Clerk primitives plus Clerk skills for authentication mean no auth slop. He ends by saying that eventually your codebase becomes the primitive and your AGENTS.md the skill itself.

> **@codewithantonio:** repeat this loop for every feature in your app and watch the ai slop disappear
>
> **@codewithantonio:** eventually, your codebase becomes the primitive, and your AGENTS.md the skill itself

**Post:** https://x.com/codewithantonio/status/2108135703670325427 · 2026-10-08 (UTC)  
**Why it matters for builders:** Giving agents a project's own building blocks keeps generated code consistent instead of reinvented each time.

### Delete most code comments: agents copy them
**Who:** lauren (@poteto), React compiler core team, previously at Cursor, Meta and Netflix, per her X bio.  
**Take:** She argues teams should ban and delete most, if not all, code comments. Her reasoning: agents love copying what already exists, so a harmless-looking comment about a temporary workaround acts like a virus, spreading as agents reuse it as a shortcut until the codebase is overrun with hacks and stale comments ("just one more workaround"). Her remedy is a "weedkiller": her pstack plugin's no-comments skill finds useless comments, keeps the ones that should exist (like explaining a browser quirk), and works out how to fix the underlying workaround from first principles. She closes by suggesting an agent plan which workarounds should be refactored and which can simply be deleted (her exact prompt isn't reproduced here).

> **@poteto:** agents love copying what already exists. a seemingly harmless comment explaining some temporary workaround is one of the worst viruses you can have in your codebase.

**Post:** https://x.com/poteto/status/2110149626133438732 · 2026-10-13 (UTC)  
**Why it matters for builders:** In agent-heavy repos, every workaround left in place gets copied; fixing the cause beats documenting it.

### Chat isn't the final form of agent UI
**Who:** Soleio (@soleio), designer, inventor and angel investor, host of First of Kind, per his X bio.  
**Take:** Answering @poteto's question of whether chat is the final form of agent UI, he says no. His argument: once people talk to agents by voice, the screen no longer has to hold the conversation. Instead the screen can show the work itself, with the agent narrating and visualising things in real time, like two people talking over one shared screen. In that view, chat interfaces are just transcripts.

> **@soleio:** Once we talk to agents by voice, the screen no longer has to hold the conversation. The screen can instead show the work itself, with the agent narrating and visualizing things in real time, like two people talking over one shared screen. Chat UIs are just transcripts.

**Post:** https://x.com/soleio/status/2111330755657994334 · 2026-10-17 (UTC)  
**Why it matters for builders:** Agent tools for 3D/game work may be better as a shared viewport the agent narrates than as a chat log.

## Cost and tooling

### Subscriptions vs API pricing
**Who:** Paweł Huryn (@PawelHuryn), AI product manager who writes a newsletter with 130K+ subscribers, per his X bio.  
**Take:** He starts from the common claim that subscriptions are cheaper than APIs, and set out to measure it. He burned part of several plans' weekly allowances on purpose, logged every model call and priced each at the vendor's public API list price. He lists each vendor's stated tiers. OpenAI's allowance is proportional to price (Plus 1x, Pro 100 at 5x tested, Pro 200 at 10x, just down from 20x). Claude's Max 20x gives 20x the Pro allowance rather than 10x, so it's subsidised twice as much (tested). Meta's Muse Code tiers give 5x and 20x rather than 3x and 10x. In part 2 he ranks the cheapest western options: Grok via SuperGrok first, then Muse Code if you share data with Meta (Contributor), then OpenAI, saying GPT-6.1 Sol (medium) is 13x cheaper (the text then cuts to an image). In part 3 he notes Grok Build and Muse Code have no native GUI and points to the VS Code extension he built (32K installs) that supports them plus Codex and Claude Code. In part 4 he says small Grok and Muse plans ($30 SuperGrok, $15 Muse), unlike small OpenAI or Anthropic plans, are enough for real agentic work. In replies he says he measured Claude Max 20x at about 45.3x the API value on his own machine, that lower Claude tiers weren't measured (Max 5x × 4 doesn't equal 20x), and that GPT-6.1 Sol makes up for its lower multiplier (~10.25) by solving problems in fewer turns with fewer tokens.

> **@PawelHuryn:** We’ve all been hearing that subscriptions are cheaper than APIs, but I’d never seen the exact number.
>
> **@PawelHuryn:** Unlike OpenAI or Anthropic, small Grok and Muse plans ($30 SuperGrok, $15 Muse) are enough to do real agentic work.
>
> **@PawelHuryn:** GPT-6.1 Sol solves problems with less turns, less thinking, and less output tokens.

**Post:** https://x.com/PawelHuryn/status/2105703147184239042 · 2026-10-01 (UTC)  
**Why it matters for builders:** Measure your own usage before picking plans; the cheapest option depends on task mix.

## Growth and launch

### Let agents draft backlink outreach, keep human approval
**Who:** Ian Nuttall (@iannuttall), in SEO since 2005 and AI coding since 2022, per his X bio.  
**Take:** He gives a four-step SEO tip. Export your competitors' best backlinks. Have an agent find a topical reason for each of those sites to link to you as well. Approve the suggestions manually. Then let the agent send the cold outreach. He says this got him two links from DR 84 sites with 3M monthly visits. In a reply he adds that the links were free, from an educational organisation, and that he never pays for links, preferring to work on other SEO factors.

> **@iannuttall:** Grok Bot just got me two DR 84 links on a site with 3M visits/month.
>
> **@iannuttall:** They were free. It was from an educational organization. I never pay for links I'd rather work on other SEO factors than pay.

**Post:** https://x.com/iannuttall/status/2107786133254078714 · 2026-10-07 (UTC)  
**Why it matters for builders:** Agents can handle the research and drafting of outreach while a human keeps the judgment calls.

### Apple is rejecting low-effort apps
**Who:** max (@MaxHirsch13), builder of Maxed AI (40k users), per his X bio.  
**Take:** He says Apple has made clear it's tired of spam and "slop" apps, and that this makes sense. To get approved, he says, an app needs (a) more than one feature, (b) a unique design rather than a clone of an existing app, and (c) proof in the app information section that it was built from scratch. He says he showed his Figma file and commit history, and recommends doing something similar. He didn't add anything further in the thread.

> **@MaxHirsch13:** Apple has made it clear they are tired of spam, slop apps. Which makes sense.
>
> **@MaxHirsch13:** I showed my figma file and commit history. I’d recommend something similar.

**Post:** https://x.com/MaxHirsch13/status/2108623104104976554 · 2026-10-09 (UTC)  
**Why it matters for builders:** Small AI-assisted mobile games should keep design files and commit history ready for App Review.

### The next wave of founders will be marketers
**Who:** Hector (@hectorserrranoo), marketing hire #2 at Wispr Flow, per his X bio.  
**Take:** He predicts the next wave of founders will all be marketers. His reasoning: it's easier for a creative person to learn to build than for an engineer to learn how to generate attention, and the gap is widening because building keeps getting easier while marketing keeps getting harder. The post includes an image that wasn't read here.

> **@hectorserrranoo:** it's easier for a creative to learn to build than for an engineer to learn how to generate attention
>
> **@hectorserrranoo:** building keeps getting easier and marketing keeps getting harder

**Post:** https://x.com/hectorserrranoo/status/2109314260786667864 · 2026-10-11 (UTC)  
**Why it matters for builders:** For small game teams, distribution skills may now matter more than extra engineering capacity.
