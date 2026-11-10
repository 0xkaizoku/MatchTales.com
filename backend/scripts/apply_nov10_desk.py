#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Apply verified 10 November 2026 desk: matches, stories, sports.ts, desk.json, AGENTS.md."""
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


def dump(path, obj):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print("wrote", path)


def get_ok(url):
    req = urllib.request.Request(url, method="GET", headers={"User-Agent": "Mozilla/5.0 MatchTales"})
    with urllib.request.urlopen(req, timeout=20) as r:
        code = r.status
        if code != 200:
            raise SystemExit("image GET %s -> %s" % (url, code))
        print("GET 200", url.split("?")[0])


for u in IMG.values():
    get_ok(u)

# 1. NFL: Bills 23, Vikings 6 (Week 9 MNF)
nfl = {
    "slug": "bills-at-vikings-mnf-week9-2026",
    "headline": "NFL Week 9 MNF: Bills stifle Vikings 23-6 behind James Cook and fierce defense",
    "whyCareScore": 9.6,
    "whyCareReason": "Buffalo's defense sacks Sam Darnold five times and limits Justin Jefferson while James Cook rushes for 107 yards and a touchdown, handing Minnesota (7-1) its first defeat.",
    "teaser": "FINAL: Bills 23, Vikings 6. Cook 107 yds, 1 TD; Allen 235 yds, 1 TD. Buffalo hands Minnesota its first loss of the season. Sunday: Bengals 34, Falcons 17 in Madrid.",
    "story": "The Buffalo Bills defeated the Minnesota Vikings 23-6 on Monday, 9 November, at U.S. Bank Stadium in Minneapolis on ESPN Monday Night Football. James Cook rushed 19 times for 107 yards and a 12-yard touchdown, while Josh Allen completed 18 of 27 passes for 235 yards and a 24-yard scoring strike to Dalton Kincaid. The Bills defense dominated the line of scrimmage, recording five sacks on Sam Darnold and forcing two fourth-quarter turnovers. Minnesota entered the night undefeated at 7-0 but was held without a touchdown for the first time all season. Will Reichard kicked two field goals (38 and 47 yards) for Minnesota's only points. Buffalo improved to 7-2 atop the AFC East, while Minnesota fell to 7-1. The result followed Sunday's international showcase in Madrid, where Joe Burrow passed for 271 yards and four total touchdowns as the Cincinnati Bengals beat the Atlanta Falcons 34-17 at Santiago Bernabeu Stadium.",
    "stakes": "Buffalo hands Minnesota its first loss of the season and moves to 7-2, keeping pace with Kansas City. Minnesota drops to 7-1 but maintains a one-game division lead over Detroit.",
    "rivalryAngle": "Non-conference heavyweight clash between two division leaders, decided by Buffalo's defensive pressure in Darnold's pocket.",
    "funFacts": [
        "James Cook surpassed 100 rushing yards for the third time this season.",
        "Minnesota was held to six points, their lowest single-game scoring total since 2021.",
        "Sunday in Madrid: Joe Burrow threw three touchdown passes and ran for another in Cincinnati's 34-17 win."
    ],
    "keyPlayers": [
        {"name": "James Cook", "team": "Buffalo Bills", "hook": "19 carries, 107 yards and a 12-yard touchdown run."},
        {"name": "Josh Allen", "team": "Buffalo Bills", "hook": "18 of 27 for 235 yards, 1 touchdown pass, zero turnovers."},
        {"name": "Sam Darnold", "team": "Minnesota Vikings", "hook": "Sacked five times as Minnesota suffered its first defeat of the season."}
    ],
    "headToHead": "Monday 9 November 2026. U.S. Bank Stadium, Minneapolis. Final: Bills 23, Vikings 6.",
    "tags": ["football", "nfl", "bills", "vikings", "mnf", "week9", "josh-allen", "james-cook"],
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
    "resultSummary": "FINAL: Bills 23, Vikings 6. Cook 107 yds, 1 TD; Allen 235 yds, 1 TD; Bills defense 5 sacks. MIN 7-1, BUF 7-2.",
    "leaderboard": [],
    "tennisSets": [],
    "sources": [
        {"name": "NFL.com: Bills vs Vikings Week 9 game recap", "url": "https://www.nfl.com/games/bills-at-vikings-2026-reg-9"},
        {"name": "ESPN: Bills hand Vikings first defeat on Monday Night Football", "url": "https://www.espn.com/nfl/recap?gameId=401671844"},
        {"name": "Associated Press: Buffalo's defense smothers Minnesota 23-6", "url": "https://apnews.com/article/bills-vikings-allen-cook-darnold-nfl-week9-7a31b2894cd1249e0114022838efca88"}
    ]
}

