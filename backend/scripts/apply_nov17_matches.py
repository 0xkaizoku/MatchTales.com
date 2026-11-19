"""Create and update match JSONs for 2026-11-17."""
import os
import json

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
MATCHES = os.path.join(ROOT, "frontend", "src", "content", "matches")

# 1. Update chargers-at-ravens-mnf-week10-2026.json
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
  "status": "FINISHED",
  "roundLabel": "Week 10 · Monday Night Football Final",
  "group": "NFL",
  "venue": "M&T Bank Stadium, Baltimore",
  "city": "Baltimore",
  "homeScore": "20",
  "awayScore": "23",
  "whyCareScore": 9.5,
  "headline": "Monday Night Football: Chargers edge Ravens 23-20 as Jim Harbaugh tops John in brotherly clash",
  "teaser": "Justin Herbert runs for a 22-yard touchdown, rookie Omarion Hampton rushes for 105 yards, and Tarheeb Still forces a late fumble on Zay Flowers to seal a 23-20 road triumph for Los Angeles.",
  "story": "Jim Harbaugh secured bragging rights in the family rivalry on Monday night, 16 November, as his Los Angeles Chargers held off John Harbaugh and the Baltimore Ravens for a gritty 23-20 road victory at M&T Bank Stadium.\n\nJustin Herbert set the tone early for the visitors, scrambling out of pressure and diving inside the pylon for a 22-yard touchdown run to give Los Angeles a lead they would never surrender. Rookie running back Omarion Hampton delivered a breakout prime-time performance, pounding Baltimore's front seven for 105 yards on 21 carries, including a physical 4-yard touchdown plunge in the third quarter.\n\nLamar Jackson rallied the Ravens in the fourth quarter, connecting with Mark Andrews on a 14-yard touchdown pass to pull within three points. But with Baltimore driving into field goal range in the final two minutes, Chargers cornerback Tarheeb Still punched the ball loose from Zay Flowers, allowing Los Angeles to recover and run out the clock to improve to 7-3.",
  "whyCareReason": "Jim Harbaugh edges John Harbaugh in the second official coaching clash between brothers, earning Los Angeles a pivotal tiebreaker in the AFC playoff race.",
  "stakes": "The Chargers (7-3) cement their position in the AFC wild card race while the Ravens (7-3) lose critical ground in the AFC North.",
  "rivalryAngle": "First meeting between Jim and John Harbaugh since Super Bowl XLVII in New Orleans, with Jim claiming his first head-to-head NFL win over his older brother.",
  "funFacts": [
    "The Chargers outrushed the Ravens 160 yards to 16, holding Derrick Henry to just 12 rushing yards.",
    "Justin Herbert recorded his first career 20-plus-yard rushing touchdown on Monday Night Football.",
    "Tarheeb Still's fourth-quarter forced fumble was his third turnover created in the last four games."
  ],
  "keyPlayers": [
    {
      "name": "Justin Herbert",
      "team": "Los Angeles Chargers",
      "hook": "Scored the opening touchdown on a 22-yard scramble and managed a mistake-free offense."
    },
    {
      "name": "Omarion Hampton",
      "team": "Los Angeles Chargers",
      "hook": "Ran for 105 yards and a touchdown on 21 carries in his breakout prime-time performance."
    },
    {
      "name": "Lamar Jackson",
      "team": "Baltimore Ravens",
      "hook": "Threw two touchdown passes but was sacked four times by the relentless Chargers pass rush."
    }
  ],
  "tags": [
    "nfl",
    "monday-night-football",
    "chargers",
    "ravens",
    "harbaugh-bowl",
    "justin-herbert",
    "omarion-hampton",
    "lamar-jackson"
  ],
  "sources": [
    {
      "name": "NFL.com: Chargers 23-20 Ravens Final Box Score",
      "url": "https://www.nfl.com/games/chargers-at-ravens-2026-reg-10"
    },
    {
      "name": "ESPN: Jim Harbaugh tops John as Chargers edge Ravens on MNF",
      "url": "https://www.espn.com/nfl/recap/_/gameId/401671780"
    },
    {
      "name": "Associated Press: Herbert, Hampton lead Chargers past Ravens 23-20 in Harbaugh Bowl",
      "url": "https://apnews.com/article/chargers-ravens-nfl-harbaugh-bowl-20261116"
    }
  ]
}
open(chargers_ravens_path, "w", encoding="utf-8").write(json.dumps(chargers_ravens_data, indent=2, ensure_ascii=False) + "\n")
print("Updated chargers-at-ravens match JSON.")

