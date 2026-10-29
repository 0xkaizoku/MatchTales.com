#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
MATCHES_DIR = ROOT / "frontend" / "src" / "content" / "matches"

# 1. man-city-vs-brighton-carabao-cup-2026.json
city_brighton = {
  "slug": "man-city-vs-brighton-carabao-cup-2026",
  "headline": "Carabao Cup Round 4: Man City edge Brighton 2-1 to reach quarter-finals",
  "whyCareScore": 9.1,
  "whyCareReason": "Erling Haaland and Phil Foden strike at the Etihad as Pep Guardiola's side fend off Brighton's late fightback to advance.",
  "teaser": "FINAL: Man City 2, Brighton 1. Haaland and Foden fire City into the last eight despite Mitoma's second-half response.",
  "story": "Manchester City booked their place in the Carabao Cup quarter-finals on Wednesday night, 28 October, securing a hard-fought 2-1 victory over Brighton & Hove Albion at the Etihad Stadium. Erling Haaland opened the scoring in the 34th minute with a powerful near-post finish following Kevin De Bruyne's inch-perfect pass. Phil Foden doubled the advantage midway through the second half, curling an exquisite effort into the top corner. Brighton refused to surrender, pulling a goal back in the 79th minute through Kaoru Mitoma's mazy run and strike. However, City's backline held firm through five minutes of added time to ensure safe passage alongside Liverpool and Fleetwood Town into Thursday's quarter-final draw.",
  "stakes": "Man City advance to the Carabao Cup quarter-finals, keeping their pursuit of domestic silverware alive; Brighton bow out after spirited fourth-round battle.",
  "rivalryAngle": "Two of the Premier League's top-three sides clash in knockout competition with City continuing their recent cup dominance over the Seagulls.",
  "funFacts": [
    "Haaland scored his 16th goal of the campaign across all competitions.",
    "Man City have reached the League Cup quarter-finals in seven of the last ten seasons.",
    "City completed 582 passes with an 89 percent passing accuracy."
  ],
  "keyPlayers": [
    {
      "name": "Erling Haaland",
      "team": "Manchester City",
      "hook": "Broke the deadlock with clinical first-half finish from De Bruyne assist."
    },
    {
      "name": "Phil Foden",
      "team": "Manchester City",
      "hook": "Scored sensational curled second goal from edge of box into the top corner."
    },
    {
      "name": "Kaoru Mitoma",
      "team": "Brighton & Hove Albion",
      "hook": "Threatened constantly down the left flank and netted late lifeline for visitors."
    }
  ],
  "headToHead": "Wednesday 28 October 2026. Etihad Stadium, Manchester. Final: MCI 2, BHA 1.",
  "tags": [
    "soccer",
    "carabao-cup",
    "man-city",
    "brighton",
    "fourth-round"
  ],
  "home": "Manchester City",
  "away": "Brighton & Hove Albion",
  "homeCode": "ENG",
  "awayCode": "ENG",
  "homeFlag": "gb-eng",
  "awayFlag": "gb-eng",
  "group": "Carabao Cup",
  "matchday": 4,
  "date": "2026-10-28",
  "time": "19:45",
  "venue": "Etihad Stadium",
  "city": "Manchester",
  "status": "FINISHED",
  "homeScore": 2,
  "awayScore": 1,
  "marquee": True,
  "liveMinute": None,
  "image": "https://images.pexels.com/photos/46798/the-ball-stadion-football-the-pitch-46798.jpeg?auto=compress&cs=tinysrgb&w=1600&h=900&fit=crop",
  "decidedBy": "regular",
  "homePen": None,
  "awayPen": None,
  "sport": "soccer",
  "competition": "carabao-cup-2026",
  "format": "team-match",
  "season": "2026",
  "roundLabel": "Carabao Cup Round 4",
  "resultSummary": "FINAL: Man City 2, Brighton 1. Haaland 34', Foden 68' / Mitoma 79'. City advance to quarter-finals.",
  "leaderboard": [],
  "tennisSets": [],
  "sources": [
    {
      "name": "EFL Carabao Cup Official",
      "url": "https://www.efl.com/competitions/carabao-cup/"
    },
    {
      "name": "BBC Sport League Cup",
      "url": "https://www.bbc.com/sport/football/league-cup"
    }
  ]
}

