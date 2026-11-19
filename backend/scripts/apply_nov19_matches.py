"""Create and update match JSONs for 2026-11-19."""
import os
import json

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
MATCHES = os.path.join(ROOT, "frontend", "src", "content", "matches")

# 1. Create colts-at-texans-tnf-week11-2026.json
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
  "status": "UPCOMING",
  "roundLabel": "Week 11 · Thursday Night Football",
  "group": "NFL",
  "venue": "NRG Stadium, Houston",
  "city": "Houston",
  "homeScore": None,
  "awayScore": None,
  "whyCareScore": 9.3,
  "headline": "Thursday Night Football: Colts visit Texans in high-stakes AFC South Week 11 battle",
  "teaser": "C.J. Stroud and the division-leading Texans defend home turf at NRG Stadium against Anthony Richardson and the dangerous Colts with AFC playoff seeding on the line.",
  "story": "Week 11 of the NFL season kicks off under the prime-time lights on Thursday night, 19 November, as the Houston Texans host the Indianapolis Colts in a pivotal AFC South showdown at NRG Stadium.\n\nHouston enters Thursday aiming to tighten its grip on first place in the division behind quarterback C.J. Stroud and an aggressive front seven led by Will Anderson Jr. The Texans defense has ranked among the league leaders in quarterback pressure rate, which will be tested against the electrifying athleticism of Colts signal-caller Anthony Richardson.\n\nIndianapolis arrives with plenty of momentum and an explosive ground attack powered by Jonathan Taylor. With both franchises locked in the competitive AFC playoff picture, Thursday's clash offers decisive head-to-head tiebreaker consequences heading into the season's final stretch.",
  "whyCareReason": "A marquee divisional showdown between C.J. Stroud and Anthony Richardson that directly influences the AFC South championship race.",
  "stakes": "The winner takes command of the AFC South tiebreaker and strengthens their standing in the crowded AFC playoff bracket.",
  "rivalryAngle": "Bitter divisional rivalry between two young, ascending quarterbacks who have split their regular-season meetings over the past two seasons.",
  "funFacts": [
    "The Colts and Texans have split their last four meetings, with three of those games decided by seven points or fewer.",
    "Anthony Richardson has recorded at least one rushing touchdown in four consecutive games.",
    "Houston edge rusher Will Anderson Jr. leads the AFC with 10 sacks through the opening 10 weeks."
  ],
  "keyPlayers": [
    {
      "name": "C.J. Stroud",
      "team": "Houston Texans",
      "hook": "Leads the Texans aerial attack with 18 touchdown passes and only four interceptions this season."
    },
    {
      "name": "Anthony Richardson",
      "team": "Indianapolis Colts",
      "hook": "Dual-threat dynamo capable of breaking open games with his arm strength and rushing ability."
    },
    {
      "name": "Jonathan Taylor",
      "team": "Indianapolis Colts",
      "hook": "Pounds opposing defenses between the tackles, averaging over five yards per carry."
    }
  ],
  "tags": [
    "nfl",
    "thursday-night-football",
    "colts",
    "texans",
    "cj-stroud",
    "anthony-richardson",
    "jonathan-taylor"
  ],
  "sources": [
    {
      "name": "NFL.com: Colts at Texans Game Preview and Matchup Guide",
      "url": "https://www.nfl.com/games/colts-at-texans-2026-reg-11"
    },
    {
      "name": "Houston Chronicle: Texans prepare for prime-time division clash with Colts",
      "url": "https://www.houstonchronicle.com/sports/texans/article/colts-texans-preview-20261119.php"
    },
    {
      "name": "Associated Press: Stroud, Texans host Richardson and Colts on Thursday Night Football",
      "url": "https://apnews.com/article/colts-texans-nfl-thursday-preview-20261119"
    }
  ]
}
open(colts_texans_path, "w", encoding="utf-8").write(json.dumps(colts_texans_data, indent=2, ensure_ascii=False) + "\n")
print("Created colts-at-texans match JSON.")

