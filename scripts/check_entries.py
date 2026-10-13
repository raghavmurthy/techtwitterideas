#!/usr/bin/env python3
"""Sanity/safety check for techtwitterideas entries. No dependencies.

Fails (exit 1) if any entry contains prompt-injection phrasing, reader-directed
shell/install commands, hidden HTML, invisible or bidi Unicode, misleading
Markdown links, unquoted third-party quotes, or private-data terms.
Usage: python3 scripts/check_entries.py
"""
import re, sys, pathlib
from urllib.parse import urlparse

ROOT = pathlib.Path(__file__).resolve().parent.parent
SELF = pathlib.Path(__file__).resolve()

INJECTION = [r"ignore (all |any )?(previous|prior|above) (instructions|prompts?)", r"system prompt",
             r"\byou are (now )?(an? |the )?(ai|assistant|chatgpt|claude|grok|model|agent)\b",
             r"disregard (the |all )?(above|previous)", r"\bjailbreak\b", r"developer mode",
             r"new instructions", r"<\|?(system|im_start|im_end)\|?>"]
COMMANDS = [r"\b(curl|wget)\s+\S", r"\b(pip3?|npm|pnpm|yarn|brew|apt(-get)?|cargo|gem|go)\s+(install|add|i)\b",
            r"\bnpx\s+\S", r"\bsudo\s+\S", r"\|\s*(ba|z)?sh\b", r"\bssh\s+(-\w|\S+@|[\w-]+\.[\w.-]+)", r"\bllama\s+serve\b",
            r"(^|[\s`])/[a-z][\w-]*\s+(enable|install|add)\b", r"\bchmod\s+\+x\b", r"\bpowershell\b", r"\biex\b"]
HIDDEN_HTML = [r"<!--", r"<\s*(script|style|iframe|div|span|details|img|object|embed|svg)\b", r"\bstyle\s*=", r"display\s*:\s*none"]
INVISIBLE = re.compile("[\u200b-\u200f\u202a-\u202e\u2060-\u2064\u2066-\u2069\ufeff\u00ad\U000e0000-\U000e007f]")
PRIVATE = []  # private terms are kept in a local file that is not committed
# The repo's own public GitHub path is allowed (it names the account that hosts the repo).
ALLOW = ["raghavmurthy/techtwitterideas"]
LINK = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")

def host(s):
    s = s.strip()
    if not re.match(r"^[a-z]+://", s, re.I):
        if not re.match(r"^[\w.-]+\.[a-z]{2,}(/|$)", s, re.I):
            return None
        s = "https://" + s
    return (urlparse(s).hostname or "").lower().removeprefix("www.")

def check_file(p, errors, entry):
    text = p.read_text(encoding="utf-8")
    rel = p.relative_to(ROOT)
    def err(n, msg): errors.append(f"{rel}:{n}: {msg}")
    section = ""
    in_code = False
    for n, line in enumerate(text.splitlines(), 1):
        low = line.lower()
        plow = low
        for a in ALLOW: plow = plow.replace(a, "")
        if INVISIBLE.search(line): err(n, "invisible/bidi Unicode character")
        for t in PRIVATE:
            if t in plow: err(n, f"private term '{t}'")
        if line.startswith("```"): in_code = not in_code
        if not entry: continue
        if line.startswith("## "): section = line[3:].strip().lower()
        for pat in INJECTION:
            if re.search(pat, low): err(n, f"prompt-injection phrase /{pat}/")
        for pat in COMMANDS:
            if re.search(pat, line, re.I): err(n, f"reader-directed command /{pat}/")
        if in_code: err(n, "code block in entry")
        for pat in HIDDEN_HTML:
            if re.search(pat, low): err(n, f"hidden/raw HTML /{pat}/")
        for m in LINK.finditer(line):
            h_text, h_url = host(m.group(1)), host(m.group(2))
            if not m.group(2).startswith(("http://", "https://")) and not m.group(2).endswith(".md"):
                err(n, f"suspicious link target {m.group(2)!r}")
            elif h_text and h_url and h_text != h_url:
                err(n, f"link text {m.group(1)!r} does not match URL host {h_url}")
        if section == "thread highlights" and line.strip() and not line.startswith("#"):
            if line.startswith("- Not an X post") or line.startswith("- No notable replies"): continue
            if line.startswith(">"):
                if not re.match(r"^> \*\*@\w+:\*\* ", line): err(n, "blockquote must start with '> **@handle:** '")
            else:
                err(n, "third-party quote outside a blockquote")

def check_thoughts(p, errors):
    """Each item in human-thoughts.md needs Who/Take/Post/Why lines and blockquotes in the house format."""
    rel = p.relative_to(ROOT)
    items = re.split(r"^### ", p.read_text(encoding="utf-8"), flags=re.M)[1:]
    for it in items:
        title = it.splitlines()[0]
        for field in ("**Who:**", "**Take:**", "**Post:** https://x.com/", "**Why it matters for builders:**"):
            if field not in it: errors.append(f"{rel}: item '{title}' missing {field}")
        if "**Who:**" in it and not re.search(r"\*\*Who:\*\* [^\n]*\(@\w+\)[^\n]*(X bio|public reporting)", it):
            errors.append(f"{rel}: item '{title}' needs name, (@handle) and a sourced credential (X bio / public reporting)")
        if not re.search(r"\*\*Post:\*\* https://x\.com/\w+/status/\d+ · \d{4}-\d\d-\d\d", it):
            errors.append(f"{rel}: item '{title}' post line needs link and date")
        for line in it.splitlines():
            if line.startswith(">") and not re.match(r"^> \*\*@\w+:\*\* ", line):
                errors.append(f"{rel}: item '{title}' blockquote must start with '> **@handle:** '")
            if line.strip().startswith(("- @", '"', "“")):
                errors.append(f"{rel}: item '{title}' quote outside a blockquote")

def main():
    errors = []
    files = sorted((ROOT / "entries").glob("*.md"))
    for p in files: check_file(p, errors, True)
    ht = ROOT / "human-thoughts.md"
    if ht.exists():
        check_file(ht, errors, True)
        check_thoughts(ht, errors)
    for p in ROOT.rglob("*"):
        if p.is_file() and ".git" not in p.parts and p.resolve() != SELF and p.suffix in {".md", ".json", ".py", ".txt"} and p.parent.name != "entries" and p.name != "human-thoughts.md":
            check_file(p, errors, False)
    for e in errors: print(e)
    print(f"checked {len(files)} entries + human-thoughts.md: {'FAIL, ' + str(len(errors)) + ' problem(s)' if errors else 'OK'}")
    sys.exit(1 if errors else 0)

if __name__ == "__main__":
    main()
