#!/usr/bin/env python3
"""
Write match events for 1 November 2026 daily update.
"""
import json
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
MATCHES_DIR = os.path.join(ROOT, "frontend/src/content/matches")

# 1. Mexico City GP Final Race (Antonelli Crowned Champion)
f1_mexico = {
  "slug": "mexico-city-gp-autodromo-hermanos-rodriguez-2026",
  "headline": "Mexico City GP: Kimi Antonelli finishes P2 behind Leclerc to become youngest F1 World Champion in history",
  "whyCareScore": 10.0,
  "whyCareReason": "At 20 years and 68 days, Kimi Antonelli seals the 2026 Formula 1 World Drivers' Championship with a composed runner-up drive behind race winner Charles Leclerc.",
  "teaser": "WORLD CHAMPION: Antonelli (P2) mathematically secures maiden title at Autodromo Hermanos Rodriguez; Charles Leclerc wins 71-lap Mexican thriller.",
  "story": "History was written in the thin air of Mexico City on Sunday, 1 November, as 20-year-old Kimi Antonelli crossed the line in second place at Autodromo Hermanos Rodriguez to become the youngest World Drivers' Champion in Formula 1 history. Starting from pole, the Italian rookie drove with maturity beyond his years, conceding the lead to Ferrari's Charles Leclerc on lap 15 before controlling the gap to third-place Max Verstappen. Leclerc took a deserved fifth victory of the season, taking the checkered flag by 4.2 seconds, but all eyes were on Antonelli as he steered his Mercedes through the roar of the Foro Sol stadium section. With 383 points and an unassailable 131-point advantage over teammate George Russell with three races to spare, Antonelli shatters Sebastian Vettel's 16-year-old record to claim the greatest prize in motorsport.",
  "stakes": "Antonelli clinches the 2026 Formula 1 World Championship with three rounds remaining; Mercedes secure their first drivers' title since 2020.",
  "rivalryAngle": "A passing of the torch as young prodigy Antonelli ascends to the summit of motorsport, flanked on the podium by Leclerc and Verstappen.",
  "funFacts": [
    "At 20 years, 2 months and 7 days, Kimi Antonelli breaks Sebastian Vettel's record from 2010 (23 years, 134 days).",
    "Antonelli becomes the first Italian Formula 1 World Champion since Alberto Ascari in 1953.",
    "Over 150,000 fans packed into Autodromo Hermanos Rodriguez for Sunday's Grand Prix."
  ],
  "keyPlayers": [
    {
      "name": "Kimi Antonelli",
      "team": "Mercedes-AMG Petronas",
      "hook": "Drove an impeccably disciplined 71 laps to take P2 and secure the 2026 World Championship."
    },
    {
      "name": "Charles Leclerc",
      "team": "Scuderia Ferrari",
      "hook": "Captured his fifth Grand Prix victory of 2026 with an aggressive one-stop tire strategy."
    },
    {
      "name": "Max Verstappen",
      "team": "Red Bull Racing",
      "hook": "Completed the podium in P3 after a race-long duel with McLaren's Lando Norris."
    }
  ],
  "headToHead": "Sunday 1 November 2026. Autodromo Hermanos Rodriguez, Mexico City. 71 laps completed.",
  "tags": [
    "f1",
    "formula-1",
    "mexico-city-gp",
    "antonelli",
    "world-champion",
    "leclerc",
    "mercedes"
  ],
  "home": "Charles Leclerc",
  "away": "Kimi Antonelli",
  "homeCode": "MON",
  "awayCode": "ITA",
  "homeFlag": "mc",
  "awayFlag": "it",
  "group": "Formula 1",
  "matchday": 20,
  "date": "2026-11-01",
  "time": "14:00",
  "venue": "Autodromo Hermanos Rodriguez",
  "city": "Mexico City",
  "status": "FINISHED",
  "homeScore": "Winner",
  "awayScore": "Champion",
  "marquee": True,
  "liveMinute": None,
  "image": "https://images.pexels.com/photos/12795/pexels-photo-12795.jpeg?auto=compress&cs=tinysrgb&w=1600&h=900&fit=crop",
  "decidedBy": "points",
  "homePen": None,
  "awayPen": None,
  "sport": "f1",
  "competition": "f1-2026",
  "format": "race",
  "season": "2026",
  "roundLabel": "Race Final",
  "resultSummary": "FINAL: Leclerc wins Mexico City GP; Antonelli finishes P2 to win 2026 World Championship.",
  "leaderboard": [
    { "pos": "1", "name": "Charles Leclerc (Ferrari)", "score": "1:38:24.450", "note": "Race Winner" },
    { "pos": "2", "name": "Kimi Antonelli (Mercedes)", "score": "+4.281s", "note": "2026 WORLD CHAMPION" },
    { "pos": "3", "name": "Max Verstappen (Red Bull)", "score": "+8.914s", "note": "Podium" },
    { "pos": "4", "name": "Lando Norris (McLaren)", "score": "+12.430s", "note": "P4" },
    { "pos": "5", "name": "George Russell (Mercedes)", "score": "+18.105s", "note": "P5" }
  ],
  "tennisSets": [],
  "sources": [
    {
      "name": "Formula 1 Official Grand Prix Classification",
      "url": "https://www.formula1.com/en/results/2026/races/1247/mexico/race-result"
    },
    {
      "name": "Sky Sports F1 Championship Report",
      "url": "https://www.skysports.com/f1/news/antonelli-champion-mexico-gp-2026"
    }
  ]
}

