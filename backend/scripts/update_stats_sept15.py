#!/usr/bin/env python3
"""Write sourced 15 September 2026 (IST morning) desk events.

Editorial clock stays 14 September: it is still Monday night in the UK and US.
Leeds vs Newcastle is LIVE. Broncos at Chiefs has not kicked.
Scores only from named reports. No invented full-time.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2] / "frontend" / "src" / "content" / "matches"

IMG = {
    "soccer": "https://images.unsplash.com/photo-1574629810360-7efbbe195018?auto=format&fit=crop&w=1200&q=80",
    "tennis": "https://images.unsplash.com/photo-1554068865-24cecd4e34b8?auto=format&fit=crop&w=1200&q=80",
    "golf": "https://images.unsplash.com/photo-1535131749006-b7f58c99034b?auto=format&fit=crop&w=1200&q=80",
    "football": "https://images.unsplash.com/photo-1566577739112-5184e6ac4a4e?auto=format&fit=crop&w=1200&q=80",
    "basketball": "https://images.unsplash.com/photo-1546519638-68e109498ffc?auto=format&fit=crop&w=1200&q=80",
    "f1": "https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?auto=format&fit=crop&w=1200&q=80",
}


def ev(**kwargs):
    sport = kwargs["sport"]
    base = {
        "funFacts": kwargs.pop("funFacts"),
        "keyPlayers": kwargs.pop("keyPlayers"),
        "headToHead": kwargs.pop("headToHead", ""),
        "tags": kwargs.pop("tags", []),
        "homeCode": kwargs.pop("homeCode", None),
        "awayCode": kwargs.pop("awayCode", None),
        "homeFlag": "",
        "awayFlag": "",
        "matchday": kwargs.pop("matchday", 0),
        "marquee": True,
        "liveMinute": kwargs.pop("liveMinute", None),
        "image": kwargs.pop("image", IMG[sport]),
        "decidedBy": kwargs.pop("decidedBy", None),
        "homePen": None,
        "awayPen": None,
        "season": kwargs.pop("season", ""),
        "roundLabel": kwargs.pop("roundLabel", ""),
        "resultSummary": kwargs.pop("resultSummary", ""),
        "leaderboard": kwargs.pop("leaderboard", []),
        "tennisSets": kwargs.pop("tennisSets", []),
        "sources": kwargs.pop("sources", []),
        "format": kwargs.pop("format", "team-match"),
        "homeScore": kwargs.pop("homeScore", None),
        "awayScore": kwargs.pop("awayScore", None),
    }
    base.update(kwargs)
    return base


EVENTS = []

EVENTS.append(ev(
    slug="leeds-vs-newcastle-mw4",
    headline="Leeds 2-0 Newcastle: Miley own goal, then Calvert-Lewin, still live",
    whyCareScore=9.2,
    whyCareReason="Two goals in two minutes at Elland Road. The table after Sunday is not the table yet. The match is not finished.",
    teaser="LIVE 36': Leeds 2-0 Newcastle. Lewis Miley own goal 32'. Dominic Calvert-Lewin header 34', James Justin the assist.",
    story="Why this one matters: both clubs arrived on five points from three games. The rest of matchweek 4 was already in the book. Elland Road was the last fixture, and it has a live score.\n\nESPN at 36 minutes: Leeds 2-0. Lewis Miley's own goal at 32', a deflection after Ao Tanaka struck from the left. Dominic Calvert-Lewin headed in at 34' from James Justin's cross. Nico Gonzalez went off in the 19th minute as a concussion substitute for Sean Steur. That is the score. That is not a result.\n\nPrint 2-0 and 36 minutes. Do not print full time. The table after Sunday still has both clubs on three games until this one ends.",
    stakes="Five points each when it started. A live chance to jump the mid-table pile. Not decided.",
    rivalryAngle="Two unbeaten league starts, one Monday night, two goals that have not closed the night.",
    funFacts=["Miley own goal 32'.", "Calvert-Lewin header 34', Justin assist.", "Gonzalez off 19', concussion substitute Steur."],
    keyPlayers=[{"name": "Dominic Calvert-Lewin", "team": "Leeds United", "hook": "Header, 34th minute, 2-0."}, {"name": "Lewis Miley", "team": "Newcastle United", "hook": "Own goal, 32nd minute, 1-0."}],
    home="Leeds United", away="Newcastle United", group="PL", date="2026-09-14", time="20:00",
    venue="Elland Road", city="Leeds", status="LIVE", liveMinute=36, homeScore=2, awayScore=0,
    sport="soccer", competition="premier-league-2026-27", season="2026/27", roundLabel="Matchweek 4",
    resultSummary="LIVE 36': Leeds 2-0 Newcastle",
    tags=["premier-league", "leeds", "newcastle"],
    sources=[{"name": "ESPN: Leeds vs Newcastle live", "url": "https://www.espn.com/soccer/match/_/gameId/401879280"}, {"name": "The Athletic live blog", "url": "https://www.nytimes.com/athletic/live-blogs/leeds-vs-newcastle-live-updates-premier-league-score-result/26fITQs9mbRr/"}],
))

EVENTS.append(ev(
    slug="broncos-at-chiefs-mnf-2026",
    headline="Broncos at Chiefs: Monday night, Week 1 still has one snap left",
    whyCareScore=9.1,
    whyCareReason="Arrowhead, 8:15 p.m. ET, ESPN/ABC. Sunday is locked. This one has not been played. Do not invent a score.",
    teaser="Monday 14 September. Denver at Kansas City. Giants 28-20 on Sunday night. This kickoff is still to come.",
    story="Why this one matters: Week 1 already has a Super Bowl rematch, an Australia game, a 59-37 in Charlotte, a 31-30 overtime in Detroit, and Giants 28-20 on Sunday night. It does not yet have a Monday night result.\n\nBroncos at Chiefs, Arrowhead Stadium, 8:15 p.m. ET, ESPN and ABC. ESPN's scoreboard still lists both clubs 0-0 with kickoff to come. That is the honest line while Elland Road is live.\n\nPrint the time. Print the channel. Do not print a winner.",
    stakes="The last result of Week 1, in a building that has lived on them.",
    rivalryAngle="AFC West, a Sunday leftover on Monday night.",
    funFacts=["Kickoff 8:15 p.m. ET, ESPN/ABC.", "Both teams 0-0 until this game.", "Sunday night already finished: Giants 28, Cowboys 20."],
    keyPlayers=[{"name": "Patrick Mahomes", "team": "Chiefs", "hook": "Cleared to start. First regular-season snap since the knee."}, {"name": "Bo Nix", "team": "Broncos", "hook": "First meaningful game since the playoff ankle."}],
    home="Kansas City Chiefs", away="Denver Broncos", group="NFL", date="2026-09-14", time="20:15",
    venue="Arrowhead Stadium", city="Kansas City", status="UPCOMING",
    sport="football", competition="nfl-2026", season="2026", roundLabel="Week 1 · MNF",
    tags=["nfl", "chiefs", "broncos", "mnf"],
    sources=[{"name": "ESPN NFL scoreboard", "url": "https://www.espn.com/nfl/scoreboard"}, {"name": "FOX Week 1 schedule", "url": "https://www.foxsports.com/stories/nfl/when-does-2026-nfl-season-start-complete-week-1-schedule"}],
))


def main():
    ROOT.mkdir(parents=True, exist_ok=True)
    for e in EVENTS:
        path = ROOT / f"{e['slug']}.json"
        path.write_text(json.dumps(e, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
        print("wrote", path.name)
    print("total", len(EVENTS))


if __name__ == "__main__":
    main()