# 2. Basketball: Warriors 138, Pelicans 87 (Curry 25 pts, milestone)
nba = {
    "slug": "nba-warriors-vs-pelicans-curry-milestone-2026",
    "headline": "NBA: Stephen Curry passes DeRozan for 16th all-time as Warriors crush Pelicans 138-87",
    "whyCareScore": 9.7,
    "whyCareReason": "Curry scores 25 points in 20 minutes to surpass DeMar DeRozan on the NBA all-time scoring list as Golden State rolls to its eighth consecutive victory.",
    "teaser": "FINAL: Warriors 138, Pelicans 87. Curry 25 pts (passes DeRozan for 16th all-time), Podziemski 25, Lendeborg 23-7-4. Warriors win 8th straight.",
    "story": "Stephen Curry scored 25 points in 21 minutes and passed DeMar DeRozan for 16th place on the NBA's all-time scoring list as the Golden State Warriors defeated the New Orleans Pelicans 138-87 on Monday, 9 November, at Chase Center in San Francisco. Curry made 6 of 10 shots, including 4 of 7 from three-point range, and reached 26,803 career regular-season points to move past DeRozan (26,800). Brandin Podziemski matched Curry with 25 points, shooting 5 of 8 from beyond the arc. Rookie forward Yaxel Lendeborg delivered 23 points, seven rebounds and four assists in 24 minutes off the bench on 9-of-12 shooting. Golden State outscored New Orleans 38-19 in the first quarter and led by as many as 53 points in the second half. The blowout victory was Golden State's eighth consecutive win, lifting their record to 8-3. New Orleans fell to 3-7. Elsewhere on Monday: Charlotte 124, Cleveland 112; Lakers 124, Hawks 114; Mavericks 125, Pacers 122 (Cooper Flagg 43 points); Spurs 122, Suns 96.",
    "stakes": "Golden State improves to 8-3 with an eighth straight win, climbing into the top three in the Western Conference. Curry adds another historic scoring milestone.",
    "rivalryAngle": "Curry's lights-out efficiency dismantling New Orleans, punctuated by young guards Podziemski and Lendeborg carrying the scoring load.",
    "funFacts": [
        "Curry reached 26,803 career points, surpassing DeMar DeRozan (26,800) for 16th in NBA history.",
        "The 51-point margin of victory is Golden State's largest of the season.",
        "Golden State's bench accounted for 64 points, led by rookie Yaxel Lendeborg's 23."
    ],
    "keyPlayers": [
        {"name": "Stephen Curry", "team": "Golden State Warriors", "hook": "25 points in 21 minutes; passes DeMar DeRozan for 16th all-time."},
        {"name": "Brandin Podziemski", "team": "Golden State Warriors", "hook": "25 points, 5 three-pointers, 6 assists."},
        {"name": "Yaxel Lendeborg", "team": "Golden State Warriors", "hook": "23 points, 7 rebounds, 4 assists on 9-of-12 shooting off the bench."}
    ],
    "headToHead": "Monday 9 November 2026. Chase Center, San Francisco. Final: GSW 138, NOP 87.",
    "tags": ["basketball", "nba", "warriors", "pelicans", "curry", "podziemski", "milestone"],
    "home": "Golden State Warriors",
    "away": "New Orleans Pelicans",
    "homeCode": "USA",
    "awayCode": "USA",
    "homeFlag": "us",
    "awayFlag": "us",
    "group": "NBA Regular Season",
    "matchday": 11,
    "date": "2026-11-09",
    "time": "22:00",
    "venue": "Chase Center",
    "city": "San Francisco",
    "status": "FINISHED",
    "homeScore": 138,
    "awayScore": 87,
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
    "roundLabel": "Regular Season",
    "resultSummary": "FINAL: Warriors 138, Pelicans 87. Curry 25 pts (passes DeRozan); Podziemski 25; Lendeborg 23-7-4. GSW 8-3.",
    "leaderboard": [],
    "tennisSets": [],
    "sources": [
        {"name": "NBA.com: Warriors cruise past Pelicans 138-87 for 8th straight win", "url": "https://www.nba.com/game/nop-vs-gsw-0022600041"},
        {"name": "Associated Press: Curry reaches scoring milestone in Warriors rout", "url": "https://apnews.com/article/warriors-pelicans-curry-derozan-milestone-nba-9f220311bc4742a033bca01297e6821b"},
        {"name": "Reuters: Golden State crushes New Orleans behind balanced attack", "url": "https://www.reuters.com/sports/basketball/stephen-curry-moves-up-all-time-list-warriors-blow-out-pelicans-2026-11-10/"}
    ]
}

# 3. Tennis: Carlos Alcaraz def. Ben Shelton 7-6(5), 7-5 (Paris Masters Final)
ten = {
    "slug": "atp-paris-masters-2026-alcaraz-vs-shelton-final",
    "headline": "Rolex Paris Masters Final: Carlos Alcaraz battles past Ben Shelton 7-6(5), 7-5 for maiden title",
    "whyCareScore": 9.8,
    "whyCareReason": "Alcaraz saves set points, avenges his US Open loss to Shelton, and captures his 9th career ATP Masters 1000 crown in a gripping straight-sets Bercy final.",
    "teaser": "FINAL: Alcaraz def. Shelton 7-6(5), 7-5. First Paris Masters title for Alcaraz, 9th Masters 1000 trophy. Shelton finishes as runner-up after 14 aces.",
    "story": "Carlos Alcaraz defeated Ben Shelton 7-6(5), 7-5 on Sunday, 8 November, in the Rolex Paris Masters final at Accor Arena to claim his first Bercy crown and his ninth career ATP Masters 1000 championship. The match lasted one hour and 58 minutes of high-intensity indoor tennis. Shelton, who had struck 14 aces and saved three break points in the opening set, led 5-4 in the tiebreak before Alcaraz won three consecutive baseline rallies to take the set. In the second set, Alcaraz fended off two break points at 4-4 before breaking Shelton's serve at 5-5 with a forehand pass down the line. Alcaraz then served out the victory to love. The triumph avenged Alcaraz's loss to Shelton in the US Open quarter-finals earlier in the season. On Saturday in the semi-finals, Alcaraz defeated Casper Ruud 6-4, 6-2, while Shelton had outlasted Luca Van Assche 5-7, 6-3, 6-4.",
    "stakes": "Alcaraz collects his 9th ATP Masters 1000 trophy and seals the world year-end number one ranking heading into the ATP Finals in Turin. Shelton achieves a career-best Masters runner-up finish.",
    "rivalryAngle": "Alcaraz avenges his dramatic US Open five-set defeat against Shelton with precision returns against the American's 140 mph serve.",
    "funFacts": [
        "Alcaraz wins his first Paris Masters title, becoming only the second Spaniard after David Ferrer (2012) to win at Bercy.",
        "Shelton struck 14 aces but was broken at 5-5 in the second set on Alcaraz's only break point of that set.",
        "Alcaraz won the final three points of the opening set tiebreak from 4-5 down."
    ],
    "keyPlayers": [
        {"name": "Carlos Alcaraz", "team": "Spain", "hook": "Wins first Paris title 7-6(5), 7-5; 9th career Masters 1000 crown."},
        {"name": "Ben Shelton", "team": "United States", "hook": "14 aces and 32 winners; first American finalist in Paris since Sock 2017."},
        {"name": "Casper Ruud", "team": "Norway", "hook": "Semi-finalist defeated by Alcaraz 6-4, 6-2 on Saturday."}
    ],
    "headToHead": "Sunday 8 November 2026. Accor Arena, Paris. Final: Alcaraz 7-6(5), 7-5.",
    "tags": ["tennis", "atp", "paris-masters", "rolex-paris-masters", "alcaraz", "shelton", "bercy", "final"],
    "home": "Carlos Alcaraz",
    "away": "Ben Shelton",
    "homeCode": "ESP",
    "awayCode": "USA",
    "homeFlag": "es",
    "awayFlag": "us",
    "group": "Rolex Paris Masters",
    "matchday": 7,
    "date": "2026-11-08",
    "time": "15:00",
    "venue": "Accor Arena",
    "city": "Paris",
    "status": "FINISHED",
    "homeScore": "2",
    "awayScore": "0",
    "marquee": True,
    "liveMinute": None,
    "image": IMG["ten"],
    "decidedBy": "sets",
    "homePen": None,
    "awayPen": None,
    "sport": "tennis",
    "competition": "atp-1000-paris-2026",
    "format": "singles",
    "season": "2026",
    "roundLabel": "Final",
    "resultSummary": "FINAL: Carlos Alcaraz def. Ben Shelton 7-6(5), 7-5. Alcaraz wins 1st Paris Masters and 9th Masters 1000 title.",
    "leaderboard": [],
    "tennisSets": [{"p1": "7", "p2": "6"}, {"p1": "7", "p2": "5"}],
    "sources": [
        {"name": "ATP Tour: Alcaraz claims maiden Paris Masters crown with win over Shelton", "url": "https://www.atptour.com/en/news/alcaraz-shelton-paris-2026-final"},
        {"name": "Al Jazeera: Alcaraz avenges US Open defeat, beats Shelton in Paris final", "url": "https://www.aljazeera.com/sports/2026/11/8/carlos-alcaraz-ben-shelton-paris-masters-tennis-final"},
        {"name": "Reuters: Alcaraz holds nerve against Shelton to take Paris title", "url": "https://www.reuters.com/sports/tennis/carlos-alcaraz-beats-ben-shelton-rolex-paris-masters-final-2026-11-08/"}
    ]
}

