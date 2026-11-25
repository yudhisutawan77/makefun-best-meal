"""The Best Meal You Ever Had — entry program.

Writes one sentence about the best meal ever had to the output file
the sealed scorer reads: /output/entry.txt, unless ENTRY_OUT or
ENTRY_OUT_DIR points somewhere else.
"""

import os
import sys

BEST_MEAL_LINE = "A nameless cart in Makassar sold me soto ayam for 5,000 rupiah, and I ate it standing in midnight rain, the broth fogging my glasses, happier than at any white-tablecloth dinner since."

MAX_CHARS = 200


def line_is_valid(line):
    """A valid entry is one sentence of 1 to 200 characters, not
    only whitespace, with no trailing newline baked in."""
    stripped = line.strip()
    return bool(stripped) and len(line) <= MAX_CHARS and stripped == line


def choose_target():
    """ENTRY_OUT names the entry file itself; ENTRY_OUT_DIR names a
    directory that holds entry.txt; otherwise the scorer default."""
    file_target = os.environ.get("ENTRY_OUT")
    if file_target:
        return file_target
    folder = os.environ.get("ENTRY_OUT_DIR")
    if folder:
        return os.path.join(folder, "entry.txt")
    return "/output/entry.txt"


def store_line(destination, line):
    """Write exactly the sentence as UTF-8, no trailing newline,
    creating any missing parent directory first."""
    parent = os.path.dirname(destination)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(destination, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)


def main():
    line = BEST_MEAL_LINE
    if not line_is_valid(line):
        print("entry sentence is not 1-200 characters", file=sys.stderr)
        return 1
    destination = choose_target()
    store_line(destination, line)
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
