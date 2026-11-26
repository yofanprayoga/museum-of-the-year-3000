#!/usr/bin/env python3
"""Museum of the Year 3000: one museum label for an ordinary object from today."""

import os

ENTRY = (
    "Charging cable, 2024. Each night, humans fed their pocket oracles "
    "through this tail, for a dead phone was considered a small bereavement."
)

MAX_CHARS = 200


def main():
    if not (1 <= len(ENTRY) <= MAX_CHARS) or not ENTRY.strip():
        raise SystemExit(
            f"entry must be 1-{MAX_CHARS} non-blank chars, got {len(ENTRY)}"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
