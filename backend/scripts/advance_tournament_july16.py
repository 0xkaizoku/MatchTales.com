#!/usr/bin/env python3
"""
Advance MatchTales to tournament state as of 2026-07-16.

Rest day after the semi-finals:
  - Spain 2-0 France (Jul 14) and Argentina 2-1 England (Jul 15) remain FINISHED
  - Third-place (MD8): France vs England (Jul 18) UPCOMING
  - Final (MD9): Spain vs Argentina (Jul 19) UPCOMING

Also refreshes final-week previews and adds a countdown editorial story.
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

TODAY = "2026-07-16"

IMAGES = {
    "france-vs-england-md8": "https://images.unsplash.com/photo-1508098682722-e99c43a406b2?crop=entropy&cs=srgb&fm=jpg&q=85&w=1200",
    "spain-vs-argentina-md9": "https://images.unsplash.com/photo-1574629810360-7efbbe195018?crop=entropy&cs=srgb&fm=jpg&q=85&w=1200",
    "final-week-countdown": "https://images.unsplash.com/photo-1529900748604-07564a03e7a6?crop=entropy&cs=srgb&fm=jpg&q=85&w=1200",
}

# Refresh only the remaining fixtures with rest-day countdown framing
MATCH_UPDATES = {
    "france-vs-england-md8": {
        "slug": "france-vs-england-md8",
        "headline": "Bronze Battle: France and England Prepare for Miami",
        "whyCareScore": 8.5,
        "whyCareReason": "Two days out from the third-place play-off: pride, ranking points and one last World Cup night for two semi-finalists.",
        "teaser": "After crushing semi-final exits, France and England have 48 hours to reset and decide who leaves North America with bronze.",
        "story": (
            "The last four are decided. Spain and Argentina wait in the final, and the other half of the semi-final story now turns to Miami. "
            "France and England still have a medal on the table, even if neither squad dreamed of this fixture a week ago.\n\n"
            "Rest-day work is tactical and emotional. Managers balance rotation against pride. Players on the fringe of club futures still see a stage "
            "that can change a career. Supporters who followed every knockout night want one more performance that feels like them.\n\n"
            "Kick-off is 18 July at Hard Rock Stadium. Bronze is not the trophy, but it is still a podium finish on the biggest stage in sport."
        ),
        "stakes": "Third place at the 2026 World Cup. Ranking points, pride, and a medal after semi-final heartbreak.",
        "rivalryAngle": "Familiar European rivals with club-level connections and recent tournament pedigree meeting with nothing left to protect except dignity.",
        "funFacts": [
            "The third-place play-off often produces open, high-scoring football after the tension of the last four.",
            "Both nations won their groups before reaching the semi-finals.",
            "Miami hosts its second major knockout night of the final week.",
        ],
        "keyPlayers": [
            {"name": "Kylian Mbappé", "team": "France", "hook": "Still France's most decisive outlet when games stretch into open space."},
            {"name": "Harry Kane", "team": "England", "hook": "A big-game finisher chasing a podium end to England's long campaign."},
        ],
        "headToHead": "Recent tournament meetings have been decided by fine margins, set pieces and who keeps their nerve longest.",
        "tags": ["france", "england", "third-place", "world-cup-2026", "final-week"],
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
        "headline": "Three Days to MetLife: Spain vs Argentina Final Watch",
        "whyCareScore": 10.0,
        "whyCareReason": "The final is set: Spain's control against Argentina's knockout steel at MetLife Stadium on 19 July.",
        "teaser": "Three days separate the football world from the 2026 World Cup final as Spain and Argentina prepare for New Jersey.",
        "story": (
            "The path is locked. Spain beat France 2-0 in Dallas. Argentina beat England 2-1 in Miami. "
            "Now the first 48-team World Cup points toward a single night at MetLife Stadium.\n\n"
            "Spain arrive as the tournament's most coherent team: midfield control, wide threat, and the confidence of a side that has not lost in regulation "
            "through the knockouts. Argentina arrive with champion steel, surviving the brutal nights and still carrying the aura of title holders.\n\n"
            "Rest days are for recovery, video, and quiet belief. On 19 July one of these nations lifts the trophy. The other joins the long list of nearly nights."
        ),
        "stakes": "The FIFA World Cup. Nothing else remains.",
        "rivalryAngle": "Style clash of the highest order: Spanish positional control against Argentina's structure, moments of magic and final experience.",
        "funFacts": [
            "This is the first World Cup final hosted in the New York / New Jersey metro area.",
            "Argentina are chasing back-to-back titles. Spain are chasing a first triumph since 2010.",
            "Both finalists topped their groups and won every knockout match in regulation time.",
        ],
        "keyPlayers": [
            {"name": "Lamine Yamal", "team": "Spain", "hook": "The breakout star of the tournament and Spain's widest creative threat."},
            {"name": "Lautaro Martínez", "team": "Argentina", "hook": "Argentina's centre-forward spearhead when the biggest nights open up."},
        ],
        "headToHead": "Major-tournament meetings between Spain and Argentina are rare at this stage, which only raises the intrigue.",
        "tags": ["spain", "argentina", "final", "world-cup-2026", "final-week"],
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

EDITORIAL = {
    "slug": "final-week-countdown-spain-argentina",
    "title": "Final Week Countdown: Spain, Argentina and Two Nights Left",
    "subtitle": "Semis done. Bronze on Saturday. The final on Sunday. How the last chapter of World Cup 2026 is shaping up.",
    "category": "Final Week",
    "excerpt": "A rest-day guide to the podium race: France vs England for bronze, then Spain vs Argentina for the world title.",
    "image": IMAGES["final-week-countdown"],
    "readingTime": 6,
    "pubDate": TODAY,
}

EDITORIAL_BODY = """## The Quiet Between Storms

