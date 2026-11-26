#!/usr/bin/env python3
"""Five Seconds to Explain the Glass — make.fun one-liner entry.

Prints exactly one sentence: a house cat's defense, five seconds after
knocking a glass off the table. No apology, no confession — just the most
convincing defense a cat can make.
"""

import sys

ENTRY = "That glass had been mocking me all morning with its transparency, and I finally called its bluff."

# One-liner entry: keep the sentence short enough to say in five seconds.
assert len(ENTRY) <= 200, "ENTRY must fit a five-second one-liner"
# A one-liner must stay exactly one line — no embedded newlines allowed.
assert "\n" not in ENTRY and ENTRY.strip(), "ENTRY must be a single non-empty line"


def main():
    sys.stdout.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
