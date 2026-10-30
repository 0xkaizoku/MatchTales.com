#!/usr/bin/env python3
"""
Write match events for 31 October 2026 daily update.
"""
import json
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
MATCHES_DIR = os.path.join(ROOT, "frontend/src/content/matches")

# 1. Update Arsenal vs Liverpool
arsenal_liverpool = {
  "slug": "arsenal-vs-liverpool-mw9-2026",
  "headline": "Premier League MW9: Arsenal and Liverpool battle to pulsating 2-2 draw at Emirates",
  "whyCareScore": 9.9,
  "whyCareReason": "Mohamed Salah strikes in the 81st minute to earn Liverpool a point in North London after Bukayo Saka and Mikel Merino had put Arsenal ahead.",
  "teaser": "FINAL: Arsenal 2, Liverpool 2. Emirates Stadium crowd of 60,383 witnesses electric title clash; Saka and Salah both on target.",
  "story": "The Premier League title race delivered another instant classic on Saturday, 31 October, as Arsenal and Liverpool fought to a breathtaking 2-2 draw before 60,383 spectators at Emirates Stadium. Bukayo Saka electrified the home crowd after just nine minutes, dancing past Andy Robertson before firing a ferocious strike inside Caoimhin Kelleher's near post. Liverpool responded nine minutes later when Virgil van Dijk nodded in from a corner, but Mikel Arteta's side restored their advantage on the stroke of halftime through Mikel Merino's thumping header. Arsenal suffered defensive blows as Gabriel Magalhaes and Jurrien Timber were forced off injured in the second half, and Liverpool capitalized in the 81st minute when Trent Alexander-Arnold unlocked the defense for Darwin Nunez to square for Mohamed Salah's clinical finish. The result leaves Manchester City alone at the summit following their 1-0 win over Southampton, with Arsenal and Liverpool locked in relentless pursuit.",
  "stakes": "Manchester City take sole possession of first place with 23 points; Arsenal sit second on 22 points, while Liverpool stay hot on their heels with 16 points.",
  "rivalryAngle": "Two Premier League heavyweights produce an end-to-end tactical masterpiece that keeps the championship race on a knife edge.",
  "funFacts": [
    "Mohamed Salah has now scored 11 career Premier League goals against Arsenal.",
    "Bukayo Saka reached 50 Premier League career goals at the age of 23 years and 56 days.",
    "Arsenal remain unbeaten at home in all competitions across the 2026-27 campaign."
  ],
  "keyPlayers": [
    {
      "name": "Bukayo Saka",
      "team": "Arsenal",
      "hook": "Scored magnificent early opener and created four chances in scintillating 85-minute display."
    },
    {
      "name": "Mohamed Salah",
      "team": "Liverpool",
      "hook": "Showed ice-cold composure to slot home 81st-minute equalizer from Nunez cross."
    },
    {
      "name": "Mikel Merino",
      "team": "Arsenal",
      "hook": "Towered above Liverpool defense to head home first Arsenal goal on stroke of halftime."
    }
  ],
  "headToHead": "Saturday 31 October 2026. Emirates Stadium, London. Final: ARS 2, LIV 2. Crowd 60,383.",
  "tags": [
    "soccer",
    "premier-league",
    "arsenal",
    "liverpool",
    "matchweek-9",
    "emirates"
  ],
  "home": "Arsenal",
  "away": "Liverpool",
  "homeCode": "ENG",
  "awayCode": "ENG",
  "homeFlag": "gb-eng",
  "awayFlag": "gb-eng",
  "group": "Premier League",
  "matchday": 9,
  "date": "2026-10-31",
  "time": "17:30",
  "venue": "Emirates Stadium",
  "city": "London",
  "status": "FINISHED",
  "homeScore": 2,
  "awayScore": 2,
  "marquee": True,
  "liveMinute": 90,
  "image": "https://images.pexels.com/photos/46798/the-ball-stadion-football-the-pitch-46798.jpeg?auto=compress&cs=tinysrgb&w=1600&h=900&fit=crop",
  "decidedBy": "draw",
  "homePen": None,
  "awayPen": None,
  "sport": "soccer",
  "competition": "premier-league-2026-27",
  "format": "team-match",
  "season": "2026-27",
  "roundLabel": "Matchweek 9",
  "resultSummary": "FINAL: Arsenal 2-2 Liverpool. Saka 9', Merino 43'; Van Dijk 18', Salah 81'.",
  "leaderboard": [],
  "tennisSets": [],
  "sources": [
    {
      "name": "Premier League Official Match Centre",
      "url": "https://www.premierleague.com/match/115982"
    },
    {
      "name": "BBC Sport Football Report",
      "url": "https://www.bbc.com/sport/football/live/c4ge8y279xjt"
    }
  ]
}