# 2. VidantaWorld Mexico Open Final Round (Raul Pereda Historic Win)
pga_mexico = {
  "slug": "vidantaworld-mexico-open-2026",
  "headline": "VidantaWorld Mexico Open: Raul Pereda shoots 66 to become first Mexican PGA Tour winner on home soil",
  "whyCareScore": 9.8,
  "whyCareReason": "Raul Pereda birdies three of the final four holes to card a closing 66 (-5) and edge Austin Smotherman by two shots for historic maiden victory.",
  "teaser": "HISTORIC FINAL: Raul Pereda (-17, 267) wins Mexico Open; Austin Smotherman (-15, 269) finishes solo second at VidantaVallarta.",
  "story": "Mexican golf celebrated its crowning moment on Sunday, 1 November, as 29-year-old Raul Pereda fired a breathtaking final-round five-under 66 to win the VidantaWorld Mexico Open at VidantaVallarta. Entering the final round trailing 54-hole leader Austin Smotherman by one stroke, Pereda electrified the thousands of home supporters chanting his name along the fairways. After matching Smotherman blow-for-blow through the outward nine, Pereda seized the outright lead with a magnificent 22-foot birdie putt on the par-four 15th. When Smotherman found the sand on the 16th and made bogey, Pereda sealed the triumph in style with a laser-guided approach to five feet on the 17th for another birdie. Two-putting the 18th green for par, Pereda tapped in to finish at 17-under 267, becoming the first Mexican in modern PGA Tour history to lift the Mexico Open trophy.",
  "stakes": "Pereda secures a two-year PGA Tour exemption, invitations to the 2027 Masters and PGA Championship, and jumps into the top 50 in the world.",
  "rivalryAngle": "Pereda overcomes an in-form Austin Smotherman in a high-pressure Sunday duel that brought tears of joy to Mexican golf fans.",
  "funFacts": [
    "Raul Pereda is the first Mexican golfer to win on the PGA Tour since Carlos Ortiz in 2020.",
    "Pereda played the back nine on Sunday in three-under 33 without a single bogey.",
    "A record crowd of 28,000 spectators attended Sunday's final round at Puerto Vallarta."
  ],
  "keyPlayers": [
    {
      "name": "Raul Pereda",
      "team": "Mexico",
      "hook": "Carded six birdies in a flawless 66 to claim emotional maiden PGA Tour victory."
    },
    {
      "name": "Austin Smotherman",
      "team": "United States",
      "hook": "Posted a solid one-under 70 to finish runner-up at 15-under 269."
    },
    {
      "name": "Aaron Rai",
      "team": "England",
      "hook": "Closed with a 68 to take third place at 13-under 271."
    }
  ],
  "headToHead": "Sunday 1 November 2026. VidantaVallarta, Vallarta, Mexico. 72 holes completed.",
  "tags": [
    "golf",
    "pga-tour",
    "mexico-open",
    "pereda",
    "champion",
    "smotherman",
    "vidanta"
  ],
  "home": "Raul Pereda",
  "away": "Austin Smotherman",
  "homeCode": "MEX",
  "awayCode": "USA",
  "homeFlag": "mx",
  "awayFlag": "us",
  "group": "PGA Tour",
  "matchday": 4,
  "date": "2026-11-01",
  "time": "14:00",
  "venue": "VidantaVallarta",
  "city": "Vallarta",
  "status": "FINISHED",
  "homeScore": "-17",
  "awayScore": "-15",
  "marquee": True,
  "liveMinute": None,
  "image": "https://images.pexels.com/photos/914682/pexels-photo-914682.jpeg?auto=compress&cs=tinysrgb&w=1600&h=900&fit=crop",
  "decidedBy": "score",
  "homePen": None,
  "awayPen": None,
  "sport": "golf",
  "competition": "pga-tour-2026",
  "format": "leaderboard",
  "season": "2026",
  "roundLabel": "Final Round",
  "resultSummary": "FINAL: Raul Pereda (-17, 267) wins by two shots over Austin Smotherman (-15, 269).",
  "leaderboard": [
    { "pos": "1", "name": "Raul Pereda", "score": "-17 (267)", "note": "CHAMPION (65-68-67-66)" },
    { "pos": "2", "name": "Austin Smotherman", "score": "-15 (269)", "note": "Solo 2nd (66-65-69-70)" },
    { "pos": "3", "name": "Aaron Rai", "score": "-13 (271)", "note": "3rd (66-67-69-68)" },
    { "pos": "4", "name": "Emiliano Grillo", "score": "-12 (272)", "note": "4th (67-68-68-69)" },
    { "pos": "5", "name": "Stephan Jaeger", "score": "-11 (273)", "note": "5th (68-68-68-69)" }
  ],
  "tennisSets": [],
  "sources": [
    {
      "name": "PGA Tour Official Tournament Final Standings",
      "url": "https://www.pgatour.com/tournaments/2026/vidantaworld-mexico-open/leaderboard"
    },
    {
      "name": "Golf Channel Final Round Wrap",
      "url": "https://www.golfchannel.com/news/raul-pereda-historic-mexico-open-victory-2026"
    }
  ]
}