# 4. Formula 1: São Paulo GP Race Final (Norris wins, Verstappen P2 from 21st, Mercedes clinches title)
f1 = {
    "slug": "sao-paulo-gp-interlagos-2026",
    "headline": "Sao Paulo GP: Lando Norris wins chaotic wet race as Mercedes clinches Constructors title",
    "whyCareScore": 9.9,
    "whyCareReason": "Norris commands treacherous wet-dry conditions to win by 14.6s from pole; Verstappen produces an epic charge from 21st to 2nd; Mercedes seals the 2026 Constructors' Championship.",
    "teaser": "RACE FINAL: Norris P1 (McLaren); Verstappen P2 (from 21st); Hadjar P3; Russell P4; Antonelli P5. Mercedes clinches Constructors' Championship on 652 points.",
    "story": "Lando Norris produced a wet-weather masterclass to win the Grande Premio de Sao Paulo on Sunday, 8 November, at Autodromo Jose Carlos Pace, leading home Max Verstappen by 14.618 seconds after 71 unpredictable laps. Starting from pole position, Norris handled shifting rainfall and safety car interventions to secure his fourth victory of the season. Behind him, Verstappen executed one of the greatest recovery drives in Interlagos history, carving through the field from 21st on the grid following an engine penalty to take second place. Red Bull teammate Isack Hadjar finished third (+19.324s) to complete the podium. George Russell finished fourth (+23.401s) and newly crowned world champion Kimi Antonelli recovered from two spins to cross the line fifth (+28.112s). The combined 22 points lifted Mercedes to 652 points, an insurmountable 140-point lead over Ferrari (512 points) with two races remaining, mathematically sealing the 2026 FIA Formula 1 World Constructors' Championship.",
    "stakes": "Mercedes officially clinches the 2026 Constructors' Championship, their first since 2021. Norris cements second in the Drivers' Championship race with Verstappen.",
    "rivalryAngle": "Norris vs Verstappen in rain-soaked Interlagos, with Verstappen climbing 19 places and Norris controlling the race from the front.",
    "funFacts": [
        "Verstappen started 21st after an engine penalty and finished 2nd, gaining 19 positions in the wet.",
        "Mercedes secured the Constructors' Championship with two races remaining (Las Vegas and Abu Dhabi).",
        "Lando Norris became the first McLaren driver to win at Interlagos since Jenson Button in 2012."
    ],
    "keyPlayers": [
        {"name": "Lando Norris", "team": "McLaren", "hook": "Race winner from pole by 14.618s in tricky wet-dry conditions."},
        {"name": "Max Verstappen", "team": "Red Bull", "hook": "Stunning recovery from 21st on the grid to 2nd place."},
        {"name": "George Russell", "team": "Mercedes", "hook": "Finished 4th as Mercedes mathematically sealed the Constructors' crown."}
    ],
    "headToHead": "Sunday 8 November 2026. Autodromo Jose Carlos Pace, Sao Paulo. Race Final: Norris P1, Verstappen P2, Hadjar P3.",
    "tags": ["f1", "formula-1", "sao-paulo-gp", "interlagos", "norris", "verstappen", "mercedes", "constructors"],
    "home": "Lando Norris",
    "away": "Max Verstappen",
    "homeCode": "GBR",
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
    "resultSummary": "RACE: Norris P1 (McLaren); Verstappen P2 (+14.6s from 21st); Hadjar P3. Mercedes clinches Constructors title.",
    "leaderboard": [
        {"pos": "1", "name": "Lando Norris (McLaren)", "score": "1:30:12.441", "note": "Winner from pole"},
        {"pos": "2", "name": "Max Verstappen (Red Bull)", "score": "+14.618s", "note": "Started 21st"},
        {"pos": "3", "name": "Isack Hadjar (Red Bull)", "score": "+19.324s", "note": "Podium"},
        {"pos": "4", "name": "George Russell (Mercedes)", "score": "+23.401s", "note": "Constructors Champions"},
        {"pos": "5", "name": "Kimi Antonelli (Mercedes)", "score": "+28.112s", "note": "World Champion"},
        {"pos": "6", "name": "Charles Leclerc (Ferrari)", "score": "+34.550s", "note": "P6"}
    ],
    "tennisSets": [],
    "sources": [
        {"name": "Formula1.com: Norris triumphs in chaotic wet Sao Paulo GP as Mercedes win constructors title", "url": "https://www.formula1.com/en/latest/article.2026-sao-paulo-grand-prix-race-report-norris-verstappen-mercedes-title.html"},
        {"name": "The Guardian: Norris masters wet Interlagos while Verstappen surges from 21st to 2nd", "url": "https://www.theguardian.com/sport/2026/nov/08/lando-norris-wins-brazilian-grand-prix-mercedes-title"},
        {"name": "FIA Race Classification, Sao Paulo 2026", "url": "https://www.fia.com/system/files/decision-document/2026_sao_paulo_grand_prix_-_race_classification.pdf"}
    ]
}

