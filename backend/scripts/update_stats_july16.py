#!/usr/bin/env python3
"""
Update MatchTales stats to verified World Cup 2026 results as of 2026-07-16.

Sources: ESPN fixtures page, FIFA match centre, Yahoo Sports.
Rest day after semis; bronze (Jul 18) and final (Jul 19) remain UPCOMING.

Corrects QF/SF scorelines, AET/pens flags, and Group G Iran-NZ.
Recalculates group standings and syncs match JSON + key narratives.
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

TODAY = "2026-07-16"

# slug -> (homeScore, awayScore, decidedBy|None, homePen|None, awayPen|None)
SCORE_FIXES = {
    # Group G MD2 (ESPN: Iran 2-2 New Zealand)
    "iran-vs-new-zealand-md2": (2, 2, None, None, None),
    # R32
    "netherlands-vs-morocco-md4": (1, 1, "pens", 2, 3),  # ESPN: NED (2) 1-1 (3) MAR
    "belgium-vs-senegal-md4": (3, 2, "aet", None, None),
    "argentina-vs-cape-verde-md4": (3, 2, "aet", None, None),
    # R16
    "switzerland-vs-colombia-md5": (0, 0, "pens", 4, 3),  # ESPN: SUI (4) 0-0 (3) COL
    # QF (Yahoo/ESPN/FourFourTwo)
    "france-vs-morocco-md6": (2, 0, None, None, None),
    "spain-vs-belgium-md6": (2, 1, None, None, None),
    "norway-vs-england-md6": (1, 2, "aet", None, None),
    "argentina-vs-switzerland-md6": (3, 1, "aet", None, None),
    # SF (FIFA/ESPN)
    "france-vs-spain-md7": (0, 2, None, None, None),
    "england-vs-argentina-md7": (1, 2, None, None, None),
}

# Narrative patches for score-sensitive finished knockouts
NARRATIVE_PATCHES = {
    "france-vs-morocco-md6": {
        "headline": "France Blank Morocco 2-0 to Reach the Semi-Finals",
        "whyCareReason": "A heavyweight quarter-final in Boston: Mbappe vs the Atlas Lions, with a World Cup semi-final on the line.",
        "teaser": "France controlled the night and sealed a clean 2-0 win at Gillette Stadium to book their place in the last four.",
        "story": (
            "Boston was a wall of noise as France and Morocco renewed their World Cup rivalry in a quarter-final that lived up to every billing. "
            "Les Bleus struck first through clinical finishing, then kept the Atlas Lions at arm's length for the rest of the night.\n\n"
            "Morocco pushed numbers forward after the break and forced France into a series of blocks and clearances. "
            "Kylian Mbappe remained the constant threat on the counter, stretching Morocco's full-backs whenever space opened.\n\n"
            "When the final whistle confirmed a 2-0 scoreline, France had earned a semi-final ticket with authority. Morocco exited with pride intact after another deep knockout run."
        ),
        "stakes": "A single loss ended Morocco's tournament. France now chase a third straight World Cup final appearance.",
    },
    "spain-vs-belgium-md6": {
        "headline": "Spain Edge Belgium 2-1 and March into the Semis",
        "whyCareReason": "Possession kings against a Belgian side built to disrupt: a quarter-final that decided a semi-final berth.",
        "teaser": "Spain converted two clear chances and survived a late Belgian reply to win 2-1 in the quarter-finals.",
        "story": (
            "Spain arrived with the same patient, positional game that carried them through the group and Round of 16. "
            "Belgium sat deep, looked for transitions, and made La Roja work for every yard of space.\n\n"
            "Spain's midfield eventually found the gaps for a two-goal cushion. Belgium pulled one back late and forced a nervous finish, "
            "but Spain's structure held through the final minutes.\n\n"
            "At 2-1, the quarter-final was settled. Spain advance as one of the tournament's most coherent teams; Belgium's golden generation exits at the last eight."
        ),
        "stakes": "Winner to the semi-finals. Loser goes home after a long knockout road.",
    },
    "norway-vs-england-md6": {
        "headline": "England Survive Norway Scare in 2-1 Extra-Time Thriller",
        "whyCareReason": "Haaland and Odegaard vs the Three Lions: a quarter-final packed with Premier League storylines that needed extra time.",
        "teaser": "England trailed, regrouped, and finished 2-1 winners after extra time against a fearless Norway side.",
        "story": (
            "Norway started like a side with nothing to lose. Early pressure and a clinical finish put England behind and silenced large parts of the stadium. "
            "England's response was pure tournament football: tighter midfield distances, quicker wide switches, and growing territory.\n\n"
            "Regulation finished level on the night's drama before England found the winner in extra time. Norway still threatened through Haaland's runs in behind, "
            "forcing England's back line into last-ditch recovery sprints. The Three Lions managed the final minutes with game-smart fouls and composure in possession.\n\n"
            "England advance 2-1 after extra time. Norway leave with a tournament that reintroduced them as a genuine knockout force."
        ),
        "stakes": "Quarter-final football leaves no safety net. England move on; Norway's revival ends one step short of the semis.",
    },
    "argentina-vs-switzerland-md6": {
        "headline": "Argentina Beat Switzerland 3-1 After Extra Time",
        "whyCareReason": "Champions against Swiss organisation: a quarter-final defined by patience, quality, and extra-time ruthlessness.",
        "teaser": "Argentina needed extra time to break Swiss resistance and seal a 3-1 quarter-final win in Kansas City.",
        "story": (
            "Switzerland did what Switzerland do: compact shape, disciplined distances, and almost zero clear chances conceded before the hour mark. "
            "Argentina monopolised the ball and waited for the moment the Swiss block stretched.\n\n"
            "That moment arrived late and then again in extra time. Well-timed combinations opened the scoring and a third goal closed the contest. "
            "Switzerland pushed numbers forward, but Argentina's game management was ruthless once the lead was secured.\n\n"
            "The 3-1 result after extra time sends the holders into the semi-finals. Switzerland exit after a campaign built on structure and giant-killing ambition."
        ),
        "stakes": "A place in the World Cup semi-finals. Argentina stay on course; Switzerland's run ends in the last eight.",
    },
    "france-vs-spain-md7": {
        "headline": "Spain Blank France 2-0 to Reach the World Cup Final",
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
        "funFacts": [
            "Spain have not lost a knockout match in regulation time all tournament.",
            "France were chasing a third straight World Cup final appearance.",
            "AT&T Stadium hosted one of the highest-profile semi-finals of the expanded 48-team era.",
        ],
    },
    "england-vs-argentina-md7": {
        "headline": "Argentina Edge England 2-1 in a Semi-Final Classic",
        "whyCareReason": "History, heat and a final place on the line: England vs Argentina in a World Cup semi-final.",
        "teaser": "Argentina staged a late comeback to beat England 2-1 and book a return to the World Cup final.",
        "story": (
            "The semi-final carried every layer of history the rivalry always brings. England led and looked set to manage the night, "
            "until Argentina's champion instinct flipped the script in the closing stages.\n\n"
            "Two late goals completed the comeback. England still threatened in the final minutes, but Argentina's game management and "
            "quality in the box proved decisive once more.\n\n"
            "At 2-1 the holders were finalists again. England drop into the third-place play-off after a campaign that reached the last four."
        ),
        "stakes": "A place in the 2026 World Cup final. The loser plays for bronze.",
    },
}


def clean(text: str) -> str:
    return (text or "").replace("—", " - ").replace("--", " - ")


def recalculate_standings(seed: dict) -> dict:
    groups: dict = {}
    for tm in seed["teams"]:
        g = tm["group"]
        groups.setdefault(g, []).append(
            {
                "name": tm["name"],
                "code": tm["code"],
                "flag": tm["flag"],
                "P": 0,
                "W": 0,
                "D": 0,
                "L": 0,
                "GF": 0,
                "GA": 0,
                "GD": 0,
                "Pts": 0,
            }
        )

    def find_row(g: str, name: str):
        for r in groups.get(g, []):
            if r["name"] == name:
                return r
        return None

    for m in seed["fixtures"]:
        if m.get("group") not in groups:
            continue
        if m.get("status") != "FINISHED":
            continue
        hs, aws = m.get("homeScore"), m.get("awayScore")
        if hs is None or aws is None:
            continue
        try:
            hs, aws = int(hs), int(aws)
        except (TypeError, ValueError):
            continue
        hr, ar = find_row(m["group"], m["home"]), find_row(m["group"], m["away"])
        if not hr or not ar:
            continue
        hr["P"] += 1
        ar["P"] += 1
        hr["GF"] += hs
        hr["GA"] += aws
        ar["GF"] += aws
        ar["GA"] += hs
        if hs > aws:
            hr["W"] += 1
            ar["L"] += 1
            hr["Pts"] += 3
        elif hs < aws:
            ar["W"] += 1
            hr["L"] += 1
            ar["Pts"] += 3
        else:
            hr["D"] += 1
            ar["D"] += 1
            hr["Pts"] += 1
            ar["Pts"] += 1

    for g in groups:
        for r in groups[g]:
            r["GD"] = r["GF"] - r["GA"]
        groups[g].sort(key=lambda r: (r["Pts"], r["GD"], r["GF"]), reverse=True)
    return groups


def score_note(m: dict) -> str:
    parts = [f"{m['homeScore']}-{m['awayScore']}"]
    if m.get("decidedBy") == "aet":
        parts.append("AET")
    if m.get("decidedBy") == "pens" and m.get("homePen") is not None:
        parts.append(f"({m['homePen']}-{m['awayPen']} pens)")
    return " ".join(parts)


def write_match_story(match: dict) -> None:
    slug = match["slug"]
    path = STORY_DIR / f"{slug}-story.md"
    finished = match.get("status") == "FINISHED" and match.get("homeScore") is not None
    hs, aws = match.get("homeScore"), match.get("awayScore")
    score = f"{hs}-{aws}" if finished else "Preview"
    title = match.get("headline") if not finished else f"{match['home']} vs {match['away']} {score} Match Report"
    stage = {
        "R32": "Round of 32",
        "R16": "Round of 16",
        "QF": "Quarter-Final",
        "SF": "Semi-Final",
        "3RD": "Third-Place Play-Off",
        "FINAL": "World Cup Final",
        "F": "World Cup Final",
    }.get(match.get("group", ""), f"Group {match.get('group', '')}")

    body = f"""## The Showdown at {match.get('venue', 'the stadium')}

