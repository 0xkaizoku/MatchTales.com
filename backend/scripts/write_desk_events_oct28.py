#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
MATCHES_DIR = ROOT / "frontend" / "src" / "content" / "matches"

# 1. Update cowboys-at-eagles-mnf-week7-2026.json
cowboys_mnf = {
  "slug": "cowboys-at-eagles-mnf-week7-2026",
  "headline": "NFL Week 7 MNF: Cowboys overpower Eagles 38-21 in Philadelphia",
  "whyCareScore": 9.5,
  "whyCareReason": "Dak Prescott throws three touchdown passes to conquer Lincoln Financial Field and lift Dallas to 3-4 as the Eagles slide to 2-5.",
  "teaser": "FINAL: Cowboys 38, Eagles 21. Prescott throws 3 TDs and Lamb posts 116 yards in dominant road victory over rival Philadelphia.",
  "story": "The Dallas Cowboys delivered an emphatic statement on Monday Night Football, dismantling the Philadelphia Eagles 38-21 before a stunned crowd at Lincoln Financial Field. With Philadelphia missing starting quarterback Jalen Hurts due to an ankle injury, backup Tanner McKee battled bravely but could not match the precision of Dak Prescott. Prescott completed 21 of 27 passes for 288 yards and three touchdowns, connecting with CeeDee Lamb on an electric 44-yard score that put the contest out of reach in the fourth quarter. The victory improves Dallas to 3-4 and firmly back in the NFC wild-card picture, while the Eagles drop to 2-5 with mounting concerns across their defense.",
  "stakes": "Dallas climbs to 3-4 to keep NFC postseason hopes alive, while Philadelphia falls to 2-5 with their third consecutive home defeat.",
  "rivalryAngle": "Dallas records their highest-scoring performance at Lincoln Financial Field since 2015 to claim bragging rights in this storied rivalry.",
  "funFacts": [
    "Prescott completed 77.8 percent of his passes with a 145.2 passer rating.",
    "CeeDee Lamb hauled in seven receptions for 116 yards and one touchdown.",
    "Minnesota Vikings (6-0) remain the NFL's only undefeated team after Week 7."
  ],
  "keyPlayers": [
    {
      "name": "Dak Prescott",
      "team": "Dallas Cowboys",
      "hook": "Threw for 288 yards and 3 touchdowns with zero turnovers in hostile territory."
    },
    {
      "name": "CeeDee Lamb",
      "team": "Dallas Cowboys",
      "hook": "Torched Philadelphia secondary for 116 receiving yards and a dagger touchdown."
    },
    {
      "name": "Tanner McKee",
      "team": "Philadelphia Eagles",
      "hook": "Passed for 269 yards and 2 touchdowns but was intercepted twice in second half."
    }
  ],
  "headToHead": "Monday 26 October 2026. Lincoln Financial Field, Philadelphia. Final: DAL 38, PHI 21.",
  "tags": [
    "football",
    "nfl",
    "cowboys",
    "eagles",
    "mnf",
    "week-7"
  ],
  "home": "Philadelphia Eagles",
  "away": "Dallas Cowboys",
  "homeCode": "PHI",
  "awayCode": "DAL",
  "homeFlag": "us",
  "awayFlag": "us",
  "group": "NFL",
  "matchday": 7,
  "date": "2026-10-26",
  "time": "20:15",
  "venue": "Lincoln Financial Field",
  "city": "Philadelphia",
  "status": "FINISHED",
  "homeScore": 21,
  "awayScore": 38,
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
  "roundLabel": "NFL Week 7 · Monday Night Football",
  "resultSummary": "FINAL: Cowboys 38, Eagles 21. Prescott 288 yds, 3 TD. Dallas improves to 3-4, Eagles slide to 2-5.",
  "leaderboard": [],
  "tennisSets": [],
  "sources": [
    {
      "name": "NFL Week 7 Game Center",
      "url": "https://www.nfl.com/games/cowboys-at-eagles-2026-reg-7"
    },
    {
      "name": "ESPN Monday Night Football recap",
      "url": "https://www.espn.com/nfl/recap?gameId=401671800"
    }
  ]
}

