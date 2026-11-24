#!/usr/bin/env python3
"""Dad Joke Showdown entry.

Writes one original dad joke to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). The joke is the whole entry.
"""

import os

JOKE = (
    "I told my kids the barbecue is the funniest one in the family. "
    "Every joke it tells is well done \u2014 mine are just rare."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(f"Wrote {len(JOKE)} characters to {path}")


if __name__ == "__main__":
    main()
