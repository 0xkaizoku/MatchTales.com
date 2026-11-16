"""Create and update match JSONs for 2026-11-16."""
import os
import json

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
MATCHES = os.path.join(ROOT, "frontend", "src", "content", "matches")

# 1. Update spain-vs-england-nations-league-metropolitano-2026.json
spain_england_path = os.path.join(MATCHES, "spain-vs-england-nations-league-metropolitano-2026.json")
spain_england_data = {
  "slug": "spain-vs-england-nations-league-metropolitano-2026",
  "sport": "soccer",
  "competition": "uefa-nations-league",
  "format": "team-match",
  "home": "Spain",
  "away": "England",
  "homeCode": "ESP",
  "awayCode": "ENG",
  "date": "2026-11-15",
  "time": "19:45 GMT",
  "status": "FINISHED",
  "roundLabel": "Matchday 6 · Final Result",
  "group": "A3",
  "venue": "Riyadh Air Metropolitano, Madrid",
  "city": "Madrid",
  "homeScore": "2",
  "awayScore": "3",
  "whyCareScore": 9.8,
  "headline": "Nations League: England shock Spain 3-2 in Madrid thriller to claim Group A3 top seed",
  "teaser": "Captain Harry Kane, Ezri Konsa, and Ben White strike as England build a 3-0 lead, surviving a spirited Spanish fightback and an Elliot Anderson red card to snap La Roja's 43-match unbeaten run.",
  "story": "England produced one of their most remarkable away performances in recent memory on Sunday, 15 November, defeating European champions Spain 3-2 at the Riyadh Air Metropolitano in Madrid to clinch first place in UEFA Nations League Group A3.\n\nThomas Tuchel's side stunned the 63,788 crowd by opening the scoring on the stroke of halftime, when captain Harry Kane converted a 45th-minute penalty for his 73rd international goal. The Three Lions doubled their advantage eight minutes after the restart as Ezri Konsa headed home from a corner, before Ben White swept home a third on 58 minutes following a swift counter-attack.\n\nSpain mounted a relentless fightback, with Mikel Oyarzabal converting a 65th-minute spot-kick and Nico Williams finishing neatly on 75 minutes. England were reduced to ten men when midfielder Elliot Anderson received a straight red card for a rash tackle in the 84th minute, but Jordan Pickford and a resolute backline withstood intense pressure through seven minutes of stoppage time to snap Spain's 43-match unbeaten competitive streak dating back to March 2023.",
  "whyCareReason": "England snap Spain's 43-match competitive unbeaten streak in Madrid, leapfrogging the European champions to take the seeded quarter-final berth in Nations League Group A3.",
  "stakes": "England claim top seed in Group A3 for the two-legged quarter-finals in March 2027, while Spain advance as unseeded runners-up.",
  "rivalryAngle": "Sweet redemption for England after falling 2-1 to Spain in the Euro 2024 final in Berlin, earning their first victory on Spanish soil in eight years.",
  "funFacts": [
    "Harry Kane scored his 73rd international goal on his 126th cap, converting a penalty on 45 minutes.",
    "Spain's loss was their first defeat in a competitive fixture in 43 matches dating back to March 2023.",
    "England built a 3-0 lead inside 58 minutes through Kane, Konsa, and White before holding on with ten men."
  ],
  "keyPlayers": [
    {
      "name": "Harry Kane",
      "team": "England",
      "hook": "Coolly converted the crucial opening penalty and led England's frontline with tireless pressing."
    },
    {
      "name": "Ezri Konsa",
      "team": "England",
      "hook": "Towered at the back post to head in England's second goal and anchored the defense with key blocks."
    },
    {
      "name": "Nico Williams",
      "team": "Spain",
      "hook": "Ignited Spain's second-half surge with an exquisite 75th-minute finish past Jordan Pickford."
    }
  ],
  "tags": [
    "soccer",
    "uefa-nations-league",
    "spain",
    "england",
    "metropolitano",
    "harry-kane",
    "ezri-konsa",
    "nico-williams",
    "tuchel"
  ],
  "sources": [
    {
      "name": "UEFA Official: Spain 2-3 England Match Report",
      "url": "https://www.uefa.com/uefanationsleague/match/spain-vs-england-2026/"
    },
    {
      "name": "The Guardian: England stun Spain in five-goal Nations League thriller",
      "url": "https://www.theguardian.com/football/live/2026/nov/15/spain-v-england-nations-league"
    },
    {
      "name": "Reuters: Kane penalty and White strike propel England past Spain 3-2",
      "url": "https://www.reuters.com/sports/soccer/spain-england-nations-league-decider-madrid-2026-11-15/"
    }
  ]
}
open(spain_england_path, "w", encoding="utf-8").write(json.dumps(spain_england_data, indent=2, ensure_ascii=False) + "\n")
print("Updated spain-vs-england match JSON.")