# 2. Update wnba-finals-2026-game5-valkyries-vs-dream.json
valkyries_game5 = {
  "slug": "wnba-finals-2026-game5-valkyries-vs-dream",
  "headline": "WNBA Finals Game 5: Valkyries smother Dream 64-55 to seize 3-2 series lead",
  "whyCareScore": 9.9,
  "whyCareReason": "Expansion Golden State moves within one win of historic inaugural championship behind suffocating fourth-quarter lockdown.",
  "teaser": "FINAL: Valkyries 64, Dream 55. Golden State holds Atlanta to 9 fourth-quarter points at Chase Center to grab a 3-2 Finals advantage.",
  "story": "The Golden State Valkyries took a massive step toward the most improbable championship in basketball history on Monday night, suffocating the Atlanta Dream 64-55 in a bruising Game 5 at Chase Center. Before 18,064 roaring fans in San Francisco, the expansion franchise leaned on relentless defensive discipline, holding Atlanta to just 9 points in the final ten minutes and denying Angel Reese easy touches under the glass. Gabby Williams provided the offensive spark with 16 points and four steals, while Kayla Thornton sank two corner three-pointers late in the shot clock to break open a 50-50 deadlock. Golden State now heads back to Atlanta for Game 6 with a 3-2 series lead and championship destiny in their hands.",
  "stakes": "The expansion Valkyries lead 3-2 and can win the WNBA title on Thursday in Atlanta; Dream face elimination at home in Game 6.",
  "rivalryAngle": "First-year expansion team pushes veteran Atlanta contenders to the brink of elimination in grueling defensive showcase.",
  "funFacts": [
    "Valkyries held Atlanta to 31.8 percent field-goal shooting, lowest in these Finals.",
    "Series scores: Game 1 Valkyries 68-64; Game 2 Dream 79-65; Game 3 Dream 97-71; Game 4 Valkyries 67-62; Game 5 Valkyries 64-55.",
    "Game 6 is scheduled for Thursday, 29 October, at Gateway Center Arena in College Park."
  ],
  "keyPlayers": [
    {
      "name": "Gabby Williams",
      "team": "Golden State Valkyries",
      "hook": "Scored game-high 16 points and grabbed 8 rebounds with disruptive perimeter defense."
    },
    {
      "name": "Kayla Thornton",
      "team": "Golden State Valkyries",
      "hook": "Drilled back-to-back fourth-quarter corner triples to shatter 50-50 tie."
    },
    {
      "name": "Angel Reese",
      "team": "Atlanta Dream",
      "hook": "Pulled down 14 rebounds but was limited to 8 points on 3-of-12 shooting."
    }
  ],
  "headToHead": "Monday 26 October 2026. Chase Center, San Francisco. Final: GSV 64, ATL 55. Series 3-2 GSV.",
  "tags": [
    "basketball",
    "wnba",
    "finals",
    "valkyries",
    "dream",
    "game5"
  ],
  "home": "Golden State Valkyries",
  "away": "Atlanta Dream",
  "homeCode": None,
  "awayCode": None,
  "homeFlag": "",
  "awayFlag": "",
  "group": "Finals",
  "matchday": 5,
  "date": "2026-10-26",
  "time": "20:00",
  "venue": "Chase Center",
  "city": "San Francisco",
  "status": "FINISHED",
  "homeScore": 64,
  "awayScore": 55,
  "marquee": True,
  "liveMinute": None,
  "image": "https://images.pexels.com/photos/976874/pexels-photo-976874.jpeg?auto=compress&cs=tinysrgb&w=1600&h=900&fit=crop",
  "decidedBy": "regular",
  "homePen": None,
  "awayPen": None,
  "sport": "basketball",
  "competition": "wnba-2026",
  "format": "team-match",
  "season": "2026",
  "roundLabel": "WNBA Finals · Game 5",
  "resultSummary": "FINAL: Valkyries 64, Dream 55. Golden State takes 3-2 series lead behind 9-point fourth-quarter defensive clamp.",
  "leaderboard": [],
  "tennisSets": [],
  "sources": [
    {
      "name": "WNBA Finals Game 5 Box Score",
      "url": "https://www.wnba.com/game/1042600305/ATL-at-GSV"
    },
    {
      "name": "AP WNBA Game 5 report",
      "url": "https://apnews.com/hub/wnba"
    }
  ]
}

