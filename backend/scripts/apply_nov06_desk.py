#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Apply verified 6 November 2026 desk: matches, stories, sports.ts, desk.json, AGENTS.md."""
import json
import os
import re
import urllib.request

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
MATCHES = os.path.join(ROOT, "frontend/src/content/matches")
STORIES = os.path.join(ROOT, "frontend/src/content/stories")

IMG = {
    "nfl": "https://images.pexels.com/photos/159745/pexels-photo-159745.jpeg?auto=compress&cs=tinysrgb&w=1600&h=900&fit=crop",
    "nba": "https://images.pexels.com/photos/1337386/pexels-photo-1337386.jpeg?auto=compress&cs=tinysrgb&w=1600&h=900&fit=crop",
    "ten": "https://images.pexels.com/photos/5739187/pexels-photo-5739187.jpeg?auto=compress&cs=tinysrgb&w=1600&h=900&fit=crop",
    "f1": "https://images.pexels.com/photos/1280361/pexels-photo-1280361.jpeg?auto=compress&cs=tinysrgb&w=1600&h=900&fit=crop",
    "golf": "https://images.pexels.com/photos/274133/pexels-photo-274133.jpeg?auto=compress&cs=tinysrgb&w=1600&h=900&fit=crop",
    "soc": "https://images.pexels.com/photos/47730/the-ball-stadion-football-the-pitch-47730.jpeg?auto=compress&cs=tinysrgb&w=1600&h=900&fit=crop",
}

def dump(path, obj):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print("wrote", path)

nfl = {
  "slug": "jaguars-at-ravens-tnf-week9-2026",
  "headline": "NFL Week 9 TNF: Jaguars thrash depleted Ravens 33-10 behind Lawrence, four Little field goals",
  "whyCareScore": 9.6,
  "whyCareReason": "Trevor Lawrence throws for 242 yards and a 50-yard touchdown to Parker Washington as Jacksonville forces three turnovers and improves to 6-2 against a Ravens side starting Joe Fagnano.",
  "teaser": "FINAL: Jaguars 33, Ravens 10. Quarters 10-7-3-13 / 3-0-0-7. Jacksonville fifth win in six games on Prime Video in Baltimore rain.",
  "story": "The Jacksonville Jaguars beat the Baltimore Ravens and a wet Thursday night 33-10 on 5 November at M&T Bank Stadium, improving to 6-2 while Baltimore fell to 4-5 with a fourth straight loss. Trevor Lawrence completed 16 of 26 passes for 242 yards and a 50-yard touchdown to Parker Washington. Cam Little tied a career high with four field goals. Bhayshul Tuten scored on a 1-yard run and Chris Rodriguez Jr. added a 2-yard score. Joe Fagnano, starting because Lamar Jackson (thumb) and Tyler Huntley (turf toe) were out, went 10 of 18 for 60 yards with two interceptions. Justice Hill broke a 65-yard touchdown, finishing 9 carries for 85 yards. Jacksonville's defense collected two interceptions and a fumble recovery, holding Baltimore to 227 yards and 10 first downs. Crowd: 70,007.",
  "stakes": "Jaguars move to 6-2 with a fifth win in six games. Ravens drop to 4-5 after a fourth consecutive defeat. Steelers remain 6-2 atop the AFC North.",
  "rivalryAngle": "Prime Video TNF in the rain at M&T Bank Stadium, with Baltimore forced into a Wildcat package around Derrick Henry and a first NFL start for Fagnano.",
  "funFacts": [
    "Cam Little tied his career high with four field goals.",
    "Justice Hill's 65-yard run snapped Jacksonville's 24-game streak of not allowing a 75-yard rusher.",
    "This was Jacksonville's third consecutive game played in rain after London in Week 6 and last Sunday's 42-7 win over Indianapolis."
  ],
  "keyPlayers": [
    {"name": "Trevor Lawrence", "team": "Jacksonville Jaguars", "hook": "Completed 16 of 26 for 242 yards and a 50-yard touchdown to Parker Washington."},
    {"name": "Cam Little", "team": "Jacksonville Jaguars", "hook": "Tied a career high with four field goals in the 33-10 win."},
    {"name": "Joe Fagnano", "team": "Baltimore Ravens", "hook": "First NFL start: 10 of 18, 60 yards, two interceptions with Jackson and Huntley out."}
  ],
  "headToHead": "Thursday 5 November 2026. M&T Bank Stadium, Baltimore. Final: JAX 33, BAL 10.",
  "tags": ["football", "nfl", "jaguars", "ravens", "tnf", "thursday-night-football", "trevor-lawrence", "joe-fagnano"],
  "home": "Baltimore Ravens",
  "away": "Jacksonville Jaguars",
  "homeCode": "USA",
  "awayCode": "USA",
  "homeFlag": "us",
  "awayFlag": "us",
  "group": "NFL Week 9",
  "matchday": 9,
  "date": "2026-11-05",
  "time": "20:15",
  "venue": "M&T Bank Stadium",
  "city": "Baltimore",
  "status": "FINISHED",
  "homeScore": 10,
  "awayScore": 33,
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
  "roundLabel": "Week 9 TNF",
  "resultSummary": "FINAL: Jaguars 33, Ravens 10. Lawrence 16/26, 242 yds, 50-yd TD; Little 4 FGs; Fagnano 10/18, 60 yds, 2 INT.",
  "leaderboard": [],
  "tennisSets": [],
  "sources": [
    {"name": "ESPN NFL recap: Jaguars 33-10 Ravens", "url": "https://www.espn.com/nfl/recap?gameId=401873037"},
    {"name": "ESPN story: Lawrence, Jags topple Fagnano, Ravens on TNF", "url": "https://www.espn.com/nfl/story/_/id/50395188/jaguars-ravens-thursday-night-football-joe-fagnano"},
    {"name": "Baltimore Ravens official game center", "url": "https://www.baltimoreravens.com/game-day/2026/reg-week9/jaguars-at-ravens/"}
  ]
}

