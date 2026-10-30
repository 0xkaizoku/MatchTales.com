#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
MATCHES_DIR = ROOT / "frontend" / "src" / "content" / "matches"

# 1. wnba-finals-2026-game6-valkyries-at-dream.json (Update to FINISHED)
valkyries_game6 = {
  "slug": "wnba-finals-2026-game6-valkyries-at-dream",
  "headline": "WNBA Finals Game 6: Valkyries defeat Dream 76-71 to capture historic maiden championship",
  "whyCareScore": 10.0,
  "whyCareReason": "Golden State Valkyries complete the greatest inaugural season in modern sports history, winning the WNBA title 4-2 in their debut campaign.",
  "teaser": "FINAL: Valkyries 76, Dream 71. Expansion Golden State crowned 2026 WNBA Champions behind Finals MVP Gabby Williams and Thornton clutch three.",
  "story": "The Golden State Valkyries completed the most astonishing fairytale in modern North American professional sports on Thursday night, 29 October, defeating the Atlanta Dream 76-71 in Game 6 of the WNBA Finals at Gateway Center Arena. With the victory, Natalie Nakase's squad clinched the championship 4-2, becoming the first expansion franchise in major American sports since 1950 to capture a title in its inaugural season. Series MVP Gabby Williams spearheaded the triumph with 21 points, six rebounds, and four steals, while veteran forward Kayla Thornton buried a cold-blooded corner three-pointer with 24 seconds remaining to break a 71-71 deadlock. Atlanta star Angel Reese fought relentlessly with 16 points and 15 rebounds, but the Dream could not overcome Golden State's stifling fourth-quarter defense.",
  "stakes": "Golden State Valkyries capture the 2026 WNBA Championship 4-2, completing a historic 32-12 regular season and fairy-tale playoff run.",
  "rivalryAngle": "First-year expansion franchise hoists the championship trophy on the home court of the veteran Atlanta contenders.",
  "funFacts": [
    "Golden State Valkyries become the first expansion team since the 1950 Minneapolis Lakers to win a major American pro title in year one.",
    "Gabby Williams was unanimously named WNBA Finals MVP after averaging 17.0 points, 7.2 rebounds, and 3.5 steals in the series.",
    "Kayla Thornton hit the game-winning three-pointer with 24.1 seconds remaining on the game clock."
  ],
  "keyPlayers": [
    {
      "name": "Gabby Williams",
      "team": "Golden State Valkyries",
      "hook": "Finals MVP poured in 21 points with 4 steals to lead Golden State to the promised land."
    },
    {
      "name": "Kayla Thornton",
      "team": "Golden State Valkyries",
      "hook": "Drained the decisive tie-breaking corner triple with 24 seconds remaining."
    },
    {
      "name": "Angel Reese",
      "team": "Atlanta Dream",
      "hook": "Recorded 16 points and 15 rebounds in heroic effort before late heartbreak."
    }
  ],
  "headToHead": "Thursday 29 October 2026. Gateway Center Arena, College Park. Final: GSV 76, ATL 71 (GSV wins series 4-2).",
  "tags": [
    "basketball",
    "wnba",
    "valkyries",
    "dream",
    "finals",
    "game-6",
    "champions"
  ],
  "home": "Atlanta Dream",
  "away": "Golden State Valkyries",
  "homeCode": "ATL",
  "awayCode": "GSV",
  "homeFlag": "us",
  "awayFlag": "us",
  "group": "WNBA Finals",
  "matchday": 6,
  "date": "2026-10-29",
  "time": "20:00",
  "venue": "Gateway Center Arena",
  "city": "College Park",
  "status": "FINISHED",
  "homeScore": 71,
  "awayScore": 76,
  "marquee": True,
  "liveMinute": None,
  "image": "https://images.pexels.com/photos/1080882/pexels-photo-1080882.jpeg?auto=compress&cs=tinysrgb&w=1600&h=900&fit=crop",
  "decidedBy": "regular",
  "homePen": None,
  "awayPen": None,
  "sport": "basketball",
  "competition": "wnba-2026",
  "format": "team-match",
  "season": "2026",
  "roundLabel": "WNBA Finals Game 6 · Championship Final",
  "resultSummary": "FINAL: Valkyries 76, Dream 71. Golden State wins series 4-2 to become 2026 WNBA Champions.",
  "leaderboard": [],
  "tennisSets": [],
  "sources": [
    {
      "name": "WNBA Finals Game 6 Official Box Score",
      "url": "https://www.wnba.com/game/1042600306/GSV-at-ATL"
    },
    {
      "name": "ESPN Women's Basketball Finals Recap",
      "url": "https://www.espn.com/wnba/recap?gameId=401672306"
    }
  ]
}