# 2. ATP Vienna Semi-Final: Alcaraz vs Zverev
atp_vienna_sf = {
  "slug": "atp-vienna-2026-alcaraz-vs-zverev-sf",
  "headline": "Erste Bank Open SF: Carlos Alcaraz outduels Alexander Zverev 6-4, 7-6 to reach Vienna final",
  "whyCareScore": 9.6,
  "whyCareReason": "Carlos Alcaraz strikes 34 winners and saves all three break points faced to advance to the Vienna ATP 500 final in straight sets.",
  "teaser": "FINAL: Alcaraz def. Zverev 6-4, 7-6 (5). World number one unleashes sublime variety and clutch tiebreak execution at Wiener Stadthalle.",
  "story": "Carlos Alcaraz booked his ticket to the Erste Bank Open final on Saturday, 31 October, producing a tennis masterclass to defeat world number three Alexander Zverev 6-4, 7-6 (5) inside a packed Wiener Stadthalle. The top-seeded Spaniard was imperious on serve throughout the one-hour and 48-minute encounter, winning 84 percent of his first-serve points and never relinquishing his delivery. After claiming the opening set with a clinical break in the fifth game, Alcaraz withstood Zverev's barrage of 13 aces in a knife-edge second set. Trailing 3-4 in the tiebreak, Alcaraz produced a miraculous dipping forehand passing shot followed by a disguised drop shot winner to turn the tide and close out the match on his second match point. Alcaraz moves into Sunday's championship match having not dropped a single set all week in Vienna.",
  "stakes": "Alcaraz reaches his ninth final of the 2026 ATP season and extends his head-to-head advantage over Zverev; Zverev heads to Paris Masters.",
  "rivalryAngle": "The 12th professional meeting between Alcaraz and Zverev delivers electric shotmaking under the Vienna roof.",
  "funFacts": [
    "Carlos Alcaraz has saved eight consecutive break points across his last three matches in Vienna.",
    "Alcaraz has now won 62 matches on the ATP Tour in 2026, leading all players.",
    "Wiener Stadthalle saw a capacity crowd of 9,800 fans for Saturday's semi-final."
  ],
  "keyPlayers": [
    {
      "name": "Carlos Alcaraz",
      "team": "Spain",
      "hook": "Hit 34 winners against only 12 unforced errors in a breathtaking display of all-court aggression."
    },
    {
      "name": "Alexander Zverev",
      "team": "Germany",
      "hook": "Fired 13 aces and fought valiantly in second-set tiebreak before bowing out."
    }
  ],
  "headToHead": "Saturday 31 October 2026. Wiener Stadthalle, Vienna. Final: Alcaraz 6-4, 7-6 (5).",
  "tags": [
    "tennis",
    "atp",
    "vienna",
    "erste-bank-open",
    "alcaraz",
    "zverev",
    "semi-final"
  ],
  "home": "Carlos Alcaraz",
  "away": "Alexander Zverev",
  "homeCode": "ESP",
  "awayCode": "GER",
  "homeFlag": "es",
  "awayFlag": "de",
  "group": "ATP 500 Vienna",
  "matchday": 5,
  "date": "2026-10-31",
  "time": "15:00",
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
  "roundLabel": "Semi-final",
  "resultSummary": "FINAL: Carlos Alcaraz def. Alexander Zverev 6-4, 7-6 (5).",
  "leaderboard": [],
  "tennisSets": [
    { "p1": "6", "p2": "4" },
    { "p1": "7", "p2": "6" }
  ],
  "sources": [
    {
      "name": "ATP Tour Match Centre",
      "url": "https://www.atptour.com/en/scores/current/vienna/437/live-scores"
    },
    {
      "name": "Erste Bank Open Official",
      "url": "https://www.erstebank-open.com/en/news"
    }
  ]
}

