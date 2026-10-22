# A benchmark of how models handle pushback: GPT-4o caves, Opus 5.5 digs in

**X post:** https://x.com/Che0dan/status/2112126344381550795  
**Author:** Che0dan (@Che0dan) · posted 2026-10-19 (UTC) · 1,713 likes, 71 replies  

## What it is
A Korean-language post summarising a paper (linked in the original post, not read here) that measures how models respond to user pushback, separating valid corrections from baseless ones. Per the post: GPT-4o changed its answer in response to baseless pushback 94.6% of the time, which the author calls a yes-bot; Claude Opus 5.5 accepted valid pushback only 32.2% of the time, so it often refuses to admit a real mistake; GPT-6 Astra accepted valid pushback 88.3% of the time. The author notes the results come from a specific document-evaluation setting and concludes that not being sycophantic and actually being correctable are two separate qualities.

## Thread highlights
> **@GillibertLuc:** According to this benchmark GPT 4o changes MORE its opinion from invalid feedback than from valid feedback...

> **@roanoke_gal:** no wonder opus feels unbearable to work with.

> **@robertomasymas:** hillarious, and actually very promising bench

## Implications
- **Agent workflows:** a model that resists valid correction can keep defending a broken approach in a long coding session; when it pushes back twice, give evidence (a failing test, an error log) rather than just disagreeing.
- **Review setups:** for reviewer or "skeptic" agents, stubbornness can be useful; for the builder agent it's a cost. Pick models per role with this in mind.
- **Experiment:** prepare five cases where your preferred model gave a wrong answer and five where it was right, push back on each with the same wording, and record how often it changes its answer correctly versus incorrectly.

## Tags
`models` `benchmarks` `sycophancy` `claude` `agent-workflow`