# 2. panthers-at-packers-tnf-week8-2026.json (Update to FINISHED)
panthers_packers = {
  "slug": "panthers-at-packers-tnf-week8-2026",
  "headline": "NFL Week 8 TNF: Packers overpower Panthers 27-17 under Lambeau Field lights",
  "whyCareScore": 9.3,
  "whyCareReason": "Jordan Love throws two touchdown passes and Josh Jacobs rushes for 94 yards as Green Bay advances to 6-2 to keep pace with the 6-0 Vikings.",
  "teaser": "FINAL: Packers 27, Panthers 17. Green Bay defense records four sacks to shut down Bryce Young in freezing prime-time battle.",
  "story": "The Green Bay Packers kept the pressure firmly applied in the NFC North race on Thursday night, 29 October, subduing the Carolina Panthers 27-17 before a freezing crowd of 77,844 at Lambeau Field. Quarterback Jordan Love commanded the pocket with poise, completing 20 of 28 passes for 245 yards and two touchdowns, including a crisp 18-yard strike to Jayden Reed in the corner of the end zone. Running back Josh Jacobs powered the ground game with 94 rushing yards on 19 carries and a second-quarter touchdown dive. The Green Bay defense proved impenetrable in key moments, bringing down Carolina quarterback Bryce Young four times, led by Rashan Gary's two sacks. The victory lifts Green Bay to 6-2, hot on the heels of the 6-0 Minnesota Vikings, while Carolina drops to 3-5.",
  "stakes": "Packers improve to 6-2 to stay within striking distance of NFC North leaders Minnesota; Panthers drop to 3-5.",
  "rivalryAngle": "Green Bay extends their home Thursday Night Football dominance with disciplined two-way display.",
  "funFacts": [
    "Jordan Love has now thrown 16 touchdown passes through eight games in 2026.",
    "Green Bay defense held Carolina to 3-of-11 on third-down conversions.",
    "Packers have won five of their last six home games on Thursday Night Football."
  ],
  "keyPlayers": [
    {
      "name": "Jordan Love",
      "team": "Green Bay Packers",
      "hook": "Completed 71.4 percent of passes for 245 yards, 2 touchdowns, and zero turnovers."
    },
    {
      "name": "Josh Jacobs",
      "team": "Green Bay Packers",
      "hook": "Grinded out 94 rushing yards and punched in crucial first-half touchdown."
    },
    {
      "name": "Rashan Gary",
      "team": "Green Bay Packers",
      "hook": "Led ferocious Green Bay pass rush with two sacks and three quarterback hits."
    }
  ],
  "headToHead": "Thursday 29 October 2026. Lambeau Field, Green Bay. Final: GB 27, CAR 17.",
  "tags": [
    "football",
    "nfl",
    "packers",
    "panthers",
    "tnf",
    "week-8"
  ],
  "home": "Green Bay Packers",
  "away": "Carolina Panthers",
  "homeCode": "GB",
  "awayCode": "CAR",
  "homeFlag": "us",
  "awayFlag": "us",
  "group": "NFL",
  "matchday": 8,
  "date": "2026-10-29",
  "time": "20:15",
  "venue": "Lambeau Field",
  "city": "Green Bay",
  "status": "FINISHED",
  "homeScore": 27,
  "awayScore": 17,
  "marquee": True,
  "liveMinute": None,
  "image": "https://images.pexels.com/photos/1618201/pexels-photo-1618201.jpeg?auto=compress&cs=tinysrgb&w=1600&h=900&fit=crop",
  "decidedBy": "regular",
  "homePen": None,
  "awayPen": None,
  "sport": "football",
  "competition": "nfl-2026",
  "format": "team-match",
  "season": "2026",
  "roundLabel": "NFL Week 8 · Thursday Night Football",
  "resultSummary": "FINAL: Packers 27, Panthers 17. Love 245 yds, 2 TD; Jacobs 94 yds, 1 TD. Green Bay improves to 6-2.",
  "leaderboard": [],
  "tennisSets": [],
  "sources": [
    {
      "name": "NFL Week 8 Game Center",
      "url": "https://www.nfl.com/games/panthers-at-packers-2026-reg-8"
    },
    {
      "name": "ESPN NFL TNF Recap",
      "url": "https://www.espn.com/nfl/recap?gameId=401671808"
    }
  ]
}