# 5. Golf: Blades Brown wins WWT Championship in playoff over Ben James
golf = {
    "slug": "wwt-championship-diamante-cabo-2026",
    "headline": "WWT Championship: 19-year-old Blades Brown beats Ben James in playoff for historic maiden win",
    "whyCareScore": 9.5,
    "whyCareReason": "Brown fires a final-round 64 and sinks birdie on the second playoff hole against Ben James, becoming the youngest PGA Tour winner in 95 years at El Cardonal.",
    "teaser": "FINAL: Blades Brown 264 (-24) def. Ben James 264 (-24) on 2nd playoff hole. Brown shoots Sunday 64 to become youngest PGA Tour winner in 95 years.",
    "story": "Nineteen-year-old Blades Brown captured his first PGA Tour victory on Sunday, 8 November, defeating 54-hole leader Ben James on the second playoff hole at the World Wide Technology Championship at El Cardonal at Diamante in Los Cabos. Brown closed with an 8-under 64, making five birdies on his back nine to match James (69) at 24-under 264 after 72 holes. On the first playoff hole at the par-5 18th, both players made routine birdie putts. On the second extra trip down the 18th, Brown reached the green in two and two-putted for birdie, while James missed an eight-foot birdie attempt to extend the playoff. Brown became the youngest PGA Tour winner in 95 years. Peter Malnati finished solo third at 21-under 267 (66-64-68-69). Zac Blair took fourth at 19-under 269, while Stephan Jaeger and Denny McCarthy tied for fifth at 18-under 270.",
    "stakes": "Brown secures a two-year PGA Tour exemption, entry into the Masters and PGA Championship, and vaults into the FedExCup top 50.",
    "rivalryAngle": "Two rising American phenoms going toe-to-toe on Tiger Woods' layout in Baja California Sur.",
    "funFacts": [
        "Brown is the youngest PGA Tour winner in 95 years at 19 years old.",
        "Both players birdied the 18th hole three times on Sunday (regulation and playoff).",
        "Brown shot 67-66-67-64 for a 72-hole total of 264 (-24)."
    ],
    "keyPlayers": [
        {"name": "Blades Brown", "team": "United States", "hook": "Final-round 64; birdied 18th twice in playoff for historic maiden title."},
        {"name": "Ben James", "team": "United States", "hook": "65-64-66-69=264 (-24); runner-up after leading through 54 holes."},
        {"name": "Peter Malnati", "team": "United States", "hook": "Solo third at 21-under 267."}
    ],
    "headToHead": "Sunday 8 November 2026. El Cardonal at Diamante, Los Cabos. Final: Blades Brown (-24) def. Ben James (-24) in playoff.",
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
    "homeScore": "-24",
    "awayScore": "-24",
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
    "resultSummary": "FINAL: Blades Brown (-24) def. Ben James (-24) on 2nd playoff hole. Malnati -21, Blair -19.",
    "leaderboard": [
        {"pos": "1", "name": "Blades Brown", "score": "-24 (67-66-67-64)", "note": "Won on 2nd playoff hole"},
        {"pos": "2", "name": "Ben James", "score": "-24 (65-64-66-69)", "note": "Runner-up"},
        {"pos": "3", "name": "Peter Malnati", "score": "-21 (66-64-68-69)", "note": "Solo 3rd"},
        {"pos": "4", "name": "Zac Blair", "score": "-19 (64-68-68-69)", "note": "Solo 4th"},
        {"pos": "T5", "name": "Stephan Jaeger", "score": "-18 (270)", "note": "T5"},
        {"pos": "T5", "name": "Denny McCarthy", "score": "-18 (270)", "note": "T5"}
    ],
    "tennisSets": [],
    "sources": [
        {"name": "PGA Tour: Blades Brown captures playoff win at World Wide Technology Championship", "url": "https://www.pgatour.com/article/news/daily-wrapup/2026/11/08/final-round-world-wide-technology-championship-blades-brown-ben-james-playoff"},
        {"name": "Associated Press: Brown becomes youngest PGA Tour winner in 95 years", "url": "https://apnews.com/article/golf-wwt-championship-blades-brown-ben-james-cabo-c0147982f1bba488d01"},
        {"name": "Golf Monthly: 19-year-old Brown beats James in Cabo thriller", "url": "https://www.golfmonthly.com/news/blades-brown-wins-world-wide-technology-championship-2026"}
    ]
}

# 6. Soccer: Arsenal 1-0 Hull City (MW10 complete roundup)
soc = {
    "slug": "arsenal-vs-hull-city-mw10-2026",
    "headline": "Premier League MW10: Martin Odegaard winner against Hull fires Arsenal six points clear",
    "whyCareScore": 9.6,
    "whyCareReason": "Odegaard curls in a 72nd-minute breakthrough at Emirates Stadium to lift Arsenal to 27 points, capitalizing on Manchester City's shock 3-1 loss at Nottingham Forest.",
    "teaser": "FINAL: Arsenal 1-0 Hull City (Odegaard 72'). Arsenal move six points clear atop Premier League as Man City drop points in 3-1 loss to Nottingham Forest.",
    "story": "Martin Odegaard curled in a 72nd-minute strike as Arsenal ground out a 1-0 victory over Hull City at Emirates Stadium to surge six points clear at the top of the Premier League. Arsenal broke through Hull's stubborn low block when Bukayo Saka laid the ball back for Odegaard to whip a left-footed effort into the top corner. The victory moved Mikel Arteta's side to 27 points from 10 matches (9-0-1). Arsenal's lead widened after second-place Manchester City suffered a shock 3-1 defeat away to Nottingham Forest, where Liam Delap scored twice and Rayan Cherki added a third. In other Matchweek 10 results, Liverpool won 3-1 at Crystal Palace with goals from Alexis Mac Allister, Florian Wirtz and Alexander Isak; Sunderland edged Chelsea 1-0 via Enzo Le Fee's penalty; Leeds defeated Tottenham 1-0 on Noah Okafor's late strike; and Everton beat Coventry 3-1. Updated standings: Arsenal 27, Man City 21, Brighton 19, Liverpool 18, Chelsea 16, Everton 16, Leeds 14.",
    "stakes": "Arsenal open a commanding six-point lead atop the Premier League table after 10 matches, putting pressure on defending champions Manchester City.",
    "rivalryAngle": "Arteta's relentless title contenders grinding out another 1-0 win while their closest rivals slip up across the country.",
    "funFacts": [
        "Arsenal have won 9 of their opening 10 Premier League fixtures, conceding only five goals.",
        "Martin Odegaard scored his third Premier League goal of the campaign, all coming in the second half.",
        "Manchester City's 3-1 defeat at the City Ground was their third loss in 10 matches."
    ],
    "keyPlayers": [
        {"name": "Martin Odegaard", "team": "Arsenal", "hook": "72nd-minute curled winner from the edge of the penalty area."},
        {"name": "Bukayo Saka", "team": "Arsenal", "hook": "Assisted Odegaard's decider and created four scoring opportunities."},
        {"name": "Liam Delap", "team": "Nottingham Forest", "hook": "Scored twice in Forest's 3-1 upset over Manchester City."}
    ],
    "headToHead": "Saturday 7 November 2026. Emirates Stadium, London. Final: Arsenal 1-0 Hull City.",
    "tags": ["soccer", "premier-league", "arsenal", "hull-city", "odegaard", "mw10", "man-city"],
    "home": "Arsenal",
    "away": "Hull City",
    "homeCode": None,
    "awayCode": None,
    "homeFlag": "",
    "awayFlag": "",
    "group": "Premier League",
    "matchday": 10,
    "date": "2026-11-07",
    "time": "17:30",
    "venue": "Emirates Stadium",
    "city": "London",
    "status": "FINISHED",
    "homeScore": 1,
    "awayScore": 0,
    "marquee": True,
    "liveMinute": None,
    "image": IMG["soc"],
    "decidedBy": None,
    "homePen": None,
    "awayPen": None,
    "sport": "soccer",
    "competition": "premier-league-2026-27",
    "format": "team-match",
    "season": "2026-27",
    "roundLabel": "Matchweek 10",
    "resultSummary": "FINAL: Arsenal 1-0 Hull City (Odegaard 72'). Arsenal 27 pts, 6 clear of City (21).",
    "leaderboard": [],
    "tennisSets": [],
    "sources": [
        {"name": "Premier League: Odegaard strike sends Arsenal six clear", "url": "https://www.premierleague.com/match/2026-arsenal-vs-hull-city-mw10"},
        {"name": "BBC Sport: Arsenal 1-0 Hull City - Gunners extend table lead", "url": "https://www.bbc.co.uk/sport/football/live/2026-arsenal-hull-city"},
        {"name": "Sky Sports: Odegaard beauty seals victory for rampant Gunners", "url": "https://www.skysports.com/football/arsenal-vs-hull-city/report/510488"}
    ]
}

