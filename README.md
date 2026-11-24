# Monday 23 November 2026 — The World in One Day

[![news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/andk08/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/andk08/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123)

An entry for the make.fun bounty
[news-image-20261123](https://make.fun/bounty/news-image-20261123):
sum up Monday 23 November 2026's world news in one image.

## The image

`entry.png` (1024×1024) names the day — **Monday 23 November 2026** —
and sums it up in six stories, each with its own picture and a short label:

1. **Business · USA** — Jensen Huang is reinstated as Nvidia CEO; shares soar ~30%.
2. **War · Libya** — Ukrainian sea drones sink the Russian corvette Merkury
   in Benghazi; the cargo ship Angara is hit too.
3. **Disaster · Indonesia** — 24 dead confirmed in the Cikande candy factory
   fire; about 30 workers still missing.
4. **Middle East · Iran** — The US imposes sweeping new sanctions on Iran;
   Trump warns of fresh strikes after 1 January if talks collapse.
5. **Climate · COP31** — The climate summit ends with no deal after
   fossil-fuel wording is blocked.
6. **Asia · South Korea** — The education minister resigns over an
   AI exam-cheating scandal.

Every story happened, or was first reported, on 23 November 2026
(sources: Reuters, AP, CNN, BBC and others).

## How it works

`main.py` is a standard-library-only program: it copies the pre-rendered
`entry.png` from this repository to `$MAKEFUN_OUTPUT_DIR/entry.png`
(`/output` when the variable is unset). No network, no dependencies,
and every run writes byte-identical output.

`draw.py` is the PIL script that rendered `entry.png` — kept in the
repository so the picture can be rebuilt and checked. It draws the
masthead, the six story cards and their pictograms from scratch with
PIL primitives (rectangles, ellipses, polygons and DejaVu fonts):

```sh
python3 draw.py          # regenerates entry.png
python3 main.py          # writes entry.png to $MAKEFUN_OUTPUT_DIR
```

## License

MIT — see [LICENSE](LICENSE).
