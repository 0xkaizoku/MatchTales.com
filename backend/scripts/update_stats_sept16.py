#!/usr/bin/env python3
"""Write sourced 16 September 2026 desk events.

Editorial clock is 16 September: Monday night is finished, Tuesday's cups are
finished, Thursday night in Buffalo has not kicked.
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
    headline="Leeds 4-1 Newcastle: third in the table, Jaissle's first defeat",
    whyCareScore=9.4,
    whyCareReason="Unbeaten Leeds go third. Miley own goal, Bogle, Calvert-Lewin, Okafor. Touré's 90th-minute reply is the only Newcastle shot that counted.",
    teaser="FINAL: Leeds 4-1 Newcastle. Miley OG 32', Bogle 34', Calvert-Lewin 45+1', Okafor 59', Touré 90'. Leeds 2-2-0, 8 points.",
    story="Why this one matters: both clubs arrived on five points from three games. The rest of matchweek 4 was already in the book. Elland Road finished it 4-1, and Leeds are third.\n\nESPN: Lewis Miley own goal 32', a double deflection after Ao Tanaka struck from the edge of the box. Jayden Bogle 34', after Calvert-Lewin's header from James Justin's cross clipped him on the way in. Dominic Calvert-Lewin 45+1', side-stepping Sven Botman. Noah Okafor 59' on the half-volley after Ethan Ampadu's long throw. Bazoumana Touré 90' for Newcastle. Nico González went off in the 20th minute; Sean Steur came on.\n\nSky, AFP and The Athletic print the same 4-1. Leeds 2-2-0, 8 points, plus four. Newcastle 1-2-1, 5 points, 12th. First league defeat for Matthias Jaissle.",
    stakes="Matchweek 4 is closed. Arsenal 12, City 12, Leeds 8, Hull 8. Newcastle slip on goal difference.",
    rivalryAngle="Two unbeaten league starts met on a Monday. Only one left Elland Road still unbeaten.",
    funFacts=["Miley own goal 32', Tanaka's shot deflected off Steur then Miley.", "Bogle given the 34th-minute goal after Calvert-Lewin's header clipped him.", "Okafor 59' from Ampadu's long throw. Touré 90' consolation."],
    keyPlayers=[{"name": "Dominic Calvert-Lewin", "team": "Leeds United", "hook": "Winner of the night's third, 45+1', after the Bogle deflection."}, {"name": "Noah Okafor", "team": "Leeds United", "hook": "Fourth goal, 59th minute, half-volley, 4-0."}],
    home="Leeds United", away="Newcastle United", group="PL", date="2026-09-14", time="20:00",
    venue="Elland Road", city="Leeds", status="FINISHED", liveMinute=None, homeScore=4, awayScore=1,
    sport="soccer", competition="premier-league-2026-27", season="2026/27", roundLabel="Matchweek 4",
    resultSummary="Leeds 4-1 Newcastle",
    tags=["premier-league", "leeds", "newcastle"],
    sources=[{"name": "ESPN: Leeds 4-1 Newcastle", "url": "https://www.espn.co.uk/football/report/_/gameId/401879280"}, {"name": "Sky Sports: Leeds 4-1 Newcastle", "url": "https://www.skysports.com/football/news/33694/13583594/leeds-4-1-newcastle-matthias-jaissle-handed-first-defeat-as-magpies-boss-as-dominic-calvert-lewin-leads-elland-road-rout"}, {"name": "The Athletic: Leeds blow Newcastle away", "url": "https://www.nytimes.com/athletic/7586940/2026/09/14/leeds-newcastle-score-result-analysis/"}],
))

EVENTS.append(ev(
    slug="broncos-at-chiefs-mnf-2026",
    headline="Chiefs 31-10 Broncos: Walker 173, Mahomes back, Week 1 closed",
    whyCareScore=9.3,
    whyCareReason="Kenneth Walker III ran for 173 yards and scored twice on his Chiefs debut. Patrick Mahomes returned from the knee with three total touchdowns. Denver left with 176 yards.",
    teaser="FINAL: Chiefs 31, Broncos 10. Walker 23-173, two TDs. Mahomes 15-27, 184, two passing TDs, one rushing. Attendance 73,543.",
    story="Why this one matters: Week 1 already had a Super Bowl rematch, an Australia game, a 59-37 in Charlotte, a 31-30 overtime in Detroit, and Giants 28-20 on Sunday night. Monday night at Arrowhead closed the book 31-10.\n\nPro-Football-Reference: Broncos 7-0-3-0, Chiefs 7-7-10-7. Mahomes 15-yard rush at 8:11 of the first. Bo Nix to Evan Engram, 19 yards, 7-7. Rashee Rice 13-yard catch late in the second, 14-7. Walker 60-yard rush in the third. Wil Lutz 31-yard field goal. Harrison Butker 28 after Travis Kelce's 59-yard catch. Walker 2-yard receiving score early in the fourth.\n\nESPN, FOX and the Denver Post agree on 31-10. Walker 23 carries, 173 yards, one rushing touchdown, three catches, 18 yards, one receiving touchdown. Mahomes 15 of 27, 184 yards, two passing touchdowns, one interception, one rushing touchdown. Nix 17 of 28, 131 yards, one touchdown, one interception, four sacks, three fumbles, one lost. Chiefs 220 rushing yards. Attendance 73,543. Kansas City 1-0. Denver 0-1.",
    stakes="Week 1 is finished. Every game was won by a different margin. Thursday is Lions at Bills in a new stadium.",
    rivalryAngle="AFC West, Mahomes' first snap since the knee, Walker's first night in red.",
    funFacts=["Walker 173 rushing yards, career high, two total TDs.", "Chiefs 220 rush yards, 392 total. Broncos 176 total, 61 rush.", "Attendance 73,543. Game time 2:59."],
    keyPlayers=[{"name": "Kenneth Walker III", "team": "Chiefs", "hook": "23-173, 60-yard rush, 2-yard receiving TD. Chiefs debut."}, {"name": "Patrick Mahomes", "team": "Chiefs", "hook": "First regular-season snap since the knee. 15-yard rushing TD, two passing TDs."}],
    home="Kansas City Chiefs", away="Denver Broncos", group="NFL", date="2026-09-14", time="20:15",
    venue="Arrowhead Stadium", city="Kansas City", status="FINISHED", liveMinute=None, homeScore=31, awayScore=10,
    sport="football", competition="nfl-2026", season="2026", roundLabel="Week 1 · MNF",
    resultSummary="Chiefs 31, Broncos 10",
    tags=["nfl", "chiefs", "broncos", "mnf"],
    sources=[{"name": "Pro-Football-Reference: Broncos at Chiefs", "url": "https://www.pro-football-reference.com/boxscores/202609140kan.htm"}, {"name": "ESPN: Chiefs 31-10 Broncos", "url": "https://www.espn.com/nfl/game/_/gameId/401872931/broncos-chiefs"}, {"name": "BBC: Walker stars for Chiefs", "url": "https://www.bbc.co.uk/sport/articles/cqx2z5edy37po"}],
))

EVENTS.append(ev(
    slug="ipswich-vs-arsenal-carabao-2026",
    headline="Dowman twice, Arsenal 4-2 at Ipswich, seven from seven",
    whyCareScore=8.7,
    whyCareReason="A 16-year-old scores twice on his first start of the season. Arsenal rotate and still go through. Ipswich get two back when it is already 4-0.",
    teaser="FINAL: Ipswich 2-4 Arsenal. Dowman 7', 47'. Madueke 16'. Merino 58'. Mehmeti 62', Akpom 90+1'.",
    story="Why this one matters: the champions had already won four league games. Tuesday was the Carabao Cup third round, a rotated side, and a 16-year-old who had not started this season.\n\nESPN and Sky: Max Dowman 7' and 47', Noni Madueke 16', Mikel Merino 58'. Anis Mehmeti 62' after Jack Clarke came on. Chuba Akpom 90+1' against his old club. Opta via Sky: Dowman is 16 years 258 days, the third-youngest League Cup scorer for a Premier League side after Cesc Fabregas and Jack Wilshere.\n\nThe Guardian: Arsenal are seven wins from seven in all competitions. Marli Salmon started next to Gabriel. That is a cup result, not a league table line. The league table is still Arsenal 12 from four.",
    stakes="Fourth round of the League Cup. A teenager with two senior goals on the night. League points unchanged.",
    rivalryAngle="A rotated champion against a promoted side that already has six league points.",
    funFacts=["Dowman 7' and 47', first start of the season.", "Madueke 16', Merino 58', first league-cup goals of the campaign.", "Mehmeti 62', Akpom 90+1'."],
    keyPlayers=[{"name": "Max Dowman", "team": "Arsenal", "hook": "Two goals, 16 years 258 days, first start of 2026/27."}, {"name": "Mikel Merino", "team": "Arsenal", "hook": "Stand-in captain. Fourth goal, 58th minute, in off the post."}],
    home="Ipswich Town", away="Arsenal", group="EFL", date="2026-09-15", time="20:00",
    venue="Portman Road", city="Ipswich", status="FINISHED", liveMinute=None, homeScore=2, awayScore=4,
    sport="soccer", competition="carabao-cup-2026-27", season="2026/27", roundLabel="Carabao Cup third round",
    resultSummary="Ipswich 2-4 Arsenal",
    tags=["carabao-cup", "arsenal", "ipswich", "dowman"],
    sources=[{"name": "ESPN: Ipswich 2-4 Arsenal", "url": "https://www.espn.co.uk/football/report/_/gameId/401914268"}, {"name": "Sky Sports: Dowman double", "url": "https://www.skysports.com/football/news/11095/13582699/ipswich-2-4-arsenal-max-dowman-shines-with-two-goals-as-gunners-ease-into-carabao-cup-fourth-round"}, {"name": "The Guardian: Dowman doubles up", "url": "https://www.theguardian.com/football/2026/sep/15/ipswich-arsenal-carabao-cup-third-round-match-report"}],
))

EVENTS.append(ev(
    slug="liverpool-vs-tottenham-carabao-2026",
    headline="Liverpool 3-1 Tottenham: Szoboszlai from distance, Spurs still without a win",
    whyCareScore=8.8,
    whyCareReason="Mac Allister, Gakpo, then a stoppage-time rocket. Gallagher scored Spurs' first against a top-flight side this season. It was not enough.",
    teaser="FINAL: Liverpool 3-1 Tottenham. Mac Allister 21', Gakpo 54', Gallagher 69', Szoboszlai 90+1'.",
    story="Why this one matters: Tottenham had two league points and no league goals. Tuesday at Anfield was supposed to be a cup reset. It became 3-1 and another exit.\n\nSky: Alexis Mac Allister 21', first-time into the roof of the net. Cody Gakpo 54'. Conor Gallagher 69' from a corner, Tottenham's first goal against top-flight opposition this season. Dominik Szoboszlai 90+1' from distance. Giorgi Mamardashvili denied Lucas Bergvall early and Omar Marmoush late.\n\nThe Independent: Andoni Iraola made ten changes and still went through. Roberto De Zerbi called the result unfair. Spurs named a strong side and still have no win in 2026/27.",
    stakes="Liverpool in the last 16. Tottenham out of one of three remaining competitions, still winless.",
    rivalryAngle="A cup tie between two league underachievers. Only one of them can still use the League Cup as a season.",
    funFacts=["Mac Allister 21', Gakpo 54', Szoboszlai 90+1'.", "Gallagher 69': Spurs' first goal against a top-flight side this season.", "Iraola made ten changes."],
    keyPlayers=[{"name": "Dominik Szoboszlai", "team": "Liverpool", "hook": "Stoppage-time strike from distance, 3-1."}, {"name": "Conor Gallagher", "team": "Tottenham Hotspur", "hook": "Header, 69th minute. First Spurs goal against a top-flight side this season."}],
    home="Liverpool", away="Tottenham Hotspur", group="EFL", date="2026-09-15", time="20:00",
    venue="Anfield", city="Liverpool", status="FINISHED", liveMinute=None, homeScore=3, awayScore=1,
    sport="soccer", competition="carabao-cup-2026-27", season="2026/27", roundLabel="Carabao Cup third round",
    resultSummary="Liverpool 3-1 Tottenham",
    tags=["carabao-cup", "liverpool", "tottenham"],
    sources=[{"name": "Sky Sports: Liverpool 3-1 Tottenham", "url": "https://www.skysports.com/football/news/11095/13582687/liverpool-3-1-tottenham-dominik-szoboszlai-strike-seals-carabao-cup-win-as-spurs-at-least-end-goal-drought"}, {"name": "The Independent: Liverpool v Tottenham", "url": "https://www.independent.co.uk/sport/football/liverpool-tottenham-result-player-ratings-carabao-cup-b3050755.html"}],
))

EVENTS.append(ev(
    slug="lions-at-bills-tnf-2026",
    headline="Lions at Bills: Thursday night, a new Highmark Stadium, no snap yet",
    whyCareScore=9.0,
    whyCareReason="Two 1-0 clubs. Prime Video, 8:15 p.m. ET. First regular-season game in Buffalo's new stadium. Do not invent a score.",
    teaser="Thursday 17 September. Detroit at Buffalo. Week 1 is in the book. This one is not.",
    story="Why this one matters: Week 1 closed 31-10 in Kansas City. Week 2 opens in a building that has not hosted a regular-season snap.\n\nNFL.com and ESPN: Lions at Bills, Highmark Stadium, Orchard Park, 8:15 p.m. ET, Prime Video. Both clubs are 1-0. Buffalo beat Houston 36-31. Detroit beat New Orleans 31-30 in overtime. That is the honest line on 16 September.\n\nPrint the time. Print the stadium. Do not print a winner.",
    stakes="The first Thursday of 2026, in a new stadium, between two clubs that already scored in Week 1.",
    rivalryAngle="AFC East host, NFC North visitor, a stadium opener instead of a rivalry.",
    funFacts=["Kickoff 8:15 p.m. ET, Prime Video.", "Both teams 1-0 until this game.", "First regular-season game at the new Highmark Stadium."],
    keyPlayers=[{"name": "Josh Allen", "team": "Bills", "hook": "Home, new stadium, 1-0 after Houston."}, {"name": "Jared Goff", "team": "Lions", "hook": "Road, 1-0 after overtime in Week 1. No Thursday score yet."}],
    home="Buffalo Bills", away="Detroit Lions", group="NFL", date="2026-09-17", time="20:15",
    venue="Highmark Stadium", city="Orchard Park", status="UPCOMING",
    sport="football", competition="nfl-2026", season="2026", roundLabel="Week 2 · TNF",
    tags=["nfl", "bills", "lions", "tnf"],
    sources=[{"name": "NFL.com: Lions at Bills Week 2", "url": "https://www.nfl.com/news/lions-bills-week-2-prime-video-2026-nfl-schedule-release"}, {"name": "ESPN NFL schedule Week 2", "url": "https://www.espn.com/nfl/schedule/_/week/2"}],
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