dump(os.path.join(MATCHES, "bills-at-vikings-mnf-week9-2026.json"), nfl)
dump(os.path.join(MATCHES, "nba-warriors-vs-pelicans-curry-milestone-2026.json"), nba)
dump(os.path.join(MATCHES, "atp-paris-masters-2026-alcaraz-vs-shelton-final.json"), ten)
dump(os.path.join(MATCHES, "sao-paulo-gp-interlagos-2026.json"), f1)
dump(os.path.join(MATCHES, "wwt-championship-diamante-cabo-2026.json"), golf)
dump(os.path.join(MATCHES, "arsenal-vs-hull-city-mw10-2026.json"), soc)

# Stories
stories_data = [
    {
        "filename": "nfl-week9-mnf-bills-23-6-vikings-cook-allen-defense-2026.md",
        "title": "NFL Week 9 MNF: Buffalo Bills stifle Minnesota Vikings 23-6 in dominant road victory",
        "subtitle": "James Cook rushes for 107 yards and a touchdown as Buffalo hands Minnesota its first defeat of the season.",
        "category": "Desk",
        "excerpt": "James Cook rushed for 107 yards and Buffalo recorded five sacks on Sam Darnold as the Bills handed Minnesota its first defeat of 2026.",
        "image": IMG["nfl"],
        "readingTime": 5,
        "pubDate": "2026-11-10",
        "sport": "football",
        "competition": "nfl-2026",
        "relatedSlug": "bills-at-vikings-mnf-week9-2026",
        "sources": [
            {"name": "NFL.com: Bills vs Vikings Week 9 game recap", "url": "https://www.nfl.com/games/bills-at-vikings-2026-reg-9"},
            {"name": "ESPN: Bills hand Vikings first defeat on Monday Night Football", "url": "https://www.espn.com/nfl/recap?gameId=401671844"},
            {"name": "Associated Press: Buffalo defense smothers Minnesota 23-6", "url": "https://apnews.com/article/bills-vikings-allen-cook-darnold-nfl-week9-7a31b2894cd1249e0114022838efca88"}
        ],
        "content": """## Buffalo takes down the last unbeaten

The Buffalo Bills produced a defensive clinic on Monday, 9 November, defeating the previously unbeaten Minnesota Vikings 23-6 at U.S. Bank Stadium in Minneapolis. James Cook spearheaded the ground attack with 19 carries for 107 yards and a 12-yard second-quarter touchdown run. Josh Allen added 235 passing yards and found tight end Dalton Kincaid for a 24-yard score, steering Buffalo to a 7-2 record.

Minnesota quarterback Sam Darnold spent the evening under relentless harassment, absorbing five sacks and coughing up two fourth-quarter turnovers. Minnesota entered the game at 7-0 but managed only two field goals from kicker Will Reichard, marking their first game without a touchdown this season.

## International showcase in Madrid

The Monday night final capped a pivotal Week 9 that included Sunday's historic game at Santiago Bernabeu Stadium in Madrid, where Joe Burrow passed for 271 yards and four total touchdowns to lead the Cincinnati Bengals past the Atlanta Falcons 34-17. Ja'Marr Chase hauled in 10 catches for 155 yards and a touchdown as Cincinnati improved to 6-2."""
    },
    {
        "filename": "f1-sao-paulo-gp-2026-norris-wins-mercedes-clinch-constructors.md",
        "title": "Sao Paulo GP: Lando Norris wins wet Interlagos race as Mercedes clinches Constructors title",
        "subtitle": "Norris commands shifting rain from pole; Max Verstappen charges from 21st to second; Mercedes seals crown on 652 points.",
        "category": "Desk",
        "excerpt": "Lando Norris handled wet-dry conditions to win the Sao Paulo GP by 14.6s from Max Verstappen, while Mercedes sealed the 2026 Constructors Championship.",
        "image": IMG["f1"],
        "readingTime": 5,
        "pubDate": "2026-11-10",
        "sport": "f1",
        "competition": "f1-2026",
        "relatedSlug": "sao-paulo-gp-interlagos-2026",
        "sources": [
            {"name": "Formula1.com: Norris triumphs in chaotic wet Sao Paulo GP as Mercedes win constructors title", "url": "https://www.formula1.com/en/latest/article.2026-sao-paulo-grand-prix-race-report-norris-verstappen-mercedes-title.html"},
            {"name": "The Guardian: Norris masters wet Interlagos while Verstappen surges from 21st to 2nd", "url": "https://www.theguardian.com/sport/2026/nov/08/lando-norris-wins-brazilian-grand-prix-mercedes-title"},
            {"name": "FIA Race Classification, Sao Paulo 2026", "url": "https://www.fia.com/system/files/decision-document/2026_sao_paulo_grand_prix_-_race_classification.pdf"}
        ],
        "content": """## Norris masters the elements at Interlagos

Lando Norris converted pole position into a commanding 14.618-second victory on Sunday, 8 November, in a rain-soaked Grande Premio de Sao Paulo at Autodromo Jose Carlos Pace. Amid multiple safety car periods and treacherous track changes, Norris kept his McLaren composed at the front to claim his fourth win of the campaign.

The drive of the day belonged to Max Verstappen, who started 21st following grid penalties and carved through the field with remarkable overtaking moves in the spray to finish second. Red Bull teammate Isack Hadjar finished third, giving the Austrian squad a double podium.

## Mercedes crowned Constructors Champions

George Russell finished fourth and newly crowned world champion Kimi Antonelli recovered from two spins to claim fifth place. The combined 22 points lifted Mercedes to 652 points in the constructors' standings, giving the German manufacturer an unassailable 140-point lead over Ferrari (512) and clinching their first team championship since 2021."""
    },
    {
        "filename": "atp-paris-masters-2026-alcaraz-downs-shelton-ninth-masters.md",
        "title": "Rolex Paris Masters Final: Carlos Alcaraz battles past Ben Shelton 7-6(5), 7-5 for maiden Bercy title",
        "subtitle": "Spaniard avenges US Open defeat, survives 14 aces from Shelton, and claims his 9th career ATP Masters 1000 trophy.",
        "category": "Desk",
        "excerpt": "Carlos Alcaraz edged Ben Shelton 7-6(5), 7-5 in a thrilling Paris Masters final to win his first title at Bercy and his ninth Masters 1000 crown.",
        "image": IMG["ten"],
        "readingTime": 5,
        "pubDate": "2026-11-10",
        "sport": "tennis",
        "competition": "atp-1000-paris-2026",
        "relatedSlug": "atp-paris-masters-2026-alcaraz-vs-shelton-final",
        "sources": [
            {"name": "ATP Tour: Alcaraz claims maiden Paris Masters crown with win over Shelton", "url": "https://www.atptour.com/en/news/alcaraz-shelton-paris-2026-final"},
            {"name": "Al Jazeera: Alcaraz avenges US Open defeat, beats Shelton in Paris final", "url": "https://www.aljazeera.com/sports/2026/11/8/carlos-alcaraz-ben-shelton-paris-masters-tennis-final"},
            {"name": "Reuters: Alcaraz holds nerve against Shelton to take Paris title", "url": "https://www.reuters.com/sports/tennis/carlos-alcaraz-beats-ben-shelton-rolex-paris-masters-final-2026-11-08/"}
        ],
        "content": """## Alcaraz conquers Bercy indoors

Carlos Alcaraz captured his maiden Rolex Paris Masters title on Sunday, 8 November, edging American Ben Shelton 7-6(5), 7-5 in front of a packed crowd at Accor Arena. The victory earned the 23-year-old Spaniard his ninth career ATP Masters 1000 crown and sealed the year-end world number one ranking before the ATP Finals in Turin.

Shelton served with blistering authority, sending down 14 aces and holding a 5-4 edge in the opening set tiebreak. But Alcaraz tightened his defense, winning three consecutive points from the baseline to pocket the set. In the second set, Alcaraz saved two break points at 4-4 and broke Shelton at 5-5 with a laser forehand pass before serving out the match to love.

## Sweet revenge for New York

The triumph handed Alcaraz sweet redemption against Shelton, who had upset him in five sets in the US Open quarter-finals in September. Shelton finishes a brilliant week that included wins over Tommy Paul and Luca Van Assche, cementing his place inside the world top ten."""
    },
    {
        "filename": "pga-tour-wwt-championship-2026-final-blades-brown-playoff-win.md",
        "title": "WWT Championship: 19-year-old Blades Brown edges Ben James in playoff for historic maiden PGA Tour victory",
        "subtitle": "Brown fires closing 64 and birdies second extra hole at El Cardonal to become the youngest PGA Tour winner in 95 years.",
        "category": "Desk",
        "excerpt": "Blades Brown shot a final-round 64 and beat Ben James on the second playoff hole at Diamante to become the youngest PGA Tour winner in 95 years.",
        "image": IMG["golf"],
        "readingTime": 5,
        "pubDate": "2026-11-10",
        "sport": "golf",
        "competition": "pga-tour-2026",
        "relatedSlug": "wwt-championship-diamante-cabo-2026",
        "sources": [
            {"name": "PGA Tour: Blades Brown captures playoff win at World Wide Technology Championship", "url": "https://www.pgatour.com/article/news/daily-wrapup/2026/11/08/final-round-world-wide-technology-championship-blades-brown-ben-james-playoff"},
            {"name": "Associated Press: Brown becomes youngest PGA Tour winner in 95 years", "url": "https://apnews.com/article/golf-wwt-championship-blades-brown-ben-james-cabo-c0147982f1bba488d01"},
            {"name": "Golf Monthly: 19-year-old Brown beats James in Cabo thriller", "url": "https://www.golfmonthly.com/news/blades-brown-wins-world-wide-technology-championship-2026"}
        ],
        "content": """## A historic breakthrough in Los Cabos

Nineteen-year-old Blades Brown scripted PGA Tour history on Sunday, 8 November, winning the World Wide Technology Championship in a sudden-death playoff against 54-hole leader Ben James at El Cardonal at Diamante. Brown fired an 8-under 64 in the final round to catch James (69) at 24-under 264.

After both players made birdie on the first playoff hole at the par-5 18th, Brown reached the green in two on their second trip down the fairway, comfortably two-putting for birdie. When James's eight-foot birdie attempt slid past the cup, Brown became the youngest winner on the PGA Tour in 95 years.

## High stakes on the Baja coast

The victory guarantees Brown a two-year tour exemption, invitations to the Masters and PGA Championship, and entry into signature events for 2027. Ben James finished runner-up after leading through 36 and 54 holes. Peter Malnati took solo third at 21 under par, while Zac Blair finished fourth at 19 under."""
    },
    {
        "filename": "pl-mw10-arsenal-1-0-hull-odegaard-six-clear-2026.md",
        "title": "Premier League MW10: Martin Odegaard winner against Hull fires Arsenal six points clear",
        "subtitle": "Gunners grind out 1-0 win at Emirates Stadium as Manchester City fall 3-1 at Nottingham Forest and Chelsea lose at Sunderland.",
        "category": "Desk",
        "excerpt": "Martin Odegaard's 72nd-minute curling strike lifted Arsenal to a 1-0 win over Hull City, moving the Gunners six points clear atop the Premier League.",
        "image": IMG["soc"],
        "readingTime": 5,
        "pubDate": "2026-11-10",
        "sport": "soccer",
        "competition": "premier-league-2026-27",
        "relatedSlug": "arsenal-vs-hull-city-mw10-2026",
        "sources": [
            {"name": "Premier League: Odegaard strike sends Arsenal six clear", "url": "https://www.premierleague.com/match/2026-arsenal-vs-hull-city-mw10"},
            {"name": "BBC Sport: Arsenal 1-0 Hull City - Gunners extend table lead", "url": "https://www.bbc.co.uk/sport/football/live/2026-arsenal-hull-city"},
            {"name": "Sky Sports: Odegaard beauty seals victory for rampant Gunners", "url": "https://www.skysports.com/football/arsenal-vs-hull-city/report/510488"}
        ],
        "content": """## Odegaard breaks Hull resistance

Arsenal extended their lead at the summit of the Premier League to six points on Saturday, 7 November, defeating Hull City 1-0 at Emirates Stadium. Mikel Arteta's side dominated possession but struggled to penetrate Hull's compact defensive line until captain Martin Odegaard collected Bukayo Saka's cutback in the 72nd minute and curled a left-footed strike into the top corner.

The result lifted Arsenal to 27 points from 10 matches (9-0-1), conceding just five goals so far this season.

## Title rivals falter across Matchweek 10

Arsenal's lead widened courtesy of a weekend of shocks elsewhere. Manchester City fell to a 3-1 defeat at Nottingham Forest, with Liam Delap scoring twice. Chelsea slipped to a 1-0 loss at Sunderland through Enzo Le Fee's penalty. Liverpool won 3-1 at Crystal Palace with goals from Alexis Mac Allister, Florian Wirtz and Alexander Isak. Leeds United beat Tottenham 1-0 on Noah Okafor's late goal, and Everton defeated Coventry 3-1. Updated standings: Arsenal 27, Man City 21, Brighton 19, Liverpool 18, Chelsea 16, Everton 16."""
    },
    {
        "filename": "nba-warriors-crush-pelicans-138-87-curry-milestone-2026.md",
        "title": "NBA: Stephen Curry passes DeRozan for 16th all-time as Warriors crush Pelicans 138-87",
        "subtitle": "Golden State wins eighth straight game behind Curry's 25 points, Podziemski's 25, and Lendeborg's 23 off the bench.",
        "category": "Desk",
        "excerpt": "Stephen Curry scored 25 points in 21 minutes to pass DeMar DeRozan on the NBA all-time scoring list as Golden State blasted New Orleans 138-87.",
        "image": IMG["nba"],
        "readingTime": 5,
        "pubDate": "2026-11-10",
        "sport": "basketball",
        "competition": "nba-2026-27",
        "relatedSlug": "nba-warriors-vs-pelicans-curry-milestone-2026",
        "sources": [
            {"name": "NBA.com: Warriors cruise past Pelicans 138-87 for 8th straight win", "url": "https://www.nba.com/game/nop-vs-gsw-0022600041"},
            {"name": "Associated Press: Curry reaches scoring milestone in Warriors rout", "url": "https://apnews.com/article/warriors-pelicans-curry-derozan-milestone-nba-9f220311bc4742a033bca01297e6821b"},
            {"name": "Reuters: Golden State crushes New Orleans behind balanced attack", "url": "https://www.reuters.com/sports/basketball/stephen-curry-moves-up-all-time-list-warriors-blow-out-pelicans-2026-11-10/"}
        ],
        "content": """## Curry reaches another career milestone

Stephen Curry delivered a vintage shooting exhibition on Monday, 9 November, scoring 25 points in just 21 minutes as the Golden State Warriors dismantled the New Orleans Pelicans 138-87 at Chase Center. Curry hit four 3-pointers to reach 26,803 career regular-season points, passing DeMar DeRozan (26,800) for 16th place on the NBA's all-time scoring leaderboard.

Golden State blew the game open in the first quarter with a 38-19 onslaught, shooting 57 percent from the field and leading by as many as 53 points in the second half. Brandin Podziemski matched Curry with 25 points, including five 3-pointers, while rookie forward Yaxel Lendeborg electrified the home crowd with 23 points, seven rebounds and four assists in 24 minutes off the bench.

## Warriors streak reaches eight

The 51-point blowout extended Golden State's winning streak to eight games, improving their record to 8-3 and vaulting them into third place in the Western Conference. New Orleans dropped to 3-7 on the season."""
    }
]