nba = {
  "slug": "nba-spurs-vs-mavericks-wembanyama-52-2026",
  "headline": "NBA: Wembanyama posts 52 points, 24 rebounds, 8 blocks as Spurs edge Mavericks 112-111",
  "whyCareScore": 9.8,
  "whyCareReason": "Victor Wembanyama becomes the first player since Bob McAdoo in 1974 with 50-plus points, 20-plus rebounds and 5-plus blocks, then hits the winning free throw with 24.2 seconds left.",
  "teaser": "FINAL: Spurs 112, Mavericks 111. Wembanyama 52-24-8; winning FT 24.2s left; Irving miss at 2.5s. San Antonio sixth straight, 6-2.",
  "story": "Victor Wembanyama set career highs of 52 points and 24 rebounds, added eight blocks, and sank the winning free throw with 24.2 seconds left as the San Antonio Spurs beat the Dallas Mavericks 112-111 on Wednesday night, 4 November, at Frost Bank Center. The French center went 16 of 28 from the field, 19 of 23 from the line and 1 of 8 from three in 34 minutes, playing through a recent virus and a rolled ankle. He had 29 points, 15 rebounds and five blocks in the first half. Dylan Harper scored 21, Stephon Castle 17 with 10 rebounds, De'Aaron Fox 10. Naji Marshall had 22, P.J. Washington 21, Cooper Flagg 19. Kyrie Irving scored 29 and missed a contested turnaround with 2.5 seconds left. The Spurs are 6-2 on a six-game winning streak. Philadelphia leads the East at 8-1. Cleveland is 4-4 after a 124-116 loss at Oklahoma City on 4 November.",
  "stakes": "Spurs extend their winning streak to six and sit 6-2. Dallas falls in a one-possession finish after Wembanyama's historic line.",
  "rivalryAngle": "Texas rivalry night: Wembanyama's career night holds off Irving, Marshall, Washington and Flagg after Dallas erased a 19-point deficit.",
  "funFacts": [
    "Wembanyama is the first player since Bob McAdoo in 1974 with at least 50 points, 20 rebounds and 5 blocks in a game.",
    "He is the first player in the play-by-play era (since 1996-97) with 25 points, 10 rebounds and 5 blocks in a half.",
    "San Antonio was plus-23 with Wembanyama on the floor."
  ],
  "keyPlayers": [
    {"name": "Victor Wembanyama", "team": "San Antonio Spurs", "hook": "Career highs 52 points and 24 rebounds plus 8 blocks; winning free throw with 24.2 seconds left."},
    {"name": "Dylan Harper", "team": "San Antonio Spurs", "hook": "Added 21 points beside Wembanyama in the 112-111 win."},
    {"name": "Kyrie Irving", "team": "Dallas Mavericks", "hook": "Scored 29 points and missed the potential winner with 2.5 seconds left."}
  ],
  "headToHead": "Wednesday 4 November 2026. Frost Bank Center, San Antonio. Final: SAS 112, DAL 111.",
  "tags": ["basketball", "nba", "spurs", "mavericks", "wembanyama", "irving", "harper"],
  "home": "San Antonio Spurs",
  "away": "Dallas Mavericks",
  "homeCode": "USA",
  "awayCode": "USA",
  "homeFlag": "us",
  "awayFlag": "us",
  "group": "NBA Regular Season",
  "matchday": 8,
  "date": "2026-11-04",
  "time": "20:00",
  "venue": "Frost Bank Center",
  "city": "San Antonio",
  "status": "FINISHED",
  "homeScore": 112,
  "awayScore": 111,
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
  "resultSummary": "FINAL: Spurs 112, Mavericks 111. Wembanyama 52 pts, 24 reb, 8 blk; Harper 21; Irving 29.",
  "leaderboard": [],
  "tennisSets": [],
  "sources": [
    {"name": "NBA.com: Wembanyama 52 points, 24 rebounds as Spurs top Mavs", "url": "https://www.nba.com/news/spurs-victor-wembanyama-52-points-mavericks"},
    {"name": "Reuters: Wembanyama pours in 52 as Spurs edge Mavericks", "url": "https://www.reuters.com/sports/basketball/victor-wembanyama-pours-52-spurs-edge-mavericks--flm-2026-11-05/"},
    {"name": "BBC Sport: Career-best Wembanyama display seals Spurs win", "url": "https://www.bbc.co.uk/sport/basketball/articles/cw4g1m6rlvxpo"}
  ]
}

ten = {
  "slug": "atp-paris-masters-2026-shelton-vs-paul-qf",
  "headline": "Rolex Paris Masters QF: Ben Shelton beats Tommy Paul 6-4, 4-6, 6-3 to reach first Bercy semi-final",
  "whyCareScore": 9.4,
  "whyCareReason": "Third seed Shelton fires 19 aces in 1 hour 46 minutes, ends Paul's Turin bid and locks Frances Tiafoe into the Nitto ATP Finals.",
  "teaser": "FINAL: Shelton def. Paul 6-4, 4-6, 6-3. First Paris Masters semi-final for Shelton; Paul out of the race to Turin.",
  "story": "Ben Shelton beat fellow American Tommy Paul 6-4, 4-6, 6-3 on Friday, 6 November, in the Rolex Paris Masters quarter-finals at Accor Arena. The third seed needed 1 hour 46 minutes, struck 19 aces to Paul's 7, converted two of four break points and won 81 of 154 points. Shelton had already qualified for Turin; this result ended Paul's Nitto ATP Finals hopes and confirmed Frances Tiafoe's first qualification. Shelton is the first American into the Paris last four since Jack Sock and John Isner in 2017. He next plays Luca Van Assche or Rinky Hijikata. Thursday round of 16 still stands: Shelton d Rinderknech 3-6, 6-4, 7-6(5); Fritz d Fils 6-3, 6-4; Paul d Halys 7-6(3), 6-4. Alcaraz vs Fritz and Ruud vs Borges were still to play Friday night. Van Assche vs Hijikata was in progress and is not published as finished.",
  "stakes": "Shelton reaches his first Bercy semi-final. Paul is eliminated from the Turin race. Tiafoe is into the ATP Finals.",
  "rivalryAngle": "All-American quarter-final between close friends: Shelton leads the head-to-head 3-2 after this win.",
  "funFacts": [
    "Shelton served 19 aces and won 82 percent of first-serve points (48 of 63).",
    "This is Shelton's first ATP Masters 1000 semi-final outside his two title runs in Canada.",
    "Frances Tiafoe became the seventh qualifier for Turin after Zverev, Alcaraz, Shelton, Medvedev, Cobolli and Fils."
  ],
  "keyPlayers": [
    {"name": "Ben Shelton", "team": "United States", "hook": "Won 6-4, 4-6, 6-3 with 19 aces to reach his first Paris Masters semi-final."},
    {"name": "Tommy Paul", "team": "United States", "hook": "Took the second set 6-4 but lost the decider; Turin bid ends."}
  ],
  "headToHead": "Friday 6 November 2026. Accor Arena, Paris. Final: Shelton 6-4, 4-6, 6-3.",
  "tags": ["tennis", "atp", "paris-masters", "rolex-paris-masters", "shelton", "paul", "bercy"],
  "home": "Ben Shelton",
  "away": "Tommy Paul",
  "homeCode": "USA",
  "awayCode": "USA",
  "homeFlag": "us",
  "awayFlag": "us",
  "group": "Rolex Paris Masters",
  "matchday": 5,
  "date": "2026-11-06",
  "time": "14:00",
  "venue": "Accor Arena",
  "city": "Paris",
  "status": "FINISHED",
  "homeScore": "2",
  "awayScore": "1",
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
  "roundLabel": "Quarter-final",
  "resultSummary": "FINAL: Ben Shelton def. Tommy Paul 6-4, 4-6, 6-3 to reach Paris SFs.",
  "leaderboard": [],
  "tennisSets": [{"p1": "6", "p2": "4"}, {"p1": "4", "p2": "6"}, {"p1": "6", "p2": "3"}],
  "sources": [
    {"name": "ATP Tour: Shelton shuts down Paul's Turin hopes, reaches Paris SFs", "url": "https://www.atptour.com/en/news/shelton-paul-paris-2026-qf"},
    {"name": "ATP Tour Paris results", "url": "https://www.atptour.com/en/scores/current/paris/352/results"}
  ]
}

