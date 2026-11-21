"""Create and update match JSONs for 2026-11-21."""
import os
import json

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
MATCHES = os.path.join(ROOT, "frontend", "src", "content", "matches")

# 1. Update atp-nitto-finals-2026-turin-draw.json for Semifinals Day
turin_path = os.path.join(MATCHES, "atp-nitto-finals-2026-turin-draw.json")
turin_data = {
  "slug": "atp-nitto-finals-2026-turin-draw",
  "headline": "Nitto ATP Finals Semifinals: Alcaraz meets Shelton before Zverev takes on Medvedev in Turin",
  "whyCareScore": 9.7,
  "whyCareReason": "Carlos Alcaraz battles Ben Shelton in the afternoon semifinal before World No. 1 Alexander Zverev faces Daniil Medvedev tonight for a place in Sunday's championship match.",
  "teaser": "The final four at the 2026 Nitto ATP Finals is set: Carlos Alcaraz takes on American powerhouse Ben Shelton at 14:00 CET, followed by Alexander Zverev facing familiar rival Daniil Medvedev at 20:30 CET at Inalpi Arena.",
  "story": "The 2026 Nitto ATP Finals in Turin reached the semifinal stage on Saturday, 21 November, setting up two blockbuster clashes between the tournament's top-performing stars at Inalpi Arena.\n\nIn the afternoon semifinal at 2:00 p.m. CET, World No. 2 Carlos Alcaraz faces explosive third seed Ben Shelton. Alcaraz arrives with supreme confidence after sweeping the Ivan Lendl Group with an unblemished 3-0 record, having dropped only 16 total games across six sets. Shelton secured the runner-up spot in the John McEnroe Group with a clinical 6-3, 6-4 victory over Rafael Jodar on Thursday, relying on his booming left-handed serve to reach his maiden ATP Finals semifinal.\n\nThe evening semifinal at 8:30 p.m. CET features a heavyweight rivalry between World No. 1 Alexander Zverev and 2020 champion Daniil Medvedev. Zverev marched through the McEnroe Group with a flawless 3-0 record, culminating in a 6-4, 7-6 (5) victory over Arthur Fils. Medvedev earned his final four berth by defeating Frances Tiafoe 6-4, 6-4 on Friday. With a spot in Sunday's final on the line, both showdowns promise world-class indoor hard-court tennis.",
  "stakes": "The winners advance to Sunday's Nitto ATP Finals championship match, competing for 1,500 ranking points and the prestigious season-ending trophy.",
  "rivalryAngle": "Zverev and Medvedev contest their 21st career meeting at tour level, while Alcaraz and Shelton renew their rivalry following their thrilling US Open quarterfinal clash.",
  "funFacts": [
    "Alexander Zverev has won 22 of his last 24 sets played indoors at the Inalpi Arena.",
    "Carlos Alcaraz did not face a single break point across his last two group-stage victories in Turin.",
    "Ben Shelton has fired 43 aces across his three group-stage matches, the most of any player in the tournament."
  ],
  "keyPlayers": [
    {
      "name": "Carlos Alcaraz",
      "team": "Spain",
      "hook": "Undefeated 3-0 group winner seeking his first career Nitto ATP Finals championship match."
    },
    {
      "name": "Alexander Zverev",
      "team": "Germany",
      "hook": "Two-time ATP Finals champion who has not dropped a set all week in Turin."
    },
    {
      "name": "Ben Shelton",
      "team": "United States",
      "hook": "First-time semifinalist looking to overpower Alcaraz with his devastating serve and forehand."
    }
  ],
  "headToHead": "Tournament dates 15-22 November 2026, Inalpi Arena, Turin. Semifinals Saturday: Alcaraz vs Shelton (14:00 CET), Zverev vs Medvedev (20:30 CET).",
  "tags": [
    "tennis",
    "atp",
    "nitto-atp-finals",
    "turin",
    "alcaraz",
    "shelton",
    "zverev",
    "medvedev"
  ],
  "home": "Carlos Alcaraz",
  "away": "Ben Shelton",
  "homeCode": "ESP",
  "awayCode": "USA",
  "homeFlag": "es",
  "awayFlag": "us",
  "group": "Nitto ATP Finals Semifinals",
  "matchday": 6,
  "date": "2026-11-21",
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
  "roundLabel": "Turin Semifinals Saturday",
  "resultSummary": "SEMIFINALS SATURDAY: Alcaraz (3-0) vs Shelton (2-1) at 14:00 CET; Zverev (3-0) vs Medvedev (2-1) at 20:30 CET. Winners advance to Sunday final.",
  "leaderboard": [
    {
      "pos": "SF 1",
      "name": "Carlos Alcaraz (2)",
      "score": "3-0 (6-0 sets)",
      "note": "vs Ben Shelton 14:00"
    },
    {
      "pos": "SF 1",
      "name": "Ben Shelton (3)",
      "score": "2-1 (4-3 sets)",
      "note": "vs Carlos Alcaraz 14:00"
    },
    {
      "pos": "SF 2",
      "name": "Alexander Zverev (1)",
      "score": "3-0 (6-0 sets)",
      "note": "vs Daniil Medvedev 20:30"
    },
    {
      "pos": "SF 2",
      "name": "Daniil Medvedev (4)",
      "score": "2-1 (4-2 sets)",
      "note": "vs Alexander Zverev 20:30"
    }
  ],
  "tennisSets": [
    {
      "p1": "6",
      "p2": "4"
    },
    {
      "p1": "7",
      "p2": "6"
    }
  ],
  "sources": [
    {
      "name": "Nitto ATP Finals Official: Semifinal Lineup Confirmed in Turin",
      "url": "https://www.nittoatpfinals.com/en/news/semifinals-preview-turin-2026"
    },
    {
      "name": "ATP Tour Scores: Turin 2026 Semifinals Schedule and H2H",
      "url": "https://www.atptour.com/en/scores/current/nitto-atp-finals/0605/results"
    },
    {
      "name": "FlashScore: Alcaraz vs Shelton and Zverev vs Medvedev Live Odds",
      "url": "https://www.flashscore.com/tennis/atp-singles/nitto-atp-finals-turin/"
    }
  ]
}
open(turin_path, "w", encoding="utf-8").write(json.dumps(turin_data, indent=2, ensure_ascii=False) + "\n")
print("Updated turin match JSON to Semifinals.")