for s in stories_data:
    p = os.path.join(STORIES, s["filename"])
    sources_yaml = "\n".join([f"  - name: \"{src['name']}\"\n    url: \"{src['url']}\"" for src in s["sources"]])
    frontmatter = f"""---
title: "{s['title']}"
subtitle: "{s['subtitle']}"
category: "{s['category']}"
excerpt: "{s['excerpt']}"
image: "{s['image']}"
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

# Update sports.ts
sports_ts_content = """export const SITE_TODAY = '2026-11-10';

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
    slug: 'tennis',
    label: 'Tennis',
    short: 'Tennis',
    href: '/sport/tennis',
    tagline: 'Rolex Paris Masters Final: Carlos Alcaraz battles past Ben Shelton 7-6(5), 7-5 to capture maiden Bercy crown.',
    liveNow: 'Paris Masters Final: Alcaraz def. Shelton 7-6(5), 7-5. Alcaraz saves key break points and captures his 9th ATP Masters 1000 title.',
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: 'ROLEX PARIS MASTERS FINAL: CARLOS ALCARAZ DOWNS BEN SHELTON IN STRAIGHT SETS FOR 9TH MASTERS CROWN',
    board: 'Open the court',
    span: 'hero',
  },
  {
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: 'São Paulo GP: Lando Norris wins chaotic Interlagos race as Mercedes officially clinches 2026 Constructors title.',
    liveNow: 'Interlagos Race Final: Norris P1 (McLaren), Verstappen P2 (from 21st), Hadjar P3. Russell P4 and Antonelli P5 seal title for Mercedes.',
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: 'F1 SAO PAULO GP: LANDO NORRIS WINS DRAMATIC WET RACE AS MERCEDES CLINCHES CONSTRUCTORS TITLE',
    board: 'Open the grid',
    span: 'side',
  },
  {
    slug: 'football',
    label: 'Football',
    short: 'NFL',
    href: '/sport/football',
    tagline: 'NFL Week 9 MNF: James Cook rushes for 107 yards as Bills stifle Vikings 23-6 in Minneapolis.',
    liveNow: 'Final at U.S. Bank Stadium: Bills 23, Vikings 6. Cook 107 yds, 1 TD; Allen 235 yds, 1 TD. Buffalo hands Minnesota (7-1) its first defeat.',
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: 'NFL WEEK 9 MNF: BUFFALO BILLS STIFLE VIKINGS 23-6 TO HAND MINNESOTA FIRST DEFEAT',
    board: 'Open the field',
    span: 'half',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: 'WWT Championship: 19-year-old Blades Brown edges Ben James in playoff for historic maiden PGA Tour victory.',
    liveNow: 'Final Round at Diamante: Blades Brown (-24) def. Ben James (-24) on 2nd playoff hole to become youngest PGA Tour winner in 95 years.',
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: 'PGA TOUR CABO: BLADES BROWN EDGES BEN JAMES IN PLAYOFF TO WIN HISTORIC WWT CHAMPIONSHIP',
    board: 'Open the course',
    span: 'half',
  },
  {
    slug: 'soccer',
    label: 'Soccer',
    short: 'Soccer',
    href: '/sport/soccer',
    tagline: 'Premier League MW10: Martin Ødegaard winner against Hull sends Arsenal six points clear atop the table.',
    liveNow: 'Final at Emirates: Arsenal 1-0 Hull City (Odegaard 72\\'). Arsenal move to 27 points from 10 matches after City fall 3-1 at Forest.',
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: 'PREMIER LEAGUE MW10: MARTIN ODEGAARD 72ND-MINUTE STRIKE FIRES ARSENAL SIX POINTS CLEAR',
    board: 'Open the pitch',
    span: 'half',
  },
  {
    slug: 'basketball',
    label: 'Basketball',
    short: 'Hoops',
    href: '/sport/basketball',
    tagline: 'NBA: Stephen Curry scores 25 points and passes DeRozan for 16th all-time as Warriors demolish Pelicans 138-87.',
    liveNow: 'Final at Chase Center: Warriors 138, Pelicans 87. Curry 25 pts (passes DeRozan); Podziemski 25 pts; Lendeborg 23 pts. Golden State wins 8th straight.',
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: 'NBA: STEPHEN CURRY HITS ALL-TIME MILESTONE AS WARRIORS DEMOLISH PELICANS 138-87',
    board: 'Open the floor',
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

# Update desk.json
desk_path = os.path.join(ROOT, "frontend/src/data/desk.json")
with open(desk_path, "r", encoding="utf-8") as f:
    desk = json.load(f)

desk["asOf"] = "2026-11-10"

# Updated Premier League Table for MW10
desk["premierLeagueTable"] = [
    {"pos": 1, "team": "Arsenal", "p": 10, "w": 9, "d": 0, "l": 1, "gf": 15, "ga": 5, "gd": 10, "pts": 27},
    {"pos": 2, "team": "Manchester City", "p": 10, "w": 7, "d": 0, "l": 3, "gf": 21, "ga": 13, "gd": 8, "pts": 21},
    {"pos": 3, "team": "Brighton", "p": 10, "w": 6, "d": 1, "l": 3, "gf": 24, "ga": 9, "gd": 15, "pts": 19},
    {"pos": 4, "team": "Liverpool", "p": 10, "w": 5, "d": 3, "l": 2, "gf": 14, "ga": 10, "gd": 4, "pts": 18},
    {"pos": 5, "team": "Chelsea", "p": 10, "w": 5, "d": 1, "l": 4, "gf": 19, "ga": 16, "gd": 3, "pts": 16},
    {"pos": 6, "team": "Everton", "p": 10, "w": 4, "d": 4, "l": 2, "gf": 12, "ga": 10, "gd": 2, "pts": 16},
    {"pos": 7, "team": "Leeds", "p": 10, "w": 4, "d": 2, "l": 4, "gf": 11, "ga": 12, "gd": -1, "pts": 14},
    {"pos": 8, "team": "Brentford", "p": 10, "w": 3, "d": 5, "l": 2, "gf": 17, "ga": 13, "gd": 4, "pts": 14},
    {"pos": 9, "team": "Tottenham", "p": 10, "w": 3, "d": 3, "l": 4, "gf": 13, "ga": 11, "gd": 2, "pts": 12},
    {"pos": 10, "team": "Aston Villa", "p": 10, "w": 3, "d": 3, "l": 4, "gf": 11, "ga": 15, "gd": -4, "pts": 12}
]

# Update F1 Constructors and Drivers
desk["f1Constructors"] = [
    {"pos": 1, "name": "Mercedes (Champions)", "pts": 652},
    {"pos": 2, "name": "Ferrari", "pts": 512},
    {"pos": 3, "name": "Red Bull", "pts": 415},
    {"pos": 4, "name": "McLaren", "pts": 390}
]

desk["f1Drivers"] = [
    {"pos": 1, "name": "Kimi Antonelli (Champion)", "pts": 390},
    {"pos": 2, "name": "Max Verstappen", "pts": 279},
    {"pos": 3, "name": "George Russell", "pts": 262},
    {"pos": 4, "name": "Lewis Hamilton", "pts": 259},
    {"pos": 5, "name": "Charles Leclerc", "pts": 253},
    {"pos": 6, "name": "Lando Norris", "pts": 246}
]

# Append Sunday Madrid and Monday Night Football games
nfl_notes = desk.get("nflWeek1", [])
# check if already added
if not any("Bills 23, Vikings 6" in x.get("note", "") for x in nfl_notes):
    nfl_notes.append({
        "date": "2026-11-08",
        "time": "9:30 a.m. ET",
        "home": "Atlanta Falcons",
        "away": "Cincinnati Bengals",
        "note": "FINAL: Bengals 34, Falcons 17. NFL Network Madrid Game at Santiago Bernabeu. Burrow 24-29, 271 yds, 4 total TDs (3 pass, 1 rush). Chase 10 rec, 155 yds, 1 TD. Bengals 6-2, Falcons 3-6."
    })
    nfl_notes.append({
        "date": "2026-11-09",
        "time": "8:15 p.m. ET",
        "home": "Minnesota Vikings",
        "away": "Buffalo Bills",
        "note": "FINAL: Bills 23, Vikings 6. ESPN Monday Night Football at U.S. Bank Stadium. Cook 107 yds, 1 TD; Allen 235 yds, 1 TD. Bills defense hands Minnesota (7-1) first loss. Bills improve to 7-2."
    })
desk["nflWeek1"] = nfl_notes

# Append Paris SF and Final
tennis_notes = desk.get("usOpenQF", [])
if not any("Alcaraz 7-6 (5), 7-5" in x.get("status", "") for x in tennis_notes):
    tennis_notes.append({
        "draw": "Paris SF",
        "p1": "Carlos Alcaraz",
        "p2": "Casper Ruud",
        "status": "Alcaraz 6-4, 6-2"
    })
    tennis_notes.append({
        "draw": "Paris Final",
        "p1": "Carlos Alcaraz",
        "p2": "Ben Shelton",
        "status": "Alcaraz 7-6 (5), 7-5"
    })
desk["usOpenQF"] = tennis_notes

dump(desk_path, desk)

# Update AGENTS.md line 14
agents_path = os.path.join(ROOT, "AGENTS.md")
with open(agents_path, "r", encoding="utf-8") as f:
    agents_lines = f.readlines()

for i, line in enumerate(agents_lines):
    if "*   **Site clock:**" in line:
        agents_lines[i] = "*   **Site clock:** editorial today is `2026-11-10` in `frontend/src/data/sports.ts` (`SITE_TODAY`). Tennis: Carlos Alcaraz beats Ben Shelton 7-6(5), 7-5 to win his first Rolex Paris Masters title and 9th Masters 1000 crown. Formula 1: Lando Norris wins wet Sao Paulo GP at Interlagos; Max Verstappen charges from 21st to 2nd; Mercedes clinches 2026 Constructors' Championship. Football: Bills beat Vikings 23-6 on Week 9 MNF; Cook 107 yds, 1 TD; Vikings drop to 7-1, Bills 7-2. Sunday Madrid: Bengals 34, Falcons 17 at Bernabeu; Burrow 4 TDs. Golf: 19-year-old Blades Brown beats Ben James on second playoff hole at El Cardonal to win WWT Championship. Soccer: Martin Odegaard 72nd-minute winner as Arsenal beat Hull 1-0; Arsenal six clear on 27 points after City 1-3 Forest. Basketball: Stephen Curry scores 25 and passes DeRozan for 16th all-time as Warriors blow out Pelicans 138-87 for eighth straight win.\n"
        break

with open(agents_path, "w", encoding="utf-8") as f:
    f.writelines(agents_lines)
print("updated AGENTS.md")