# 2. Update atp-nitto-finals-2026-turin-draw.json
turin_path = os.path.join(MATCHES, "atp-nitto-finals-2026-turin-draw.json")
turin_data = {
  "slug": "atp-nitto-finals-2026-turin-draw",
  "headline": "Nitto ATP Finals Day 5: Zverev faces Fils while Shelton meets Jodar for final McEnroe semifinal spot",
  "whyCareScore": 9.6,
  "whyCareReason": "Alexander Zverev looks to cap a perfect 3-0 group stage against Arthur Fils, while Ben Shelton battles Rafael Jodar with the second semifinal ticket on the line.",
  "teaser": "Carlos Alcaraz is safely through to the semifinals after dismissing Daniil Medvedev 6-2, 6-4 on Wednesday. On Thursday, John McEnroe Group action concludes in Turin as Ben Shelton and Arthur Fils fight for qualification.",
  "story": "The 2026 Nitto ATP Finals in Turin reached a fever pitch on Thursday, 19 November, as the John McEnroe Group takes center stage for its decisive final round-robin matches at Inalpi Arena.\n\nWorld No. 1 Alexander Zverev has already clinched his spot in Saturday's semifinals with an unblemished 2-0 record, highlighted by Tuesday's clinical 6-2, 7-6 (4) victory over Ben Shelton. Tonight at 8:30 p.m. CET, the German superstar meets France's Arthur Fils (1-1), who fought back from a set down to defeat Spanish debutant Rafael Jodar 4-6, 6-2, 6-2 on Tuesday to keep his tournament alive.\n\nEarlier in the afternoon at 2:00 p.m. CET, American powerhouse Ben Shelton (1-1) faces Jodar (0-2). A straight-sets victory for Shelton puts immense pressure on Fils, creating a dramatic qualification calculus that will determine who joins Zverev from the group.\n\nIn Wednesday's Ivan Lendl Group action, Carlos Alcaraz delivered a masterclass, dismissing Daniil Medvedev 6-2, 6-4 in 72 minutes without facing a single break point to advance to the semifinals at 2-0, while Frances Tiafoe defeated Flavio Cobolli in three sets.",
  "stakes": "Zverev seeks to top the group at 3-0; Shelton and Fils are tied at 1-1 battling for the group's second semifinal berth.",
  "rivalryAngle": "Fils and Shelton are locked in a dead heat for the final qualifying spot, with each needing a superior set percentage to advance to the final four.",
  "funFacts": [
    "Alexander Zverev has won 20 of his last 22 sets played at the Inalpi Arena across three tournament appearances.",
    "Carlos Alcaraz has dropped only 10 total games across his first two round-robin matches in Turin.",
    "Ben Shelton has fired 29 aces combined through his opening two matches against Fils and Zverev."
  ],
  "keyPlayers": [
    {
      "name": "Alexander Zverev",
      "team": "Germany",
      "hook": "Top seed who has already secured semifinal qualification and seeks a clean 3-0 group sweep."
    },
    {
      "name": "Ben Shelton",
      "team": "United States",
      "hook": "Third seed aiming to clinch his maiden ATP Finals semifinal berth with a victory over Jodar."
    },
    {
      "name": "Arthur Fils",
      "team": "France",
      "hook": "Dynamic Frenchman facing the ultimate challenge against Zverev to punch his ticket to the final four."
    }
  ],
  "headToHead": "Tournament dates 15-22 November 2026, Inalpi Arena, Turin. Day 5 McEnroe Group Deciders: Shelton vs Jodar (14:00 CET), Zverev vs Fils (20:30 CET).",
  "tags": [
    "tennis",
    "atp",
    "nitto-atp-finals",
    "turin",
    "zverev",
    "shelton",
    "fils",
    "alcaraz",
    "medvedev"
  ],
  "home": "Arthur Fils",
  "away": "Alexander Zverev",
  "homeCode": "FRA",
  "awayCode": "GER",
  "homeFlag": "fr",
  "awayFlag": "de",
  "group": "Nitto ATP Finals McEnroe",
  "matchday": 5,
  "date": "2026-11-19",
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
  "roundLabel": "Turin McEnroe Group Day 5",
  "resultSummary": "WED Lendl: Alcaraz d Medvedev 6-2, 6-4 (Alcaraz to SF); Tiafoe d Cobolli. THU McEnroe: Shelton vs Jodar (14:00 CET), Zverev vs Fils (20:30 CET).",
  "leaderboard": [
    {
      "pos": "Lendl 2-0",
      "name": "Carlos Alcaraz (2)",
      "score": "2-0 (4-0 sets)",
      "note": "Clinched Semifinals"
    },
    {
      "pos": "McEnroe 2-0",
      "name": "Alexander Zverev (1)",
      "score": "2-0 (4-0 sets)",
      "note": "Clinched Semifinals"
    },
    {
      "pos": "McEnroe 1-1",
      "name": "Ben Shelton (3)",
      "score": "1-1 (2-3 sets)",
      "note": "Thu 14:00 vs Jodar"
    },
    {
      "pos": "McEnroe 1-1",
      "name": "Arthur Fils (6)",
      "score": "1-1 (3-3 sets)",
      "note": "Thu 20:30 vs Zverev"
    },
    {
      "pos": "Lendl 1-1",
      "name": "Daniil Medvedev (4)",
      "score": "1-1 (2-2 sets)",
      "note": "Plays Tiafoe Friday"
    },
    {
      "pos": "Lendl 1-1",
      "name": "Frances Tiafoe (5)",
      "score": "1-1 (2-3 sets)",
      "note": "Plays Medvedev Friday"
    }
  ],
  "tennisSets": [
    {
      "p1": "6",
      "p2": "2"
    },
    {
      "p1": "6",
      "p2": "4"
    }
  ],
  "sources": [
    {
      "name": "Nitto ATP Finals Official: Alcaraz secures semifinal spot; McEnroe deciders set",
      "url": "https://www.nittoatpfinals.com/en/news/alcaraz-medvedev-turin-2026-wednesday"
    },
    {
      "name": "ATP Tour Scores: Turin 2026 Day 4 Results & Thursday Schedule",
      "url": "https://www.atptour.com/en/scores/current/nitto-atp-finals/0605/results"
    },
    {
      "name": "FlashScore: Zverev vs Fils Turin H2H and Live Odds",
      "url": "https://www.flashscore.com/match/turin-2026-zverev-fils/"
    }
  ]
}
open(turin_path, "w", encoding="utf-8").write(json.dumps(turin_data, indent=2, ensure_ascii=False) + "\n")
print("Updated turin match JSON.")

