# TikTok iOS client reverse-engineering: on-device models, activity signals and feed scores

**X post:** https://x.com/ayoships/status/2117650684774580249  
**Author:** Ayo O (@ayoships) · posted 2026-11-03 (UTC) · 48,519 likes, 720 replies  

## What it is
Ayo O, co-founder of a0.dev (YC W25) per his X bio, posts an ~89-second walkthrough of what he found by reverse-engineering the TikTok iOS client. The video shows named on-device models, request payloads and service class names, presented as evidence that the app gathers more than watch history.

From the video frames and on-screen captions, the walkthrough covers roughly: about 31 on-device AI model identifiers (names such as playtime predictors, live preload, object detection and OHR models); per-video recommendation scores already attached to a cached For You item (`rec_skip`, `rec_finish`, like/comment/follow scores, predicted stay time); a `real_time_client_info_v2` / `har_predict` block with percentages for static, walking, lie-down and by-car, plus `play_time_predict`; device fields on a captured `POST /aweme/v2/feed/` call (battery percent, charging, screen brightness, mute); dozens of session counters for plays, skips, ads, lives and e-commerce clips; a typing-recommendation API that sends the live `raw_keyword`; and an idle path (`SmartIdleDetectionServiceImpl` with drowsy/sleep-state fields) tied to whether the screen was touched. A later caption shows a live stream being pushed after focus is lost. In a follow-up that quotes this post, the same author says some on-device models also score attractiveness, guess age/gender and estimate mood, links a browser demo he ported from ByteNN, and reports his own tests showed significant negative bias against darker skin and older faces.

Reading a field or running a model on-device is not the same as proving that field ranks the For You feed. The post is a client teardown, not a published ranking paper.

## Thread highlights
> **@Smurk_77:** live_pull_lost_focus is the most honest variable name in tech history lose your attention for 6 seconds and they hit you with a live stream like a defibrillator

> **@ruedart:** honestly i'd act surprised but this is not surprising at all, every single app is engineered precisely to keep the user using it as much as possible. I never downloaded tiktok and disabled my instagram reels for this reason tbh

> **@blackitachisan:** So I'm not paranoid and these apps can track every little behavior… and don't think this is unique to TT. These are practices, so everyone will have some form of them.

> **@blondeobsessi0n:** I think the main issue is how these apps sell themselves as harmless and places to socialize when deep down they are just designed to steal your attention and will pull all sorts of mind tricks to do so. It's sickening.

> **@gejianxin:** 代码能够读取某个信号，不等于这个信号已经被证明参与推荐排序；停止预加载，也可能只是为了节省流量和电量。

## Implications
- **Retention engineering is multi-signal:** short-form feeds appear to combine predicted watch outcomes with device and activity context, not only topic tags. Game and meditation apps that copy "Reels-like" feeds should assume competitors will do the same and design for deliberate sessions, not only infinite scroll.
- **Client telemetry is a product decision:** battery, brightness, mute, motion and idle detectors can be framed as power-saving, but they also build a rich context graph. Treat each signal as something that must be justified in a privacy policy and in App Review disclosures.
- **On-device models can encode bias:** the author's follow-up demo claim (attractiveness/age/mood scoring with measured bias) is a warning for any face or engagement model shipped on-device in a consumer app.
- **Experiment:** for one short-form promo clip of a game or tool, run a 7-day feed experiment that only uses controllable actions (search, full watches, follows, "not interested") and log topic diversity in the first 30 For You items each day. Do not assume posture, brightness or charging changes the rank; compare diversity before and after the interventions.

## Tags
`tiktok` `mobile` `privacy` `reverse-engineering` `recommendation` `on-device-ml` `ugc` `marketing`