f1 = {
  "slug": "sao-paulo-gp-interlagos-2026",
  "headline": "São Paulo GP FP1: Lando Norris leads Kimi Antonelli and Max Verstappen at Interlagos",
  "whyCareScore": 9.3,
  "whyCareReason": "Norris posts 1:11.717 in an upgraded McLaren, 0.082s clear of newly crowned champion Antonelli, on a standard weekend with no Sprint. Mercedes lead Ferrari 630-504 in constructors.",
  "teaser": "FP1: Norris 1:11.717; Antonelli +0.082s; Verstappen +0.236s; Hamilton +0.324s. No Sprint this weekend. Qualifying Saturday, race Sunday.",
  "story": "Lando Norris finished fastest in Free Practice 1 for the Grande Premio de São Paulo on Friday, 6 November, at Autodromo Jose Carlos Pace. The McLaren driver lapped in 1:11.717, 0.082 seconds ahead of world champion Kimi Antonelli and 0.236s ahead of Max Verstappen. Lewis Hamilton was fourth (+0.324s) on his 400th Grand Prix weekend, George Russell fifth (+0.386s). Isack Hadjar was sixth, Gabriel Mini seventh in for Pierre Gasly, Gabriel Bortoleto eighth at his home race. Leonardo Fornaroli ran Piastri's McLaren. Rafael Camara made his Haas Grand Prix weekend debut in 18th. Dino Beganovic ran for Ferrari with Charles Leclerc away after the birth of his daughter. Freddie Slater stopped in Nico Hulkenberg's Audi. This is a conventional weekend: FP1 and FP2 Friday, FP3 and qualifying Saturday, race Sunday. There is no Sprint. After Mexico, ESPN and FIA standings list Antonelli champion on 380 points, Verstappen 261, Hamilton 259, Russell 250, Leclerc 245, Norris 221. Constructors: Mercedes 630, Ferrari 504 (gap 126), Red Bull 382, McLaren 365. Mexico City race result: Verstappen won, Hamilton second, Antonelli third to clinch the title. FP2 times are not published here.",
  "stakes": "Mercedes can clinch the constructors' championship this weekend with a 126-point lead over Ferrari and four races remaining. Drivers' title is already settled.",
  "rivalryAngle": "McLaren upgrades vs champion Mercedes vs Verstappen's Red Bull vs Hamilton's Ferrari on the Interlagos climb.",
  "funFacts": [
    "There is no Sprint in São Paulo in 2026: FP1, FP2, FP3, qualifying, race.",
    "Hamilton is contesting his 400th Grand Prix weekend.",
    "Rafael Camara made his Haas F1 race-weekend debut at his home circuit and finished 18th in FP1."
  ],
  "keyPlayers": [
    {"name": "Lando Norris", "team": "McLaren", "hook": "Set the FP1 benchmark at 1:11.717 in an upgraded McLaren."},
    {"name": "Kimi Antonelli", "team": "Mercedes", "hook": "Second, 0.082s off Norris, beginning his title reign on 380 points."},
    {"name": "Max Verstappen", "team": "Red Bull", "hook": "Third at +0.236s after winning the Mexico City Grand Prix."}
  ],
  "headToHead": "Friday 6 November 2026. Autodromo Jose Carlos Pace, São Paulo. FP1 complete.",
  "tags": ["f1", "formula-1", "sao-paulo-gp", "interlagos", "norris", "antonelli", "verstappen", "fp1"],
  "home": "Lando Norris",
  "away": "Kimi Antonelli",
  "homeCode": "GBR",
  "awayCode": "ITA",
  "homeFlag": "gb-eng",
  "awayFlag": "it",
  "group": "Formula 1",
  "matchday": 21,
  "date": "2026-11-06",
  "time": "11:30",
  "venue": "Autodromo Jose Carlos Pace",
  "city": "São Paulo",
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
  "roundLabel": "Free Practice 1",
  "resultSummary": "FP1: Norris 1:11.717; Antonelli +0.082s; Verstappen +0.236s; Hamilton +0.324s. No Sprint weekend.",
  "leaderboard": [
    {"pos": "1", "name": "Lando Norris (McLaren)", "score": "1:11.717", "note": "FP1 fastest"},
    {"pos": "2", "name": "Kimi Antonelli (Mercedes)", "score": "+0.082s", "note": "World Champion"},
    {"pos": "3", "name": "Max Verstappen (Red Bull)", "score": "+0.236s", "note": "Mexico winner"},
    {"pos": "4", "name": "Lewis Hamilton (Ferrari)", "score": "+0.324s", "note": "400th GP weekend"},
    {"pos": "5", "name": "George Russell (Mercedes)", "score": "+0.386s", "note": "P5"}
  ],
  "tennisSets": [],
  "sources": [
    {"name": "Formula 1: FP1 Norris leads Antonelli and Verstappen", "url": "https://www.formula1.com/en/latest/article/fp1-norris-leads-antonelli-and-verstappen-in-opening-sao-paulo-gp-practice-session.3GXL3rAROwHsLxnxn9hReY"},
    {"name": "ESPN F1 2026 drivers standings", "url": "https://www.espn.com/f1/standings"},
    {"name": "Sky Sports F1: Norris tops Brazil first practice", "url": "https://www.skysports.com/f1/news/13608857/sao-paulo-gp-lando-norris-tops-brazil-first-practice-in-upgraded-mclaren-from-kimi-antonelli-and-max-verstappen"}
  ]
}

golf = {
  "slug": "wwt-championship-diamante-cabo-2026",
  "headline": "WWT Championship Round 1: Chris Kirk fires bogey-free 63 to lead by one at El Cardonal",
  "whyCareScore": 9.1,
  "whyCareReason": "Kirk, 110th in FedExCup Fall, shoots 9-under 63 with every fairway hit to lead Nick Dunlap and Zac Blair by one as 2027 PGA Tour cards hang in the balance.",
  "teaser": "R1 COMPLETE: Chris Kirk 63 (-9) leads Dunlap and Blair 64. T4 at 65: Pavon, Hall, Montgomery, Hirata, Ben James. Purse $6 million. Round 2 in progress, not final.",
  "story": "Chris Kirk posted a bogey-free 9-under 63 on Thursday, 5 November, to lead the World Wide Technology Championship after round one at El Cardonal at Diamante in Los Cabos. Associated Press and PGA Tour reports say he hit every fairway and missed only one green on the Tiger Woods design (par 72, 7,452 yards). Nick Dunlap and Zac Blair shot 64. Tied for fourth at 65: Matthieu Pavon, Harry Hall, Taylor Montgomery, Kensei Hirata and Ben James. More than half of the 120-player field broke 70. Kirk sits about 110th in FedExCup Fall with three events left to finish inside the top 100 and keep a full 2027 card. The purse is $6 million. Round 2 was in progress on Friday and is not published as a finished board.",
  "stakes": "Fall Series card race: Kirk needs a top-100 FedExCup Fall finish. Winner takes the $6 million purse event.",
  "rivalryAngle": "Kirk's first 18-hole lead of the week vs Dunlap, Blair and a five-way logjam at 7-under on the Baja coast.",
  "funFacts": [
    "Kirk putted for birdie on 17 of 18 holes; his only missed green was the par-3 second.",
    "The 63 matches his lowest round of the season and sits one off his career-low 62.",
    "Ben James, No. 1 from PGA Tour University, is already locked for a 2027 card and opened 65."
  ],
  "keyPlayers": [
    {"name": "Chris Kirk", "team": "United States", "hook": "Bogey-free 63, one-shot lead, FedExCup Fall No. 110."},
    {"name": "Nick Dunlap", "team": "United States", "hook": "Opening 64, tied for second with Zac Blair."},
    {"name": "Zac Blair", "team": "United States", "hook": "Birdied four of his last five holes to reach 8-under 64."}
  ],
  "headToHead": "Thursday 5 November 2026. El Cardonal at Diamante, Los Cabos. Round 1 complete.",
  "tags": ["golf", "pga-tour", "wwt-championship", "los-cabos", "el-cardonal", "diamante", "chris-kirk"],
  "home": "Chris Kirk",
  "away": "Nick Dunlap",
  "homeCode": "USA",
  "awayCode": "USA",
  "homeFlag": "us",
  "awayFlag": "us",
  "group": "PGA Tour",
  "matchday": 5,
  "date": "2026-11-05",
  "time": "08:00",
  "venue": "El Cardonal at Diamante",
  "city": "Los Cabos",
  "status": "FINISHED",
  "homeScore": "-9",
  "awayScore": "-8",
  "marquee": False,
  "liveMinute": None,
  "image": IMG["golf"],
  "decidedBy": "score",
  "homePen": None,
  "awayPen": None,
  "sport": "golf",
  "competition": "pga-tour-2026",
  "format": "leaderboard",
  "season": "2026",
  "roundLabel": "Round 1",
  "resultSummary": "R1: Chris Kirk 63 (-9) leads Nick Dunlap and Zac Blair 64. Purse $6 million.",
  "leaderboard": [
    {"pos": "1", "name": "Chris Kirk", "score": "-9 (63)", "note": "Leader, bogey-free"},
    {"pos": "T2", "name": "Nick Dunlap", "score": "-8 (64)", "note": "T2"},
    {"pos": "T2", "name": "Zac Blair", "score": "-8 (64)", "note": "T2"},
    {"pos": "T4", "name": "Matthieu Pavon", "score": "-7 (65)", "note": "T4"},
    {"pos": "T4", "name": "Harry Hall", "score": "-7 (65)", "note": "T4"},
    {"pos": "T4", "name": "Taylor Montgomery", "score": "-7 (65)", "note": "T4"},
    {"pos": "T4", "name": "Kensei Hirata", "score": "-7 (65)", "note": "T4"},
    {"pos": "T4", "name": "Ben James", "score": "-7 (65)", "note": "T4"}
  ],
  "tennisSets": [],
  "sources": [
    {"name": "PGA Tour: Kirk fires bogey-free 63, grabs early lead", "url": "https://www.pgatour.com/article/news/daily-wrapup/2026/11/05/round-1-world-wide-technology-championship-recap-el-cardonal-scores-leaderboard-results"},
    {"name": "ESPN/AP: Chris Kirk leads after 63", "url": "https://www.espn.com/golf/story/_/id/50394522/chris-kirk-leads-pga-tour-world-wide-technology-champ"},
    {"name": "AP News par scores, purse $6 million", "url": "https://apnews.com/article/golf-3c730f124aa1ce9bd091b57cb2bc60fd"}
  ]
}

