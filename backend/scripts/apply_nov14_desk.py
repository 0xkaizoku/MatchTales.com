#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Apply verified 14 November 2026 Saturday desk: Thu/Fri finals, Sat upcoming only, 6 stories, sports.ts, desk.json, AGENTS.md."""
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


def patch_featured(path, new_slugs):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    # Insert new featured slugs immediately after the LIVE finder.
    marker = "matches.find((m) => m.status === 'LIVE') ||"
    if marker not in text:
        raise SystemExit(f"LIVE marker missing in {path}")
    extra = "\n".join([f"  matches.find((m) => m.slug === '{s}') ||" for s in new_slugs])
    # Avoid duplicating if rerun: strip any of these slugs that already sit at the top.
    text = text.replace(
        marker,
        marker + "\n" + extra,
        1,
    )
    # De-dupe consecutive identical lines
    lines = text.splitlines(True)
    out = []
    seen_block = set()
    for line in lines:
        key = line.strip()
        if key.startswith("matches.find((m) => m.slug ===") and key in seen_block:
            continue
        if key.startswith("matches.find((m) => m.slug ==="):
            seen_block.add(key)
        else:
            seen_block = set() if "const featured" in key or "const liveMatch" in key else seen_block
        out.append(line)
    with open(path, "w", encoding="utf-8") as f:
        f.writelines(out)
    print("patched featured", path)


