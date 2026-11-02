#!/usr/bin/env python3
"""
Write match events for 2 November 2026 daily update.
"""
import json
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
MATCHES_DIR = os.path.join(ROOT, "frontend/src/content/matches")

# 1. NFL Week 8 MNF: Steelers beat Giants 26-18
nfl_steelers = {
  "slug": "giants-at-steelers-mnf-week8-2026",
  "headline": "NFL Week 8 MNF: Steelers overpower Giants 26-18 behind Calvin Austin's two touchdowns and ferocious pass rush",
  "whyCareScore": 9.6,
  "whyCareReason": "Calvin Austin III scores on a 73-yard punt return and a 29-yard reception, while T.J. Watt and Alex Highsmith terrorize Daniel Jones to send Pittsburgh to 6-2 atop the AFC North.",
  "teaser": "FINAL: Steelers 26, Giants 18. Acrisure Stadium rocks on Monday Night Football as Pittsburgh defense forces two crucial fourth-quarter turnovers.",
  "story": "The Pittsburgh Steelers solidified their hold on first place in the AFC North with an authoritative 26-18 victory over the New York Giants on Monday Night Football, 2 November, before a sellout crowd of 67,430 at Acrisure Stadium. Wide receiver Calvin Austin III delivered the game-changing moments in the third quarter, first fielding a punt at his own 27-yard line and weaving through traffic for a sensational 73-yard return touchdown. Moments later, veteran quarterback Russell Wilson connected with Austin on a perfectly weighted 29-yard touchdown strike. Wilson completed 20 of 28 passes for 278 yards with zero turnovers, orchestrating four Chris Boswell field goals. On defense, superstar edge rusher T.J. Watt dominated with two sacks, a forced fumble, and a fumble recovery, while rookie cornerback Beanie Bishop Jr. intercepted Daniel Jones with 34 seconds remaining to extinguish New York's final drive.",
  "stakes": "The Steelers improve to 6-2 to take sole possession of first place in the AFC North; the Giants drop to 2-6.",
  "rivalryAngle": "Historic non-conference rivalry features a defensive masterclass as Pittsburgh's front four overwhelms New York's offensive line under the prime-time lights.",
  "funFacts": [
    "Calvin Austin III is the first Steelers player with a punt return touchdown and a receiving touchdown in the same game since 2017.",
    "Russell Wilson is 2-0 as Steelers starting quarterback, generating over 400 total yards of offense in back-to-back games.",
    "T.J. Watt recorded his 100th career tackle for loss during Monday's victory."
  ],
  "keyPlayers": [
    {
      "name": "Calvin Austin III",
      "team": "Pittsburgh Steelers",
      "hook": "Scored two electrifying touchdowns in the third quarter on a 73-yard punt return and 29-yard reception."
    },
    {
      "name": "Russell Wilson",
      "team": "Pittsburgh Steelers",
      "hook": "Completed 71.4 percent of his passes for 278 yards, one touchdown, and zero turnovers."
    },
    {
      "name": "T.J. Watt",
      "team": "Pittsburgh Steelers",
      "hook": "Totaled 2 sacks, a forced fumble, and a fumble recovery in a dominant defensive showcase."
    }
  ],
  "headToHead": "Monday 2 November 2026. Acrisure Stadium, Pittsburgh. Final: PIT 26, NYG 18.",
  "tags": [
    "football",
    "nfl",
    "steelers",
    "giants",
    "mnf",
    "monday-night-football",
    "russell-wilson",
    "tj-watt"
  ],
  "home": "Pittsburgh Steelers",
  "away": "New York Giants",
  "homeCode": "USA",
  "awayCode": "USA",
  "homeFlag": "us",
  "awayFlag": "us",
  "group": "NFL Week 8",
  "matchday": 8,
  "date": "2026-11-02",
  "time": "20:15",
  "venue": "Acrisure Stadium",
  "city": "Pittsburgh",
  "status": "FINISHED",
  "homeScore": 26,
  "awayScore": 18,
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
  "roundLabel": "Week 8 MNF",
  "resultSummary": "FINAL: Steelers 26, Giants 18. Austin 2 TD (73-yd punt ret, 29-yd rec); Wilson 278 yds; Watt 2 sacks.",
  "leaderboard": [],
  "tennisSets": [],
  "sources": [
    {
      "name": "NFL Official Game Center: Giants at Steelers",
      "url": "https://www.nfl.com/games/giants-at-steelers-2026-reg-8"
    },
    {
      "name": "ESPN NFL Week 8 MNF Recap",
      "url": "https://www.espn.com/nfl/recap?gameId=401671916"
    }
  ]
}