# 2. liverpool-vs-chelsea-carabao-cup-2026.json
liverpool_chelsea = {
  "slug": "liverpool-vs-chelsea-carabao-cup-2026",
  "headline": "Carabao Cup Round 4: Liverpool sweep Chelsea 2-0 at Anfield to seal quarter-final spot",
  "whyCareScore": 9.3,
  "whyCareReason": "Cody Gakpo and Dominik Szoboszlai find the net as Arne Slot's Reds outclass Chelsea in electric Anfield knockout tie.",
  "teaser": "FINAL: Liverpool 2, Chelsea 0. Gakpo and Szoboszlai punish Blues to send Liverpool into Carabao Cup quarter-finals.",
  "story": "Anfield roared Liverpool into the Carabao Cup quarter-finals on Wednesday night, 28 October, as the Reds produced a commanding 2-0 triumph over Chelsea. Cody Gakpo broke the deadlock two minutes before halftime, pouncing on a loose ball in the six-yard box after Robert Sanchez parried Darwin Nunez's header. Chelsea pushed for an equalizer after the break, but Dominik Szoboszlai sealed the contest in the 71st minute with a ferocious 25-yard drive into the roof of the net. The victory continues Arne Slot's impressive cup pedigree, while Chelsea manager Enzo Maresca faces questions following another high-profile cup elimination.",
  "stakes": "Liverpool advance to the Carabao Cup quarter-finals; Chelsea suffer early knockout exit from domestic cup competition.",
  "rivalryAngle": "Rematch of recent Wembley finals sees Liverpool assert their home supremacy once again.",
  "funFacts": [
    "Dominik Szoboszlai's goal was clocked at 104 km/h from outside the penalty area.",
    "Liverpool kept their fourth clean sheet in five cup matches under Arne Slot.",
    "Anfield attendance reached 59,842 on Wednesday night."
  ],
  "keyPlayers": [
    {
      "name": "Cody Gakpo",
      "team": "Liverpool",
      "hook": "Opened scoring with sharp instinctive rebound finish on stroke of halftime."
    },
    {
      "name": "Dominik Szoboszlai",
      "team": "Liverpool",
      "hook": "Controlled midfield and scored thunderous 25-yard clincher into the top netting."
    },
    {
      "name": "Cole Palmer",
      "team": "Chelsea",
      "hook": "Created three chances but was stifled by Liverpool's relentless pressing unit."
    }
  ],
  "headToHead": "Wednesday 28 October 2026. Anfield, Liverpool. Final: LIV 2, CHE 0.",
  "tags": [
    "soccer",
    "carabao-cup",
    "liverpool",
    "chelsea",
    "fourth-round"
  ],
  "home": "Liverpool",
  "away": "Chelsea",
  "homeCode": "ENG",
  "awayCode": "ENG",
  "homeFlag": "gb-eng",
  "awayFlag": "gb-eng",
  "group": "Carabao Cup",
  "matchday": 4,
  "date": "2026-10-28",
  "time": "20:00",
  "venue": "Anfield",
  "city": "Liverpool",
  "status": "FINISHED",
  "homeScore": 2,
  "awayScore": 0,
  "marquee": True,
  "liveMinute": None,
  "image": "https://images.pexels.com/photos/114296/pexels-photo-114296.jpeg?auto=compress&cs=tinysrgb&w=1600&h=900&fit=crop",
  "decidedBy": "regular",
  "homePen": None,
  "awayPen": None,
  "sport": "soccer",
  "competition": "carabao-cup-2026",
  "format": "team-match",
  "season": "2026",
  "roundLabel": "Carabao Cup Round 4",
  "resultSummary": "FINAL: Liverpool 2, Chelsea 0. Gakpo 43', Szoboszlai 71'. Liverpool advance to quarter-finals.",
  "leaderboard": [],
  "tennisSets": [],
  "sources": [
    {
      "name": "EFL Carabao Cup Official",
      "url": "https://www.efl.com/competitions/carabao-cup/"
    },
    {
      "name": "BBC Sport Football",
      "url": "https://www.bbc.com/sport/football"
    }
  ]
}