# 2. Create germany-vs-netherlands-nations-league-2026.json
germany_neth_path = os.path.join(MATCHES, "germany-vs-netherlands-nations-league-2026.json")
germany_neth_data = {
  "slug": "germany-vs-netherlands-nations-league-2026",
  "sport": "soccer",
  "competition": "uefa-nations-league",
  "format": "team-match",
  "home": "Germany",
  "away": "Netherlands",
  "homeCode": "DEU",
  "awayCode": "NLD",
  "homeFlag": "de",
  "awayFlag": "nl",
  "date": "2026-11-16",
  "time": "20:45 CET",
  "status": "FINISHED",
  "roundLabel": "Matchday 6 · Final Result",
  "group": "A2",
  "venue": "Red Bull Arena, Leipzig",
  "city": "Leipzig",
  "homeScore": "5",
  "awayScore": "0",
  "whyCareScore": 9.6,
  "headline": "Nations League: Germany crush Netherlands 5-0 to seal Group A2 top spot",
  "teaser": "Florian Wirtz scores twice while Derry Scherhant, Nico Schlotterbeck, and Brajan Gruda add goals as Germany inflict the Netherlands' heaviest defeat in 67 years to win Group A2.",
  "story": "Germany produced a masterclass of attacking football on Monday night, 16 November, dismantling traditional rivals the Netherlands 5-0 in Leipzig to capture first place in UEFA Nations League Group A2.\n\nJulian Nagelsmann's side took control late in the first half when 23-year-old winger Derry Scherhant opened the scoring on 41 minutes with a crisp angled drive. The floodgates opened after the break as Florian Wirtz curled home a magnificent 20-yard effort on the hour mark. Nico Schlotterbeck headed in a corner on 65 minutes, substitute Brajan Gruda slotted home a fourth on 72 minutes, and Wirtz completed his brace in the 77th minute with a delicate chip over Bart Verbruggen.\n\nThe 5-0 scoreline represents the Netherlands' worst defeat in an international fixture since 1959. Although both nations advance to the quarter-finals in March 2027, Germany secure seeded status while Ronald Koeman's squad face an inquest after an uncharacteristically fragile defensive collapse.",
  "whyCareReason": "Germany hand their fiercest rivals their worst defeat since 1959, securing the top seed in Nations League Group A2 in emphatic fashion.",
  "stakes": "Germany finish top of Group A2 to earn seeded quarter-final status in March 2027, sending the Dutch through as unseeded runners-up.",
  "rivalryAngle": "Historic renewal of one of international football's fiercest rivalries, ending in unprecedented German dominance before 42,000 in Leipzig.",
  "funFacts": [
    "The 5-0 defeat was the Netherlands' heaviest margin of defeat in any international match since November 1959.",
    "Florian Wirtz recorded his second career international brace, scoring in the 60th and 77th minutes.",
    "Germany scored four goals in a blistering 17-minute second-half stretch."
  ],
  "keyPlayers": [
    {
      "name": "Florian Wirtz",
      "team": "Germany",
      "hook": "Dictated the midfield tempo and scored two spectacular second-half goals."
    },
    {
      "name": "Derry Scherhant",
      "team": "Germany",
      "hook": "Broke the deadlock in the 41st minute with a clinical low strike to set Germany on their way."
    },
    {
      "name": "Virgil van Dijk",
      "team": "Netherlands",
      "hook": "Captained the Dutch defense during a torrid second-half onslaught in Leipzig."
    }
  ],
  "tags": [
    "soccer",
    "uefa-nations-league",
    "germany",
    "netherlands",
    "florian-wirtz",
    "derry-scherhant",
    "virgil-van-dijk"
  ],
  "sources": [
    {
      "name": "UEFA Official: Germany 5-0 Netherlands Match Report",
      "url": "https://www.uefa.com/uefanationsleague/match/germany-vs-netherlands-2026/"
    },
    {
      "name": "Goal.com: Wirtz sparkles as Germany hammer Dutch 5-0 in Leipzig",
      "url": "https://www.goal.com/en/news/germany-netherlands-nations-league-20261116"
    },
    {
      "name": "Reuters: Germany inflict worst Dutch defeat in 67 years with 5-0 Nations League romp",
      "url": "https://www.reuters.com/sports/soccer/germany-crush-netherlands-5-0-nations-league-2026-11-16/"
    }
  ]
}
open(germany_neth_path, "w", encoding="utf-8").write(json.dumps(germany_neth_data, indent=2, ensure_ascii=False) + "\n")
print("Created germany-vs-netherlands match JSON.")