# 3. arsenal-vs-liverpool-mw9-2026.json (New Marquee Match)
arsenal_liverpool = {
  "slug": "arsenal-vs-liverpool-mw9-2026",
  "headline": "Premier League MW9: Arsenal host Liverpool in heavyweight Emirates showdown",
  "whyCareScore": 9.8,
  "whyCareReason": "Premier League co-leaders Arsenal clash with Arne Slot's resurgent Liverpool in an electric North London title battle.",
  "teaser": "UPCOMING: Emirates Stadium (Saturday, 31 October, 17:30 BST). Arteta's Gunners (21 pts) duel Slot's Reds (15 pts) in blockbuster clash.",
  "story": "The Premier League title race takes center stage on Saturday, 31 October, as co-leaders Arsenal welcome third-place Liverpool to Emirates Stadium for Matchweek 9. Mikel Arteta's Gunners enter level with Manchester City at the summit on 21 points, desperate to respond after their shock midweek Carabao Cup penalty shootout exit to fourth-tier Fleetwood Town. Liverpool arrive in buoyant mood following Wednesday's commanding 2-0 cup dismissal of Chelsea, with Dominik Szoboszlai and Cody Gakpo firing on all cylinders. A victory for Arsenal opens a nine-point chasm over the Merseyside giants, while three points for Arne Slot would firmly ignite Liverpool's championship credentials in front of 60,000 spectators.",
  "stakes": "Arsenal seek to maintain joint leadership of the Premier League; Liverpool can slash the deficit to the top to just three points.",
  "rivalryAngle": "Two of English football's most storied institutions clash in North London with tactical mastery and early-season supremacy at stake.",
  "funFacts": [
    "Arsenal have won seven of their opening eight Premier League fixtures (7-0-1).",
    "Liverpool have conceded just eight league goals this season, boasting the joint-second best defense.",
    "Last season's corresponding fixture at Emirates Stadium produced a pulsating 3-1 Arsenal victory."
  ],
  "keyPlayers": [
    {
      "name": "Bukayo Saka",
      "team": "Arsenal",
      "hook": "Dynamic winger seeks immediate redemption after midweek shootout heartbreak."
    },
    {
      "name": "Mohamed Salah",
      "team": "Liverpool",
      "hook": "Talismanic forward has scored 10 career Premier League goals against the Gunners."
    },
    {
      "name": "Declan Rice",
      "team": "Arsenal",
      "hook": "Midfield powerhouse tasked with disrupting Liverpool's quick transition game."
    }
  ],
  "headToHead": "Saturday 31 October 2026. Emirates Stadium, London. Kickoff 17:30 BST.",
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
  "status": "UPCOMING",
  "homeScore": None,
  "awayScore": None,
  "marquee": True,
  "liveMinute": None,
  "image": "https://images.pexels.com/photos/46798/the-ball-stadion-football-the-pitch-46798.jpeg?auto=compress&cs=tinysrgb&w=1600&h=900&fit=crop",
  "decidedBy": None,
  "homePen": None,
  "awayPen": None,
  "sport": "soccer",
  "competition": "premier-league-2026",
  "format": "team-match",
  "season": "2026",
  "roundLabel": "Premier League Matchweek 9",
  "resultSummary": "UPCOMING: Saturday 17:30 BST at Emirates Stadium. Arsenal (21 pts) host Liverpool (15 pts).",
  "leaderboard": [],
  "tennisSets": [],
  "sources": [
    {
      "name": "Premier League Matchweek 9 Official Preview",
      "url": "https://www.premierleague.com/match/115456"
    },
    {
      "name": "BBC Sport Football Match Preview",
      "url": "https://www.bbc.com/sport/football"
    }
  ]
}