soccer = {
  "slug": "rb-leipzig-vs-man-city-ucl-md4-2026",
  "headline": "UCL MD4: Haaland winner as Manchester City edge RB Leipzig 3-2",
  "whyCareScore": 9.5,
  "whyCareReason": "Captain Erling Haaland taps in Elliot Anderson's 78th-minute cross for a 3-2 win that lifts City to 3-1 in the league phase, seventh in the table.",
  "teaser": "FINAL: RB Leipzig 2-3 Manchester City. Lukeba OG 37, Baku 49, Enzo Fernandez 58, Nusa 61, Haaland 78. City 3-1 in league phase.",
  "story": "Manchester City beat RB Leipzig 3-2 on Wednesday, 4 November, at Red Bull Arena on Champions League matchday 4. Castello Lukeba turned Nico O'Reilly's cross into his own net in the 37th minute. Ridle Baku equalised in the 49th, squeezing a finish in at Gianluigi Donnarumma's near post. Enzo Fernandez headed City back in front in the 58th from Iliman Ndiaye's cross. Antonio Nusa levelled in the 61st from Christopher Nkunku's pass. Haaland, captain for the night, slid in Anderson's low cross in the 78th for the winner, his 13th goal in nine appearances against Leipzig. City sit 3-1 in the league phase, seventh, inside the automatic last-16 places. Enzo Maresca's side had lost to Brighton in the Premier League. Other MD4 results include Slavia Prague 1-2 Arsenal. Premier League table after matchweek 9 (BBC, NBC, 6 November): Arsenal 24, Manchester City 21, Brighton 19, Chelsea 16, Liverpool 15. Next Premier League fixture is Everton vs Coventry on Friday 6 November at 20:00 GMT, unpublished here as unfinished.",
  "stakes": "City move to 3-1 in the UCL league phase and seventh place. Leipzig suffer a third European defeat after losses to Como and Real Madrid.",
  "rivalryAngle": "Haaland vs his former Bundesliga club: 13 goals in nine games against Leipzig, his most versus any opponent.",
  "funFacts": [
    "Haaland scored with his first real chance after a quiet night, his 14th goal of the season.",
    "Leipzig had won five straight home matches without conceding before this game.",
    "Both sides hit the woodwork late: David Raum and Rayan Cherki struck the bar."
  ],
  "keyPlayers": [
    {"name": "Erling Haaland", "team": "Manchester City", "hook": "78th-minute winner from Anderson's cross; 13th goal in nine games vs Leipzig."},
    {"name": "Enzo Fernandez", "team": "Manchester City", "hook": "Powerful 58th-minute header from Ndiaye's cross."},
    {"name": "Antonio Nusa", "team": "RB Leipzig", "hook": "61st-minute equaliser from Nkunku's pass after Baku's 49th-minute strike."}
  ],
  "headToHead": "Wednesday 4 November 2026. Red Bull Arena, Leipzig. Final: Leipzig 2-3 Manchester City.",
  "tags": ["soccer", "ucl", "champions-league", "manchester-city", "rb-leipzig", "haaland"],
  "home": "RB Leipzig",
  "away": "Manchester City",
  "homeCode": None,
  "awayCode": None,
  "homeFlag": "",
  "awayFlag": "",
  "group": "UCL",
  "matchday": 4,
  "date": "2026-11-04",
  "time": "21:00",
  "venue": "Red Bull Arena",
  "city": "Leipzig",
  "status": "FINISHED",
  "homeScore": 2,
  "awayScore": 3,
  "marquee": True,
  "liveMinute": None,
  "image": IMG["soc"],
  "decidedBy": None,
  "homePen": None,
  "awayPen": None,
  "sport": "soccer",
  "competition": "champions-league-2026-27",
  "format": "team-match",
  "season": "2026/27",
  "roundLabel": "Champions League · Matchday 4",
  "resultSummary": "FINAL: RB Leipzig 2-3 Manchester City (Lukeba OG 37, Baku 49, Fernandez 58, Nusa 61, Haaland 78).",
  "leaderboard": [],
  "tennisSets": [],
  "sources": [
    {"name": "Manchester City official match report", "url": "https://www.mancity.com/news/mens/rb-leipzig-manchester-city-uefa-champions-league-match-report-63929402"},
    {"name": "Sky Sports: Haaland late winner at Leipzig", "url": "https://www.skysports.com/football/news/13607404/rb-leipzig-2-3-man-city-erling-haaland-haunts-bundesliga-side-again-with-late-winner-in-champions-league-thriller"},
    {"name": "The Guardian: Haaland settles thriller", "url": "https://www.theguardian.com/football/2026/nov/04/rb-leipzig-manchester-city-champions-league-match-report"}
  ]
}

matches = [nfl, nba, ten, f1, golf, soccer]
for m in matches:
    dump(os.path.join(MATCHES, m["slug"] + ".json"), m)