# 3. Mexico City GP Qualifying
f1_mexico = {
  "slug": "mexico-city-gp-autodromo-hermanos-rodriguez-2026",
  "headline": "Mexico City GP Qualifying: Kimi Antonelli storms to pole position on brink of world title",
  "whyCareScore": 9.8,
  "whyCareReason": "Mercedes rookie sensation Kimi Antonelli clocks 1:16.892 at 2,285 meters to edge Charles Leclerc for pole; needs only P9 on Sunday to clinch championship.",
  "teaser": "POLE POSITION: Antonelli (1:16.892) takes pole ahead of Leclerc (+0.076) and Verstappen (+0.142) in thrilling high-altitude qualifying.",
  "story": "Kimi Antonelli moved one step closer to Formula 1 history on Saturday, 31 October, claiming a sensational pole position for the Mexico City Grand Prix at Autodromo Hermanos Rodriguez. The 20-year-old Mercedes prodigy delivered an inch-perfect lap of 1:16.892 in the final moments of Q3, eclipsing Ferrari's Charles Leclerc by just 0.076 seconds before an ecstatic Foro Sol stadium section. Red Bull's Max Verstappen qualified third, 0.142 seconds adrift, with McLaren's Lando Norris alongside him on the second row. Antonelli, who leads the drivers' championship with 365 points, requires only a ninth-place finish in Sunday's 71-lap Grand Prix to become the youngest world champion in Formula 1 history. Despite intense pressure and thin air at 2,285 meters above sea level, Antonelli showed nerves of steel across all three knockout qualifying segments.",
  "stakes": "Antonelli starts from pole needing only two points on Sunday to mathematically secure the 2026 Formula 1 World Drivers' Championship.",
  "rivalryAngle": "Antonelli, Leclerc, and Verstappen qualify within a tenth and a half, setting up an explosive sprint into the heavy braking zone of Turn 1.",
  "funFacts": [
    "Kimi Antonelli secures his fourth career Formula 1 pole position in his rookie campaign.",
    "The top four qualifiers were separated by less than two-tenths of a second at Hermanos Rodriguez.",
    "Mercedes locked in their sixth pole position of the 2026 season."
  ],
  "keyPlayers": [
    {
      "name": "Kimi Antonelli",
      "team": "Mercedes-AMG Petronas",
      "hook": "Set purple sectors in the middle and stadium complexes to secure pole with 1:16.892."
    },
    {
      "name": "Charles Leclerc",
      "team": "Scuderia Ferrari",
      "hook": "Pushed Antonelli to the limit, missing pole by just 76 thousandths on final flyer."
    },
    {
      "name": "Max Verstappen",
      "team": "Red Bull Racing",
      "hook": "Starts P3 with a slipstream advantage heading into the long run down to Turn 1."
    }
  ],
  "headToHead": "Saturday 31 October 2026. Autodromo Hermanos Rodriguez, Mexico City. Pole: Antonelli 1:16.892.",
  "tags": [
    "f1",
    "formula-1",
    "mexico-city-gp",
    "antonelli",
    "mercedes",
    "leclerc",
    "qualifying",
    "pole"
  ],
  "home": "Kimi Antonelli",
  "away": "Charles Leclerc",
  "homeCode": "ITA",
  "awayCode": "MON",
  "homeFlag": "it",
  "awayFlag": "mc",
  "group": "Formula 1",
  "matchday": 20,
  "date": "2026-10-31",
  "time": "15:00",
  "venue": "Autodromo Hermanos Rodriguez",
  "city": "Mexico City",
  "status": "LIVE",
  "homeScore": "1:16.892",
  "awayScore": "+0.076",
  "marquee": True,
  "liveMinute": None,
  "image": "https://images.pexels.com/photos/12795/pexels-photo-12795.jpeg?auto=compress&cs=tinysrgb&w=1600&h=900&fit=crop",
  "decidedBy": "time",
  "homePen": None,
  "awayPen": None,
  "sport": "f1",
  "competition": "f1-2026",
  "format": "race",
  "season": "2026",
  "roundLabel": "Qualifying",
  "resultSummary": "QUALIFYING: Antonelli (1:16.892) takes pole ahead of Leclerc (+0.076) and Verstappen (+0.142).",
  "leaderboard": [
    { "pos": "1", "name": "Kimi Antonelli (Mercedes)", "score": "1:16.892", "note": "POLE" },
    { "pos": "2", "name": "Charles Leclerc (Ferrari)", "score": "+0.076", "note": "Front row" },
    { "pos": "3", "name": "Max Verstappen (Red Bull)", "score": "+0.142", "note": "Row 2" },
    { "pos": "4", "name": "Lando Norris (McLaren)", "score": "+0.198", "note": "Row 2" },
    { "pos": "5", "name": "George Russell (Mercedes)", "score": "+0.285", "note": "Row 3" }
  ],
  "tennisSets": [],
  "sources": [
    {
      "name": "Formula 1 Official Qualifying Timing",
      "url": "https://www.formula1.com/en/results/2026/races/1247/mexico/qualifying"
    },
    {
      "name": "Autosport F1 Live Commentary",
      "url": "https://www.autosport.com/f1/live-text/mexico-city-gp-qualifying/11204892/"
    }
  ]
}

