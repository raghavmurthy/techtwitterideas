# An RWKV model that predicts recall directly, as an experimental Anki scheduler

**X post:** https://x.com/PantsuThief/status/2123277729235939752  
**Author:** Panty Thief (@PantsuThief) · posted 2026-11-19 (UTC) · 4,946 likes, 66 replies  
**Source:** the post, the author's replies, and the release notes of the Anki fork he links (https://github.com/JSchoreels/anki/releases/tag/26.09.4%2Bfsrs7.build.115)

## What it is
The author describes an experimental Anki scheduling algorithm that, in his view, beats every other one by a wide margin. Instead of fitting a forgetting curve, it uses an RWKV model (a hybrid RNN/transformer) to predict retrievability, the chance a card will be recalled right now. It can be run through an add-on, or, as he does, through a community fork of Anki. In replies he explains the difference: FSRS is a parameterised equation fit to one person's history, while this model learns many abstract memory patterns in pretraining and looks for them in the user's own review history when it builds a cached state. He prefers the "instantaneous" variant, which ranks cards by current recall instead of producing a schedule; Anki still computes an FSRS fallback curve so cards stay scheduled on mobile or if RWKV is switched off. He also reports odd but effective behaviour, like a struggling new card shown three times in one day and twice a few days later, after which it stuck.

The linked fork's release notes add concrete numbers: Big, Small and Tiny RWKV model sizes, with Tiny's per-card state about 5.3 KB versus Small's 7.1 KB (26% less) at a small accuracy cost; dedicated models for the instant recall query; and an answer-time prediction with 17.3% lower log loss than a per-button running-median baseline on held-out reviews.

## Thread highlights
> **@PantsuThief:** FSRS is a parameterized equation fit to your history, this model encodes 100, 1000s, who knows how many abstract patterns in flashcard memory in pretraining then looks for the same patterns in your review history when it builds your cached model state

> **@PantsuThief:** Its not just a marginally better scheduling curve, its doing crazy random emergent behavior.

> **@JSchoreels:** Small note tho : For my Fork, I took the choice to redo an "epoch" of training on 8k/2k split. But for srs-benchmark, it's a 5k/5k

> **@symstym:** That "benchmark" is trivially gameable, so success on it is not evidence that an algo will be more efficient for learning.

> **@OyDuman:** this just radically changed my review queue in Korean deck, which is both great and terrible haha

> **@PantsuThief:** Btw thank you for your work on FSRS Jarrett, I adopted it as soon as I could and it was a massive leap forward over SM2. I didn't write this to put down fsrs

## Implications
- **Small sequence models can replace hand-tuned curves:** a compact RNN-style model with a per-user cached state (a few KB per item) is a practical pattern for on-device personalisation, such as adaptive difficulty or tutorial pacing in a mobile game.
- **Model size tiers are a compression lever:** offering Big/Small/Tiny variants with stated memory, disk and accuracy trade-offs is a clean way to ship ML on constrained devices.
- **Benchmarks can mislead:** one reply argues offline prediction scores don't prove better learning outcomes; any adaptive system should be judged on real user outcomes, not log loss alone.
- **Experiment:** log per-level attempts in a small game, train a tiny RNN or RWKV-style model to predict the chance a player clears the next level, keep a fixed difficulty curve as the fallback, and A/B the two on completion and retention.

## Tags
`rwkv` `rnn` `small-models` `on-device` `personalization` `compression` `ml` `learning`