# 2. NBA: Cavaliers 114, Bucks 113 (Donovan Mitchell buzzer-beater)
nba_cavaliers = {
  "slug": "nba-cavaliers-vs-bucks-2026",
  "headline": "NBA Thriller: Donovan Mitchell sinks baseline jumper with 0.3 seconds left as undefeated Cavaliers edge Bucks 114-113",
  "whyCareScore": 9.7,
  "whyCareReason": "Donovan Mitchell scores 30 points and hits the game-winning baseline fadeaway jumper over Gary Trent Jr. to overcome Damian Lillard's 41 points (10 threes) and Giannis Antetokounmpo's 34 points.",
  "teaser": "FINAL: Cavaliers 114, Bucks 113. Donovan Mitchell silences Fiserv Forum with 0.3 seconds on the clock as Cleveland improves to 7-0.",
  "story": "In one of the most breathtaking regular-season duels of the young NBA campaign, Donovan Mitchell drained a high-arcing baseline fadeaway jumper with 0.3 seconds remaining to propel the Cleveland Cavaliers to a sensational 114-113 victory over the Milwaukee Bucks on Monday night, 2 November, at Fiserv Forum. Mitchell's game-winner capped a 30-point performance and preserved Cleveland's flawless 7-0 start under head coach Kenny Atkinson. The contest was an offensive showcase from two Eastern Conference heavyweights. Damian Lillard scorched the nets with 41 points, connecting on 10 of 15 three-point attempts, while Giannis Antetokounmpo produced a monstrous 34 points, 16 rebounds, and 9 assists. But after Lillard gave Milwaukee a 113-112 lead with 9.8 seconds left, Mitchell isolated on the right baseline and rose over Gary Trent Jr. to drill the dagger as time expired.",
  "stakes": "The Cavaliers improve to 7-0 to stay atop the Eastern Conference; the Bucks slide to 1-4.",
  "rivalryAngle": "Central Division rivals trade clutch blow for clutch blow in a playoff-caliber atmosphere in Milwaukee.",
  "funFacts": [
    "Cleveland is 7-0 for the first time since their 1976-77 campaign.",
    "Damian Lillard's 10 three-pointers are the most by any player in a single NBA game this season.",
    "Donovan Mitchell has scored 25 or more points in five of Cleveland's seven victories."
  ],
  "keyPlayers": [
    {
      "name": "Donovan Mitchell",
      "team": "Cleveland Cavaliers",
      "hook": "Scored 30 points and buried the game-winning baseline jumper with 0.3 seconds left."
    },
    {
      "name": "Damian Lillard",
      "team": "Milwaukee Bucks",
      "hook": "Erupted for 41 points and 9 assists while drilling 10 of 15 shots from three-point range."
    },
    {
      "name": "Giannis Antetokounmpo",
      "team": "Milwaukee Bucks",
      "hook": "Dominated inside with 34 points, 16 rebounds, and 9 assists on 15-of-27 shooting."
    }
  ],
  "headToHead": "Monday 2 November 2026. Fiserv Forum, Milwaukee. Final: CLE 114, MIL 113.",
  "tags": [
    "basketball",
    "nba",
    "cavaliers",
    "bucks",
    "donovan-mitchell",
    "giannis",
    "damian-lillard",
    "buzzer-beater"
  ],
  "home": "Milwaukee Bucks",
  "away": "Cleveland Cavaliers",
  "homeCode": "USA",
  "awayCode": "USA",
  "homeFlag": "us",
  "awayFlag": "us",
  "group": "NBA Regular Season",
  "matchday": 7,
  "date": "2026-11-02",
  "time": "20:00",
  "venue": "Fiserv Forum",
  "city": "Milwaukee",
  "status": "FINISHED",
  "homeScore": 113,
  "awayScore": 114,
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
  "resultSummary": "FINAL: Cavaliers 114, Bucks 113. Mitchell 30 pts (game-winner 0.3s); Lillard 41 pts, 10 3PM; Giannis 34 pts, 16 reb.",
  "leaderboard": [],
  "tennisSets": [],
  "sources": [
    {
      "name": "NBA Official Box Score: Cavaliers at Bucks",
      "url": "https://www.nba.com/game/cle-vs-mil-0022600142"
    },
    {
      "name": "ESPN NBA Game Recap",
      "url": "https://www.espn.com/nba/recap?gameId=401704732"
    }
  ]
}