if __name__ == "__main__":
    for u in IMG.values():
        get_ok(u)

    # =========================================================================
    # MATCHES
    # =========================================================================

    dump(os.path.join(MATCHES, "uwcl-barcelona-vs-arsenal-md4-2026.json"), {
        "slug": "uwcl-barcelona-vs-arsenal-md4-2026",
        "headline": "UWCL MD4: Arsenal hold Barcelona 1-1 at Camp Nou as Maanum leads and Hansen equalises",
        "whyCareScore": 9.5,
        "whyCareReason": "Frida Maanum's 22nd-minute strike snaps Barcelona's perfect UWCL start before Caroline Graham Hansen's 59th-minute rocket shares the points at Spotify Camp Nou.",
        "teaser": "FINAL: Barcelona 1-1 Arsenal (Maanum 22', Graham Hansen 59'). Barcelona 10 pts (joint with Lyon); Arsenal 8 pts, fourth. Sunday: Spain vs England in Madrid.",
        "story": "Arsenal Women earned a battling 1-1 draw at Spotify Camp Nou on Thursday, 12 November, ending FC Barcelona Femeni's 100 percent start to the UEFA Women's Champions League league phase. Frida Maanum fired the visitors ahead in the 22nd minute against the run of play after Caitlin Foord was denied. Barcelona poured on 24 shots and nearly 70 percent possession, with Aitana Bonmati introduced from the bench, before Caroline Graham Hansen cut inside and finished in the 59th minute. Alessia Russo headed wide of an open goal early and later missed a late chance as Arsenal held on. The point lifts Arsenal to eight from four matches (fourth) while Barcelona sit on 10, level with Lyon. Men's Nations League Thursday also closed: England 2-1 Croatia, Italy 3-1 France, Czechia 0-2 Spain. Sunday 15 November, Spain host England at the Metropolitano (19:45 GMT) for Group A3 top spot. Premier League table is frozen on the international break: Arsenal 27, Brighton 22, Manchester City 21, Liverpool 18.",
        "stakes": "Arsenal climb into the UWCL top four on eight points while Barcelona share the league-phase lead on 10 with Lyon.",
        "rivalryAngle": "Lisbon final rematch ends level at Camp Nou: Maanum's smash-and-grab opener, Hansen's equaliser, and a Sunday Spain-England Nations League decider still to come.",
        "funFacts": [
            "Frida Maanum scored in the 22nd minute; Caroline Graham Hansen equalised in the 59th.",
            "Barcelona finished with 24 shots and about 70 percent possession but could not find a winner.",
            "Arsenal sit fourth on 8 points; Barcelona have 10, level with Lyon. Sunday: Spain vs England, 19:45 GMT, Metropolitano."
        ],
        "keyPlayers": [
            {"name": "Frida Maanum", "team": "Arsenal Women", "hook": "Scored the 22nd-minute opener against the run of play at Camp Nou."},
            {"name": "Caroline Graham Hansen", "team": "FC Barcelona Femeni", "hook": "Cut inside and finished in the 59th minute to salvage a point."},
            {"name": "Alessia Russo", "team": "Arsenal Women", "hook": "Missed an early open-goal header and a late chance as Arsenal held 1-1."}
        ],
        "headToHead": "Thursday 12 November 2026, 18:45 CET. Spotify Camp Nou, Barcelona. Final: Barcelona 1-1 Arsenal.",
        "tags": ["soccer", "uwcl", "barcelona", "arsenal", "camp-nou", "maanum", "graham-hansen"],
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
        "status": "FINISHED",
        "homeScore": 1,
        "awayScore": 1,
        "marquee": True,
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
        "resultSummary": "FINAL: Barcelona 1-1 Arsenal (Maanum 22', Graham Hansen 59'). Barca 10 pts, Arsenal 8. Sunday: Spain vs England 19:45 GMT.",
        "leaderboard": [],
        "tennisSets": [],
        "sources": [
            {"name": "ESPN: Barcelona 1-1 Arsenal UWCL 12 Nov 2026", "url": "https://www.espn.co.uk/football/match/_/gameId/401916986/arsenal-barcelona"},
            {"name": "UEFA Women's Champions League full-time report, Camp Nou MD4", "url": "https://www.uefa.com/womenschampionsleague/"}
        ]
    })

    dump(os.path.join(MATCHES, "england-vs-croatia-nations-league-2026.json"), {
        "slug": "england-vs-croatia-nations-league-2026",
        "headline": "Nations League: Kane penalty wins it 2-1 on his 126th England cap; Italy 3-1 France, Spain 2-0 Czechia",
        "whyCareScore": 9.6,
        "whyCareReason": "Harry Kane became England's most-capped men's player (126) and scored the 64th-minute penalty that sealed a Nations League quarterfinal place, 2-1 over Croatia.",
        "teaser": "FINAL: England 2-1 Croatia (Rogers 24', Kane 64' pen; Sucic 59'). Also Thu: Italy 3-1 France; Czechia 0-2 Spain. Sunday: Spain vs England, Metropolitano, 19:45 GMT.",
        "story": "Harry Kane marked a record 126th England appearance by converting a 64th-minute penalty as the Three Lions beat Croatia 2-1 at Wembley on Thursday, 12 November, and booked a UEFA Nations League quarterfinal place. Morgan Rogers bundled in the opener in the 24th minute after Jude Bellingham's volleyed delivery. Petar Sucic equalised in the 59th minute from close range. Four minutes later VAR awarded a penalty for Ivan Smolcic's shirt pull on Jarell Quansah, and Kane (92nd England goal) rolled it down the middle. England sit second in Group A3 on 12 points; Spain lead on 15 after beating 10-man Czechia 2-0 in Prague (Alex Baena 39' pen, Marc Pubill 90+6'; Ladislav Krejci sent off 69'). In Group A1, Italy came from behind to beat France 3-1 at San Siro: Michael Olise 10', Francesco Pio Esposito 26' and 75' pen, Davide Frattesi 63' (Sebastiano Esposito missed a 60th-minute penalty). Sunday 15 November, Spain host England at the Metropolitano (19:45 GMT) for first place. Premier League: Arsenal 27, Brighton 22, Manchester City 21.",
        "stakes": "England are into the quarterfinals on 12 points; Sunday's trip to Madrid decides whether Spain or England top Group A3.",
        "rivalryAngle": "Kane's record cap night at Wembley sets up a Sunday group-title shootout against world champions Spain in Madrid.",
        "funFacts": [
            "Harry Kane's 126th cap broke Peter Shilton's England men's appearance record; he scored his 92nd England goal from the spot.",
            "Italy 3-1 France at San Siro (Olise 10', Pio Esposito 26' and 75' pen, Frattesi 63') handed Zinedine Zidane a first defeat as France coach.",
            "Spain made it five from five with a 2-0 win in Prague (Baena pen, Pubill 90+6') and host England on Sunday."
        ],
        "keyPlayers": [
            {"name": "Harry Kane", "team": "England", "hook": "Record 126th cap and 64th-minute penalty winner in a 2-1 victory."},
            {"name": "Morgan Rogers", "team": "England", "hook": "Opened the scoring in the 24th minute at Wembley."},
            {"name": "Francesco Pio Esposito", "team": "Italy", "hook": "Scored twice (26', 75' pen) in Italy's 3-1 win over France."}
        ],
        "headToHead": "Thursday 12 November 2026, 19:45 GMT. Wembley Stadium, London. Final: England 2-1 Croatia.",
        "tags": ["soccer", "nations-league", "england", "croatia", "harry-kane", "italy", "france", "spain"],
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
        "status": "FINISHED",
        "homeScore": 2,
        "awayScore": 1,
        "marquee": True,
        "liveMinute": None,
        "image": IMG["soc"],
        "decidedBy": "90min",
        "homePen": None,
        "awayPen": None,
        "sport": "soccer",
        "competition": "nations-league-2026-27",
        "format": "team-match",
        "season": "2026-27",
        "roundLabel": "Nations League MD5 Final",
        "resultSummary": "FINAL: England 2-1 Croatia (Rogers 24', Kane 64' pen; Sucic 59'). Italy 3-1 France. Czechia 0-2 Spain. Sunday: Spain vs England 19:45 GMT.",
        "leaderboard": [],
        "tennisSets": [],
        "sources": [
            {"name": "England Football: England 2-1 Croatia match report", "url": "https://www.englandfootball.com/england/mens-senior-team/fixtures-results/2026-27/nations-league/england-v-croatia-uefa-nations-league-thursday-12-november-2026-match-centre"},
            {"name": "UEFA Nations League: Italy 3-1 France; Czechia 0-2 Spain", "url": "https://www.uefa.com/uefanationsleague/"}
        ]
    })

    dump(os.path.join(MATCHES, "commanders-at-giants-tnf-week10-2026.json"), {
        "slug": "commanders-at-giants-tnf-week10-2026",
        "headline": "TNF: Diggs 32-yard TD with 0:57 left lifts Commanders 24-21 over Giants at MetLife",
        "whyCareScore": 9.7,
        "whyCareReason": "Jayden Daniels (23 of 33, 249 yards, 3 TD, 2 INT) hit Stefon Diggs for a 32-yard go-ahead score with 57 seconds left, then Rasul Douglas intercepted J.J. McCarthy to seal it.",
        "teaser": "FINAL: Commanders 24, Giants 21. Quarters 0-10-7-7 / 0-7-7-7. WSH 3-5-1, NYG 5-3-1. Sunday: Patriots vs Lions in Munich, 9:30 a.m. ET FOX. No Saturday NFL game.",
        "story": "Jayden Daniels and the Washington Commanders stunned the New York Giants 24-21 on Thursday Night Football, 12 November, at MetLife Stadium (attendance 80,450). After a scoreless first quarter, Drew Stevens kicked a 46-yard field goal and Daniels found Ben Sinnott from a yard out just before halftime. Cam Skattebo scored twice on the ground (1 yard, 13 yards) and J.J. McCarthy hit Isaiah Likely for a 66-yard touchdown to put New York up 21-17 with 8:13 left. Daniels, who threw his first two interceptions of the season on consecutive fourth-quarter drives, answered with a 32-yard strike to Stefon Diggs (6 catches, 83 yards) with 57 seconds remaining. Rasul Douglas then intercepted McCarthy's deep ball intended for Malik Nabers. Daniels finished 23 of 33 for 249 yards and three touchdowns plus 11 rushes for 28 yards. McCarthy went 23 of 36 for 293 yards, one TD and one INT. Skattebo had 18 carries for 78 yards and two scores; Likely caught nine for 127. Washington is 3-5-1, two games behind the NFC East-leading Giants (5-3-1) with the head-to-head tiebreaker after October's 27-27 draw. Saturday 14 November has no NFL game. Sunday Week 10 opens in Munich: New England Patriots (5-4) vs Detroit Lions (6-2), 9:30 a.m. ET on FOX, then a 12-game domestic slate. Monday: Chargers at Ravens, 8:15 p.m. ET.",
        "stakes": "Washington stays alive in the NFC East at 3-5-1; the Giants fall to 5-3-1 heading into Sunday's Munich kickoff and a 12-game Week 10 slate.",
        "rivalryAngle": "Five weeks after a 27-27 overtime tie, Daniels and Diggs stole MetLife's White Out in the final minute.",
        "funFacts": [
            "Scoring: Stevens 46 FG; Skattebo 1-yd rush; Sinnott 1-yd pass; Skattebo 13-yd rush; Williams 31-yd pass; Likely 66-yd pass; Diggs 32-yd pass at 0:57.",
            "Jayden Daniels: 23/33, 249 yards, 3 TD, 2 INT. J.J. McCarthy: 23/36, 293 yards, 1 TD, 1 INT (Douglas).",
            "No NFL game Saturday 14 Nov. Next: Patriots vs Lions, Munich, Sunday 9:30 a.m. ET FOX."
        ],
        "keyPlayers": [
            {"name": "Jayden Daniels", "team": "Washington Commanders", "hook": "23 of 33, 249 yards, three TDs including the 32-yard winner to Diggs."},
            {"name": "Stefon Diggs", "team": "Washington Commanders", "hook": "Six catches, 83 yards, 32-yard go-ahead TD with 57 seconds left."},
            {"name": "Cam Skattebo", "team": "New York Giants", "hook": "18 carries, 78 yards, rushing TDs of 1 and 13 yards in his return."}
        ],
        "headToHead": "Thursday 12 November 2026, 8:15 p.m. ET. MetLife Stadium, East Rutherford. Final: Commanders 24, Giants 21.",
        "tags": ["football", "nfl", "commanders", "giants", "jayden-daniels", "stefon-diggs", "thursday-night-football"],
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
        "status": "FINISHED",
        "homeScore": 21,
        "awayScore": 24,
        "marquee": True,
        "liveMinute": None,
        "image": IMG["nfl"],
        "decidedBy": "regulation",
        "homePen": None,
        "awayPen": None,
        "sport": "football",
        "competition": "nfl-2026",
        "format": "team-match",
        "season": "2026",
        "roundLabel": "TNF Final",
        "resultSummary": "FINAL: Commanders 24, Giants 21. Daniels 3 TD, Diggs 32-yd winner, Douglas INT. WSH 3-5-1, NYG 5-3-1. Next: Sunday Munich Patriots vs Lions 9:30 a.m. ET.",
        "leaderboard": [],
        "tennisSets": [],
        "sources": [
            {"name": "ESPN: Commanders 24-21 Giants box score and recap", "url": "https://www.espn.com/nfl/game/_/gameId/401873052/commanders-giants"},
            {"name": "Pro-Football-Reference: Commanders at Giants November 12 2026", "url": "https://www.pro-football-reference.com/boxscores/202611120nyg.htm"}
        ]
    })

    dump(os.path.join(MATCHES, "nba-spurs-vs-warriors-nov13-2026.json"), {
        "slug": "nba-spurs-vs-warriors-nov13-2026",
        "headline": "NBA Cup: Castle scores 32 as Spurs rout Curry-less Warriors 123-85 for 11th straight win",
        "whyCareScore": 9.4,
        "whyCareReason": "Stephon Castle's season-high 32 points and Victor Wembanyama's 12-12-6 power San Antonio to 11-2 while Golden State plays without Stephen Curry (oblique tear).",
        "teaser": "FINAL Fri: Spurs 123, Warriors 85 (Castle 32, Wemby 12/12/6; Cryer 20). Also Thu: Cunningham 52, Pistons 144-140 2OT. Tonight Sat: 5 NBA games, none live as final.",
        "story": "The San Antonio Spurs demolished the Golden State Warriors 123-85 on Friday, 13 November, at Frost Bank Center on Prime Video, stretching their winning streak to 11 games and improving to 11-2 (unbeaten in NBA Cup group play). Stephon Castle scored a season-high 32 points (12 of 18, 5 of 8 from three) with six assists in 25 minutes. Victor Wembanyama added 12 points, 12 rebounds, six assists and two blocks. Keldon Johnson scored 18 off the bench. Golden State, missing Stephen Curry for at least two weeks after a right oblique tear suffered Wednesday in Houston, managed 14 first-quarter points. L.J. Cryer led the Warriors with 20; Charles Bassey had 11. Thursday's board still stands as the other headline: Cade Cunningham scored 52 points with 11 assists and no turnovers as Detroit beat Washington 144-140 in double overtime. Friday also: Heat 133-121 Cavaliers (Giannis 37), Pacers 106-104 Knicks (Brunson 33), Magic 107-99 Bucks (Wagner 35), Bulls 125-117 OT Hawks (Powell 33), Grizzlies 142-111 Pelicans, Rockets 125-118 Jazz (Sengun 43), Trail Blazers 120-107 Kings, Clippers 113-112 Thunder. Saturday 14 November (upcoming, unpublished as final): Nuggets at Pelicans 7:00 p.m. ET, Mavericks at Cavaliers 7:30, Pistons at Heat, Nets at Grizzlies, Bulls at Timberwolves (all 8:00).",
        "stakes": "San Antonio sits 11-2 with an 11-game streak; Golden State is 8-5 without Curry for at least two weeks.",
        "rivalryAngle": "Castle's 32-point explosion met a Curry-less Warriors side that scored 33 points in a first half.",
        "funFacts": [
            "Stephon Castle: 32 points on 12-of-18 shooting, 5-of-8 threes, six assists in 25 minutes.",
            "Spurs led 38-14 after one quarter and 63-33 at halftime in an NBA Cup group game.",
            "Thursday: Cade Cunningham 52 points, Pistons 144-140 2OT at Washington. Saturday: five upcoming NBA games."
        ],
        "keyPlayers": [
            {"name": "Stephon Castle", "team": "San Antonio Spurs", "hook": "Season-high 32 points (12-18 FG) in a 123-85 NBA Cup blowout."},
            {"name": "Victor Wembanyama", "team": "San Antonio Spurs", "hook": "12 points, 12 rebounds, six assists as San Antonio went to 11-2."},
            {"name": "Cade Cunningham", "team": "Detroit Pistons", "hook": "Thursday: 52 points, 11 assists, zero turnovers in a 144-140 2OT win."}
        ],
        "headToHead": "Friday 13 November 2026. Frost Bank Center, San Antonio. Final: Spurs 123, Warriors 85.",
        "tags": ["basketball", "nba", "spurs", "warriors", "stephon-castle", "wembanyama", "nba-cup"],
        "home": "San Antonio Spurs",
        "away": "Golden State Warriors",
        "homeCode": "USA",
        "awayCode": "USA",
        "homeFlag": "us",
        "awayFlag": "us",
        "group": "NBA Cup Group Play",
        "matchday": 13,
        "date": "2026-11-13",
        "time": "21:30",
        "venue": "Frost Bank Center",
        "city": "San Antonio",
        "status": "FINISHED",
        "homeScore": 123,
        "awayScore": 85,
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
        "roundLabel": "NBA Cup Friday",
        "resultSummary": "FINAL: Spurs 123, Warriors 85. Castle 32, Wemby 12/12/6. Spurs 11-2, 11-game streak. Thu: Cunningham 52, DET 144-140 2OT WAS. Sat: 5 games upcoming.",
        "leaderboard": [],
        "tennisSets": [],
        "sources": [
            {"name": "ESPN: Spurs 123-85 Warriors recap, Castle 32", "url": "https://www.espn.com/nba/recap?gameId=401909302"},
            {"name": "NBA.com: Warriors at Spurs November 13 2026 box score", "url": "https://www.nba.com/game/gsw-vs-sas-0022600040/box-score"}
        ]
    })

    dump(os.path.join(MATCHES, "atp-stockholm-open-2026-fritz-vs-rune-qf.json"), {
        "slug": "atp-stockholm-open-2026-fritz-vs-rune-qf",
        "headline": "Stockholm: Fritz advances by walkover over Rune, then beats Musetti 6-4, 6-2 to reach today's final",
        "whyCareScore": 8.8,
        "whyCareReason": "Taylor Fritz reached the Bybit Stockholm Open final in 63 minutes over Lorenzo Musetti after Holger Rune withdrew from Thursday's quarterfinal.",
        "teaser": "QF: Fritz walkover Rune. SF Fri: Fritz d Musetti 6-4, 6-2; Tirante d Tabilo 7-5, 7-6 (1). TODAY Final: Fritz vs Thiago Agustin Tirante. Turin starts Sunday.",
        "story": "Taylor Fritz is into the Bybit Stockholm Open final on Saturday, 14 November, at Kungliga Tennishallen. The top seed advanced through Thursday's quarterfinal when Holger Rune withdrew (walkover), then needed only 63 minutes on Friday to beat third seed Lorenzo Musetti 6-4, 6-2. In the other semifinal, Argentina's Thiago Agustin Tirante (ATP 51) reached the first ATP Tour final of his career by defeating fourth seed Alejandro Tabilo 7-5, 7-6 (1). Thursday's other quarters: Musetti d Ugo Humbert 7-6 (5), 3-6, 6-4; Tirante d Aleksandr Shevchenko 7-6 (5), 6-7 (5), 6-3; Tabilo d Alex Michelsen 7-5, 7-6 (2). The final is today. The Nitto ATP Finals in Turin open Sunday 15 November at Inalpi Arena: Alexander Zverev vs Rafael Jodar (not before 2:00 p.m. CET) and Ben Shelton vs Arthur Fils (not before 8:30 p.m.); Carlos Alcaraz vs Frances Tiafoe and Daniil Medvedev vs Flavio Cobolli play Monday.",
        "stakes": "Fritz chases a sixth indoor ATP final of 2026 against first-time finalist Tirante, one day before Turin group play begins.",
        "rivalryAngle": "A walkover over Rune and a 63-minute dismissal of Musetti put Fritz across from Tirante's maiden tour final.",
        "funFacts": [
            "Holger Rune withdrew from the Thursday quarterfinal; Fritz advanced by walkover.",
            "Friday SF: Fritz d Musetti 6-4, 6-2 in 63 minutes; Tirante d Tabilo 7-5, 7-6 (1).",
            "Turin Sunday: Zverev vs Jodar (14:00 CET), Shelton vs Fils (20:30 CET)."
        ],
        "keyPlayers": [
            {"name": "Taylor Fritz", "team": "United States", "hook": "Walkover vs Rune, then 6-4, 6-2 over Musetti into today's Stockholm final."},
            {"name": "Thiago Agustin Tirante", "team": "Argentina", "hook": "First ATP Tour final after 7-5, 7-6 (1) over Alejandro Tabilo."},
            {"name": "Lorenzo Musetti", "team": "Italy", "hook": "Beaten 6-4, 6-2 in Friday's semifinal in 63 minutes."}
        ],
        "headToHead": "Friday 13 November 2026 SF. Kungliga Tennishallen, Stockholm. Fritz d Musetti 6-4, 6-2.",
        "tags": ["tennis", "atp", "stockholm-open", "taylor-fritz", "tirante", "musetti"],
        "home": "Taylor Fritz",
        "away": "Lorenzo Musetti",
        "homeCode": "USA",
        "awayCode": "ITA",
        "homeFlag": "us",
        "awayFlag": "it",
        "group": "Stockholm Open SF",
        "matchday": 5,
        "date": "2026-11-13",
        "time": "16:00",
        "venue": "Kungliga Tennishallen",
        "city": "Stockholm",
        "status": "FINISHED",
        "homeScore": 2,
        "awayScore": 0,
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
        "roundLabel": "Stockholm SF Final",
        "resultSummary": "SF: Fritz d Musetti 6-4, 6-2; Tirante d Tabilo 7-5, 7-6 (1). QF: Fritz walkover Rune. TODAY F: Fritz vs Tirante.",
        "leaderboard": [],
        "tennisSets": [
            {"p1": "6", "p2": "4"},
            {"p1": "6", "p2": "2"}
        ],
        "sources": [
            {"name": "ATP Tour: Stockholm results, Fritz d Musetti 6-4, 6-2", "url": "https://www.atptour.com/en/scores/current/stockholm/429/results"},
            {"name": "ATP Tour: Nitto ATP Finals 2026 Sunday-Monday order of play", "url": "https://www.nittoatpfinals.com/en/news/nitto-atp-finals-2026-schedule-sunday-monday"}
        ]
    })

    dump(os.path.join(MATCHES, "atp-stockholm-open-2026-fritz-vs-tirante-final.json"), {
        "slug": "atp-stockholm-open-2026-fritz-vs-tirante-final",
        "headline": "Stockholm Final Today: Taylor Fritz faces first-time ATP finalist Thiago Agustin Tirante",
        "whyCareScore": 8.7,
        "whyCareReason": "Top seed Fritz, into a sixth indoor final of 2026, meets Argentina's Tirante in the Bybit Stockholm Open championship match. No final score published.",
        "teaser": "TODAY Final (Sat 14 Nov, Kungliga Tennishallen): Taylor Fritz vs Thiago Agustin Tirante. Turin round robin starts Sunday 15 Nov.",
        "story": "The Bybit Stockholm Open championship match is today, Saturday 14 November, at Kungliga Tennishallen. Top seed Taylor Fritz (walkover vs Holger Rune in the quarterfinals, 6-4, 6-2 vs Lorenzo Musetti in the semifinals) meets Thiago Agustin Tirante, who is in his first ATP Tour final after beating Alejandro Tabilo 7-5, 7-6 (1). The match is upcoming. Do not treat any in-progress score as final. The Nitto ATP Finals open Sunday in Turin: Zverev vs Jodar not before 2:00 p.m. CET, Shelton vs Fils not before 8:30 p.m. CET.",
        "stakes": "Fritz seeks his first Stockholm title; Tirante plays for a maiden ATP trophy the day before Turin begins.",
        "rivalryAngle": "American top seed versus Argentine first-time finalist on indoor hard in Sweden.",
        "funFacts": [
            "Fritz reached the final via a Rune walkover and a 6-4, 6-2 win over Musetti.",
            "Tirante (ATP 51) is in his first tour final after 7-5, 7-6 (1) over Tabilo.",
            "Turin starts Sunday 15 November at Inalpi Arena."
        ],
        "keyPlayers": [
            {"name": "Taylor Fritz", "team": "United States", "hook": "Top seed into the Stockholm final; sixth indoor final of 2026."},
            {"name": "Thiago Agustin Tirante", "team": "Argentina", "hook": "First ATP Tour final of his career."}
        ],
        "headToHead": "Saturday 14 November 2026. Kungliga Tennishallen, Stockholm. Final upcoming. No score.",
        "tags": ["tennis", "atp", "stockholm-open", "taylor-fritz", "tirante", "final"],
        "home": "Taylor Fritz",
        "away": "Thiago Agustin Tirante",
        "homeCode": "USA",
        "awayCode": "ARG",
        "homeFlag": "us",
        "awayFlag": "ar",
        "group": "Stockholm Open Final",
        "matchday": 6,
        "date": "2026-11-14",
        "time": "13:00",
        "venue": "Kungliga Tennishallen",
        "city": "Stockholm",
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
        "competition": "atp-250-stockholm-2026",
        "format": "singles",
        "season": "2026",
        "roundLabel": "Stockholm Final Today",
        "resultSummary": "TODAY Final: Taylor Fritz vs Thiago Agustin Tirante. No score. Turin starts Sunday.",
        "leaderboard": [],
        "tennisSets": [],
        "sources": [
            {"name": "ATP Tour: Stockholm draw and Saturday final", "url": "https://www.atptour.com/en/scores/current/stockholm/429/results"},
            {"name": "Nitto ATP Finals: Sunday 15 November order of play", "url": "https://www.nittoatpfinals.com/en/news/nitto-atp-finals-2026-schedule-sunday-monday"}
        ]
    })

    dump(os.path.join(MATCHES, "atp-nitto-finals-2026-turin-draw.json"), {
        "slug": "atp-nitto-finals-2026-turin-draw",
        "headline": "Nitto ATP Finals open Sunday in Turin: Zverev vs Jodar, then Shelton vs Fils",
        "whyCareScore": 9.2,
        "whyCareReason": "Round-robin play at Inalpi Arena starts Sunday 15 November with Alexander Zverev against Rafael Jodar and Ben Shelton against Arthur Fils. No Turin match has been played.",
        "teaser": "SUNDAY Turin (15 Nov): Zverev vs Jodar (not before 14:00 CET); Shelton vs Fils (not before 20:30 CET). Monday: Alcaraz vs Tiafoe; Medvedev vs Cobolli. Groups unchanged.",
        "story": "The 2026 Nitto ATP Finals still start Sunday, 15 November, at Inalpi Arena in Turin (15-22 November). Thursday's draw is unchanged: John McEnroe Group is Alexander Zverev (1), Ben Shelton (3), Arthur Fils (6) and Rafael Jodar (8). Ivan Lendl Group is Carlos Alcaraz (2), Daniil Medvedev (4), Flavio Cobolli (5) and Frances Tiafoe (7). Sunday order of play: doubles from 11:30 a.m. CET, then Zverev vs Jodar not before 2:00 p.m., evening doubles, then Shelton vs Fils not before 8:30 p.m. Monday: Alcaraz vs Tiafoe not before 2:00 p.m., Medvedev vs Cobolli not before 8:30 p.m. No Turin singles match has been played. In Stockholm today, Fritz meets Tirante in the final.",
        "stakes": "Eight season finalists open round-robin play Sunday; first matches are unpublished.",
        "rivalryAngle": "Zverev-Jodar and Shelton-Fils open McEnroe Group on Sunday; Alcaraz-Tiafoe and Medvedev-Cobolli wait until Monday.",
        "funFacts": [
            "McEnroe Group: Zverev (1), Shelton (3), Fils (6), Jodar (8).",
            "Lendl Group: Alcaraz (2), Medvedev (4), Cobolli (5), Tiafoe (7).",
            "Sunday first singles: Zverev vs Jodar, not before 14:00 CET. No result yet."
        ],
        "keyPlayers": [
            {"name": "Alexander Zverev", "team": "Germany", "hook": "Top seed opens Sunday against Rafael Jodar, not before 2:00 p.m. CET."},
            {"name": "Carlos Alcaraz", "team": "Spain", "hook": "No. 2 seed plays Frances Tiafoe on Monday in the Lendl Group."},
            {"name": "Ben Shelton", "team": "United States", "hook": "Sunday night McEnroe Group match against Arthur Fils, not before 8:30 p.m. CET."}
        ],
        "headToHead": "Tournament dates 15-22 November 2026, Inalpi Arena, Turin. First singles Sunday. No score.",
        "tags": ["tennis", "atp", "nitto-atp-finals", "turin", "zverev", "alcaraz", "jodar", "shelton"],
        "home": "Alexander Zverev",
        "away": "Rafael Jodar",
        "homeCode": "GER",
        "awayCode": "ESP",
        "homeFlag": "de",
        "awayFlag": "es",
        "group": "Nitto ATP Finals McEnroe",
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
        "roundLabel": "Turin Sunday Opener",
        "resultSummary": "SUNDAY: Zverev vs Jodar (14:00 CET), Shelton vs Fils (20:30 CET). Groups unchanged. No Turin score.",
        "leaderboard": [
            {"pos": "McEnroe", "name": "Alexander Zverev (1)", "score": "Top Seed", "note": "Opens Sun vs Jodar"},
            {"pos": "McEnroe", "name": "Ben Shelton (3)", "score": "No. 3 Seed", "note": "Sun night vs Fils"},
            {"pos": "McEnroe", "name": "Arthur Fils (6)", "score": "No. 6 Seed", "note": "John McEnroe Group"},
            {"pos": "McEnroe", "name": "Rafael Jodar (8)", "score": "No. 8 Seed", "note": "Opens vs Zverev"},
            {"pos": "Lendl", "name": "Carlos Alcaraz (2)", "score": "No. 2 Seed", "note": "Monday vs Tiafoe"},
            {"pos": "Lendl", "name": "Daniil Medvedev (4)", "score": "No. 4 Seed", "note": "Monday vs Cobolli"},
            {"pos": "Lendl", "name": "Flavio Cobolli (5)", "score": "No. 5 Seed", "note": "Ivan Lendl Group"},
            {"pos": "Lendl", "name": "Frances Tiafoe (7)", "score": "No. 7 Seed", "note": "Monday vs Alcaraz"}
        ],
        "tennisSets": [],
        "sources": [
            {"name": "Nitto ATP Finals: Sunday and Monday 2026 schedule", "url": "https://www.nittoatpfinals.com/en/news/nitto-atp-finals-2026-schedule-sunday-monday"},
            {"name": "ATP Tour: 2026 Turin draw and format", "url": "https://www.atptour.com/en/news/nitto-atp-finals-2026-history-draw-schedule"}
        ]
    })

    dump(os.path.join(MATCHES, "dp-world-tour-championship-dubai-2026.json"), {
        "slug": "dp-world-tour-championship-dubai-2026",
        "headline": "Dubai R2 complete: McIlroy and Hatton share the lead on 139 (-5); R3 in progress unpublished",
        "whyCareScore": 9.4,
        "whyCareReason": "Associated Press Friday totals put Rory McIlroy (69-70) and Tyrrell Hatton (70-69) at 139, one clear of Joost Luiten and Kristoffer Reitan. Round 3 is not posted as final.",
        "teaser": "R2 FINAL (AP, Earth Course): T1 McIlroy 69-70=139 (-5), Hatton 70-69=139; T3 Luiten 67-73=140, Reitan 70-70=140. Chacarra 72-71=143 (T11). R3 Saturday in progress, no final.",
        "story": "The DP World Tour Championship second round closed Friday, 13 November, at the Earth Course, Jumeirah Golf Estates, Dubai (par 72, 7,706 yards, $10 million purse). Associated Press posted complete 36-hole totals: Rory McIlroy 69-70 for 139 (five under) shares the lead with Tyrrell Hatton 70-69. Joost Luiten, Thursday's 67 leader, carded 73 for 140 alongside Kristoffer Reitan (70-70). A shot further back at 141: Mikael Lindberg 72-69, Victor Perez 69-72, Freddy Schott 69-72. Jon Rahm is 71-71=142 with David Puig and Jayden Schaper. Race to Dubai leader Eugenio Lopez-Chacarra shot 72-71 for 143, tied for 11th with Francesco Laporta, Adrian Meronk and Jacob Skov Olesen (68-75). Round 3 is underway Saturday 14 November and is not published as a final. Sunday is Round 4.",
        "stakes": "McIlroy and Hatton take a one-shot 36-hole lead into the weekend while Chacarra sits four back on 143.",
        "rivalryAngle": "McIlroy's 139 matches Hatton at the top; Luiten dropped from the R1 lead with a 73; Chacarra is four off the pace.",
        "funFacts": [
            "AP Friday: McIlroy 69-70=139, Hatton 70-69=139, both five under par.",
            "Luiten 67-73=140 after the first-round lead; Olesen 68-75=143.",
            "Round 3 Saturday is live and unpublished as a final."
        ],
        "keyPlayers": [
            {"name": "Rory McIlroy", "team": "Northern Ireland", "hook": "69-70=139, shares the 36-hole lead at five under."},
            {"name": "Tyrrell Hatton", "team": "England", "hook": "70-69=139 to join McIlroy at the top after 36 holes."},
            {"name": "Eugenio Chacarra", "team": "Spain", "hook": "Race leader 72-71=143, four shots back, tied for 11th."}
        ],
        "headToHead": "Friday 13 November 2026, Round 2 complete. Earth Course, Jumeirah Golf Estates, Dubai. R3 Saturday unpublished.",
        "tags": ["golf", "dp-world-tour", "dubai", "rory-mcilroy", "tyrrell-hatton", "joost-luiten", "eugenio-chacarra"],
        "home": "Rory McIlroy",
        "away": "Tyrrell Hatton",
        "homeCode": "ENG",
        "awayCode": "ENG",
        "homeFlag": "gb-eng",
        "awayFlag": "gb-eng",
        "group": "DP World Tour Finale",
        "matchday": 2,
        "date": "2026-11-13",
        "time": "12:40",
        "venue": "Earth Course, Jumeirah Golf Estates",
        "city": "Dubai",
        "status": "FINISHED",
        "homeScore": "-5 (139)",
        "awayScore": "-5 (139)",
        "marquee": True,
        "liveMinute": None,
        "image": IMG["golf"],
        "decidedBy": "round2",
        "homePen": None,
        "awayPen": None,
        "sport": "golf",
        "competition": "dp-world-tour-2026",
        "format": "leaderboard",
        "season": "2026",
        "roundLabel": "Round 2 Complete",
        "resultSummary": "R2 DUBAI (AP): T1 McIlroy & Hatton -5 (139); T3 Luiten & Reitan -4 (140); Chacarra -1 (143, T11). R3 Saturday in progress, unpublished.",
        "leaderboard": [
            {"pos": "T1", "name": "Rory McIlroy", "score": "-5 (69-70=139)", "note": "Shares 36-hole lead"},
            {"pos": "T1", "name": "Tyrrell Hatton", "score": "-5 (70-69=139)", "note": "Shares 36-hole lead"},
            {"pos": "T3", "name": "Joost Luiten", "score": "-4 (67-73=140)", "note": "R1 leader; Friday 73"},
            {"pos": "T3", "name": "Kristoffer Reitan", "score": "-4 (70-70=140)", "note": "Two even-par 70s"},
            {"pos": "T5", "name": "Mikael Lindberg", "score": "-3 (72-69=141)", "note": "Friday 69"},
            {"pos": "T5", "name": "Victor Perez", "score": "-3 (69-72=141)", "note": "T5 after 36"},
            {"pos": "T5", "name": "Freddy Schott", "score": "-3 (69-72=141)", "note": "T5 after 36"},
            {"pos": "T11", "name": "Eugenio Chacarra", "score": "-1 (72-71=143)", "note": "Race to Dubai leader"}
        ],
        "tennisSets": [],
        "sources": [
            {"name": "Associated Press via WTOP: DP World Tour Championship second-round scores", "url": "https://wtop.com/sports/2026/11/dp-world-tour-championship-scores-2/"},
            {"name": "DP World Tour: Championship Dubai leaderboard", "url": "https://www.europeantour.com/dpworld-tour/dp-world-tour-championship-dubai-2026/leaderboard"}
        ]
    })

    dump(os.path.join(MATCHES, "las-vegas-gp-strip-2026.json"), {
        "slug": "las-vegas-gp-strip-2026",
        "headline": "Five days to Round 21 Las Vegas: 33 points still split Verstappen to Norris behind Champion Antonelli",
        "whyCareScore": 9.0,
        "whyCareReason": "No 2026 Las Vegas Grand Prix has been run. Standings remain post-Sao Paulo: Antonelli 390, Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246.",
        "teaser": "ROUND 21 NEXT (19-21 Nov, 6.201 km Strip): Antonelli 390 Champion; Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246. Mercedes 652, Ferrari 510, Red Bull 415, McLaren 398. No race result.",
        "story": "Saturday 14 November sits five days before Round 21 of the 2026 FIA Formula One World Championship on the 6.201-kilometre Las Vegas Strip Circuit (19-21 November, Saturday night Grand Prix 21 November). Both titles remain settled after Interlagos: Kimi Antonelli is Drivers Champion on 390 points, Mercedes Constructors Champion on 652. The fight for second is unchanged because no race has been held since Sao Paulo: Max Verstappen 279, George Russell 262, Lewis Hamilton 261, Charles Leclerc 249, Lando Norris 246. Constructors behind Mercedes: Ferrari 510, Red Bull 415, McLaren 398. Qatar follows on 29 November and Abu Dhabi on 6 December. Do not publish a Las Vegas race result, pole, or practice time.",
        "stakes": "Thirty-three points still divide Drivers P2 through P6 heading into next week's night race on the Strip.",
        "rivalryAngle": "Verstappen's 279-point hold on P2 remains 17 clear of Russell and 33 clear of Norris until cars run in Nevada.",
        "funFacts": [
            "Las Vegas is Round 21, 19-21 November, 6.201 km Strip Circuit, GP Saturday night 21 November.",
            "Standings frozen post-Sao Paulo: Antonelli 390, Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246.",
            "No 2026 Las Vegas FP, qualifying, or race result exists yet."
        ],
        "keyPlayers": [
            {"name": "Max Verstappen", "team": "Red Bull", "hook": "Holds P2 on 279 points with five days until Las Vegas."},
            {"name": "George Russell", "team": "Mercedes", "hook": "262 points, one ahead of Hamilton, 17 behind Verstappen."},
            {"name": "Lando Norris", "team": "McLaren", "hook": "246 points after winning in Sao Paulo; 33 behind Verstappen."}
        ],
        "headToHead": "19-21 November 2026 (Round 21). 6.201 km Las Vegas Strip Circuit. Upcoming. No score.",
        "tags": ["f1", "formula-1", "las-vegas-gp", "verstappen", "norris", "antonelli", "mercedes"],
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
        "resultSummary": "ROUND 21 VEGAS (19-21 Nov): Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246 (Antonelli Champion 390; Mercedes 652). No race result.",
        "leaderboard": [
            {"pos": "1", "name": "Kimi Antonelli (Mercedes)", "score": "390 pts", "note": "2026 Drivers Champion"},
            {"pos": "2", "name": "Max Verstappen (Red Bull)", "score": "279 pts", "note": "P2 entering Round 21"},
            {"pos": "3", "name": "George Russell (Mercedes)", "score": "262 pts", "note": "+1 over Hamilton"},
            {"pos": "4", "name": "Lewis Hamilton (Ferrari)", "score": "261 pts", "note": "One behind Russell"},
            {"pos": "5", "name": "Charles Leclerc (Ferrari)", "score": "249 pts", "note": "Ferrari 510 Constructors"},
            {"pos": "6", "name": "Lando Norris (McLaren)", "score": "246 pts", "note": "Sao Paulo winner; McLaren 398"}
        ],
        "tennisSets": [],
        "sources": [
            {"name": "Formula1.com: 2026 Heineken Las Vegas Grand Prix Round 21", "url": "https://www.formula1.com/en/racing/2026/las-vegas"},
            {"name": "FIA / Formula1.com: 2026 Drivers Championship standings", "url": "https://www.formula1.com/en/results/2026/drivers"}
        ]
    })

    # =========================================================================
    # 6 Why Care stories
    # =========================================================================
    stories_data = [
        {
            "slug": "uwcl-barcelona-arsenal-1-1-nations-league-thursday-2026",
            "title": "Arsenal hold Barcelona 1-1 at Camp Nou; Kane penalty sends England through 2-1",
            "subtitle": "Maanum and Graham Hansen share UWCL spoils while Kane's record 126th cap night sets up Sunday's Spain-England group decider in Madrid.",
            "category": "Match Report",
            "excerpt": "Frida Maanum's 22nd-minute opener and Caroline Graham Hansen's 59th-minute equaliser finish 1-1. England beat Croatia 2-1, Italy 3-1 France, Spain 2-0 Czechia.",
            "image": IMG["soc"],
            "readingTime": 4,
            "pubDate": "2026-11-14",
            "sport": "soccer",
            "competition": "uwcl-2026-27",
            "relatedSlug": "uwcl-barcelona-vs-arsenal-md4-2026",
            "sources": [
                {"name": "ESPN: Barcelona 1-1 Arsenal UWCL", "url": "https://www.espn.co.uk/football/match/_/gameId/401916986/arsenal-barcelona"},
                {"name": "England Football: England 2-1 Croatia report", "url": "https://www.englandfootball.com/england/mens-senior-team/fixtures-results/2026-27/nations-league/england-v-croatia-uefa-nations-league-thursday-12-november-2026-match-centre"}
            ],
            "content": """Arsenal Women left Spotify Camp Nou with a 1-1 draw on Thursday, 12 November, snapping FC Barcelona Femeni's perfect UWCL start. Frida Maanum scored in the 22nd minute after Caitlin Foord was denied. Barcelona piled up 24 shots and nearly 70 percent of the ball, then Caroline Graham Hansen cut inside and finished in the 59th minute. Alessia Russo headed wide of an open goal early. Arsenal sit fourth on eight points; Barcelona have 10, level with Lyon.

Men's Nations League Matchday 5 delivered three finals the same night. At Wembley, Morgan Rogers scored in the 24th minute and Harry Kane converted a 64th-minute penalty on his record 126th England cap after Petar Sucic had equalised (59'). England are into the quarterfinals on 12 points. Italy came from behind to beat France 3-1 at San Siro (Olise 10', Pio Esposito 26' and 75' pen, Frattesi 63'). Spain beat 10-man Czechia 2-0 in Prague (Baena 39' pen, Pubill 90+6').

Sunday 15 November, Spain host England at the Metropolitano (19:45 GMT) for Group A3 first place. The Premier League table is unchanged on the international break: Arsenal 27, Brighton 22, Manchester City 21, Liverpool 18."""
        },
        {
            "slug": "nfl-week10-tnf-commanders-24-21-giants-diggs-2026",
            "title": "TNF: Diggs 32-yard score with 0:57 left lifts Commanders 24-21 over Giants",
            "subtitle": "Jayden Daniels threw three touchdowns, Rasul Douglas sealed it with an interception, and Saturday has no NFL game before Sunday's Munich kickoff.",
            "category": "Match Report",
            "excerpt": "Commanders 24, Giants 21 at MetLife. Daniels 23 of 33, 249 yards, 3 TD. Skattebo two rushing TDs. Washington 3-5-1, New York 5-3-1. Next: Patriots vs Lions, Munich, 9:30 a.m. ET Sunday.",
            "image": IMG["nfl"],
            "readingTime": 4,
            "pubDate": "2026-11-14",
            "sport": "football",
            "competition": "nfl-2026",
            "relatedSlug": "commanders-at-giants-tnf-week10-2026",
            "sources": [
                {"name": "ESPN: Commanders 24-21 Giants recap", "url": "https://www.espn.com/nfl/recap?gameId=401873052"},
                {"name": "NFL.com: What we learned from Washington's 24-21 win", "url": "https://www.nfl.com/news/commanders-giants-on-thursday-night-football-what-we-learned-from-washington-s-24-21-win"}
            ],
            "content": """Jayden Daniels found Stefon Diggs for a 32-yard touchdown with 57 seconds left as the Washington Commanders beat the New York Giants 24-21 on Thursday Night Football at MetLife Stadium (80,450). Daniels finished 23 of 33 for 249 yards and three scores after throwing his first two interceptions of the season on consecutive fourth-quarter drives. Rasul Douglas then intercepted J.J. McCarthy's deep ball to Malik Nabers.

Cam Skattebo scored twice on the ground (1 yard, 13 yards) and McCarthy hit Isaiah Likely for a 66-yard touchdown that made it 21-17 with 8:13 remaining. McCarthy went 23 of 36 for 293 yards. Likely caught nine for 127. Washington is 3-5-1; the Giants are 5-3-1.

Saturday 14 November has no NFL game. Week 10 continues Sunday in Munich: New England Patriots (5-4) vs Detroit Lions (6-2) at 9:30 a.m. ET on FOX, then a 12-game domestic slate. Monday Night Football is Chargers at Ravens, 8:15 p.m. ET. Do not publish Sunday scores."""
        },
        {
            "slug": "nba-spurs-11th-straight-castle-32-warriors-2026",
            "title": "Castle scores 32 as Spurs blow out Warriors 123-85 for an 11th straight win",
            "subtitle": "San Antonio is 11-2 without allowing Golden State a foothold, a night after Cade Cunningham's 52-point double-overtime classic in Washington.",
            "category": "Match Report",
            "excerpt": "Spurs 123, Warriors 85. Castle 32, Wembanyama 12/12/6. Curry out at least two weeks (oblique). Thursday: Cunningham 52, Pistons 144-140 2OT. Saturday: five NBA games upcoming.",
            "image": IMG["nba"],
            "readingTime": 4,
            "pubDate": "2026-11-14",
            "sport": "basketball",
            "competition": "nba-2026-27",
            "relatedSlug": "nba-spurs-vs-warriors-nov13-2026",
            "sources": [
                {"name": "ESPN: Spurs 123-85 Warriors, Castle 32", "url": "https://www.espn.com/nba/recap?gameId=401909302"},
                {"name": "ESPN NBA scoreboard November 13 2026", "url": "https://www.espn.com/nba/scoreboard/_/date/20261113"}
            ],
            "content": """Stephon Castle scored a season-high 32 points (12 of 18, five threes) as the San Antonio Spurs routed the Golden State Warriors 123-85 on Friday night at Frost Bank Center, their 11th straight win and a 11-2 start. Victor Wembanyama posted 12 points, 12 rebounds and six assists. The Spurs led 38-14 after one quarter. Stephen Curry is out at least two weeks with a right oblique tear from Wednesday in Houston. L.J. Cryer led Golden State with 20.

Thursday's other board-setter: Cade Cunningham scored 52 points with 11 assists and no turnovers as Detroit beat Washington 144-140 in double overtime. Friday also included Miami 133-121 Cleveland (Giannis 37), Indiana 106-104 New York (Brunson 33), Orlando 107-99 Milwaukee, Chicago 125-117 OT Atlanta, Memphis 142-111 New Orleans, Houston 125-118 Utah (Sengun 43), Portland 120-107 Sacramento and the Clippers 113-112 over Oklahoma City.

Saturday 14 November has five upcoming games (Nuggets at Pelicans 7:00 p.m. ET, Mavericks at Cavaliers 7:30, then Pistons at Heat, Nets at Grizzlies, Bulls at Timberwolves). None are published as final."""
        },
        {
            "slug": "atp-stockholm-fritz-tirante-final-turin-sunday-2026",
            "title": "Fritz reaches Stockholm final after Musetti; Tirante debuts in an ATP final today",
            "subtitle": "A Rune walkover and a 6-4, 6-2 semifinal put Taylor Fritz across from Thiago Agustin Tirante. Turin group play starts Sunday with Zverev vs Jodar.",
            "category": "Desk",
            "excerpt": "Stockholm final today: Fritz vs Tirante. Friday: Fritz d Musetti 6-4, 6-2; Tirante d Tabilo 7-5, 7-6 (1). Turin opens Sunday. No final score and no Turin score.",
            "image": IMG["ten"],
            "readingTime": 4,
            "pubDate": "2026-11-14",
            "sport": "tennis",
            "competition": "atp-250-stockholm-2026",
            "relatedSlug": "atp-stockholm-open-2026-fritz-vs-tirante-final",
            "sources": [
                {"name": "ATP Tour: Stockholm current results", "url": "https://www.atptour.com/en/scores/current/stockholm/429/results"},
                {"name": "Nitto ATP Finals Sunday-Monday schedule", "url": "https://www.nittoatpfinals.com/en/news/nitto-atp-finals-2026-schedule-sunday-monday"}
            ],
            "content": """Taylor Fritz is in the Bybit Stockholm Open final today, Saturday 14 November, at Kungliga Tennishallen. The top seed advanced when Holger Rune withdrew from Thursday's quarterfinal (walkover) and then beat Lorenzo Musetti 6-4, 6-2 in 63 minutes on Friday. Thiago Agustin Tirante, ranked 51, reached the first ATP Tour final of his career by defeating Alejandro Tabilo 7-5, 7-6 (1). The championship match is upcoming. Do not publish a final score.

The Nitto ATP Finals in Turin still open Sunday 15 November at Inalpi Arena. Groups are unchanged from Thursday's draw: McEnroe (Zverev, Shelton, Fils, Jodar) and Lendl (Alcaraz, Medvedev, Cobolli, Tiafoe). Sunday singles: Zverev vs Jodar not before 2:00 p.m. CET, Shelton vs Fils not before 8:30 p.m. Monday: Alcaraz vs Tiafoe, Medvedev vs Cobolli. No Turin match has been played."""
        },
        {
            "slug": "dp-world-tour-dubai-r2-mcilroy-hatton-share-lead-2026",
            "title": "Dubai 36 holes: McIlroy and Hatton share 139 as Luiten slips; R3 unpublished",
            "subtitle": "Associated Press Friday totals put Rory McIlroy and Tyrrell Hatton at five under, one ahead of Joost Luiten. Saturday's third round is not posted as final.",
            "category": "Match Report",
            "excerpt": "R2 complete: McIlroy 69-70 and Hatton 70-69 lead on 139. Luiten 67-73=140. Chacarra 72-71=143 (T11). Round 3 Saturday is in progress and unpublished.",
            "image": IMG["golf"],
            "readingTime": 4,
            "pubDate": "2026-11-14",
            "sport": "golf",
            "competition": "dp-world-tour-2026",
            "relatedSlug": "dp-world-tour-championship-dubai-2026",
            "sources": [
                {"name": "Associated Press Friday second-round scores", "url": "https://wtop.com/sports/2026/11/dp-world-tour-championship-scores-2/"},
                {"name": "DP World Tour Championship Dubai leaderboard", "url": "https://www.europeantour.com/dpworld-tour/dp-world-tour-championship-dubai-2026/leaderboard"}
            ],
            "content": """Associated Press posted complete second-round scores Friday, 13 November, from the Earth Course at Jumeirah Golf Estates. Rory McIlroy shot 69-70 for 139 (five under) and shares the DP World Tour Championship lead with Tyrrell Hatton (70-69). Joost Luiten, who opened with 67, added a 73 for 140 alongside Kristoffer Reitan (70-70). Mikael Lindberg, Victor Perez and Freddy Schott sit at 141.

Race to Dubai leader Eugenio Lopez-Chacarra is 72-71 for 143, tied for 11th with Francesco Laporta, Adrian Meronk and first-round runner-up Jacob Skov Olesen (68-75). The $10 million season finale has 36 holes remaining. Round 3 is in progress Saturday 14 November and is not published as a final. Sunday is the fourth round."""
        },
        {
            "slug": "f1-five-days-las-vegas-round-21-p2-chase-2026",
            "title": "Five days to Las Vegas: Verstappen to Norris still packed inside 33 points",
            "subtitle": "No 2026 Strip Grand Prix has been run. Antonelli (390) and Mercedes (652) remain champions after Sao Paulo.",
            "category": "Desk",
            "excerpt": "Round 21 is 19-21 November on the 6.201 km Las Vegas Strip. Standings unchanged: Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246. No race result.",
            "image": IMG["f1"],
            "readingTime": 4,
            "pubDate": "2026-11-14",
            "sport": "f1",
            "competition": "f1-2026",
            "relatedSlug": "las-vegas-gp-strip-2026",
            "sources": [
                {"name": "Formula1.com: 2026 Las Vegas Grand Prix event guide", "url": "https://www.formula1.com/en/racing/2026/las-vegas"},
                {"name": "Formula1.com: 2026 Drivers standings", "url": "https://www.formula1.com/en/results/2026/drivers"}
            ],
            "content": """Five days remain before Round 21 of the 2026 FIA Formula One World Championship on the 6.201-kilometre Las Vegas Strip Circuit (19-21 November, Saturday night race 21 November). No practice, qualifying, or race result from this event has been recorded.

Drivers Champion Kimi Antonelli sits on 390 points and Mercedes on 652 Constructors points after Interlagos. The fight for second is frozen: Max Verstappen 279, George Russell 262, Lewis Hamilton 261, Charles Leclerc 249, Lando Norris 246. Ferrari has 510 Constructors points, Red Bull 415, McLaren 398. Qatar is 29 November, Abu Dhabi 6 December. Do not convert a prior-year Las Vegas result into this clock."""
        },
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

    sports_ts_content = """export const SITE_TODAY = '2026-11-14';

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
    slug: 'football',
    label: 'Football',
    short: 'NFL',
    href: '/sport/football',
    tagline: "TNF Final: Diggs 32-yard TD with 0:57 left lifts Commanders 24-21 over Giants. No Saturday NFL game.",
    liveNow: "FINAL Thu: Commanders 24, Giants 21 (Daniels 3 TD, Diggs winner, Douglas INT). WSH 3-5-1, NYG 5-3-1. Sunday Munich: Patriots vs Lions, 9:30 a.m. ET FOX.",
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: "NFL TNF FINAL: COMMANDERS 24-21 GIANTS ON DIGGS TD AT 0:57; SATURDAY DARK, SUNDAY MUNICH",
    board: 'Open the field',
    span: 'hero',
  },
  {
    slug: 'soccer',
    label: 'Soccer',
    short: 'Soccer',
    href: '/sport/soccer',
    tagline: "Kane penalty wins England 2-1 on cap 126; Arsenal hold Barcelona 1-1 at Camp Nou. Sunday: Spain vs England.",
    liveNow: "Thu Finals: England 2-1 Croatia (Rogers 24, Kane 64 pen); Italy 3-1 France; Czechia 0-2 Spain; Barcelona 1-1 Arsenal. Sunday 19:45 GMT: Spain vs England, Madrid.",
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: "ENGLAND 2-1 CROATIA AND BARCELONA 1-1 ARSENAL; SUNDAY SPAIN VS ENGLAND IN MADRID",
    board: 'Open the pitch',
    span: 'side',
  },
  {
    slug: 'basketball',
    label: 'Basketball',
    short: 'Hoops',
    href: '/sport/basketball',
    tagline: "Spurs 123-85 Warriors for an 11th straight win; Castle 32. Thursday: Cunningham 52 in 2OT.",
    liveNow: "Fri: Spurs 123, Warriors 85 (Castle 32, Wemby 12/12/6). Thu: Pistons 144-140 2OT Wizards (Cunningham 52). Tonight: 5 NBA games upcoming.",
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: "NBA: SPURS 11TH STRAIGHT 123-85, CASTLE 32; CUNNINGHAM 52 IN DOUBLE OT THURSDAY",
    board: 'Open the floor',
    span: 'half',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: "Dubai R2 complete: McIlroy and Hatton share 139 (-5). Round 3 Saturday unpublished as final.",
    liveNow: "R2 AP: T1 McIlroy 69-70=139, Hatton 70-69=139; T3 Luiten 140, Reitan 140; Chacarra 143 (T11). R3 in progress, not posted as final.",
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: "DUBAI R2: MCILROY AND HATTON SHARE 139; LUITEN 140; R3 NOT PUBLISHED AS FINAL",
    board: 'Open the course',
    span: 'half',
  },
  {
    slug: 'tennis',
    label: 'Tennis',
    short: 'Tennis',
    href: '/sport/tennis',
    tagline: "Stockholm Final Today: Fritz vs Tirante after a 6-4, 6-2 SF. Turin opens Sunday with Zverev vs Jodar.",
    liveNow: "Today Final: Fritz vs Tirante (upcoming). Fri SF: Fritz d Musetti 6-4, 6-2; Tirante d Tabilo 7-5, 7-6 (1). QF: Fritz walkover Rune. Turin Sunday.",
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: "STOCKHOLM FINAL TODAY FRITZ VS TIRANTE; TURIN OPENS SUNDAY ZVEREV VS JODAR",
    board: 'Open the court',
    span: 'half',
  },
  {
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: "Five days to Round 21 Las Vegas: 33 points still split Verstappen to Norris. No Strip race yet.",
    liveNow: "Drivers P2 race unchanged: Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246 (Antonelli 390; Mercedes 652). Round 21: 19-21 Nov.",
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: "FIVE DAYS TO VEGAS: VERSTAPPEN TO NORRIS STILL 33 PTS BEHIND CHAMPION ANTONELLI",
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

    desk_path = os.path.join(ROOT, "frontend/src/data/desk.json")
    with open(desk_path, "r", encoding="utf-8") as f:
        desk = json.load(f)
    desk["asOf"] = "2026-11-14"

    nfl_notes = [x for x in desk.get("nflWeek1", []) if not (x.get("date") == "2026-11-12" and "Giants" in x.get("home", ""))]
    nfl_notes.append({
        "date": "2026-11-12",
        "time": "8:15 p.m. ET",
        "home": "New York Giants",
        "away": "Washington Commanders",
        "note": "FINAL: Commanders 24, Giants 21. Daniels 23/33, 249 yds, 3 TD; Diggs 32-yd TD at 0:57; Douglas INT. Skattebo 2 rush TD. WSH 3-5-1, NYG 5-3-1."
    })
    nfl_notes.append({
        "date": "2026-11-15",
        "time": "9:30 a.m. ET",
        "home": "Detroit Lions",
        "away": "New England Patriots",
        "note": "UPCOMING Sunday Munich (FOX, Allianz Arena): Patriots (5-4) vs Lions (6-2), 9:30 a.m. ET. Saturday 14 Nov has no NFL game. Last final: Commanders 24, Giants 21."
    })
    desk["nflWeek1"] = nfl_notes

    tennis_notes = [x for x in desk.get("usOpenQF", []) if not (x.get("draw", "").startswith("Stockholm") or x.get("draw", "").startswith("Turin"))]
    tennis_notes.extend([
        {"draw": "Stockholm R16", "p1": "Taylor Fritz", "p2": "Cameron Norrie", "status": "Fritz 7-5, 6-3"},
        {"draw": "Stockholm R16", "p1": "Holger Rune", "p2": "Miomir Kecmanovic", "status": "Rune 2-6, 6-1, 6-4"},
        {"draw": "Stockholm QF", "p1": "Taylor Fritz", "p2": "Holger Rune", "status": "Fritz walkover"},
        {"draw": "Stockholm SF", "p1": "Taylor Fritz", "p2": "Lorenzo Musetti", "status": "Fritz 6-4, 6-2"},
        {"draw": "Stockholm SF", "p1": "Thiago Agustin Tirante", "p2": "Alejandro Tabilo", "status": "Tirante 7-5, 7-6 (1)"},
        {"draw": "Stockholm Final", "p1": "Taylor Fritz", "p2": "Thiago Agustin Tirante", "status": "Today Center Court"},
        {"draw": "Turin McEnroe Group", "p1": "Alexander Zverev (1)", "p2": "Ben Shelton (3)", "status": "Sun: Zverev vs Jodar; Shelton vs Fils"},
        {"draw": "Turin Lendl Group", "p1": "Carlos Alcaraz (2)", "p2": "Daniil Medvedev (4)", "status": "Mon: Alcaraz vs Tiafoe; Medvedev vs Cobolli"},
    ])
    desk["usOpenQF"] = tennis_notes
    dump(desk_path, desk)

    agents_path = os.path.join(ROOT, "AGENTS.md")
    with open(agents_path, "r", encoding="utf-8") as f:
        agents_lines = f.readlines()
    new_clock_line = (
        "*   **Site clock:** editorial today is `2026-11-14` in `frontend/src/data/sports.ts` (`SITE_TODAY`). "
        "Soccer: Thu UWCL Barcelona 1-1 Arsenal (Maanum 22, Graham Hansen 59); Nations League England 2-1 Croatia (Rogers 24, Kane 64 pen on cap 126), Italy 3-1 France (Pio Esposito 2), Czechia 0-2 Spain; Sunday Spain vs England 19:45 GMT Metropolitano; PL Arsenal 27, Brighton 22, Man City 21. "
        "Football: TNF Thu Commanders 24, Giants 21 (Daniels 3 TD, Diggs 32-yd at 0:57, Douglas INT; WSH 3-5-1, NYG 5-3-1); Saturday 14 Nov has no NFL game; Sunday Munich Patriots vs Lions 9:30 a.m. ET FOX unpublished. "
        "Basketball: Fri Spurs 123-85 Warriors (Castle 32, Wemby 12/12/6, 11th straight, 11-2; Curry out oblique); Thu Pistons 144-140 2OT Wizards (Cunningham 52); Saturday 5 NBA games upcoming. "
        "Golf: Dubai R2 complete AP: McIlroy and Hatton -5 (139), Luiten and Reitan -4 (140), Chacarra -1 (143 T11); R3 Saturday unpublished as final. "
        "Tennis: Stockholm Fritz walkover Rune, then 6-4, 6-2 Musetti; Tirante 7-5, 7-6 (1) Tabilo; today final Fritz vs Tirante unpublished; Turin starts Sunday Zverev vs Jodar. "
        "Formula 1: Five days to Round 21 Las Vegas (19-21 Nov, 6.201 km Strip), 33 pts separate Verstappen (279) through Norris (246) behind Champion Antonelli (390); Mercedes 652, Ferrari 510, Red Bull 415, McLaren 398. No Vegas race result.\n"
    )
    check_dashes(new_clock_line, "AGENTS.md:Site clock")
    for i, line in enumerate(agents_lines):
        if "*   **Site clock:**" in line:
            agents_lines[i] = new_clock_line
            break
    with open(agents_path, "w", encoding="utf-8") as f:
        f.writelines(agents_lines)
    print("updated AGENTS.md")

    featured = [
        "commanders-at-giants-tnf-week10-2026",
        "nba-spurs-vs-warriors-nov13-2026",
        "england-vs-croatia-nations-league-2026",
        "uwcl-barcelona-vs-arsenal-md4-2026",
        "atp-stockholm-open-2026-fritz-vs-tirante-final",
        "dp-world-tour-championship-dubai-2026",
        "atp-nitto-finals-2026-turin-draw",
    ]
    patch_featured(os.path.join(ROOT, "frontend/src/views/HomePage.astro"), featured)
    patch_featured(os.path.join(ROOT, "frontend/src/views/LivePage.astro"), featured)
    print("apply_nov14_desk complete")