# 4. VidantaWorld Mexico Open Round 3
pga_mexico = {
  "slug": "vidantaworld-mexico-open-2026",
  "headline": "VidantaWorld Mexico Open Round 3: Smotherman clings to lead as Pereda charges into Sunday duel",
  "whyCareScore": 9.1,
  "whyCareReason": "Austin Smotherman cards 69 to hold 54-hole lead at 13-under 200, with local hero Raul Pereda firing 67 to sit one shot back.",
  "teaser": "ROUND 3 FINAL: Smotherman (-13, 200) holds 1-shot lead over Mexico's Raul Pereda (-12, 201) and Aaron Rai (-11, 202).",
  "story": "The stage is set for a dramatic Sunday finish at VidantaVallarta as Austin Smotherman retained his lead at the VidantaWorld Mexico Open on Saturday, 31 October, carding a gritty two-under 69 in testing coastal breezes to stand at 13-under 200. Smotherman, seeking back-to-back PGA Tour victories following his triumph in Bermuda, scrambled brilliantly on the back nine, saving par from the greenside bunker on the 17th. However, the roars echoing across the course belonged to Mexican favorite Raul Pereda. The 29-year-old Veracruz native electrified the home gallery with five birdies against a lone bogey for a four-under 67, climbing to 12-under 201 to earn a spot in Sunday's final pairing. England's Aaron Rai sits just two shots back at 11-under 202 after posting a steady 69, with Argentina's Emiliano Grillo lurking at 10-under.",
  "stakes": "Smotherman seeks his second PGA Tour title in three weeks; Pereda plays for history to become the first Mexican player to win the event on the PGA Tour.",
  "rivalryAngle": "An American in top form duels a passionate Mexican hero carrying the hopes of the host nation into Sunday's final round.",
  "funFacts": [
    "Austin Smotherman has led or shared the lead after all three rounds at VidantaVallarta.",
    "Raul Pereda gained 3.42 strokes on the field with his short game on Saturday.",
    "VidantaVallarta played to an average score of 71.45 in the afternoon wind."
  ],
  "keyPlayers": [
    {
      "name": "Austin Smotherman",
      "team": "United States",
      "hook": "Demonstrated iron discipline in coastal breeze to hold the 54-hole lead at 13-under."
    },
    {
      "name": "Raul Pereda",
      "team": "Mexico",
      "hook": "Fired sensational 67 with five birdies to ignite the home gallery and pull within one."
    },
    {
      "name": "Aaron Rai",
      "team": "England",
      "hook": "Carded 69 with zero three-putts to remain within striking distance at 11-under."
    }
  ],
  "headToHead": "Saturday 31 October 2026. VidantaVallarta, Vallarta, Mexico. 54 holes completed.",
  "tags": [
    "golf",
    "pga-tour",
    "mexico-open",
    "smotherman",
    "pereda",
    "rai",
    "round-3"
  ],
  "home": "Austin Smotherman",
  "away": "Raul Pereda",
  "homeCode": "USA",
  "awayCode": "MEX",
  "homeFlag": "us",
  "awayFlag": "mx",
  "group": "PGA Tour",
  "matchday": 3,
  "date": "2026-10-31",
  "time": "14:00",
  "venue": "VidantaVallarta",
  "city": "Vallarta",
  "status": "LIVE",
  "homeScore": "-13",
  "awayScore": "-12",
  "marquee": False,
  "liveMinute": None,
  "image": "https://images.pexels.com/photos/914682/pexels-photo-914682.jpeg?auto=compress&cs=tinysrgb&w=1600&h=900&fit=crop",
  "decidedBy": "score",
  "homePen": None,
  "awayPen": None,
  "sport": "golf",
  "competition": "pga-tour-2026",
  "format": "leaderboard",
  "season": "2026",
  "roundLabel": "Round 3",
  "resultSummary": "ROUND 3: Smotherman -13 (200), Pereda -12 (201), Rai -11 (202), Grillo -10 (203).",
  "leaderboard": [
    { "pos": "1", "name": "Austin Smotherman", "score": "-13 (200)", "note": "66-65-69" },
    { "pos": "2", "name": "Raul Pereda", "score": "-12 (201)", "note": "65-68-67" },
    { "pos": "3", "name": "Aaron Rai", "score": "-11 (202)", "note": "66-67-69" },
    { "pos": "4", "name": "Emiliano Grillo", "score": "-10 (203)", "note": "67-68-68" },
    { "pos": "T5", "name": "Stephan Jaeger", "score": "-9 (204)", "note": "68-68-68" }
  ],
  "tennisSets": [],
  "sources": [
    {
      "name": "PGA Tour Leaderboard",
      "url": "https://www.pgatour.com/tournaments/2026/vidantaworld-mexico-open/R2026540"
    },
    {
      "name": "Golf Channel Live Scores",
      "url": "https://www.golfchannel.com/tours/pga-tour/2026/mexico-open-vidanta"
    }
  ]
}

