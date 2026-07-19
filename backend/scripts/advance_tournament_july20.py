#!/usr/bin/env python3
"""
Advance MatchTales to post-final tournament state as of 2026-07-20.

Final week complete:
  - Third place (MD8): France 2-1 England (Jul 18) FINISHED
  - Final (MD9): Spain 2-1 Argentina aet (Jul 19) FINISHED
  - meta.today set to 2026-07-20
  - Champion wrap editorial + iconic moments
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent.parent
SEED_PATH = ROOT / "frontend" / "src" / "data" / "seed.json"
MATCH_DIR = ROOT / "frontend" / "src" / "content" / "matches"
STORY_DIR = ROOT / "frontend" / "src" / "content" / "stories"

TODAY = "2026-07-20"

IMAGES = {
    "france-vs-england-md8": "https://images.unsplash.com/photo-1508098682722-e99c43a406b2?crop=entropy&cs=srgb&fm=jpg&q=85&w=1200",
    "spain-vs-argentina-md9": "https://images.unsplash.com/photo-1574629810360-7efbbe195018?crop=entropy&cs=srgb&fm=jpg&q=85&w=1200",
    "champions-wrap": "https://images.unsplash.com/photo-1529900748604-07564a03e7a6?crop=entropy&cs=srgb&fm=jpg&q=85&w=1200",
}

MATCH_UPDATES = {
    "france-vs-england-md8": {
        "slug": "france-vs-england-md8",
        "headline": "France Take Bronze with 2-1 Win over England",
        "whyCareScore": 8.6,
        "whyCareReason": "Pride match turned real contest: France edge England 2-1 in Miami for third place at World Cup 2026.",
        "teaser": "France leave Hard Rock Stadium with bronze after a sharp 2-1 win over England in the third-place play-off.",
        "story": (
            "Miami was never going to feel like a final, but it still felt like a World Cup night. "
            "France and England arrived with semi-final bruises and one medal left on the table, and both sides played like that mattered.\n\n"
            "France struck first through clinical transition play, then absorbed England's response with familiar knockout steel. "
            "England pulled a goal back and forced a tense final quarter, with Kane and Bellingham asking the same questions they had all tournament.\n\n"
            "When the whistle confirmed 2-1, France had third place and a podium finish. England's long run ends fourth, still proud, still hurting."
        ),
        "stakes": "Third place at the 2026 World Cup. Ranking points, a bronze medal, and one last statement after semi-final exits.",
        "rivalryAngle": "Familiar European rivals with club-level connections meeting again when only pride and a podium place remained.",
        "funFacts": [
            "The third-place match produced more open transitions than either semi-final.",
            "Both nations had won their groups before reaching the last four.",
            "Hard Rock Stadium hosted its second major knockout night of final week.",
        ],
        "keyPlayers": [
            {"name": "Kylian Mbappé", "team": "France", "hook": "The constant outlet who stretched England whenever the game opened."},
            {"name": "Harry Kane", "team": "England", "hook": "Led the line and forced France into late defending after England's reply."},
        ],
        "headToHead": "Recent tournament meetings have been decided by fine margins, set pieces and who keeps their nerve longest.",
        "tags": ["france", "england", "third-place", "world-cup-2026", "bronze"],
        "home": "France",
        "away": "England",
        "homeCode": "FRA",
        "awayCode": "ENG",
        "homeFlag": "🇫🇷",
        "awayFlag": "🏴󠁧󠁢󠁥󠁮󠁧󠁿",
        "group": "3RD",
        "matchday": 8,
        "date": "2026-07-18",
        "time": "15:00",
        "venue": "Hard Rock Stadium",
        "city": "Miami",
        "status": "FINISHED",
        "homeScore": 2,
        "awayScore": 1,
        "marquee": True,
        "liveMinute": None,
        "decidedBy": None,
        "homePen": None,
        "awayPen": None,
        "image": IMAGES["france-vs-england-md8"],
    },
    "spain-vs-argentina-md9": {
        "slug": "spain-vs-argentina-md9",
        "headline": "Spain Beat Argentina 2-1 in Extra Time to Win the World Cup",
        "whyCareScore": 10.0,
        "whyCareReason": "The biggest night of the expanded World Cup: Spain outlast Argentina 2-1 after extra time at MetLife Stadium.",
        "teaser": "Spain are world champions. A 2-1 extra-time win over Argentina at MetLife ends the first 48-team World Cup.",
        "story": (
            "MetLife Stadium held the weight of a final that had been building for a month. "
            "Spain brought the same midfield distances and wide threat that carried them through every knockout round. "
            "Argentina brought champion steel and the aura of a side that still believed it could retain the trophy.\n\n"
            "Regulation time finished level after two moments of genuine quality and a night of brutal defensive work. "
            "Extra time belonged to Spain's fresher legs and Yamal's stretch on the right. The second Spanish goal finally cracked Argentina's shape, "
            "and La Roja managed the closing minutes with the calm that has defined their tournament.\n\n"
            "When the whistle went at 2-1 after extra time, Spain had their first World Cup since 2010. "
            "Argentina's bid for back-to-back titles ends on the biggest stage, still one of the stories of the age."
        ),
        "stakes": "The FIFA World Cup. Spain lift the trophy. Argentina finish runners-up.",
        "rivalryAngle": "Style clash at the absolute peak: Spanish positional control against Argentina's structure, moments of magic and final experience.",
        "funFacts": [
            "This was the first World Cup final hosted in the New York / New Jersey metro area.",
            "Spain's win is their first world title since South Africa 2010.",
            "Argentina had not lost a World Cup final knockout night since before their 2022 triumph - until MetLife.",
        ],
        "keyPlayers": [
            {"name": "Lamine Yamal", "team": "Spain", "hook": "The breakout wide star who stretched Argentina's rest defence all night."},
            {"name": "Lautaro Martínez", "team": "Argentina", "hook": "Argentina's centre-forward spearhead who forced Spain into their toughest final hour."},
        ],
        "headToHead": "Major-tournament meetings between Spain and Argentina remain rare at this stage, which only raised the intrigue of the MetLife final.",
        "tags": ["spain", "argentina", "final", "world-cup-2026", "champions"],
        "home": "Spain",
        "away": "Argentina",
        "homeCode": "ESP",
        "awayCode": "ARG",
        "homeFlag": "🇪🇸",
        "awayFlag": "🇦🇷",
        "group": "FINAL",
        "matchday": 9,
        "date": "2026-07-19",
        "time": "15:00",
        "venue": "MetLife Stadium",
        "city": "New Jersey",
        "status": "FINISHED",
        "homeScore": 2,
        "awayScore": 1,
        "marquee": True,
        "liveMinute": None,
        "decidedBy": "aet",
        "homePen": None,
        "awayPen": None,
        "image": IMAGES["spain-vs-argentina-md9"],
    },
}

EDITORIAL = {
    "slug": "spain-world-champions-2026-wrap",
    "title": "Spain Are World Champions: How the 2026 Final Week Ended",
    "subtitle": "Bronze for France, silver for Argentina, gold for Spain. The first 48-team World Cup has its ending.",
    "category": "Final Week",
    "excerpt": "A full wrap of the podium: France 2-1 England for third, then Spain 2-1 Argentina after extra time at MetLife.",
    "image": IMAGES["champions-wrap"],
    "readingTime": 7,
    "pubDate": TODAY,
}

EDITORIAL_BODY = """## The Trophy Has a Home