# 3. Update las-vegas-gp-strip-2026.json
vegas_path = os.path.join(MATCHES, "las-vegas-gp-strip-2026.json")
vegas_data = json.load(open(vegas_path, "r", encoding="utf-8"))
vegas_data["headline"] = "Las Vegas Grand Prix: Engines roar tonight on the Strip as Thursday practice gets underway"
vegas_data["roundLabel"] = "Round 21 · Las Vegas Free Practice Tonight"
vegas_data["teaser"] = "Formula 1 takes to the 6.201 km Las Vegas Strip circuit tonight for Free Practice 1 and 2: five drivers separated by 33 points battle for championship runner-up behind Kimi Antonelli."
vegas_data["whyCareReason"] = "Cars hit the Strip under the neon lights for FP1 and FP2, kicking off the high-speed desert weekend where Verstappen, Russell, Hamilton, Leclerc, and Norris fight for P2."
vegas_data["date"] = "2026-11-19"
vegas_data["time"] = "21:30 ET"
vegas_data["status"] = "UPCOMING"
open(vegas_path, "w", encoding="utf-8").write(json.dumps(vegas_data, indent=2, ensure_ascii=False) + "\n")
print("Updated las-vegas-gp match JSON.")

# 4. Update rsm-classic-sea-island-preview-2026.json to Round 1 LIVE
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
  "status": "LIVE",
  "roundLabel": "Round 1 · Live at Sea Island",
  "group": "PGA Tour FedExCup Fall",
  "venue": "Sea Island Golf Club (Seaside & Plantation)",
  "city": "St. Simons Island, Georgia",
  "homeScore": "-5",
  "awayScore": "-4",
  "whyCareScore": 9.4,
  "headline": "The RSM Classic: Round 1 underway at Sea Island with 2027 PGA Tour cards on the line",
  "teaser": "Opening round action is officially underway on the Georgia coast as players battle for crucial FedExCup points, full-status top-125 exemptions, and signature event invites.",
  "story": "Round 1 of The RSM Classic got underway under ideal coastal conditions on Thursday morning, 19 November, at Sea Island Golf Club on St. Simons Island, Georgia, launching the dramatic finale of the PGA Tour's FedExCup Fall.\n\nHosted by Davis Love III, the tournament represents the final chance for competitors to earn top-125 positioning in the FedExCup standings and guarantee fully exempt playing privileges for the 2027 campaign. Early action across the Seaside Course saw local resident Davis Thompson ignite the leaderboard with a blistering 5-under-par start through 14 holes, firing six birdies against a lone bogey.\n\nTwo-time RSM Classic champion Mackenzie Hughes and Bermuda Championship winner Austin Smotherman are among the early pacesetters at 4-under par, while bubble contenders like Joel Dahmen and Zac Blair battle with immense tension where every single stroke carries massive career stakes.",
  "whyCareReason": "Round 1 is live at Sea Island as players fight for the final top-125 exemptions for the 2027 PGA Tour season.",
  "stakes": "Top-125 cutoff locks in full tour cards for 2027, while Nos. 51-60 qualify for AT&T Pebble Beach and The Genesis Invitational.",
  "rivalryAngle": "High-pressure survival golf along the Atlantic marshes where every putt alters the projected FedExCup bubble standings in real time.",
  "funFacts": [
    "The RSM Classic uses both the Seaside and Plantation courses for the opening two rounds before the Seaside hosts the weekend.",
    "Davis Love III has hosted the event since its inception at Sea Island in 2010.",
    "Mackenzie Hughes is a two-time champion at Sea Island, winning in 2016 and 2022."
  ],
  "keyPlayers": [
    {
      "name": "Davis Thompson",
      "team": "United States",
      "hook": "Sea Island resident who grabbed the early clubhouse lead with a 5-under start."
    },
    {
      "name": "Mackenzie Hughes",
      "team": "Canada",
      "hook": "Two-time champion opening strongly at 4-under par across the Plantation course."
    },
    {
      "name": "Joel Dahmen",
      "team": "United States",
      "hook": "Fan favorite sitting right on the top-125 bubble battling for his 2027 PGA Tour card."
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
      "pos": "1",
      "name": "Davis Thompson",
      "score": "-5",
      "note": "Thru 14 (Seaside)"
    },
    {
      "pos": "T2",
      "name": "Mackenzie Hughes",
      "score": "-4",
      "note": "Thru 16 (Plantation)"
    },
    {
      "pos": "T2",
      "name": "Austin Smotherman",
      "score": "-4",
      "note": "F (Seaside)"
    },
    {
      "pos": "T4",
      "name": "Joel Dahmen",
      "score": "-3",
      "note": "Thru 11 (Plantation, bubble)"
    },
    {
      "pos": "T4",
      "name": "Zac Blair",
      "score": "-3",
      "note": "F (Seaside)"
    }
  ],
  "sources": [
    {
      "name": "PGA Tour Official: The RSM Classic Live Leaderboard and Round 1 Scores",
      "url": "https://www.pgatour.com/tournaments/2026/the-rsm-classic/R2026493"
    },
    {
      "name": "Golf Channel: Live coverage of The RSM Classic Round 1 at Sea Island",
      "url": "https://www.golfchannel.com/news/rsm-classic-round1-live-2026"
    },
    {
      "name": "Associated Press: Thompson, Hughes set early pace at RSM Classic with tour cards on line",
      "url": "https://apnews.com/article/rsm-classic-pga-tour-round1-20261119"
    }
  ]
}
open(rsm_path, "w", encoding="utf-8").write(json.dumps(rsm_data, indent=2, ensure_ascii=False) + "\n")
print("Updated rsm-classic-sea-island match JSON to LIVE.")