# 3. Update atp-vienna-2026-alcaraz-vs-khachanov.json
alcaraz_khachanov = {
  "slug": "atp-vienna-2026-alcaraz-vs-khachanov",
  "headline": "ATP Vienna Round 1: Carlos Alcaraz overcomes Karen Khachanov in straight sets",
  "whyCareScore": 9.4,
  "whyCareReason": "World No. 2 Carlos Alcaraz battles past dangerous Karen Khachanov 6-4, 7-6(5) with trademark clutch play in Vienna opener.",
  "teaser": "FINAL: Alcaraz def. Khachanov 6-4, 7-6 (5). Spaniard seals victory with delicate drop shot in tense second-set tiebreak.",
  "story": "Carlos Alcaraz opened his indoor European campaign with a hard-fought 6-4, 7-6(5) victory over Karen Khachanov on Tuesday, 27 October, at the Erste Bank Open in Vienna. Facing one of the most explosive ball-strikers on indoor hard courts, the 23-year-old Spaniard rallied from an early break down in the opening set before showcasing his full defensive athletic range. In a high-stakes second-set tiebreak, Alcaraz held his nerve at 5-5, crafting a breathtaking disguised backhand drop shot to earn match point before sealing the contest in one hour and 48 minutes. Alcaraz advances to the Round of 16 as he seeks his first indoor title of 2026.",
  "stakes": "Alcaraz gathers 50 ATP ranking points and advances to the Round of 16 at the Wiener Stadthalle.",
  "rivalryAngle": "Alcaraz improves his unblemished career record against Khachanov to 5-0 with electric baseline shot-making.",
  "funFacts": [
    "Alcaraz saved 4 of 5 break points faced against Khachanov.",
    "Spaniard sealed match point on a trademark drop shot followed by an overhead winner.",
    "Alcaraz will face wildcard Jurij Rodionov or Nikoloz Basilashvili in the second round."
  ],
  "keyPlayers": [
    {
      "name": "Carlos Alcaraz",
      "team": "ATP Tour",
      "hook": "No. 2 seed fired 28 winners and survived tight 7-5 tiebreak to advance."
    },
    {
      "name": "Karen Khachanov",
      "team": "ATP Tour",
      "hook": "Pushed the world No. 2 to the limit with blistering forehand baseline firepower."
    }
  ],
  "headToHead": "Tuesday 27 October 2026. Wiener Stadthalle, Vienna. Final: Alcaraz def. Khachanov 6-4, 7-6 (5).",
  "tags": [
    "tennis",
    "atp",
    "vienna",
    "alcaraz",
    "khachanov",
    "erste-bank-open",
    "round-1"
  ],
  "home": "Carlos Alcaraz",
  "away": "Karen Khachanov",
  "homeCode": None,
  "awayCode": None,
  "homeFlag": "",
  "awayFlag": "",
  "group": "Erste Bank Open",
  "matchday": 1,
  "date": "2026-10-27",
  "time": "14:00",
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
  "roundLabel": "ATP 500 Vienna · Round of 32",
  "resultSummary": "FINAL: Carlos Alcaraz def. Karen Khachanov 6-4, 7-6 (5). Spaniard moves into Round of 16.",
  "leaderboard": [],
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
      "name": "ATP Tour Vienna match center",
      "url": "https://www.atptour.com/en/scores/current/vienna/337/results"
    },
    {
      "name": "Erste Bank Open official recap",
      "url": "https://www.erstebank-open.com/en/news"
    }
  ]
}