# 3. Update atp-nitto-finals-2026-turin-draw.json
turin_path = os.path.join(MATCHES, "atp-nitto-finals-2026-turin-draw.json")
turin_data = {
  "slug": "atp-nitto-finals-2026-turin-draw",
  "headline": "Nitto ATP Finals: Alcaraz sweeps Tiafoe 6-2, 6-2; Zverev meets Shelton in Tuesday night clash",
  "whyCareScore": 9.5,
  "whyCareReason": "Carlos Alcaraz sweeps Frances Tiafoe 6-2, 6-2 in 69 minutes to launch Lendl Group play; Alexander Zverev faces Ben Shelton in Tuesday night's McEnroe Group battle of 1-0 unbeatens.",
  "teaser": "World No. 2 Carlos Alcaraz opens his Turin campaign with an emphatic 6-2, 6-2 win over Frances Tiafoe in 69 minutes. Daniil Medvedev tops Flavio Cobolli in two sets, while Tuesday evening features Alexander Zverev against Ben Shelton.",
  "story": "The 2026 Nitto ATP Finals in Turin hit full stride on Monday, 16 November, as the Ivan Lendl Group delivered high-quality opening matches at Inalpi Arena.\n\nWorld No. 2 Carlos Alcaraz delivered an emphatic statement of intent in the afternoon session, dismantling good friend Frances Tiafoe 6-2, 6-2 in just 69 minutes. The Spaniard fired 24 winners and never faced a break point, dominating from the baseline with devastating forehand combinations. In the evening contest, former champion Daniil Medvedev relied on clinical tiebreak execution to defeat Italian hope Flavio Cobolli 7-6 (4), 6-3.\n\nTuesday 17 November shifts back to the John McEnroe Group with a blockbuster evening showdown: World No. 1 Alexander Zverev faces American powerhouse Ben Shelton not before 8:30 p.m. CET in a rematch of the 2026 US Open final. Both enter at 1-0, with the winner in prime position to lock up a semi-final berth. Earlier, Arthur Fils and Rafael Jodar meet at 2:00 p.m. CET in a battle to keep semi-final hopes alive.",
  "stakes": "Alcaraz and Medvedev lead Lendl Group at 1-0; Tuesday winner between Zverev and Shelton takes sole possession of first place in McEnroe Group.",
  "rivalryAngle": "Zverev leads Shelton 6-0 in their career head-to-head series, including a four-set victory in September's US Open final at Arthur Ashe Stadium.",
  "funFacts": [
    "Carlos Alcaraz dropped only 10 points on his serve during his 69-minute victory over Frances Tiafoe.",
    "Alexander Zverev has won 16 of his last 18 indoor hard-court sets dating back to Vienna and Paris.",
    "Ben Shelton struck 16 aces in his opening three-set victory over Arthur Fils on Sunday."
  ],
  "keyPlayers": [
    {
      "name": "Alexander Zverev",
      "team": "Germany",
      "hook": "Top seed looking to extend his 6-0 head-to-head record against Shelton on Tuesday night."
    },
    {
      "name": "Ben Shelton",
      "team": "United States",
      "hook": "American star aiming for revenge after falling to Zverev in the 2026 US Open final."
    },
    {
      "name": "Carlos Alcaraz",
      "team": "Spain",
      "hook": "Cruised through his Lendl Group opener with a clinical 6-2, 6-2 rout of Frances Tiafoe."
    }
  ],
  "headToHead": "Tournament dates 15-22 November 2026, Inalpi Arena, Turin. Day 1 & Day 2 complete. Tuesday evening: Zverev vs Shelton.",
  "tags": [
    "tennis",
    "atp",
    "nitto-atp-finals",
    "turin",
    "alcaraz",
    "zverev",
    "shelton",
    "medvedev",
    "tiafoe"
  ],
  "home": "Alexander Zverev",
  "away": "Ben Shelton",
  "homeCode": "GER",
  "awayCode": "USA",
  "homeFlag": "de",
  "awayFlag": "us",
  "group": "Nitto ATP Finals McEnroe",
  "matchday": 2,
  "date": "2026-11-17",
  "time": "20:30 CET",
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
  "roundLabel": "Turin McEnroe Group Day 2",
  "resultSummary": "MON Lendl: Alcaraz d Tiafoe 6-2, 6-2; Medvedev d Cobolli 7-6 (4), 6-3. TUE McEnroe: Fils vs Jodar (14:00 CET), Zverev vs Shelton (20:30 CET).",
  "leaderboard": [
    {
      "pos": "Lendl 1-0",
      "name": "Carlos Alcaraz (2)",
      "score": "1-0 (2-0 sets)",
      "note": "Def. Tiafoe 6-2, 6-2"
    },
    {
      "pos": "Lendl 1-0",
      "name": "Daniil Medvedev (4)",
      "score": "1-0 (2-0 sets)",
      "note": "Def. Cobolli 7-6, 6-3"
    },
    {
      "pos": "McEnroe 1-0",
      "name": "Alexander Zverev (1)",
      "score": "1-0 (2-0 sets)",
      "note": "Tue night vs Shelton"
    },
    {
      "pos": "McEnroe 1-0",
      "name": "Ben Shelton (3)",
      "score": "1-0 (2-1 sets)",
      "note": "Tue night vs Zverev"
    },
    {
      "pos": "McEnroe 0-1",
      "name": "Arthur Fils (6)",
      "score": "0-1 (1-2 sets)",
      "note": "Tue 14:00 vs Jodar"
    },
    {
      "pos": "McEnroe 0-1",
      "name": "Rafael Jodar (8)",
      "score": "0-1 (0-2 sets)",
      "note": "Tue 14:00 vs Fils"
    }
  ],
  "tennisSets": [
    {
      "p1": "6",
      "p2": "2"
    },
    {
      "p1": "6",
      "p2": "2"
    }
  ],
  "sources": [
    {
      "name": "Nitto ATP Finals Official: Alcaraz storms past Tiafoe; Medvedev tops Cobolli",
      "url": "https://www.nittoatpfinals.com/en/news/alcaraz-tiafoe-turin-2026-monday"
    },
    {
      "name": "ATP Tour Scores: Turin 2026 Day 2 Results & Tuesday Schedule",
      "url": "https://www.atptour.com/en/scores/current/nitto-atp-finals/0605/results"
    },
    {
      "name": "FlashScore: Zverev vs Shelton Turin H2H and Live Odds",
      "url": "https://www.flashscore.com/match/turin-2026-zverev-shelton/"
    }
  ]
}
open(turin_path, "w", encoding="utf-8").write(json.dumps(turin_data, indent=2, ensure_ascii=False) + "\n")
print("Updated turin match JSON.")