stories = {
"nfl-week9-tnf-jaguars-33-10-ravens-lawrence-2026.md": f"""---
title: "NFL Week 9 TNF: Jaguars thrash depleted Ravens 33-10 behind Lawrence and four Little field goals"
subtitle: "Jacksonville forces three turnovers on Prime Video in Baltimore rain as Joe Fagnano starts with Jackson and Huntley out."
category: "Desk"
excerpt: "Trevor Lawrence threw for 242 yards and a 50-yard touchdown as the Jacksonville Jaguars beat the Baltimore Ravens 33-10 on Thursday Night Football."
image: "{IMG['nfl']}"
readingTime: 5
pubDate: 2026-11-06
sport: football
competition: nfl-2026
relatedSlug: jaguars-at-ravens-tnf-week9-2026
sources:
  - name: "ESPN NFL recap: Jaguars 33-10 Ravens"
    url: "https://www.espn.com/nfl/recap?gameId=401873037"
  - name: "ESPN story: Lawrence, Jags topple Fagnano, Ravens on TNF"
    url: "https://www.espn.com/nfl/story/_/id/50395188/jaguars-ravens-thursday-night-football-joe-fagnano"
  - name: "Baltimore Ravens official game center"
    url: "https://www.baltimoreravens.com/game-day/2026/reg-week9/jaguars-at-ravens/"
---

## Rain, takeaways, and a 33-10 TNF result

The Jacksonville Jaguars beat the Baltimore Ravens 33-10 on Thursday, 5 November, at M&T Bank Stadium on Prime Video. Jacksonville improved to 6-2 with a fifth win in six games. Baltimore fell to 4-5 after a fourth consecutive loss.

Trevor Lawrence completed 16 of 26 passes for 242 yards and a 50-yard touchdown to Parker Washington. Cam Little tied a career high with four field goals. Bhayshul Tuten scored from a yard out in the first quarter and Chris Rodriguez Jr. added a 2-yard touchdown. The Jaguars outgained Baltimore 319-227 and forced three turnovers, including interceptions by Montaric Brown and Jourdan Lewis.

## Fagnano's first start, Hill's 65-yard run

Joe Fagnano made his first NFL start with Lamar Jackson (right thumb) and Tyler Huntley (turf toe) injured. He finished 10 of 18 for 60 yards and two interceptions. Baltimore used Wildcat snaps to Derrick Henry. Justice Hill broke a 65-yard touchdown, finishing with 9 carries for 85 yards, Baltimore's first second-half touchdown since Week 5.

Quarters ran 10-7-3-13 for Jacksonville and 3-0-0-7 for Baltimore. Crowd: 70,007. Next: Jaguars at Tennessee on 15 November; Ravens host the Chargers on 16 November. Pittsburgh remains 6-2 in the AFC North.
""",
"nba-wembanyama-52-24-8-spurs-edge-mavs-112-111-2026.md": f"""---
title: "NBA: Wembanyama posts 52 points, 24 rebounds, 8 blocks as Spurs edge Mavericks 112-111"
subtitle: "First 50-20-5 block night since Bob McAdoo in 1974, sealed by a free throw with 24.2 seconds left."
category: "Desk"
excerpt: "Victor Wembanyama set career highs of 52 points and 24 rebounds and added eight blocks as San Antonio beat Dallas 112-111 on Wednesday night."
image: "{IMG['nba']}"
readingTime: 5
pubDate: 2026-11-06
sport: basketball
competition: nba-2026-27
relatedSlug: nba-spurs-vs-mavericks-wembanyama-52-2026
sources:
  - name: "NBA.com: Wembanyama 52 points, 24 rebounds as Spurs top Mavs"
    url: "https://www.nba.com/news/spurs-victor-wembanyama-52-points-mavericks"
  - name: "Reuters: Wembanyama pours in 52 as Spurs edge Mavericks"
    url: "https://www.reuters.com/sports/basketball/victor-wembanyama-pours-52-spurs-edge-mavericks--flm-2026-11-05/"
  - name: "BBC Sport: Career-best Wembanyama display seals Spurs win"
    url: "https://www.bbc.co.uk/sport/basketball/articles/cw4g1m6rlvxpo"
---

## A historic line in San Antonio

Victor Wembanyama finished with 52 points, 24 rebounds and eight blocks as the San Antonio Spurs beat the Dallas Mavericks 112-111 on Wednesday, 4 November, at Frost Bank Center. NBA.com and the Associated Press recorded career highs in points and rebounds. He shot 16 of 28 from the field, 19 of 23 from the line and 1 of 8 from three in 34 minutes, playing through a virus and a rolled ankle.

He had 29 points, 15 rebounds and five blocks before halftime, the first 25-10-5 half in the play-by-play era. He is the first player since Bob McAdoo in 1974 with at least 50 points, 20 rebounds and five blocks in a game.

## One free throw, one miss

Dallas erased a 19-point deficit. Naji Marshall tied the game at 111. Wembanyama's free throw with 24.2 seconds left made it 112-111. Kyrie Irving missed a contested turnaround with 2.5 seconds left. Harper scored 21, Castle 17 and 10 rebounds, Fox 10. Marshall had 22, Washington 21, Flagg 19, Irving 29.

San Antonio is 6-2 on a six-game winning streak. Philadelphia leads the East at 8-1. Cleveland is 4-4 after losing 124-116 at Oklahoma City on 4 November (Shai Gilgeous-Alexander 42). Friday's 76ers at Cavaliers game is not published with a score.
""",
"atp-paris-masters-2026-shelton-beats-paul-first-bercy-semi.md": f"""---
title: "Rolex Paris Masters QF: Ben Shelton beats Tommy Paul 6-4, 4-6, 6-3 to reach first Bercy semi-final"
subtitle: "Nineteen aces in 1 hour 46 minutes end Paul's Turin bid and lock Frances Tiafoe into the ATP Finals."
category: "Desk"
excerpt: "Third seed Ben Shelton outlasted Tommy Paul 6-4, 4-6, 6-3 on Friday at Accor Arena to reach his first Rolex Paris Masters semi-final."
image: "{IMG['ten']}"
readingTime: 5
pubDate: 2026-11-06
sport: tennis
competition: atp-1000-paris-2026
relatedSlug: atp-paris-masters-2026-shelton-vs-paul-qf
sources:
  - name: "ATP Tour: Shelton shuts down Paul's Turin hopes, reaches Paris SFs"
    url: "https://www.atptour.com/en/news/shelton-paul-paris-2026-qf"
  - name: "ATP Tour Paris results"
    url: "https://www.atptour.com/en/scores/current/paris/352/results"
---

## All-American quarter-final, American semi-finalist

Ben Shelton beat Tommy Paul 6-4, 4-6, 6-3 on Friday, 6 November, at the Rolex Paris Masters. ATP Tour stats list 19 aces for Shelton, 7 for Paul, two breaks from four chances, and a 1 hour 46 minute match. Shelton won 81 of 154 points and 48 of 63 first-serve points.

The third seed is into his first Paris Masters semi-final, the first American in the last four here since Jack Sock and John Isner in 2017. He next faces Luca Van Assche or Rinky Hijikata. That second quarter-final was still on court and is not listed as finished.

## Turin picture

Shelton had already qualified for the Nitto ATP Finals. This result ended Paul's campaign and confirmed Frances Tiafoe's first Turin berth. Thursday's round of 16: Shelton d Arthur Rinderknech 3-6, 6-4, 7-6(5); Taylor Fritz d Arthur Fils 6-3, 6-4; Paul d Quentin Halys 7-6(3), 6-4. Alcaraz vs Fritz and Ruud vs Borges were still to come Friday night. Alexander Zverev, the top seed, lost in the round of 32 to Lorenzo Musetti 7-6(5), 6-2 and is not in this quarter-final.
""",
"f1-sao-paulo-gp-2026-norris-leads-fp1-interlagos.md": f"""---
title: "São Paulo GP FP1: Lando Norris leads Kimi Antonelli and Max Verstappen at Interlagos"
subtitle: "McLaren upgrades put Norris 0.082s clear of the new world champion on a weekend with no Sprint."
category: "Desk"
excerpt: "Lando Norris lapped Interlagos in 1:11.717 in Free Practice 1, ahead of Kimi Antonelli and Max Verstappen, with qualifying on Saturday and the race on Sunday."
image: "{IMG['f1']}"
readingTime: 5
pubDate: 2026-11-06
sport: f1
competition: f1-2026
relatedSlug: sao-paulo-gp-interlagos-2026
sources:
  - name: "Formula 1: FP1 Norris leads Antonelli and Verstappen"
    url: "https://www.formula1.com/en/latest/article/fp1-norris-leads-antonelli-and-verstappen-in-opening-sao-paulo-gp-practice-session.3GXL3rAROwHsLxnxn9hReY"
  - name: "ESPN F1 2026 drivers standings"
    url: "https://www.espn.com/f1/standings"
  - name: "Sky Sports F1: Norris tops Brazil first practice"
    url: "https://www.skysports.com/f1/news/13608857/sao-paulo-gp-lando-norris-tops-brazil-first-practice-in-upgraded-mclaren-from-kimi-antonelli-and-max-verstappen"
---

## FP1 order, no Sprint

Lando Norris was fastest in Free Practice 1 on Friday, 6 November, at Autodromo Jose Carlos Pace. Formula 1 listed Norris in 1:11.717, Kimi Antonelli +0.082s, Max Verstappen +0.236s, Lewis Hamilton +0.324s, George Russell +0.386s. Sky Sports noted McLaren brought a new front wing, rear wing, beam wing and floor furniture.

This São Paulo weekend has no Sprint. The timetable is FP1 and FP2 Friday, FP3 and qualifying Saturday, race Sunday. FP2 times are not published as finished.

## Standings after Mexico

ESPN's championship table after Mexico City: Antonelli 380 (champion), Verstappen 261, Hamilton 259, Russell 250, Leclerc 245, Norris 221, Piastri 144. Constructors: Mercedes 630, Ferrari 504, Red Bull 382, McLaren 365. RaceFans lists the Mexico result as Verstappen, Hamilton, Antonelli. Mercedes lead Ferrari by 126 points with four Grands Prix left. Rookies in FP1 included Fornaroli, Mini, Camara (Haas debut, P18), Beganovic, Slater and Herta. Hamilton is on his 400th Grand Prix weekend.
""",
"pga-tour-wwt-championship-2026-round1-chris-kirk-63.md": f"""---
title: "WWT Championship Round 1: Chris Kirk fires bogey-free 63 to lead by one at El Cardonal"
subtitle: "FedExCup Fall No. 110 hits every fairway; Dunlap and Blair sit one back on 64. Purse $6 million."
category: "Desk"
excerpt: "Chris Kirk shot a bogey-free 9-under 63 to lead the World Wide Technology Championship after Thursday's opening round in Los Cabos."
image: "{IMG['golf']}"
readingTime: 5
pubDate: 2026-11-06
sport: golf
competition: pga-tour-2026
relatedSlug: wwt-championship-diamante-cabo-2026
sources:
  - name: "PGA Tour: Kirk fires bogey-free 63, grabs early lead"
    url: "https://www.pgatour.com/article/news/daily-wrapup/2026/11/05/round-1-world-wide-technology-championship-recap-el-cardonal-scores-leaderboard-results"
  - name: "ESPN/AP: Chris Kirk leads after 63"
    url: "https://www.espn.com/golf/story/_/id/50394522/chris-kirk-leads-pga-tour-world-wide-technology-champ"
  - name: "AP News par scores, purse $6 million"
    url: "https://apnews.com/article/golf-3c730f124aa1ce9bd091b57cb2bc60fd"
---

## Kirk's 63 on the Tiger Woods design

Chris Kirk led the World Wide Technology Championship after round one on Thursday, 5 November, at El Cardonal at Diamante (par 72, 7,452 yards). Associated Press copy on PGA Tour and ESPN says he hit every fairway, missed one green, and shot a bogey-free 9-under 63. Nick Dunlap and Zac Blair opened 64. Five players sat T4 at 65: Matthieu Pavon, Harry Hall, Taylor Montgomery, Kensei Hirata and Ben James.

The purse is $6 million. Kirk is about 110th in FedExCup Fall with three events left to finish inside the top 100 and keep a full 2027 PGA Tour card. More than half of the 120-man field broke 70.

## Round 2 is not the desk

Friday's second round was in progress at the time of this desk. Live widgets that move Kirk or Ben James during R2 are not treated as a finished 36-hole board. This story publishes the completed Thursday round only.
""",
"ucl-matchday4-haaland-winner-city-edge-leipzig-3-2-2026.md": f"""---
title: "UCL MD4: Haaland winner as Manchester City edge RB Leipzig 3-2"
subtitle: "Captain taps in Anderson's 78th-minute cross after Leipzig twice equalise. City 3-1 in the league phase, seventh."
category: "Desk"
excerpt: "Erling Haaland scored the 78th-minute winner as Manchester City beat RB Leipzig 3-2 on Champions League matchday 4 at Red Bull Arena."
image: "{IMG['soc']}"
readingTime: 5
pubDate: 2026-11-06
sport: soccer
competition: champions-league-2026-27
relatedSlug: rb-leipzig-vs-man-city-ucl-md4-2026
sources:
  - name: "Manchester City official match report"
    url: "https://www.mancity.com/news/mens/rb-leipzig-manchester-city-uefa-champions-league-match-report-63929402"
  - name: "Sky Sports: Haaland late winner at Leipzig"
    url: "https://www.skysports.com/football/news/13607404/rb-leipzig-2-3-man-city-erling-haaland-haunts-bundesliga-side-again-with-late-winner-in-champions-league-thriller"
  - name: "The Guardian: Haaland settles thriller"
    url: "https://www.theguardian.com/football/2026/nov/04/rb-leipzig-manchester-city-champions-league-match-report"
---

## Five goals, two comebacks, one tap-in

Manchester City beat RB Leipzig 3-2 on Wednesday, 4 November, at Red Bull Arena. Castello Lukeba scored an own goal in the 37th minute. Ridle Baku equalised in the 49th. Enzo Fernandez headed City in front again in the 58th from Iliman Ndiaye's cross. Antonio Nusa made it 2-2 in the 61st from Christopher Nkunku's pass. Erling Haaland, captain on the night, finished Elliot Anderson's low cross in the 78th.

City's official report and Sky Sports both list Haaland's 13th goal in nine games against Leipzig. The win made City 3-1 in the league phase and seventh, inside the automatic round-of-16 places under Enzo Maresca.

## Premier League table, next fixture unpublished

BBC and NBC tables on 6 November, after matchweek 9: Arsenal 24 points (8-0-1), Manchester City 21, Brighton 19, Chelsea 16, Liverpool 15, Brentford 14. Everton vs Coventry on Friday 6 November at 20:00 GMT is upcoming and has no score on this desk. Harry Wilson's Fulham 2-1 Brentford from 2 November remains a prior result, not the current soccer lead.
""",
}