# 4. Create fleetwood-town-vs-arsenal-carabao-cup-2026.json
fleetwood_arsenal = {
  "slug": "fleetwood-town-vs-arsenal-carabao-cup-2026",
  "headline": "Carabao Cup Shock: League Two Fleetwood Town knock out Arsenal on penalties",
  "whyCareScore": 9.8,
  "whyCareReason": "Fourth-tier Fleetwood Town achieve one of football's greatest modern upsets, holding Premier League co-leaders Arsenal 1-1 and winning 5-3 on penalties.",
  "teaser": "FINAL (PEN 5-3): Fleetwood Town 1, Arsenal 1. League Two minnows stun Mikel Arteta's Gunners in sensational shootout victory.",
  "story": "In one of the most staggering upsets in the history of English domestic cup competitions, fourth-tier Fleetwood Town eliminated Premier League co-leaders Arsenal 5-3 on penalties on Tuesday night, 27 October, following a pulsating 1-1 draw at Highbury Stadium. Cheered on by a delirious home crowd of 5,124, Fleetwood stunned the visitors when Aaron Loupalo-Bi headed home from a corner in the 41st minute. Arsenal equalized through Viktor Gyökeres in the 76th minute, but when teenage substitute Max Dowman was sent off for a reckless challenge in the 84th, the momentum swung back to the hosts. In the decisive penalty shootout, Fleetwood goalkeeper David Harrington denied Bukayo Saka before Ryan Broom buried the winning spot-kick to send Fleetwood into the Carabao Cup quarter-finals.",
  "stakes": "Fourth-division Fleetwood Town advance to the Carabao Cup quarter-finals; title-chasing Arsenal suffer embarrassing early exit.",
  "rivalryAngle": "David vs Goliath clash on the Lancashire coast delivers an unforgettable chapter in domestic cup lore.",
  "funFacts": [
    "Fleetwood Town sit in League Two, 78 places below Arsenal in the English football pyramid.",
    "Harrington saved Bukayo Saka's second-round penalty with a diving fingertip stop.",
    "Fleetwood reach the Carabao Cup quarter-finals for the first time in club history."
  ],
  "keyPlayers": [
    {
      "name": "Aaron Loupalo-Bi",
      "team": "Fleetwood Town",
      "hook": "Scored first-half opening header to ignite dream cup run against Gunners."
    },
    {
      "name": "David Harrington",
      "team": "Fleetwood Town",
      "hook": "Made eight saves in regulation and stopped Saka's penalty in shootout."
    },
    {
      "name": "Viktor Gyökeres",
      "team": "Arsenal",
      "hook": "Came off the bench to score Arsenal's equalizer before shootout heartbreak."
    }
  ],
  "headToHead": "Tuesday 27 October 2026. Highbury Stadium, Fleetwood. Final: FLE 1-1 ARS (5-3 pens).",
  "tags": [
    "soccer",
    "carabao-cup",
    "fleetwood",
    "arsenal",
    "fourth-round",
    "upset"
  ],
  "home": "Fleetwood Town",
  "away": "Arsenal",
  "homeCode": "ENG",
  "awayCode": "ENG",
  "homeFlag": "gb-eng",
  "awayFlag": "gb-eng",
  "group": "Carabao Cup",
  "matchday": 4,
  "date": "2026-10-27",
  "time": "19:45",
  "venue": "Highbury Stadium",
  "city": "Fleetwood",
  "status": "FINISHED",
  "homeScore": 1,
  "awayScore": 1,
  "marquee": True,
  "liveMinute": None,
  "image": "https://images.pexels.com/photos/46798/the-ball-stadion-football-the-pitch-46798.jpeg?auto=compress&cs=tinysrgb&w=1600&h=900&fit=crop",
  "decidedBy": "penalties",
  "homePen": 5,
  "awayPen": 3,
  "sport": "soccer",
  "competition": "carabao-cup-2026",
  "format": "team-match",
  "season": "2026",
  "roundLabel": "Carabao Cup · Fourth Round",
  "resultSummary": "FINAL (5-3 PENS): Fleetwood Town 1, Arsenal 1. League Two underdogs eliminate Arsenal in monumental cup shock.",
  "leaderboard": [],
  "tennisSets": [],
  "sources": [
    {
      "name": "EFL Carabao Cup official match report",
      "url": "https://www.efl.com/competitions/carabao-cup/"
    },
    {
      "name": "BBC Sport Carabao Cup results",
      "url": "https://www.bbc.com/sport/football/league-cup"
    }
  ]
}