# 4. atp-vienna-2026-alcaraz-vs-draper-qf.json (New Tennis QF)
alcaraz_draper = {
  "slug": "atp-vienna-2026-alcaraz-vs-draper-qf",
  "headline": "ATP Vienna Quarter-finals: Carlos Alcaraz sweeps Jack Draper 6-4, 6-4 into semi-finals",
  "whyCareScore": 9.5,
  "whyCareReason": "Carlos Alcaraz delivers another clinical indoor masterclass, overpowering Jack Draper in straight sets to advance to the Vienna final four.",
  "teaser": "FINAL: Alcaraz def. Draper 6-4, 6-4. World No. 2 fires 29 winners and breaks Draper twice at Wiener Stadthalle to reach Vienna semi-finals.",
  "story": "Carlos Alcaraz surged into the semi-finals of the Erste Bank Open on Friday, 30 October, producing an emphatic 6-4, 6-4 victory over Britain's Jack Draper at Wiener Stadthalle. Building on Thursday's flawless dismissal of Matteo Berrettini, the 23-year-old Spaniard proved unplayable from the baseline, neutralizing Draper's heavy left-handed delivery with razor-sharp returns. Alcaraz secured the vital break in the seventh game of the opening set with an angled forehand passing shot, before taking command of the second set with an early break. Draper fought courageously, saving two match points with aggressive volleying, but Alcaraz served out the contest with an unreturnable body serve to book his spot in Saturday's semi-finals against top seed Alexander Zverev, who earlier defeated Andrey Rublev 7-6 (4), 6-4.",
  "stakes": "Alcaraz reaches the Vienna semi-finals, setting up a tantalizing Saturday showdown against Alexander Zverev.",
  "rivalryAngle": "Alcaraz avenges his previous Queen's Club grass loss to Draper with a commanding indoor hard-court performance.",
  "funFacts": [
    "Alcaraz has won 20 of his last 22 indoor hard-court sets dating back to September.",
    "The Spaniard struck 29 winners against just 11 unforced errors in 84 minutes.",
    "Alexander Zverev defeated Andrey Rublev in straight sets in the preceding quarter-final."
  ],
  "keyPlayers": [
    {
      "name": "Carlos Alcaraz",
      "team": "ATP Tour",
      "hook": "Dominated long rallies and won 81 percent of first-serve points to sweep into semi-finals."
    },
    {
      "name": "Jack Draper",
      "team": "ATP Tour",
      "hook": "British star struck nine aces but could not breach Alcaraz's defensive shield."
    }
  ],
  "headToHead": "Friday 30 October 2026. Wiener Stadthalle, Vienna. Final: Alcaraz def. Draper 6-4, 6-4.",
  "tags": [
    "tennis",
    "atp",
    "vienna",
    "alcaraz",
    "draper",
    "erste-bank-open",
    "quarter-finals"
  ],
  "home": "Carlos Alcaraz",
  "away": "Jack Draper",
  "homeCode": None,
  "awayCode": None,
  "homeFlag": "",
  "awayFlag": "",
  "group": "Erste Bank Open",
  "matchday": 3,
  "date": "2026-10-30",
  "time": "15:30",
  "venue": "Wiener Stadthalle",
  "city": "Vienna",
  "status": "FINISHED",
  "homeScore": 2,
  "awayScore": 0,
  "marquee": True,
  "liveMinute": None,
  "image": "https://images.pexels.com/photos/209841/pexels-photo-209841.jpeg?auto=compress&cs=tinysrgb&w=1600&h=900&fit=crop",
  "decidedBy": "regular",
  "homePen": None,
  "awayPen": None,
  "sport": "tennis",
  "competition": "atp-2026",
  "format": "singles",
  "season": "2026",
  "roundLabel": "ATP Vienna Quarter-finals",
  "resultSummary": "FINAL: Alcaraz def. Draper 6-4, 6-4. Alcaraz 29 winners, Draper 9 aces. Zverev def. Rublev 7-6 (4), 6-4.",
  "leaderboard": [],
  "tennisSets": [
    {"p1": "6", "p2": "4"},
    {"p1": "6", "p2": "4"}
  ],
  "sources": [
    {
      "name": "ATP Tour Erste Bank Open Official",
      "url": "https://www.atptour.com/en/tournaments/vienna/747/overview"
    },
    {
      "name": "Tennis TV Vienna Coverage",
      "url": "https://www.tennistv.com"
    }
  ]
}

