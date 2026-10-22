# Rejected under 2.5.19 for test switches left in a release build

**X post:** https://x.com/vovalukashov/status/2111747424569978994  
**Author:** Luka Shaw (@vovalukashov) · posted 2026-10-18 (UTC) · 800 likes, 57 replies  

## What it is
A firsthand account of Apple's hidden-features rule, now a separate guideline, 2.5.19, which the author says can lead to a whole developer account being removed. Apple rejected one of his apps because the release build still contained three testing switches (a screenshots mode, a slow-entitlement simulation and mock unlocked purchases). Users couldn't reach them from the App Store build, but Apple said they "appear to have been intentionally hidden". He now inspects the strings in every archive before uploading. In replies he says a first rejection like this usually just needs a fix and doesn't threaten the account, and that the real risk is repeated rejections. He suggests describing any feature and switch in the review notes, and has moved his screenshot tooling into simulator-only builds.

## Thread highlights
> **@vovalukashov:** Don’t worry, if you haven’t had any rejections before, you’ll likely just receive the same notification I did. You’ll simply need to make the necessary fixes, and that’s it.

> **@vovalukashov:** I'd describe the feature and the switch in the review notes, Apple's rules ask for every feature to be there

> **@sulka:** I’m not aware of a single game engine that makes it easy to compile out full feature sets including all art and UI of a feature

> **@Somany0314:** I turned what we learned into an open-source agent skill, with a bundle scanner and checks for native code, localized strings, and build isolation.

## Implications
- **Unity/mobile:** debug menus, cheat toggles and mock-purchase flags are common in Unity builds; strip them with scripting define symbols or editor-only assemblies, not runtime flags.
- **Release process:** a strings scan of the final IPA for words like debug, cheat, mock or unlock is a cheap pre-upload gate.
- **Experiment:** add a build step that dumps strings from the release binary and fails the build if any known debug-flag names appear, then run it on your current release.

## Tags
`app-store` `ios` `compliance` `unity` `release`