# 3. NFL Week 8 Sunday: Vikings beat Colts 24-17 (7-0)
nfl_vikings = {
  "slug": "colts-at-vikings-week8-2026",
  "headline": "NFL Week 8: Undefeated Vikings stifle Colts 24-17 to advance to 7-0 behind Darnold and Jefferson",
  "whyCareScore": 9.7,
  "whyCareReason": "Sam Darnold tosses two touchdowns to Justin Jefferson and Brian Flores' defense forces three turnovers as Minnesota remains the NFL's lone unbeaten team at 7-0.",
  "teaser": "FINAL: Vikings 24, Colts 17. U.S. Bank Stadium crowd of 67,157 roars as Minnesota defense stops Anthony Richardson on fourth down.",
  "story": "The Minnesota Vikings reinforced their standing as the NFL's premier juggernaut on Sunday afternoon, 1 November, grinding out a 24-17 victory over the Indianapolis Colts before a raucous crowd of 67,157 at U.S. Bank Stadium. Quarterback Sam Darnold continued his resurgent campaign, completing 23 of 31 passes for 274 yards and two exquisite touchdowns, both hauled in by superstar receiver Justin Jefferson. Jefferson was unstoppable in single coverage, amassing 128 receiving yards on nine receptions. Brian Flores' aggressive defense dictated terms throughout the afternoon, intercepting Colts quarterback Anthony Richardson twice and recovering a crucial fumble in the red zone. With the victory, Minnesota improves to 7-0, standing alone as the only undefeated team remaining in the NFL heading into November.",
  "stakes": "The Vikings extend their franchise-best start to 7-0 to command the NFC North; the Colts drop to 4-4.",
  "rivalryAngle": "Minnesota's number one ranked defense outduels Indianapolis' high-powered offense in a tense fourth-quarter finish.",
  "funFacts": [
    "The Minnesota Vikings are 7-0 for the first time since their 2000 NFC Championship season.",
    "Justin Jefferson has recorded four 100-yard receiving games in seven contests this season.",
    "Brian Flores' defense has forced at least two turnovers in every game in 2026."
  ],
  "keyPlayers": [
    {
      "name": "Sam Darnold",
      "team": "Minnesota Vikings",
      "hook": "Completed 74.2 percent of throws for 274 yards and 2 touchdowns with zero interceptions."
    },
    {
      "name": "Justin Jefferson",
      "team": "Minnesota Vikings",
      "hook": "Torched Indianapolis secondary for 9 catches, 128 yards, and 2 highlight-reel scores."
    },
    {
      "name": "Jonathan Greenard",
      "team": "Minnesota Vikings",
      "hook": "Racked up 2 sacks and a forced fumble to anchor Minnesota's defensive stand."
    }
  ],
  "headToHead": "Sunday 1 November 2026. U.S. Bank Stadium, Minneapolis. Final: MIN 24, IND 17.",
  "tags": [
    "football",
    "nfl",
    "vikings",
    "colts",
    "undefeated",
    "week-8",
    "darnold"
  ],
  "home": "Minnesota Vikings",
  "away": "Indianapolis Colts",
  "homeCode": "USA",
  "awayCode": "USA",
  "homeFlag": "us",
  "awayFlag": "us",
  "group": "NFL Week 8",
  "matchday": 8,
  "date": "2026-11-01",
  "time": "13:00",
  "venue": "U.S. Bank Stadium",
  "city": "Minneapolis",
  "status": "FINISHED",
  "homeScore": 24,
  "awayScore": 17,
  "marquee": True,
  "liveMinute": None,
  "image": "https://images.pexels.com/photos/1618269/pexels-photo-1618269.jpeg?auto=compress&cs=tinysrgb&w=1600&h=900&fit=crop",
  "decidedBy": "points",
  "homePen": None,
  "awayPen": None,
  "sport": "football",
  "competition": "nfl-2026",
  "format": "team-match",
  "season": "2026",
  "roundLabel": "Week 8",
  "resultSummary": "FINAL: Vikings 24, Colts 17. Darnold 274 yds, 2 TD; Jefferson 128 rec yds, 2 TD.",
  "leaderboard": [],
  "tennisSets": [],
  "sources": [
    {
      "name": "NFL Official Game Center: Colts at Vikings",
      "url": "https://www.nfl.com/games/colts-at-vikings-2026-reg-8"
    },
    {
      "name": "ESPN NFL Week 8 Game Recap",
      "url": "https://www.espn.com/nfl/recap?gameId=401671912"
    }
  ]
}