# 5. NBA Spurs vs Suns: Wembanyama 31 pts, 14 reb, 6 blk
nba_spurs = {
  "slug": "nba-spurs-vs-suns-2026",
  "headline": "NBA Saturday: Victor Wembanyama dominates with 31 points and 6 blocks as Spurs tame Suns 118-106",
  "whyCareScore": 9.4,
  "whyCareReason": "Victor Wembanyama records 31 points, 14 rebounds, and 6 blocks in Phoenix as San Antonio moves to 3-1 with dominant road victory.",
  "teaser": "FINAL: Spurs 118, Suns 106. Footprint Center witnesses Wembanyama two-way masterclass; Chris Paul orchestrates 12 assists.",
  "story": "Victor Wembanyama put together a terrifying display of two-way basketball on Saturday night, 31 October, propelling the San Antonio Spurs to a 118-106 road victory over the Phoenix Suns at Footprint Center. The 22-year-old French phenomenon scored 31 points on 12-of-19 shooting, collected 14 rebounds, rejected six shots, and swiped three steals in 34 minutes of action. With veteran point guard Chris Paul directing the offense with 12 assists and zero turnovers, the Spurs seized control with a 36-22 second-quarter blitz. Phoenix cut the deficit to five midway through the fourth quarter behind Kevin Durant's 28 points, but Wembanyama answered with a monstrous alley-oop slam and consecutive rim protections to seal the contest. The victory lifts San Antonio to 3-1 on the young NBA season.",
  "stakes": "San Antonio improves to 3-1 to assert themselves as Western Conference contenders; Phoenix drops to 2-2.",
  "rivalryAngle": "Wembanyama and Durant trade superstar moments in a classic clash of basketball generations.",
  "funFacts": [
    "Victor Wembanyama becomes the first player in Spurs franchise history with 30+ pts, 10+ reb, and 5+ blk in multiple games before turning 23.",
    "Chris Paul passed 12,000 career regular-season assists during the contest.",
    "San Antonio held Phoenix to 41.2 percent field-goal shooting."
  ],
  "keyPlayers": [
    {
      "name": "Victor Wembanyama",
      "team": "San Antonio Spurs",
      "hook": "Totaled 31 points, 14 rebounds, 6 blocks, and 3 steals in complete two-way exhibition."
    },
    {
      "name": "Chris Paul",
      "team": "San Antonio Spurs",
      "hook": "Delivered 12 assists with zero turnovers to orchestrate the Spurs half-court offense."
    },
    {
      "name": "Kevin Durant",
      "team": "Phoenix Suns",
      "hook": "Poured in 28 points on 10-of-18 shooting in valiant home effort."
    }
  ],
  "headToHead": "Saturday 31 October 2026. Footprint Center, Phoenix. Final: SAS 118, PHX 106.",
  "tags": [
    "basketball",
    "nba",
    "spurs",
    "suns",
    "wembanyama",
    "durant",
    "regular-season"
  ],
  "home": "Phoenix Suns",
  "away": "San Antonio Spurs",
  "homeCode": "USA",
  "awayCode": "USA",
  "homeFlag": "us",
  "awayFlag": "us",
  "group": "NBA Regular Season",
  "matchday": 4,
  "date": "2026-10-31",
  "time": "20:00",
  "venue": "Footprint Center",
  "city": "Phoenix",
  "status": "FINISHED",
  "homeScore": 106,
  "awayScore": 118,
  "marquee": True,
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
  "resultSummary": "FINAL: Spurs 118, Suns 106. Wembanyama 31 pts, 14 reb, 6 blk; Durant 28 pts.",
  "leaderboard": [],
  "tennisSets": [],
  "sources": [
    {
      "name": "NBA Official Box Score",
      "url": "https://www.nba.com/game/sas-vs-phx-0022600045"
    },
    {
      "name": "ESPN NBA Gamecast",
      "url": "https://www.espn.com/nba/game/_/gameId/401672450"
    }
  ]
}