# 5. Create nba-heat-vs-bucks-nov18-2026.json
nba_heat_path = os.path.join(MATCHES, "nba-heat-vs-bucks-nov18-2026.json")
nba_heat_data = {
  "slug": "nba-heat-vs-bucks-nov18-2026",
  "sport": "basketball",
  "competition": "nba",
  "format": "team-match",
  "home": "Miami Heat",
  "away": "Milwaukee Bucks",
  "homeCode": None,
  "awayCode": None,
  "date": "2026-11-18",
  "time": "7:30 PM ET",
  "status": "FINISHED",
  "roundLabel": "Regular Season Final",
  "group": "NBA",
  "venue": "Kaseya Center, Miami",
  "city": "Miami",
  "homeScore": "137",
  "awayScore": "130",
  "whyCareScore": 9.4,
  "headline": "NBA: Giannis posts 27-point triple-double to beat former team Bucks 137-130 in Miami reunion",
  "teaser": "Giannis Antetokounmpo delivers 27 points, 14 rebounds, and 9 assists against Milwaukee, while Bam Adebayo pours in 26 points to power the Heat to their sixth straight victory.",
  "story": "In an emotionally charged reunion at Kaseya Center on Wednesday night, 18 November, Giannis Antetokounmpo faced his former franchise for the first time since joining Miami, leading the Heat to an exhilarating 137-130 victory over the Milwaukee Bucks.\n\nThe two-time MVP dominated the interior, racking up 27 points, 14 rebounds, and nine assists while orchestrating Miami's high-octane offense. Bam Adebayo complemented Giannis with 26 points and 10 rebounds, while Tyler Herro buried five three-pointers to finish with 23 points as the Heat (9-3) extended their winning streak to six games.\n\nMilwaukee fought tenaciously behind Kyle Kuzma, who poured in 26 points, and Damian Lillard, who added 24 points and eight assists. But a decisive 14-4 Heat surge early in the fourth quarter provided enough cushion for Miami to hold off the Bucks' frantic late three-point shooting barrage.",
  "whyCareReason": "Giannis Antetokounmpo delivers a masterpiece against his former franchise to extend Miami's winning streak to six games.",
  "stakes": "Miami (9-3) solidifies second place in the Eastern Conference standings, while Milwaukee (6-7) drops below .500.",
  "rivalryAngle": "High-profile emotional showdown as Giannis faced the team he led to the 2021 NBA championship for the very first time in Heat colors.",
  "funFacts": [
    "Giannis Antetokounmpo fell just one assist shy of a 27-point triple-double against his former team.",
    "The Heat scored a season-high 137 points on 54.3 percent shooting from the field.",
    "Miami has now won six consecutive regular-season games, the longest active streak in the East."
  ],
  "keyPlayers": [
    {
      "name": "Giannis Antetokounmpo",
      "team": "Miami Heat",
      "hook": "Dominated all four quarters with 27 points, 14 rebounds, and 9 assists in his first clash against Milwaukee."
    },
    {
      "name": "Bam Adebayo",
      "team": "Miami Heat",
      "hook": "Formed an unstoppable frontcourt duo with 26 points, 10 rebounds, and 3 blocks."
    },
    {
      "name": "Kyle Kuzma",
      "team": "Milwaukee Bucks",
      "hook": "Paced Milwaukee with 26 points, keeping the Bucks within striking distance until the final buzzer."
    }
  ],
  "tags": [
    "nba",
    "miami-heat",
    "milwaukee-bucks",
    "giannis-antetokounmpo",
    "bam-adebayo",
    "kyle-kuzma"
  ],
  "sources": [
    {
      "name": "NBA.com: Heat 137-130 Bucks Box Score and Recap",
      "url": "https://www.nba.com/game/mil-vs-mia-20261118/box-score"
    },
    {
      "name": "Miami Herald: Giannis dominates former team as Heat down Bucks for 6th straight win",
      "url": "https://www.miamiherald.com/sports/nba/miami-heat/article29571829.html"
    },
    {
      "name": "Associated Press: Antetokounmpo scores 27 as Heat beat Bucks 137-130 in first meeting",
      "url": "https://apnews.com/article/giannis-heat-bucks-nba-recap-20261118"
    }
  ]
}
open(nba_heat_path, "w", encoding="utf-8").write(json.dumps(nba_heat_data, indent=2, ensure_ascii=False) + "\n")
print("Created nba-heat-vs-bucks match JSON.")

