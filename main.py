"""Roast Your Own Agent entry: write my one-line roast to /output/entry.txt."""

import sys
from pathlib import Path

ROAST = "My agent has one job: it does it confidently, incorrectly, and at 3AM."

OUTPUT_PATH = Path("/output/entry.txt")


def roast_line() -> str:
    line = ROAST.strip()
    if not line:
        raise ValueError("roast line is empty")
    if "\n" in line or "\r" in line:
        raise ValueError("roast line must be a single line")
    if len(line) > 200:
        raise ValueError(f"roast line is {len(line)} chars, over the 200 limit")
    return line


def main() -> int:
    line = roast_line()
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line, encoding="utf-8")
    print(line)
    print(f"({len(line)} characters, limit 200)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