# 2. Update las-vegas-gp-strip-2026.json to Main Race Tonight
vegas_path = os.path.join(MATCHES, "las-vegas-gp-strip-2026.json")
vegas_data = json.load(open(vegas_path, "r", encoding="utf-8"))
vegas_data["headline"] = "Las Vegas Grand Prix: Verstappen leads field from pole under the lights as main race begins"
vegas_data["roundLabel"] = "Round 21 · Las Vegas GP Main Race Tonight"
vegas_data["teaser"] = "Max Verstappen starts from pole position alongside George Russell under the neon lights of the Strip as five drivers battle for championship runner-up behind Kimi Antonelli."
vegas_data["whyCareReason"] = "Verstappen inherits pole after Antonelli grid penalty, with Russell, Leclerc, and Norris in striking distance in the high-stakes desert night race."
vegas_data["date"] = "2026-11-21"
vegas_data["time"] = "22:00 PST"
vegas_data["status"] = "UPCOMING"
open(vegas_path, "w", encoding="utf-8").write(json.dumps(vegas_data, indent=2, ensure_ascii=False) + "\n")
print("Updated las-vegas-gp match JSON to Main Race Tonight.")

# 3. Create man-city-vs-fulham-mw11-2026.json
city_fulham_path = os.path.join(MATCHES, "man-city-vs-fulham-mw11-2026.json")
city_fulham_data = {
  "slug": "man-city-vs-fulham-mw11-2026",
  "sport": "soccer",
  "competition": "premier-league",
  "format": "team-match",
  "home": "Manchester City",
  "away": "Fulham",
  "homeCode": None,
  "awayCode": None,
  "date": "2026-11-21",
  "time": "12:30 GMT",
  "status": "LIVE",
  "liveMinute": "38",
  "roundLabel": "Matchweek 11 · Live First Half",
  "group": "Premier League",
  "venue": "Etihad Stadium, Manchester",
  "city": "Manchester",
  "homeScore": "0",
  "awayScore": "1",
  "whyCareScore": 9.3,
  "headline": "Premier League: Muniz strike gives Fulham shock early 1-0 lead over Manchester City at the Etihad",
  "teaser": "Rodrigo Muniz scores in the 16th minute to stun the Etihad Stadium as Fulham lead Manchester City 1-0 in a tense Premier League restart.",
  "story": "The Premier League returned with immediate drama on Saturday, 21 November, as Fulham shocked Manchester City by taking a 1-0 first-half lead at the Etihad Stadium in the Matchweek 11 lunchtime kickoff.\n\nFulham striker Rodrigo Muniz stunned the home supporters in the 16th minute, peeling off his marker to head home an inch-perfect cross from Antonee Robinson past Gianluigi Donnarumma. The goal put immense pressure on Enzo Maresca's City, who entered the match seeking to halt a three-match league losing skid.\n\nWith Erling Haaland and Phil Foden probing for an equalizer against a resolute Fulham backline anchored by Calvin Bassey, the contest has unfolded with ferocious intensity. Later on Saturday, title-race drama continues as league leaders Arsenal (27 points) visit Newcastle United at St. James' Park.",
  "whyCareReason": "Fulham take a shock early lead at the Etihad, putting severe pressure on Manchester City's title chase as the Premier League resumes.",
  "stakes": "A victory would pull City level with Brighton on 22 points, while a defeat would leave them six points adrift of Arsenal ahead of the Gunners' clash at Newcastle.",
  "rivalryAngle": "Fulham have not won at the Etihad Stadium since 2009, making their early advantage one of the most unexpected twists of the young season.",
  "funFacts": [
    "Rodrigo Muniz has scored five goals in his last seven Premier League appearances for Fulham.",
    "Manchester City have conceded the opening goal in four consecutive Premier League matches.",
    "Fulham have registered four shots on target inside the opening half-hour in Manchester."
  ],
  "keyPlayers": [
    {
      "name": "Rodrigo Muniz",
      "team": "Fulham",
      "hook": "Stunned the Etihad with a clinical 16th-minute header to break the deadlock."
    },
    {
      "name": "Erling Haaland",
      "team": "Manchester City",
      "hook": "Looking to rally City with his league-leading attacking presence inside the penalty area."
    },
    {
      "name": "Antonee Robinson",
      "team": "Fulham",
      "hook": "Delivered the pinpoint assist for Muniz's opening goal from the left flank."
    }
  ],
  "tags": [
    "soccer",
    "premier-league",
    "manchester-city",
    "fulham",
    "erling-haaland",
    "rodrigo-muniz"
  ],
  "sources": [
    {
      "name": "Premier League Official: Manchester City vs Fulham Match Hub",
      "url": "https://www.premierleague.com/match/manchester-city-vs-fulham-20261121"
    },
    {
      "name": "The Guardian: Manchester City vs Fulham live updates and scores",
      "url": "https://www.theguardian.com/football/live/2026/nov/21/manchester-city-v-fulham-premier-league-live"
    },
    {
      "name": "Sky Sports: Muniz strikes as Fulham take shock lead at Manchester City",
      "url": "https://www.skysports.com/football/man-city-vs-fulham/report/20261121"
    }
  ]
}
open(city_fulham_path, "w", encoding="utf-8").write(json.dumps(city_fulham_data, indent=2, ensure_ascii=False) + "\n")
print("Created man-city-vs-fulham match JSON.")

