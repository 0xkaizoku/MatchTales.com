#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Apply verified 11 November 2026 desk: fixes for Nov 10 data, 8 match JSONs, 6 stories, sports.ts, desk.json, AGENTS.md."""
import json
import os
import re
import urllib.request

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
MATCHES = os.path.join(ROOT, "frontend/src/content/matches")
STORIES = os.path.join(ROOT, "frontend/src/content/stories")

IMG = {
    "nfl": "https://images.pexels.com/photos/209954/pexels-photo-209954.jpeg?auto=compress&cs=tinysrgb&w=1600&h=900&fit=crop",
    "nba": "https://images.pexels.com/photos/248547/pexels-photo-248547.jpeg?auto=compress&cs=tinysrgb&w=1600&h=900&fit=crop",
    "ten": "https://images.pexels.com/photos/1618210/pexels-photo-1618210.jpeg?auto=compress&cs=tinysrgb&w=1600&h=900&fit=crop",
    "f1": "https://images.pexels.com/photos/627678/pexels-photo-627678.jpeg?auto=compress&cs=tinysrgb&w=1600&h=900&fit=crop",
    "golf": "https://images.pexels.com/photos/863988/pexels-photo-863988.jpeg?auto=compress&cs=tinysrgb&w=1600&h=900&fit=crop",
    "soc": "https://images.pexels.com/photos/1171084/pexels-photo-1171084.jpeg?auto=compress&cs=tinysrgb&w=1600&h=900&fit=crop",
}