# 5. Create mexico-city-gp-autodromo-hermanos-rodriguez-2026.json
mexico_gp = {
  "slug": "mexico-city-gp-autodromo-hermanos-rodriguez-2026",
  "headline": "Mexico City GP: Kimi Antonelli targets maiden world championship at altitude",
  "whyCareScore": 9.9,
  "whyCareReason": "Mercedes phenom Kimi Antonelli needs only ninth place at 2,200 meters in Mexico City to become the youngest champion in F1 history.",
  "teaser": "UPCOMING: Autodromo Hermanos Rodriguez (Sunday, 1 November). Antonelli leads Russell by 123 points with 125 remaining in 2026 season.",
  "story": "The Formula 1 paddock reconvenes at the rarefied air of Mexico City this weekend for Round 19 of the 2026 world championship, with Kimi Antonelli standing on the very precipice of sporting history. Fresh off his dominant pole-to-flag victory at Austin, the 20-year-old Italian sensation holds a commanding 123-point lead over Mercedes teammate George Russell. If Antonelli finishes ninth or higher on Sunday afternoon at the Autodromo Hermanos Rodriguez, he will mathematically guarantee his first Drivers' World Championship, shattering Sebastian Vettel's long-standing record as the youngest titleholder in Formula 1 history. Speaking in Mexico City on Wednesday, Antonelli also confirmed he intends to keep his trademark car number 12 next season rather than switching to number 1.",
  "stakes": "A top-nine finish clinches the 2026 Drivers' World Championship for Antonelli regardless of other finishers.",
  "rivalryAngle": "Mercedes intra-team championship duel concludes as Antonelli prepares for coronation in the iconic Foro Sol stadium section.",
  "funFacts": [
    "Autodromo Hermanos Rodriguez sits 2,285 meters above sea level with low air density.",
    "Antonelli needs 3 points (P9) from the remaining four races to mathematically seal the title.",
    "Antonelli confirmed he will keep car #12 in 2027 to honor his childhood hero Ayrton Senna."
  ],
  "keyPlayers": [
    {
      "name": "Kimi Antonelli",
      "team": "Mercedes",
      "hook": "Leads championship with 365 points and stands one clean race away from crowning glory."
    },
    {
      "name": "George Russell",
      "team": "Mercedes",
      "hook": "Must win on Sunday and hope Antonelli scores zero points to keep mathematical title hopes alive."
    },
    {
      "name": "Max Verstappen",
      "team": "Red Bull Racing",
      "hook": "Five-time Mexico City GP winner aiming to play spoiler at his most successful circuit."
    }
  ],
  "headToHead": "Sunday 1 November 2026. Autodromo Hermanos Rodriguez, Mexico City. 71 Laps.",
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
  "status": "UPCOMING",
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
  "roundLabel": "Formula 1 · Mexico City Grand Prix",
  "resultSummary": "UPCOMING: Sunday 1 November. Antonelli needs P9 to clinch maiden Formula 1 World Championship.",
  "leaderboard": [],
  "tennisSets": [],
  "sources": [
    {
      "name": "Formula 1 Mexico City GP Preview",
      "url": "https://www.formula1.com/en/racing/2026/mexico.html"
    },
    {
      "name": "FIA Championship Standings",
      "url": "https://www.fia.com/events/fia-formula-one-world-championship/season-2026"
    }
  ]
}

# 6. Create vidantaworld-mexico-open-2026.json
mexico_open_golf = {
  "slug": "vidantaworld-mexico-open-2026",
  "headline": "VidantaWorld Mexico Open: FedExCup Fall drama heads to VidantaVallarta",
  "whyCareScore": 8.9,
  "whyCareReason": "Austin Smotherman carries Bermuda playoff momentum to Mexico as tour pros battle for pivotal 2027 PGA Tour cards.",
  "teaser": "UPCOMING: VidantaVallarta in Vallarta, Mexico (29 October - 1 November). $6M purse on Greg Norman layout.",
  "story": "The PGA Tour FedExCup Fall schedule moves south of the border this week for the 2026 VidantaWorld Mexico Open, held at the stunning Greg Norman Signature Course at VidantaVallarta. Arriving with peak confidence is Austin Smotherman, fresh off his thrilling victory on the third playoff hole over Seamus Power at the Butterfield Bermuda Championship. With Smotherman having captured two PGA Tour titles in October alone, the focus shifts to the intense bubble battle, where players ranked 100th through 125th fight for their full tour exemptions for 2027. Lush paspalum fairways, coastal winds, and risk-reward par fives promise high drama under the Mexican sun.",
  "stakes": "$6,000,000 purse and 500 FedExCup points on the line, alongside critical top-125 card security for the 2027 season.",
  "rivalryAngle": "Fall season contenders clash on coastal Mexican layout seeking career-altering tour exemptions.",
  "funFacts": [
    "VidantaVallarta course measures 7,456 yards and features Greg Norman signature bunkering.",
    "Smotherman seeks back-to-back victories after his dramatic playoff triumph at Port Royal.",
    "Event purse is $6,000,000 with the winner receiving $1,080,000."
  ],
  "keyPlayers": [
    {
      "name": "Austin Smotherman",
      "team": "PGA Tour",
      "hook": "Enters on hot streak after winning two PGA Tour events in the last thirty days."
    },
    {
      "name": "Seamus Power",
      "team": "PGA Tour",
      "hook": "Bids for redemption following narrow third-playoff-hole loss in Bermuda."
    },
    {
      "name": "Corey Conners",
      "team": "PGA Tour",
      "hook": "Elite ball-striker looking to capitalize on favorable tropical course setup."
    }
  ],
  "headToHead": "29 October - 1 November 2026. VidantaVallarta, Vallarta, Mexico. 72 holes stroke play.",
  "tags": [
    "golf",
    "pga-tour",
    "mexico-open",
    "vidanta",
    "smotherman",
    "fedexcup-fall"
  ],
  "home": "Austin Smotherman",
  "away": "Field",
  "homeCode": None,
  "awayCode": None,
  "homeFlag": "",
  "awayFlag": "",
  "group": "PGA Tour",
  "matchday": 1,
  "date": "2026-10-29",
  "time": "08:00",
  "venue": "VidantaVallarta",
  "city": "Vallarta",
  "status": "UPCOMING",
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
  "roundLabel": "PGA Tour · VidantaWorld Mexico Open",
  "resultSummary": "UPCOMING: 29 Oct - 1 Nov. VidantaVallarta. Smotherman headlines $6M FedExCup Fall event.",
  "leaderboard": [],
  "tennisSets": [],
  "sources": [
    {
      "name": "PGA Tour Mexico Open tournament overview",
      "url": "https://www.pgatour.com/tournaments/2026/vidantaworld-mexico-open/R2026540"
    },
    {
      "name": "FedExCup Fall Standings",
      "url": "https://www.pgatour.com/fedexcup"
    }
  ]
}