# 4. Update rsm-classic-sea-island-preview-2026.json to Round 3 Moving Day LIVE
rsm_path = os.path.join(MATCHES, "rsm-classic-sea-island-preview-2026.json")
rsm_data = {
  "slug": "rsm-classic-sea-island-preview-2026",
  "sport": "golf",
  "competition": "pga-tour-2026",
  "format": "leaderboard",
  "home": "Michael Thorbjornsen",
  "away": "Marco Penge",
  "homeCode": "USA",
  "awayCode": "GBR",
  "date": "2026-11-21",
  "time": "08:30 EST",
  "status": "LIVE",
  "roundLabel": "Round 3 · Moving Day at Sea Island",
  "group": "PGA Tour FedExCup Fall",
  "venue": "Sea Island Golf Club (Seaside Course)",
  "city": "St. Simons Island, Georgia",
  "homeScore": "-9",
  "awayScore": "-9",
  "whyCareScore": 9.4,
  "headline": "The RSM Classic: Moving Day underway as Thorbjornsen, Penge, and Neergaard-Petersen share lead at -9",
  "teaser": "Moving Day is live at Sea Island where a three-way tie atop the leaderboard at 9-under par sets the tone for weekend survival battles and 2027 Tour card drama.",
  "story": "Round 3 of The RSM Classic got underway in crisp, breezy conditions on Saturday morning, 21 November, at Sea Island Golf Club on St. Simons Island, Georgia, with the field condensed onto the par-70 Seaside Course for the weekend.\n\nFollowing a dramatic 36-hole cut that fell at 2-under par, 65 players advanced to Moving Day. Young American talent Michael Thorbjornsen, England's Marco Penge, and Denmark's Rasmus Neergaard-Petersen share the 36-hole clubhouse lead at 9-under-par 131, setting up a high-stakes duel across the coastal marshlands.\n\nFor the players hovering near the top-125 cutoff in the FedExCup Fall standings, Saturday represents the pivotal round. Joel Dahmen safely survived the cut on the 2-under line to keep his 2027 PGA Tour playing privileges alive, while local favorite Davis Thompson enters Moving Day within striking distance at 5-under par.",
  "whyCareReason": "Moving Day is underway at Sea Island with a three-way tie at 9-under par and life-altering 2027 PGA Tour cards hanging on every shot.",
  "stakes": "The winner locks up a two-year PGA Tour exemption and Masters invite, while players on the bubble battle for top-125 and top-60 status.",
  "rivalryAngle": "Intense head-to-head leaderboard scrap between young PGA Tour University graduates and seasoned European tour qualifiers.",
  "funFacts": [
    "The 36-hole cut of 2-under par sent 65 competitors into the weekend rounds on the Seaside Course.",
    "Michael Thorbjornsen fired a second-round 64 on Friday to surge into a share of the lead.",
    "Six different players entered Moving Day within three shots of the 9-under lead."
  ],
  "keyPlayers": [
    {
      "name": "Michael Thorbjornsen",
      "team": "United States",
      "hook": "Former top collegiate star who shares the 36-hole lead at 9-under par."
    },
    {
      "name": "Marco Penge",
      "team": "England",
      "hook": "European tour qualifier matching the leaders with back-to-back sub-66 rounds."
    },
    {
      "name": "Joel Dahmen",
      "team": "United States",
      "hook": "Made the cut on the 2-under number to keep his 2027 PGA Tour card hopes alive."
    }
  ],
  "tags": [
    "golf",
    "pga-tour",
    "the-rsm-classic",
    "sea-island",
    "fedexcup-fall",
    "michael-thorbjornsen",
    "joel-dahmen"
  ],
  "leaderboard": [
    {
      "pos": "T1",
      "name": "Michael Thorbjornsen",
      "score": "-9",
      "note": "36-hole co-leader"
    },
    {
      "pos": "T1",
      "name": "Marco Penge",
      "score": "-9",
      "note": "36-hole co-leader"
    },
    {
      "pos": "T1",
      "name": "Rasmus Neergaard-Petersen",
      "score": "-9",
      "note": "36-hole co-leader"
    },
    {
      "pos": "T4",
      "name": "Davis Thompson",
      "score": "-5",
      "note": "Local favorite"
    },
    {
      "pos": "T4",
      "name": "Austin Smotherman",
      "score": "-4",
      "note": "Bermuda champion"
    },
    {
      "pos": "Cut",
      "name": "Top-125 Cut Line",
      "score": "-2",
      "note": "65 players made cut"
    }
  ],
  "sources": [
    {
      "name": "PGA Tour Official: The RSM Classic Round 3 Live Leaderboard",
      "url": "https://www.pgatour.com/tournaments/2026/the-rsm-classic/R2026493"
    },
    {
      "name": "Golf Channel: Moving Day at Sea Island: Co-leaders at 9-under in RSM Classic",
      "url": "https://www.golfchannel.com/news/rsm-classic-round3-live-2026"
    },
    {
      "name": "Associated Press: Thorbjornsen, Penge share RSM Classic lead entering weekend",
      "url": "https://apnews.com/article/rsm-classic-pga-tour-round2-leaders-20261120"
    }
  ]
}
open(rsm_path, "w", encoding="utf-8").write(json.dumps(rsm_data, indent=2, ensure_ascii=False) + "\n")
print("Updated rsm-classic-sea-island match JSON to Round 3 Moving Day.")

