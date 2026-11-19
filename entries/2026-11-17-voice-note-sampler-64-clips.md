# Playing any song with 64 clips of one person's voice, built with an AI coding model

**X post:** https://x.com/aj_dev_smith/status/2122538394710687871  
**Author:** A.J. (@aj_dev_smith) · posted 2026-11-17 (UTC) · 5,298 likes, 198 replies  
**Source:** the post, the author's replies and his earlier related post; the demo video was not transcribed here

## What it is
A.J., who describes himself in his X bio as a musician, developer and architect, built (with Claude Fable 5.2, he says) a voice-based instrument: he recorded himself singing and whistling every note in his range, 64 clips each holding a single note, and the tool plays songs using only those clips. No backing track is playing in the demo. In replies he explains that the higher notes are falsetto and the rest chest voice, with whistles layered in, and that a version which copied and transposed notes beyond his range sounded only slightly better, so he posted the raw, unedited takes. He says there is no goal beyond personal curiosity.

It follows his earlier experiment in which 259 simulated "throat" voices each sang one assigned note to reproduce a song, with no instruments or lyrics, and your brain fills in the rest.

## Thread highlights
> **@aj_dev_smith:** yeah I had a version where it copied and transposed the notes out of my range. it sounded better but not significantly more.

> **@aj_dev_smith:** I did the math and you'd need like ~250 for it to be possible with realistic timing.

> **@koorinohonou:** Do one in your chest voice, one in falsetto, then play your voice on two manuals like an organ

> **@discobiscuit900:** Congrats! You have made the equivalent of a 1998 MP3 file.

> **@sphenreckson:** And it doesn't sound good at all. What's the benefit of this?

## Implications
- **Personal sample instruments are now a weekend project:** a coding model can write the note mapping, MIDI playback and sample triggering from a short brief.
- **Game audio use:** a voice or object recorded at a few pitches can become a playable instrument for UI sounds, ambient pads or character "voices" in the style of Animal Crossing babble, with very small audio budgets.
- **Small footprint:** 64 short clips compress well (Ogg or ADPCM in Unity), and pitch-shifting a few root notes can cut that further at some quality cost, the same trade-off the author describes.
- **Experiment:** record one sound source (voice, a glass, a string) at 12 to 24 pitches, have an agent build a Unity script that maps MIDI notes to the nearest clip with pitch correction, and compare the sound and build size against a single pitch-shifted clip.

## Tags
`audio` `music` `game-dev` `unity` `prototyping` `claude` `compression` `sfx`