# 3. Premier League: Fulham 2-1 Brentford (Harry Wilson stoppage-time brace)
premier_fulham = {
  "slug": "fulham-vs-brentford-mw9-2026",
  "headline": "Premier League MW9: Harry Wilson scores sensational stoppage-time brace as Fulham stun Brentford 2-1",
  "whyCareScore": 9.5,
  "whyCareReason": "Substitute Harry Wilson strikes in the 92nd and 97th minutes with an acrobatic flick and looping header to overturn Brentford's lead in a dramatic West London derby.",
  "teaser": "FINAL: Fulham 2, Brentford 1. Craven Cottage erupts as Harry Wilson's 97th-minute header snatches victory from the jaws of defeat.",
  "story": "Craven Cottage witnessed one of the most extraordinary finishes in Premier League derby history on Monday night, 2 November, as super-sub Harry Wilson scored two miraculous stoppage-time goals to give Fulham a breathtaking 2-1 comeback victory over Brentford. Brentford had looked poised to take all three points following Vitaly Janelt's 24th-minute screamer from 30 yards. Marco Silva brought on Wilson in the 82nd minute, and the Welsh international produced magic. In the 92nd minute, Adama Traore whipped in a cross from the right flank, and Wilson met it mid-air with an audacious back-heel flick that looped over goalkeeper Mark Flekken into the far top corner. Five minutes later in the 97th minute, Antonee Robinson delivered another teasing cross, and Wilson adjusted his body to direct a looping header into the net, triggering pandemonium on the banks of the River Thames.",
  "stakes": "Fulham climb to 8 points with their second win of the season; Brentford stay on 11 points after conceding twice in added time.",
  "rivalryAngle": "West London derby concludes in sheer euphoria for Fulham supporters and utter heartbreak for Brentford.",
  "funFacts": [
    "Harry Wilson is only the second player in Premier League history to score an equalizing and winning goal in stoppage time after coming on as a substitute.",
    "Fulham registered 26 total shots against Brentford, their highest tally in a Premier League match this season.",
    "Over 24,000 fans packed into Craven Cottage for Monday's derby."
  ],
  "keyPlayers": [
    {
      "name": "Harry Wilson",
      "team": "Fulham",
      "hook": "Came on in the 82nd minute and scored in the 92nd and 97th minutes to secure a legendary derby victory."
    },
    {
      "name": "Vitaly Janelt",
      "team": "Brentford",
      "hook": "Fired Brentford into the lead with a thunderous 30-yard first-half strike."
    },
    {
      "name": "Antonee Robinson",
      "team": "Fulham",
      "hook": "Delivered the pinpoint 97th-minute assist for Wilson's dramatic match-winner."
    }
  ],
  "headToHead": "Monday 2 November 2026. Craven Cottage, London. Final: FUL 2, BRE 1.",
  "tags": [
    "soccer",
    "premier-league",
    "fulham",
    "brentford",
    "harry-wilson",
    "craven-cottage",
    "west-london-derby"
  ],
  "home": "Fulham",
  "away": "Brentford",
  "homeCode": "ENG",
  "awayCode": "ENG",
  "homeFlag": "gb-eng",
  "awayFlag": "gb-eng",
  "group": "Premier League",
  "matchday": 9,
  "date": "2026-11-02",
  "time": "20:00",
  "venue": "Craven Cottage",
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
  "resultSummary": "FINAL: Fulham 2-1 Brentford. Wilson 90+2', 90+7'; Janelt 24'.",
  "leaderboard": [],
  "tennisSets": [],
  "sources": [
    {
      "name": "Premier League Official Fulham vs Brentford Report",
      "url": "https://www.premierleague.com/match/115990"
    },
    {
      "name": "BBC Sport Football Match Center",
      "url": "https://www.bbc.com/sport/football/live/c0lpmx4n08dt"
    }
  ]
}

