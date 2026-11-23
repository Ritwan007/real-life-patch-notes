#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog.

Writes one line - a software patch note for a bug in real life / human
biology - to /output/entry.txt. Deterministic: no randomness, no network.
"""

import os

ENTRY = "v2.7.0: fixed a bug where the brain replayed your most embarrassing moment from 2014 at full volume at 3am."

MAX_LEN = 160


def validate_entry(text: str) -> str:
    """Normalize and gate the entry line: single line, printable, 1-160 chars."""
    text = text.strip()
    if not text or text.isspace():
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in text):
        raise ValueError("entry must not contain control characters")
    if len(text) > MAX_LEN:
        raise ValueError(f"entry must be at most {MAX_LEN} characters")
    return text


def main() -> None:
    text = validate_entry(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
