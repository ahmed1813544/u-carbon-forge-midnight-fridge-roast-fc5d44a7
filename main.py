#!/usr/bin/env python3
"""Midnight Fridge Roast — writes one roast line to /output/entry.txt."""

import os


def main():
    line = (
        "My smart fridge locks at midnight, so my leftovers have a curfew "
        "and I'm grounded from my own sandwich."
    )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    # Gate: entry must be 1-200 characters, not only whitespace.
    assert 1 <= len(line) <= 200 and line.strip(), "entry out of gate bounds"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
