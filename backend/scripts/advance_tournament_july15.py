#!/usr/bin/env python3
"""
Advance MatchTales to tournament state as of 2026-07-15.

QF winners (already in data): France, Spain, England, Argentina.
Adds:
  - Semi-finals (MD7): France vs Spain (Jul 14), England vs Argentina (Jul 15)
  - Third-place (MD8): France vs England (Jul 18) UPCOMING
  - Final (MD9): Spain vs Argentina (Jul 19) UPCOMING
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent.parent
SEED_PATH = ROOT / "frontend" / "src" / "data" / "seed.json"
MATCH_DIR = ROOT / "frontend" / "src" / "content" / "matches"
STORY_DIR = ROOT / "frontend" / "src" / "content" / "stories"

IMAGES = {
    "france-vs-spain-md7": "https://images.unsplash.com/photo-1529900748604-07564a03e7a6?crop=entropy&cs=srgb&fm=jpg&q=85&w=1200",
    "england-vs-argentina-md7": "https://images.unsplash.com/photo-1431324155629-1a6deb1dec8d?crop=entropy&cs=srgb&fm=jpg&q=85&w=1200",
    "france-vs-england-md8": "https://images.unsplash.com/photo-1508098682722-e99c43a406b2?crop=entropy&cs=srgb&fm=jpg&q=85&w=1200",
    "spain-vs-argentina-md9": "https://images.unsplash.com/photo-1574629810360-7efbbe195018?crop=entropy&cs=srgb&fm=jpg&q=85&w=1200",
}

# Full match packages for late knockout
MATCHES = {
    "france-vs-spain-md7": {
        "slug": "france-vs-spain-md7",
        "headline": "Spain Blank France 2-0 to Reach the World Cup Final",
        "whyCareScore": 9.7,
        "whyCareReason": "European heavyweights collide in Dallas: a semi-final that decided the first finalist of 2026.",
        "teaser": "Spain produced a masterclass of control and finishing to beat France 2-0 and book a place in the MetLife final.",
        "story": (
            "Dallas delivered a semi-final worthy of the last four. France arrived with knockout steel and Mbappe's threat in behind; "
            "Spain arrived with the same patient control that has defined their entire tournament.\n\n"
            "La Roja never panicked. Pedri and the midfield dictated rest defence distances, Yamal stretched the right channel, "
            "and two moments of quality either side of half-time broke French resistance.\n\n"
            "France threw everything forward in the final minutes but could not force a way back. Spain are World Cup finalists. France drop into the third-place play-off."
        ),
        "stakes": "A place in the 2026 World Cup final. The loser plays for bronze four days later.",
        "rivalryAngle": "Modern European football's two schools: French athleticism and vertical threat against Spanish positional control.",
        "funFacts": [
            "Spain have not lost a knockout match in regulation time all tournament.",
            "France were chasing a third straight World Cup final appearance.",
            "AT&T Stadium hosted one of the highest-profile semi-finals of the expanded 48-team era.",
        ],
        "keyPlayers": [
            {"name": "Lamine Yamal", "team": "Spain", "hook": "The teenage wide threat who continually broke France's last line."},
            {"name": "Kylian Mbappé", "team": "France", "hook": "France's outlet on the break and their best hope of a second goal."},
        ],
        "headToHead": "Recent meetings have been tight, tactical affairs where midfield control has usually decided the night.",
        "tags": ["france", "spain", "semi-final", "world-cup-2026"],
        "home": "France",
        "away": "Spain",
        "homeCode": "FRA",
        "awayCode": "ESP",
        "homeFlag": "🇫🇷",
        "awayFlag": "🇪🇸",
        "group": "SF",
        "matchday": 7,
        "date": "2026-07-14",
        "time": "20:00",
        "venue": "AT&T Stadium",
        "city": "Dallas",
        "status": "FINISHED",
        "homeScore": 0,
        "awayScore": 2,
        "marquee": True,
        "liveMinute": None,
        "decidedBy": None,
        "homePen": None,
        "awayPen": None,
        "image": IMAGES["france-vs-spain-md7"],
    },
    "england-vs-argentina-md7": {
        "slug": "england-vs-argentina-md7",
        "headline": "Argentina Edge England 2-1 in a Semi-Final Classic",
        "whyCareScore": 9.8,
        "whyCareReason": "History, heat and a final place on the line: England vs Argentina in Miami on 15 July.",
        "teaser": "Argentina survived an England surge and sealed a 2-1 semi-final win to reach another World Cup final.",
        "story": (
            "Miami knew the script before kick-off: two football cultures with unfinished World Cup business, and ninety minutes to decide a finalist. "
            "England started with intensity, Bellingham driving transitions and Kane occupying Argentina's centre-backs.\n\n"
            "Argentina absorbed the storm, then struck twice in a ruthless ten-minute spell either side of half-time. "
            "England refused to fold. A late goal set up a frantic finale, with corners raining in and Hard Rock Stadium roaring for an equaliser.\n\n"
            "When the whistle went at 2-1, Argentina had earned the right to chase back-to-back titles. England's long run ends in the last four, "
            "with bronze still available in the third-place match."
        ),
        "stakes": "Winner to the final at MetLife Stadium. Loser faces France for third place.",
        "rivalryAngle": "One of football's most loaded fixtures: 1986 ghosts, 1998 red cards, 2002 penalties, and a 2026 semi-final chapter.",
        "funFacts": [
            "This was the first England-Argentina World Cup semi-final meeting.",
            "Argentina are aiming to become the first side to retain the World Cup since Brazil in 1962.",
            "Hard Rock Stadium hosted a full-capacity night for the last four.",
        ],
        "keyPlayers": [
            {"name": "Lautaro Martínez", "team": "Argentina", "hook": "The focal point of Argentina's finishing when the game opened up."},
            {"name": "Jude Bellingham", "team": "England", "hook": "England's engine room and the man most likely to force chaos in the box."},
        ],
        "headToHead": "World Cup meetings between England and Argentina are rarely quiet. History hangs over every challenge and every set piece.",
        "tags": ["england", "argentina", "semi-final", "world-cup-2026"],
        "home": "England",
        "away": "Argentina",
        "homeCode": "ENG",
        "awayCode": "ARG",
        "homeFlag": "🏴󠁧󠁢󠁥󠁮󠁧󠁿",
        "awayFlag": "🇦🇷",
        "group": "SF",
        "matchday": 7,
        "date": "2026-07-15",
        "time": "20:00",
        "venue": "Hard Rock Stadium",
        "city": "Miami",
        "status": "FINISHED",
        "homeScore": 1,
        "awayScore": 2,
        "marquee": True,
        "liveMinute": None,
        "decidedBy": None,
        "homePen": None,
        "awayPen": None,
        "image": IMAGES["england-vs-argentina-md7"],
    },
    "france-vs-england-md8": {
        "slug": "france-vs-england-md8",
        "headline": "France vs England: Bronze Medal on the Line",
        "whyCareScore": 8.4,
        "whyCareReason": "Two semi-final losers, one last chance to leave North America with a medal.",
        "teaser": "France and England meet in the third-place play-off after agonising semi-final exits. Pride, ranking points and a podium finish are all on the line.",
        "story": (
            "The third-place match is never the one either side dreamed of, but it is still a World Cup night. "
            "France arrive looking to salvage something from a tournament that ended one step short of another final. "
            "England arrive with the same hunger after a semi-final that slipped away late.\n\n"
            "Expect rotation mixed with pride. Managers will rest some legs and still demand a performance. "
            "For players on the fringe of club moves and national hierarchies, this is a stage that still matters.\n\n"
            "Kick-off is set for 18 July. One of these nations will leave with bronze."
        ),
        "stakes": "Third place at the 2026 World Cup. No final, but a medal and lasting ranking value.",
        "rivalryAngle": "Familiar tournament opponents with overlapping club ties and recent knockout pedigree.",
        "funFacts": [
            "The third-place play-off has produced some of the World Cup's freest attacking games.",
            "Both sides reached the last four after winning their groups.",
            "Miami hosts another high-profile European meeting in this tournament.",
        ],
        "keyPlayers": [
            {"name": "Kylian Mbappé", "team": "France", "hook": "Still the most decisive attacker France can throw at open space."},
            {"name": "Harry Kane", "team": "England", "hook": "A proven big-game finisher chasing a podium end to the campaign."},
        ],
        "headToHead": "Recent tournament meetings have been defined by fine margins and set-piece quality.",
        "tags": ["france", "england", "third-place", "world-cup-2026"],
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
        "status": "UPCOMING",
        "homeScore": None,
        "awayScore": None,
        "marquee": True,
        "liveMinute": None,
        "decidedBy": None,
        "homePen": None,
        "awayPen": None,
        "image": IMAGES["france-vs-england-md8"],
    },
    "spain-vs-argentina-md9": {
        "slug": "spain-vs-argentina-md9",
        "headline": "The Final: Spain vs Argentina for the World Cup",
        "whyCareScore": 10.0,
        "whyCareReason": "The biggest match of 2026: possession kings against the holders, one night for the trophy at MetLife Stadium.",
        "teaser": "Spain's tournament control meets Argentina's knockout steel in the 2026 World Cup final on 19 July in New Jersey.",
        "story": (
            "The path is set. Spain have danced through the knockout rounds with control and courage. "
            "Argentina have survived the brutal nights, including a semi-final against England, and still carry the aura of champions.\n\n"
            "MetLife Stadium will host the final chapter of the first 48-team World Cup. One side will complete a statement tournament. "
            "The other will try to author a second straight crowning night.\n\n"
            "Four days separate the last semi-final from kick-off. The world will be watching."
        ),
        "stakes": "The FIFA World Cup. Nothing else remains.",
        "rivalryAngle": "Style clash of the highest order: Spain's positional game against Argentina's balance of structure and moments of magic.",
        "funFacts": [
            "This is the first World Cup final hosted in the New York / New Jersey metro area.",
            "Argentina enter looking to retain the title. Spain enter looking for a first triumph since 2010.",
            "Both finalists topped their groups and won every knockout match in regulation time.",
        ],
        "keyPlayers": [
            {"name": "Lamine Yamal", "team": "Spain", "hook": "The breakout star of the tournament and Spain's widest creative threat."},
            {"name": "Lautaro Martínez", "team": "Argentina", "hook": "Argentina's centre-forward spearhead in the biggest games."},
        ],
        "headToHead": "Major-tournament meetings between Spain and Argentina are rare at this stage, which only raises the intrigue.",
        "tags": ["spain", "argentina", "final", "world-cup-2026"],
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
        "status": "UPCOMING",
        "homeScore": None,
        "awayScore": None,
        "marquee": True,
        "liveMinute": None,
        "decidedBy": None,
        "homePen": None,
        "awayPen": None,
        "image": IMAGES["spain-vs-argentina-md9"],
    },
}


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


def write_story(m: dict) -> None:
    slug = m["slug"]
    path = STORY_DIR / f"{slug}-story.md"
    finished = m["status"] == "FINISHED" and m["homeScore"] is not None
    score = f"{m['homeScore']}-{m['awayScore']}" if finished else "Preview"
    title = m["headline"] if not finished else f"{m['home']} vs {m['away']} {score} Match Report"
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
        body += f"\n## Final Score\n\n**{m['home']} {score} {m['away']}**\n"

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


def main() -> None:
    seed = json.loads(SEED_PATH.read_text(encoding="utf-8"))
    seed["meta"]["today"] = "2026-07-15"

    # Upsert late-knockout fixtures in seed
    by_slug = {f["slug"]: i for i, f in enumerate(seed["fixtures"])}
    for slug, match in MATCHES.items():
        fx = fixture_from_match(match)
        if slug in by_slug:
            seed["fixtures"][by_slug[slug]].update(fx)
            print(f"  updated fixture {slug}")
        else:
            seed["fixtures"].append(fx)
            print(f"  added fixture {slug}")

        # Write match JSON
        mpath = MATCH_DIR / f"{slug}.json"
        mpath.write_text(json.dumps(match, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        write_story(match)
        print(f"  wrote match + story for {slug}")

    # Sort fixtures by date/time for readability
    seed["fixtures"].sort(key=lambda f: (f["date"], f.get("time", ""), f["slug"]))

    SEED_PATH.write_text(json.dumps(seed, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"\nDone. fixtures={len(seed['fixtures'])} today={seed['meta']['today']}")
    print("Finalists: Spain vs Argentina (Jul 19)")
    print("Third place: France vs England (Jul 18)")
    print("Semi-finals: Spain 2-0 France (Jul 14), Argentina 2-1 England (Jul 15)")


if __name__ == "__main__":
    main()
