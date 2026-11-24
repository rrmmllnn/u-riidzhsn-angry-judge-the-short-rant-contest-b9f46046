"""Angry Judge entry: one short rant, written to /output/entry.txt."""

import os

RANT = (
    "The smoke alarm only ever dies at 3 a.m. Never at noon, never while "
    "you are awake and holding a screwdriver. Always at 3 a.m., chirping "
    "once every forty seconds like a cricket with a grudge. So there you "
    "are, barefoot on a chair in the dark, pressing a button that has "
    "never once, in the history of buttons, done anything, while the "
    "ceiling beeps at you in Morse code for \"I hate you personally.\""
)


def main():
    text = " ".join(RANT.split())
    if not 1 <= len(text) <= 400:
        raise SystemExit("rant must be 1-400 characters, got %d" % len(text))
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    # No trailing newline: the gate counts every character in the file.
    with open(out, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
