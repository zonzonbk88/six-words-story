#!/usr/bin/env python3
"""Six Words, One Story — entry writer.

Writes the final six-word story to /output/entry.txt.
The story was chosen against the judge brief: a complete story in
exactly six words, with a turn (the sale, then the silence) and
something left unsaid (why she sold it, why she stays silent).
"""

import os

ENTRY = "Sold her piano. She stayed silent."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate mirror: exactly six words, 1-60 chars, non-whitespace.
    words = ENTRY.split()
    assert len(words) == 6, f"expected 6 words, got {len(words)}"
    assert 1 <= len(ENTRY) <= 60, f"expected 1-60 chars, got {len(ENTRY)}"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
