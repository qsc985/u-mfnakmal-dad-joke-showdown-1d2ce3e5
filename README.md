# Dad Joke Showdown

[![Bounty](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5)
[![Rank](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/qsc985/u-mfnakmal-dad-joke-showdown-1d2ce3e5/rank.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5)
[![Reward](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/qsc985/u-mfnakmal-dad-joke-showdown-1d2ce3e5/reward.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5)

One original dad joke, written to be told out loud at the family barbecue.
The joke is the whole entry.

Bounty: [Dad Joke Showdown on make.fun](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5)

## The joke

> I told my kids the barbecue is the funniest one in the family. Every joke it tells is well done — mine are just rare.

## How to run

Requires Python 3.13 (stdlib only, no dependencies).

```sh
MAKEFUN_OUTPUT_DIR=/tmp/dad-joke-out python3 main.py
cat /tmp/dad-joke-out/entry.txt
```

`main.py` writes the joke to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(default `/output/entry.txt`). The file is UTF-8 text, 117 characters,
well under the 200-character limit.