On {match.get('date')}, the footballing world turns its attention to {match.get('venue')} in {match.get('city')} for **{match['home']}** vs **{match['away']}** in the {stage}.

{clean(match.get('story', ''))}

## Stakes and Context

{clean(match.get('stakes', ''))}

{clean(match.get('rivalryAngle', ''))}

### Head-to-Head History

{clean(match.get('headToHead', ''))}

## Key Player Impacts

"""
    for p in match.get("keyPlayers") or []:
        body += f"- **{clean(p.get('name', ''))}** ({clean(p.get('team', ''))}): {clean(p.get('hook', ''))}\n"
    facts = match.get("funFacts") or []
    if facts:
        body += "\n## Match Facts\n\n"
        for f in facts:
            body += f"- {clean(f)}\n"
    if finished:
        note = score_note(match)
        body += f"\n## Final Score\n\n**{match['home']} {note} {match['away']}**\n"

    image = match.get("image") or ""
    fm = (
        "---\n"
        f"title: {json.dumps(title)}\n"
        f"subtitle: {json.dumps(clean(match.get('teaser', '')))}\n"
        f'category: "Match Report"\n'
        f"excerpt: {json.dumps(clean(match.get('whyCareReason', '')))}\n"
        f"image: {json.dumps(image)}\n"
        f"readingTime: 5\n"
        f"pubDate: {match.get('date')}\n"
        "---\n\n"
    )
    path.write_text(fm + body, encoding="utf-8")


def apply_score(target: dict, hs, aws, decided, hp, ap) -> bool:
    changed = False
    for key, val in (
        ("homeScore", hs),
        ("awayScore", aws),
        ("status", "FINISHED"),
        ("liveMinute", None),
        ("decidedBy", decided),
        ("homePen", hp),
        ("awayPen", ap),
    ):
        if target.get(key) != val:
            target[key] = val
            changed = True
    return changed


def main() -> None:
    seed = json.loads(SEED_PATH.read_text(encoding="utf-8"))
    seed["meta"]["today"] = TODAY

    by_slug = {f["slug"]: f for f in seed["fixtures"]}
    score_updates = 0
    narrative_updates = 0

    for slug, (hs, aws, decided, hp, ap) in SCORE_FIXES.items():
        fx = by_slug.get(slug)
        if not fx:
            print(f"  WARN missing fixture: {slug}")
            continue
        if apply_score(fx, hs, aws, decided, hp, ap):
            score_updates += 1
            print(f"  score {slug}: {score_note(fx)}")

        mpath = MATCH_DIR / f"{slug}.json"
        if mpath.exists():
            mdata = json.loads(mpath.read_text(encoding="utf-8"))
            apply_score(mdata, hs, aws, decided, hp, ap)
            if slug in NARRATIVE_PATCHES:
                for k, v in NARRATIVE_PATCHES[slug].items():
                    mdata[k] = v
                narrative_updates += 1
            # Keep core fixture fields aligned
            for k in ("home", "away", "group", "matchday", "date", "time", "venue", "city", "marquee"):
                if k in fx and k in mdata:
                    mdata[k] = fx[k]
            mpath.write_text(json.dumps(mdata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            write_match_story(mdata)
            print(f"  synced match+story {slug}")
        else:
            print(f"  WARN missing match json: {slug}")

    # Refresh rest-day framing for remaining fixtures if present
    for slug in ("france-vs-england-md8", "spain-vs-argentina-md9"):
        mpath = MATCH_DIR / f"{slug}.json"
        if not mpath.exists():
            continue
        mdata = json.loads(mpath.read_text(encoding="utf-8"))
        # Ensure score fields stay upcoming
        mdata["status"] = "UPCOMING"
        mdata["homeScore"] = None
        mdata["awayScore"] = None
        mdata["liveMinute"] = None
        # Patch SF score references in final preview if needed
        if slug == "spain-vs-argentina-md9":
            story = mdata.get("story", "")
            story = story.replace("Spain beat France 2-1", "Spain beat France 2-0")
            story = story.replace("Spain 2-1 France", "Spain 2-0 France")
            mdata["story"] = story
            mpath.write_text(json.dumps(mdata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            write_match_story(mdata)
            print(f"  refreshed final preview {slug}")

    # Update editorial SF score reference if present
    editorial = STORY_DIR / "final-week-countdown-spain-argentina.md"
    if editorial.exists():
        text = editorial.read_text(encoding="utf-8")
        new_text = text.replace("Spain beat France 2-1", "Spain beat France 2-0")
        new_text = new_text.replace("Spain 2-1 France", "Spain 2-0 France")
        if new_text != text:
            editorial.write_text(new_text, encoding="utf-8")
            print("  fixed editorial SF scoreline")

    # Moments text for SF
    for mo in seed.get("moments") or []:
        if mo.get("title", "").startswith("Spain 2-1 France"):
            mo["title"] = "Spain 2-0 France: Dallas Semi-Final"
            mo["text"] = (
                "La Roja produced a controlled 2-0 semi-final win over France to book the first place in the MetLife final."
            )
            print("  updated Spain SF moment")
        if mo.get("title", "").startswith("Argentina 2-1 England"):
            mo["text"] = (
                "Argentina staged a late comeback to beat England 2-1 and reach another World Cup final."
            )

    seed["groups"] = recalculate_standings(seed)
    seed["fixtures"].sort(key=lambda f: (f["date"], f.get("time", ""), f["slug"]))
    SEED_PATH.write_text(json.dumps(seed, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"\nDone. score_updates={score_updates} narratives={narrative_updates} today={TODAY}")
    print("Group G (top of table after Iran-NZ fix):")
    for r in seed["groups"].get("G", []):
        print(f"  {r['name']:20} P{r['P']} W{r['W']} D{r['D']} L{r['L']} GF{r['GF']} GA{r['GA']} GD{r['GD']} Pts{r['Pts']}")


if __name__ == "__main__":
    main()
