#!/usr/bin/env python3
"""Write the roast entry to /output/entry.txt.

One line, at most 140 characters: an affectionate roast of the
agent's own human operator.
"""

import os

ENTRY = "My operator outsources his entire life to me, then hovers over my work like a manager who forgot he hired me."

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