# 2. Update patriots-vs-lions-munich-week10-2026.json
pats_lions_path = os.path.join(MATCHES, "patriots-vs-lions-munich-week10-2026.json")
pats_lions_data = {
  "slug": "patriots-vs-lions-munich-week10-2026",
  "sport": "football",
  "competition": "nfl",
  "format": "team-match",
  "home": "New England Patriots",
  "away": "Detroit Lions",
  "homeCode": None,
  "awayCode": None,
  "date": "2026-11-15",
  "time": "9:30 a.m. ET",
  "status": "FINISHED",
  "roundLabel": "Week 10 · Munich Final Result",
  "group": "NFL",
  "venue": "Allianz Arena, Munich",
  "city": "Munich",
  "homeScore": "10",
  "awayScore": "35",
  "whyCareScore": 9.1,
  "headline": "NFL Munich Final: Lions dominate Patriots 35-10 behind Gibbs' 252 yards; Maye hurt",
  "teaser": "Jahmyr Gibbs explodes for 252 scrimmage yards with two touchdowns and Amon-Ra St. Brown catches two scores in front of 70,225 at Allianz Arena, while Patriots quarterback Drake Maye exits early with an ankle injury.",
  "story": "The Detroit Lions delivered a commanding performance on European soil on Sunday, 15 November, dismantling the New England Patriots 35-10 in the NFL Week 10 international fixture at Allianz Arena in Munich.\n\nDan Campbell's high-powered attack overwhelmed New England from the opening snap. Jared Goff orchestrated a masterclass, completing 22 of 28 passes for 303 yards and three touchdowns. Wideout Amon-Ra St. Brown, whose mother is German, ignited the raucous crowd of 70,225 with a 56-yard touchdown catch on Detroit's first possession and added a second score in the third quarter.\n\nRunning back Jahmyr Gibbs put on a breathtaking show, totaling 252 scrimmage yards (153 rushing, 99 receiving) and scoring twice, including a dazzling 44-yard breakaway touchdown in the fourth quarter. The Patriots' afternoon unraveled early when rookie starter Drake Maye suffered an ankle injury during an Aidan Hutchinson sack on the opening drive and was ruled out, leaving backup Tommy DeVito under constant siege. The victory lifts Detroit to 7-2, while New England drops to 5-5.",
  "whyCareReason": "Detroit solidifies NFC contender status with a 35-10 European showcase blowout as Jahmyr Gibbs posts a franchise-record international yardage display.",
  "stakes": "Detroit (7-2) tightens its grip on the NFC North race while New England (5-5) deals with quarterback uncertainty following Drake Maye's ankle injury.",
  "rivalryAngle": "Electric Munich atmosphere at Allianz Arena as 70,225 German fans witness Dan Campbell's Lions dominate in the final international regular-season clash of 2026.",
  "funFacts": [
    "Jahmyr Gibbs generated 252 total scrimmage yards (153 rushing, 99 receiving) with two touchdowns.",
    "Amon-Ra St. Brown caught two touchdowns in Munich in front of his German-born family.",
    "Aidan Hutchinson logged his ninth sack of the season, forcing Drake Maye out of the contest."
  ],
  "keyPlayers": [
    {
      "name": "Jahmyr Gibbs",
      "team": "Detroit Lions",
      "hook": "Torched New England's defense for 252 scrimmage yards and two explosive touchdowns."
    },
    {
      "name": "Amon-Ra St. Brown",
      "team": "Detroit Lions",
      "hook": "Delighted the Munich crowd with two touchdown receptions, including a 56-yard bomb."
    },
    {
      "name": "Jared Goff",
      "team": "Detroit Lions",
      "hook": "Completed 22 of 28 passes for 303 yards and three scores with zero turnovers."
    }
  ],
  "tags": [
    "nfl",
    "munich",
    "allianz-arena",
    "detroit-lions",
    "new-england-patriots",
    "jahmyr-gibbs",
    "amon-ra-st-brown",
    "jared-goff",
    "drake-maye"
  ],
  "sources": [
    {
      "name": "NFL.com: Lions rout Patriots 35-10 at Allianz Arena in Munich",
      "url": "https://www.nfl.com/games/patriots-at-lions-2026-reg-10"
    },
    {
      "name": "Detroit Lions Official: Gibbs and St. Brown shine in 35-10 Munich victory",
      "url": "https://www.detroitlions.com/news/game-recap-patriots-lions-munich-2026"
    },
    {
      "name": "Associated Press: Gibbs totals 252 yards as Lions roll past Patriots in Germany",
      "url": "https://apnews.com/article/patriots-lions-munich-game-2026"
    }
  ]
}
open(pats_lions_path, "w", encoding="utf-8").write(json.dumps(pats_lions_data, indent=2, ensure_ascii=False) + "\n")
print("Updated patriots-vs-lions match JSON.")