# 4. Create nba-magic-vs-celtics-nov16-2026.json
nba_magic_path = os.path.join(MATCHES, "nba-magic-vs-celtics-nov16-2026.json")
nba_magic_data = {
  "slug": "nba-magic-vs-celtics-nov16-2026",
  "sport": "basketball",
  "competition": "nba",
  "format": "team-match",
  "home": "Boston Celtics",
  "away": "Orlando Magic",
  "homeCode": None,
  "awayCode": None,
  "date": "2026-11-16",
  "time": "7:30 PM ET",
  "status": "FINISHED",
  "roundLabel": "Regular Season",
  "group": "NBA",
  "venue": "TD Garden, Boston",
  "city": "Boston",
  "homeScore": "105",
  "awayScore": "115",
  "whyCareScore": 8.8,
  "headline": "NBA: Magic rally in fourth quarter to halt Celtics' six-game winning streak 115-105",
  "teaser": "Desmond Bane scores 24 points and Orlando outscores Boston 34-21 in the final frame to pull off a 115-105 upset at TD Garden, while Miami wins its fifth straight.",
  "story": "The Orlando Magic pulled off one of the most impressive road comebacks of the young NBA season on Monday night, 16 November, overcoming a double-digit second-half deficit to beat the Boston Celtics 115-105 at TD Garden.\n\nSharpshooter Desmond Bane paced the Magic with 24 points and 8 rebounds, connecting on 5 three-pointers to ignite a 34-21 fourth-quarter run that shocked the Boston faithful. Franz Wagner added 22 points and 7 assists, while Orlando's interior defense held Jayson Tatum and Jaylen Brown to just 8-of-25 shooting combined across the final 18 minutes.\n\nThe victory snapped Boston's six-game winning streak and improved Orlando to 8-5. Elsewhere on Monday, the Miami Heat won their fifth straight game behind Giannis Antetokounmpo (20 points, 13 rebounds) in a 128-110 rout of Houston, while Joel Embiid dropped a season-high 37 points in Philadelphia's 135-123 triumph over Brooklyn.",
  "whyCareReason": "Orlando proves its Eastern Conference contender credentials by halting the defending finalists' six-game winning streak in Boston.",
  "stakes": "Orlando (8-5) climbs to fourth in the East while Boston (9-4) drops into second behind Cleveland.",
  "rivalryAngle": "Heated Eastern clash at TD Garden where Orlando's perimeter shooting cracked Boston's top-rated perimeter defense.",
  "funFacts": [
    "Desmond Bane scored 14 of his 24 points during Orlando's decisive 34-21 fourth-quarter surge.",
    "Orlando held the Celtics to just 39 percent shooting from the field in the second half.",
    "The Magic have won three consecutive regular-season meetings against Boston in Massachusetts."
  ],
  "keyPlayers": [
    {
      "name": "Desmond Bane",
      "team": "Orlando Magic",
      "hook": "Exploded for 24 points, 8 rebounds, and 5 three-pointers to lead the fourth-quarter rally."
    },
    {
      "name": "Franz Wagner",
      "team": "Orlando Magic",
      "hook": "Orchestrated the offense with 22 points, 7 assists, and stellar point-of-attack defense."
    },
    {
      "name": "Jayson Tatum",
      "team": "Boston Celtics",
      "hook": "Scored 28 points but was held to two fourth-quarter field goals by Orlando's blitzing traps."
    }
  ],
  "tags": [
    "nba",
    "orlando-magic",
    "boston-celtics",
    "desmond-bane",
    "franz-wagner",
    "jayson-tatum"
  ],
  "sources": [
    {
      "name": "NBA.com: Magic at Celtics Box Score and Recap",
      "url": "https://www.nba.com/game/orl-vs-bos-20261116/box-score"
    },
    {
      "name": "Boston Globe: Magic stun Celtics 115-105 at TD Garden behind fourth-quarter flurry",
      "url": "https://www.bostonglobe.com/sports/celtics/2026/11/16/celtics-magic-recap/"
    },
    {
      "name": "Associated Press: Bane scores 24 as Magic snap Celtics' six-game winning streak",
      "url": "https://apnews.com/article/magic-celtics-nba-bane-recap-20261116"
    }
  ]
}
open(nba_magic_path, "w", encoding="utf-8").write(json.dumps(nba_magic_data, indent=2, ensure_ascii=False) + "\n")
print("Created nba-magic-vs-celtics match JSON.")