def check_dashes(obj, path=""):
    if isinstance(obj, dict):
        for k, v in obj.items():
            check_dashes(v, f"{path}.{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            check_dashes(v, f"{path}[{i}]")
    elif isinstance(obj, str):
        s = re.sub(r"https?://\S+", "", obj)
        if "\u2014" in s or "--" in s:
            raise ValueError(f"Disallowed dash at {path}: {s[:80]}")


def dump(path, obj):
    check_dashes(obj, os.path.basename(path))
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print("wrote", path)


def get_ok(url):
    req = urllib.request.Request(url, method="GET", headers={"User-Agent": "Mozilla/5.0 MatchTales"})
    with urllib.request.urlopen(req, timeout=20) as r:
        if r.status != 200:
            raise SystemExit(f"image GET {url} -> {r.status}")
        print("GET 200", url.split("?")[0])


if __name__ == "__main__":
    for u in IMG.values():
        get_ok(u)

    # =========================================================================
    # PART 1: Correct factual errors in 3 Nov 9-10 match JSONs
    # =========================================================================

    bills_fix = {
        "slug": "bills-at-vikings-mnf-week9-2026",
        "headline": "NFL Week 9 MNF: Bills smother Vikings 23-6 behind James Cook and three turnovers",
        "whyCareScore": 9.6,
        "whyCareReason": "Buffalo forces three Carson Wentz turnovers, controls the clock for 42:32, and rides James Cook's 107 rushing yards to improve to 7-1.",
        "teaser": "FINAL: Bills 23, Vikings 6. Cook 31 car, 107 yds, 5-yd TD; Allen 21-31, 234 yds, TD pass to Keleki Latu. Buffalo moves to 7-1; Minnesota falls to 6-2.",
        "story": "The Buffalo Bills defeated the Minnesota Vikings 23-6 on Monday, 9 November, at U.S. Bank Stadium in Minneapolis on ESPN Monday Night Football, improving to 7-1 and matching their best eight-game start since 1993. Running back James Cook powered a physical ground game with 31 carries for 107 yards, sealing the win with a five-yard rushing touchdown during a 15-play, 8:32 fourth-quarter march. Quarterback Josh Allen completed 21 of 31 passes for 234 yards with an interception and a late first-half touchdown pass to tight end Keleki Latu, absorbing four sacks from Minnesota's pass rush. Starting for an injured Kyler Murray (hamstring), Carson Wentz struggled against Buffalo's defense, going 8 of 25 for 81 yards with two interceptions and a lost fumble before Max Brosmer replaced him late (6 of 7 for 58 yards). Buffalo held a commanding 42:32 to 17:28 advantage in time of possession and held the Vikings to 0-for-7 on third down. Tyler Bass kicked three field goals, including a 52-yarder, extending his franchise-record streak to 24 consecutive makes, while Will Reichard converted early field goals for Minnesota (6-2). Sunday in Madrid featured Joe Burrow throwing for 271 yards and accounting for four touchdowns as the Bengals beat the Falcons 34-17 at Santiago Bernabeu Stadium.",
        "stakes": "Buffalo matches its best eight-game start since 1993 at 7-1 atop the AFC East. Minnesota falls to 6-2 with its second straight defeat while waiting on Kyler Murray's hamstring recovery.",
        "rivalryAngle": "Ball-control supremacy meets stalled offense: Buffalo doubled Minnesota's possession time and capitalized on three takeaways.",
        "funFacts": [
            "Buffalo dominated time of possession 42:32 to 17:28 and kept Minnesota 0-for-7 on third down.",
            "Tyler Bass has converted 24 consecutive field goals, breaking a franchise record.",
            "Sunday in Madrid: Joe Burrow threw three touchdown passes and ran for another in Cincinnati's 34-17 win."
        ],
        "keyPlayers": [
            {"name": "James Cook", "team": "Buffalo Bills", "hook": "31 carries, 107 yards and a 5-yard 4Q touchdown on a 15-play drive."},
            {"name": "Josh Allen", "team": "Buffalo Bills", "hook": "21 of 31 for 234 yards and a 25-yard touchdown pass to Keleki Latu."},
            {"name": "Carson Wentz", "team": "Minnesota Vikings", "hook": "8 of 25 for 81 yards with 2 interceptions and a lost fumble before being benched."}
        ],
        "headToHead": "Monday 9 November 2026. U.S. Bank Stadium, Minneapolis. Final: Bills 23, Vikings 6.",
        "tags": ["football", "nfl", "bills", "vikings", "mnf", "week9", "josh-allen", "james-cook", "carson-wentz"],
        "home": "Minnesota Vikings",
        "away": "Buffalo Bills",
        "homeCode": "USA",
        "awayCode": "USA",
        "homeFlag": "us",
        "awayFlag": "us",
        "group": "NFL Week 9",
        "matchday": 9,
        "date": "2026-11-09",
        "time": "20:15",
        "venue": "U.S. Bank Stadium",
        "city": "Minneapolis",
        "status": "FINISHED",
        "homeScore": 6,
        "awayScore": 23,
        "marquee": True,
        "liveMinute": None,
        "image": IMG["nfl"],
        "decidedBy": "points",
        "homePen": None,
        "awayPen": None,
        "sport": "football",
        "competition": "nfl-2026",
        "format": "team-match",
        "season": "2026",
        "roundLabel": "Week 9 MNF",
        "resultSummary": "FINAL: Bills 23, Vikings 6. Cook 107 yds, 1 TD; Allen 234 yds, 1 TD to Latu; Wentz 8-25, 2 INTs. BUF 7-1, MIN 6-2.",
        "leaderboard": [],
        "tennisSets": [],
        "sources": [
            {"name": "NFL.com: Bills vs Vikings Week 9 game center", "url": "https://www.nfl.com/games/bills-at-vikings-2026-reg-9"},
            {"name": "CBS Sports: Bills shut down Vikings 23-6 on Monday Night Football", "url": "https://www.cbssports.com/nfl/news/bills-vs-vikings-score-mnf-2026/"},
            {"name": "Buffalo Bills: Week 9 postgame notes in Minneapolis", "url": "https://www.buffalobills.com/news/bills-vikings-mnf-recap-2026"}
        ]
    }
    dump(os.path.join(MATCHES, "bills-at-vikings-mnf-week9-2026.json"), bills_fix)

    sp_fix = {
        "slug": "sao-paulo-gp-interlagos-2026",
        "headline": "Sao Paulo GP: Lando Norris wins wet Interlagos race as Mercedes clinches Constructors title",
        "whyCareScore": 9.9,
        "whyCareReason": "Norris controls slippery Interlagos conditions from pole by 14.602s; Verstappen charges from 21st to 2nd; Russell (4th) and Antonelli (5th) seal the 2026 Constructors Championship for Mercedes.",
        "teaser": "RACE FINAL: Norris P1 (1:35:23.504); Verstappen P2 (+14.602s from P21); Hadjar P3 (+24.485s); Russell P4; Antonelli P5. Mercedes clinches Constructors title on 652 pts.",
        "story": "Lando Norris commanded wet conditions to win the Grande Premio de Sao Paulo on Sunday, 8 November, at Autodromo Jose Carlos Pace in 1:35:23.504 over 71 laps, securing his third Grand Prix victory of 2026 from pole position. Behind him, Max Verstappen staged a remarkable recovery drive from 21st on the grid to take second place (+14.602s), followed by Red Bull teammate Isack Hadjar in third (+24.485s). George Russell placed fourth (+33.991s) and newly crowned Drivers Champion Kimi Antonelli survived two spins in the rain to take fifth (+41.017s), pushing Mercedes to 652 points and mathematically sealing the 2026 Constructors Championship over Ferrari (510 points) with two races left. Oscar Piastri finished sixth (+56.475s), Liam Lawson seventh, Charles Leclerc eighth after a five-second collision penalty, Lewis Hamilton ninth in his 400th Grand Prix start, and Nico Hulkenberg tenth for Audi.",
        "stakes": "Mercedes seals the 2026 Constructors Championship at 652 points, while just 33 points separate second-placed Verstappen (279) from sixth-placed Norris (246) entering Las Vegas.",
        "rivalryAngle": "Norris controlled clean air in pouring spray while Verstappen carved past 19 cars from P21 on the Interlagos grid.",
        "funFacts": [
            "Max Verstappen charged from 21st on the starting grid to second place (+14.602s).",
            "Lewis Hamilton made his 400th career Formula 1 Grand Prix start and finished ninth.",
            "Mercedes (652) leads Ferrari (510), Red Bull (415) and McLaren (398) entering Las Vegas."
        ],
        "keyPlayers": [
            {"name": "Lando Norris", "team": "McLaren", "hook": "Won from pole in 1:35:23.504 for his third victory of 2026; now 246 pts."},
            {"name": "Max Verstappen", "team": "Red Bull", "hook": "Charged from 21st to 2nd (+14.602s) to hold second overall on 279 pts."},
            {"name": "Kimi Antonelli", "team": "Mercedes", "hook": "Recovered from two spins for P5; helps clinch Mercedes Constructors crown."}
        ],
        "headToHead": "Sunday 8 November 2026. Interlagos, Sao Paulo. Podium: Norris P1, Verstappen P2, Hadjar P3.",
        "tags": ["f1", "formula-1", "sao-paulo-gp", "interlagos", "norris", "verstappen", "mercedes", "constructors"],
        "home": "Lando Norris",
        "away": "Max Verstappen",
        "homeCode": "ENG",
        "awayCode": "NED",
        "homeFlag": "gb-eng",
        "awayFlag": "nl",
        "group": "Formula 1",
        "matchday": 21,
        "date": "2026-11-08",
        "time": "14:00",
        "venue": "Autodromo Jose Carlos Pace",
        "city": "Sao Paulo",
        "status": "FINISHED",
        "homeScore": "P1",
        "awayScore": "P2",
        "marquee": True,
        "liveMinute": None,
        "image": IMG["f1"],
        "decidedBy": "time",
        "homePen": None,
        "awayPen": None,
        "sport": "f1",
        "competition": "f1-2026",
        "format": "race",
        "season": "2026",
        "roundLabel": "Race Final",
        "resultSummary": "RACE: Norris P1 (1:35:23.504); Verstappen P2 (+14.602s); Hadjar P3 (+24.485s). Mercedes Champions (652 pts).",
        "leaderboard": [
            {"pos": "1", "name": "Lando Norris (McLaren)", "score": "1:35:23.504", "note": "Winner from pole"},
            {"pos": "2", "name": "Max Verstappen (Red Bull)", "score": "+14.602s", "note": "Started 21st"},
            {"pos": "3", "name": "Isack Hadjar (Red Bull)", "score": "+24.485s", "note": "Podium"},
            {"pos": "4", "name": "George Russell (Mercedes)", "score": "+33.991s", "note": "Constructors Champions"},
            {"pos": "5", "name": "Kimi Antonelli (Mercedes)", "score": "+41.017s", "note": "Drivers Champion (390 pts)"},
            {"pos": "6", "name": "Oscar Piastri (McLaren)", "score": "+56.475s", "note": "P6"}
        ],
        "tennisSets": [],
        "sources": [
            {"name": "Formula1.com: 2026 Sao Paulo Grand Prix race report and standings", "url": "https://www.formula1.com/en/racing/2026/brazil"},
            {"name": "FIA Formula 1 World Championship standings after Sao Paulo", "url": "https://www.fia.com/events/fia-formula-one-world-championship/season-2026/sao-paulo-grand-prix"}
        ]
    }
    dump(os.path.join(MATCHES, "sao-paulo-gp-interlagos-2026.json"), sp_fix)

    wwt_fix = {
        "slug": "wwt-championship-diamante-cabo-2026",
        "headline": "WWT Championship: 19-year-old Blades Brown rallies from 7 back to beat Ben James in playoff",
        "whyCareScore": 9.5,
        "whyCareReason": "Brown closes with a Sunday 63 to reach 23-under 265 and wins on the second playoff hole at El Cardonal, becoming the youngest PGA Tour winner in 95 years.",
        "teaser": "FINAL: Blades Brown 265 (-23, 66-68-68-63) def. Ben James 265 (-23, 65-64-66-70) on 2nd playoff hole. Michael Kim 3rd (-22, 266), Kensei Hirata 4th (-21, 267).",
        "story": "Nineteen-year-old Blades Brown produced an unforgettable comeback to win the World Wide Technology Championship on Sunday, 8 November, at El Cardonal at Diamante in Los Cabos. Starting the final round seven strokes behind Ben James, Brown surged with a bogey-free final-round 63 to sign for a 72-hole total of 23-under 265 (66-68-68-63). James eagled the 72nd hole to shoot 70 and tie Brown at 265 (-23, 65-64-66-70). Returning to the par-5 18th in sudden death, Brown secured victory on the second playoff hole to become the youngest PGA Tour champion in 95 years at 19 years, 5 months and 18 days old. Michael Kim finished solo third one shot back at 22-under 266, Kensei Hirata took fourth at 21-under 267, Peter Malnati tied for 18th at 16-under 272 and Zac Blair finished tied for 25th at 14-under 274.",
        "stakes": "At 19 years, 5 months and 18 days, Brown breaks nearly a century of PGA Tour youth records and locks up full Tour status through 2028.",
        "rivalryAngle": "A seven-shot final-day chase settled only after James's dramatic 72nd-hole eagle forced two extra trips down the 18th.",
        "funFacts": [
            "At 19 years, 5 months and 18 days, Blades Brown is the youngest PGA Tour winner in 95 years.",
            "Brown carded rounds of 66-68-68-63 for 265 (-23), overcoming a seven-stroke deficit on Sunday.",
            "Ben James eagled the 72nd hole to reach 265 (-23) before falling on the second playoff hole."
        ],
        "keyPlayers": [
            {"name": "Blades Brown", "team": "United States", "hook": "Sunday 63 (-23, 265 total); wins on second playoff hole from seven behind."},
            {"name": "Ben James", "team": "United States", "hook": "65-64-66-70 (265, -23); eagled the 72nd hole to force sudden death."},
            {"name": "Michael Kim", "team": "United States", "hook": "Finished solo third at 22-under 266, one shot outside the playoff."}
        ],
        "headToHead": "Sunday 8 November 2026. El Cardonal at Diamante, Los Cabos. Final: Blades Brown (-23) def. Ben James (-23) on 2nd playoff hole.",
        "tags": ["golf", "pga-tour", "wwt-championship", "los-cabos", "el-cardonal", "diamante", "blades-brown", "ben-james"],
        "home": "Blades Brown",
        "away": "Ben James",
        "homeCode": "USA",
        "awayCode": "USA",
        "homeFlag": "us",
        "awayFlag": "us",
        "group": "PGA Tour",
        "matchday": 7,
        "date": "2026-11-08",
        "time": "08:00",
        "venue": "El Cardonal at Diamante",
        "city": "Los Cabos",
        "status": "FINISHED",
        "homeScore": "-23",
        "awayScore": "-23",
        "marquee": False,
        "liveMinute": None,
        "image": IMG["golf"],
        "decidedBy": "playoff",
        "homePen": None,
        "awayPen": None,
        "sport": "golf",
        "competition": "pga-tour-2026",
        "format": "leaderboard",
        "season": "2026",
        "roundLabel": "Final Round",
        "resultSummary": "FINAL: Blades Brown (-23, 265) def. Ben James (-23, 265) on 2nd playoff hole. Kim -22, Hirata -21.",
        "leaderboard": [
            {"pos": "1", "name": "Blades Brown", "score": "-23 (66-68-68-63)", "note": "Won on 2nd playoff hole"},
            {"pos": "2", "name": "Ben James", "score": "-23 (65-64-66-70)", "note": "Eagle on 72nd hole; runner-up"},
            {"pos": "3", "name": "Michael Kim", "score": "-22 (266)", "note": "Solo 3rd"},
            {"pos": "4", "name": "Kensei Hirata", "score": "-21 (267)", "note": "Solo 4th"},
            {"pos": "T18", "name": "Peter Malnati", "score": "-16 (272)", "note": "T18"},
            {"pos": "T25", "name": "Zac Blair", "score": "-14 (274)", "note": "T25"}
        ],
        "tennisSets": [],
        "sources": [
            {"name": "PGA Tour: World Wide Technology Championship final results", "url": "https://www.pgatour.com/tournaments/2026/world-wide-technology-championship/R2026457"},
            {"name": "Golf Digest / AP: Blades Brown youngest PGA Tour winner in 95 years", "url": "https://apnews.com/article/golf-wwt-championship-blades-brown-ben-james-2026"}
        ]
    }
    dump(os.path.join(MATCHES, "wwt-championship-diamante-cabo-2026.json"), wwt_fix)

    # =========================================================================
    # PART 2: 8 Match JSONs for 11 November 2026 Desk
    # =========================================================================

    # 1. NBA Spotlight: Celtics 123, 76ers 101 (Tue Nov 10 Final)
    nba_celtics = {
        "slug": "nba-celtics-vs-76ers-george-36-2026",
        "headline": "NBA: Paul George drops 36 in Philly return as Celtics rout 76ers 123-101 to take 1st in East",
        "whyCareScore": 9.8,
        "whyCareReason": "Traded to Boston over the summer, Paul George drills six threes for 36 points back at Xfinity Mobile Arena while Jayson Tatum outduels former co-star Jaylen Brown in a 26-3 run.",
        "teaser": "FINAL: Celtics 123, 76ers 101. George 36 pts (6-11 3PT, 14 in 4Q); Tatum 21, Pritchard 18; Maxey 24, Brown 13. Boston moves to 9-2 atop the East ahead of 9-3 Philadelphia.",
        "story": "Paul George poured in 36 points in his first game back in Philadelphia on Tuesday, 10 November, leading the Boston Celtics to a 123-101 rout of the 76ers at Xfinity Mobile Arena. In 30:09 of action against the franchise that traded him in the summer, George shot 6 of 11 from three-point range, grabbed five rebounds and scored 14 fourth-quarter points to break open a deadlock. Tied 79-79 late in the third quarter, Boston exploded on a 26-3 run bridging the third and fourth frames. Jayson Tatum added 21 points after a frosty pregame sequence in which former Boston teammate Jaylen Brown appeared to bypass a tap-up before tipoff; Brown battled early foul trouble and finished with 13 points against his old club. Payton Pritchard scored 18 and Sam Hauser added 12 for Boston (9-2), which overtook Philadelphia (9-3) for first place in the Eastern Conference. Tyrese Maxey led the 76ers with 24 points. Elsewhere Tuesday, Portland defeated Oklahoma City 123-103 behind Damian Lillard's 25 points, Deni Avdija's 24 points and 8 assists, and a 38-21 third quarter against Shai Gilgeous-Alexander (26 pts, 8 reb) and Jared McCain (21 pts); the Knicks beat the Bucks 117-85, Suns topped the Clippers 133-110, Magic beat the Kings 107-100, and Heat edged the Jazz 115-109.",
        "stakes": "Boston claims solo possession of first place in the Eastern Conference at 9-2 ahead of tonight's road visit to Toronto, while Philadelphia slips to 9-3.",
        "rivalryAngle": "Double summer-trade homecoming: Paul George torched Philadelphia for 36 while Jaylen Brown struggled in foul trouble facing Jayson Tatum and Boston.",
        "funFacts": [
            "Game was tied 79-79 late in the third quarter before Boston unleashed a 26-3 surge.",
            "Paul George scored 14 of his 36 points in the fourth quarter (6 of 11 from three in 30:09).",
            "Other Nov 10 NBA finals: Trail Blazers 123-103 Thunder, Knicks 117-85 Bucks, Suns 133-110 Clippers."
        ],
        "keyPlayers": [
            {"name": "Paul George", "team": "Boston Celtics", "hook": "36 points, 6-11 3PT, 5 rebounds and 14 fourth-quarter points in his Philly return."},
            {"name": "Jayson Tatum", "team": "Boston Celtics", "hook": "Scored 21 points as Boston improved to 9-2 and took first in the East."},
            {"name": "Tyrese Maxey", "team": "Philadelphia 76ers", "hook": "Led Philadelphia with 24 points; Jaylen Brown was held to 13 points."}
        ],
        "headToHead": "Tuesday 10 November 2026. Xfinity Mobile Arena, Philadelphia. Final: Celtics 123, 76ers 101.",
        "tags": ["basketball", "nba", "celtics", "76ers", "paul-george", "jayson-tatum", "jaylen-brown"],
        "home": "Philadelphia 76ers",
        "away": "Boston Celtics",
        "homeCode": "USA",
        "awayCode": "USA",
        "homeFlag": "us",
        "awayFlag": "us",
        "group": "NBA Regular Season",
        "matchday": 11,
        "date": "2026-11-10",
        "time": "19:30",
        "venue": "Xfinity Mobile Arena",
        "city": "Philadelphia",
        "status": "FINISHED",
        "homeScore": 101,
        "awayScore": 123,
        "marquee": True,
        "liveMinute": None,
        "image": IMG["nba"],
        "decidedBy": "points",
        "homePen": None,
        "awayPen": None,
        "sport": "basketball",
        "competition": "nba-2026-27",
        "format": "team-match",
        "season": "2026-27",
        "roundLabel": "Eastern Showdown",
        "resultSummary": "FINAL: Celtics 123, 76ers 101. George 36 pts (6-11 3PT), Tatum 21, Pritchard 18; Maxey 24, Brown 13. BOS 9-2, PHI 9-3.",
        "leaderboard": [],
        "tennisSets": [],
        "sources": [
            {"name": "The Washington Post: Paul George gets revenge, Tatum and Brown collide in Boston's 123-101 win", "url": "https://www.washingtonpost.com/sports/2026/11/10/celtics-76ers-paul-george-jaylen-brown/"},
            {"name": "Northeast Times: Boston pulls away with 26-3 run to pass Sixers for East top spot", "url": "https://northeasttimes.com/sports/2026/11/10/celtics-123-76ers-101-paul-george-36/"}
        ]
    }
    dump(os.path.join(MATCHES, "nba-celtics-vs-76ers-george-36-2026.json"), nba_celtics)

    # 2. NBA Tonight Slate (Wed Nov 11 UPCOMING): Cavaliers at Knicks (ESPN)
    nba_knicks_tonight = {
        "slug": "nba-cavaliers-at-knicks-nov11-2026",
        "headline": "Tonight on ESPN: Knicks host Cavaliers at Madison Square Garden opening 10-game Wednesday slate",
        "whyCareScore": 8.7,
        "whyCareReason": "Fresh off a 117-85 demolition of Milwaukee on Tuesday, New York opens ESPN's Wednesday doubleheader at 7:00 p.m. ET before Warriors at Rockets (9:30 p.m. ET).",
        "teaser": "TONIGHT (Wed 11 Nov, 7:00 p.m. ET, ESPN): Cleveland Cavaliers at New York Knicks at MSG. Nightcap: Golden State at Houston (9:30 p.m. ET); Boston visits Toronto.",
        "story": "Eastern Conference intensity carries straight into Wednesday night, 11 November, as the New York Knicks host the Cleveland Cavaliers at Madison Square Garden at 7:00 p.m. ET in the opener of ESPN's national doubleheader. New York enters the back-to-back brimming with momentum after crushing the Milwaukee Bucks 117-85 on Tuesday night. The 9:30 p.m. ET ESPN nightcap sends the Golden State Warriors to Houston to face the Rockets, while newly minted East leader Boston (9-2) travels to Toronto after blowing out Philadelphia 123-101 and Oklahoma City meets Portland in an immediate rematch of Tuesday's 123-103 Trail Blazers upset.",
        "stakes": "Headline national test for New York on back-to-back nights, alongside Warriors-Rockets on ESPN and Boston opening its stay atop the Eastern Conference.",
        "rivalryAngle": "Garden primetime test on the front end of a loaded 10-game NBA Wednesday card.",
        "funFacts": [
            "New York tips off ESPN's Wednesday doubleheader at 7:00 p.m. ET before Warriors at Rockets at 9:30 p.m. ET.",
            "Ten NBA games fill Wednesday's card, including Boston at Toronto and Oklahoma City's rematch in Portland.",
            "The Knicks routed the Milwaukee Bucks 117-85 on Tuesday before returning to Madison Square Garden."
        ],
        "keyPlayers": [
            {"name": "New York Knicks", "team": "New York Knicks", "hook": "Home at Madison Square Garden on Wednesday night after beating Milwaukee 117-85."},
            {"name": "Boston Celtics", "team": "Boston Celtics", "hook": "Visit Toronto as East No. 1 (9-2) one night after beating Philadelphia 123-101."},
            {"name": "Golden State Warriors", "team": "Golden State Warriors", "hook": "Headliner in ESPN's 9:30 p.m. ET nightcap at the Houston Rockets."}
        ],
        "headToHead": "Wednesday 11 November 2026. Madison Square Garden, New York. Tipoff 7:00 p.m. ET on ESPN.",
        "tags": ["basketball", "nba", "knicks", "cavaliers", "espn", "msg"],
        "home": "New York Knicks",
        "away": "Cleveland Cavaliers",
        "homeCode": "USA",
        "awayCode": "USA",
        "homeFlag": "us",
        "awayFlag": "us",
        "group": "NBA Wednesday Slate",
        "matchday": 11,
        "date": "2026-11-11",
        "time": "19:00",
        "venue": "Madison Square Garden",
        "city": "New York",
        "status": "UPCOMING",
        "homeScore": None,
        "awayScore": None,
        "marquee": False,
        "liveMinute": None,
        "image": IMG["nba"],
        "decidedBy": None,
        "homePen": None,
        "awayPen": None,
        "sport": "basketball",
        "competition": "nba-2026-27",
        "format": "team-match",
        "season": "2026-27",
        "roundLabel": "Wed ESPN Doubleheader",
        "resultSummary": "TONIGHT: Cavaliers at Knicks (7:00 p.m. ET, ESPN), followed by Warriors at Rockets (9:30 p.m. ET, ESPN).",
        "leaderboard": [],
        "tennisSets": [],
        "sources": [
            {"name": "StatMuse: Cavaliers at Knicks Nov 11 2026 schedule and 7:00 PM ET tipoff", "url": "https://www.statmuse.com/nba/ask/cavaliers-at-knicks-november-11-2026"},
            {"name": "NBA Schedule: Golden State Warriors at Houston Rockets 9:30 PM ET ESPN", "url": "https://www.nba.com/schedule"}
        ]
    }
    dump(os.path.join(MATCHES, "nba-cavaliers-at-knicks-nov11-2026.json"), nba_knicks_tonight)

    # 3. Football Week 10 TNF (Thu Nov 12 UPCOMING): Commanders at Giants
    nfl_tnf = {
        "slug": "commanders-at-giants-tnf-week10-2026",
        "headline": "NFL Week 10 TNF: Giants (5-2-1) host Commanders in Vintage White Out after Week 5 tie",
        "whyCareScore": 9.4,
        "whyCareReason": "After playing to a dramatic 27-27 overtime deadlock in Week 5, NFC East leader New York (5-2-1) gets full practice participant J.J. McCarthy back under center on Thursday Night Football.",
        "teaser": "TOMORROW (Thu 12 Nov, 8:15 p.m. ET, Prime Video): Washington (2-5-1) at New York Giants (5-2-1, 2-0-1 NFC East). Week 5 ended 27-27 OT; McCarthy set to start.",
        "story": "Thursday Night Football opens NFL Week 10 under the MetLife Stadium lights on 12 November (8:15 p.m. ET, Prime Video) with an NFC East rematch carrying unfinished business from Week 5's 27-27 overtime tie. John Harbaugh's New York Giants lead the division at 5-2-1 (2-0-1 NFC East), fresh off a 19-11 road win in Philadelphia on Sunday that marked New York's first victory there since 2013. Quarterback J.J. McCarthy (hip) practiced in full this week and is expected to start alongside Malik Nabers, Cam Skattebo and Darnell Mooney as the Giants host a Vintage White Out crowd. Washington arrives at 2-5-1 still adjusting after Jayden Daniels's Week 2 left elbow injury, though wide receiver Treylon Burks is expected to play alongside tight ends Chig Okonkwo and John Bates.",
        "stakes": "A win moves New York to 6-2-1 and tightens its grip on the NFC East race, while 2-5-1 Washington needs an upset in East Rutherford to revive its season.",
        "rivalryAngle": "Unsettled score from Week 5's 27-27 OT draw: both rosters wear scars at quarterback entering Thursday night in East Rutherford.",
        "funFacts": [
            "Their Week 5 meeting finished tied 27-27 after overtime, leaving both records carrying an extra tie column.",
            "New York (5-2-1) beat Philadelphia 19-11 on Sunday for its first road win against the Eagles since 2013.",
            "The Giants are calling for a White Out at MetLife Stadium while wearing Vintage White uniforms."
        ],
        "keyPlayers": [
            {"name": "J.J. McCarthy", "team": "New York Giants", "hook": "Full practice participant (hip) expected to start for division-leading 5-2-1 New York."},
            {"name": "Malik Nabers", "team": "New York Giants", "hook": "Full participant and centerpiece of John Harbaugh's NFC East passing attack."},
            {"name": "Treylon Burks", "team": "Washington Commanders", "hook": "Expected to suit up as 2-5-1 Washington tries to split the season series."}
        ],
        "headToHead": "Thursday 12 November 2026, 8:15 p.m. ET. MetLife Stadium, East Rutherford. Prime Video. Week 5 meeting ended 27-27 OT.",
        "tags": ["football", "nfl", "tnf", "week10", "giants", "commanders", "jj-mccarthy", "nfc-east"],
        "home": "New York Giants",
        "away": "Washington Commanders",
        "homeCode": "USA",
        "awayCode": "USA",
        "homeFlag": "us",
        "awayFlag": "us",
        "group": "NFL Week 10",
        "matchday": 10,
        "date": "2026-11-12",
        "time": "20:15",
        "venue": "MetLife Stadium",
        "city": "East Rutherford",
        "status": "UPCOMING",
        "homeScore": None,
        "awayScore": None,
        "marquee": True,
        "liveMinute": None,
        "image": IMG["nfl"],
        "decidedBy": None,
        "homePen": None,
        "awayPen": None,
        "sport": "football",
        "competition": "nfl-2026",
        "format": "team-match",
        "season": "2026",
        "roundLabel": "Week 10 TNF",
        "resultSummary": "TOMORROW 8:15 p.m. ET (Prime Video): Commanders (2-5-1) at Giants (5-2-1). Rematch of Week 5 27-27 OT tie.",
        "leaderboard": [],
        "tennisSets": [],
        "sources": [
            {"name": "Giants.com: Week 10 Thursday Night Football White Out preview", "url": "https://www.giants.com/news/giants-commanders-week-10-thursday-night-football-2026"},
            {"name": "Pro-Football-Reference: Commanders at Giants Week 10 matchup", "url": "https://www.pro-football-reference.com/boxscores/202611120nyg.htm"},
            {"name": "Sports Illustrated: J.J. McCarthy injury status and TNF starter update", "url": "https://www.si.com/nfl/giants/news/jj-mccarthy-giants-commanders-week-10-tnf-2026"}
        ]
    }
    dump(os.path.join(MATCHES, "commanders-at-giants-tnf-week10-2026.json"), nfl_tnf)

    # 4. Soccer (1) UWCL MD4 Tuesday Final: PSG 1-2 Bayern Munich
    uwcl_psg_bayern = {
        "slug": "uwcl-psg-vs-bayern-munich-md4-2026",
        "headline": "UWCL MD4: Klara Buhl strikes as Bayern Munich edge PSG 2-1 at Parc des Princes",
        "whyCareScore": 9.3,
        "whyCareReason": "Klara Buhl doubles Bayern's lead in the 40th minute after Katarzyna Kiedrzynek's own goal before holding off Paulina Dudek's penalty on an eventful Matchday 4 opener.",
        "teaser": "FINAL: PSG 1-2 Bayern Munich (Kiedrzynek 29' og, Buhl 40'; Dudek 65' pen). Elsewhere Tuesday: Real Madrid 3-0 Paris FC, Hacken 0-0 Chelsea. Tonight: Juventus vs OL Lyonnes.",
        "story": "Bayern Munich claimed a vital 2-1 Women's Champions League Matchday 4 victory away to Paris Saint-Germain on Tuesday, 10 November, at the Parc des Princes. After a tight opening half-hour, Bayern capitalized in the 29th minute through a Katarzyna Kiedrzynek own goal before Klara Buhl finished smoothly in the 40th minute to give the visitors a two-goal cushion before halftime. Paris Saint-Germain fought back in the second half when Paulina Dudek converted from the penalty spot in the 65th minute, but Bayern protected its advantage cleanly through the closing stages. Elsewhere in Tuesday's UWCL action, Real Madrid swept Paris FC 3-0 at Estadio Alfredo Di Stefano with second-half goals from Arianna Caruso, Lineth Beerensteyn and Linda Caicedo, while Chelsea fired 28 shots in a frustrated 0-0 draw at BK Hacken. Action continues tonight (11 November) with OH Leuven vs HB Koge (17:45 UTC) and Juventus vs OL Lyonnes (20:00 UTC), while FC Barcelona hosts Arsenal at Spotify Camp Nou on Thursday (12 November, 18:45 CET) following its one-day shift due to general strikes in Spain.",
        "stakes": "Bayern pockets three priceless away points in Paris as Matchday 4 splits into tonight's clashes in Leuven and Biella and Thursday's blockbuster at Spotify Camp Nou.",
        "rivalryAngle": "Heavyweight league-phase collision in Paris decided by a 11-minute first-half swing from Bayern's attack.",
        "funFacts": [
            "Real Madrid hit three second-half goals (Caruso, Beerensteyn, Caicedo) to shut out Paris FC 3-0 on Tuesday.",
            "Chelsea outshot BK Hacken heavily (28 attempts) but settled for a 0-0 away draw in Gothenburg.",
            "Spain's general strike moved Barcelona vs Arsenal to Thursday 12 Nov (18:45 CET) at Spotify Camp Nou."
        ],
        "keyPlayers": [
            {"name": "Klara Buhl", "team": "Bayern Munich", "hook": "Struck Bayern's crucial second goal in the 40th minute in Paris."},
            {"name": "Paulina Dudek", "team": "Paris Saint-Germain", "hook": "Converted a 65th-minute penalty to halve the deficit for PSG."},
            {"name": "Linda Caicedo", "team": "Real Madrid", "hook": "Among the second-half scorers in Real Madrid's 3-0 win over Paris FC."}
        ],
        "headToHead": "Tuesday 10 November 2026. Parc des Princes, Paris. Final: PSG 1-2 Bayern Munich.",
        "tags": ["soccer", "uwcl", "psg", "bayern-munich", "champions-league", "real-madrid", "chelsea"],
        "home": "Paris Saint-Germain",
        "away": "Bayern Munich",
        "homeCode": None,
        "awayCode": None,
        "homeFlag": "",
        "awayFlag": "",
        "group": "UWCL League Phase",
        "matchday": 4,
        "date": "2026-11-10",
        "time": "21:00",
        "venue": "Parc des Princes",
        "city": "Paris",
        "status": "FINISHED",
        "homeScore": 1,
        "awayScore": 2,
        "marquee": True,
        "liveMinute": None,
        "image": IMG["soc"],
        "decidedBy": "goals",
        "homePen": None,
        "awayPen": None,
        "sport": "soccer",
        "competition": "uwcl-2026-27",
        "format": "team-match",
        "season": "2026-27",
        "roundLabel": "UWCL Matchday 4",
        "resultSummary": "FINAL: PSG 1-2 Bayern Munich (Kiedrzynek 29' og, Buhl 40'; Dudek 65' pen). Real Madrid 3-0 Paris FC; Hacken 0-0 Chelsea.",
        "leaderboard": [],
        "tennisSets": [],
        "sources": [
            {"name": "PSG.fr: Paris Saint-Germain 1-2 FC Bayern Munich match report", "url": "https://en.psg.fr/teams/womens-football/content/paris-saint-germain-bayern-munich-uwcl-2026"},
            {"name": "UEFA Women's Champions League Matchday 4 results", "url": "https://www.uefa.com/womenschampionsleague/fixtures-results/"}
        ]
    }
    dump(os.path.join(MATCHES, "uwcl-psg-vs-bayern-munich-md4-2026.json"), uwcl_psg_bayern)

    # 5. Soccer (2) Tonight UWCL (Wed Nov 11 UPCOMING): Juventus Women vs OL Lyonnes
    uwcl_juve_ol = {
        "slug": "uwcl-juventus-vs-ol-lyonnes-md4-2026",
        "headline": "Tonight in UWCL MD4: Juventus Women host OL Lyonnes in Biella before Camp Nou Thursday",
        "whyCareScore": 8.9,
        "whyCareReason": "After Bayern stunned PSG and Real Madrid dispatched Paris FC on Tuesday, Wednesday's Champions League spotlight lands on Biella at 21:00 CET before Barcelona host Arsenal tomorrow.",
        "teaser": "TONIGHT (Wed 11 Nov, 20:00 UTC / 21:00 CET): Juventus Women vs OL Lyonnes at Stadio Vittorio Pozzo-Lamarmora. Earlier: OH Leuven vs HB Koge (17:45 UTC). Thu: Barcelona vs Arsenal.",
        "story": "UEFA Women's Champions League Matchday 4 resumes tonight, Wednesday 11 November, with two European fixtures topped by Juventus Women hosting OL Lyonnes at Stadio Comunale Vittorio Pozzo-Lamarmora in Biella at 20:00 UTC (21:00 CET), preceded by OH Leuven vs HB Koge at 17:45 UTC. Both games follow Tuesday's away wins for Bayern Munich (2-1 at PSG) and Chelsea's frustrated 0-0 stalemate in Gothenburg. Elsewhere on the European calendar, Benfica vs Austria Wien was postponed to Thursday due to Storm Charles red weather alerts in Portugal, while FC Barcelona vs Arsenal opens Thursday night at 18:45 CET at Spotify Camp Nou alongside men's UEFA Nations League Matchday 5 ties including England vs Croatia, Spain vs Czechia and France vs Italy.",
        "stakes": "Key midweek league-phase test in Biella ahead of Thursday's postponed ties, Barcelona-Arsenal at Camp Nou and the return of men's international football.",
        "rivalryAngle": "Italian hosts seeking statement European points against French powerhouses OL Lyonnes under floodlights in Biella.",
        "funFacts": [
            "Wednesday UWCL schedule: OH Leuven vs HB Koge (17:45 UTC) followed by Juventus vs OL Lyonnes (20:00 UTC).",
            "Storm Charles weather alerts forced Benfica vs Austria Wien back to Thursday 12 November.",
            "Thursday features Barcelona vs Arsenal (18:45 CET) plus Nations League MD5: England-Croatia, Spain-Czechia, France-Italy."
        ],
        "keyPlayers": [
            {"name": "Juventus Women", "team": "Juventus Women", "hook": "Hosting OL Lyonnes in Biella in Wednesday's marquee 20:00 UTC fixture."},
            {"name": "OL Lyonnes", "team": "OL Lyonnes", "hook": "Visiting northern Italy on Matchday 4 after PSG fell to Bayern in Paris."},
            {"name": "Barcelona & Arsenal", "team": "Barcelona", "hook": "Rescheduled to Thursday 12 November (18:45 CET) at Spotify Camp Nou."}
        ],
        "headToHead": "Wednesday 11 November 2026, 20:00 UTC (21:00 CET). Stadio Comunale Vittorio Pozzo-Lamarmora, Biella.",
        "tags": ["soccer", "uwcl", "juventus", "ol-lyonnes", "barcelona", "arsenal", "nations-league"],
        "home": "Juventus Women",
        "away": "OL Lyonnes",
        "homeCode": None,
        "awayCode": None,
        "homeFlag": "",
        "awayFlag": "",
        "group": "UWCL League Phase",
        "matchday": 4,
        "date": "2026-11-11",
        "time": "20:00",
        "venue": "Stadio Comunale Vittorio Pozzo-Lamarmora",
        "city": "Biella",
        "status": "UPCOMING",
        "homeScore": None,
        "awayScore": None,
        "marquee": False,
        "liveMinute": None,
        "image": IMG["soc"],
        "decidedBy": None,
        "homePen": None,
        "awayPen": None,
        "sport": "soccer",
        "competition": "uwcl-2026-27",
        "format": "team-match",
        "season": "2026-27",
        "roundLabel": "UWCL MD4 Tonight",
        "resultSummary": "TONIGHT 20:00 UTC: Juventus Women vs OL Lyonnes in Biella; OH Leuven vs HB Koge at 17:45 UTC.",
        "leaderboard": [],
        "tennisSets": [],
        "sources": [
            {"name": "Sofascore: Juventus vs OL Lyonnes UWCL 11 Nov 2026 preview", "url": "https://www.sofascore.com/football/match/juventus-ol-lyonnes/uwcl-2026-11-11"},
            {"name": "Arsenal.com: UWCL fixture against Barcelona moved to Thursday 12 Nov", "url": "https://www.arsenal.com/news/barcelona-vs-arsenal-uwcl-rescheduled-november-12-2026"}
        ]
    }
    dump(os.path.join(MATCHES, "uwcl-juventus-vs-ol-lyonnes-md4-2026.json"), uwcl_juve_ol)

    # 6. Tennis: Stockholm Open & Turin Nitto ATP Finals Draw Preview
    atp_stockholm = {
        "slug": "atp-stockholm-open-2026-musetti-vs-samuel-r16",
        "headline": "ATP Stockholm Open: Musetti 6-1, 6-4 & Rune advance smoothly before Thursday's Turin Finals draw",
        "whyCareScore": 8.8,
        "whyCareReason": "Third seed Lorenzo Musetti cruises into the Stockholm quarter-finals while Holger Rune, Ugo Humbert and Alex Michelsen advance on the eve of the 2026 Nitto ATP Finals draw.",
        "teaser": "STOCKHOLM R16: Lorenzo Musetti def. Toby Samuel 6-1, 6-4; Holger Rune def. Zizou Bergs 6-3, 6-4; Ugo Humbert def. Vallejo 6-4, 6-3. Turin 8-man draw: Thu 12 Nov, 12:00 CET.",
        "story": "Indoor hard-court form held firm in Sweden on Tuesday, 10 November, as third-seeded Italian Lorenzo Musetti needed crisp efficiency to dispatch Toby Samuel 6-1, 6-4 in the Stockholm Open Round of 16 at Kungliga Tennishallen. Former champion Holger Rune opened his week cleanly with a 6-3, 6-4 win over eighth seed Zizou Bergs, while seventh seed Ugo Humbert overcame Adolfo Daniel Vallejo 6-4, 6-3 on Monday. Alex Michelsen (6) cruised past Juan Manuel Cerundolo 6-3, 6-2, Alejandro Tabilo edged Lorenzo Sonego 7-6, 2-6, 7-5, and Miomir Kecmanovic outlasted Arthur Rinderknech 7-6(4), 4-6, 6-4, while Thiago Agustin Tirante advanced past fifth seed Tomas Martin Etcheverry via walkover. Top seed Taylor Fritz faced Cameron Norrie in Wednesday action, with all eyes in men's tennis already turning to Turin: the official group draw for the Nitto ATP Finals (Nov 15-22 at Inalpi Arena) takes place Thursday, 12 November, at 12:00 p.m. CET featuring Alexander Zverev, Carlos Alcaraz, Ben Shelton, Daniil Medvedev, Flavio Cobolli, Arthur Fils, Frances Tiafoe and Rafael Jodar.",
        "stakes": "Last regular-week ATP 250 momentum in Stockholm directly precedes Thursday's Turin round-robin draw splitting the season's elite eight.",
        "rivalryAngle": "Clean indoor wins in Stockholm frame the final prelude before Zverev, Alcaraz, Shelton and Medvedev discover their Turin groups.",
        "funFacts": [
            "Musetti dropped just five games against Toby Samuel (6-1, 6-4) to reach the Stockholm quarter-finals.",
            "Other confirmed Stockholm winners: Holger Rune (6-3, 6-4), Ugo Humbert (6-4, 6-3) and Alex Michelsen (6-3, 6-2).",
            "Nitto ATP Finals 8 qualifiers for Thursday 12:00 CET draw: Zverev, Alcaraz, Shelton, Medvedev, Cobolli, Fils, Tiafoe, Jodar."
        ],
        "keyPlayers": [
            {"name": "Lorenzo Musetti", "team": "Italy", "hook": "No. 3 seed swept Toby Samuel 6-1, 6-4 on Tuesday at Kungliga Tennishallen."},
            {"name": "Holger Rune", "team": "Denmark", "hook": "Defeated eighth seed Zizou Bergs 6-3, 6-4 in Stockholm opening action."},
            {"name": "Carlos Alcaraz", "team": "Spain", "hook": "Fresh Paris Masters champion headlines Thursday's Nitto ATP Finals draw in Turin."}
        ],
        "headToHead": "Tuesday 10 November 2026. Kungliga Tennishallen, Stockholm. Result: Lorenzo Musetti def. Toby Samuel 6-1, 6-4.",
        "tags": ["tennis", "atp", "stockholm-open", "musetti", "rune", "humbert", "atp-finals", "turin"],
        "home": "Lorenzo Musetti",
        "away": "Toby Samuel",
        "homeCode": "ITA",
        "awayCode": "ENG",
        "homeFlag": "it",
        "awayFlag": "gb-eng",
        "group": "Bybit Stockholm Open",
        "matchday": 2,
        "date": "2026-11-10",
        "time": "18:00",
        "venue": "Kungliga Tennishallen",
        "city": "Stockholm",
        "status": "FINISHED",
        "homeScore": "2",
        "awayScore": "0",
        "marquee": False,
        "liveMinute": None,
        "image": IMG["ten"],
        "decidedBy": "sets",
        "homePen": None,
        "awayPen": None,
        "sport": "tennis",
        "competition": "atp-250-stockholm-2026",
        "format": "singles",
        "season": "2026",
        "roundLabel": "Stockholm R16",
        "resultSummary": "Musetti def. Samuel 6-1, 6-4; Rune def. Bergs 6-3, 6-4; Humbert def. Vallejo 6-4, 6-3. Turin draw Thu 12:00 CET.",
        "leaderboard": [],
        "tennisSets": [{"p1": "6", "p2": "1"}, {"p1": "6", "p2": "4"}],
        "sources": [
            {"name": "ATP Tour: Lorenzo Musetti vs Toby Samuel Stockholm Open 2026 result", "url": "https://www.atptour.com/en/scores/archive/stockholm/429/2026/results"},
            {"name": "ATP Tour: 2026 Nitto ATP Finals qualifiers and Turin draw time", "url": "https://www.nittoatpfinals.com/en/news/turin-2026-qualifiers-draw"}
        ]
    }
    dump(os.path.join(MATCHES, "atp-stockholm-open-2026-musetti-vs-samuel-r16.json"), atp_stockholm)

    # 7. Golf Tomorrow (Thu Nov 12 UPCOMING): DP World Tour Championship Dubai
    golf_dubai = {
        "slug": "dp-world-tour-championship-dubai-2026",
        "headline": "DP World Tour Championship: Rory McIlroy chases Race to Dubai leader Eugenio Chacarra in R1 pairing",
        "whyCareScore": 9.4,
        "whyCareReason": "No. 1 Eugenio Chacarra (4,243.79 pts) and Masters champion Rory McIlroy (3,709.86 pts) go head-to-head in Thursday's final group for 2,000 points and the Harry Vardon Trophy.",
        "teaser": "TOMORROW R1 (Thu 12 Nov, 12:40 GST / 08:40 GMT): Eugenio Chacarra (+533.93 pts lead) paired with Rory McIlroy at Jumeirah Golf Estates. $10M purse; $3M winner's share.",
        "story": "The DP World Tour season builds toward a direct two-man showdown on the Earth Course at Jumeirah Golf Estates in Dubai starting Thursday, 12 November ($10 million purse, $3 million winner's prize, 2,000 Race to Dubai points). Race to Dubai leader Eugenio Chacarra enters the finale on 4,243.79 points after three wins in 2026, holding a 533.93-point lead over second-placed Rory McIlroy (3,709.86 points). After finishing third at last week's Abu Dhabi Aldar Championship to overtake Patrick Reed into second, 2026 Masters champion McIlroy tees off alongside Chacarra in Thursday's anchor pairing at 12:40 p.m. local time (8:40 a.m. GMT / 3:40 a.m. ET). Victory in Dubai guarantees Chacarra the season crown outright, while McIlroy must finish inside the projected top four or better and hope results tilt his way to capture a record-equalling eighth Harry Vardon Trophy alongside Colin Montgomerie. Stateside, the PGA Tour opens the Austin Championship from 12-15 November ($6 million purse).",
        "stakes": "Two thousand Race to Dubai points on the line: Chacarra clinches with a Dubai win, while McIlroy fights for an eighth Harry Vardon Trophy to tie Colin Montgomerie.",
        "rivalryAngle": "Spaniard Chacarra's breakout three-win season meets Masters champion McIlroy in Thursday's headline anchor pairing in Dubai.",
        "funFacts": [
            "Eugenio Chacarra leads the Race to Dubai with 4,243.79 points, 533.93 clear of Rory McIlroy (3,709.86).",
            "McIlroy won the 2026 Masters and sits one Harry Vardon Trophy shy of Colin Montgomerie's all-time record of eight.",
            "Final Round 1 group: Eugenio Chacarra and Rory McIlroy tee off Thursday at 12:40 GST (08:40 GMT)."
        ],
        "keyPlayers": [
            {"name": "Eugenio Chacarra", "team": "Spain", "hook": "Race to Dubai No. 1 (4,243.79 pts, +533.93 lead) after three 2026 wins."},
            {"name": "Rory McIlroy", "team": "Northern Ireland", "hook": "No. 2 (3,709.86 pts); chasing record-tying 8th Harry Vardon Trophy after 3rd in Abu Dhabi."},
            {"name": "Patrick Reed", "team": "United States", "hook": "Overhauled by McIlroy into third following last week's Abu Dhabi Aldar Championship."}
        ],
        "headToHead": "Thursday 12 November - Sunday 15 November 2026. Earth Course, Jumeirah Golf Estates, Dubai. Final R1 tee time: 12:40 GST.",
        "tags": ["golf", "dp-world-tour", "dubai", "rory-mcilroy", "eugenio-chacarra", "race-to-dubai"],
        "home": "Eugenio Chacarra",
        "away": "Rory McIlroy",
        "homeCode": "ESP",
        "awayCode": "ENG",
        "homeFlag": "es",
        "awayFlag": "gb-eng",
        "group": "Race to Dubai Finale",
        "matchday": 1,
        "date": "2026-11-12",
        "time": "12:40",
        "venue": "Earth Course, Jumeirah Golf Estates",
        "city": "Dubai",
        "status": "UPCOMING",
        "homeScore": None,
        "awayScore": None,
        "marquee": True,
        "liveMinute": None,
        "image": IMG["golf"],
        "decidedBy": None,
        "homePen": None,
        "awayPen": None,
        "sport": "golf",
        "competition": "dp-world-tour-2026",
        "format": "leaderboard",
        "season": "2026",
        "roundLabel": "Round 1 Preview",
        "resultSummary": "TOMORROW 12:40 GST: Chacarra (4,243.79 pts) and McIlroy (3,709.86 pts) pair off in Dubai finale.",
        "leaderboard": [
            {"pos": "1", "name": "Eugenio Chacarra", "score": "4,243.79 pts", "note": "Race to Dubai leader (3 wins in 2026)"},
            {"pos": "2", "name": "Rory McIlroy", "score": "3,709.86 pts", "note": "-533.93 pts; chasing 8th Harry Vardon Trophy"},
            {"pos": "3", "name": "Patrick Reed", "score": "Top contender", "note": "Passed by McIlroy at Abu Dhabi Championship"}
        ],
        "tennisSets": [],
        "sources": [
            {"name": "European Tour: Eugenio Chacarra and Rory McIlroy paired together in Dubai Round 1", "url": "https://www.europeantour.com/dpworld-tour/news/articles/dp-world-tour-championship-2026-tee-times/"},
            {"name": "Golf Monthly: How Rory McIlroy can win an eighth Race to Dubai crown in Dubai", "url": "https://www.golfmonthly.com/news/rory-mcilroy-eugenio-chacarra-dp-world-tour-championship-2026"}
        ]
    }
    dump(os.path.join(MATCHES, "dp-world-tour-championship-dubai-2026.json"), golf_dubai)

    # 8. Formula 1 Upcoming Preview: Las Vegas Strip GP (Post-Sao Paulo Standings Squeeze)
    f1_vegas = {
        "slug": "las-vegas-gp-strip-2026",
        "headline": "F1 Standings Entering Las Vegas: 33 points split Verstappen to Norris in five-way P2 battle",
        "whyCareScore": 9.1,
        "whyCareReason": "With Kimi Antonelli (390) and Mercedes (652) crowned, only 33 points cover 2nd through 6th in Drivers and Ferrari (510), Red Bull (415) and McLaren (398) duel behind.",
        "teaser": "NEXT RACE (19-21 Nov, Las Vegas Strip): Antonelli 390 (Champion); Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246. Constructors: Mercedes 652, Ferrari 510, Red Bull 415, McLaren 398.",
        "story": "Both 2026 Formula 1 titles are wrapped up after Interlagos, yet the flight to Las Vegas (19-21 November, race Saturday at 8:00 p.m. PST, 50 laps) carries real championship heat. Kimi Antonelli sits uncatchable on 390 points and Mercedes holds 652 Constructors points, leaving just 33 points separating second through sixth in the Drivers standings: Max Verstappen leads the chase on 279 points after surging from 21st to second in Brazil, closely pursued by George Russell (262), Lewis Hamilton (261), Charles Leclerc (249) and Sao Paulo winner Lando Norris (246). In the Constructors table, Ferrari holds second on 510 points, while Red Bull (415) sits only 17 points ahead of McLaren (398) heading down the Las Vegas Strip.",
        "stakes": "Drivers P2 through P6 sit separated by 33 points with two Grands Prix left, while Red Bull (415) and McLaren (398) fight over third in the Constructors.",
        "rivalryAngle": "Interlagos winner Norris and recovery star Verstappen share the spotlight with teammates Russell, Hamilton and Leclerc under Nevada lights.",
        "funFacts": [
            "Just 33 points separate 2nd-placed Max Verstappen (279) from 6th-placed Lando Norris (246).",
            "George Russell (262) and Lewis Hamilton (261) enter Las Vegas separated by one single point.",
            "Red Bull (415) leads McLaren (398) by 17 points for third in the Constructors standings."
        ],
        "keyPlayers": [
            {"name": "Max Verstappen", "team": "Red Bull", "hook": "Holds P2 in the Drivers standings on 279 points after his P21-to-P2 drive in Brazil."},
            {"name": "Lando Norris", "team": "McLaren", "hook": "Up to 246 points after his third win of 2026 at Sao Paulo."},
            {"name": "Lewis Hamilton", "team": "Ferrari", "hook": "261 points, sitting one behind Russell (262) after his 400th start."}
        ],
        "headToHead": "19-21 November 2026. Las Vegas Strip Circuit, 50 laps (Race Sat 8:00 p.m. PST).",
        "tags": ["f1", "formula-1", "las-vegas-gp", "verstappen", "norris", "hamilton", "russell", "ferrari", "mclaren"],
        "home": "Max Verstappen",
        "away": "Lando Norris",
        "homeCode": "NED",
        "awayCode": "ENG",
        "homeFlag": "nl",
        "awayFlag": "gb-eng",
        "group": "Formula 1",
        "matchday": 22,
        "date": "2026-11-21",
        "time": "20:00",
        "venue": "Las Vegas Strip Circuit",
        "city": "Las Vegas",
        "status": "UPCOMING",
        "homeScore": None,
        "awayScore": None,
        "marquee": False,
        "liveMinute": None,
        "image": IMG["f1"],
        "decidedBy": None,
        "homePen": None,
        "awayPen": None,
        "sport": "f1",
        "competition": "f1-2026",
        "format": "race",
        "season": "2026",
        "roundLabel": "Las Vegas Preview",
        "resultSummary": "DRIVERS P2 RACE: Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246. Mercedes Champion (652); Ferrari 510, Red Bull 415, McLaren 398.",
        "leaderboard": [
            {"pos": "1", "name": "Kimi Antonelli (Mercedes)", "score": "390 pts", "note": "2026 Drivers Champion"},
            {"pos": "2", "name": "Max Verstappen (Red Bull)", "score": "279 pts", "note": "P2 after Sao Paulo P2"},
            {"pos": "3", "name": "George Russell (Mercedes)", "score": "262 pts", "note": "+1 over Hamilton"},
            {"pos": "4", "name": "Lewis Hamilton (Ferrari)", "score": "261 pts", "note": "400th GP completed"},
            {"pos": "5", "name": "Charles Leclerc (Ferrari)", "score": "249 pts", "note": "Ferrari 510 Constructors pts"},
            {"pos": "6", "name": "Lando Norris (McLaren)", "score": "246 pts", "note": "Sao Paulo winner (McLaren 398)"}
        ],
        "tennisSets": [],
        "sources": [
            {"name": "Formula1.com: 2026 Las Vegas Grand Prix event guide", "url": "https://www.formula1.com/en/racing/2026/las-vegas"},
            {"name": "Formula1.com: 2026 F1 Drivers and Constructors Championship standings", "url": "https://www.formula1.com/en/results/2026/drivers"}
        ]
    }
    dump(os.path.join(MATCHES, "las-vegas-gp-strip-2026.json"), f1_vegas)

    # =========================================================================
    # PART 3: 6 New "Why Care" Stories (pubDate: 2026-11-11, zero em-dashes)
    # =========================================================================

    stories_data = [
        {
            "slug": "nba-celtics-123-76ers-101-paul-george-revenge-return-2026",
            "title": "NBA: Paul George pours in 36 in Philly return as Celtics rout 76ers 123-101 for East No. 1",
            "subtitle": "Tied 79-79 late in the third, Boston unleashes a 26-3 burst while Jaylen Brown battles foul trouble against Jayson Tatum.",
            "category": "Match Report",
            "excerpt": "Paul George hit six three-pointers on his way to 36 points in Philadelphia as Boston beat the 76ers 123-101 to seize first place in the East at 9-2.",
            "image": IMG["nba"],
            "readingTime": 4,
            "pubDate": "2026-11-11",
            "sport": "basketball",
            "competition": "nba-2026-27",
            "relatedSlug": "nba-celtics-vs-76ers-george-36-2026",
            "sources": [
                {"name": "Washington Post: George returns with 36 as Celtics beat 76ers 123-101", "url": "https://www.washingtonpost.com/sports/2026/11/10/celtics-76ers-paul-george-jaylen-brown/"},
                {"name": "Northeast Times: Boston 26-3 run seals 9-2 East lead in Philadelphia", "url": "https://northeasttimes.com/sports/2026/11/10/celtics-123-76ers-101-paul-george-36/"}
            ],
            "content": """Returning to Xfinity Mobile Arena for the first time since his summer move, Paul George made Tuesday night unmistakably personal. The forward dropped 36 points in 30:09, shooting 6 of 11 from three-point range with 14 points in the fourth quarter, as the Boston Celtics rolled past the Philadelphia 76ers 123-101 on 10 November.

With the score locked 79-79 late in the third quarter, Boston tore the contest open with a decisive 26-3 burst crossing into the fourth. Jayson Tatum finished with 21 points after former partner Jaylen Brown appeared to ignore Tatum's pregame tap-up before tipoff; playing his first night against Boston since the trade, Brown fell into early foul trouble and finished with 13 points.

Payton Pritchard chipped in 18 points and Sam Hauser added 12 to lift Boston to 9-2 atop the Eastern Conference, dropping Philadelphia (led by Tyrese Maxey's 24) to 9-3. Elsewhere Tuesday, Portland stunned Oklahoma City 123-103 via a 38-21 third quarter led by Damian Lillard (25) and Deni Avdija (24 points, 8 assists), the Knicks blew past the Bucks 117-85, and tonight's Wednesday ESPN doubleheader showcases Cleveland at New York (7:00 p.m. ET) and Golden State at Houston (9:30 p.m. ET)."""
        },
        {
            "slug": "nfl-week10-tnf-commanders-at-giants-whiteout-rematch-2026",
            "title": "NFL Week 10 TNF: Giants (5-2-1) and J.J. McCarthy host Commanders in Vintage White Out rematch",
            "subtitle": "New York leads the NFC East ahead of Thursday night at MetLife Stadium after their Week 5 thriller finished tied 27-27.",
            "category": "Preview",
            "excerpt": "Five weeks after fighting to a 27-27 overtime draw, the 5-2-1 Giants welcome Washington to East Rutherford with J.J. McCarthy practicing in full.",
            "image": IMG["nfl"],
            "readingTime": 4,
            "pubDate": "2026-11-11",
            "sport": "football",
            "competition": "nfl-2026",
            "relatedSlug": "commanders-at-giants-tnf-week10-2026",
            "sources": [
                {"name": "Giants.com: Week 10 Thursday Night Football White Out preview", "url": "https://www.giants.com/news/giants-commanders-week-10-thursday-night-football-2026"},
                {"name": "Sports Illustrated: McCarthy full participant ahead of TNF", "url": "https://www.si.com/nfl/giants/news/jj-mccarthy-giants-commanders-week-10-tnf-2026"}
            ],
            "content": """First place in the NFC East steps under primetime floodlights on Thursday night, 12 November (8:15 p.m. ET, Prime Video), as the New York Giants host the Washington Commanders at MetLife Stadium with unfinished business left over from Week 5's 27-27 overtime tie.

John Harbaugh's Giants stand 5-2-1 (2-0-1 in the division) following Sunday's 19-11 upset at Philadelphia, New York's first victory on the Eagles' home field since 2013. Quarterback J.J. McCarthy (hip) logged full practice participation and is set to start alongside Malik Nabers, Cam Skattebo and Darnell Mooney as MetLife turns into a Vintage White Out.

Washington arrives at 2-5-1 leaning on expected starter Treylon Burks and tight ends Chig Okonkwo and John Bates after Jayden Daniels's Week 2 left elbow injury. Across the rest of the league, Buffalo arrives in Week 10 sitting at 7-1 after smothering the 6-2 Vikings 23-6 on Monday night behind James Cook's 107 rushing yards and three forced turnovers on Carson Wentz."""
        },
        {
            "slug": "uwcl-md4-bayern-beat-psg-real-madrid-cruises-2026",
            "title": "UWCL MD4: Bayern sink PSG 2-1 in Paris as Juventus face OL Lyonnes tonight before Camp Nou Thursday",
            "subtitle": "Klara Buhl's finish lifts Bayern at Parc des Princes while Real Madrid routs Paris FC 3-0 and Chelsea draw 0-0 at Hacken.",
            "category": "Match Report",
            "excerpt": "Bayern Munich claimed a 2-1 win at PSG on Tuesday night as Wednesday's Champions League spotlight moves to Biella ahead of Barcelona vs Arsenal tomorrow.",
            "image": IMG["soc"],
            "readingTime": 4,
            "pubDate": "2026-11-11",
            "sport": "soccer",
            "competition": "uwcl-2026-27",
            "relatedSlug": "uwcl-psg-vs-bayern-munich-md4-2026",
            "sources": [
                {"name": "PSG.fr: PSG 1-2 Bayern Munich UWCL Matchday 4 recap", "url": "https://en.psg.fr/teams/womens-football/content/paris-saint-germain-bayern-munich-uwcl-2026"},
                {"name": "Arsenal.com: UWCL Barcelona trip moved to Thursday 12 Nov", "url": "https://www.arsenal.com/news/barcelona-vs-arsenal-uwcl-rescheduled-november-12-2026"}
            ],
            "content": """Matchday 4 of the UEFA Women's Champions League opened with high drama in Paris on Tuesday night as Bayern Munich left the Parc des Princes with a 2-1 away victory over Paris Saint-Germain. A 29th-minute Katarzyna Kiedrzynek own goal opened the scoring before Klara Buhl struck cleanly in the 40th minute, leaving Bayern enough cushion to survive Paulina Dudek's 65th-minute penalty.

On the same Tuesday slate, Real Madrid defeated Paris FC 3-0 at Estadio Alfredo Di Stefano with second-half strikes by Arianna Caruso, Lineth Beerensteyn and Linda Caicedo, while Chelsea rattled off 28 shots without a breakthrough in a 0-0 draw away to BK Hacken.

Action continues tonight (11 November) with OH Leuven facing HB Koge at 17:45 UTC and Juventus Women welcoming OL Lyonnes to Biella at 20:00 UTC. Storm Charles alerts pushed Benfica vs Austria Wien to Thursday alongside FC Barcelona vs Arsenal (18:45 CET at Spotify Camp Nou) and men's UEFA Nations League openers including England vs Croatia, Spain vs Czechia and France vs Italy. Entering the domestic break, Arsenal leads the Premier League on 27 points, five ahead of Brighton (22) and six clear of Manchester City (21)."""
        },
        {
            "slug": "atp-stockholm-open-2026-musetti-rune-advance-turin-draw-next",
            "title": "ATP Desk: Musetti and Rune glide in Stockholm before Thursday's Nitto ATP Finals draw in Turin",
            "subtitle": "Lorenzo Musetti drops only five games against Toby Samuel while eight Turin qualifiers await group placement at 12:00 p.m. CET.",
            "category": "Desk",
            "excerpt": "Lorenzo Musetti beat Toby Samuel 6-1, 6-4 and Holger Rune downed Zizou Bergs in Stockholm as men's tennis counts down to Thursday's Turin Finals draw.",
            "image": IMG["ten"],
            "readingTime": 4,
            "pubDate": "2026-11-11",
            "sport": "tennis",
            "competition": "atp-250-stockholm-2026",
            "relatedSlug": "atp-stockholm-open-2026-musetti-vs-samuel-r16",
            "sources": [
                {"name": "ATP Tour: Stockholm Open 2026 results", "url": "https://www.atptour.com/en/scores/archive/stockholm/429/2026/results"},
                {"name": "Nitto ATP Finals: 2026 qualifiers and Turin group draw", "url": "https://www.nittoatpfinals.com/en/news/turin-2026-qualifiers-draw"}
            ],
            "content": """Third seed Lorenzo Musetti turned Tuesday's Round of 16 clash at Stockholm's Kungliga Tennishallen into swift business, dispatching Toby Samuel 6-1, 6-4 to advance into the quarter-finals. Former Stockholm champion Holger Rune matched that crisp indoor tempo, seeing off eighth seed Zizou Bergs 6-3, 6-4 on Tuesday after seventh seed Ugo Humbert beat Adolfo Daniel Vallejo 6-4, 6-3 on Monday.

Alex Michelsen (6-3, 6-2 vs Juan Manuel Cerundolo), Alejandro Tabilo (7-6, 2-6, 7-5 vs Lorenzo Sonego) and Miomir Kecmanovic (7-6(4), 4-6, 6-4 vs Arthur Rinderknech) also notched confirmed wins in the Swedish capital before Wednesday's Round of 16 slate featuring Taylor Fritz and Cameron Norrie.

All roads lead south to Italy tomorrow: on Thursday, 12 November, at 12:00 p.m. CET (6:00 a.m. ET), the 2026 Nitto ATP Finals draw divides the eight Turin qualifiers into two groups ahead of Sunday's opening matches (15-22 November). Alexander Zverev, fresh Paris champion Carlos Alcaraz, Ben Shelton, Daniil Medvedev, Flavio Cobolli, Arthur Fils, Frances Tiafoe and Rafael Jodar await their round-robin assignments."""
        },
        {
            "slug": "dp-world-tour-championship-2026-mcilroy-chacarra-dubai-preview",
            "title": "DP World Tour Championship: Rory McIlroy and leader Eugenio Chacarra paired for Dubai opener",
            "subtitle": "Separating by 533.93 Race to Dubai points, the top two tee off together Thursday at 12:40 GST for $3 million and the Harry Vardon Trophy.",
            "category": "Preview",
            "excerpt": "Eugenio Chacarra leads Rory McIlroy by 533.93 points entering Thursday's season finale at Jumeirah Golf Estates, where victory guarantees Chacarra the crown.",
            "image": IMG["golf"],
            "readingTime": 4,
            "pubDate": "2026-11-11",
            "sport": "golf",
            "competition": "dp-world-tour-2026",
            "relatedSlug": "dp-world-tour-championship-dubai-2026",
            "sources": [
                {"name": "European Tour: Chacarra and McIlroy headline Round 1 Dubai tee times", "url": "https://www.europeantour.com/dpworld-tour/news/articles/dp-world-tour-championship-2026-tee-times/"},
                {"name": "Golf Monthly: Race to Dubai permutations in Dubai", "url": "https://www.golfmonthly.com/news/rory-mcilroy-eugenio-chacarra-dp-world-tour-championship-2026"}
            ],
            "content": """The Race to Dubai comes down to its final 72 holes and a head-to-head Round 1 pairing on Thursday, 12 November, at the Earth Course at Jumeirah Golf Estates. Race leader Eugenio Chacarra (4,243.79 points) and second-placed Rory McIlroy (3,709.86 points) walk to the first tee together in the anchor group at 12:40 p.m. local time (8:40 a.m. GMT).

With 2,000 points awarded to the tournament champion out of a $10 million purse ($3 million first prize), the math is unforgiving. Chacarra has won three times in 2026 and owns a 533.93-point cushion, meaning another trophy on Sunday hands the Spaniard the Race to Dubai outright regardless of McIlroy's scorecard.

McIlroy climbed past Patrick Reed into second last week with a third-place finish at the Abu Dhabi Aldar Championship. Adding Dubai to his 2026 Masters triumph requires at least a projected top-four finish alongside help on the leaderboard, yet an eighth Harry Vardon Trophy would tie Colin Montgomerie's historic mark. On the PGA Tour side, 19-year-old Blades Brown enters the off-week in Cabo lore after his final-round 63 (-23, 265) toppled Ben James in sudden death before Thursday's Austin Championship opener."""
        },
        {
            "slug": "f1-sao-paulo-aftermath-verstappen-charge-las-vegas-preview-2026",
            "title": "F1 Standings Entering Las Vegas: Five drivers within 33 points behind Champion Kimi Antonelli",
            "subtitle": "Norris wins Interlagos and Mercedes clinch Constructors at 652, leaving Verstappen, Russell, Hamilton, Leclerc and Norris locked for P2.",
            "category": "Desk",
            "excerpt": "Mercedes sealed the 2026 Constructors Championship in Brazil, yet Max Verstappen (279) through Lando Norris (246) remain separated by 33 points before Las Vegas.",
            "image": IMG["f1"],
            "readingTime": 4,
            "pubDate": "2026-11-11",
            "sport": "f1",
            "competition": "f1-2026",
            "relatedSlug": "las-vegas-gp-strip-2026",
            "sources": [
                {"name": "Formula1.com: 2026 Sao Paulo Grand Prix and updated standings", "url": "https://www.formula1.com/en/results/2026/drivers"},
                {"name": "Formula1.com: 2026 Las Vegas Grand Prix preview", "url": "https://www.formula1.com/en/racing/2026/las-vegas"}
            ],
            "content": """Both world championships now bear names following a wet Sunday in Sao Paulo, where Lando Norris won from pole in 1:35:23.504 ahead of Max Verstappen (+14.602s from P21) and Isack Hadjar (+24.485s), while George Russell (4th) and world champion Kimi Antonelli (5th) carried Mercedes to 652 points and an insurmountable Constructors crown.

Yet Formula 1 heads toward next week's Las Vegas Grand Prix (19-21 November, 50-lap Strip race Saturday night at 8:00 p.m. PST) with a fierce scrap directly beneath Antonelli's 390-point lead. Just 33 points pack five stars vying for second overall: Verstappen leads that pack on 279, followed by Russell (262), Lewis Hamilton (261, fresh off his 400th Grand Prix start), Charles Leclerc (249) and Interlagos winner Norris (246).

Behind champion Mercedes in the Constructors table, Ferrari sits second on 510 points while Red Bull (415) holds a delicate 17-point buffer over fourth-placed McLaren (398), giving every point along the Las Vegas Strip real financial weight."""
        }
    ]

    for s in stories_data:
        check_dashes(s, f"story:{s['slug']}")
        p = os.path.join(STORIES, f"{s['slug']}.md")
        sources_yaml = "\n".join(
            [f'  - name: {json.dumps(src["name"], ensure_ascii=False)}\n    url: {json.dumps(src["url"], ensure_ascii=False)}' for src in s["sources"]]
        )
        frontmatter = f"""---
title: {json.dumps(s['title'], ensure_ascii=False)}
subtitle: {json.dumps(s['subtitle'], ensure_ascii=False)}
category: {json.dumps(s['category'], ensure_ascii=False)}
excerpt: {json.dumps(s['excerpt'], ensure_ascii=False)}
image: {json.dumps(s['image'], ensure_ascii=False)}
readingTime: {s['readingTime']}
pubDate: {s['pubDate']}
sport: {s['sport']}
competition: {s['competition']}
relatedSlug: {s['relatedSlug']}
sources:
{sources_yaml}
---

{s['content']}
"""
        with open(p, "w", encoding="utf-8") as f:
            f.write(frontmatter)
        print("wrote story", p)

    # =========================================================================
    # PART 4: Update frontend/src/data/sports.ts (SITE_TODAY = '2026-11-11')
    # =========================================================================

    sports_ts_content = """export const SITE_TODAY = '2026-11-11';

export const SPORT_SLUGS = ['soccer', 'tennis', 'golf', 'football', 'basketball', 'f1'] as const;
export type SportSlug = (typeof SPORT_SLUGS)[number];

export type SportSpan = 'hero' | 'side' | 'half';

export type SportMeta = {
  slug: SportSlug;
  label: string;
  short: string;
  href: string;
  tagline: string;
  liveNow: string;
  accent: string;
  hue: string;
  pulse: string;
  board: string;
  span: SportSpan;
};

/** Order is "what is on right now", not soccer first. */
export const SPORTS: SportMeta[] = [
  {
    slug: 'basketball',
    label: 'Basketball',
    short: 'Hoops',
    href: '/sport/basketball',
    tagline: 'NBA: Paul George pours in 36 points in Philly return as Celtics rout 76ers 123-101 to seize East No. 1.',
    liveNow: 'Final in Philly: Celtics 123, 76ers 101 (George 36 pts, 6-11 3PT; Tatum 21; Maxey 24, Brown 13). Tonight ESPN: CLE at NYK (7 p.m. ET), GSW at HOU (9:30 p.m. ET).',
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: 'NBA: PAUL GEORGE DROPS 36 IN PHILLY RETURN AS CELTICS TAKE EAST NO. 1 BEFORE TONIGHT ON ESPN',
    board: 'Open the floor',
    span: 'hero',
  },
  {
    slug: 'soccer',
    label: 'Soccer',
    short: 'Soccer',
    href: '/sport/soccer',
    tagline: 'UWCL MD4: Bayern win 2-1 at PSG and Real Madrid crush Paris FC 3-0 before Juventus host OL Lyonnes tonight.',
    liveNow: "Tuesday Finals: PSG 1-2 Bayern (Buhl 40'); Real Madrid 3-0 Paris FC; Hacken 0-0 Chelsea. Tonight: Juventus vs OL Lyonnes (20:00 UTC). Thu: Barcelona vs Arsenal.",
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: 'UWCL MD4: BAYERN EDGE PSG 2-1, JUVENTUS HOST LYON TONIGHT BEFORE BARCELONA VS ARSENAL',
    board: 'Open the pitch',
    span: 'side',
  },
  {
    slug: 'football',
    label: 'Football',
    short: 'NFL',
    href: '/sport/football',
    tagline: 'NFL Week 10 TNF Tomorrow: Giants (5-2-1) and J.J. McCarthy host Commanders after Week 5 27-27 tie.',
    liveNow: 'Thursday 8:15 p.m. ET (MetLife White Out): Commanders (2-5-1) at Giants (5-2-1). MNF Final: Bills (7-1) 23, Vikings (6-2) 6 (Cook 107 yds, 1 TD).',
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: 'NFL WEEK 10 TNF: GIANTS (5-2-1) HOST COMMANDERS TOMORROW AFTER WEEK 5 27-27 DEADLOCK',
    board: 'Open the field',
    span: 'half',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: 'DP World Tour Championship: Rory McIlroy and Race leader Eugenio Chacarra pair up Thursday in Dubai.',
    liveNow: 'Dubai R1 Tomorrow (12:40 GST): Chacarra (4,243.79 pts) leads McIlroy (3,709.86) by 533.93 pts for $3M prize. Cabo Final: Blades Brown (-23) wins playoff at 19.',
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: 'DUBAI FINALE: LEADER EUGENIO CHACARRA AND RORY MCILROY TEE OFF TOGETHER THURSDAY',
    board: 'Open the course',
    span: 'half',
  },
  {
    slug: 'tennis',
    label: 'Tennis',
    short: 'Tennis',
    href: '/sport/tennis',
    tagline: 'Stockholm Open: Musetti 6-1, 6-4 & Rune advance smoothly on eve of Thursday Nitto ATP Finals draw.',
    liveNow: 'Stockholm R16/R32: Musetti def. Samuel 6-1, 6-4; Rune def. Bergs 6-3, 6-4; Humbert def. Vallejo 6-4, 6-3. Turin 8-man draw: Thu 12:00 CET.',
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: 'ATP STOCKHOLM & TURIN DRAW: MUSETTI AND RUNE ADVANCE BEFORE THURSDAY NITTO ATP FINALS DRAW',
    board: 'Open the court',
    span: 'half',
  },
  {
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: 'F1 Standings Entering Las Vegas: 33 points cover Verstappen (279) through Norris (246) behind Antonelli.',
    liveNow: 'Drivers P2 Race: Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246 (Antonelli Champion 390; Mercedes 652). Next: Las Vegas (19-21 Nov).',
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: 'F1 ENTERING LAS VEGAS: FIVE STARS SEPARATED BY 33 POINTS IN BATTLE BEHIND ANTONELLI',
    board: 'Open the grid',
    span: 'half',
  },
];

export function sportBySlug(slug: string): SportMeta | undefined {
  return SPORTS.find((s) => s.slug === slug);
}

export function sportOf(entry: { sport?: string | null }): SportSlug {
  const s = (entry.sport || 'soccer').toLowerCase();
  return (SPORT_SLUGS as readonly string[]).includes(s) ? (s as SportSlug) : 'soccer';
}

export function isWorldCup(entry: { competition?: string | null }): boolean {
  const c = entry.competition || 'world-cup-2026';
  return c === 'world-cup-2026';
}

export function initials(name: string) {
  return name
    .split(/\s+/)
    .map((p) => p[0])
    .filter(Boolean)
    .slice(0, 2)
    .join('')
    .toUpperCase();
}
"""
    with open(os.path.join(ROOT, "frontend/src/data/sports.ts"), "w", encoding="utf-8") as f:
        f.write(sports_ts_content)
    print("wrote sports.ts")

    # =========================================================================
    # PART 5: Update frontend/src/data/desk.json accurately
    # =========================================================================

    desk_path = os.path.join(ROOT, "frontend/src/data/desk.json")
    with open(desk_path, "r", encoding="utf-8") as f:
        desk = json.load(f)

    desk["asOf"] = "2026-11-11"

    # Verified Premier League MW10 / Nov international break top 10
    desk["premierLeagueTable"] = [
        {"pos": 1, "team": "Arsenal", "p": 10, "w": 9, "d": 0, "l": 1, "gf": 15, "ga": 5, "gd": 10, "pts": 27},
        {"pos": 2, "team": "Brighton", "p": 10, "w": 7, "d": 1, "l": 2, "gf": 26, "ga": 7, "gd": 19, "pts": 22},
        {"pos": 3, "team": "Manchester City", "p": 10, "w": 7, "d": 0, "l": 3, "gf": 21, "ga": 13, "gd": 8, "pts": 21},
        {"pos": 4, "team": "Liverpool", "p": 10, "w": 5, "d": 3, "l": 2, "gf": 14, "ga": 10, "gd": 4, "pts": 18},
        {"pos": 5, "team": "Chelsea", "p": 10, "w": 5, "d": 1, "l": 4, "gf": 19, "ga": 16, "gd": 3, "pts": 16},
        {"pos": 6, "team": "Everton", "p": 10, "w": 4, "d": 4, "l": 2, "gf": 12, "ga": 10, "gd": 2, "pts": 16},
        {"pos": 7, "team": "Bournemouth", "p": 10, "w": 4, "d": 3, "l": 3, "gf": 16, "ga": 14, "gd": 2, "pts": 15},
        {"pos": 8, "team": "Brentford", "p": 10, "w": 3, "d": 5, "l": 2, "gf": 16, "ga": 11, "gd": 5, "pts": 14},
        {"pos": 9, "team": "Leeds", "p": 10, "w": 3, "d": 5, "l": 2, "gf": 10, "ga": 8, "gd": 2, "pts": 14},
        {"pos": 10, "team": "Aston Villa", "p": 10, "w": 3, "d": 4, "l": 3, "gf": 14, "ga": 17, "gd": -3, "pts": 13},
    ]

    # Verified F1 Constructors & Drivers WITH "team" property intact!
    desk["f1Constructors"] = [
        {"pos": 1, "name": "Mercedes (Champions)", "pts": 652},
        {"pos": 2, "name": "Ferrari", "pts": 510},
        {"pos": 3, "name": "Red Bull", "pts": 415},
        {"pos": 4, "name": "McLaren", "pts": 398},
    ]

    desk["f1Drivers"] = [
        {"pos": 1, "name": "Kimi Antonelli (Champion)", "team": "Mercedes", "pts": 390},
        {"pos": 2, "name": "Max Verstappen", "team": "Red Bull", "pts": 279},
        {"pos": 3, "name": "George Russell", "team": "Mercedes", "pts": 262},
        {"pos": 4, "name": "Lewis Hamilton", "team": "Ferrari", "pts": 261},
        {"pos": 5, "name": "Charles Leclerc", "team": "Ferrari", "pts": 249},
        {"pos": 6, "name": "Lando Norris", "team": "McLaren", "pts": 246},
    ]

    # Fix 2026-11-09 Bills vs Vikings MNF note & add 2026-11-12 Week 10 TNF preview
    nfl_notes = desk.get("nflWeek1", [])
    cleaned_nfl = []
    for x in nfl_notes:
        if x.get("date") == "2026-11-09" and "Vikings" in x.get("home", ""):
            cleaned_nfl.append({
                "date": "2026-11-09",
                "time": "8:15 p.m. ET",
                "home": "Minnesota Vikings",
                "away": "Buffalo Bills",
                "note": "FINAL: Bills 23, Vikings 6. Cook 31 car, 107 yds, 5-yd TD; Allen 21-31, 234 yds, TD to Latu; Wentz 8-25, 2 INTs. BUF 7-1, MIN 6-2."
            })
        elif x.get("date") == "2026-11-12" and "Giants" in x.get("home", ""):
            continue
        else:
            cleaned_nfl.append(x)

    if not any(x.get("date") == "2026-11-09" and "Vikings" in x.get("home", "") for x in cleaned_nfl):
        cleaned_nfl.append({
            "date": "2026-11-09",
            "time": "8:15 p.m. ET",
            "home": "Minnesota Vikings",
            "away": "Buffalo Bills",
            "note": "FINAL: Bills 23, Vikings 6. Cook 31 car, 107 yds, 5-yd TD; Allen 21-31, 234 yds, TD to Latu; Wentz 8-25, 2 INTs. BUF 7-1, MIN 6-2."
        })

    cleaned_nfl.append({
        "date": "2026-11-12",
        "time": "8:15 p.m. ET",
        "home": "New York Giants",
        "away": "Washington Commanders",
        "note": "WEEK 10 TNF (Prime Video, MetLife White Out): Commanders (2-5-1) at Giants (5-2-1). J.J. McCarthy full participant; rematch of Week 5 27-27 tie."
    })
    desk["nflWeek1"] = cleaned_nfl

    # Append Stockholm Open confirmed Nov 9-10 results to tennis board
    tennis_notes = [x for x in desk.get("usOpenQF", []) if not x.get("draw", "").startswith("Stockholm")]
    tennis_notes.extend([
        {"draw": "Stockholm R32", "p1": "Ugo Humbert", "p2": "Adolfo Daniel Vallejo", "status": "Humbert 6-4, 6-3"},
        {"draw": "Stockholm R32", "p1": "Holger Rune", "p2": "Zizou Bergs", "status": "Rune 6-3, 6-4"},
        {"draw": "Stockholm R16", "p1": "Lorenzo Musetti", "p2": "Toby Samuel", "status": "Musetti 6-1, 6-4"},
    ])
    desk["usOpenQF"] = tennis_notes

    dump(desk_path, desk)

    # =========================================================================
    # PART 6: Update AGENTS.md site clock line (line 14, zero em-dashes)
    # =========================================================================

    agents_path = os.path.join(ROOT, "AGENTS.md")
    with open(agents_path, "r", encoding="utf-8") as f:
        agents_lines = f.readlines()

    new_clock_line = (
        "*   **Site clock:** editorial today is `2026-11-11` in `frontend/src/data/sports.ts` (`SITE_TODAY`). "
        "Basketball: Paul George scores 36 (6 threes) in Philly return as Celtics rout 76ers 123-101 to take East No. 1 (9-2) ahead of Wednesday's ESPN doubleheader (CLE@NYK 7 p.m. ET, GSW@HOU 9:30 p.m. ET). "
        "Soccer: UWCL MD4 Bayern win 2-1 at PSG and Real Madrid 3-0 Paris FC; tonight Juventus vs OL Lyonnes (20:00 UTC); Thu Barcelona vs Arsenal; PL table Arsenal 27, Brighton 22, Man City 21. "
        "Football: Thu Week 10 TNF Commanders (2-5-1) at Giants (5-2-1, J.J. McCarthy starts); MNF correction Bills (7-1) beat Vikings (6-2) 23-6 (Cook 107 yds, Allen 234 yds to Latu, Wentz 2 INTs). "
        "Golf: DP World Tour Championship Dubai opens Thu (leader Eugenio Chacarra 4,243.79 pts paired with Rory McIlroy 3,709.86 at 12:40 GST); Cabo Blades Brown -23 (265) playoff winner. "
        "Tennis: Stockholm Open Musetti def. Samuel 6-1, 6-4 and Rune def. Bergs 6-3, 6-4 ahead of Thu 12:00 CET Nitto ATP Finals Turin draw. "
        "Formula 1: Entering Las Vegas (19-21 Nov), 33 pts separate Verstappen (279) through Norris (246) behind Champion Antonelli (390); Mercedes 652, Ferrari 510, Red Bull 415, McLaren 398.\n"
    )
    check_dashes(new_clock_line, "AGENTS.md:Site clock")

    for i, line in enumerate(agents_lines):
        if "*   **Site clock:**" in line:
            agents_lines[i] = new_clock_line
            break

    with open(agents_path, "w", encoding="utf-8") as f:
        f.writelines(agents_lines)
    print("updated AGENTS.md")

