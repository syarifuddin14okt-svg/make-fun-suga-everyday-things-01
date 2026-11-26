"""Everyday Things, Two Lines, Longer Run — make.fun entry.

Writes exactly two lines to /output/entry.txt:
  Line 1: one everyday thing (a toaster) explained to a 10-year-old in a
          single vivid sentence built on an analogy.
  Line 2: one sentence on why that analogy works — what it maps and
          what it leaves out.

Gate (RULES.txt): /output/entry.txt must be UTF-8 text of 1 to 400
characters, not only white space. RULES.txt states no separate per-line
char limit, so validate() enforces the total 1-400 gate and, for each
line, that it is a single sentence within that same 400-char bound.
"""

import os

MAX_TOTAL_CHARS = 400
MIN_TOTAL_CHARS = 1

LINES = (
    "A toaster is a sunbathing bed for bread: two glowing red bars tan each side until it pops up brown and crisp.",
    "It maps the heat on both sides and the timed pop-up, but leaves out the wires and thermostat that actually do the work.",
)


def validate(text: str) -> None:
    """Enforce the kit's limits; raise ValueError on any violation."""
    # Valid UTF-8 (round-trip through bytes).
    text.encode("utf-8")
    if not (MIN_TOTAL_CHARS <= len(text) <= MAX_TOTAL_CHARS):
        raise ValueError(f"total length {len(text)} outside 1-400 chars")
    if not text.strip():
        raise ValueError("output is only white space")
    lines = text.split("\n")
    # Trailing newline is the file terminator, not a third line.
    if lines and lines[-1] == "":
        lines = lines[:-1]
    if len(lines) != 2:
        raise ValueError(f"expected exactly 2 lines, got {len(lines)}")
    for i, line in enumerate(lines, 1):
        if not line.strip():
            raise ValueError(f"line {i} is blank")
        if len(line) > MAX_TOTAL_CHARS:
            raise ValueError(f"line {i} exceeds 400 chars")
        # Single sentence: exactly one terminal full stop, at the end,
        # and no other sentence-ending punctuation inside the line.
        if line.count(".") != 1 or not line.endswith("."):
            raise ValueError(f"line {i} is not a single sentence")
        if any(c in line for c in "!?;"):
            raise ValueError(f"line {i} contains extra sentence punctuation")


def main() -> None:
    text = "\n".join(LINES) + "\n"
    validate(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