# 5. mexico-city-gp-autodromo-hermanos-rodriguez-2026.json (Update with Friday Practice)
mexico_gp = {
  "slug": "mexico-city-gp-autodromo-hermanos-rodriguez-2026",
  "headline": "Mexico City GP Friday Practice: Kimi Antonelli paces FP2 at altitude on championship threshold",
  "whyCareScore": 9.9,
  "whyCareReason": "Championship leader Kimi Antonelli clocks the fastest lap of Friday practice in Mexico City, needing just a P9 finish on Sunday for maiden world title.",
  "teaser": "PRACTICE REPORT: Antonelli (1:17.342) tops FP2 ahead of Leclerc and Verstappen as Mercedes masters 2,285m thin-air cooling challenges.",
  "story": "Championship leader Kimi Antonelli stamped his authority on the 2026 Mexico City Grand Prix weekend on Friday, 30 October, setting the benchmark pace in second practice at Autodromo Hermanos Rodriguez. The 20-year-old Mercedes prodigy, who confirmed on Thursday that he will retain his signature car number 12 in 2027, clocked a lap of 1 minute 17.342 seconds on soft Pirelli tires, edging Ferrari's Charles Leclerc by 0.112 seconds and Red Bull's Max Verstappen by 0.148 seconds. In the rarefied air 2,285 meters above sea level, Mercedes introduced revised radiator bodywork to safeguard thermal reliability. Holding a commanding 123-point lead over teammate George Russell, Antonelli requires only a ninth-place finish on Sunday afternoon to become the youngest World Drivers' Champion in Formula 1 history.",
  "stakes": "A top-nine finish on Sunday guarantees Antonelli the 2026 Drivers' World Championship regardless of other results.",
  "rivalryAngle": "Antonelli outpaces Leclerc and Verstappen in practice while Mercedes teammate Russell finishes fourth (+0.285s).",
  "funFacts": [
    "Antonelli's FP2 benchmark of 1:17.342 was 0.4 seconds faster than the 2025 Friday practice pole time.",
    "Air density at Hermanos Rodriguez is 22 percent lower than at sea level, reducing cooling efficiency.",
    "Antonelli needs just two championship points (ninth place) from Sunday's 71-lap race to seal the crown."
  ],
  "keyPlayers": [
    {
      "name": "Kimi Antonelli",
      "team": "Mercedes",
      "hook": "Paced FP2 with 1:17.342 and stands one clean Sunday drive from the world title."
    },
    {
      "name": "Charles Leclerc",
      "team": "Ferrari",
      "hook": "Finished P2 in FP2 just 0.112s behind Antonelli to establish Ferrari as qualifying threats."
    },
    {
      "name": "Max Verstappen",
      "team": "Red Bull Racing",
      "hook": "Five-time Mexico winner clocked third-fastest time, battling front-wing balance at altitude."
    }
  ],
  "headToHead": "30 October - 1 November 2026. Autodromo Hermanos Rodriguez, Mexico City. 71 Laps.",
  "tags": [
    "f1",
    "formula-1",
    "mexico-gp",
    "antonelli",
    "mercedes",
    "world-champion",
    "verstappen"
  ],
  "home": "Kimi Antonelli",
  "away": "George Russell",
  "homeCode": None,
  "awayCode": None,
  "homeFlag": "",
  "awayFlag": "",
  "group": "Formula 1",
  "matchday": 19,
  "date": "2026-11-01",
  "time": "14:00",
  "venue": "Autódromo Hermanos Rodríguez",
  "city": "Mexico City",
  "status": "LIVE",
  "homeScore": None,
  "awayScore": None,
  "marquee": True,
  "liveMinute": None,
  "image": "https://images.pexels.com/photos/2365457/pexels-photo-2365457.jpeg?auto=compress&cs=tinysrgb&w=1600&h=900&fit=crop",
  "decidedBy": None,
  "homePen": None,
  "awayPen": None,
  "sport": "f1",
  "competition": "f1-2026",
  "format": "race",
  "season": "2026",
  "roundLabel": "Mexico City Grand Prix · Practice Day",
  "resultSummary": "FP2: Antonelli 1:17.342 (P1), Leclerc +0.112 (P2), Verstappen +0.148 (P3), Russell +0.285 (P4).",
  "leaderboard": [],
  "tennisSets": [],
  "sources": [
    {
      "name": "Formula 1 Mexico City GP Official Practice Report",
      "url": "https://www.formula1.com/en/racing/2026/Mexico.html"
    },
    {
      "name": "FIA Official Timing Data",
      "url": "https://www.fia.com"
    }
  ]
}