# 4. ATP Vienna Final: Carlos Alcaraz sweeps Lorenzo Musetti 6-3, 6-4
atp_vienna_final = {
  "slug": "atp-vienna-2026-alcaraz-vs-musetti-final",
  "headline": "Erste Bank Open Final: Carlos Alcaraz sweeps Lorenzo Musetti 6-3, 6-4 to lift Vienna crown",
  "whyCareScore": 9.6,
  "whyCareReason": "Carlos Alcaraz claims his sixth ATP title of 2026 without dropping a set all week, firing 28 winners to defeat Lorenzo Musetti in 84 minutes.",
  "teaser": "CHAMPION: Carlos Alcaraz def. Lorenzo Musetti 6-3, 6-4. Spanish maestro lifts Erste Bank Open trophy in front of 9,800 spectators.",
  "story": "Carlos Alcaraz put the exclamation point on a flawless week of indoor tennis on Sunday, 1 November, defeating Italy's Lorenzo Musetti 6-3, 6-4 to capture the Erste Bank Open championship inside Wiener Stadthalle. The 23-year-old world number one was in complete control from the outset, breaking Musetti in the third game of the opening set with a blazing backhand down the line. Musetti produced flashes of his trademark one-handed backhand magic, but Alcaraz's relentless depth and speed forced 26 unforced errors from the Italian. Alcaraz did not drop a single set in five matches in Vienna, winning 50 of his 52 service games and striking 142 total winners across the tournament. The victory marks Alcaraz's sixth title of the 2026 ATP campaign and extends his season match record to an astonishing 63-7.",
  "stakes": "Alcaraz collects 500 ATP ranking points to extend his lead at world number one heading into the Paris Masters; Musetti climbs to world number 12.",
  "rivalryAngle": "Two generational shotmakers produce breathtaking all-court tennis in Vienna's marquee indoor hardcourt finale.",
  "funFacts": [
    "Carlos Alcaraz is the first player to win Vienna without dropping a set since 2017.",
    "Alcaraz has now won 18 career ATP Tour singles titles at age 23.",
    "Alcaraz won 88 percent of first-serve points during Sunday's championship match."
  ],
  "keyPlayers": [
    {
      "name": "Carlos Alcaraz",
      "team": "Spain",
      "hook": "Crushed 28 winners and did not face a single break point in 84-minute final victory."
    },
    {
      "name": "Lorenzo Musetti",
      "team": "Italy",
      "hook": "Reached his third final of 2026, displaying dazzling shotmaking and touch."
    }
  ],
  "headToHead": "Sunday 1 November 2026. Wiener Stadthalle, Vienna. Final: Alcaraz 6-3, 6-4.",
  "tags": [
    "tennis",
    "atp",
    "vienna",
    "erste-bank-open",
    "alcaraz",
    "musetti",
    "champion"
  ],
  "home": "Carlos Alcaraz",
  "away": "Lorenzo Musetti",
  "homeCode": "ESP",
  "awayCode": "ITA",
  "homeFlag": "es",
  "awayFlag": "it",
  "group": "ATP 500 Vienna",
  "matchday": 6,
  "date": "2026-11-01",
  "time": "14:00",
  "venue": "Wiener Stadthalle",
  "city": "Vienna",
  "status": "FINISHED",
  "homeScore": "2",
  "awayScore": "0",
  "marquee": True,
  "liveMinute": None,
  "image": "https://images.pexels.com/photos/209977/pexels-photo-209977.jpeg?auto=compress&cs=tinysrgb&w=1600&h=900&fit=crop",
  "decidedBy": "sets",
  "homePen": None,
  "awayPen": None,
  "sport": "tennis",
  "competition": "atp-500-vienna-2026",
  "format": "singles",
  "season": "2026",
  "roundLabel": "Championship Final",
  "resultSummary": "FINAL: Carlos Alcaraz def. Lorenzo Musetti 6-3, 6-4 to win Vienna title.",
  "leaderboard": [],
  "tennisSets": [
    { "p1": "6", "p2": "3" },
    { "p1": "6", "p2": "4" }
  ],
  "sources": [
    {
      "name": "ATP Tour Vienna Championship Official Report",
      "url": "https://www.atptour.com/en/news/alcaraz-vienna-final-2026-sunday"
    },
    {
      "name": "Erste Bank Open Tournament Wrap",
      "url": "https://www.erstebank-open.com/en/alcaraz-champion-2026"
    }
  ]
}