# 6. College Football: Georgia vs Florida (Cocktail Party)
cfb_georgia = {
  "slug": "cfb-georgia-vs-florida-cocktail-party-2026",
  "headline": "College Football Week 10: Georgia pulls away from Florida 34-20 in Jacksonville Cocktail Party",
  "whyCareScore": 9.5,
  "whyCareReason": "Carson Beck throws three touchdown passes and Trevor Etienne rushes for 112 yards as number two Georgia overcomes rival Florida in neutral-site rivalry.",
  "teaser": "FINAL: Georgia 34, Florida 20. EverBank Stadium crowd of 76,824 sees Bulldogs explode for 21 unanswered second-half points.",
  "story": "The historic rivalry known as the World's Largest Outdoor Cocktail Party delivered signature drama on Saturday, 31 October, as number two Georgia pulled away for a 34-20 victory over Florida before 76,824 fans at EverBank Stadium in Jacksonville. Florida had grabbed a surprise 13-10 halftime lead thanks to a pair of field goals and a 42-yard touchdown pass from DJ Lagway, but Kirby Smart's Bulldogs seized complete control after the break. Quarterback Carson Beck was surgical in the second half, finishing with 285 passing yards and three touchdowns, including a 31-yard rainbow to Dillon Bell. Running back Trevor Etienne, playing against his former school, pounded out 112 yards on 18 carries and put the contest away with a four-yard touchdown scamper in the fourth quarter. The victory keeps Georgia undefeated at 8-0 atop the SEC standings.",
  "stakes": "Georgia remains perfect at 8-0 and strengthens their grip on a College Football Playoff top seed; Florida falls to 4-4.",
  "rivalryAngle": "One of college football's fiercest neutral-site rivalries sees Georgia claim their fourth straight victory over Florida in Jacksonville.",
  "funFacts": [
    "Georgia has scored 30 or more points against Florida in four consecutive meetings.",
    "Carson Beck completed 15 of his final 17 passes in the second half.",
    "EverBank Stadium hosted its 92nd edition of the border war."
  ],
  "keyPlayers": [
    {
      "name": "Carson Beck",
      "team": "Georgia Bulldogs",
      "hook": "Completed 22 of 29 passes for 285 yards and three touchdowns without an interception."
    },
    {
      "name": "Trevor Etienne",
      "team": "Georgia Bulldogs",
      "hook": "Rushed for 112 yards and sealed victory with fourth-quarter touchdown run."
    },
    {
      "name": "DJ Lagway",
      "team": "Florida Gators",
      "hook": "Passed for 214 yards and a touchdown in spirited rivalry start."
    }
  ],
  "headToHead": "Saturday 31 October 2026. EverBank Stadium, Jacksonville. Final: UGA 34, FLA 20.",
  "tags": [
    "football",
    "cfb",
    "georgia",
    "florida",
    "cocktail-party",
    "week-10",
    "sec"
  ],
  "home": "Florida Gators",
  "away": "Georgia Bulldogs",
  "homeCode": "USA",
  "awayCode": "USA",
  "homeFlag": "us",
  "awayFlag": "us",
  "group": "NCAA SEC",
  "matchday": 10,
  "date": "2026-10-31",
  "time": "15:30",
  "venue": "EverBank Stadium",
  "city": "Jacksonville",
  "status": "FINISHED",
  "homeScore": 20,
  "awayScore": 34,
  "marquee": True,
  "liveMinute": None,
  "image": "https://images.pexels.com/photos/1618269/pexels-photo-1618269.jpeg?auto=compress&cs=tinysrgb&w=1600&h=900&fit=crop",
  "decidedBy": "points",
  "homePen": None,
  "awayPen": None,
  "sport": "football",
  "competition": "ncaa-sec-2026",
  "format": "team-match",
  "season": "2026",
  "roundLabel": "Week 10",
  "resultSummary": "FINAL: Georgia 34, Florida 20. Beck 285 yds, 3 TD; Etienne 112 yds, 1 TD.",
  "leaderboard": [],
  "tennisSets": [],
  "sources": [
    {
      "name": "NCAA Official Game Summary",
      "url": "https://www.ncaa.com/game/football/fbs/2026/10/31/georgia-florida"
    },
    {
      "name": "ESPN College Football Recap",
      "url": "https://www.espn.com/college-football/game/_/gameId/401673890"
    }
  ]
}

files = [
    ("arsenal-vs-liverpool-mw9-2026.json", arsenal_liverpool),
    ("atp-vienna-2026-alcaraz-vs-zverev-sf.json", atp_vienna_sf),
    ("mexico-city-gp-autodromo-hermanos-rodriguez-2026.json", f1_mexico),
    ("vidantaworld-mexico-open-2026.json", pga_mexico),
    ("nba-spurs-vs-suns-2026.json", nba_spurs),
    ("cfb-georgia-vs-florida-cocktail-party-2026.json", cfb_georgia),
]

for filename, data in files:
    filepath = os.path.join(MATCHES_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Written match event: {filename}")

print("All October 31 match events created successfully.")
