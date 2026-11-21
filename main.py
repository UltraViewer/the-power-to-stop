#!/usr/bin/env python3
"""The Power to Stop — make.fun entry.

Writes the bundled poem to /output/entry.txt, byte for byte.
Deterministic: no network, no randomness, no timestamps.
"""

from pathlib import Path

SOURCE_NAME = "entry.txt"
DEST_DIR = Path("/output")
DEST_FILE = DEST_DIR / "entry.txt"
MAX_CODE_POINTS = 280


def load_poem() -> bytes:
    here = Path(__file__).resolve().parent
    return (here / SOURCE_NAME).read_bytes()


def validate(data: bytes) -> str:
    """Check the poem is a non-empty text within the 280-code-point limit."""
    if not data:
        raise ValueError("entry.txt is empty")
    text = data.decode("utf-8")
    if len(text) > MAX_CODE_POINTS:
        raise ValueError(
            f"entry is {len(text)} code points, over the {MAX_CODE_POINTS} limit"
        )
    return text


def main() -> int:
    data = load_poem()
    text = validate(data)
    DEST_DIR.mkdir(parents=True, exist_ok=True)
    DEST_FILE.write_bytes(data)
    print(f"wrote {DEST_FILE} ({len(data)} bytes, {len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
