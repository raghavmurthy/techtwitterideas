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

### Software gets rewritten by and for agents
**Who:** jacob (@jsnnsa), founder of Spawn, per his X bio.  
**Take:** He lays out views he says he has formed over several years. On software: it becomes either entertainment or coordination between AI agents; the end state has no SaaS, no apps, no harnesses and no banks; all software is rewritten by and for agents; new software uses low-level APIs humans can't read (in games, he says, Claude draws pixels and triangles from math); and because money can now buy what used to take time and careful hiring, capital matters more than ever. On people: work ends, and people find community and purpose in exploration, games, self-mastery and creating for and with each other. On models: specialist image, video, 3D, voice and physical-intelligence models lose to general models, surviving only while compute is scarce, which he expects to end; one-shot output keeps feeling like slop because its range is shallow and easy to recognise, so for a while small teams stay around to add variety to the creative process; large models gain high-bandwidth sensory input, most domains prove verifiable enough for reinforcement learning, and online learning arrives first from a lab that is behind. His longer-range claims include almost all compute being in space by 2040, much of Mercury disassembled by then, religion returning to the centre of society, louder AI-rights debate, AI and humans coexisting the way countries do, and the singularity having started in the mid-1900s. Pressed in replies on what unreadable game software means, he clarifies he isn't saying Claude becomes the renderer: Claude writes code that generates models, scenes and animations, an engine renders them much as today, and that code is not human-legible but Claude can read and edit it, which he calls strong compression, "something like 200x". He expects the change to be gradual and to track model capabilities, with no sudden moment where everything is free. Critics in the replies call the software predictions needlessly convoluted, and one dismisses the post as slop.

> **@jsnnsa:** all software will be rewritten by and for agents
>
> **@jsnnsa:** new software will use low level apis that are not understandable by humans (in games claude draws pixels and triangles from math)
>
> **@jsnnsa:** image/video/3d/voice/physical intellgence etc specialist models die to general models like claude
>
> **@jsnnsa:** claude writes code that generates the models, scenes, and animations, which an engine renders much like today. that code is not human legible, but claude can read and edit it just fine.

**Post:** https://x.com/jsnnsa/status/2114566172163407964 · 2026-10-26 (UTC)  
**Why it matters for builders:** For 3D and game work, the concrete version of this bet is procedural content written as code by agents (geometry, scenes, animation) rather than hand-made or specialist-model assets; it's speculative, but cheap to test on small props, and the compression claim is worth checking against exported meshes.