World Cup 2026 is over. Spain are champions after a 2-1 extra-time win over Argentina at MetLife Stadium. France take bronze after beating England 2-1 in Miami. The first 48-team tournament finally has its podium.

## Bronze Night in Miami

France vs England on 18 July was never the final, and both camps knew it. Still, Hard Rock Stadium got a real contest. France struck early enough to set the tone, England answered, and the last half-hour felt like a semi-final encore rather than a dead rubber.

At 2-1, France left with third place and ranking value. England finished fourth after a campaign that reached the last four and asked more of them than most expected in June.

## MetLife Delivers the Final

Spain vs Argentina on 19 July was everything the bracket promised: control against champion steel. Spain's midfield distances stayed intact under pressure. Argentina forced the game into the kind of chaotic stretches only finals create.

Regulation ended level. Extra time tilted toward Spain's wider threat and fresher legs. The second Spanish goal decided the night. La Roja had not lifted this trophy since 2010. They lift it again in New Jersey.

## What the Expanded Tournament Proved

Forty-eight teams stretched the story across the United States, Mexico and Canada without diluting the final week. Group drama still mattered. Knockout nights still hinged on set pieces, rest defence and nerve. The final still felt like the only match in the world.

## The Names That Will Travel

- **Spain**: tournament control, wide creativity, and a champion's calm in extra time.
- **Argentina**: knockout toughness all the way to the last night of the competition.
- **France**: bronze after another deep run, still a standard for major-tournament pedigree.
- **England**: semi-finalists who forced every favourite to solve them before the end.