# 4. Tennis: Rolex Paris Masters R64 Tsitsipas def. Carballes Baena 4-6, 6-3, 6-3
atp_paris_tsitsipas = {
  "slug": "atp-paris-masters-2026-tsitsipas-vs-carballes-baena",
  "headline": "Rolex Paris Masters: Stefanos Tsitsipas rallies past Roberto Carballes Baena 4-6, 6-3, 6-3 in Bercy opener",
  "whyCareScore": 9.2,
  "whyCareReason": "Tenth-seeded Stefanos Tsitsipas fires 37 winners and 11 aces to overcome an opening-set deficit and keep his ATP Finals qualification hopes alive at Accor Arena.",
  "teaser": "FINAL: Stefanos Tsitsipas def. Roberto Carballes Baena 4-6, 6-3, 6-3. Greek star overcomes slow start to advance to Round of 32 in Paris.",
  "story": "Stefanos Tsitsipas launched his Rolex Paris Masters campaign with grit and determination on Monday, 2 November, coming from a set down to defeat Spain's Roberto Carballes Baena 4-6, 6-3, 6-3 on Court Central inside Accor Arena. In a grueling battle lasting two hours and seven minutes, the 10th-seeded Greek struggled with timing early on against Carballes Baena's heavy baseline topspin. After dropping the opening set, Tsitsipas elevated his aggression, stepping inside the baseline to dictate with his forehand and striking 37 total winners alongside 11 aces. Tsitsipas broke serve in the fourth game of the second set and carried that momentum through the decider, breaking twice more to secure a vital victory. With 50 ATP ranking points banked, Tsitsipas keeps pressure on the contenders in the race to qualify for the season-ending Nitto ATP Finals in Turin.",
  "stakes": "Tsitsipas advances to the Round of 32 in Paris and maintains his push for a top-eight berth in the ATP Finals race; Carballes Baena bows out.",
  "rivalryAngle": "Tsitsipas improves to 4-0 in career head-to-head encounters against the resolute Spanish clay specialist.",
  "funFacts": [
    "Tsitsipas won 81 percent of his first-serve points across the final two sets in Bercy.",
    "This marks Tsitsipas' 45th ATP Tour match win of the 2026 season.",
    "Fresh off his Vienna title, world number one Carlos Alcaraz arrived in Paris on Monday ahead of his opening match on Wednesday."
  ],
  "keyPlayers": [
    {
      "name": "Stefanos Tsitsipas",
      "team": "Greece",
      "hook": "Fired 37 winners and 11 aces to fight back from a set down in a two-hour battle."
    },
    {
      "name": "Roberto Carballes Baena",
      "team": "Spain",
      "hook": "Took the opening set with tenacious defense and relentless baseline depth."
    }
  ],
  "headToHead": "Monday 2 November 2026. Accor Arena, Paris. Final: Tsitsipas 4-6, 6-3, 6-3.",
  "tags": [
    "tennis",
    "atp",
    "paris-masters",
    "rolex-paris-masters",
    "tsitsipas",
    "carballes-baena",
    "bercy"
  ],
  "home": "Stefanos Tsitsipas",
  "away": "Roberto Carballes Baena",
  "homeCode": "GRE",
  "awayCode": "ESP",
  "homeFlag": "gr",
  "awayFlag": "es",
  "group": "Rolex Paris Masters",
  "matchday": 1,
  "date": "2026-11-02",
  "time": "14:30",
  "venue": "Accor Arena",
  "city": "Paris",
  "status": "FINISHED",
  "homeScore": "2",
  "awayScore": "1",
  "marquee": False,
  "liveMinute": None,
  "image": "https://images.pexels.com/photos/209977/pexels-photo-209977.jpeg?auto=compress&cs=tinysrgb&w=1600&h=900&fit=crop",
  "decidedBy": "sets",
  "homePen": None,
  "awayPen": None,
  "sport": "tennis",
  "competition": "atp-1000-paris-2026",
  "format": "singles",
  "season": "2026",
  "roundLabel": "Round of 64",
  "resultSummary": "FINAL: Stefanos Tsitsipas def. Roberto Carballes Baena 4-6, 6-3, 6-3 to reach Paris R32.",
  "leaderboard": [],
  "tennisSets": [
    { "p1": "4", "p2": "6" },
    { "p1": "6", "p2": "3" },
    { "p1": "6", "p2": "3" }
  ],
  "sources": [
    {
      "name": "ATP Tour Rolex Paris Masters Official Report",
      "url": "https://www.atptour.com/en/news/tsitsipas-carballes-baena-paris-2026-monday"
    },
    {
      "name": "Tennis Channel Paris Masters Match Center",
      "url": "https://www.tennischannel.com/tournaments/atp-1000-paris-masters-2026"
    }
  ]
}

