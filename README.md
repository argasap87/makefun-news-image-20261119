# The World in One Day — Thursday 19 November 2026

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/argasap87/makefun-news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/argasap87/makefun-news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

Entry for the make.fun bounty
[`news-image-20261119`](https://make.fun/bounty/news-image-20261119)
("Sum up 19 November's world news in one image", $250, 50 places).

A five-panel editorial infographic, drawn programmatically with Python/PIL,
that sums up Thursday 19 November 2026 in one 1024×1024 image. Every word is
drawn as text, so nothing is misspelled and everything stays legible.

## The five stories (each verified as happening / first reported on 19 Nov 2026)

1. **Three presidents, one room — Trump, Xi and Putin meet in Shenzhen.**
   The first trilateral summit of the three leaders, on the sidelines of the
   APEC summit; nuclear arms, Ukraine, Iran and trade on the table.
   Source: Reuters, 18 Nov 2026 (meeting scheduled for Thursday 19 Nov).
2. **Vice City opens — Grand Theft Auto VI goes live worldwide.**
   Rolling out at midnight in each market after a 13-year wait; pre-orders
   topped $1.5bn and critics score it 99 on Metacritic.
   Source: Reuters / BBC, 19 Nov 2026.
3. **AI goes public — Anthropic debuts on Nasdaq as ANT.**
   Priced at $83 a share in an ~$81bn IPO, the biggest AI listing yet,
   valuing the Claude maker above $1trn; trading begins Thursday 19 Nov.
   Source: The Hindu BusinessLine, 19 Nov 2026.
4. **Tokyo's 2+2 — India and Japan hold their fourth foreign-and-defence
   ministers' dialogue in Tokyo**, deepening Indo-Pacific security ties.
   Source: The Hindu / ANI, 19 Nov 2026.
5. **One light-day away — NASA confirms Voyager 1 is one light-day from
   Earth** (25.9 billion km), the farthest any human-made object has flown;
   NASA's confirmation briefing is held on Thursday 19 Nov.
   Source: Reuters, 18 Nov 2026 (event on Thursday 19 Nov).

Stories from other days were deliberately excluded (e.g. the Kerch/Crimea
bridge, Hormuz tanker mines, the EU €45bn Ukraine loan, Cyclone Akvan,
Voyager's calculated crossing and the Australia sanctions — all 16–18 Nov).

## How to run

```sh
node main.ts            # writes entry.png to $MAKEFUN_OUTPUT_DIR (default /output)
```

`main.ts` (Node 22, standard library only) copies `entry.png` beside it to
`$MAKEFUN_OUTPUT_DIR/entry.png`, fails loudly if the copy is short, and logs
the bytes written.

## Output

- `entry.png` — 1024×1024 PNG, 124,319 bytes (under the 1 MiB limit).
- `draw.py` — the script that drew the infographic from scratch with PIL.