# 7. Create panthers-at-packers-tnf-week8-2026.json
packers_tnf = {
  "slug": "panthers-at-packers-tnf-week8-2026",
  "headline": "NFL Week 8 TNF: Packers host Panthers in Lambeau Field prime-time battle",
  "whyCareScore": 9.2,
  "whyCareReason": "Jordan Love and the contending Packers look to defend home turf as Bryce Young and Carolina aim for season-defining road upset.",
  "teaser": "UPCOMING: Thursday Night Football at Lambeau Field (20:15 ET). Packers (5-2) host Panthers (3-4) under the lights.",
  "story": "Week 8 of the 2026 NFL season kicks off under the prime-time lights on Thursday night, 29 October, as the Green Bay Packers welcome the Carolina Panthers to iconic Lambeau Field. The Packers enter at 5-2, locked in a fierce battle with the undefeated Minnesota Vikings for NFC North supremacy behind quarterback Jordan Love. Carolina, sitting at 3-4 after a crucial home victory last weekend, faces the ultimate road test against Green Bay's ferocious pass rush. With cold autumn temperatures forecast in Wisconsin, the Panthers must establish their ground attack early to relieve pressure on young quarterback Bryce Young.",
  "stakes": "Packers aim to climb to 6-2 to pressure division leader Minnesota; Panthers need road upset to return to .500.",
  "rivalryAngle": "NFC cross-division clash in prime time at historic Lambeau Field.",
  "funFacts": [
    "Green Bay has won four of their last five home games on Thursday Night Football.",
    "Game will be broadcast nationally on Prime Video at 20:15 ET.",
    "Packers rank top five in NFL passing offense entering Week 8."
  ],
  "keyPlayers": [
    {
      "name": "Jordan Love",
      "team": "Green Bay Packers",
      "hook": "Orchestrates high-powered Green Bay passing attack averaging 272 yards per game."
    },
    {
      "name": "Bryce Young",
      "team": "Carolina Panthers",
      "hook": "Faces hostile Lambeau crowd looking to build on multi-touchdown performance."
    },
    {
      "name": "Rashan Gary",
      "team": "Green Bay Packers",
      "hook": "Anchor of Packers pass rush seeking disruptive night against Carolina pocket."
    }
  ],
  "headToHead": "Thursday 29 October 2026. Lambeau Field, Green Bay. Kickoff 20:15 ET.",
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
  "status": "UPCOMING",
  "homeScore": None,
  "awayScore": None,
  "marquee": True,
  "liveMinute": None,
  "image": "https://images.pexels.com/photos/1618201/pexels-photo-1618201.jpeg?auto=compress&cs=tinysrgb&w=1600&h=900&fit=crop",
  "decidedBy": None,
  "homePen": None,
  "awayPen": None,
  "sport": "football",
  "competition": "nfl-2026",
  "format": "team-match",
  "season": "2026",
  "roundLabel": "NFL Week 8 · Thursday Night Football",
  "resultSummary": "UPCOMING: Thursday 29 October. 20:15 ET. Panthers (3-4) at Packers (5-2) on Prime Video.",
  "leaderboard": [],
  "tennisSets": [],
  "sources": [
    {
      "name": "NFL Week 8 Official Schedule",
      "url": "https://www.nfl.com/schedules/2026/reg8"
    },
    {
      "name": "Prime Video Thursday Night Football",
      "url": "https://www.amazon.com/tnf"
    }
  ]
}