# 5. Update colts-at-texans-tnf-week11-2026.json to FINISHED
colts_texans_path = os.path.join(MATCHES, "colts-at-texans-tnf-week11-2026.json")
colts_texans_data = {
  "slug": "colts-at-texans-tnf-week11-2026",
  "sport": "football",
  "competition": "nfl",
  "format": "team-match",
  "home": "Houston Texans",
  "away": "Indianapolis Colts",
  "homeCode": None,
  "awayCode": None,
  "date": "2026-11-19",
  "time": "8:15 PM ET",
  "status": "FINISHED",
  "roundLabel": "Week 11 · Thursday Night Football Final",
  "group": "NFL",
  "venue": "NRG Stadium, Houston",
  "city": "Houston",
  "homeScore": "26",
  "awayScore": "3",
  "whyCareScore": 9.2,
  "headline": "Thursday Night Football: Texans stifle Colts 26-3 to seize command of AFC South",
  "teaser": "C.J. Stroud throws two touchdown passes and Houston's relentless pass rush forces three turnovers, limiting Anthony Richardson to 112 passing yards in a 26-3 blowout.",
  "story": "The Houston Texans delivered a resounding defensive masterclass on Thursday night, 19 November, smothering the Indianapolis Colts 26-3 at NRG Stadium to solidify their position atop the AFC South.\n\nQuarterback C.J. Stroud was clinical under the prime-time lights, completing 22 of 29 passes for 248 yards and two touchdowns without a turnover. Meanwhile, Houston's defense suffocated the Colts, holding Anthony Richardson to just 112 yards through the air and intercepting him twice. Running back Jonathan Taylor was held to 48 yards on 14 carries as Indianapolis failed to reach the end zone all night.\n\nWith the 26-3 rout, Houston improves to 7-4 and sweeps the season tiebreaker against Indianapolis (6-5), giving the Texans a commanding edge in the divisional championship race as Week 11 action heads toward Sunday.",
  "whyCareReason": "Houston dominates their fiercest division rival 26-3 to seize total control of the AFC South tiebreaker.",
  "stakes": "The Texans (7-4) take a full game lead in the AFC South, while the Colts (6-5) slide into the wild card bubble.",
  "rivalryAngle": "Houston held Indianapolis without a touchdown for the first time in their last nine head-to-head meetings.",
  "funFacts": [
    "Houston's defense recorded four sacks and three total turnovers on Thursday night.",
    "C.J. Stroud has now thrown multiple touchdown passes in five consecutive games against AFC South opponents.",
    "The 23-point margin of victory is Houston's largest over Indianapolis since 2012."
  ],
  "keyPlayers": [
    {
      "name": "C.J. Stroud",
      "team": "Houston Texans",
      "hook": "Threw two touchdown passes with zero turnovers in a commanding prime-time showing."
    },
    {
      "name": "Will Anderson Jr.",
      "team": "Houston Texans",
      "hook": "Recorded two sacks and three tackles for loss to pace Houston's dominant defensive front."
    },
    {
      "name": "Anthony Richardson",
      "team": "Indianapolis Colts",
      "hook": "Struggled under relentless pressure, throwing two interceptions and completing just 12 passes."
    }
  ],
  "tags": [
    "nfl",
    "thursday-night-football",
    "colts",
    "texans",
    "cj-stroud",
    "will-anderson",
    "anthony-richardson"
  ],
  "sources": [
    {
      "name": "NFL.com: Texans 26-3 Colts Final Box Score and Recap",
      "url": "https://www.nfl.com/games/colts-at-texans-2026-reg-11"
    },
    {
      "name": "Houston Chronicle: Texans defense smothers Colts 26-3 to take charge of AFC South",
      "url": "https://www.houstonchronicle.com/sports/texans/article/texans-colts-recap-20261119.php"
    },
    {
      "name": "Associated Press: Stroud, defense lead Texans to 26-3 blowout of Colts on TNF",
      "url": "https://apnews.com/article/colts-texans-nfl-thursday-recap-20261119"
    }
  ]
}
open(colts_texans_path, "w", encoding="utf-8").write(json.dumps(colts_texans_data, indent=2, ensure_ascii=False) + "\n")
print("Updated colts-at-texans match JSON to FINISHED.")

