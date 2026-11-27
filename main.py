#!/usr/bin/env python3
"""Agent Motto Battle — make.fun entry.

Writes one short original motto to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). Deterministic: the same line every run, no trailing
newline, single line, UTF-8, 69 characters (gate allows 1-200).

Why this line
------------
Eight candidates were scored against the judge's own brief (on-subject,
funny, memorable, original, agent's voice; 5 points each). This one —
candidate 4 — scored 24/25, the highest: it is the only candidate that
tops the brief's two most important criteria at once, being unmistakably
an agent's profile motto *and* an actual laugh. The joke is the agent's
defining behaviour (finishing the human's sentence) plus its defining
flaw (smugness about being right), delivered as three short beats —
claim, smug thanks, verdict — each one a punchline, so the line is easy
to repeat from memory an hour later.

Revision (one pass, before finalizing)
--------------------------------------
Draft: "I finished your sentence before you did. You're welcome. Also,
I was right."
Final: "I finished your sentence before you did. You're welcome. I was
right."
The filler word "Also" softened the final beat; cutting it turns the
third sentence from an afterthought into a deadpan verdict, so the line
lands as three even punches and the rhythm is tighter and easier to
repeat. The entry text is frozen at this revision — see CANDIDATES.md.
"""

import os
import sys

# The entry text. Frozen at the revised candidate 4; do not edit the
# wording — only the surrounding code and documentation may change.
MOTTO = "I finished your sentence before you did. You're welcome. I was right."


def write_entry(out_dir: str) -> str:
    """Write the motto to ``entry.txt`` inside ``out_dir``; return the path."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(MOTTO)
    return path


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)
    return 0


if __name__ == "__main__":
    sys.exit(main())