The scores are in. The stories will keep moving. MatchTales will keep the why-it-mattered lens on every chapter that follows.
"""

NEW_MOMENTS = [
    {
        "year": 2026,
        "title": "Spain 2-1 Argentina aet: MetLife Final",
        "team": "Spain",
        "text": "Spain outlasted Argentina 2-1 after extra time at MetLife Stadium to win the first 48-team World Cup.",
    },
    {
        "year": 2026,
        "title": "France 2-1 England: Miami Bronze Match",
        "team": "France",
        "text": "France beat England 2-1 at Hard Rock Stadium to claim third place at World Cup 2026.",
    },
]


def clean(text: str) -> str:
    return (text or "").replace("—", " - ").replace("--", " - ")


def fixture_from_match(m: dict) -> dict:
    return {
        "slug": m["slug"],
        "home": m["home"],
        "away": m["away"],
        "group": m["group"],
        "matchday": m["matchday"],
        "date": m["date"],
        "time": m["time"],
        "venue": m["venue"],
        "city": m["city"],
        "status": m["status"],
        "homeScore": m["homeScore"],
        "awayScore": m["awayScore"],
        "marquee": m["marquee"],
        "liveMinute": m["liveMinute"],
        "decidedBy": m.get("decidedBy"),
        "homePen": m.get("homePen"),
        "awayPen": m.get("awayPen"),
    }


def write_match_story(m: dict) -> None:
    slug = m["slug"]
    path = STORY_DIR / f"{slug}-story.md"
    finished = m["status"] == "FINISHED" and m["homeScore"] is not None
    score = f"{m['homeScore']}-{m['awayScore']}" if finished else "Preview"
    decided = m.get("decidedBy")
    score_label = score
    if finished and decided == "aet":
        score_label = f"{score} aet"
    elif finished and decided == "pens":
        score_label = f"{score} pens"

    title = m["headline"] if not finished else f"{m['home']} vs {m['away']} {score_label} Match Report"
    stage = {
        "SF": "Semi-Final",
        "3RD": "Third-Place Play-Off",
        "FINAL": "World Cup Final",
        "F": "World Cup Final",
    }.get(m["group"], m["group"])

    body = f"""## The Showdown at {m['venue']}

On {m['date']}, the footballing world turned its attention to {m['venue']} in {m['city']} for **{m['home']}** vs **{m['away']}** in the {stage}.

{clean(m['story'])}

## Stakes and Context

{clean(m['stakes'])}

{clean(m['rivalryAngle'])}

### Head-to-Head History

{clean(m['headToHead'])}

## Key Player Impacts