for name, body in stories.items():
    path = os.path.join(STORIES, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(body)
    print("wrote", path)

delete_files = [
    os.path.join(MATCHES, "atp-paris-masters-2026-zverev-vs-tsitsipas-qf.json"),
    os.path.join(STORIES, "atp-paris-masters-2026-zverev-subdues-tsitsipas-books-bercy-semi-final.md"),
    os.path.join(MATCHES, "nba-cavaliers-vs-pelicans-2026.json"),
    os.path.join(STORIES, "nba-cavaliers-top-pelicans-131-122-historic-9-0-start-2026.md"),
    os.path.join(MATCHES, "sporting-cp-vs-man-city-ucl-2026.json"),
    os.path.join(STORIES, "ucl-matchday4-sporting-demolish-city-4-1-gyokeres-hat-trick-2026.md"),
    os.path.join(MATCHES, "texans-at-jets-tnf-week9-2026.json"),
    os.path.join(STORIES, "nfl-week9-tnf-jets-down-texans-21-13-garrett-wilson-miracle-catch-2026.md"),
    os.path.join(STORIES, "f1-sao-paulo-gp-2026-piastri-edges-norris-sprint-pole-interlagos.md"),
    os.path.join(STORIES, "pga-tour-wwt-championship-2026-round2-echavarria-leads-smotherman-chases.md"),
]
for p in delete_files:
    if os.path.exists(p):
        os.remove(p)
        print("deleted", p)

# sports.ts
sports_path = os.path.join(ROOT, "frontend/src/data/sports.ts")
with open(sports_path, "r", encoding="utf-8") as f:
    st = f.read()
st = st.replace("export const SITE_TODAY = '2026-11-02';", "export const SITE_TODAY = '2026-11-06';")
replacements = {
    "NFL Week 8 MNF: Steelers overpower Giants 26-18 behind Calvin Austin's two touchdowns and ferocious pass rush.":
    "NFL Week 9 TNF: Jaguars thrash depleted Ravens 33-10 behind Lawrence, four Little field goals.",
    "Final in Pittsburgh: Steelers 26, Giants 18. Austin 2 TD (73-yd punt ret, 29-yd rec); Wilson 278 yds; Watt 2 sacks. Steelers improve to 6-2.":
    "Final in Baltimore: Jaguars 33, Ravens 10. Lawrence 242 yds, 50-yd TD; Little 4 FGs; Fagnano 2 INT. Jaguars 6-2, Ravens 4-5.",
    "NFL WEEK 8 MNF: PITTSBURGH STEELERS TOP GIANTS 26-18 TO LEAD AFC NORTH AT 6-2":
    "NFL WEEK 9 TNF: JACKSONVILLE JAGUARS THRASH RAVENS 33-10; JAGUARS 6-2, RAVENS 4-5",
    "NBA Thriller: Donovan Mitchell sinks baseline jumper with 0.3 seconds left as Cavaliers edge Bucks 114-113.":
    "NBA: Wembanyama posts 52 points, 24 rebounds, 8 blocks as Spurs edge Mavericks 112-111.",
    "Final in Milwaukee: Cavaliers 114, Bucks 113. Mitchell 30 pts (game-winner 0.3s) answers Lillard's 41 pts (10 threes). Cleveland moves to 7-0.":
    "Final in San Antonio: Spurs 112, Mavericks 111. Wembanyama 52-24-8; winning FT 24.2s. Spurs 6-2. Cavs are 4-4.",
    "NBA THRILLER: DONOVAN MITCHELL HITS GAME-WINNER AS CAVALIERS STAY UNBEATEN (7-0)":
    "NBA: WEMBANYAMA 52-24-8 AS SPURS EDGE MAVERICKS 112-111 FOR SIXTH STRAIGHT",
    "Premier League MW9: Harry Wilson scores sensational stoppage-time brace as Fulham stun Brentford 2-1.":
    "UCL MD4: Haaland winner as Manchester City edge RB Leipzig 3-2. Arsenal lead Premier League on 24 points.",
    "Final at Craven Cottage: Fulham 2-1 Brentford (Wilson 90+2', 90+7'; Janelt 24'). Fulham climb to 8 points after dramatic derby comeback.":
    "Final in Leipzig: RB Leipzig 2-3 Manchester City (Lukeba OG 37, Baku 49, Fernandez 58, Nusa 61, Haaland 78). City 3-1, 7th in UCL.",
    "PREMIER LEAGUE MW9: HARRY WILSON 97TH-MINUTE HEADER CAPS MIRACLE FULHAM COMEBACK":
    "UCL MD4: HAALAND 78TH-MINUTE WINNER LIFTS CITY PAST LEIPZIG 3-2; ARSENAL LEAD PL ON 24",
    "Rolex Paris Masters: Stefanos Tsitsipas rallies past Roberto Carballes Baena 4-6, 6-3, 6-3 in Bercy opener.":
    "Rolex Paris Masters QF: Ben Shelton beats Tommy Paul 6-4, 4-6, 6-3 to reach first Bercy semi-final.",
    "Paris Masters R64: Tsitsipas def. Carballes Baena 4-6, 6-3, 6-3 in 2h07m. Tsitsipas fires 37 winners and 11 aces to keep ATP Finals bid alive.":
    "Paris Masters QF: Shelton def. Paul 6-4, 4-6, 6-3 in 1h46m, 19 aces. Tiafoe qualifies for Turin; Paul is out.",
    "ROLEX PARIS MASTERS: STEFANOS TSITSIPAS BATTLES BACK TO WIN THREE-SET BERCY OPENER":
    "ROLEX PARIS MASTERS: BEN SHELTON BEATS TOMMY PAUL TO REACH FIRST BERCY SEMI-FINAL",
    "São Paulo GP Preview: Fresh off Antonelli's coronation, F1 heads to Interlagos for high-stakes Constructors' showdown.":
    "São Paulo GP FP1: Lando Norris leads Kimi Antonelli and Max Verstappen at Interlagos.",
    "Next up: Grande Prêmio de São Paulo (6-8 Nov). Mercedes (607 pts) lead Ferrari (474 pts) by 133 points heading into Interlagos Sprint weekend.":
    "FP1: Norris 1:11.717, Antonelli +0.082s, Verstappen +0.236s. No Sprint. Mercedes 630, Ferrari 504 after Mexico.",
    "F1 INTERLAGOS PREVIEW: MERCEDES AND FERRARI CLASH IN SAO PAULO SPRINT SHOWDOWN":
    "F1 INTERLAGOS FP1: NORRIS LEADS ANTONELLI; NO SPRINT; MERCEDES 630, FERRARI 504",
    "WWT Championship Preview: Following Pereda's historic triumph, PGA Tour arrives in Cabo with FedExCup cards on the line.":
    "WWT Championship Round 1: Chris Kirk fires bogey-free 63 to lead by one at El Cardonal.",
    "Next up at El Cardonal at Diamante (5-8 Nov). Raul Pereda vaults into world top 50; Smotherman and Rai chase redemption in Los Cabos.":
    "R1 complete: Kirk 63 leads Dunlap and Blair 64. Purse $6 million. Round 2 in progress, unpublished as final.",
    "PGA TOUR CABO PREVIEW: PLAYERS CHASE TOP 125 STATUS AT TIGER WOODS-DESIGNED DIAMANTE":
    "PGA TOUR CABO R1: CHRIS KIRK 63 LEADS WWT CHAMPIONSHIP; FEDEXCUP FALL CARDS ON THE LINE",
}
for old, new in replacements.items():
    if old not in st:
        print("WARN sports.ts missing:", old[:80])
    st = st.replace(old, new)
with open(sports_path, "w", encoding="utf-8") as f:
    f.write(st)
print("updated sports.ts")

# desk.json
desk_path = os.path.join(ROOT, "frontend/src/data/desk.json")
with open(desk_path, "r", encoding="utf-8") as f:
    desk = json.load(f)
desk["asOf"] = "2026-11-06"
desk["premierLeagueTable"] = [
    {"pos": 1, "team": "Arsenal", "p": 9, "w": 8, "d": 0, "l": 1, "gf": 14, "ga": 5, "gd": 9, "pts": 24},
    {"pos": 2, "team": "Manchester City", "p": 9, "w": 7, "d": 0, "l": 2, "gf": 20, "ga": 10, "gd": 10, "pts": 21},
    {"pos": 3, "team": "Brighton", "p": 9, "w": 6, "d": 1, "l": 2, "gf": 24, "ga": 7, "gd": 17, "pts": 19},
    {"pos": 4, "team": "Chelsea", "p": 9, "w": 5, "d": 1, "l": 3, "gf": 19, "ga": 15, "gd": 4, "pts": 16},
    {"pos": 5, "team": "Liverpool", "p": 9, "w": 4, "d": 3, "l": 2, "gf": 11, "ga": 9, "gd": 2, "pts": 15},
    {"pos": 6, "team": "Brentford", "p": 9, "w": 3, "d": 5, "l": 1, "gf": 16, "ga": 9, "gd": 7, "pts": 14},
    {"pos": 7, "team": "Everton", "p": 9, "w": 3, "d": 4, "l": 2, "gf": 9, "ga": 9, "gd": 0, "pts": 13},
    {"pos": 8, "team": "Bournemouth", "p": 9, "w": 3, "d": 3, "l": 3, "gf": 14, "ga": 13, "gd": 1, "pts": 12},
    {"pos": 9, "team": "Tottenham Hotspur", "p": 9, "w": 3, "d": 3, "l": 3, "gf": 10, "ga": 10, "gd": 0, "pts": 12},
    {"pos": 10, "team": "Aston Villa", "p": 9, "w": 3, "d": 3, "l": 3, "gf": 10, "ga": 13, "gd": -3, "pts": 12},
    {"pos": 11, "team": "Hull City", "p": 9, "w": 2, "d": 5, "l": 2, "gf": 11, "ga": 10, "gd": 1, "pts": 11},
    {"pos": 12, "team": "Leeds United", "p": 9, "w": 2, "d": 5, "l": 2, "gf": 9, "ga": 8, "gd": 1, "pts": 11},
    {"pos": 13, "team": "Newcastle United", "p": 9, "w": 3, "d": 2, "l": 4, "gf": 12, "ga": 15, "gd": -3, "pts": 11},
    {"pos": 14, "team": "Ipswich", "p": 9, "w": 3, "d": 2, "l": 4, "gf": 14, "ga": 18, "gd": -4, "pts": 11},
    {"pos": 15, "team": "Fulham", "p": 9, "w": 2, "d": 3, "l": 4, "gf": 9, "ga": 11, "gd": -2, "pts": 9},
    {"pos": 16, "team": "Coventry", "p": 9, "w": 3, "d": 0, "l": 6, "gf": 9, "ga": 16, "gd": -7, "pts": 9},
    {"pos": 17, "team": "Manchester United", "p": 9, "w": 1, "d": 4, "l": 4, "gf": 10, "ga": 15, "gd": -5, "pts": 7},
    {"pos": 18, "team": "Crystal Palace", "p": 9, "w": 2, "d": 1, "l": 6, "gf": 9, "ga": 21, "gd": -12, "pts": 7},
    {"pos": 19, "team": "Nottingham Forest", "p": 9, "w": 1, "d": 3, "l": 5, "gf": 6, "ga": 12, "gd": -6, "pts": 6},
    {"pos": 20, "team": "Sunderland", "p": 9, "w": 1, "d": 2, "l": 6, "gf": 7, "ga": 17, "gd": -10, "pts": 5},
]
desk["f1Drivers"] = [
    {"pos": 1, "name": "Kimi Antonelli", "team": "Mercedes", "pts": 380},
    {"pos": 2, "name": "Max Verstappen", "team": "Red Bull", "pts": 261},
    {"pos": 3, "name": "Lewis Hamilton", "team": "Ferrari", "pts": 259},
    {"pos": 4, "name": "George Russell", "team": "Mercedes", "pts": 250},
    {"pos": 5, "name": "Charles Leclerc", "team": "Ferrari", "pts": 245},
    {"pos": 6, "name": "Lando Norris", "team": "McLaren", "pts": 221},
    {"pos": 7, "name": "Oscar Piastri", "team": "McLaren", "pts": 144},
    {"pos": 8, "name": "Isack Hadjar", "team": "Red Bull", "pts": 107},
    {"pos": 9, "name": "Liam Lawson", "team": "Racing Bulls", "pts": 83},
    {"pos": 10, "name": "Pierre Gasly", "team": "Alpine", "pts": 42},
]
desk["f1Constructors"] = [
    {"pos": 1, "name": "Mercedes", "pts": 630},
    {"pos": 2, "name": "Ferrari", "pts": 504},
    {"pos": 3, "name": "Red Bull", "pts": 382},
    {"pos": 4, "name": "McLaren", "pts": 365},
    {"pos": 5, "name": "Racing Bulls", "pts": 108},
    {"pos": 6, "name": "Alpine", "pts": 69},
    {"pos": 7, "name": "Haas", "pts": 31},
    {"pos": 8, "name": "Audi", "pts": 27},
    {"pos": 9, "name": "Williams", "pts": 12},
    {"pos": 10, "name": "Aston Martin", "pts": 7},
    {"pos": 11, "name": "Cadillac", "pts": 0},
]
desk["nflWeek1"].append({
    "date": "2026-11-05",
    "time": "8:15 p.m. ET",
    "home": "Baltimore Ravens",
    "away": "Jacksonville Jaguars",
    "note": "FINAL: Jaguars 33, Ravens 10. ESPN/Prime TNF. Lawrence 16/26, 242 yds, 50-yd TD. Little 4 FGs. Fagnano 10/18, 60 yds, 2 INT. Jaguars 6-2, Ravens 4-5."
})
desk["usOpenQF"].append({
    "draw": "Paris QF",
    "p1": "Ben Shelton",
    "p2": "Tommy Paul",
    "status": "Shelton 6-4, 4-6, 6-3"
})
with open(desk_path, "w", encoding="utf-8") as f:
    json.dump(desk, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("updated desk.json, PL rows", len(desk["premierLeagueTable"]))

# AGENTS.md clock
agents = os.path.join(ROOT, "AGENTS.md")
with open(agents, "r", encoding="utf-8") as f:
    ag = f.read()
old_clock = "*   **Site clock:** editorial today is `2026-11-02`"
idx = ag.find(old_clock)
if idx == -1:
    print("WARN AGENTS clock line not found")
else:
    end = ag.find("\n\n---", idx)
    new_clock = (
        "*   **Site clock:** editorial today is `2026-11-06` in `frontend/src/data/sports.ts` (`SITE_TODAY`). "
        "Football: Jacksonville Jaguars defeat Baltimore Ravens 33-10 on Thursday Night Football (5 Nov) as Trevor Lawrence throws for 242 yards and a 50-yard touchdown; Cam Little four field goals; Joe Fagnano two interceptions in his first start. Jaguars 6-2, Ravens 4-5. Steelers remain 6-2 in the AFC North. "
        "Basketball: Victor Wembanyama posts 52 points, 24 rebounds and 8 blocks as San Antonio Spurs edge Dallas Mavericks 112-111 on 4 Nov; Spurs 6-2. Cleveland Cavaliers are 4-4. Philadelphia 76ers lead the East at 8-1. "
        "Soccer: Erling Haaland scores the 78th-minute winner as Manchester City beat RB Leipzig 3-2 on UCL matchday 4 (4 Nov). Premier League after MW9: Arsenal 24, City 21, Brighton 19. "
        "Tennis: Ben Shelton beats Tommy Paul 6-4, 4-6, 6-3 in the Rolex Paris Masters quarter-finals on 6 Nov; Tiafoe qualifies for Turin. "
        "Formula 1: Lando Norris leads São Paulo GP FP1 in 1:11.717 from Antonelli and Verstappen. No Sprint this weekend. After Mexico (Verstappen-Hamilton-Antonelli), Antonelli is champion on 380; Mercedes 630, Ferrari 504. "
        "Golf: Chris Kirk shoots a bogey-free 63 to lead WWT Championship round 1 at El Cardonal; Dunlap and Blair 64. Purse $6 million. Round 2 unpublished as final."
    )
    ag = ag[:idx] + new_clock + ag[end:]
    with open(agents, "w", encoding="utf-8") as f:
        f.write(ag)
    print("updated AGENTS.md")

# Homepage / LivePage featured fallback
for rel in ["frontend/src/views/HomePage.astro", "frontend/src/views/LivePage.astro"]:
    path = os.path.join(ROOT, rel)
    with open(path, "r", encoding="utf-8") as f:
        txt = f.read()
    needle = "matches.find((m) => m.slug === 'bills-at-rams-mnf-week5-2026') ||"
    insert = "matches.find((m) => m.slug === 'jaguars-at-ravens-tnf-week9-2026') ||\n  " + needle
    if "jaguars-at-ravens-tnf-week9-2026" not in txt:
        if needle not in txt:
            print("WARN featured needle missing in", rel)
        else:
            txt = txt.replace(needle, insert, 1)
            with open(path, "w", encoding="utf-8") as f:
                f.write(txt)
            print("featured slug added in", rel)

# dash lint (skip YAML fences and URLs)
def lint_text(s):
    s = re.sub(r"https?://\S+", "", s)
    s = s.replace("---", "")
    if "—" in s or "--" in s:
        raise SystemExit("em-dash or double-hyphen found: " + s[max(0, s.find("--")-40):s.find("--")+40])

for m in matches:
    lint_text(json.dumps(m, ensure_ascii=False))
for body in stories.values():
    lint_text(body)
print("dash lint ok")

print("apply_nov06_desk.py done")
