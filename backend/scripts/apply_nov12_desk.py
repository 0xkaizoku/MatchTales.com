#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Apply verified 12 November 2026 desk: updated Nov 11 finals, Nov 12 matchups/draws, 6 stories, sports.ts, desk.json, AGENTS.md."""
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
    # PART 1: Convert Nov 11 upcoming JSONs to FINISHED + update Nov 12 matchups
    # =========================================================================

    # 1. UWCL MD4 Wed Nov 11 FINAL: Juventus Women 0-6 OL Lyonnes
    juve_lyon_final = {
        "slug": "uwcl-juventus-vs-ol-lyonnes-md4-2026",
        "headline": "UWCL MD4: OL Lyonnes crush Juventus Women 6-0 in Biella behind Katoto brace",
        "whyCareScore": 9.0,
        "whyCareReason": "Marie-Antoinette Katoto struck twice in four minutes before Melchie Dumornay, Lily Yohannes, Korbin Albert and Wendie Renard completed a 6-0 statement.",
        "teaser": "FINAL: Juventus Women 0-6 OL Lyonnes (Katoto 31', 35', Dumornay 40', Yohannes 80', Albert 85', Renard 90+1'). Also Wed: OH Leuven 1-1 HB Koge.",
        "story": "OL Lyonnes delivered one of the most emphatic away performances of the UEFA Women's Champions League league phase on Wednesday, 11 November, dismantling Juventus Women 6-0 at Stadio Comunale Vittorio Pozzo-Lamarmora in Biella. Marie-Antoinette Katoto broke open the contest with quickfire strikes in the 31st and 35th minutes before Melchie Dumornay added a third five minutes before halftime. Any hopes of an Italian response faded late as Lily Yohannes netted in the 80th minute, Korbin Albert scored in the 85th and captain Wendie Renard converted in stoppage time (90+1'). Elsewhere on Wednesday's Matchday 4 slate, OH Leuven and HB Koge shared a 1-1 draw.",
        "stakes": "OL Lyonnes strengthen their league-phase standing with six unanswered road goals while Juventus absorbs a bruising home setback ahead of tonight's Camp Nou clash.",
        "rivalryAngle": "French clinical finishing tore open a marquee European night in Biella, turning tight opening half-hour tension into a six-goal clinic.",
        "funFacts": [
            "Marie-Antoinette Katoto scored twice inside four minutes (31', 35') to spark OL Lyonnes' 6-0 rout.",
            "Melchie Dumornay (40'), Lily Yohannes (80'), Korbin Albert (85') and Wendie Renard (90+1') rounded out the scoring.",
            "Earlier on Wednesday in Matchday 4, OH Leuven and HB Koge finished locked 1-1."
        ],
        "keyPlayers": [
            {"name": "Marie-Antoinette Katoto", "team": "OL Lyonnes", "hook": "Struck in the 31st and 35th minutes to break Juventus open before halftime."},
            {"name": "Melchie Dumornay", "team": "OL Lyonnes", "hook": "Added the 40th-minute third goal to seal control before the interval."},
            {"name": "Wendie Renard", "team": "OL Lyonnes", "hook": "Added stoppage-time finishing touch (90+1') alongside Yohannes (80') and Albert (85')."}
        ],
        "headToHead": "Wednesday 11 November 2026. Stadio Comunale Vittorio Pozzo-Lamarmora, Biella. Final: Juventus Women 0-6 OL Lyonnes.",
        "tags": ["soccer", "uwcl", "juventus", "ol-lyonnes", "katoto", "dumornay", "renard"],
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
        "status": "FINISHED",
        "homeScore": 0,
        "awayScore": 6,
        "marquee": False,
        "liveMinute": None,
        "image": IMG["soc"],
        "decidedBy": "90min",
        "homePen": None,
        "awayPen": None,
        "sport": "soccer",
        "competition": "uwcl-2026-27",
        "format": "team-match",
        "season": "2026-27",
        "roundLabel": "UWCL MD4 Final",
        "resultSummary": "FINAL: Juventus Women 0-6 OL Lyonnes (Katoto 31', 35', Dumornay 40', Yohannes 80', Albert 85', Renard 90+1'). OH Leuven 1-1 HB Koge.",
        "leaderboard": [],
        "tennisSets": [],
        "sources": [
            {"name": "UEFA Women's Champions League: Juventus vs OL Lyonnes 0-6 match summary", "url": "https://www.uefa.com/womenschampionsleague/"},
            {"name": "ESPN Soccer: Katoto scores twice in OL Lyonnes 6-0 win over Juventus", "url": "https://www.espn.com/soccer/scoreboard"}
        ]
    }
    dump(os.path.join(MATCHES, "uwcl-juventus-vs-ol-lyonnes-md4-2026.json"), juve_lyon_final)

    # 2. UWCL MD4 Tonight Thu Nov 12 UPCOMING: FC Barcelona Femeni vs Arsenal Women
    barca_arsenal = {
        "slug": "uwcl-barcelona-vs-arsenal-md4-2026",
        "headline": "Tonight at Camp Nou: Barcelona host Arsenal in 2025 Lisbon final rematch",
        "whyCareScore": 9.7,
        "whyCareReason": "After Storm Charles forced a 24-hour move, unbeaten UWCL leader Barcelona plays holders Arsenal in Arsenal Women's first official match at Spotify Camp Nou.",
        "teaser": "TONIGHT (Thu 12 Nov, 18:45 CET / 17:45 UTC): FC Barcelona Femeni (9 pts) vs Arsenal Women (7 pts) at Spotify Camp Nou. Bonmati & Putellas vs Russo.",
        "story": "UEFA Women's Champions League Matchday 4 saves its grandest stage for Thursday night, 12 November (6:45 p.m. CET / 5:45 p.m. UTC / 12:45 p.m. ET), as FC Barcelona Femeni hosts Arsenal Women at Spotify Camp Nou. Rescheduled by 24 hours after Storm Charles weather warnings, the fixture marks Arsenal Women's first official match inside Camp Nou and a high-stakes rematch of the 2025 Lisbon final. Barcelona enters top of the table with three wins from three (5-2 vs Paris FC, 6-0 vs Roma, 8-0 at HB Koge) alongside a 7-0 domestic rout of Real Madrid, anchored by Ballon d'Or stars Aitana Bonmati and Alexia Putellas. Arsenal sits third on seven points and arrives on the back of a 2-1 Women's Super League win at Liverpool led by forward Alessia Russo.",
        "stakes": "Group supremacy on the line at Camp Nou: Barcelona chases 12 points from four matches while third-placed Arsenal aims to leapfrog the unbeaten hosts.",
        "rivalryAngle": "A Lisbon final rematch under Camp Nou floodlights pairing Barcelona's Ballon d'Or midfield with Alessia Russo and Arsenal's European pedigree.",
        "funFacts": [
            "Arsenal Women play their first official competitive fixture at Spotify Camp Nou tonight.",
            "Barcelona enters 3-from-3 in the UWCL (19 goals scored in wins over Paris FC, Roma and HB Koge).",
            "Rescheduled from Wednesday night following Storm Charles weather alerts in Spain and Portugal."
        ],
        "keyPlayers": [
            {"name": "Aitana Bonmati", "team": "FC Barcelona Femeni", "hook": "Drives Barcelona's unbeaten UWCL attack after a 7-0 domestic Clasico win."},
            {"name": "Alexia Putellas", "team": "FC Barcelona Femeni", "hook": "Anchors midfield as Barcelona hunts four wins from four in Europe."},
            {"name": "Alessia Russo", "team": "Arsenal Women", "hook": "Leads Arsenal's frontline at Camp Nou fresh off a 2-1 WSL win at Liverpool."}
        ],
        "headToHead": "Thursday 12 November 2026, 18:45 CET (17:45 UTC). Spotify Camp Nou, Barcelona. Repeat of the 2025 UWCL final.",
        "tags": ["soccer", "uwcl", "barcelona", "arsenal", "camp-nou", "bonmati", "putellas", "russo"],
        "home": "FC Barcelona Femeni",
        "away": "Arsenal Women",
        "homeCode": None,
        "awayCode": None,
        "homeFlag": "",
        "awayFlag": "",
        "group": "UWCL League Phase",
        "matchday": 4,
        "date": "2026-11-12",
        "time": "17:45",
        "venue": "Spotify Camp Nou",
        "city": "Barcelona",
        "status": "UPCOMING",
        "homeScore": None,
        "awayScore": None,
        "marquee": True,
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
        "resultSummary": "TONIGHT 18:45 CET: Barcelona (9 pts) host Arsenal (7 pts) at Spotify Camp Nou in 2025 final rematch.",
        "leaderboard": [],
        "tennisSets": [],
        "sources": [
            {"name": "FC Barcelona: UWCL Matchday 4 vs Arsenal at Spotify Camp Nou preview", "url": "https://www.fcbarcelona.com/en/football/womens-football"},
            {"name": "Arsenal.com: Rescheduled Camp Nou UWCL tie on Thursday 12 Nov", "url": "https://www.arsenal.com/news/barcelona-vs-arsenal-uwcl-rescheduled-november-12-2026"}
        ]
    }
    dump(os.path.join(MATCHES, "uwcl-barcelona-vs-arsenal-md4-2026.json"), barca_arsenal)

    # 3. Men's UEFA Nations League MD5 Tonight Thu Nov 12 UPCOMING: England vs Croatia
    eng_cro = {
        "slug": "england-vs-croatia-nations-league-2026",
        "headline": "UEFA Nations League MD5 Tonight: England host Croatia at Wembley alongside Italy vs France",
        "whyCareScore": 9.3,
        "whyCareReason": "England need only a point at Wembley to reach the Nations League quarterfinals, on a stacked Thursday night featuring Czechia vs Spain and Italy vs France.",
        "teaser": "TONIGHT (Thu 12 Nov, 19:45 UK / 20:45 CET): England vs Croatia at Wembley (Group A3). Also tonight: Italy vs France (San Siro, 20:45 CET), Czechia vs Spain (20:45 CET).",
        "story": "Men's international football steals the Thursday evening spotlight on 12 November across UEFA Nations League Matchday 5. In Group A3 at Wembley Stadium (7:45 p.m. UK / 8:45 p.m. CET), England host Croatia needing at least a draw to clinch a Nations League quarterfinal berth, while Spain already holds its quarterfinal spot ahead of its 8:45 p.m. CET visit to Czechia at Letna Stadium in Prague. In Group A1, heavyweights Italy and France collide at San Siro in Milan (8:45 p.m. CET) after Turkiye faces Belgium in Izmir (6:00 p.m. CET). Entering the international window, Arsenal still tops the Premier League table on 27 points, five ahead of Brighton (22) and six above Manchester City (21).",
        "stakes": "England seals a Nations League quarterfinal berth with a point or win at Wembley while Italy and France duel at San Siro in Group A1.",
        "rivalryAngle": "Wembley knockout math for England vs Croatia headlines alongside Group A1 giants Italy and France in Milan.",
        "funFacts": [
            "England needs a draw or victory at Wembley tonight to confirm a Nations League quarterfinal place.",
            "Men's Nations League Thursday slate: Turkiye vs Belgium (18:00 CET), England vs Croatia, Italy vs France, Czechia vs Spain (all 20:45 CET).",
            "Spain has already clinched a quarterfinal berth in Group A3 before visiting Prague."
        ],
        "keyPlayers": [
            {"name": "England", "team": "England", "hook": "Host Croatia at Wembley at 19:45 UK needing one point to advance."},
            {"name": "Croatia", "team": "Croatia", "hook": "Looking to disrupt Wembley celebrations on Matchday 5 in Group A3."},
            {"name": "Italy & France", "team": "Italy", "hook": "Lock horns at San Siro in Milan at 20:45 CET in Group A1."}
        ],
        "headToHead": "Thursday 12 November 2026, 19:45 GMT (20:45 CET). Wembley Stadium, London. UEFA Nations League Group A3 MD5.",
        "tags": ["soccer", "nations-league", "england", "croatia", "wembley", "italy", "france", "spain"],
        "home": "England",
        "away": "Croatia",
        "homeCode": "ENG",
        "awayCode": "CRO",
        "homeFlag": "gb-eng",
        "awayFlag": "hr",
        "group": "Nations League Group A3",
        "matchday": 5,
        "date": "2026-11-12",
        "time": "19:45",
        "venue": "Wembley Stadium",
        "city": "London",
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
        "competition": "nations-league-2026-27",
        "format": "team-match",
        "season": "2026-27",
        "roundLabel": "Nations League MD5",
        "resultSummary": "TONIGHT 19:45 UK: England vs Croatia (Wembley); also Italy vs France & Czechia vs Spain (20:45 CET).",
        "leaderboard": [],
        "tennisSets": [],
        "sources": [
            {"name": "UEFA.com: Nations League MD5 England vs Croatia & Italy vs France schedule", "url": "https://www.uefa.com/uefanationsleague/"},
            {"name": "BBC Sport: England Nations League Group A3 permutations at Wembley", "url": "https://www.bbc.com/sport/football"}
        ]
    }
    dump(os.path.join(MATCHES, "england-vs-croatia-nations-league-2026.json"), eng_cro)

    # 4. NBA Wed Nov 11 FINAL: Cavaliers 115, Knicks 107
    cavs_knicks_final = {
        "slug": "nba-cavaliers-at-knicks-nov11-2026",
        "headline": "NBA: James Harden drops 32 at MSG as Cavaliers top Knicks 115-107",
        "whyCareScore": 9.1,
        "whyCareReason": "James Harden scores 32 with five three-pointers and Donovan Mitchell adds 23 at Madison Square Garden, handing New York a home defeat after Tuesday's rout of Milwaukee.",
        "teaser": "FINAL: Cavaliers 115, Knicks 107. Harden 32 pts (5 threes), Mitchell 23; Brunson 27, Towns 21. Cleveland pulls away at Madison Square Garden.",
        "story": "James Harden poured in a game-high 32 points with five three-pointers on Wednesday night, 11 November, powering the Cleveland Cavaliers past the New York Knicks 115-107 on ESPN at Madison Square Garden. Donovan Mitchell added 23 points as Cleveland spoiled the second night of New York's back-to-back following Tuesday's 117-85 win over Milwaukee. Jalen Brunson led the Knicks with 27 points and Karl-Anthony Towns chipped in 21, but Cleveland's perimeter shot-making carried the decisive stretch in the fourth quarter.",
        "stakes": "Cleveland picks up a statement Eastern Conference road win at Madison Square Garden while halting New York's home momentum.",
        "rivalryAngle": "Veteran guard duel under MSG lights: Harden (32) and Mitchell (23) outgun Brunson (27) and Towns (21) on national television.",
        "funFacts": [
            "James Harden knocked down five three-pointers on his way to a game-high 32 points.",
            "Donovan Mitchell contributed 23 points alongside Harden for 55 combined Cleveland guard points.",
            "Jalen Brunson (27) and Karl-Anthony Towns (21) combined for 48 points in the Knicks defeat."
        ],
        "keyPlayers": [
            {"name": "James Harden", "team": "Cleveland Cavaliers", "hook": "Scored a game-high 32 points with five made three-pointers at MSG."},
            {"name": "Donovan Mitchell", "team": "Cleveland Cavaliers", "hook": "Backed up Harden with 23 points in Cleveland's 115-107 road victory."},
            {"name": "Jalen Brunson", "team": "New York Knicks", "hook": "Led New York with 27 points alongside Karl-Anthony Towns' 21."}
        ],
        "headToHead": "Wednesday 11 November 2026. Madison Square Garden, New York. Final: Cavaliers 115, Knicks 107.",
        "tags": ["basketball", "nba", "cavaliers", "knicks", "james-harden", "donovan-mitchell", "jalen-brunson"],
        "home": "New York Knicks",
        "away": "Cleveland Cavaliers",
        "homeCode": "USA",
        "awayCode": "USA",
        "homeFlag": "us",
        "awayFlag": "us",
        "group": "NBA Regular Season",
        "matchday": 12,
        "date": "2026-11-11",
        "time": "19:00",
        "venue": "Madison Square Garden",
        "city": "New York",
        "status": "FINISHED",
        "homeScore": 107,
        "awayScore": 115,
        "marquee": False,
        "liveMinute": None,
        "image": IMG["nba"],
        "decidedBy": "points",
        "homePen": None,
        "awayPen": None,
        "sport": "basketball",
        "competition": "nba-2026-27",
        "format": "team-match",
        "season": "2026-27",
        "roundLabel": "ESPN Recap",
        "resultSummary": "FINAL: Cavaliers 115, Knicks 107. Harden 32 pts (5 threes), Mitchell 23; Brunson 27, Towns 21.",
        "leaderboard": [],
        "tennisSets": [],
        "sources": [
            {"name": "ESPN: Cavaliers vs Knicks Nov 11 2026 box score", "url": "https://www.espn.com/nba/scoreboard"},
            {"name": "NBA.com: Harden 32 powers Cavaliers past Knicks at MSG", "url": "https://www.nba.com/games"}
        ]
    }
    dump(os.path.join(MATCHES, "nba-cavaliers-at-knicks-nov11-2026.json"), cavs_knicks_final)

    # 5. NBA Wed Nov 11 FINAL + Thu Nov 12 4-Game Card: Rockets 115, Warriors 108
    rockets_warriors = {
        "slug": "nba-rockets-vs-warriors-nov11-2026",
        "headline": "NBA: Rockets top Warriors 115-108 as Curry exits early; Celtics rally from 22 down in Toronto",
        "whyCareScore": 9.3,
        "whyCareReason": "Stephen Curry departs early in the first quarter with an injury (3 pts) as Houston's balanced attack beats Golden State, while Jayson Tatum's 24 rallies Boston past Toronto 98-93.",
        "teaser": "FINAL: Rockets 115, Warriors 108 (Sengun 19, Smith Jr. 14, Sheppard 13; Lendeborg 25, Curry injured 1Q). Also Wed: Celtics 98-93 Raptors (-22 comeback). Thu: 4 games.",
        "story": "The Houston Rockets closed ESPN's Wednesday nightcap on 11 November with a 115-108 home victory over a Golden State Warriors side shaken early when Stephen Curry left the game in the first quarter due to injury after scoring three points. Alperen Sengun paced Houston's balanced scoring with 19 points, Jabari Smith Jr. scored 14 and Reed Sheppard contributed 13 at Toyota Center. Yaxel Lendeborg led all Warriors scorers with 25 points alongside Brandin Podziemski (22), L.J. Cryer (13) and De'Anthony Melton (11) in defeat. Earlier in Toronto, East-leading Boston stormed back from a 22-point deficit behind Jayson Tatum's 24 points to defeat the Raptors 98-93. Tonight, Thursday 12 November, features a four-game NBA slate: Raptors at 76ers (7:00 p.m. ET), Pistons at Wizards (7:00 p.m. ET), Mavericks at Timberwolves (8:00 p.m. ET) and Hornets at Suns (9:00 p.m. ET).",
        "stakes": "Stephen Curry's injury watch looms over Golden State while Boston stays unbeaten on its road trip before tonight's four-game Thursday card.",
        "rivalryAngle": "Houston's young core outlasts Golden State's shorthanded surge after Curry's premature first-quarter departure.",
        "funFacts": [
            "Stephen Curry exited in the first quarter with an injury after scoring three points.",
            "Rockets balanced leaders: Alperen Sengun (19 pts), Jabari Smith Jr. (14) and Reed Sheppard (13); Warriors led by Yaxel Lendeborg (25) and Brandin Podziemski (22).",
            "Wednesday also saw Boston erase a 22-point deficit in Toronto behind Jayson Tatum (24) to win 98-93; Thursday hosts TOR@PHI, DET@WAS, DAL@MIN, CHA@PHX."
        ],
        "keyPlayers": [
            {"name": "Alperen Sengun", "team": "Houston Rockets", "hook": "Led Houston's balanced attack with 19 points alongside Jabari Smith Jr. (14) and Reed Sheppard (13)."},
            {"name": "Yaxel Lendeborg", "team": "Golden State Warriors", "hook": "Scored 25 points with Brandin Podziemski adding 22 after Stephen Curry exited in Q1."},
            {"name": "Jayson Tatum", "team": "Boston Celtics", "hook": "Scored 24 points as Boston rallied from 22 behind to beat Toronto 98-93."}
        ],
        "headToHead": "Wednesday 11 November 2026. Toyota Center, Houston. Final: Rockets 115, Warriors 108. Celtics 98, Raptors 93.",
        "tags": ["basketball", "nba", "rockets", "warriors", "stephen-curry", "sengun", "celtics", "tatum"],
        "home": "Houston Rockets",
        "away": "Golden State Warriors",
        "homeCode": "USA",
        "awayCode": "USA",
        "homeFlag": "us",
        "awayFlag": "us",
        "group": "NBA Regular Season",
        "matchday": 12,
        "date": "2026-11-11",
        "time": "21:30",
        "venue": "Toyota Center",
        "city": "Houston",
        "status": "FINISHED",
        "homeScore": 115,
        "awayScore": 108,
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
        "roundLabel": "ESPN Nightcap",
        "resultSummary": "FINAL: Rockets 115, Warriors 108 (Curry injured 1Q, Sengun 19); Celtics 98-93 Raptors (-22). Thu: 4 NBA games.",
        "leaderboard": [],
        "tennisSets": [],
        "sources": [
            {"name": "ESPN: Warriors vs Rockets Nov 11 2026 box score and Curry injury report", "url": "https://www.espn.com/nba/scoreboard"},
            {"name": "NBA.com: Celtics erase 22-point hole in Toronto; Nov 12 Thursday slate", "url": "https://www.nba.com/schedule"}
        ]
    }
    dump(os.path.join(MATCHES, "nba-rockets-vs-warriors-nov11-2026.json"), rockets_warriors)

    # 6. Football Week 10 TNF TONIGHT Thu Nov 12 UPCOMING: Commanders at Giants (final injury report)
    nfl_tnf_tonight = {
        "slug": "commanders-at-giants-tnf-week10-2026",
        "headline": "TONIGHT TNF Week 10: Giants (5-2-1) & McCarthy host Commanders & cleared Jayden Daniels in White Out",
        "whyCareScore": 9.6,
        "whyCareReason": "Both Week 5 27-27 OT rivals are led by cleared QBs tonight as J.J. McCarthy (no designation) meets full participant Jayden Daniels on Prime Video, while Washington misses center Lucas Patrick.",
        "teaser": "TONIGHT (Thu 12 Nov, 8:15 p.m. ET, Prime Video): Commanders (2-5-1) at Giants (5-2-1, Vintage White Out). Jayden Daniels & J.J. McCarthy cleared; C Lucas Patrick & TE Yankoff OUT.",
        "story": "NFL Week 10 opens tonight, Thursday 12 November (8:15 p.m. ET, Prime Video), under MetLife Stadium floodlights with an NFC East rematch loaded with fresh stakes from Week 5's 27-27 overtime deadlock. John Harbaugh's first-place New York Giants enter at 5-2-1 (2-0-1 NFC East) after Sunday's 19-11 upset win in Philadelphia, New York's first victory there since 2013, with quarterback J.J. McCarthy (hip), running back Cam Skattebo (hamstring), wideout Malik Nabers (knee), left tackle Andrew Thomas (groin) and tight end Theo Johnson (neck) all cleared with no game status designation (only LB Malik Harrison is questionable with a groin injury). Washington (2-5-1) also receives massive quarterback news for tonight's Vintage White Out: Jayden Daniels practiced fully with his left elbow and carries no injury designation, though center Lucas Patrick (concussion; Nick Allegretti starts) and tight end Colson Yankoff (knee) are officially OUT, and receiver Treylon Burks (foot) is expected to play despite missing short-week practices.",
        "stakes": "A victory pushes New York to 6-2-1 atop the NFC East; a healthy Jayden Daniels tries to reignite 2-5-1 Washington without starting center Lucas Patrick.",
        "rivalryAngle": "Rematch of Week 5's 27-27 tie features both young quarterbacks cleared for primetime at MetLife Stadium.",
        "funFacts": [
            "Final TNF injury report: Jayden Daniels (left elbow) and J.J. McCarthy (hip) both carry zero injury designation tonight.",
            "Commanders OUT: Center Lucas Patrick (concussion, Nick Allegretti starts) and TE Colson Yankoff (knee). Giants questionable: LB Malik Harrison (groin).",
            "Week 5 between these rivals ended 27-27 in overtime; MetLife Stadium stages a Vintage White Out tonight at 8:15 p.m. ET."
        ],
        "keyPlayers": [
            {"name": "J.J. McCarthy", "team": "New York Giants", "hook": "Cleared (no designation after hip) with Skattebo, Nabers and Andrew Thomas active for 5-2-1 New York."},
            {"name": "Jayden Daniels", "team": "Washington Commanders", "hook": "Full practice participant (left elbow) with zero designation entering tonight's White Out."},
            {"name": "Nick Allegretti", "team": "Washington Commanders", "hook": "Steps in at center tonight with Lucas Patrick ruled OUT (concussion)."}
        ],
        "headToHead": "TONIGHT Thursday 12 November 2026, 8:15 p.m. ET. MetLife Stadium, East Rutherford. Prime Video. Week 5 meeting ended 27-27 OT.",
        "tags": ["football", "nfl", "tnf", "week10", "giants", "commanders", "jj-mccarthy", "jayden-daniels", "nfc-east"],
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
        "roundLabel": "TNF Tonight",
        "resultSummary": "TONIGHT 8:15 p.m. ET (Prime Video): Commanders (2-5-1, Daniels cleared, C Patrick OUT) at Giants (5-2-1, McCarthy/Nabers/Skattebo active).",
        "leaderboard": [],
        "tennisSets": [],
        "sources": [
            {"name": "NFL.com: Commanders at Giants Week 10 Thursday Night Football injury report", "url": "https://www.nfl.com/games/commanders-at-giants-2026-reg-10"},
            {"name": "Giants.com: Week 10 TNF White Out preview & final designations", "url": "https://www.giants.com/news/giants-commanders-week-10-thursday-night-football-2026"}
        ]
    }
    dump(os.path.join(MATCHES, "commanders-at-giants-tnf-week10-2026.json"), nfl_tnf_tonight)

    # 7a. Tennis Today Thu Nov 12: Nitto ATP Finals Turin Official Draw + Group Assignments
    atp_turin_draw = {
        "slug": "atp-nitto-finals-2026-turin-draw",
        "headline": "Nitto ATP Finals Draw Set: Zverev heads McEnroe Group while Alcaraz leads Lendl Group in Turin",
        "whyCareScore": 9.3,
        "whyCareReason": "Thursday's official draw splits Alexander Zverev, Ben Shelton, Arthur Fils and Rafael Jodar into the John McEnroe Group, opposite Carlos Alcaraz, Daniil Medvedev, Flavio Cobolli and Frances Tiafoe.",
        "teaser": "TURIN GROUPS SET (15-22 Nov): McEnroe Group = Zverev (1), Shelton (3), Fils (6), Jodar (8). Lendl Group = Alcaraz (2), Medvedev (4), Cobolli (5), Tiafoe (7).",
        "story": "The 2026 Nitto ATP Finals draw is officially locked after Thursday's ceremony in Turin ahead of Sunday's tournament opener (15-22 November) at Inalpi Arena. Top seed Alexander Zverev headlines the John McEnroe Group alongside third seed Ben Shelton, sixth seed Arthur Fils and eighth seed Rafael Jodar. Fresh off his Paris Masters triumph, second seed Carlos Alcaraz anchors the Ivan Lendl Group alongside fourth seed Daniil Medvedev, fifth seed and home favourite Flavio Cobolli, and seventh seed Frances Tiafoe. Meanwhile in Stockholm today, top seed Taylor Fritz and Holger Rune meet in a blockbuster Center Court quarterfinal.",
        "stakes": "Eight season finalists now have clear round-robin paths inside Turin's Inalpi Arena starting Sunday, 15 November.",
        "rivalryAngle": "Power servers Zverev and Shelton meet young risers Fils and Jodar in McEnroe; Alcaraz and Medvedev share Lendl with Cobolli and Tiafoe.",
        "funFacts": [
            "John McEnroe Group: Alexander Zverev (1), Ben Shelton (3), Arthur Fils (6), Rafael Jodar (8).",
            "Ivan Lendl Group: Carlos Alcaraz (2), Daniil Medvedev (4), Flavio Cobolli (5), Frances Tiafoe (7).",
            "Group-stage play runs 15-22 November on indoor hard courts at Inalpi Arena in Turin."
        ],
        "keyPlayers": [
            {"name": "Alexander Zverev", "team": "Germany", "hook": "No. 1 seed heading the John McEnroe Group with Ben Shelton, Arthur Fils and Rafael Jodar."},
            {"name": "Carlos Alcaraz", "team": "Spain", "hook": "No. 2 seed anchoring the Ivan Lendl Group alongside Daniil Medvedev, Flavio Cobolli and Frances Tiafoe."},
            {"name": "Flavio Cobolli", "team": "Italy", "hook": "Home No. 5 seed drawn into the Ivan Lendl Group at Inalpi Arena."}
        ],
        "headToHead": "Official draw completed Thursday 12 November 2026. Tournament dates: 15-22 November 2026, Inalpi Arena, Turin.",
        "tags": ["tennis", "atp", "nitto-atp-finals", "turin", "alcaraz", "zverev", "medvedev", "shelton", "cobolli"],
        "home": "Alexander Zverev",
        "away": "Carlos Alcaraz",
        "homeCode": "GER",
        "awayCode": "ESP",
        "homeFlag": "de",
        "awayFlag": "es",
        "group": "Nitto ATP Finals Groups",
        "matchday": 1,
        "date": "2026-11-15",
        "time": "14:00",
        "venue": "Inalpi Arena",
        "city": "Turin",
        "status": "UPCOMING",
        "homeScore": None,
        "awayScore": None,
        "marquee": True,
        "liveMinute": None,
        "image": IMG["ten"],
        "decidedBy": None,
        "homePen": None,
        "awayPen": None,
        "sport": "tennis",
        "competition": "atp-finals-2026",
        "format": "leaderboard",
        "season": "2026",
        "roundLabel": "Turin Draw Set",
        "resultSummary": "MCENROE GROUP: Zverev (1), Shelton (3), Fils (6), Jodar (8) | LENDL GROUP: Alcaraz (2), Medvedev (4), Cobolli (5), Tiafoe (7).",
        "leaderboard": [
            {"pos": "McEnroe", "name": "Alexander Zverev (1)", "score": "Top Seed", "note": "John McEnroe Group"},
            {"pos": "McEnroe", "name": "Ben Shelton (3)", "score": "No. 3 Seed", "note": "John McEnroe Group"},
            {"pos": "McEnroe", "name": "Arthur Fils (6)", "score": "No. 6 Seed", "note": "John McEnroe Group"},
            {"pos": "McEnroe", "name": "Rafael Jodar (8)", "score": "No. 8 Seed", "note": "John McEnroe Group"},
            {"pos": "Lendl", "name": "Carlos Alcaraz (2)", "score": "No. 2 Seed", "note": "Ivan Lendl Group"},
            {"pos": "Lendl", "name": "Daniil Medvedev (4)", "score": "No. 4 Seed", "note": "Ivan Lendl Group"},
            {"pos": "Lendl", "name": "Flavio Cobolli (5)", "score": "No. 5 Seed", "note": "Ivan Lendl Group"},
            {"pos": "Lendl", "name": "Frances Tiafoe (7)", "score": "No. 7 Seed", "note": "Ivan Lendl Group"}
        ],
        "tennisSets": [],
        "sources": [
            {"name": "Nitto ATP Finals: 2026 Turin official group draw announcement", "url": "https://www.nittoatpfinals.com/en/news/turin-2026-qualifiers-draw"},
            {"name": "ATP Tour: Zverev and Alcaraz head 2026 Turin groups", "url": "https://www.atptour.com/en/tournaments/nitto-atp-finals/605/overview"}
        ]
    }
    dump(os.path.join(MATCHES, "atp-nitto-finals-2026-turin-draw.json"), atp_turin_draw)

    # 7b. Tennis Today Thu Nov 12 Stockholm QF: Taylor Fritz vs Holger Rune
    stockholm_qf = {
        "slug": "atp-stockholm-open-2026-fritz-vs-rune-qf",
        "headline": "Stockholm Open QF Today: Top seed Taylor Fritz faces former champion Holger Rune",
        "whyCareScore": 8.6,
        "whyCareReason": "After Fritz defeated Cameron Norrie 7-5, 6-3 and Rune rallied past Miomir Kecmanovic 2-6, 6-1, 6-4 on Wednesday, both meet on Center Court today.",
        "teaser": "TODAY QF (Thu 12 Nov, Stockholm Center Court): Taylor Fritz vs Holger Rune. Wed R16: Fritz def. Norrie 7-5, 6-3; Rune def. Kecmanovic 2-6, 6-1, 6-4.",
        "story": "The Bybit Stockholm Open delivers a marquee indoor quarterfinal today, Thursday 12 November, on Center Court at Kungliga Tennishallen as top seed Taylor Fritz meets former champion Holger Rune. Both punched their tickets with impressive Wednesday wins: Fritz dismissed Cameron Norrie in straight sets, 7-5, 6-3, while Rune recovered from a slow opening frame to subdue Miomir Kecmanovic 2-6, 6-1, 6-4. Elsewhere in Stockholm's draw, third seed Lorenzo Musetti had earlier beaten Toby Samuel 6-1, 6-4 and seventh seed Ugo Humbert defeated Adolfo Daniel Vallejo 6-4, 6-3.",
        "stakes": "A semifinal berth at Kungliga Tennishallen goes to the winner between No. 1 seed Fritz and former Stockholm titleholder Rune.",
        "rivalryAngle": "Fritz's heavy indoor first strike faces Rune's counterpunching athleticism right after Rune's three-set comeback over Kecmanovic.",
        "funFacts": [
            "Wednesday R16 finals: Taylor Fritz def. Cameron Norrie 7-5, 6-3; Holger Rune def. Miomir Kecmanovic 2-6, 6-1, 6-4.",
            "Wednesday victory over Kecmanovic marked Holger Rune's second consecutive win in Stockholm after defeating Zizou Bergs 6-3, 6-4.",
            "Played alongside Thursday's official Nitto ATP Finals Turin group draw."
        ],
        "keyPlayers": [
            {"name": "Taylor Fritz", "team": "United States", "hook": "Top seed into the Stockholm QFs after a 7-5, 6-3 win over Cameron Norrie."},
            {"name": "Holger Rune", "team": "Denmark", "hook": "Came back from a set down to beat Miomir Kecmanovic 2-6, 6-1, 6-4 on Wednesday."}
        ],
        "headToHead": "Thursday 12 November 2026. Kungliga Tennishallen, Stockholm. Center Court quarterfinal.",
        "tags": ["tennis", "atp", "stockholm-open", "taylor-fritz", "holger-rune", "quarterfinal"],
        "home": "Taylor Fritz",
        "away": "Holger Rune",
        "homeCode": "USA",
        "awayCode": "DEN",
        "homeFlag": "us",
        "awayFlag": "dk",
        "group": "Stockholm Open QF",
        "matchday": 4,
        "date": "2026-11-12",
        "time": "17:30",
        "venue": "Kungliga Tennishallen",
        "city": "Stockholm",
        "status": "UPCOMING",
        "homeScore": None,
        "awayScore": None,
        "marquee": False,
        "liveMinute": None,
        "image": IMG["ten"],
        "decidedBy": None,
        "homePen": None,
        "awayPen": None,
        "sport": "tennis",
        "competition": "atp-250-stockholm-2026",
        "format": "singles",
        "season": "2026",
        "roundLabel": "Stockholm QF Today",
        "resultSummary": "TODAY QF: Taylor Fritz vs Holger Rune (Wed: Fritz 7-5, 6-3 Norrie; Rune 2-6, 6-1, 6-4 Kecmanovic).",
        "leaderboard": [],
        "tennisSets": [],
        "sources": [
            {"name": "ATP Tour: Stockholm Open 2026 Thursday Center Court order of play", "url": "https://www.atptour.com/en/scores/current/stockholm/429/daily-schedule"},
            {"name": "Sportskeeda: Fritz vs Rune Stockholm Open quarterfinal preview", "url": "https://www.sportskeeda.com/tennis"}
        ]
    }
    dump(os.path.join(MATCHES, "atp-stockholm-open-2026-fritz-vs-rune-qf.json"), stockholm_qf)

    # 8. Golf R1 Complete TODAY Thu Nov 12: DP World Tour Championship Dubai
    golf_dubai_r1 = {
        "slug": "dp-world-tour-championship-dubai-2026",
        "headline": "Dubai R1 Complete: Joost Luiten leads with 67 (-5) while Rory McIlroy opens 69 (-3), three clear of Chacarra",
        "whyCareScore": 9.5,
        "whyCareReason": "Last man into the 50-player field Joost Luiten shoots 67 (-5) ahead of Jacob Skov Olesen (-4, 68), while Rory McIlroy (-3, 69) trims three shots off leader Eugenio Chacarra (E, 72).",
        "teaser": "R1 FINAL (Dubai): 1. Joost Luiten -5 (67); 2. Jacob Skov Olesen -4 (68); T3. Rory McIlroy -3 (69), Victor Perez -3, Gregorio De Leo -3, Freddy Schott -3, Francesco Laporta -3; T28. Eugenio Chacarra E (72).",
        "story": "Opening-day fireworks reshaped the DP World Tour Championship on Thursday, 12 November, at the Earth Course in Jumeirah Golf Estates. Joost Luiten, the 50th and final player to qualify for the season finale field, charged into the solo first-round lead with a five-under 67 featuring seven birdies and two bogeys, his lowest round on the Earth Course since 2016. Denmark's Jacob Skov Olesen sits one shot back in second after a 68 (-4). Playing together in the marquee anchor group, Masters champion Rory McIlroy opened with a steady three-under 69 highlighted by a tap-in birdie on the par-5 18th to join a five-way tie for third alongside Victor Perez, Gregorio De Leo, Freddy Schott and Francesco Laporta (-3). Crucially in the Race to Dubai duel ($10 million purse, $3 million first prize), points leader Eugenio Chacarra (4,243.79 pts) carded an even-par 72 for a share of 28th, handing McIlroy (3,709.86 pts) a three-stroke head start with 54 holes remaining.",
        "stakes": "McIlroy trims the immediate gap in Dubai by firing 69 to Chacarra's 72 while Joost Luiten holds a one-shot cushion at 5-under entering Round 2 Friday.",
        "rivalryAngle": "Anchor-group contrast in Dubai: Rory McIlroy gained three shots on Race leader Eugenio Chacarra right out of the gate on Thursday.",
        "funFacts": [
            "Last man in the 50-player field Joost Luiten hit seven birdies against two bogeys for 67 (-5), his best Earth Course round since 2016.",
            "Rory McIlroy closed with a tap-in birdie at the par-5 18th for 69 (-3, T3), three clear of anchor partner Eugenio Chacarra (72, E, T28).",
            "Five players share third at -3: Rory McIlroy, Victor Perez, Gregorio De Leo, Freddy Schott and Francesco Laporta behind Jacob Skov Olesen (-4, 68)."
        ],
        "keyPlayers": [
            {"name": "Joost Luiten", "team": "Netherlands", "hook": "50th man in the field leads Round 1 at 5-under 67 with seven birdies."},
            {"name": "Rory McIlroy", "team": "Northern Ireland", "hook": "Carded 69 (-3, T3), opening a three-shot edge over Race leader Eugenio Chacarra."},
            {"name": "Eugenio Chacarra", "team": "Spain", "hook": "Opened with even-par 72 (T28) to sit five back after 18 holes in Dubai."}
        ],
        "headToHead": "Thursday 12 November 2026, Round 1 Complete. Earth Course, Jumeirah Golf Estates, Dubai.",
        "tags": ["golf", "dp-world-tour", "dubai", "joost-luiten", "rory-mcilroy", "eugenio-chacarra", "jacob-skov-olesen"],
        "home": "Joost Luiten",
        "away": "Rory McIlroy",
        "homeCode": "NED",
        "awayCode": "ENG",
        "homeFlag": "nl",
        "awayFlag": "gb-eng",
        "group": "DP World Tour Finale",
        "matchday": 1,
        "date": "2026-11-12",
        "time": "12:40",
        "venue": "Earth Course, Jumeirah Golf Estates",
        "city": "Dubai",
        "status": "FINISHED",
        "homeScore": "-5 (67)",
        "awayScore": "-3 (69)",
        "marquee": True,
        "liveMinute": None,
        "image": IMG["golf"],
        "decidedBy": "round1",
        "homePen": None,
        "awayPen": None,
        "sport": "golf",
        "competition": "dp-world-tour-2026",
        "format": "leaderboard",
        "season": "2026",
        "roundLabel": "Round 1 Complete",
        "resultSummary": "R1 DUBAI: Luiten -5 (67), Skov Olesen -4 (68), McIlroy -3 (69, T3 w/ Perez, De Leo, Schott, Laporta), Chacarra E (72, T28).",
        "leaderboard": [
            {"pos": "1", "name": "Joost Luiten", "score": "-5 (67)", "note": "7 birdies, 2 bogeys; solo R1 lead"},
            {"pos": "2", "name": "Jacob Skov Olesen", "score": "-4 (68)", "note": "One shot off the lead"},
            {"pos": "T3", "name": "Rory McIlroy", "score": "-3 (69)", "note": "Tap-in birdie at 18; +3 over Chacarra"},
            {"pos": "T3", "name": "Victor Perez", "score": "-3", "note": "Five-way tie for third"},
            {"pos": "T3", "name": "Gregorio De Leo", "score": "-3", "note": "Five-way tie for third"},
            {"pos": "T3", "name": "Freddy Schott", "score": "-3", "note": "Five-way tie for third"},
            {"pos": "T3", "name": "Francesco Laporta", "score": "-3", "note": "Five-way tie for third"},
            {"pos": "T28", "name": "Eugenio Chacarra", "score": "E (72)", "note": "Race to Dubai leader (4,243.79 pts)"}
        ],
        "tennisSets": [],
        "sources": [
            {"name": "European Tour: Joost Luiten leads DP World Tour Championship after R1 67", "url": "https://www.europeantour.com/dpworld-tour/news/articles/dp-world-tour-championship-2026-round-1/"},
            {"name": "Golf Digest ME: Jacob Skov Olesen (-4) & Rory McIlroy (-3) trail Luiten in Dubai", "url": "https://www.golfdigestme.com/dp-world-tour-championship-2026-r1"}
        ]
    }
    dump(os.path.join(MATCHES, "dp-world-tour-championship-dubai-2026.json"), golf_dubai_r1)

    # 9. Formula 1 Las Vegas Strip GP (correct Round 21 & 6.201-km Strip distance)
    f1_vegas = {
        "slug": "las-vegas-gp-strip-2026",
        "headline": "F1 Countdown to Las Vegas (Round 21): 33 points split Verstappen to Norris behind Antonelli",
        "whyCareScore": 9.1,
        "whyCareReason": "Entering Round 21 on the 6.201 km Las Vegas Strip Circuit (19-21 Nov), Kimi Antonelli (390) and Mercedes (652) are Champions while five drivers pack within 33 points for P2.",
        "teaser": "ROUND 21 NEXT (19-21 Nov, Las Vegas Strip): Antonelli 390 (Champion); Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246. Mercedes 652, Ferrari 510, Red Bull 415, McLaren 398.",
        "story": "One week ahead of Round 21 of the 2026 FIA Formula One World Championship under the neon lights of the 6.201-kilometre Las Vegas Strip Circuit (19-21 November, Grand Prix Saturday night 21 November), both major crowns are settled after Interlagos, yet the race for second overall remains razor sharp. Drivers Champion Kimi Antonelli sits uncatchable on 390 points and Mercedes holds 652 Constructors points, leaving just 33 points separating second through sixth in the Drivers table: Max Verstappen leads that five-way fight on 279 points after surging from 21st to second in Sao Paulo, pursued by George Russell (262), Lewis Hamilton (261), Charles Leclerc (249) and Interlagos winner Lando Norris (246). In the Constructors battle behind Mercedes, Ferrari sits second on 510 points while Red Bull (415) protects a 17-point gap over McLaren (398).",
        "stakes": "Thirty-three points divide Drivers P2 (Verstappen 279) through P6 (Norris 246) ahead of next week's Round 21 night race on the Strip, with Red Bull (415) 17 ahead of McLaren (398).",
        "rivalryAngle": "Interlagos winner Norris and P21-to-P2 charger Verstappen lead a five-driver dash with Russell, Hamilton and Leclerc entering Nevada.",
        "funFacts": [
            "Las Vegas (19-21 Nov) marks Round 21 of the 2026 season around the 6.201 km Las Vegas Strip Circuit.",
            "George Russell (262) leads Ferrari's Lewis Hamilton (261) by a single point, with Charles Leclerc (249) and Lando Norris (246) in range.",
            "Red Bull (415) defends third in Constructors just 17 points ahead of McLaren (398)."
        ],
        "keyPlayers": [
            {"name": "Max Verstappen", "team": "Red Bull", "hook": "Holds P2 on 279 points entering Round 21 after climbing from 21st to second in Sao Paulo."},
            {"name": "Lando Norris", "team": "McLaren", "hook": "Surged to 246 points with his wet-weather victory in Brazil as McLaren chases Red Bull."},
            {"name": "Lewis Hamilton", "team": "Ferrari", "hook": "Sits on 261 points, one behind George Russell (262) in a tightly packed top six."}
        ],
        "headToHead": "19-21 November 2026 (Round 21). 6.201 km Las Vegas Strip Circuit, Saturday night GP on 21 November.",
        "tags": ["f1", "formula-1", "las-vegas-gp", "verstappen", "norris", "hamilton", "russell", "ferrari", "mclaren"],
        "home": "Max Verstappen",
        "away": "Lando Norris",
        "homeCode": "NED",
        "awayCode": "ENG",
        "homeFlag": "nl",
        "awayFlag": "gb-eng",
        "group": "Formula 1",
        "matchday": 21,
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
        "roundLabel": "Round 21 Countdown",
        "resultSummary": "ROUND 21 VEGAS (19-21 Nov): Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246 (Antonelli Champion 390; Mercedes 652).",
        "leaderboard": [
            {"pos": "1", "name": "Kimi Antonelli (Mercedes)", "score": "390 pts", "note": "2026 Drivers Champion"},
            {"pos": "2", "name": "Max Verstappen (Red Bull)", "score": "279 pts", "note": "P2 entering Round 21"},
            {"pos": "3", "name": "George Russell (Mercedes)", "score": "262 pts", "note": "+1 over Hamilton"},
            {"pos": "4", "name": "Lewis Hamilton (Ferrari)", "score": "261 pts", "note": "400th GP completed"},
            {"pos": "5", "name": "Charles Leclerc (Ferrari)", "score": "249 pts", "note": "Ferrari 510 Constructors pts"},
            {"pos": "6", "name": "Lando Norris (McLaren)", "score": "246 pts", "note": "Sao Paulo winner (McLaren 398)"}
        ],
        "tennisSets": [],
        "sources": [
            {"name": "Formula1.com: 2026 Heineken Las Vegas Grand Prix Round 21 event guide", "url": "https://www.formula1.com/en/racing/2026/las-vegas"},
            {"name": "FIA / Formula1.com: 2026 Drivers and Constructors Championship standings", "url": "https://www.formula1.com/en/results/2026/drivers"}
        ]
    }
    dump(os.path.join(MATCHES, "las-vegas-gp-strip-2026.json"), f1_vegas)

    # =========================================================================
    # PART 2: 6 New "Why Care" Stories (pubDate: 2026-11-12, zero em-dashes)
    # =========================================================================

    stories_data = [
        {
            "slug": "uwcl-barcelona-arsenal-camp-nou-ol-lyonnes-6-0-juventus-2026",
            "title": "Camp Nou Blockbuster: Barcelona host Arsenal tonight after OL Lyonnes crush Juventus 6-0",
            "subtitle": "Arsenal Women play their first official match at Camp Nou in a 2025 Lisbon final rematch alongside England vs Croatia at Wembley.",
            "category": "Preview",
            "excerpt": "Rescheduled by Storm Charles, unbeaten Barcelona (9 pts) host Arsenal (7 pts) at Spotify Camp Nou hours after OL Lyonnes tore through Juventus 6-0 in Biella.",
            "image": IMG["soc"],
            "readingTime": 4,
            "pubDate": "2026-11-12",
            "sport": "soccer",
            "competition": "uwcl-2026-27",
            "relatedSlug": "uwcl-barcelona-vs-arsenal-md4-2026",
            "sources": [
                {"name": "FC Barcelona: UWCL Matchday 4 vs Arsenal at Spotify Camp Nou", "url": "https://www.fcbarcelona.com/en/football/womens-football"},
                {"name": "UEFA: Nations League MD5 England vs Croatia & Italy vs France schedule", "url": "https://www.uefa.com/uefanationsleague/"}
            ],
            "content": """European club and international soccer collide under Thursday night lights on 12 November, anchored by FC Barcelona Femeni hosting Arsenal Women at Spotify Camp Nou (6:45 p.m. CET) in a repeat of the 2025 Lisbon final. Pushed back 24 hours by Storm Charles alerts, tonight marks Arsenal Women's first official fixture at Camp Nou. Barcelona brings three wins from three (scoring 19 across victories over Paris FC, Roma and HB Koge, plus a 7-0 domestic rout of Real Madrid) with Aitana Bonmati and Alexia Putellas facing Alessia Russo and third-placed Arsenal (7 points, fresh off beating Liverpool 2-1 in the WSL).

The Camp Nou showcase lands directly after OL Lyonnes tore through Juventus Women 6-0 in Biella on Wednesday night, sparked by two Marie-Antoinette Katoto strikes inside four minutes (31', 35') before Melchie Dumornay (40'), Lily Yohannes (80'), Korbin Albert (85') and Wendie Renard (90+1') completed the rout as OH Leuven and HB Koge drew 1-1.

Men's UEFA Nations League Matchday 5 runs alongside UWCL tonight: England hosts Croatia at Wembley (19:45 UK) needing just a point for the quarterfinals, Italy meets France at San Siro (20:45 CET), already-qualified Spain visits Czechia (20:45 CET), and Turkiye welcomes Belgium (18:00 CET) while Arsenal keeps its five-point Premier League cushion (27 to Brighton's 22 and Man City's 21)."""
        },
        {
            "slug": "nfl-week10-tnf-tonight-daniels-mccarthy-giants-commanders-2026",
            "title": "NFL TNF Tonight: Both QBs cleared as Giants (5-2-1) host Commanders minus center Lucas Patrick",
            "subtitle": "Jayden Daniels carries zero injury designation opposite J.J. McCarthy for MetLife Stadium's Vintage White Out five weeks after a 27-27 tie.",
            "category": "Preview",
            "excerpt": "Washington gets Jayden Daniels back without an injury tag tonight in East Rutherford, but loses starting center Lucas Patrick and TE Colson Yankoff against 5-2-1 New York.",
            "image": IMG["nfl"],
            "readingTime": 4,
            "pubDate": "2026-11-12",
            "sport": "football",
            "competition": "nfl-2026",
            "relatedSlug": "commanders-at-giants-tnf-week10-2026",
            "sources": [
                {"name": "NFL.com: Commanders at Giants Week 10 TNF final injury report", "url": "https://www.nfl.com/games/commanders-at-giants-2026-reg-10"},
                {"name": "Giants.com: Week 10 White Out status updates for McCarthy, Nabers and Skattebo", "url": "https://www.giants.com/news/giants-commanders-week-10-thursday-night-football-2026"}
            ],
            "content": """Both young quarterbacks enter tonight's Week 10 Thursday Night Football showcase with green lights. Ahead of the 8:15 p.m. ET Prime Video kickoff at MetLife Stadium, Washington quarterback Jayden Daniels logged full participation with his left elbow and carries no game status designation for tonight's rematch of Week 5's 27-27 overtime thriller.

Even with Daniels cleared, the Commanders (2-5-1) face a stiff test on the offensive line: starting center Lucas Patrick (concussion, replaced by Nick Allegretti) and tight end Colson Yankoff (knee) are officially OUT, while wide receiver Treylon Burks (foot) is expected to suit up after missing short-week practices.

John Harbaugh's NFC East-leading Giants (5-2-1, 2-0-1 in division) arrive healthy across their skill core after winning 19-11 in Philadelphia last Sunday. J.J. McCarthy (hip), running back Cam Skattebo (hamstring), Malik Nabers (knee), left tackle Andrew Thomas (groin) and tight end Theo Johnson (neck) are all completely clear of the injury report (only linebacker Malik Harrison is questionable) as East Rutherford stages its Vintage White Out."""
        },
        {
            "slug": "nba-harden-32-cavs-knicks-rockets-beat-warriors-curry-injury-2026",
            "title": "NBA: Harden scores 32 at MSG as Cavs beat Knicks; Rockets down Warriors after early Curry injury",
            "subtitle": "Sengun, Smith Jr. and Sheppard lift Houston 115-108 after Stephen Curry exits Q1, while Boston rallies from 22 down to edge Toronto 98-93.",
            "category": "Match Report",
            "excerpt": "Cleveland tops New York 115-107 behind James Harden's 32 points while Golden State loses Stephen Curry in the first quarter of a 115-108 loss at Houston.",
            "image": IMG["nba"],
            "readingTime": 4,
            "pubDate": "2026-11-12",
            "sport": "basketball",
            "competition": "nba-2026-27",
            "relatedSlug": "nba-rockets-vs-warriors-nov11-2026",
            "sources": [
                {"name": "ESPN: Cavaliers 115-107 Knicks and Rockets 115-108 Warriors recaps", "url": "https://www.espn.com/nba/scoreboard"},
                {"name": "NBA.com: Celtics rally from 22 down in Toronto; Thursday 4-game slate", "url": "https://www.nba.com/schedule"}
            ],
            "content": """ESPN's Wednesday night doubleheader delivered fireworks in New York and anxious injury news in Houston on 11 November. At Madison Square Garden, James Harden drilled five three-pointers on his way to a game-high 32 points alongside Donovan Mitchell's 23, lifting the Cleveland Cavaliers past Jalen Brunson (27), Karl-Anthony Towns (21) and the New York Knicks 115-107.

Later at Toyota Center, Golden State lost Stephen Curry early in the first quarter to injury after scoring three points, and Houston's balanced attack took full advantage in a 115-108 Rockets win. Alperen Sengun led Houston with 19 points, Jabari Smith Jr. added 14 and Reed Sheppard chipped in 13, withstanding 25 points from Yaxel Lendeborg, 22 from Brandin Podziemski, 13 from L.J. Cryer and 11 from De'Anthony Melton.

Elsewhere Wednesday, East leader Boston wiped out a 22-point hole in Toronto behind Jayson Tatum's 24 points to defeat the Raptors 98-93. Tonight, Thursday 12 November brings a four-game slate: Raptors at 76ers (7:00 p.m. ET), Pistons at Wizards (7:00 p.m. ET), Mavericks at Timberwolves (8:00 p.m. ET) and Hornets at Suns (9:00 p.m. ET)."""
        },
        {
            "slug": "atp-nitto-finals-2026-turin-draw-alcaraz-zverev-fritz-rune-stockholm",
            "title": "Nitto ATP Finals Draw: Zverev heads McEnroe Group opposite Alcaraz as Fritz meets Rune in Stockholm QF",
            "subtitle": "Turin splits the final eight into two balanced groups ahead of Sunday while Fritz and Rune square off today on Center Court in Sweden.",
            "category": "Desk",
            "excerpt": "Alexander Zverev draws Ben Shelton, Arthur Fils and Rafael Jodar in Turin while Carlos Alcaraz meets Daniil Medvedev, Flavio Cobolli and Frances Tiafoe.",
            "image": IMG["ten"],
            "readingTime": 4,
            "pubDate": "2026-11-12",
            "sport": "tennis",
            "competition": "atp-finals-2026",
            "relatedSlug": "atp-nitto-finals-2026-turin-draw",
            "sources": [
                {"name": "Nitto ATP Finals: 2026 official Turin group draw", "url": "https://www.nittoatpfinals.com/en/news/turin-2026-qualifiers-draw"},
                {"name": "ATP Tour: Stockholm Open R16 results and Thursday QF order of play", "url": "https://www.atptour.com/en/scores/current/stockholm/429/daily-schedule"}
            ],
            "content": """The eight-man battle lines for Turin are officially drawn. At Thursday's 2026 Nitto ATP Finals ceremony, top seed Alexander Zverev landed in the John McEnroe Group alongside third seed Ben Shelton, sixth seed Arthur Fils and eighth seed Rafael Jodar ahead of Sunday's tournament start (15-22 November) at Inalpi Arena.

In the opposing Ivan Lendl Group, Paris Masters champion and second seed Carlos Alcaraz drew fourth seed Daniil Medvedev, Italian fifth seed Flavio Cobolli and seventh seed Frances Tiafoe, locking up a marquee blend of baseline firepower and home-court Italian noise.

North in Sweden, Thursday's Stockholm Open quarterfinals feature a compelling Center Court clash between top seed Taylor Fritz and former champion Holger Rune. Both advanced through Wednesday's Round of 16: Fritz defeated Cameron Norrie in straight sets, 7-5, 6-3, while Rune rallied past Miomir Kecmanovic 2-6, 6-1, 6-4 after Musetti (6-1, 6-4 vs Toby Samuel) and Ugo Humbert had earlier progressed."""
        },
        {
            "slug": "dp-world-tour-championship-2026-luiten-leads-67-mcilroy-69-chacarra-72",
            "title": "Dubai R1: Joost Luiten leads with 67 as Rory McIlroy opens 69 to gain three on Chacarra",
            "subtitle": "Last man into the 50-player field shoots five-under at Jumeirah Golf Estates while McIlroy finishes strong on 18 against Race leader Chacarra (72).",
            "category": "Match Report",
            "excerpt": "Joost Luiten carded 67 (-5) to lead Jacob Skov Olesen (68) by one in Dubai, while Rory McIlroy shot 69 (-3, T3) to gain three strokes on Eugenio Chacarra (72, T28).",
            "image": IMG["golf"],
            "readingTime": 4,
            "pubDate": "2026-11-12",
            "sport": "golf",
            "competition": "dp-world-tour-2026",
            "relatedSlug": "dp-world-tour-championship-dubai-2026",
            "sources": [
                {"name": "European Tour: Joost Luiten shoots 67 to lead Dubai Round 1", "url": "https://www.europeantour.com/dpworld-tour/news/articles/dp-world-tour-championship-2026-round-1/"},
                {"name": "Golf Digest ME: McIlroy beats Chacarra by three in opening Dubai group", "url": "https://www.golfdigestme.com/dp-world-tour-championship-2026-r1"}
            ],
            "content": """Joost Luiten walked onto the Earth Course at Jumeirah Golf Estates as the 50th and last qualifier into the DP World Tour Championship and walked off Thursday with the solo first-round lead. Mixing seven birdies with two bogeys, the Dutchman signed for a five-under 67, his lowest round on the Earth Course since 2016.

Denmark's Jacob Skov Olesen sits one shot off the pace after an opening 68 (-4), followed by a five-way tie for third at three-under featuring Rory McIlroy (69), Victor Perez, Gregorio De Leo, Freddy Schott and Francesco Laporta.

For the Race to Dubai ($10 million purse, $3 million first prize), Thursday's anchor pairing already tilted toward drama: Masters champion McIlroy capped a crisp 69 with a tap-in birdie at the par-5 18th, trimming three early strokes off points leader Eugenio Chacarra (4,243.79 pts vs 3,709.86), who settled for an even-par 72 in a share of 28th."""
        },
        {
            "slug": "f1-countdown-las-vegas-round-21-five-way-chase-behind-antonelli-2026",
            "title": "One Week to Round 21 in Las Vegas: Five F1 drivers packed within 33 points behind Champion Antonelli",
            "subtitle": "With Mercedes (652) and Antonelli (390) crowned, Verstappen (279) leads Russell, Hamilton, Leclerc and Norris along the 6.201 km Strip.",
            "category": "Desk",
            "excerpt": "Next week's Round 21 Las Vegas GP carries fierce top-six stakes: just 33 points divide Verstappen (279) from Norris (246), while Red Bull holds a 17-point edge over McLaren.",
            "image": IMG["f1"],
            "readingTime": 4,
            "pubDate": "2026-11-12",
            "sport": "f1",
            "competition": "f1-2026",
            "relatedSlug": "las-vegas-gp-strip-2026",
            "sources": [
                {"name": "Formula1.com: 2026 Heineken Las Vegas Grand Prix Round 21 preview", "url": "https://www.formula1.com/en/racing/2026/las-vegas"},
                {"name": "FIA / Formula1.com: 2026 World Championship standings", "url": "https://www.formula1.com/en/results/2026/drivers"}
            ],
            "content": """Seven days before cars hit the 6.201-kilometre Las Vegas Strip Circuit for Round 21 of the 2026 FIA Formula One World Championship (19-21 November, Saturday night race), both headline trophies already belong to Mercedes and Kimi Antonelli. Yet the scoreboard directly below Antonelli's uncatchable 390 points remains wide open.

Fresh off climbing from 21st to second behind winner Lando Norris in wet Sao Paulo, Max Verstappen holds P2 on 279 points, holding off George Russell (262) and Ferrari's Lewis Hamilton (261), separated by a solitary point. Charles Leclerc sits fourth-best of the chasers on 249, only three clear of Interlagos victor Norris (246), compressing second through sixth into a tight 33-point corridor.

Behind Constructors champion Mercedes (652 points), Ferrari sits firm in second on 510 points while Red Bull (415) carries a delicate 17-point buffer over fourth-placed McLaren (398) heading under the Strip floodlights."""
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
    # PART 3: Update frontend/src/data/sports.ts (SITE_TODAY = '2026-11-12')
    # Use double quotes ("...") for tagline/liveNow/pulse where needed so no apostrophes collide!
    # =========================================================================

    sports_ts_content = """export const SITE_TODAY = '2026-11-12';

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
    slug: 'soccer',
    label: 'Soccer',
    short: 'Soccer',
    href: '/sport/soccer',
    tagline: "UWCL & Nations League Tonight: Barcelona host Arsenal at Camp Nou; England face Croatia at Wembley after OL Lyonnes crushed Juventus 6-0.",
    liveNow: "Tonight: Barcelona vs Arsenal (18:45 CET Camp Nou); England vs Croatia (19:45 UK), Italy vs France, Czechia vs Spain (20:45 CET). Wed UWCL: Juventus 0-6 OL Lyonnes.",
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: "TONIGHT: BARCELONA VS ARSENAL AT CAMP NOU & ENGLAND VS CROATIA AFTER LYON 6-0 AT JUVENTUS",
    board: 'Open the pitch',
    span: 'hero',
  },
  {
    slug: 'football',
    label: 'Football',
    short: 'NFL',
    href: '/sport/football',
    tagline: "TNF Tonight (8:15 p.m. ET, Prime Video): Both Jayden Daniels & J.J. McCarthy cleared for Giants White Out vs Commanders.",
    liveNow: "Tonight 8:15 p.m. ET: Commanders (2-5-1, C Patrick & TE Yankoff OUT, Daniels cleared) at Giants (5-2-1, McCarthy/Nabers/Skattebo active). MNF Final: Bills 23, Vikings 6.",
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: "NFL TNF TONIGHT: JAYDEN DANIELS & J.J. MCCARTHY CLEARED FOR METLIFE WHITE OUT REMATCH",
    board: 'Open the field',
    span: 'side',
  },
  {
    slug: 'basketball',
    label: 'Basketball',
    short: 'Hoops',
    href: '/sport/basketball',
    tagline: "NBA: Harden's 32 leads Cavaliers past Knicks 115-107; Rockets beat Warriors 115-108 as Curry exits Q1 injured.",
    liveNow: "Wed Finals: Cavaliers 115, Knicks 107 (Harden 32, Brunson 27); Rockets 115, Warriors 108 (Curry Q1 inj., Sengun 19); Celtics 98, Raptors 93 (-22 rally). Tonight: 4 NBA games.",
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: "NBA: HARDEN DROPS 32 AT MSG, WARRIORS LOSE CURRY EARLY AT HOUSTON & CELTICS RALLY FROM 22",
    board: 'Open the floor',
    span: 'half',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: "Dubai R1 Complete: Joost Luiten fires 67 (-5) to lead Jacob Skov Olesen (68) & Rory McIlroy (69, T3).",
    liveNow: "Dubai R1: 1. Joost Luiten -5 (67); 2. Jacob Skov Olesen -4 (68); T3. Rory McIlroy -3 (69), Perez, De Leo, Schott, Laporta; T28. Eugenio Chacarra E (72).",
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: "DUBAI R1: LUITEN LEADS ON 67 (-5) WHILE MCILROY OPENS 69 TO GAIN THREE ON CHACARRA",
    board: 'Open the course',
    span: 'half',
  },
  {
    slug: 'tennis',
    label: 'Tennis',
    short: 'Tennis',
    href: '/sport/tennis',
    tagline: "Turin Draw Set: Zverev anchors McEnroe Group & Alcaraz leads Lendl Group; Fritz faces Rune today in Stockholm QF.",
    liveNow: "Turin: McEnroe = Zverev (1), Shelton (3), Fils (6), Jodar (8); Lendl = Alcaraz (2), Medvedev (4), Cobolli (5), Tiafoe (7). Stockholm Today: Fritz vs Rune QF.",
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: "NITTO ATP FINALS DRAW SET: ALCARAZ & ZVEREV SPLIT IN TURIN AS FRITZ MEETS RUNE IN STOCKHOLM",
    board: 'Open the court',
    span: 'half',
  },
  {
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: "One Week to Round 21 in Las Vegas: Five F1 drivers packed inside 33 points behind Champion Antonelli.",
    liveNow: "Drivers P2 Race: Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246 (Antonelli Champion 390; Mercedes 652). Round 21: Las Vegas (19-21 Nov).",
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: "ROUND 21 VEGAS COUNTDOWN: VERSTAPPEN TO NORRIS SEPARATED BY 33 PTS BEHIND ANTONELLI",
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
    .split(/\\s+/)
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
    # PART 4: Update frontend/src/data/desk.json accurately
    # =========================================================================

    desk_path = os.path.join(ROOT, "frontend/src/data/desk.json")
    with open(desk_path, "r", encoding="utf-8") as f:
        desk = json.load(f)

    desk["asOf"] = "2026-11-12"

    # Keep Nov 12 Week 10 TNF entry updated with final injury designations (Daniels/McCarthy cleared, Patrick OUT)
    nfl_notes = [x for x in desk.get("nflWeek1", []) if not (x.get("date") == "2026-11-12" and "Giants" in x.get("home", ""))]
    nfl_notes.append({
        "date": "2026-11-12",
        "time": "8:15 p.m. ET",
        "home": "New York Giants",
        "away": "Washington Commanders",
        "note": "TONIGHT TNF (Prime Video, MetLife White Out): Commanders (2-5-1) at Giants (5-2-1). Jayden Daniels & J.J. McCarthy cleared; C Lucas Patrick & TE Colson Yankoff OUT."
    })
    desk["nflWeek1"] = nfl_notes

    # Update Stockholm & Turin rows on tennis board (desk["usOpenQF"])
    tennis_notes = [x for x in desk.get("usOpenQF", []) if not (x.get("draw", "").startswith("Stockholm") or x.get("draw", "").startswith("Turin"))]
    tennis_notes.extend([
        {"draw": "Stockholm R16", "p1": "Lorenzo Musetti", "p2": "Toby Samuel", "status": "Musetti 6-1, 6-4"},
        {"draw": "Stockholm R16", "p1": "Taylor Fritz", "p2": "Cameron Norrie", "status": "Fritz 7-5, 6-3"},
        {"draw": "Stockholm R16", "p1": "Holger Rune", "p2": "Miomir Kecmanovic", "status": "Rune 2-6, 6-1, 6-4"},
        {"draw": "Stockholm QF", "p1": "Taylor Fritz", "p2": "Holger Rune", "status": "Today Center Court"},
        {"draw": "Turin McEnroe Group", "p1": "Alexander Zverev (1)", "p2": "Ben Shelton (3)", "status": "w/ Fils (6), Jodar (8)"},
        {"draw": "Turin Lendl Group", "p1": "Carlos Alcaraz (2)", "p2": "Daniil Medvedev (4)", "status": "w/ Cobolli (5), Tiafoe (7)"},
    ])
    desk["usOpenQF"] = tennis_notes

    dump(desk_path, desk)

    # =========================================================================
    # PART 5: Update AGENTS.md site clock line (zero em-dashes)
    # =========================================================================

    agents_path = os.path.join(ROOT, "AGENTS.md")
    with open(agents_path, "r", encoding="utf-8") as f:
        agents_lines = f.readlines()

    new_clock_line = (
        "*   **Site clock:** editorial today is `2026-11-12` in `frontend/src/data/sports.ts` (`SITE_TODAY`). "
        "Soccer: Tonight UWCL MD4 Barcelona vs Arsenal (18:45 CET Camp Nou) & Nations League MD5 England vs Croatia (19:45 UK Wembley), Italy vs France, Czechia vs Spain (20:45 CET); Wed UWCL Juventus 0-6 OL Lyonnes (Katoto 2) & OH Leuven 1-1 HB Koge; PL Arsenal 27, Brighton 22, Man City 21. "
        "Football: Tonight Week 10 TNF Commanders (2-5-1, Jayden Daniels cleared, C Lucas Patrick & TE Colson Yankoff OUT) at Giants (5-2-1, J.J. McCarthy/Nabers/Skattebo active, 8:15 p.m. ET Prime Video); MNF Bills (7-1) 23-6 Vikings (6-2). "
        "Basketball: Wed NBA Cavs 115-107 Knicks (Harden 32, Mitchell 23; Brunson 27), Rockets 115-108 Warriors (Curry injured 1Q, Sengun 19, Lendeborg 25), Celtics 98-93 Raptors (-22 comeback, Tatum 24); tonight 4 NBA games. "
        "Golf: DP World Tour Championship Dubai R1 complete: Joost Luiten -5 (67), Jacob Skov Olesen -4 (68), Rory McIlroy -3 (69, T3 w/ Perez, De Leo, Schott, Laporta), Race leader Eugenio Chacarra E (72, T28). "
        "Tennis: Nitto ATP Finals Turin draw set (McEnroe: Zverev, Shelton, Fils, Jodar; Lendl: Alcaraz, Medvedev, Cobolli, Tiafoe); Stockholm QF tonight Taylor Fritz (7-5, 6-3 Norrie) vs Holger Rune (2-6, 6-1, 6-4 Kecmanovic). "
        "Formula 1: One week to Round 21 Las Vegas (19-21 Nov, 6.201 km Strip), 33 pts separate Verstappen (279) through Norris (246) behind Champion Antonelli (390); Mercedes 652, Ferrari 510, Red Bull 415, McLaren 398.\n"
    )
    check_dashes(new_clock_line, "AGENTS.md:Site clock")

    for i, line in enumerate(agents_lines):
        if "*   **Site clock:**" in line:
            agents_lines[i] = new_clock_line
            break

    with open(agents_path, "w", encoding="utf-8") as f:
        f.writelines(agents_lines)
    print("updated AGENTS.md")