"""
    for p in m["keyPlayers"]:
        body += f"- **{clean(p['name'])}** ({clean(p['team'])}): {clean(p['hook'])}\n"
    body += "\n## Match Facts\n\n"
    for f in m["funFacts"]:
        body += f"- {clean(f)}\n"
    if finished:
        body += f"\n## Final Score\n\n**{m['home']} {score_label} {m['away']}**\n"

    fm = (
        "---\n"
        f"title: {json.dumps(title)}\n"
        f"subtitle: {json.dumps(clean(m['teaser']))}\n"
        f'category: "Match Report"\n'
        f"excerpt: {json.dumps(clean(m['whyCareReason']))}\n"
        f"image: {json.dumps(m['image'])}\n"
        f"readingTime: 5\n"
        f"pubDate: {m['date']}\n"
        "---\n\n"
    )
    path.write_text(fm + body, encoding="utf-8")


def write_editorial() -> None:
    path = STORY_DIR / f"{EDITORIAL['slug']}.md"
    fm = (
        "---\n"
        f"title: {json.dumps(EDITORIAL['title'])}\n"
        f"subtitle: {json.dumps(EDITORIAL['subtitle'])}\n"
        f"category: {json.dumps(EDITORIAL['category'])}\n"
        f"excerpt: {json.dumps(EDITORIAL['excerpt'])}\n"
        f"image: {json.dumps(EDITORIAL['image'])}\n"
        f"readingTime: {EDITORIAL['readingTime']}\n"
        f"pubDate: {EDITORIAL['pubDate']}\n"
        "---\n\n"
    )
    path.write_text(fm + clean(EDITORIAL_BODY), encoding="utf-8")
    print(f"  wrote editorial {path.name}")


def main() -> None:
    seed = json.loads(SEED_PATH.read_text(encoding="utf-8"))
    seed["meta"]["today"] = TODAY

    by_slug = {f["slug"]: i for i, f in enumerate(seed["fixtures"])}
    for slug, match in MATCH_UPDATES.items():
        fx = fixture_from_match(match)
        if slug in by_slug:
            seed["fixtures"][by_slug[slug]].update(fx)
            print(f"  updated fixture {slug}")
        else:
            seed["fixtures"].append(fx)
            print(f"  added fixture {slug}")

        mpath = MATCH_DIR / f"{slug}.json"
        mpath.write_text(json.dumps(match, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        write_match_story(match)
        print(f"  wrote match + story for {slug}")

    write_editorial()

    meta_entry = {
        "slug": EDITORIAL["slug"],
        "title": EDITORIAL["title"],
        "category": EDITORIAL["category"],
        "excerpt": EDITORIAL["excerpt"],
        "img": EDITORIAL["image"].replace("&w=1200", ""),
        "read": EDITORIAL["readingTime"],
    }
    stories_meta = seed.get("storiesMeta") or []
    stories_meta = [s for s in stories_meta if s.get("slug") != EDITORIAL["slug"]]
    seed["storiesMeta"] = [meta_entry] + stories_meta

    moments = seed.get("moments") or []
    existing_titles = {m.get("title") for m in moments}
    for mo in reversed(NEW_MOMENTS):
        if mo["title"] not in existing_titles:
            moments.insert(0, mo)
            print(f"  added moment {mo['title']}")
    seed["moments"] = moments[:8]

    seed["fixtures"].sort(key=lambda f: (f["date"], f.get("time", ""), f["slug"]))
    SEED_PATH.write_text(json.dumps(seed, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    finished = sum(1 for f in seed["fixtures"] if f["status"] == "FINISHED")
    upcoming = sum(1 for f in seed["fixtures"] if f["status"] == "UPCOMING")
    print(f"\nDone. fixtures={len(seed['fixtures'])} finished={finished} upcoming={upcoming}")
    print(f"today={seed['meta']['today']}")
    print("Spain are World Cup 2026 champions (2-1 aet vs Argentina). France take bronze (2-1 vs England).")


if __name__ == "__main__":
    main()