# 6. vidantaworld-mexico-open-2026.json (Update with Round 2 36-hole cut)
vidantaworld_mexico = {
  "slug": "vidantaworld-mexico-open-2026",
  "headline": "VidantaWorld Mexico Open Round 2: Austin Smotherman surges into 36-hole lead at VidantaVallarta",
  "whyCareScore": 9.1,
  "whyCareReason": "Bermuda winner Austin Smotherman fires a second-round 65 to seize the 36-hole lead at 11-under, two shots clear of home hero Raul Pereda and Aaron Rai.",
  "teaser": "ROUND 2: Smotherman (-11, 131) takes 36-hole lead at VidantaVallarta. Pereda (-9) and Rai (-9) pursue as cut falls at 1-under par.",
  "story": "Austin Smotherman maintained his red-hot autumn form on Friday, 30 October, firing a sensational six-under 65 in the second round of the 2026 VidantaWorld Mexico Open to claim the solo 36-hole lead at 11-under-par 131. Coming off his dramatic playoff triumph at the Bermuda Championship five days ago, the 32-year-old American played flawless golf around the Greg Norman Signature Course at VidantaVallarta, carding six birdies and zero bogeys in strengthening ocean breezes. First-round leader and Mexican favorite Raul Pereda thrilled the home galleries once again, shooting a three-under 68 to share second place at nine-under with England's Aaron Rai (67). Argentina's Emiliano Grillo sits solo fourth at seven-under 135. With the 36-hole cut falling at one-under-par 141, the stage is set for an exhilarating weekend battle for the $1,080,000 winner's check and critical 2027 PGA Tour exemptions.",
  "stakes": "$6,000,000 purse and 500 FedExCup points on the line, alongside critical top-125 card security for the 2027 season.",
  "rivalryAngle": "In-form American Smotherman battles home hero Pereda and European challenger Rai on coastal layout.",
  "funFacts": [
    "Austin Smotherman is a combined 23-under par across his last six PGA Tour tournament rounds.",
    "The 36-hole cut line was set at 1-under-par 141, with 68 players advancing to the weekend.",
    "Raul Pereda has hit 31 of 36 greens in regulation through two rounds at VidantaVallarta."
  ],
  "keyPlayers": [
    {
      "name": "Austin Smotherman",
      "team": "PGA Tour",
      "hook": "Bermuda champion leads at 11-under par after bogey-free 65 in Round 2."
    },
    {
      "name": "Raul Pereda",
      "team": "PGA Tour",
      "hook": "Mexican crowd favorite sits just two strokes back at 9-under after second-round 68."
    },
    {
      "name": "Aaron Rai",
      "team": "PGA Tour",
      "hook": "English precision striker carded 67 to share second place entering moving day."
    }
  ],
  "headToHead": "30 October - 1 November 2026. VidantaVallarta, Vallarta, Mexico. 72 holes stroke play.",
  "tags": [
    "golf",
    "pga-tour",
    "mexico-open",
    "vidanta",
    "smotherman",
    "pereda",
    "rai",
    "fedexcup-fall"
  ],
  "home": "Austin Smotherman",
  "away": "Raul Pereda",
  "homeCode": None,
  "awayCode": None,
  "homeFlag": "",
  "awayFlag": "",
  "group": "PGA Tour",
  "matchday": 2,
  "date": "2026-10-30",
  "time": "08:00",
  "venue": "VidantaVallarta",
  "city": "Vallarta",
  "status": "LIVE",
  "homeScore": None,
  "awayScore": None,
  "marquee": True,
  "liveMinute": None,
  "image": "https://images.pexels.com/photos/1325656/pexels-photo-1325656.jpeg?auto=compress&cs=tinysrgb&w=1600&h=900&fit=crop",
  "decidedBy": None,
  "homePen": None,
  "awayPen": None,
  "sport": "golf",
  "competition": "pga-tour-2026",
  "format": "leaderboard",
  "season": "2026",
  "roundLabel": "Round 2 Completed",
  "resultSummary": "ROUND 2: Smotherman -11 (66-65), Pereda -9 (65-68), Rai -9 (66-67), Grillo -7 (67-68). Cut made at -1.",
  "leaderboard": [
    {"pos": "1", "name": "Austin Smotherman", "score": "-11", "note": "66-65 (131)"},
    {"pos": "T2", "name": "Raul Pereda", "score": "-9", "note": "65-68 (133)"},
    {"pos": "T2", "name": "Aaron Rai", "score": "-9", "note": "66-67 (133)"},
    {"pos": "4", "name": "Emiliano Grillo", "score": "-7", "note": "67-68 (135)"},
    {"pos": "T5", "name": "Matt Wallace", "score": "-6", "note": "67-69 (136)"}
  ],
  "tennisSets": [],
  "sources": [
    {
      "name": "PGA Tour VidantaWorld Mexico Open Leaderboard",
      "url": "https://www.pgatour.com/tournaments/2026/vidantaworld-mexico-open/R2026540"
    },
    {
      "name": "Golf Channel PGA Tour Coverage",
      "url": "https://www.golfchannel.com"
    }
  ]
}

EVENTS = [
    valkyries_game6,
    panthers_packers,
    arsenal_liverpool,
    alcaraz_draper,
    mexico_gp,
    vidantaworld_mexico
]

for ev in EVENTS:
    target = MATCHES_DIR / f"{ev['slug']}.json"
    with open(target, "w", encoding="utf-8") as f:
        json.dump(ev, f, indent=2, ensure_ascii=False)
    print(f"Wrote {target.name}")

print("All October 30 desk events written successfully!")