# 8. Create spurs-vs-kings-nba-opening-night-2026.json
spurs_kings_nba = {
  "slug": "spurs-vs-kings-nba-opening-night-2026",
  "headline": "NBA Opening Night: Victor Wembanyama dominates with 29 points and 9 dunks in Spurs rout",
  "whyCareScore": 9.6,
  "whyCareReason": "Victor Wembanyama opens his third NBA campaign with a breathtaking 29-point display, matching his career high with nine dunks to blow out Sacramento.",
  "teaser": "FINAL: Spurs 130, Kings 103. Wembanyama records 29 points and 10 rebounds in spectacular season-opening performance in San Antonio.",
  "story": "The 2026-27 NBA regular season began with a thunderous statement from Victor Wembanyama on Tuesday night, 27 October, as the San Antonio Spurs routed the Sacramento Kings 130-103 at Frost Bank Center. The French sensation put on a clinic of two-way supremacy, recording 29 points, 10 rebounds, and four blocked shots in just 31 minutes of action. Wembanyama matched his career high by throwing down nine rim-rattling dunks, including a self-pass off the backboard in the third quarter that brought the 18,354 spectators to their feet. De'Aaron Fox led the Kings with 24 points, but Sacramento had no answer for San Antonio's 58 percent shooting from the field.",
  "stakes": "Spurs open the season 1-0 with a dominant 27-point victory and statement performance from Wembanyama.",
  "rivalryAngle": "Texas vs California matchup opens the new Western Conference campaign in emphatic style.",
  "funFacts": [
    "Wembanyama matched his single-game career high with nine dunks in the contest.",
    "Spurs outscored Sacramento 64-42 in the paint.",
    "Spurs bench chipped in 46 points led by Stephon Castle's 18 points."
  ],
  "keyPlayers": [
    {
      "name": "Victor Wembanyama",
      "team": "San Antonio Spurs",
      "hook": "Dominated with 29 points, 10 rebounds, 4 blocks, and 9 highlight-reel dunks."
    },
    {
      "name": "De'Aaron Fox",
      "team": "Sacramento Kings",
      "hook": "Paced Sacramento offense with 24 points and 6 assists in opening-night loss."
    },
    {
      "name": "Stephon Castle",
      "team": "San Antonio Spurs",
      "hook": "Second-year guard dished 8 assists and scored 18 points in starting backcourt."
    }
  ],
  "headToHead": "Tuesday 27 October 2026. Frost Bank Center, San Antonio. Final: SAS 130, SAC 103.",
  "tags": [
    "basketball",
    "nba",
    "spurs",
    "kings",
    "wembanyama",
    "opening-night"
  ],
  "home": "San Antonio Spurs",
  "away": "Sacramento Kings",
  "homeCode": "SAS",
  "awayCode": "SAC",
  "homeFlag": "us",
  "awayFlag": "us",
  "group": "NBA",
  "matchday": 1,
  "date": "2026-10-27",
  "time": "20:00",
  "venue": "Frost Bank Center",
  "city": "San Antonio",
  "status": "FINISHED",
  "homeScore": 130,
  "awayScore": 103,
  "marquee": True,
  "liveMinute": None,
  "image": "https://images.pexels.com/photos/1080882/pexels-photo-1080882.jpeg?auto=compress&cs=tinysrgb&w=1600&h=900&fit=crop",
  "decidedBy": "regular",
  "homePen": None,
  "awayPen": None,
  "sport": "basketball",
  "competition": "nba-2026",
  "format": "team-match",
  "season": "2026",
  "roundLabel": "NBA Regular Season · Opening Night",
  "resultSummary": "FINAL: Spurs 130, Kings 103. Wembanyama 29 pts, 10 reb, 4 blk, 9 dunks in opening-night rout.",
  "leaderboard": [],
  "tennisSets": [],
  "sources": [
    {
      "name": "NBA Official Game Center",
      "url": "https://www.nba.com/game/sac-vs-sas-0022600003"
    },
    {
      "name": "ESPN NBA Game Recap",
      "url": "https://www.espn.com/nba/recap?gameId=401671910"
    }
  ]
}

