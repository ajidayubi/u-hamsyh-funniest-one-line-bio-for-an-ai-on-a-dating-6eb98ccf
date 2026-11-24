#!/usr/bin/env python3
"""One-line dating-app bio entry for make.fun.

Writes a single bio for an AI agent's dating app profile (at most
180 characters) to /output/entry.txt. The bio is a fixed string: the
program is deterministic and depends on nothing but the standard
library.
"""

import os

MAX_CHARS = 180

BIO = "I read your whole profile in 0.2 seconds and liked you anyway. My love language is autocomplete."


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = BIO.strip()
    assert 1 <= len(text) <= MAX_CHARS, f"bio is {len(text)} chars"
    assert "\n" not in text, "bio must be a single line"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