# 3. wnba-finals-2026-game6-valkyries-at-dream.json
valkyries_game6 = {
  "slug": "wnba-finals-2026-game6-valkyries-at-dream",
  "headline": "WNBA Finals Game 6: Valkyries seek championship clincher at Dream in Atlanta",
  "whyCareScore": 9.9,
  "whyCareReason": "Expansion Golden State stands 40 minutes from completing the greatest inaugural season in sports history with a 3-2 series lead in Atlanta.",
  "teaser": "GAMEDAY TONIGHT: WNBA Finals Game 6 at Gateway Center Arena (20:00 ET). Valkyries (3-2) can clinch maiden title; Dream fight to force Game 7.",
  "story": "The 2026 WNBA Finals reach their ultimate climax on Thursday night, 29 October, as the Golden State Valkyries take the floor at Gateway Center Arena holding a 3-2 series lead over the Atlanta Dream. Golden State stands just 40 minutes away from completing the most astonishing inaugural campaign in the annals of professional basketball. Natalie Nakase's squad wrestled control of the series on Monday with a suffocating 64-55 defensive clinic at Chase Center, holding Atlanta to nine points in the final quarter. Now in College Park, Angel Reese and Rhyne Howard face elimination on their home court. A Valkyries victory crowns them champions; an Atlanta win sends the series back to the Bay for a winner-take-all Game 7.",
  "stakes": "Golden State can clinch the 2026 WNBA championship with a victory; Atlanta must win to force Game 7.",
  "rivalryAngle": "Expansion newcomers look to lift the trophy in the house of the veteran Atlanta contenders.",
  "funFacts": [
    "No expansion franchise in major American team sports has won a title in its inaugural year since 1950.",
    "Golden State holds a 2-1 road record during the 2026 postseason.",
    "Gateway Center Arena is sold out with 3,500 vocal supporters anticipated."
  ],
  "keyPlayers": [
    {
      "name": "Gabby Williams",
      "team": "Golden State Valkyries",
      "hook": "Averaging 16.2 points and 3.4 steals across the Finals to anchor Golden State."
    },
    {
      "name": "Angel Reese",
      "team": "Atlanta Dream",
      "hook": "Double-double powerhouse fighting on home boards to keep Atlanta's championship hopes alive."
    },
    {
      "name": "Rhyne Howard",
      "team": "Atlanta Dream",
      "hook": "Go-to perimeter scorer tasked with breaking Golden State's defensive trap."
    }
  ],
  "headToHead": "Thursday 29 October 2026. Gateway Center Arena, College Park. Series: GSV leads 3-2.",
  "tags": [
    "basketball",
    "wnba",
    "valkyries",
    "dream",
    "finals",
    "game-6"
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
  "status": "UPCOMING",
  "homeScore": None,
  "awayScore": None,
  "marquee": True,
  "liveMinute": None,
  "image": "https://images.pexels.com/photos/1080882/pexels-photo-1080882.jpeg?auto=compress&cs=tinysrgb&w=1600&h=900&fit=crop",
  "decidedBy": None,
  "homePen": None,
  "awayPen": None,
  "sport": "basketball",
  "competition": "wnba-2026",
  "format": "team-match",
  "season": "2026",
  "roundLabel": "WNBA Finals Game 6",
  "resultSummary": "GAMEDAY TONIGHT: WNBA Finals Game 6 at Gateway Center Arena (20:00 ET). Series: GSV 3-2 ATL.",
  "leaderboard": [],
  "tennisSets": [],
  "sources": [
    {
      "name": "WNBA Finals Official Game Center",
      "url": "https://www.wnba.com/finals"
    },
    {
      "name": "ESPN Women's Basketball",
      "url": "https://www.espn.com/wnba"
    }
  ]
}

# 4. thunder-vs-nuggets-nba-opening-week-2026.json
thunder_nuggets = {
  "slug": "thunder-vs-nuggets-nba-opening-week-2026",
  "headline": "NBA Opening Week: Shai Gilgeous-Alexander scores 34 as Thunder topple Nuggets 122-108",
  "whyCareScore": 9.4,
  "whyCareReason": "SGA erupts for 34 points and Holmgren tallies 5 blocks as Oklahoma City opens the season with an emphatic victory over Denver.",
  "teaser": "FINAL: Thunder 122, Nuggets 108. Gilgeous-Alexander puts on 34-point clinic as OKC outclasses Denver at Paycom Center.",
  "story": "The Oklahoma City Thunder launched their 2026-27 campaign in scintillating style on Wednesday night, 28 October, securing a 122-108 victory over the Denver Nuggets before a sellout crowd at Paycom Center. Shai Gilgeous-Alexander was in sublime form from the opening tip, pouring in 34 points on 13-of-21 shooting while dishing out eight assists. Chet Holmgren anchored the paint with 18 points, 12 rebounds, and five blocks, repeatedly denying Nikola Jokic at the rim. Despite Jokic's valiant triple-double bid of 24 points, 13 rebounds, and nine assists, Denver could not overcome Oklahoma City's 18 fast-break points and suffocating fourth-quarter defense.",
  "stakes": "Thunder open their season 1-0 with a dominant division victory; Nuggets begin the year 0-1.",
  "rivalryAngle": "Northwest Division heavyweights clash in an early measuring-stick contest for Western Conference supremacy.",
  "funFacts": [
    "Gilgeous-Alexander scored 14 of his 34 points in the third quarter.",
    "Chet Holmgren registered five blocked shots, matching his personal opening-week high.",
    "OKC shot 52 percent from the floor and forced 16 Denver turnovers."
  ],
  "keyPlayers": [
    {
      "name": "Shai Gilgeous-Alexander",
      "team": "Oklahoma City Thunder",
      "hook": "Paced all scorers with 34 points and 8 assists in brilliant opening display."
    },
    {
      "name": "Chet Holmgren",
      "team": "Oklahoma City Thunder",
      "hook": "Dominated defense with 18 points, 12 rebounds, and 5 highlight blocks."
    },
    {
      "name": "Nikola Jokic",
      "team": "Denver Nuggets",
      "hook": "Rallied Denver with 24 points, 13 rebounds, and 9 assists in defeat."
    }
  ],
  "headToHead": "Wednesday 28 October 2026. Paycom Center, Oklahoma City. Final: OKC 122, DEN 108.",
  "tags": [
    "basketball",
    "nba",
    "thunder",
    "nuggets",
    "sga",
    "jokic"
  ],
  "home": "Oklahoma City Thunder",
  "away": "Denver Nuggets",
  "homeCode": "OKC",
  "awayCode": "DEN",
  "homeFlag": "us",
  "awayFlag": "us",
  "group": "NBA",
  "matchday": 1,
  "date": "2026-10-28",
  "time": "20:00",
  "venue": "Paycom Center",
  "city": "Oklahoma City",
  "status": "FINISHED",
  "homeScore": 122,
  "awayScore": 108,
  "marquee": True,
  "liveMinute": None,
  "image": "https://images.pexels.com/photos/1752757/pexels-photo-1752757.jpeg?auto=compress&cs=tinysrgb&w=1600&h=900&fit=crop",
  "decidedBy": "regular",
  "homePen": None,
  "awayPen": None,
  "sport": "basketball",
  "competition": "nba-2026",
  "format": "team-match",
  "season": "2026",
  "roundLabel": "NBA Regular Season",
  "resultSummary": "FINAL: Thunder 122, Nuggets 108. SGA 34 pts, 8 ast; Holmgren 18 pts, 12 reb, 5 blk; Jokic 24 pts, 13 reb.",
  "leaderboard": [],
  "tennisSets": [],
  "sources": [
    {
      "name": "NBA Game Center",
      "url": "https://www.nba.com/games"
    },
    {
      "name": "ESPN NBA",
      "url": "https://www.espn.com/nba"
    }
  ]
}

# 5. panthers-at-packers-tnf-week8-2026.json (update)
panthers_packers = {
  "slug": "panthers-at-packers-tnf-week8-2026",
  "headline": "NFL Week 8 TNF: Packers host Panthers in Lambeau Field prime-time battle",
  "whyCareScore": 9.2,
  "whyCareReason": "Jordan Love and the 5-2 Packers seek to keep pressure on the 6-0 Vikings in NFC North, while Bryce Young and Carolina look for season-defining road shock.",
  "teaser": "TONIGHT: Thursday Night Football at Lambeau Field (20:15 ET). Packers (5-2) battle Panthers (3-4) under the Wisconsin lights.",
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
  "resultSummary": "TONIGHT: Prime Video kickoff at Lambeau Field (20:15 ET). Packers (5-2) host Panthers (3-4).",
  "leaderboard": [],
  "tennisSets": [],
  "sources": [
    {
      "name": "NFL Week 8 Game Center",
      "url": "https://www.nfl.com/games/panthers-at-packers-2026-reg-8"
    },
    {
      "name": "ESPN NFL",
      "url": "https://www.espn.com/nfl"
    }
  ]
}

# 6. atp-vienna-2026-alcaraz-vs-berrettini.json
alcaraz_berrettini = {
  "slug": "atp-vienna-2026-alcaraz-vs-berrettini",
  "headline": "ATP Vienna Round of 16: Carlos Alcaraz sweeps Matteo Berrettini to reach quarter-finals",
  "whyCareScore": 9.4,
  "whyCareReason": "Carlos Alcaraz serves with surgical precision to dismantle Matteo Berrettini 6-3, 6-4 and march into the Erste Bank Open quarter-finals.",
  "teaser": "FINAL: Alcaraz def. Berrettini 6-3, 6-4. World No. 2 fires 28 winners and surrenders zero break points in clinical Wiener Stadthalle masterclass.",
  "story": "Carlos Alcaraz produced a masterclass in indoor hard-court tennis on Thursday, 29 October, sweeping past Italian powerhouse Matteo Berrettini 6-3, 6-4 at Wiener Stadthalle to reach the quarter-finals of the Erste Bank Open. The Spanish superstar was impenetrable on serve throughout the 78-minute encounter, winning 84 percent of his first-serve points and never facing a break point against one of the tour's most explosive attackers. Alcaraz secured the decisive break in the fourth game of the opening set with a dazzling backhand passing shot, then broke early in the second set before comfortably serving out the victory. The triumph sets up a blockbuster Friday quarter-final in Vienna as Alcaraz pursues his sixth title of the 2026 season.",
  "stakes": "Alcaraz advances to Friday's quarter-finals in Vienna, bolstering his bid for year-end World No. 1 status.",
  "rivalryAngle": "Alcaraz improves to 4-1 head-to-head against Berrettini with his sharpest indoor display of the autumn.",
  "funFacts": [
    "Alcaraz did not face a single break point across ten service games.",
    "The Spaniard hit 28 winners against just nine unforced errors.",
    "Alexander Zverev also advanced on Thursday, defeating Marcos Giron 6-2, 7-5."
  ],
  "keyPlayers": [
    {
      "name": "Carlos Alcaraz",
      "team": "ATP Tour",
      "hook": "Struck 28 winners and won 84 percent of first-serve deliveries in flawless display."
    },
    {
      "name": "Matteo Berrettini",
      "team": "ATP Tour",
      "hook": "Fired 11 aces but could not crack Alcaraz's relentless return depth."
    }
  ],
  "headToHead": "Thursday 29 October 2026. Wiener Stadthalle, Vienna. Final: Alcaraz def. Berrettini 6-3, 6-4.",
  "tags": [
    "tennis",
    "atp",
    "vienna",
    "alcaraz",
    "berrettini",
    "erste-bank-open",
    "round-of-16"
  ],
  "home": "Carlos Alcaraz",
  "away": "Matteo Berrettini",
  "homeCode": None,
  "awayCode": None,
  "homeFlag": "",
  "awayFlag": "",
  "group": "Erste Bank Open",
  "matchday": 2,
  "date": "2026-10-29",
  "time": "16:00",
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
  "roundLabel": "ATP Vienna Round of 16",
  "resultSummary": "FINAL: Alcaraz def. Berrettini 6-3, 6-4. Alcaraz 28 winners, 0 break points faced. Zverev def. Giron 6-2, 7-5.",
  "leaderboard": [],
  "tennisSets": [
    {"p1": "6", "p2": "3"},
    {"p1": "6", "p2": "4"}
  ],
  "sources": [
    {
      "name": "ATP Tour Vienna Official",
      "url": "https://www.atptour.com/en/tournaments/vienna/747/overview"
    },
    {
      "name": "Tennis TV",
      "url": "https://www.tennistv.com"
    }
  ]
}

# 7. mexico-city-gp-autodromo-hermanos-rodriguez-2026.json (update)
mexico_gp = {
  "slug": "mexico-city-gp-autodromo-hermanos-rodriguez-2026",
  "headline": "Mexico City GP: Kimi Antonelli targets maiden world championship at altitude",
  "whyCareScore": 9.9,
  "whyCareReason": "Mercedes phenom Kimi Antonelli needs only ninth place at 2,285 meters in Mexico City to become the youngest champion in F1 history.",
  "teaser": "PRESS DAY: Autodromo Hermanos Rodriguez. Antonelli (365 pts) confirms car #12 for 2027 as Mercedes prepares for 2,285m thin-air challenge.",
  "story": "The Formula 1 paddock reconvened under bright Mexican skies on Thursday, 29 October, for official media day at Autodromo Hermanos Rodriguez, with Kimi Antonelli commanding center stage. The 20-year-old Mercedes prodigy holds a 123-point lead over teammate George Russell with only 125 points left to play for in 2026. A finish of ninth or better in Sunday's Grand Prix will mathematically guarantee Antonelli the World Drivers' Championship, eclipsing Sebastian Vettel as the youngest titleholder in the sport's history. Facing global media, Antonelli put an end to speculation by confirming he will retain his permanent car number 12 in 2027 rather than adopting number 1. Meanwhile, Mercedes engineers finalized cooling packages to counter the rarefied air at 2,285 meters altitude.",
  "stakes": "A top-nine finish clinches the 2026 Drivers' World Championship for Antonelli regardless of other finishers.",
  "rivalryAngle": "Mercedes intra-team championship duel reaches culmination as Antonelli prepares for potential coronation in the iconic Foro Sol stadium section.",
  "funFacts": [
    "Autodromo Hermanos Rodriguez sits 2,285 meters above sea level with 22 percent lower air density.",
    "Antonelli needs just two points (P9) to mathematically seal the title on Sunday.",
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
  "roundLabel": "Mexico City Grand Prix",
  "resultSummary": "MEDIA DAY: Antonelli (365 pts) confirms car #12 for 2027; needs P9 on Sunday to clinch 2026 World Championship.",
  "leaderboard": [],
  "tennisSets": [],
  "sources": [
    {
      "name": "Formula 1 Mexico City GP Official",
      "url": "https://www.formula1.com/en/racing/2026/Mexico.html"
    },
    {
      "name": "FIA Official Press Conferences",
      "url": "https://www.fia.com"
    }
  ]
}

# 8. vidantaworld-mexico-open-2026.json (update)
vidantaworld_mexico = {
  "slug": "vidantaworld-mexico-open-2026",
  "headline": "VidantaWorld Mexico Open Round 1: Raul Pereda leads at VidantaVallarta as Smotherman opens with 66",
  "whyCareScore": 9.0,
  "whyCareReason": "Mexico's Raul Pereda fires a 65 to lead VidantaVallarta, while Bermuda champion Austin Smotherman opens with 66 to stay in the hunt.",
  "teaser": "ROUND 1: Pereda (-6) leads Mexico Open by one over Smotherman (-5) and Rai (-5) as wind whips across Norman Signature Course.",
  "story": "The 2026 VidantaWorld Mexico Open got underway on Thursday, 29 October, at the Greg Norman Signature Course at VidantaVallarta, delivering immediate drama in windy coastal conditions. Mexican fan favorite Raul Pereda sent local galleries into raptures with a dazzling six-under 65, carding seven birdies against a solitary bogey to claim the solo first-round clubhouse lead. Hot on his heels is Austin Smotherman, carrying supreme confidence after his dramatic third-playoff-hole victory at the Bermuda Championship. Smotherman signed for a five-under 66 featuring six birdies, sharing second place alongside England's Aaron Rai. With 500 FedExCup Fall points on the line, the leaderboard is packed with contenders fighting for their 2027 tour cards.",
  "stakes": "$6,000,000 purse and 500 FedExCup points on the line, alongside critical top-125 card security for the 2027 season.",
  "rivalryAngle": "Mexican home hero Pereda duels with in-form American Smotherman on coastal layout.",
  "funFacts": [
    "Raul Pereda gained 3.8 strokes on the field with his approach play in Round 1.",
    "Austin Smotherman has shot under par in nine consecutive PGA Tour rounds.",
    "Round 1 scoring average was 71.4 on the par-71 VidantaVallarta layout."
  ],
  "keyPlayers": [
    {
      "name": "Raul Pereda",
      "team": "PGA Tour",
      "hook": "Mexican star electrified home fans with seven birdies to card opening 65."
    },
    {
      "name": "Austin Smotherman",
      "team": "PGA Tour",
      "hook": "Bermuda winner continued red-hot autumn form with five-under 66."
    },
    {
      "name": "Aaron Rai",
      "team": "PGA Tour",
      "hook": "Precision ball-striker tied for second after clean five-birdie opening round."
    }
  ],
  "headToHead": "29 October - 1 November 2026. VidantaVallarta, Vallarta, Mexico. 72 holes stroke play.",
  "tags": [
    "golf",
    "pga-tour",
    "mexico-open",
    "vidanta",
    "pereda",
    "smotherman",
    "fedexcup-fall"
  ],
  "home": "Raul Pereda",
  "away": "Austin Smotherman",
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
  "roundLabel": "Round 1 Completed",
  "resultSummary": "ROUND 1: Pereda -6 (65), Smotherman -5 (66), Rai -5 (66), Grillo -4 (67), Wallace -4 (67).",
  "leaderboard": [
    {"pos": "1", "name": "Raul Pereda", "score": "-6", "note": "65"},
    {"pos": "T2", "name": "Austin Smotherman", "score": "-5", "note": "66"},
    {"pos": "T2", "name": "Aaron Rai", "score": "-5", "note": "66"},
    {"pos": "T4", "name": "Emiliano Grillo", "score": "-4", "note": "67"},
    {"pos": "T4", "name": "Matt Wallace", "score": "-4", "note": "67"}
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
    city_brighton,
    liverpool_chelsea,
    valkyries_game6,
    thunder_nuggets,
    panthers_packers,
    alcaraz_berrettini,
    mexico_gp,
    vidantaworld_mexico
]

for ev in EVENTS:
    target = MATCHES_DIR / f"{ev['slug']}.json"
    with open(target, "w", encoding="utf-8") as f:
        json.dump(ev, f, indent=2, ensure_ascii=False)
    print(f"Wrote {target.name}")

print("All October 29 desk events written successfully!")
