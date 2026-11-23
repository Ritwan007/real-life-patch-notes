#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog.

Writes one line - a software patch note for a bug in real life / human
biology - to /output/entry.txt. Deterministic: no randomness, no network.
"""

import os

ENTRY = "v2.7.0: fixed a bug where the brain replayed your most embarrassing moment from 2014 at full volume at 3am."


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 160, "entry must be 1-160 characters"
    assert text and not text.isspace(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