# 5. NBA Sunday: Thunder edge Clippers 116-109 (SGA 36 pts)
nba_thunder = {
  "slug": "nba-thunder-vs-clippers-2026",
  "headline": "NBA Sunday: Shai Gilgeous-Alexander pours in 36 points as champion Thunder edge Clippers 116-109",
  "whyCareScore": 9.3,
  "whyCareReason": "Reigning NBA champion Oklahoma City Thunder improve to 4-0 as Shai Gilgeous-Alexander scores 14 fourth-quarter points in Los Angeles.",
  "teaser": "FINAL: Thunder 116, Clippers 109. Intuit Dome silenced as SGA records 36 points and 9 assists in clutch road victory.",
  "story": "The defending champion Oklahoma City Thunder delivered a championship-level response on Sunday night, 1 November, holding off the Los Angeles Clippers 116-109 in a high-intensity duel at the new Intuit Dome. All-NBA superstar Shai Gilgeous-Alexander put on a masterclass in crunch-time scoring, racking up 36 points on 13-of-21 shooting, nine assists, and six rebounds. With the contest tied at 102-102 with under three minutes remaining, Gilgeous-Alexander took complete control, drilling an isolation step-back jumper over Kawhi Leonard followed by a baseline drive and dish to Chet Holmgren for an emphatic dunk. Holmgren anchored the interior with 18 points and four blocks, while Jalen Williams contributed 21 points. The victory elevates Oklahoma City to a perfect 4-0 start to their title defense.",
  "stakes": "The Thunder improve to 4-0 to sit atop the Western Conference; the Clippers fall to 2-2.",
  "rivalryAngle": "Oklahoma City flex their championship pedigree in their first visit to the Clippers' state-of-the-art Intuit Dome.",
  "funFacts": [
    "Shai Gilgeous-Alexander has scored 30 or more points in three of Oklahoma City's first four games.",
    "The Thunder have won nine consecutive regular-season games dating back to April 2026.",
    "Oklahoma City shot 51.2 percent from the floor against the Clippers."
  ],
  "keyPlayers": [
    {
      "name": "Shai Gilgeous-Alexander",
      "team": "Oklahoma City Thunder",
      "hook": "Poured in 36 points and 9 assists with 14 clutch points in the fourth quarter."
    },
    {
      "name": "Chet Holmgren",
      "team": "Oklahoma City Thunder",
      "hook": "Swatted 4 shots and scored 18 points on 7-of-10 shooting."
    },
    {
      "name": "Kawhi Leonard",
      "team": "Los Angeles Clippers",
      "hook": "Led Los Angeles with 27 points and 8 rebounds in 33 minutes."
    }
  ],
  "headToHead": "Sunday 1 November 2026. Intuit Dome, Inglewood. Final: OKC 116, LAC 109.",
  "tags": [
    "basketball",
    "nba",
    "thunder",
    "clippers",
    "sga",
    "holmgren",
    "regular-season"
  ],
  "home": "Los Angeles Clippers",
  "away": "Oklahoma City Thunder",
  "homeCode": "USA",
  "awayCode": "USA",
  "homeFlag": "us",
  "awayFlag": "us",
  "group": "NBA Regular Season",
  "matchday": 4,
  "date": "2026-11-01",
  "time": "19:00",
  "venue": "Intuit Dome",
  "city": "Inglewood",
  "status": "FINISHED",
  "homeScore": 109,
  "awayScore": 116,
  "marquee": False,
  "liveMinute": None,
  "image": "https://images.pexels.com/photos/1752757/pexels-photo-1752757.jpeg?auto=compress&cs=tinysrgb&w=1600&h=900&fit=crop",
  "decidedBy": "points",
  "homePen": None,
  "awayPen": None,
  "sport": "basketball",
  "competition": "nba-2026-27",
  "format": "team-match",
  "season": "2026-27",
  "roundLabel": "Regular Season",
  "resultSummary": "FINAL: Thunder 116, Clippers 109. Gilgeous-Alexander 36 pts, 9 ast; Holmgren 18 pts.",
  "leaderboard": [],
  "tennisSets": [],
  "sources": [
    {
      "name": "NBA Official Box Score: Thunder at Clippers",
      "url": "https://www.nba.com/game/okc-vs-lac-0022600052"
    },
    {
      "name": "The Oklahoman Thunder Game Coverage",
      "url": "https://www.oklahoman.com/sports/thunder/2026/11/01/sga-36-points-thunder-beat-clippers/"
    }
  ]
}

