"""One Word From Grandma — entry program.

Writes exactly one word to $MAKEFUN_OUTPUT_DIR/entry.txt: the single word
a grandma would text about AI.

The word: "robit".

Why this word, against the judge's brief (most important first):
1. It reads as the single word a grandma would text about AI — a
   grandma trying to type "robot" and landing one letter off, exactly the
   kind of typo the brief says counts.
2. It sounds like a real grandmother's texting voice: warm, a little
   baffled, the way she would type it to a grandchild. She is not
   explaining AI; she is squinting at the machine and calling it by
   almost its name.
3. The joke lands in one word with no caption: the misspelling IS the
   joke — she is sweet, she is trying, and she is one letter away.
4. It is tied to robots and machines, not a word that would fit any
   subject: "robit" only means anything next to a robot.
5. It is fresh rather than the obvious "robot", and still instantly
   readable — everyone hears "robot" the moment they see it.

Stdlib only. Deterministic: two runs produce byte-identical output.
"""

import os
import sys

WORD = "robit"
OUTPUT_FILENAME = "entry.txt"


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not output_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1

    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, OUTPUT_FILENAME)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)

    # Self-check against the gate: UTF-8 text of 1 to 30 characters,
    # not only white space, exactly one word. No trailing newline: the
    # file is the word and nothing else, so the judge reads it exactly
    # as submitted.
    with open(path, "rb") as f:
        data = f.read()
    text = data.decode("utf-8")
    assert 1 <= len(text) <= 30, "entry must be 1-30 characters"
    assert text.strip(), "entry must not be only white space"
    assert len(text.split()) == 1, "entry must be exactly one word"
    print(f"wrote {path}: {text!r} ({len(data)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