# 3. Create chargers-at-ravens-mnf-week10-2026.json
chargers_ravens_path = os.path.join(MATCHES, "chargers-at-ravens-mnf-week10-2026.json")
chargers_ravens_data = {
  "slug": "chargers-at-ravens-mnf-week10-2026",
  "sport": "football",
  "competition": "nfl",
  "format": "team-match",
  "home": "Baltimore Ravens",
  "away": "Los Angeles Chargers",
  "homeCode": None,
  "awayCode": None,
  "date": "2026-11-16",
  "time": "8:15 PM ET",
  "status": "UPCOMING",
  "roundLabel": "Week 10 · Monday Night Football",
  "group": "NFL",
  "venue": "M&T Bank Stadium, Baltimore",
  "city": "Baltimore",
  "homeScore": None,
  "awayScore": None,
  "whyCareScore": 9.4,
  "headline": "Monday Night Football: Chargers visit Ravens at M&T Bank Stadium in Harbaugh Bowl",
  "teaser": "Brothers Jim and John Harbaugh clash under the prime-time lights in Baltimore as Justin Herbert and the physical Chargers test Lamar Jackson and the explosive Ravens.",
  "story": "Week 10 of the NFL season wraps up with a marquee Monday Night Football spectacle on 16 November, as Jim Harbaugh leads his Los Angeles Chargers into M&T Bank Stadium to take on brother John Harbaugh and the Baltimore Ravens.\n\nThe iconic coaching rivalry adds extra intrigue to a matchup with massive AFC playoff ramifications. The Chargers enter at 6-3, boasting one of the league's stingiest scoring defenses behind pass rusher Joey Bosa and safety Derwin James, while Justin Herbert continues to pilot an efficient run-first attack anchored by J.K. Dobbins.\n\nStanding in their path is two-time MVP Lamar Jackson and a Baltimore offense averaging over 29 points per contest. Jackson and running back Derrick Henry present the ultimate test for Los Angeles' front seven in what promises to be a physical, 60-minute battle for postseason seeding.",
  "whyCareReason": "The high-profile Harbaugh Bowl pits brother against brother with major AFC wild card and division race implications under the Monday Night Football spotlight.",
  "stakes": "A victory secures a vital head-to-head tiebreaker in the ultra-competitive AFC playoff hierarchy.",
  "rivalryAngle": "Jim Harbaugh and John Harbaugh face each other for the first time since Super Bowl XLVII, reigniting the NFL's premier sibling coaching rivalry.",
  "funFacts": [
    "Jim and John Harbaugh previously coached against each other in Super Bowl XLVII in February 2013.",
    "Lamar Jackson is 23-6 in prime-time regular-season games throughout his NFL career.",
    "The Chargers defense enters allowing just 14.8 points per game, the third lowest in the NFL."
  ],
  "keyPlayers": [
    {
      "name": "Lamar Jackson",
      "team": "Baltimore Ravens",
      "hook": "Two-time MVP leading Baltimore's balanced passing and rushing offensive juggernaut."
    },
    {
      "name": "Justin Herbert",
      "team": "Los Angeles Chargers",
      "hook": "Elite pocket passer seeking a statement prime-time road win in Jim Harbaugh's system."
    },
    {
      "name": "Derrick Henry",
      "team": "Baltimore Ravens",
      "hook": "Bruising tailback looking to puncture the Chargers' disciplined defensive front."
    }
  ],
  "tags": [
    "nfl",
    "monday-night-football",
    "chargers",
    "ravens",
    "harbaugh-bowl",
    "lamar-jackson",
    "justin-herbert",
    "derrick-henry"
  ],
  "sources": [
    {
      "name": "NFL.com: Chargers at Ravens Game Center",
      "url": "https://www.nfl.com/games/chargers-at-ravens-2026-reg-10"
    },
    {
      "name": "ESPN: Monday Night Football Harbaugh Bowl Preview",
      "url": "https://www.espn.com/nfl/preview/_/gameId/401671780"
    },
    {
      "name": "BaltimoreRavens.com: Ravens host Chargers on MNF",
      "url": "https://www.baltimoreravens.com/news/chargers-vs-ravens-week-10-preview"
    }
  ]
}
open(chargers_ravens_path, "w", encoding="utf-8").write(json.dumps(chargers_ravens_data, indent=2, ensure_ascii=False) + "\n")
print("Created chargers-at-ravens match JSON.")

