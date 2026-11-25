# SKILL_ISSUES.md: PufferLib's hand-written refactoring and style guide, written for humans and LLMs

**X post:** https://x.com/yacineMTB/status/2123466099429900778  
**Author:** kache (@yacineMTB) · posted 2026-11-19 (UTC) · 3,426 likes, 55 replies  
**Source:** the post, replies including from the file's author Joseph Suarez (@jsuarez), and the file itself at https://github.com/PufferAI/PufferLib/blob/5.0/SKILL_ISSUES.md

## What it is
kache, whose X bio lists RL, robots, embedded work and simulators and previous engineering roles at X and Stripe, calls Joseph Suarez's "skill issues" Markdown file worth a hundred million dollars and notes it was open-sourced for free. The file, in the PufferLib reinforcement-learning repo, is a short hand-written guide to how Suarez styles and refactors PufferLib, which he says is equally useful for human and AI programmers and for other projects. Its stated objective is to reduce source length without code golf while preserving behaviour, performance and determinism, and to drop biases against long files or functions. Its "refactoring algorithm": inline every function used only once; remove defensive checks and replace complex error handling with plain asserts; flatten deep nesting by merging and inverting conditionals; co-optimise shared functions with their callers; then apply the style guide. Style rules include not splitting code into more files, soft 80 and hard 100 column limits, not adding complexity or shims just for testability, and not counting test length against code quality. For C it says to avoid forward declarations, preallocate memory at init, keep runtime allocations rare and freed in the same scope, and avoid keyword bloat and conditional macros; for CUDA, to write plain C99-style code without the C++ standard library, templates or classes. Asked why, Suarez says he wrote down how he programs because LLMs are steeped in big-tech abstraction habits.

## Thread highlights
> **@jsuarez:** I just wrote down how I program stuff because all the LLMs are fried on big tech abstraction garbage

> **@BlueTearsPT:** The md file that captures skills, failure modes and judgment calls often carries more value than the demo itself.

> **@whichaiwon:** copy the relevant rules into your chat instructions instead of dumping in the whole file

> **@Swarm_caste:** bro it's 44 lines of code. what are you talking about $100s of millions, you don't understand money

## Implications
- **A style guide is an agent's taste:** coding agents default to layered abstractions, defensive checks and many small files; a short, opinionated file of house rules is a direct counterweight.
- **Fits performance-critical code:** the C and CUDA rules (preallocate, no hidden allocations, flat control flow) map well onto game loops, simulation code and Burst/Jobs-style Unity code where allocation and indirection cost frame time.
- **Short beats long:** the whole guide is a few dozen lines, so it can sit in an agent's instructions without crowding context.
- **Experiment:** add a trimmed version of these rules to an agent's repo instructions, ask it to refactor one hot-path script under the "inline single-use functions, asserts over defensive checks" algorithm, and compare line count, allocations per frame and test results before and after.

## Tags
`code-quality` `refactoring` `agents-md` `style-guide` `agent-workflow` `performance` `c` `cuda` `reinforcement-learning`