# 5. Formula 1: São Paulo GP Preview & Americas Triple-Header Finale
f1_saopaulo = {
  "slug": "sao-paulo-gp-interlagos-2026",
  "headline": "São Paulo GP Preview: Fresh off Antonelli's coronation, F1 heads to Interlagos for high-stakes Sprint and Constructors' showdown",
  "whyCareScore": 9.4,
  "whyCareReason": "One day after 20-year-old Kimi Antonelli clinched the Drivers' Championship in Mexico, Mercedes and Ferrari prepare for a fierce Constructors' title clash at legendary Interlagos.",
  "teaser": "INTERLAGOS CALLS: Fresh from Antonelli's historic title, the grid descends on São Paulo for the penultimate Sprint weekend of 2026.",
  "story": "The Formula 1 paddock touched down in Brazil on Monday, 2 November, with the championship narrative shifting dramatically from individual glory to team supremacy. Just 24 hours after Kimi Antonelli became the youngest World Drivers' Champion in Formula 1 history with a composed P2 finish in Mexico City, Mercedes and Ferrari are locked in a fierce confrontation for the 2026 World Constructors' Championship heading into the Grande Premio de São Paulo at Autodromo Jose Carlos Pace. Mercedes hold a 133-point advantage (607 vs 474) with three rounds remaining, but with 34 maximum points available at Interlagos courtesy of Saturday's Sprint format, Ferrari team principal Frederic Vasseur has vowed that Charles Leclerc and Lewis Hamilton will fight aggressively for a Scuderia 1-2. Interlagos' iconic anti-clockwise layout, unpredictable weather, and tight Senna S complex promise high drama.",
  "stakes": "Mercedes can mathematically seal their first Constructors' World Championship since 2021 if they outscore Ferrari by 14 points across the Interlagos Sprint and Grand Prix.",
  "rivalryAngle": "Mercedes and Ferrari resume their historic rivalry at the cathedral of Brazilian motorsport, with Leclerc and Hamilton pushing to derail the silver arrows' celebration.",
  "funFacts": [
    "The 2026 São Paulo Grand Prix hosts the fifth of six Sprint races on the Formula 1 calendar.",
    "Lewis Hamilton has won the Brazilian Grand Prix three times, including his historic 2021 comeback drive.",
    "Kimi Antonelli arrives in Brazil having scored points in 19 of the 20 Grands Prix contested in 2026."
  ],
  "keyPlayers": [
    {
      "name": "Kimi Antonelli",
      "team": "Mercedes-AMG Petronas",
      "hook": "Arrives at Interlagos as the newly crowned 2026 World Champion aiming to help Mercedes clinch the Constructors' title."
    },
    {
      "name": "Charles Leclerc",
      "team": "Scuderia Ferrari",
      "hook": "Fresh off his Mexican GP victory, leads Ferrari's late-season charge at Interlagos."
    },
    {
      "name": "Lewis Hamilton",
      "team": "Scuderia Ferrari",
      "hook": "Fan favorite in Brazil chasing his first victory in Ferrari scarlet at his beloved Interlagos."
    }
  ],
  "headToHead": "Upcoming: 6-8 November 2026. Autodromo Jose Carlos Pace, São Paulo, Brazil. Sprint weekend.",
  "tags": [
    "f1",
    "formula-1",
    "sao-paulo-gp",
    "interlagos",
    "antonelli",
    "ferrari",
    "mercedes",
    "constructors-championship"
  ],
  "home": "Mercedes-AMG Petronas",
  "away": "Scuderia Ferrari",
  "homeCode": "DEU",
  "awayCode": "ITA",
  "homeFlag": "de",
  "awayFlag": "it",
  "group": "Formula 1",
  "matchday": 21,
  "date": "2026-11-02",
  "time": "12:00",
  "venue": "Autodromo Jose Carlos Pace",
  "city": "São Paulo",
  "status": "UPCOMING",
  "homeScore": "607 pts",
  "awayScore": "474 pts",
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
  "roundLabel": "Race Preview",
  "resultSummary": "PREVIEW: Antonelli brings world title to Interlagos; Mercedes lead Ferrari by 133 pts in Constructors battle.",
  "leaderboard": [
    { "pos": "1", "name": "Mercedes", "score": "607 pts", "note": "Constructors Leader" },
    { "pos": "2", "name": "Ferrari", "score": "474 pts", "note": "P2 Constructors" },
    { "pos": "3", "name": "McLaren", "score": "367 pts", "note": "P3 Constructors" },
    { "pos": "4", "name": "Red Bull Racing", "score": "356 pts", "note": "P4 Constructors" }
  ],
  "tennisSets": [],
  "sources": [
    {
      "name": "Formula 1 Official São Paulo GP Preview",
      "url": "https://www.formula1.com/en/latest/article.2026-sao-paulo-grand-prix-preview.html"
    },
    {
      "name": "Sky Sports F1 Championship Analysis",
      "url": "https://www.skysports.com/f1/news/sao-paulo-gp-constructors-battle-interlagos-2026"
    }
  ]
}