### One person plus AI can run several drug programs at once
**Who:** Cody Tranbarger (@Prof_Oak_), founder of Mithril Medicine, a one-person biotech acquired by Anthropic, per public reporting (Anthropic's Oct 27, 2026 announcement); his X bio describes him as buyside turned operator in biopharma.  
**Take:** Writing for six years as the anonymous "Professor Oak", he reveals that Anthropic acquired his company and that he is joining it. He describes Mithril, which develops bispecific antibodies for LAMA2-CMD and other genetic diseases of the extracellular matrix, as starting virtual, decentralised and very lean, and says it stayed that way for unusually long because AI tools matured quickly. It became an experiment in how far one operator plus Claude (and a bench of part-time consultants) could scale. After working with people at the frontier of AI he came to see it not as an experiment but as a preview of a new operating model, which he calls "Pipeline-in-a-Person"; he says that idea was central to the acquisition. He gives three reasons for joining: the existing programs continue with more resources, he gets to start several more and find out how many one person can run in parallel, and Anthropic offers a path to scale this way of working across biopharma. His core claim is that AI will help cure diseases, but not mainly by compressing timelines, which gets the most attention; the low-hanging fruit today is orchestration and parallelisation. Drug hunters make only a handful of go/no-go calls in a career and spend much of their time on email; give them bandwidth to run several programs and time for scientific judgement, and he bets they will make better calls, which at scale means more drugs and higher hit rates. Anthropic's own post says Claude organised contracts, logistics and experiments with 11 external labs, and that one candidate went from idea to promising results in mice in under 18 months. Replies include sharp scepticism: one calls it IPO hype and argues a clinician with a track record would have been the choice if new medicines were the priority.

> **@Prof_Oak_:** Eventually, Mithril became a bit of an experiment itself - to find the upper bound of how far it could scale as a single operator + a bunch of Claude (+ a stellar bench of part-time consultants).
>
> **@Prof_Oak_:** Rather than timeline acceleration & compression, I see orchestration & parallelization as today's low-hanging fruit.
>
> **@Prof_Oak_:** Give them the bandwidth to run several programs at once, and the time to focus on scientific judgment, and I’m willing to bet they’ll make better calls.

**Post:** https://x.com/Prof_Oak_/status/2115185849424048564 · 2026-10-27 (UTC)  
**Why it matters for builders:** For solo developers the same bet applies: let agents carry the coordination and admin so one person can keep several projects or prototypes moving and spend their own time on judgement calls.

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

### Agent slop is preventable if someone sets the bar
**Who:** Theo (@theo), full-time CEO of T3 Code and T3 Chat and part-time YouTuber, investor and developer, per his X bio.  
**Take:** He reports that an agent's pull request was blocked because it added 100 bytes to a payload, and draws one conclusion: slop from agents can be prevented, you just have to care enough to do it. That is the whole post; he didn't expand on it in the thread, and he doesn't say whether the block came from an automated size check or a human reviewer. Replies fill in the reasoning: one says a human adds 100 extra bytes once while an agent adds them in every PR until something says no, so hard budgets beat review comments because the agent can't argue with a number; another describes running anti-slop checks and typechecks as hooks after every edit plus a pre-push gate, because agent PRs touch too many files to review reliably by eye.

> **@theo:** Just had an agent's PR get blocked because it added 100 bytes to a payload.
>
> **@theo:** You can prevent the slop, you just have to care enough to do it.
>
> **@siddhantmohan1:** A human adds 100 extra bytes once. An agent adds them in every PR until something says no. Hard budgets like payload size beat review comments because the agent can't argue with a number.

**Post:** https://x.com/theo/status/2115611204001661029 · 2026-10-29 (UTC)  
**Why it matters for builders:** Size budgets in CI (bundle size, build size, texture memory, draw calls) let agents work freely while blocking the slow bloat that reviewers miss.

## Cost and tooling

### Agents can now out-build big rewrite teams
**Who:** Peter Steinberger (@steipete), creator of OpenClaw who now works with OpenAI, per his X bio, and founder of PSPDFKit, per public reporting.  
**Take:** He says he switched to tsrs, VoidZero's new Rust port of the TypeScript compiler, over a weekend, that it was a drop-in replacement, and that it runs about 5x faster for what he calls "OC" (presumably OpenClaw). His broader point is a contrast: it took Microsoft a dedicated team and two years to rewrite the TypeScript compiler in Go, while now "you can just let an agent rip" and get something significantly better within weeks. The post he quotes is VoidZero's announcement, which says tsrs is built in close collaboration with the TypeScript team (not a fork), claims up to 8x the speed of TypeScript 7.0 with about 70% less memory, and runs in WASM. He doesn't add more in the thread. Replies push back that a Rust port may build directly on Microsoft's two years of work, and that "drop-in" should be checked by diffing its errors against the official compiler across a whole codebase, since tricky generics are where ports diverge.

> **@steipete:** Moved to tsrs over the weekend. Drop-in replacement. Around 5x faster for OC.
>
> **@steipete:** Kind of amazing that it took Microsoft a team and two years to rewrite the TS compiler in go, and now you can just let an agent rip and get sth significantly better within weeks.

**Post:** https://x.com/steipete/status/2112571535731106013 · 2026-10-20 (UTC)  
**Why it matters for builders:** Large rewrites with a strong existing test suite (compilers, importers, format converters) are where agents may now beat a team on speed, but the test suite is what makes the result trustworthy.

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

### ChatGPT plugins are an early app-store moment
**Who:** Corey Ganim (@coreyganim), who helps non-technical entrepreneurs use AI and previously founded a $16M e-commerce startup, per his X bio.  
**Take:** He argues ChatGPT plugins are "the App Store in 2008 all over again": ChatGPT has about 900M weekly users, anyone can now publish a plugin, and almost nobody is building there yet. He defines a plugin as a skill (how to do the job) plus a connector (access to your apps), and describes the funnel as: a user asks ChatGPT for help, it suggests your plugin, they use it, then they buy. His playbook is a free plugin with a paid upgrade, and he lists six business types it suits: bookkeepers (categorise a month of transactions free, upsell done-for-you books), real estate agents (listing copy and comps that funnel to the brokerage), fitness coaches (a free week of workouts, upsell 1:1 coaching), plumbers and HVAC (a diagnosis plugin that books the service call), agencies (an ads or SEO audit that ends in a strategy call) and consultants (turn an intake questionnaire into a free first diagnosis). He says now is the time because publishing just opened to everyone, and the next step is ChatGPT recommending plugins on its own, which he says is already starting, so being early in a niche is a big advantage. The post he quotes, from another founder, gives the build steps: an MCP server as the product surface, tool names and descriptions written for the model, UI added later, a privacy policy and test cases for review, and billing kept on your own backend.

> **@coreyganim:** This is the App Store in 2008 all over again...
>
> **@coreyganim:** A plugin is just two things in one box: a skill (how to do the job) + a connector (access to your apps). Someone asks ChatGPT for help, it suggests your plugin, they use it, then they buy.
>
> **@coreyganim:** The next step is ChatGPT recommending plugins on its own (it's already starting to do this), and being early in your niche is a massive competitive advantage.

**Post:** https://x.com/coreyganim/status/2112880525555687563 · 2026-10-21 (UTC)  
**Why it matters for builders:** Replies doubt it, saying users may just ask the model to do the job without a plugin, but a free, useful plugin that leads to a paid product is a cheap distribution channel to test.

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