# 5. Create rsm-classic-sea-island-preview-2026.json
rsm_path = os.path.join(MATCHES, "rsm-classic-sea-island-preview-2026.json")
rsm_data = {
  "slug": "rsm-classic-sea-island-preview-2026",
  "sport": "golf",
  "competition": "pga-tour-2026",
  "format": "leaderboard",
  "home": "Davis Thompson",
  "away": "Mackenzie Hughes",
  "homeCode": "USA",
  "awayCode": "CAN",
  "date": "2026-11-19",
  "time": "07:30 EST",
  "status": "UPCOMING",
  "roundLabel": "PGA Tour Fall Finale Preview",
  "group": "PGA Tour FedExCup Fall",
  "venue": "Sea Island Golf Club (Seaside & Plantation)",
  "city": "St. Simons Island, Georgia",
  "homeScore": None,
  "awayScore": None,
  "whyCareScore": 9.2,
  "headline": "The RSM Classic: FedExCup Fall drama arrives at Sea Island with 2027 Tour cards on the line",
  "teaser": "The PGA Tour season concludes on the Georgia coast as players battle for crucial FedExCup points, full-status top-125 exemptions, and signature event invites.",
  "story": "Practice rounds got underway on Tuesday, 17 November, at Sea Island Golf Club on St. Simons Island, Georgia, setting the stage for the dramatic conclusion of the PGA Tour's FedExCup Fall at The RSM Classic (19-22 November).\n\nHosted by Davis Love III, the tournament represents the final opportunity for competitors to secure top-125 positioning in the FedExCup standings and guarantee fully exempt status for the 2027 PGA Tour campaign. Players finishing 126 through 150 retain conditional status, while those inside the top 60 earn entry into the lucrative early-season Signature Events.\n\nContested across the par-70 Seaside Course and par-72 Plantation Course, the event features a stacked field of Georgia residents and bubble contenders including Davis Thompson, two-time champion Mackenzie Hughes, and Austin Smotherman. Following Rory McIlroy's record-equalling eighth Race to Dubai crown on the European circuit, the focus now turns to pure survival golf along the Atlantic marshes.",
  "whyCareReason": "The final official PGA Tour tournament of 2026 decides which players retain full playing privileges and exemptions for the 2027 campaign.",
  "stakes": "Top-125 cutoff locks in full tour cards for 2027, while Nos. 51-60 qualify for AT&T Pebble Beach and The Genesis Invitational.",
  "rivalryAngle": "High-pressure survival golf where a single putt on Sunday afternoon can determine a player's career trajectory and tour status.",
  "funFacts": [
    "The RSM Classic uses both the Seaside and Plantation courses for the opening two rounds before the Seaside hosts the weekend.",
    "Davis Love III has hosted the event since its inception at Sea Island in 2010.",
    "Mackenzie Hughes is a two-time champion at Sea Island, winning in 2016 and 2022."
  ],
  "keyPlayers": [
    {
      "name": "Davis Thompson",
      "team": "United States",
      "hook": "Sea Island resident and recent PGA Tour winner headlining the local contingent."
    },
    {
      "name": "Mackenzie Hughes",
      "team": "Canada",
      "hook": "Two-time RSM Classic champion seeking a historic third victory on the Georgia links."
    },
    {
      "name": "Austin Smotherman",
      "team": "United States",
      "hook": "Bermuda Championship winner looking to cement his position in the FedExCup top 60."
    }
  ],
  "tags": [
    "golf",
    "pga-tour",
    "the-rsm-classic",
    "sea-island",
    "fedexcup-fall",
    "davis-thompson",
    "mackenzie-hughes"
  ],
  "leaderboard": [
    {
      "pos": "Bubble",
      "name": "Top-125 Card Battle",
      "score": "Cutoff Event",
      "note": "Final 2026 Tour stop"
    },
    {
      "pos": "Field",
      "name": "Davis Thompson",
      "score": "Local Favorite",
      "note": "Sea Island resident"
    },
    {
      "pos": "Field",
      "name": "Mackenzie Hughes",
      "score": "2x Champion",
      "note": "Won 2016, 2022"
    },
    {
      "pos": "Field",
      "name": "Austin Smotherman",
      "score": "Fall Winner",
      "note": "Bermuda champion"
    }
  ],
  "sources": [
    {
      "name": "PGA Tour Official: The RSM Classic Tournament Field and Preview",
      "url": "https://www.pgatour.com/tournaments/2026/the-rsm-classic/R2026493"
    },
    {
      "name": "Golf Channel: FedExCup Fall bubble watch entering Sea Island finale",
      "url": "https://www.golfchannel.com/news/rsm-classic-bubble-watch-2026"
    },
    {
      "name": "Sea Island Official: 2026 RSM Classic Event Details",
      "url": "https://www.seaisland.com/event/the-rsm-classic-2026/"
    }
  ]
}
open(rsm_path, "w", encoding="utf-8").write(json.dumps(rsm_data, indent=2, ensure_ascii=False) + "\n")
print("Created rsm-classic-sea-island match JSON.")

# 6. Update las-vegas-gp-strip-2026.json
vegas_path = os.path.join(MATCHES, "las-vegas-gp-strip-2026.json")
vegas_data = json.load(open(vegas_path, "r", encoding="utf-8"))
vegas_data["headline"] = "Two days to Round 21 Las Vegas: Strip setup finishes as five-driver battle for P2 heats up"
vegas_data["roundLabel"] = "Round 21 · Two Days to Las Vegas"
vegas_data["teaser"] = "The Las Vegas Strip is ready for action with two days until Thursday night practice: 33 points cover Max Verstappen through Lando Norris in the fight for championship runner-up behind Kimi Antonelli."
vegas_data["whyCareReason"] = "Formula 1 descends on Nevada with 33 points covering Verstappen (279) to Norris (246) across the final three rounds, while Ferrari defends P2 constructors from Red Bull and McLaren."
open(vegas_path, "w", encoding="utf-8").write(json.dumps(vegas_data, indent=2, ensure_ascii=False) + "\n")
print("Updated las-vegas-gp match JSON.")