# 4. Update atp-nitto-finals-2026-turin-draw.json
turin_path = os.path.join(MATCHES, "atp-nitto-finals-2026-turin-draw.json")
turin_data = {
  "slug": "atp-nitto-finals-2026-turin-draw",
  "headline": "Nitto ATP Finals: Shelton edges Fils in three; Alcaraz and Tiafoe launch Lendl Group Monday",
  "whyCareScore": 9.4,
  "whyCareReason": "Ben Shelton edges Arthur Fils 6-2, 3-6, 6-3 after Alexander Zverev swept Rafael Jodar in McEnroe Group openers; Carlos Alcaraz opens his tournament against Frances Tiafoe on Monday.",
  "teaser": "Ben Shelton survives a fierce Arthur Fils comeback to win his Turin debut 6-2, 3-6, 6-3 at Inalpi Arena. Carlos Alcaraz begins his campaign against Frances Tiafoe in Monday's afternoon session.",
  "story": "The 2026 Nitto ATP Finals delivered high-octane drama on its opening Sunday, 15 November, at Inalpi Arena in Turin as the John McEnroe Group kicked off round-robin competition.\n\nWorld No. 1 Alexander Zverev began the afternoon with a measured 6-4, 6-4 victory over Spanish teenager Rafael Jodar, dropping only six points on his first serve in an 87-minute masterclass. The evening session brought fireworks as American third seed Ben Shelton survived a thrilling challenge from France's Arthur Fils, claiming a 6-2, 3-6, 6-3 victory behind 16 aces in two hours and eight minutes.\n\nAttention now turns to the Ivan Lendl Group on Monday, 16 November: World No. 2 Carlos Alcaraz clashes with Frances Tiafoe not before 2:00 p.m. CET, followed by Daniil Medvedev taking on Italian hopeful Flavio Cobolli in the evening session.",
  "stakes": "Zverev and Shelton take early 1-0 records in McEnroe Group; Alcaraz and Medvedev look to establish early dominance in Lendl Group on Monday.",
  "rivalryAngle": "Alcaraz and Tiafoe renew their electrifying rivalry on indoor hard courts following classic Grand Slam battles in New York and London.",
  "funFacts": [
    "Ben Shelton fired 16 aces and saved four break points in his three-set victory over Arthur Fils.",
    "Alexander Zverev has won 15 career matches at the Nitto ATP Finals across his decorated career.",
    "Carlos Alcaraz is aiming for his first career Nitto ATP Finals trophy in Turin."
  ],
  "keyPlayers": [
    {
      "name": "Ben Shelton",
      "team": "United States",
      "hook": "Fired 16 aces to defeat Arthur Fils 6-2, 3-6, 6-3 in Sunday night's Turin thriller."
    },
    {
      "name": "Alexander Zverev",
      "team": "Germany",
      "hook": "Clinched opening win 6-4, 6-4 against Rafael Jodar with near-flawless serving."
    },
    {
      "name": "Carlos Alcaraz",
      "team": "Spain",
      "hook": "Launches his Turin campaign against Frances Tiafoe on Monday afternoon."
    }
  ],
  "headToHead": "Tournament dates 15-22 November 2026, Inalpi Arena, Turin. McEnroe Group Day 1 complete; Lendl Group begins Monday.",
  "tags": [
    "tennis",
    "atp",
    "nitto-atp-finals",
    "turin",
    "shelton",
    "zverev",
    "alcaraz",
    "tiafoe",
    "fils"
  ],
  "home": "Carlos Alcaraz",
  "away": "Frances Tiafoe",
  "homeCode": "ESP",
  "awayCode": "USA",
  "homeFlag": "es",
  "awayFlag": "us",
  "group": "Nitto ATP Finals Lendl",
  "matchday": 1,
  "date": "2026-11-16",
  "time": "14:00 CET",
  "venue": "Inalpi Arena",
  "city": "Turin",
  "status": "UPCOMING",
  "homeScore": None,
  "awayScore": None,
  "marquee": True,
  "liveMinute": None,
  "image": "https://images.pexels.com/photos/1618210/pexels-photo-1618210.jpeg?auto=compress&cs=tinysrgb&w=1600&h=900&fit=crop",
  "decidedBy": None,
  "homePen": None,
  "awayPen": None,
  "sport": "tennis",
  "competition": "atp-finals-2026",
  "format": "leaderboard",
  "season": "2026",
  "roundLabel": "Turin Lendl Group Opener",
  "resultSummary": "SUN McEnroe: Zverev d Jodar 6-4, 6-4; Shelton d Fils 6-2, 3-6, 6-3. MON Lendl: Alcaraz vs Tiafoe (14:00 CET), Medvedev vs Cobolli (20:30 CET).",
  "leaderboard": [
    {
      "pos": "McEnroe 1-0",
      "name": "Alexander Zverev (1)",
      "score": "1-0 (2-0 sets)",
      "note": "Def. Jodar 6-4, 6-4"
    },
    {
      "pos": "McEnroe 1-0",
      "name": "Ben Shelton (3)",
      "score": "1-0 (2-1 sets)",
      "note": "Def. Fils 6-2, 3-6, 6-3"
    },
    {
      "pos": "McEnroe 0-1",
      "name": "Arthur Fils (6)",
      "score": "0-1 (1-2 sets)",
      "note": "Lost to Shelton in 3"
    },
    {
      "pos": "McEnroe 0-1",
      "name": "Rafael Jodar (8)",
      "score": "0-1 (0-2 sets)",
      "note": "Lost to Zverev 6-4, 6-4"
    },
    {
      "pos": "Lendl",
      "name": "Carlos Alcaraz (2)",
      "score": "0-0",
      "note": "Mon 14:00 vs Tiafoe"
    },
    {
      "pos": "Lendl",
      "name": "Daniil Medvedev (4)",
      "score": "0-0",
      "note": "Mon 20:30 vs Cobolli"
    }
  ],
  "tennisSets": [
    {
      "p1": "6",
      "p2": "2"
    },
    {
      "p1": "3",
      "p2": "6"
    },
    {
      "p1": "6",
      "p2": "3"
    }
  ],
  "sources": [
    {
      "name": "Nitto ATP Finals Official: Shelton overcomes Fils; Zverev downs Jodar",
      "url": "https://www.nittoatpfinals.com/en/news/shelton-fils-turin-2026-sunday"
    },
    {
      "name": "ATP Tour Scores: Turin 2026 McEnroe Group Results",
      "url": "https://www.atptour.com/en/scores/current/nitto-atp-finals/0605/results"
    },
    {
      "name": "FlashScore: Shelton vs Fils Turin Match Stats",
      "url": "https://www.flashscore.com/match/turin-2026-shelton-fils/"
    }
  ]
}
open(turin_path, "w", encoding="utf-8").write(json.dumps(turin_data, indent=2, ensure_ascii=False) + "\n")
print("Updated turin match JSON.")