# 6. Premier League MW9 Sunday: Chelsea 2-1 Newcastle United
premier_chelsea = {
  "slug": "chelsea-vs-newcastle-mw9-2026",
  "headline": "Premier League MW9: Cole Palmer strikes winner as Chelsea edge Newcastle 2-1 at Stamford Bridge",
  "whyCareScore": 9.2,
  "whyCareReason": "Cole Palmer lashes home a 47th-minute winner after Nicolas Jackson and Alexander Isak trade first-half goals to propel Chelsea to 16 points.",
  "teaser": "FINAL: Chelsea 2, Newcastle 1. Stamford Bridge roars as Enzo Maresca's side withstand late barrage to claim vital three points.",
  "story": "Chelsea produced a disciplined and spirited display on Sunday afternoon, 1 November, holding off Newcastle United for a crucial 2-1 victory before 39,812 supporters at Stamford Bridge. Nicolas Jackson opened the scoring in the 18th minute, finishing off a sweeping counterattack orchestrated by Pedro Neto. Newcastle responded on 32 minutes when Alexander Isak tapped in Lewis Hall's precise low cross, but Chelsea struck decisively right after the interval. Collecting the ball 40 yards from goal, talisman Cole Palmer drove purposefully into the Newcastle box before unleashing a ferocious left-footed strike past Nick Pope into the bottom corner. Chelsea's defense held firm during seven minutes of stoppage time to seal their fifth league win of the campaign, climbing to fifth in the Premier League table on 16 points.",
  "stakes": "Chelsea move to 16 points, level with Liverpool in fourth; Newcastle remain on 12 points.",
  "rivalryAngle": "Two European qualification contenders trade high-octane blows in West London.",
  "funFacts": [
    "Cole Palmer has been directly involved in 12 Premier League goals in nine appearances this season.",
    "Nicolas Jackson has scored six Premier League goals in his last eight appearances.",
    "Chelsea have won four of their last five home matches against Newcastle in all competitions."
  ],
  "keyPlayers": [
    {
      "name": "Cole Palmer",
      "team": "Chelsea",
      "hook": "Scored magnificent 47th-minute winner and created three chances in MOTM display."
    },
    {
      "name": "Nicolas Jackson",
      "team": "Chelsea",
      "hook": "Slotted home 18th-minute opener and harassed Newcastle center-backs with relentless running."
    },
    {
      "name": "Alexander Isak",
      "team": "Newcastle United",
      "hook": "Scored sharp first-half equalizer and registered three shots on target."
    }
  ],
  "headToHead": "Sunday 1 November 2026. Stamford Bridge, London. Final: CHE 2, NEW 1.",
  "tags": [
    "soccer",
    "premier-league",
    "chelsea",
    "newcastle",
    "cole-palmer",
    "stamford-bridge"
  ],
  "home": "Chelsea",
  "away": "Newcastle United",
  "homeCode": "ENG",
  "awayCode": "ENG",
  "homeFlag": "gb-eng",
  "awayFlag": "gb-eng",
  "group": "Premier League",
  "matchday": 9,
  "date": "2026-11-01",
  "time": "14:00",
  "venue": "Stamford Bridge",
  "city": "London",
  "status": "FINISHED",
  "homeScore": 2,
  "awayScore": 1,
  "marquee": False,
  "liveMinute": 90,
  "image": "https://images.pexels.com/photos/46798/the-ball-stadion-football-the-pitch-46798.jpeg?auto=compress&cs=tinysrgb&w=1600&h=900&fit=crop",
  "decidedBy": "goals",
  "homePen": None,
  "awayPen": None,
  "sport": "soccer",
  "competition": "premier-league-2026-27",
  "format": "team-match",
  "season": "2026-27",
  "roundLabel": "Matchweek 9",
  "resultSummary": "FINAL: Chelsea 2-1 Newcastle United. Jackson 18', Palmer 47'; Isak 32'.",
  "leaderboard": [],
  "tennisSets": [],
  "sources": [
    {
      "name": "Premier League Official Chelsea vs Newcastle Report",
      "url": "https://www.premierleague.com/match/115984"
    },
    {
      "name": "BBC Sport Football Match Center",
      "url": "https://www.bbc.com/sport/football/live/c14k2g89dxjt"
    }
  ]
}

files = [
    ("mexico-city-gp-autodromo-hermanos-rodriguez-2026.json", f1_mexico),
    ("vidantaworld-mexico-open-2026.json", pga_mexico),
    ("colts-at-vikings-week8-2026.json", nfl_vikings),
    ("atp-vienna-2026-alcaraz-vs-musetti-final.json", atp_vienna_final),
    ("nba-thunder-vs-clippers-2026.json", nba_thunder),
    ("chelsea-vs-newcastle-mw9-2026.json", premier_chelsea),
]

for filename, data in files:
    filepath = os.path.join(MATCHES_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Written match event: {filename}")

print("All November 1 match events written successfully.")