There are no fixtures on 16 July. After a semi-final week that sent Spain and Argentina to the final and France and England into the bronze match, the tournament finally exhales.

That pause matters. Final-week football is not only tactics and travel. It is recovery rooms, quiet hotel corridors, and the strange mix of relief and dread that comes when only one match remains between you and history.

## How We Got Here

Spain beat France 2-0 in Dallas on 14 July, a semi-final of control and quality. Argentina beat England 2-1 in Miami on 15 July, staging a late comeback to book a return to the biggest night.

Those results set a clean bracket for the first 48-team World Cup:
- **18 July, Miami**: France vs England (third place)
- **19 July, MetLife Stadium**: Spain vs Argentina (final)

## Bronze Still Means Something

The third-place match will never be the final, but it is still a World Cup night with a medal. France and England both won their groups and both fell one step short. Miami gives them ninety minutes to leave with pride and ranking value rather than only what-ifs.

Expect rotation mixed with urgency. Managers will protect tired legs and still demand a performance their supporters can live with.

## The Final Is a Style Clash

Spain have looked like the tournament's most complete side: midfield distances, wide threat, and the calm of a team that keeps solving problems. Argentina still carry champion aura, knockout toughness, and the ability to win ugly when nights turn chaotic.

MetLife Stadium will host the crowning night of a tournament that stretched across the United States, Mexico and Canada. One nation will complete a statement campaign. The other will join the long list of sides who came within a single match of the trophy.

## What to Watch Over the Rest Days

- **Recovery first**: both finalists need fresh legs more than tactical reinvention.
- **Set pieces**: late knockout matches often swing on dead-ball quality.
- **Wide channels**: Yamal's threat for Spain versus Argentina's rest defence will be a central plotline.
- **Bench impact**: bronze and final nights reward squads that can change a game after the hour.

Two nights left. The stories are already written in outline. The scores still have to be lived.
"""

NEW_MOMENTS = [
    {
        "year": 2026,
        "title": "Spain 2-0 France: Dallas Semi-Final",
        "team": "Spain",
        "text": "La Roja produced a controlled 2-0 semi-final win over France to book the first place in the MetLife final.",
    },
    {
        "year": 2026,
        "title": "Argentina 2-1 England: Miami Semi-Final",
        "team": "Argentina",
        "text": "Argentina survived a late England surge to reach another World Cup final and keep the dream of retaining the title alive.",
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
    title = m["headline"] if not finished else f"{m['home']} vs {m['away']} {score} Match Report"
    stage = {
        "SF": "Semi-Final",
        "3RD": "Third-Place Play-Off",
        "FINAL": "World Cup Final",
        "F": "World Cup Final",
    }.get(m["group"], m["group"])

    body = f"""## The Showdown at {m['venue']}

On {m['date']}, the footballing world turns its attention to {m['venue']} in {m['city']} for **{m['home']}** vs **{m['away']}** in the {stage}.

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

    # Prepend editorial to storiesMeta if missing
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

    # Prepend new moments if missing
    moments = seed.get("moments") or []
    existing_titles = {m.get("title") for m in moments}
    for mo in reversed(NEW_MOMENTS):
        if mo["title"] not in existing_titles:
            moments.insert(0, mo)
            print(f"  added moment {mo['title']}")
    seed["moments"] = moments[:8]

    seed["fixtures"].sort(key=lambda f: (f["date"], f.get("time", ""), f["slug"]))
    SEED_PATH.write_text(json.dumps(seed, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"\nDone. fixtures={len(seed['fixtures'])} today={seed['meta']['today']}")
    print("Rest day: 2026-07-16")
    print("Next: France vs England (Jul 18 bronze), Spain vs Argentina (Jul 19 final)")


if __name__ == "__main__":
    main()