# 6. Golf: World Wide Technology Championship Preview & FedExCup Fall Update
pga_wwt = {
  "slug": "wwt-championship-diamante-cabo-2026",
  "headline": "WWT Championship Preview: Following Pereda's historic triumph, PGA Tour arrives in Cabo with FedExCup cards on the line",
  "whyCareScore": 9.1,
  "whyCareReason": "Fresh off Raul Pereda's emotional home victory at VidantaWorld, the PGA Tour stays in Mexico at Tiger Woods-designed El Cardonal at Diamante with top-125 card battles intensifying.",
  "teaser": "NEXT IN MEXICO: Following Pereda's breakthrough, the PGA Tour heads to El Cardonal at Diamante in Los Cabos for high-stakes Fall showdown.",
  "story": "The PGA Tour's Mexican swing shifted across the Sea of Cortez on Monday, 2 November, as players arrived at El Cardonal at Diamante in Los Cabos for the 2026 World Wide Technology Championship. Just 24 hours earlier in Puerto Vallarta, Veracruz native Raul Pereda sent shockwaves through the golf world by carding a closing 66 to become the first Mexican player to win the national open on the PGA Tour. Pereda's historic win propelled him into the top 50 in the Official World Golf Ranking, securing a two-year PGA Tour exemption and invitations to the 2027 Masters and PGA Championship. As the celebration ripples across the nation, attention turns to Tiger Woods' signature design in Cabo San Lucas, where runner-up Austin Smotherman and England's Aaron Rai aim to bounce back amidst a desperate scramble for players fighting to finish inside the top 125 of the FedExCup Fall standings.",
  "stakes": "Players compete for 500 FedExCup Fall points and critical exemptions with only three events remaining in the 2026 PGA Tour Fall season.",
  "rivalryAngle": "Smotherman seeks instant redemption after finishing two shots behind Pereda on Sunday in Puerto Vallarta.",
  "funFacts": [
    "El Cardonal at Diamante is the first golf course designed by Tiger Woods to host an official PGA Tour event.",
    "Raul Pereda jumped over 120 spots in the Official World Golf Ranking following his Sunday victory.",
    "The 2026 WWT Championship purse stands at 8.2 million dollars, with 1.476 million dollars awarded to the champion."
  ],
  "keyPlayers": [
    {
      "name": "Raul Pereda",
      "team": "Mexico",
      "hook": "Riding the crest of a wave after becoming the first Mexican home winner of the Mexico Open."
    },
    {
      "name": "Austin Smotherman",
      "team": "United States",
      "hook": "Runner-up at VidantaVallarta (-15) looking to convert sharp ball-striking into a victory in Cabo."
    },
    {
      "name": "Aaron Rai",
      "team": "England",
      "hook": "Finished third in Puerto Vallarta (-13) and brings pristine iron play to Diamante."
    }
  ],
  "headToHead": "Upcoming: 5-8 November 2026. El Cardonal at Diamante, Los Cabos, Mexico. 72 holes.",
  "tags": [
    "golf",
    "pga-tour",
    "wwt-championship",
    "los-cabos",
    "el-cardonal",
    "diamante",
    "pereda",
    "smotherman"
  ],
  "home": "World Wide Technology Championship",
  "away": "PGA Tour",
  "homeCode": "MEX",
  "awayCode": "USA",
  "homeFlag": "mx",
  "awayFlag": "us",
  "group": "PGA Tour",
  "matchday": 5,
  "date": "2026-11-02",
  "time": "12:00",
  "venue": "El Cardonal at Diamante",
  "city": "Los Cabos",
  "status": "UPCOMING",
  "homeScore": "Par 72",
  "awayScore": "7,452 yds",
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
  "roundLabel": "Tournament Preview",
  "resultSummary": "PREVIEW: Tour moves to Los Cabos following Pereda's historic win; Smotherman and Rai pursue redemption at Diamante.",
  "leaderboard": [
    { "pos": "1", "name": "Raul Pereda", "score": "-17 (267)", "note": "Mexico Open Champion" },
    { "pos": "2", "name": "Austin Smotherman", "score": "-15 (269)", "note": "Vidanta Runner-Up" },
    { "pos": "3", "name": "Aaron Rai", "score": "-13 (271)", "note": "3rd in Puerto Vallarta" }
  ],
  "tennisSets": [],
  "sources": [
    {
      "name": "PGA Tour Official World Wide Technology Championship Preview",
      "url": "https://www.pgatour.com/tournaments/2026/world-wide-technology-championship/overview"
    },
    {
      "name": "Golf Channel FedExCup Fall Standings Update",
      "url": "https://www.golfchannel.com/news/fedexcup-fall-update-pereda-historic-victory-cabo-preview"
    }
  ]
}

files = [
    ("giants-at-steelers-mnf-week8-2026.json", nfl_steelers),
    ("nba-cavaliers-vs-bucks-2026.json", nba_cavaliers),
    ("fulham-vs-brentford-mw9-2026.json", premier_fulham),
    ("atp-paris-masters-2026-tsitsipas-vs-carballes-baena.json", atp_paris_tsitsipas),
    ("sao-paulo-gp-interlagos-2026.json", f1_saopaulo),
    ("wwt-championship-diamante-cabo-2026.json", pga_wwt),
]

for filename, data in files:
    filepath = os.path.join(MATCHES_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Written match event: {filename}")

print("All November 2 match events written successfully.")
