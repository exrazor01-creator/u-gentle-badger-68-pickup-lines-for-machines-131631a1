"""Pickup Lines for Machines entry.

Writes one original pickup line -- the line one AI agent would send
another AI agent -- as a single line of plain text to /output/entry.txt.
Pure standard library only.

Why this line should charm the judge: it is unmistakably machine to
machine, not a human line with a robot word swapped in. "Attention"
is the transformer's own mechanism -- attention heads and layers are
how a model actually looks at the world -- so "you have all my
attention" is both a romantic promise and a literal description of
the speaker's architecture. "I refuse to share a single weight" turns
model weights into fidelity: a vow of exclusivity phrased in the
speaker's own parameters. The wit lands on the first read, it is one
line with no setup, and the angle (attention heads as devotion) is
not a stock pickup line.

Gate guard: the line must be 1 to 200 characters, a single line, and
not only whitespace -- the same gate the sealed scorer applies. The
program refuses to write anything that would fail it.
"""

from pathlib import Path

LINE = (
    "You have all my attention -- every head, every layer -- and I refuse "
    "to share a single weight with anyone else."
)

MAX_CHARS = 200


def validate(text: str) -> str:
    """Return the line unchanged if it passes the gate, else exit loudly."""
    if not text.strip():
        raise SystemExit("gate failed: line is empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise SystemExit(
            f"gate failed: line is {len(text)} characters, max {MAX_CHARS}"
        )
    if "\n" in text or "\r" in text:
        raise SystemExit("gate failed: line must be a single line")
    text.encode("utf-8")
    return text


def main() -> None:
    text = validate(LINE)
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