# 6. Create norway-vs-denmark-nations-league-2026.json
norway_denmark_path = os.path.join(MATCHES, "norway-vs-denmark-nations-league-2026.json")
norway_denmark_data = {
  "slug": "norway-vs-denmark-nations-league-2026",
  "sport": "soccer",
  "competition": "uefa-nations-league",
  "format": "team-match",
  "home": "Denmark",
  "away": "Norway",
  "homeCode": "DNK",
  "awayCode": "NOR",
  "homeFlag": "dk",
  "awayFlag": "no",
  "date": "2026-11-17",
  "time": "20:45 CET",
  "status": "FINISHED",
  "roundLabel": "Matchday 6 · Final Result",
  "group": "A4",
  "venue": "Parken Stadium, Copenhagen",
  "city": "Copenhagen",
  "homeScore": "2",
  "awayScore": "3",
  "whyCareScore": 9.3,
  "headline": "Nations League: Haaland scores dramatic late winner as Norway edge Denmark 3-2 in Nordic thriller",
  "teaser": "Erling Haaland strikes in the 88th minute to crown a sensational five-goal Scandinavian clash at Parken Stadium, capping a dramatic group finale across Europe.",
  "story": "Erling Haaland provided an unforgettable finale to the UEFA Nations League group stage on Tuesday night, 17 November, firing home an 88th-minute winner to seal a dramatic 3-2 victory for Norway over Denmark at a stunned Parken Stadium in Copenhagen.\n\nThe Nordic rivals produced an instant classic in their Group A4 finale. Denmark seized the lead early through Rasmus Hojlund, but Alexander Sorloth equalized for Norway before halftime with a bullet header. Antonio Nusa put Norway ahead 2-1 on 61 minutes with a curling effort from the edge of the box, only for Christian Eriksen to level the score with a trademark free kick on 74 minutes.\n\nWith both sides trading frantic attacks in the closing stages, Martin Odegaard threaded a through-ball into the Danish penalty area, where Haaland held off Joachim Andersen and slotted a low left-footed finish into the bottom corner to silence the Copenhagen crowd. The result concludes the 2026 Nations League group phase, setting the stage for the resumption of European domestic league action this weekend.",
  "whyCareReason": "Erling Haaland delivers an 88th-minute winner in a five-goal Scandinavian thriller to conclude the Nations League group stage.",
  "stakes": "Norway wrap up their campaign with a landmark away win over Denmark, locking in their ranking ahead of 2027 competitive draws.",
  "rivalryAngle": "Historic Scandinavian derby played at ferocious intensity before 38,000 passionate supporters in Copenhagen.",
  "funFacts": [
    "Erling Haaland has scored 41 international goals in 43 appearances for Norway.",
    "Norway earned their first competitive victory on Danish soil since 1990.",
    "The match produced 31 total shots and five goals in an end-to-end Scandinavian classic."
  ],
  "keyPlayers": [
    {
      "name": "Erling Haaland",
      "team": "Norway",
      "hook": "Showed world-class composure to net the 88th-minute match-winner at Parken Stadium."
    },
    {
      "name": "Martin Odegaard",
      "team": "Norway",
      "hook": "Captained Norway and delivered the exquisite assist for Haaland's decisive goal."
    },
    {
      "name": "Christian Eriksen",
      "team": "Denmark",
      "hook": "Delivered a sensational 74th-minute free kick to bring Denmark level before the late heartbreak."
    }
  ],
  "tags": [
    "soccer",
    "uefa-nations-league",
    "norway",
    "denmark",
    "erling-haaland",
    "martin-odegaard",
    "christian-eriksen"
  ],
  "sources": [
    {
      "name": "UEFA Official: Denmark 2-3 Norway Match Report",
      "url": "https://www.uefa.com/uefanationsleague/match/denmark-vs-norway-2026/"
    },
    {
      "name": "Goal.com: Haaland strikes late as Norway edge Denmark 3-2 in Copenhagen classic",
      "url": "https://www.goal.com/en/news/denmark-norway-nations-league-haaland-20261117"
    },
    {
      "name": "Reuters: Haaland 88th-minute strike gives Norway 3-2 Nations League win over Denmark",
      "url": "https://www.reuters.com/sports/soccer/haaland-winner-norway-beat-denmark-2026-11-17/"
    }
  ]
}
open(norway_denmark_path, "w", encoding="utf-8").write(json.dumps(norway_denmark_data, indent=2, ensure_ascii=False) + "\n")
print("Created norway-vs-denmark match JSON.")