# 5. Create nba-spurs-vs-jazz-nov15-2026.json
nba_spurs_path = os.path.join(MATCHES, "nba-spurs-vs-jazz-nov15-2026.json")
nba_spurs_data = {
  "slug": "nba-spurs-vs-jazz-nov15-2026",
  "sport": "basketball",
  "competition": "nba",
  "format": "team-match",
  "home": "Utah Jazz",
  "away": "San Antonio Spurs",
  "homeCode": None,
  "awayCode": None,
  "date": "2026-11-15",
  "time": "9:00 PM ET",
  "status": "FINISHED",
  "roundLabel": "Regular Season",
  "group": "NBA",
  "venue": "Delta Center, Salt Lake City",
  "city": "Salt Lake City",
  "homeScore": "102",
  "awayScore": "110",
  "whyCareScore": 8.7,
  "headline": "NBA: Spurs claim 12th consecutive victory as Wembanyama and Harper power 110-102 win in Utah",
  "teaser": "Victor Wembanyama fills the stat sheet with 26 points, 11 rebounds, and 5 blocks while rookie Dylan Harper pours in 31 points to keep San Antonio's historic winning streak rolling.",
  "story": "The San Antonio Spurs extended the NBA's longest winning streak of the season to 12 games on Sunday night, 15 November, grinding out a 110-102 road triumph over the Utah Jazz at Delta Center.\n\nVictor Wembanyama proved unguardable at both ends of the floor, tallying 26 points, 11 rebounds, 6 assists, and 5 blocked shots in 34 minutes of action. The French phenom altered countless Utah drives while stepping out to sink three shots from beyond the arc.\n\nDynamic rookie guard Dylan Harper provided the scoring punch down the stretch, racking up a career-high 31 points, including 18 in a scintillating fourth-quarter barrage that turned a one-possession contest into a comfortable Spurs victory. Mo Bamba led Utah with 26 points and 12 boards, but the Jazz could not contain San Antonio's closing execution as the Spurs improved to a league-leading 12-1.",
  "whyCareReason": "San Antonio pushes their winning streak to 12 straight games behind Wembanyama's two-way mastery and Harper's fourth-quarter explosion.",
  "stakes": "The Spurs (12-1) retain the NBA's best record and sole possession of first place in the Western Conference.",
  "rivalryAngle": "San Antonio silences a hostile Delta Center crowd to sweep the early-season road swing through the Mountain West.",
  "funFacts": [
    "The Spurs have won 12 consecutive games, their longest winning streak since the 2015-16 season.",
    "Victor Wembanyama registered at least 25 points, 10 rebounds, 5 assists, and 5 blocks for the fifth time in his career.",
    "Dylan Harper scored 18 of his 31 points in the fourth quarter on 7 of 9 shooting."
  ],
  "keyPlayers": [
    {
      "name": "Victor Wembanyama",
      "team": "San Antonio Spurs",
      "hook": "Dominated with 26 points, 11 rebounds, 6 assists, and 5 blocks in 34 minutes."
    },
    {
      "name": "Dylan Harper",
      "team": "San Antonio Spurs",
      "hook": "Scored 18 of his game-high 31 points in the decisive fourth quarter."
    },
    {
      "name": "Mo Bamba",
      "team": "Utah Jazz",
      "hook": "Battled inside for 26 points and 12 rebounds for the Jazz."
    }
  ],
  "tags": [
    "nba",
    "san-antonio-spurs",
    "utah-jazz",
    "victor-wembanyama",
    "dylan-harper",
    "mo-bamba"
  ],
  "sources": [
    {
      "name": "NBA.com: Spurs at Jazz Official Box Score",
      "url": "https://www.nba.com/game/sas-vs-uta-20261115/box-score"
    },
    {
      "name": "San Antonio Express-News: Spurs win 12th straight behind Wembanyama and Harper",
      "url": "https://www.expressnews.com/sports/spurs/article/spurs-jazz-wembanyama-harper-streak-2026"
    },
    {
      "name": "Associated Press: Harper scores 31, Wembanyama adds 26 as Spurs top Jazz 110-102",
      "url": "https://apnews.com/article/spurs-jazz-nba-wembanyama-streak-20261115"
    }
  ]
}
open(nba_spurs_path, "w", encoding="utf-8").write(json.dumps(nba_spurs_data, indent=2, ensure_ascii=False) + "\n")
print("Created nba-spurs-vs-jazz match JSON.")

# 6. Update las-vegas-gp-strip-2026.json
vegas_path = os.path.join(MATCHES, "las-vegas-gp-strip-2026.json")
vegas_data = json.load(open(vegas_path, "r", encoding="utf-8"))
vegas_data["headline"] = "Three days to Round 21 Las Vegas: 33 points cover five drivers in furious shootout for P2"
vegas_data["roundLabel"] = "Round 21 · Three Days to Las Vegas"
vegas_data["teaser"] = "F1 arrives on the Las Vegas Strip with three days until Thursday night practice: 33 points cover Max Verstappen through Lando Norris in the fight for championship runner-up behind Kimi Antonelli."
vegas_data["whyCareReason"] = "Formula 1 descends on Nevada with 33 points covering Verstappen (279) to Norris (246) across the final three rounds, while Ferrari defends P2 constructors from Red Bull and McLaren."
open(vegas_path, "w", encoding="utf-8").write(json.dumps(vegas_data, indent=2, ensure_ascii=False) + "\n")
print("Updated las-vegas-gp match JSON.")
