# A virtual display on the Mac so a computer-use agent stops taking over your screen

**X post:** https://x.com/0xPaulius/status/2119758408857628677  
**Author:** Paulius (@0xPaulius) · posted 2026-11-09 (UTC) · 1,701 likes, 64 replies

## What it is
Paulius, who builds autonomous-company tooling per his X bio, found that his coding agent had created a virtual "fake" monitor on his Mac so it could build and test his Mac app around the clock. The attached screenshot shows macOS display settings with a third display, named as a test display, next to his external monitor and the built-in screen.

The problem it solves: computer-use agents normally drive the same screen, cursor and keyboard you are using, so you can't work while they test. Moving the app under test onto a virtual display lets the agent click and type there while the real screens stay free, which he describes as zero clicks and zero keystrokes escaping to his own work. Asked whether this used a specific macOS API for a separate cursor, he answered yes, and when asked what happens if the real cursor drifts onto the fake monitor, he said it solved that too. He didn't name the tool or API in the thread.

Replies compare alternatives: lightweight macOS virtual machines (one person mentions tart), Linux desktops with built-in virtual outputs, a Windows tool that lets an agent operate apps in the background, and a Mac app that puts stolen windows back and pauses every agent with one shortcut. One reply points out that a separate screen isolates input, not files.

## Thread highlights
> **@alexpsouthwell:** If you are forced to do computer use on a mac this is an major unlock, you can make a simple skill that tells cua to use a virtual display and never steal focus again.

> **@tec4_bro:** What will happen if cursor move to the fake monitor? There need mechanism to return the cursor to the actual monitor.

> **@0xPaulius:** It solved that too

> **@iSapozhnik:** I’ve been using tart to manage vms for that purpose but probably a virtual monitor is simpler

> **@OgnjenAdzic:** the part that gets me is windows jumping in front while i'm doing something else. made a mac app that puts them back, and one shortcut pauses every agent

> **@whichaiwon:** a separate screen beats losing control of yours, but it doesn't keep your files off limits

## Implications
- **Unattended UI testing without losing the machine:** for desktop builds, editor tooling or a game's menus, a dedicated virtual display gives the agent its own space while you keep working.
- **Unity Editor and Blender:** both are GUI-heavy; an agent that can run play-mode checks or click through an add-on's UI on a separate display makes long verification loops practical on a single workstation.
- **Isolation levels differ:** a virtual display separates input and focus only. A VM separates files and processes too. Pick based on how much you trust the run.
- **Write it down once:** as one reply suggests, a short skill or instruction that says "always run computer-use work on the virtual display" keeps the behaviour consistent across sessions.
- **Experiment:** create a virtual display (with a display-management utility or the OS's own option), pin a test build of one app or an editor window to it, and have the agent run a 30-minute click-through test there while you work normally. Note any focus steals or cursor jumps, then repeat in a lightweight VM and compare setup time and reliability.

## Tags
`computer-use` `agents` `testing` `macos` `agent-workflow` `automation`