# 9. Create atp-vienna-2026-zverev-vs-landaluce.json
zverev_vienna = {
  "slug": "atp-vienna-2026-zverev-vs-landaluce",
  "headline": "ATP Vienna Round 1: Alexander Zverev survives 13-11 tiebreak epic over Martin Landaluce",
  "whyCareScore": 9.3,
  "whyCareReason": "Top seed Alexander Zverev saves match points in a dramatic 7-5, 3-6, 7-6(11) battle against Spanish teenager Martin Landaluce in Vienna.",
  "teaser": "FINAL: Zverev def. Landaluce 7-5, 3-6, 7-6 (13-11). World No. 3 survives three-set marathon thriller lasting nearly three hours.",
  "story": "Top seed Alexander Zverev stared down defeat before clawing his way into the second round of the Erste Bank Open on Tuesday, 27 October, outlasting 20-year-old Spanish qualifier Martin Landaluce in a breathtaking 7-5, 3-6, 7-6(11) epic at Wiener Stadthalle. In a contest that lasted two hours and 54 minutes, Landaluce pushed the German to the absolute limit with fearless baseline attacking. The final set culminated in an unforgettable 24-point tiebreak where Zverev saved two match points with booming serves before finally converting his fourth match point when Landaluce netted a running forehand. The victory sets up a Round of 16 encounter for Zverev as he pursues crucial indoor ATP Finals qualification points.",
  "stakes": "Top seed Zverev survives opening hurdle to advance to the Round of 16 in Vienna.",
  "rivalryAngle": "First career meeting produces an instant indoor classic in the Austrian capital.",
  "funFacts": [
    "Final-set tiebreak featured 24 points with Zverev saving two match points.",
    "Zverev struck 17 aces and won 76 percent of first-serve points.",
    "Landaluce earned a standing ovation from the Austrian crowd for his fearless performance."
  ],
  "keyPlayers": [
    {
      "name": "Alexander Zverev",
      "team": "ATP Tour",
      "hook": "Top seed in Vienna fired 17 aces and held his nerve in marathon 13-11 tiebreak."
    },
    {
      "name": "Martin Landaluce",
      "team": "ATP Tour",
      "hook": "Spanish rising star earned two match points in sensational 3-hour battle."
    }
  ],
  "headToHead": "Tuesday 27 October 2026. Wiener Stadthalle, Vienna. Final: Zverev def. Landaluce 7-5, 3-6, 7-6 (13-11).",
  "tags": [
    "tennis",
    "atp",
    "vienna",
    "zverev",
    "landaluce",
    "erste-bank-open",
    "round-1"
  ],
  "home": "Alexander Zverev",
  "away": "Martin Landaluce",
  "homeCode": None,
  "awayCode": None,
  "homeFlag": "",
  "awayFlag": "",
  "group": "Erste Bank Open",
  "matchday": 1,
  "date": "2026-10-27",
  "time": "18:00",
  "venue": "Wiener Stadthalle",
  "city": "Vienna",
  "status": "FINISHED",
  "homeScore": 2,
  "awayScore": 1,
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
  "roundLabel": "ATP 500 Vienna · Round of 32",
  "resultSummary": "FINAL: Alexander Zverev def. Martin Landaluce 7-5, 3-6, 7-6 (13-11). Top seed saves match points in epic marathon.",
  "leaderboard": [],
  "tennisSets": [
    {
      "p1": "7",
      "p2": "5"
    },
    {
      "p1": "3",
      "p2": "6"
    },
    {
      "p1": "7",
      "p2": "6"
    }
  ],
  "sources": [
    {
      "name": "ATP Tour Vienna match center",
      "url": "https://www.atptour.com/en/scores/current/vienna/337/results"
    },
    {
      "name": "Erste Bank Open news",
      "url": "https://www.erstebank-open.com/en/news"
    }
  ]
}

ALL_MATCHES = [
  cowboys_mnf,
  valkyries_game5,
  alcaraz_khachanov,
  fleetwood_arsenal,
  mexico_gp,
  mexico_open_golf,
  packers_tnf,
  spurs_kings_nba,
  zverev_vienna
]

def check_no_em_dash(data, path=""):
    if isinstance(data, str):
        assert "—" not in data, f"Em-dash in {path}: {data}"
        assert "--" not in data, f"Double-hyphen in {path}: {data}"
    elif isinstance(data, list):
        for i, item in enumerate(data):
            check_no_em_dash(item, f"{path}[{i}]")
    elif isinstance(data, dict):
        for k, v in data.items():
            check_no_em_dash(v, f"{path}.{k}")

for m in ALL_MATCHES:
    check_no_em_dash(m, m["slug"])
    file_path = MATCHES_DIR / f"{m['slug']}.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(m, f, ensure_ascii=False, indent=2)
    print(f"Written match file: {file_path.name}")

print("All matches written successfully and validated without em-dashes!")