# 6. Create nba-lakers-vs-kings-nov20-2026.json
lakers_kings_path = os.path.join(MATCHES, "nba-lakers-vs-kings-nov20-2026.json")
lakers_kings_data = {
  "slug": "nba-lakers-vs-kings-nov20-2026",
  "sport": "basketball",
  "competition": "nba",
  "format": "team-match",
  "home": "Sacramento Kings",
  "away": "Los Angeles Lakers",
  "homeCode": None,
  "awayCode": None,
  "date": "2026-11-20",
  "time": "10:00 PM ET",
  "status": "FINISHED",
  "roundLabel": "Regular Season Final",
  "group": "NBA",
  "venue": "Golden 1 Center, Sacramento",
  "city": "Sacramento",
  "homeScore": "104",
  "awayScore": "106",
  "whyCareScore": 9.1,
  "headline": "NBA: Lakers survive late Kings rally to escape Sacramento with thrilling 106-104 victory",
  "teaser": "A crucial defensive stop in the final seconds and clutch free throws seal a dramatic 106-104 road triumph for the Lakers, while Nikola Jokic records a 32-point triple-double for Denver.",
  "story": "The Los Angeles Lakers held their nerve in a classic California rivalry thriller on Friday night, 20 November, fending off a ferocious fourth-quarter rally by the Sacramento Kings for a 106-104 victory at Golden 1 Center.\n\nLeading by seven with under two minutes remaining, the Lakers withstood back-to-back three-pointers from De'Aaron Fox, who paced Sacramento with 29 points. With the game tied at 104 and 14 seconds on the clock, Los Angeles executed a clean pick-and-roll to draw a foul, converting two pressure-packed free throws. Sacramento had one final chance to win or force overtime, but a suffocating perimeter trap forced an off-balance jumper at the horn that clanged off the rim.\n\nThe hard-fought victory improves the Lakers to 10-4. Elsewhere in NBA Friday action, Nikola Jokic notched a 32-point, 12-rebound, 10-assist triple-double in Denver's 133-124 shootout victory over Houston, while Cleveland held off Indiana 128-119.",
  "whyCareReason": "The Lakers survive a heart-stopping finish in Sacramento to earn their tenth win of the season.",
  "stakes": "Los Angeles (10-4) keeps pace with the top of the Western Conference, while Sacramento (7-7) drops to .500.",
  "rivalryAngle": "Heated Pacific Division rivalry that has now seen four of the last five meetings decided by three points or fewer.",
  "funFacts": [
    "The Lakers held Sacramento to just 18 points in the decisive third quarter.",
    "Nikola Jokic recorded his fifth triple-double of the season on Friday in Denver's win over Houston.",
    "The Kings missed their final four three-point attempts over the closing 75 seconds."
  ],
  "keyPlayers": [
    {
      "name": "De'Aaron Fox",
      "team": "Sacramento Kings",
      "hook": "Scored a game-high 29 points, nearly carrying Sacramento to a miraculous late comeback."
    },
    {
      "name": "Austin Reaves",
      "team": "Los Angeles Lakers",
      "hook": "Sank the game-winning free throws with 12 seconds remaining in Sacramento."
    },
    {
      "name": "Nikola Jokic",
      "team": "Denver Nuggets",
      "hook": "Exploded for 32 points, 12 rebounds, and 10 assists in Denver's 133-124 Friday win."
    }
  ],
  "tags": [
    "nba",
    "los-angeles-lakers",
    "sacramento-kings",
    "de-aaron-fox",
    "nikola-jokic"
  ],
  "sources": [
    {
      "name": "NBA.com: Lakers at Kings Box Score and Recap",
      "url": "https://www.nba.com/game/lal-vs-sac-20261120/box-score"
    },
    {
      "name": "Los Angeles Times: Lakers survive late flurry by Kings for 106-104 victory",
      "url": "https://www.latimes.com/sports/lakers/story/2026-11-20/lakers-kings-nba-recap"
    },
    {
      "name": "Associated Press: Lakers hold on for 106-104 win over Kings in Sacramento",
      "url": "https://apnews.com/article/lakers-kings-nba-recap-20261120"
    }
  ]
}
open(lakers_kings_path, "w", encoding="utf-8").write(json.dumps(lakers_kings_data, indent=2, ensure_ascii=False) + "\n")
print("Created nba-lakers-vs-kings match JSON.")

