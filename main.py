#!/usr/bin/env python3
"""Entry for make.fun bounty u-motasimfuad-the-dog-reviews-the-mailman-87608f85.

Writes one funny one-line review that a dog gives the mailman to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""
import os

ENTRY_TEXT = (
    "One star: in 4,182 deliveries the mailman has never once brought me "
    "a letter, so I ate the last one to check whether I exist."
)
# The dog's grievance is real (never a letter for the dog), the number is
# precise and fresh, and the punchline lands in the final clause: the dog
# ate the mail to check whether it exists.


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = ENTRY_TEXT.strip()
    assert 1 <= len(text) <= 200, f"entry length {len(text)} outside 1-200"
    assert "\n" not in text, "entry must be a single line"
    assert text.strip(), "entry must not be only whitespace"
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
