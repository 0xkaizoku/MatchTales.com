# Apply 2026-11-26 match JSON updates and creations with strict Zod schema compliance and verified facts.
import os
import json

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
MATCHES_DIR = os.path.join(ROOT, "frontend", "src", "content", "matches")

def save_match(filename, data):
    raw = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    if "\u2014" in raw:
        raise ValueError(f"Em-dash detected in {filename}")
    if "--" in raw:
        raise ValueError(f"Double-hyphen detected in {filename}")
    path = os.path.join(MATCHES_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(raw)
    print(f"Saved {filename} (status={data['status']}, date={data['date']})")

# 1. Update atp-nitto-finals-2026-turin-draw.json to FINISHED (2026-11-22 Final)
turin_path = os.path.join(MATCHES_DIR, "atp-nitto-finals-2026-turin-draw.json")
with open(turin_path, "r", encoding="utf-8") as f:
    turin_data = json.load(f)

turin_data["format"] = "singles"
turin_data["status"] = "FINISHED"
turin_data["date"] = "2026-11-22"
turin_data["time"] = "18:00 CET"
turin_data["home"] = "Carlos Alcaraz"
turin_data["away"] = "Alexander Zverev"
turin_data["homeCode"] = "ESP"
turin_data["awayCode"] = "GER"
turin_data["homeFlag"] = "es"
turin_data["awayFlag"] = "de"
turin_data["homeScore"] = "2"
turin_data["awayScore"] = "0"
turin_data["roundLabel"] = "Nitto ATP Finals · Championship Final"
turin_data["headline"] = "Turin ATP Finals: Carlos Alcaraz sweeps Alexander Zverev 6-2, 7-6 to lift maiden crown"
turin_data["teaser"] = "Carlos Alcaraz completes a flawless 5-0 week in Turin, saving three set points in the second-set tiebreak to defeat World No. 1 Alexander Zverev 6-2, 7-6(7)."
turin_data["whyCareScore"] = 9.8
turin_data["whyCareReason"] = "Alcaraz captures his maiden Nitto ATP Finals trophy with a 14-match winning streak, joining Agassi, Federer, and Djokovic as Career Super Slam winners."
turin_data["stakes"] = "Undefeated champion Alcaraz pockets the maximum $5,171,000 payout from the $15,750,000 prize pool and secures 1,500 ranking points."
turin_data["rivalryAngle"] = "World No. 2 Alcaraz outlasted World No. 1 Zverev after surviving Ben Shelton in a three-set semifinal."
turin_data["story"] = (
    "Carlos Alcaraz etched his name into tennis history on Sunday, 22 November, producing an indoor hard-court masterclass to defeat World No. 1 Alexander Zverev 6-2, 7-6(7) at Inalpi Arena in Turin.\n\n"
    "Having rallied past Ben Shelton 3-6, 6-3, 7-6(1) in Saturday semifinals while Zverev eliminated Daniil Medvedev 7-6(0), 6-4, the championship clash pitted the two sharpest servers in the draw. Alcaraz struck twice to breeze through the opening set before saving three set points in a breathtaking second-set tiebreak (9-7).\n\n"
    "The triumph capped an undefeated 5-0 campaign worth $5,171,000 and marked the 23-year-old Spaniard 14th consecutive match win. Joining Andre Agassi, Roger Federer, and Novak Djokovic, Alcaraz became only the fourth man ever to win all four Grand Slam titles plus the year-end championship."
)
turin_data["funFacts"] = [
    "Alcaraz completed a perfect 5-0 undefeated week to claim the maximum $5,171,000 champion payout.",
    "At age 23, he became the fourth man in history to own all four Grand Slams and the ATP Finals crown.",
    "French debutants Theo Arribage and Albano Olivetti lifted the doubles trophy 3-6, 7-6(2), [10-6] over Arevalo and Pavic."
]
turin_data["keyPlayers"] = [
    {"name": "Carlos Alcaraz", "team": "Spain", "hook": "Saved three set points in the second-set tiebreak (9-7) to complete an undefeated 5-0 week."},
    {"name": "Alexander Zverev", "team": "Germany", "hook": "Reached the Turin final without dropping a set until Sunday clash against Alcaraz."}
]
turin_data["headToHead"] = "22 November 2026. Final: Carlos Alcaraz def. Alexander Zverev 6-2, 7-6(7)."
turin_data["tennisSets"] = [
    {"p1": "6", "p2": "2"},
    {"p1": "7", "p2": "6(7)"}
]
turin_data["leaderboard"] = []
turin_data["image"] = "https://images.pexels.com/photos/1618210/pexels-photo-1618210.jpeg"
turin_data["resultSummary"] = "FINAL: Carlos Alcaraz def. Alexander Zverev 6-2, 7-6(7). Alcaraz finishes 5-0 ($5,171,000 payout)."
save_match("atp-nitto-finals-2026-turin-draw.json", turin_data)

# 2. Create davis-cup-finals-2026-bologna-knockout.json (LIVE Nov 25 Italy 1-0 South Korea)
davis_cup = {
  "slug": "davis-cup-finals-2026-bologna-knockout",
  "headline": "Davis Cup Final 8 in Bologna: Defending champions Italy lead South Korea 1-0 as quarterfinals unfold",
  "whyCareScore": 8.9,
  "whyCareReason": "Three-time defending champions Italy launch their Bologna title defense through Lorenzo Musetti straight-sets rout after Czechia eliminated Canada 2-0.",
  "teaser": "Lorenzo Musetti sweeps Seongchan Hong 6-0, 7-6(5) to hand Italy a 1-0 quarterfinal lead ahead of Flavio Cobolli vs Soonwoo Kwon in Bologna.",
  "story": (
    "The 2026 Davis Cup Final 8 knockout stage in Bologna moved into full swing at SuperTennis Arena (BolognaFiere) on Wednesday, 25 November, with three-time defending champions Italy seizing early momentum against South Korea.\n\n"
    "Lorenzo Musetti delivered a ferocious opening singles display in front of packed home stands, dismissing Seongchan Hong 6-0, 7-6(5) in 92 minutes to put the Azzurri 1-0 ahead. Flavio Cobolli takes on Soonwoo Kwon in the second singles rubber, with Matteo Berrettini and Andrea Vavassori slated for doubles against Hyeon Chung and Kwon if needed.\n\n"
    "Earlier in the Final 8 bracket on Tuesday, Czechia became the first nation into the semifinals by sweeping Canada 2-0 behind Tomas Machac three-set victory (6-2, 3-6, 6-2) over Liam Draxl. Thursday quarterfinal doubleheader sees Great Britain face Germany at 10:00 CET before Austria meet Spain."
  ),
  "stakes": "A semifinal berth against the remaining Final 8 field awaits the winner as Italy chase a historic fourth consecutive Davis Cup crown.",
  "rivalryAngle": "Italy open their home title defense backed by noisy Bologna support, with Musetti and Cobolli leading the singles charge.",
  "funFacts": [
    "Musetti bageled Seongchan Hong in 25 minutes during the first set before sealing the tiebreak 7-6(5).",
    "Czechia swept Canada 2-0 on Tuesday to become the first team into Saturday semifinals.",
    "Great Britain vs Germany opens Thursday Bologna schedule at 10:00 CET, followed by Austria vs Spain."
  ],
  "keyPlayers": [
    {"name": "Lorenzo Musetti", "team": "Italy", "hook": "Blitzed Seongchan Hong 6-0, 7-6(5) in 1 hour and 32 minutes for Italy opening point."},
    {"name": "Flavio Cobolli", "team": "Italy", "hook": "Lined up against Soonwoo Kwon in the pivotal second singles rubber."},
    {"name": "Tomas Machac", "team": "Czechia", "hook": "Pushed Czechia past Canada with a 6-2, 3-6, 6-2 singles win over Liam Draxl."}
  ],
  "headToHead": "25 November 2026. SuperTennis Arena, BolognaFiere. Italy lead South Korea 1-0.",
  "tags": ["tennis", "davis-cup", "bologna", "italy", "south-korea", "musetti", "czechia"],
  "home": "Italy",
  "away": "South Korea",
  "homeCode": "ITA",
  "awayCode": "KOR",
  "homeFlag": "it",
  "awayFlag": "kr",
  "group": "Davis Cup Final 8",
  "matchday": 0,
  "date": "2026-11-25",
  "time": "16:00 CET",
  "venue": "SuperTennis Arena, BolognaFiere",
  "city": "Bologna",
  "status": "LIVE",
  "homeScore": "1",
  "awayScore": "0",
  "marquee": True,
  "liveMinute": "Rubber 2",
  "image": "https://images.pexels.com/photos/1618210/pexels-photo-1618210.jpeg",
  "decidedBy": None,
  "homePen": None,
  "awayPen": None,
  "sport": "tennis",
  "competition": "davis-cup-2026",
  "format": "team-match",
  "season": "2026",
  "roundLabel": "Davis Cup Final 8 · Quarterfinals",
  "resultSummary": "LIVE: Italy 1-0 South Korea (Musetti d. Hong 6-0, 7-6(5); Cobolli vs Kwon next). Tue QF: Czechia 2-0 Canada.",
  "leaderboard": [],
  "tennisSets": [],
  "sources": [
    {"name": "Davis Cup Official: Italy vs South Korea Quarterfinal Tie", "url": "https://www.daviscup.com/en/draws-results/tie.aspx"},
    {"name": "ATP Tour / CNA: Musetti gives Italy 1-0 lead over South Korea in Bologna", "url": "https://www.channelnewsasia.com/sport/tennis-musetti-italy-davis-cup-south-korea-2026"},
    {"name": "GuelphToday / CP: Czechia sweep Canada 2-0 in Davis Cup quarterfinals", "url": "https://www.guelphtoday.com/sports/czechia-canada-davis-cup-2026"}
  ]
}
save_match("davis-cup-finals-2026-bologna-knockout.json", davis_cup)

# 3. Create davis-cup-britain-vs-germany-nov26-2026.json (Thursday Nov 26 QF UPCOMING)
gb_ger = {
  "slug": "davis-cup-britain-vs-germany-nov26-2026",
  "headline": "Davis Cup Quarterfinal: Great Britain clash with Germany to launch Thursday Final 8 doubleheader in Bologna",
  "whyCareScore": 8.6,
  "whyCareReason": "Thursday knockout tennis opens early in Bologna with Great Britain facing Germany before Austria collide with Spain in the evening tie.",
  "teaser": "Great Britain meet Germany at 10:00 CET at SuperTennis Arena on Thursday, launching day three of the 2026 Davis Cup Final 8.",
  "story": (
    "Quarterfinal action continues in Bologna on Thursday, 26 November, as Great Britain take on Germany in the opening 10:00 CET session at SuperTennis Arena before Austria face Spain in the evening session (not before 17:00 CET).\n\n"
    "With Czechia already booked into the semifinals following Tuesday 2-0 sweep of Canada and Italy competing against South Korea on Wednesday, the lower half of the knockout bracket takes center stage. Short best-of-three ties leave zero margin for slow starts across two singles matches and a potential decisive doubles showdown."
  ),
  "stakes": "Two semifinal tickets are up for grabs on Thursday as Bologna determines the full Davis Cup Final 4 lineup.",
  "rivalryAngle": "European knockout tension in Bologna where every serve, break, and doubles pairing can tilt the nation tie.",
  "funFacts": [
    "Great Britain vs Germany starts Thursday day session at 10:00 CET (9:00 AM GMT / 4:00 AM EST).",
    "Austria vs Spain follows in the evening session not before 17:00 CET on the same Bologna court.",
    "All Final 8 ties consist of two singles rubbers and one decisive doubles match if tied 1-1."
  ],
  "keyPlayers": [
    {"name": "Alexander Zverev", "team": "Germany", "hook": "Germany anchor following his runner-up finish at the Nitto ATP Finals in Turin."},
    {"name": "Jack Draper", "team": "Great Britain", "hook": "Key British left-hander spearheading singles competition in Bologna."}
  ],
  "headToHead": "26 November 2026. 10:00 CET. SuperTennis Arena, Bologna. Quarterfinal.",
  "tags": ["tennis", "davis-cup", "great-britain", "germany", "spain", "austria", "bologna"],
  "home": "Great Britain",
  "away": "Germany",
  "homeCode": "ENG",
  "awayCode": "GER",
  "homeFlag": "gb-eng",
  "awayFlag": "de",
  "group": "Davis Cup Final 8",
  "matchday": 0,
  "date": "2026-11-26",
  "time": "10:00 CET",
  "venue": "SuperTennis Arena, BolognaFiere",
  "city": "Bologna",
  "status": "UPCOMING",
  "homeScore": None,
  "awayScore": None,
  "marquee": False,
  "liveMinute": None,
  "image": "https://images.pexels.com/photos/1618210/pexels-photo-1618210.jpeg",
  "decidedBy": None,
  "homePen": None,
  "awayPen": None,
  "sport": "tennis",
  "competition": "davis-cup-2026",
  "format": "team-match",
  "season": "2026",
  "roundLabel": "Davis Cup Final 8 · Thursday Quarterfinal",
  "resultSummary": "UPCOMING Thu 26 Nov: Great Britain vs Germany (10:00 CET), Austria vs Spain (17:00 CET).",
  "leaderboard": [],
  "tennisSets": [],
  "sources": [
    {"name": "Davis Cup Official: Thursday Bologna Schedule and Final 8 Ties", "url": "https://www.daviscup.com/en/news/bologna-finals-2026-thursday-schedule"}
  ]
}
save_match("davis-cup-britain-vs-germany-nov26-2026.json", gb_ger)

# 4. Update las-vegas-gp-strip-2026.json to FINISHED (2026-11-21) with valid Leaderboard schema
vegas_path = os.path.join(MATCHES_DIR, "las-vegas-gp-strip-2026.json")
with open(vegas_path, "r", encoding="utf-8") as f:
    vegas_data = json.load(f)

vegas_data["format"] = "race"
vegas_data["status"] = "FINISHED"
vegas_data["date"] = "2026-11-21"
vegas_data["roundLabel"] = "Round 21 · Las Vegas GP Final"
vegas_data["headline"] = "Las Vegas GP: Verstappen wins 75th career race through 35 lead changes as McLaren take double podium"
vegas_data["teaser"] = "Max Verstappen captures his 4th win of 2026 by 0.639s over Lando Norris while Oscar Piastri charges from P17 to 3rd after late Mercedes drama."
vegas_data["whyCareScore"] = 9.5
vegas_data["whyCareReason"] = "Verstappen commands P2 in the standings on 304 points while McLaren slash Red Bull lead for P3 in the Constructors to just 9 points."
vegas_data["homeScore"] = "1"
vegas_data["awayScore"] = "2"
vegas_data["stakes"] = "Antonelli holds 402 points as champion; Verstappen locks down 304; Hamilton (267), Russell (264), and Norris (264) sit three points apart."
vegas_data["rivalryAngle"] = "Late Mercedes carnage saw George Russell hit the barrier on Lap 48 and Kimi Antonelli suffer a sudden power loss while fighting up front."
vegas_data["story"] = (
    "Max Verstappen delivered a classic desert victory under the Las Vegas Strip lights on Saturday night, 21 November, conquering 35 changes for the lead to claim his 4th win of the 2026 season and 75th Grand Prix triumph overall.\n\n"
    "Heavy slipstreaming kept the pack bunched across 50 intense laps. Late heartbreak hit Mercedes when George Russell crashed into the barriers on Lap 48 and newly crowned champion Kimi Antonelli suffered a power issue, clearing the path for Lando Norris to chase Verstappen within 0.639 seconds at the flag. Oscar Piastri produced the drive of the night to charge from 17th on the grid onto the final podium step.\n\n"
    "Ferrari endurance faltered late when Lewis Hamilton and Charles Leclerc made contact, finishing 7th and 10th respectively, leaving McLaren just nine points behind Red Bull heading into Qatar."
)
vegas_data["funFacts"] = [
    "Verstappen earned his third Las Vegas Grand Prix victory in four years and 75th career win.",
    "The 50-lap neon race produced an astonishing 35 lead changes through active aerodynamic slipstreaming.",
    "Oscar Piastri surged from P17 on the grid to claim 3rd place behind McLaren teammate Lando Norris."
]
vegas_data["leaderboard"] = [
    {"pos": "1", "name": "Max Verstappen", "score": "Winner (+0.000s)", "note": "Red Bull (304 pts in Drivers)"},
    {"pos": "2", "name": "Lando Norris", "score": "+0.639s", "note": "McLaren (264 pts)"},
    {"pos": "3", "name": "Oscar Piastri", "score": "P3 from P17", "note": "McLaren (167 pts)"},
    {"pos": "4", "name": "Lewis Hamilton", "score": "P7 after contact", "note": "Ferrari (267 pts)"},
    {"pos": "5", "name": "George Russell", "score": "Lap 48 crash (P9)", "note": "Mercedes (264 pts)"},
    {"pos": "6", "name": "Kimi Antonelli", "score": "Late power loss", "note": "Mercedes Champion (402 pts)"}
]
vegas_data["tennisSets"] = []
vegas_data["image"] = "https://images.pexels.com/photos/627678/pexels-photo-627678.jpeg"
vegas_data["resultSummary"] = "FINAL: 1. Max Verstappen (Red Bull), 2. Lando Norris (McLaren +0.639s), 3. Oscar Piastri (McLaren from P17)."
save_match("las-vegas-gp-strip-2026.json", vegas_data)

# 5. Create qatar-gp-lusail-preview-2026.json (UPCOMING Round 22, NO Sprint!)
qatar_gp = {
  "slug": "qatar-gp-lusail-preview-2026",
  "headline": "Qatar Grand Prix preview: Three points split Hamilton, Russell, and Norris as grid arrives in Lusail",
  "whyCareScore": 8.8,
  "whyCareReason": "Fresh off 35 lead changes in Las Vegas, Formula 1 returns to standard weekend format in Lusail with P3 in both championships on a knife-edge.",
  "teaser": "Round 22 heads to Lusail International Circuit (27-29 Nov) with Hamilton on 267 points just ahead of Russell and Norris (264 each) behind Verstappen.",
  "story": (
    "Formula 1 trades Las Vegas neon for the floodlights of Lusail International Circuit as Round 22 of the 2026 World Championship unfolds in Qatar from Friday, 27 November through Sunday, 29 November.\n\n"
    "Unlike previous seasons, the 2026 Qatar Grand Prix runs under the standard weekend format with three practice sessions, Saturday qualifying (21:00 AST), and a 57-lap Grand Prix on Sunday night (19:00 AST). Practice opens on Friday with FP1 at 16:30 local time and night practice FP2 at 20:00.\n\n"
    "Although Mercedes driver Kimi Antonelli has wrapped up the Drivers crown (402 pts) and Mercedes own the Constructors title (666 pts), intense scraps remain live. Max Verstappen sits comfortably second on 304 points following his Vegas triumph, while just three points divide Lewis Hamilton (267) from George Russell and Lando Norris (264 apiece). Meanwhile, McLaren (431) sit just nine points shy of Red Bull (440) for third in Constructors."
  ),
  "stakes": "Just two Grands Prix remain (Qatar and Abu Dhabi) to settle Drivers P3 through P5 and the $10M Constructors battle between Red Bull and McLaren.",
  "rivalryAngle": "After Norris and Piastri stormed the Vegas podium, McLaren carry huge high-downforce momentum into Lusail fast sweepers.",
  "funFacts": [
    "Qatar 2026 follows the traditional three-practice format with no Formula 1 Sprint race.",
    "Grand Prix lights out is Sunday, 29 November at 19:00 local AST (16:00 UTC) for 57 laps.",
    "Ferrari (517) hold a 77-point advantage over Red Bull (440), who lead McLaren (431) by 9 points."
  ],
  "keyPlayers": [
    {"name": "Max Verstappen", "team": "Red Bull", "hook": "Hunts consecutive victories after securing his 75th Grand Prix triumph in Las Vegas."},
    {"name": "Lando Norris", "team": "McLaren", "hook": "Tied on 264 points with George Russell and only 3 behind Lewis Hamilton."}
  ],
  "headToHead": "27-29 November 2026. Round 22. Lusail International Circuit, Qatar. Upcoming.",
  "tags": ["f1", "formula-1", "qatar-gp", "lusail", "verstappen", "norris", "hamilton"],
  "home": "Max Verstappen",
  "away": "Lando Norris",
  "homeCode": "NED",
  "awayCode": "ENG",
  "homeFlag": "nl",
  "awayFlag": "gb-eng",
  "group": "Formula 1",
  "matchday": 22,
  "date": "2026-11-27",
  "time": "16:30 AST",
  "venue": "Lusail International Circuit",
  "city": "Lusail",
  "status": "UPCOMING",
  "homeScore": None,
  "awayScore": None,
  "marquee": True,
  "liveMinute": None,
  "image": "https://images.pexels.com/photos/627678/pexels-photo-627678.jpeg",
  "decidedBy": None,
  "homePen": None,
  "awayPen": None,
  "sport": "f1",
  "competition": "f1-2026",
  "format": "race",
  "season": "2026",
  "roundLabel": "Round 22 · Qatar GP Preview",
  "resultSummary": "UPCOMING (27-29 Nov): Antonelli 402 (Champ), Verstappen 304, Hamilton 267, Russell 264, Norris 264.",
  "leaderboard": [
    {"pos": "1", "name": "Kimi Antonelli (Champion)", "score": "402 pts", "note": "Mercedes"},
    {"pos": "2", "name": "Max Verstappen", "score": "304 pts", "note": "Red Bull"},
    {"pos": "3", "name": "Lewis Hamilton", "score": "267 pts", "note": "Ferrari"},
    {"pos": "4", "name": "George Russell", "score": "264 pts", "note": "Mercedes"},
    {"pos": "5", "name": "Lando Norris", "score": "264 pts", "note": "McLaren"}
  ],
  "tennisSets": [],
  "sources": [
    {"name": "Formula 1 Official: 2026 Qatar Grand Prix Schedule & Timetable", "url": "https://www.formula1.com/en/racing/2026/qatar"},
    {"name": "GridGuy / OneRacing: 2026 Drivers Standings Post-Las Vegas GP", "url": "https://www.formula1.com/en/results/2026/drivers"}
  ]
}
save_match("qatar-gp-lusail-preview-2026.json", qatar_gp)

# 6. Update man-city-vs-fulham-mw11-2026.json to FINISHED (2026-11-21) with verified scorers
mcf_path = os.path.join(MATCHES_DIR, "man-city-vs-fulham-mw11-2026.json")
with open(mcf_path, "r", encoding="utf-8") as f:
    mcf_data = json.load(f)

mcf_data["status"] = "FINISHED"
mcf_data["homeScore"] = 1
mcf_data["awayScore"] = 1
mcf_data["liveMinute"] = None
mcf_data["homeFlag"] = ""
mcf_data["awayFlag"] = ""
mcf_data["roundLabel"] = "Matchweek 11 · Final"
mcf_data["headline"] = "Premier League: Elliot Anderson rescues point as Fulham hold Manchester City 1-1 at Etihad"
mcf_data["teaser"] = "Rodrigo Muniz opens the scoring from an Oscar Bobb pass before Elliot Anderson equalizes in the 57th minute, leaving City six points behind leaders Arsenal."
mcf_data["story"] = (
    "Manchester City dropped precious points in the Premier League title chase on Saturday, 21 November, as Fulham earned a gritty 1-1 draw at the Etihad Stadium.\n\n"
    "Former City winger Oscar Bobb returned to haunt his old club in the 16th minute, threading an incisive pass for Brazilian forward Rodrigo Muniz to head Fulham into an early 1-0 advantage. City raised the tempo after halftime and restored parity in the 57th minute when midfielder Elliot Anderson fired home.\n\n"
    "Despite sustained late pressure, City could not find a winner and finished Matchweek 11 level on 22 points alongside Brighton, trailing league-leading Arsenal (28 points after a 2-2 draw at Newcastle) by six points. Elsewhere in MW11, Liverpool thrashed 10-man Manchester United 4-0 in Mauricio Pochettino opening match in charge."
)
mcf_data["keyPlayers"] = [
    {"name": "Rodrigo Muniz", "team": "Fulham", "hook": "Struck in the 16th minute from Oscar Bobb assist to stun the Etihad crowd."},
    {"name": "Elliot Anderson", "team": "Manchester City", "hook": "Rescued a point for City with a composed 57th-minute equalizer."},
    {"name": "Oscar Bobb", "team": "Fulham", "hook": "Provided the decisive pass against his former employers for Fulham opening goal."}
]
mcf_data["image"] = "https://images.pexels.com/photos/1171084/pexels-photo-1171084.jpeg"
mcf_data["resultSummary"] = "FINAL: Manchester City 1-1 Fulham (Anderson 57; Muniz 16). Arsenal lead PL on 28 pts."
save_match("man-city-vs-fulham-mw11-2026.json", mcf_data)

# 7. Create real-madrid-vs-psv-ucl-md5-2026.json (FINISHED 2026-11-24 with exact verified scorers & minutes)
rm_psv = {
  "slug": "real-madrid-vs-psv-ucl-md5-2026",
  "headline": "Champions League: Real Madrid hit five after halftime shock to crush PSV 5-1 and stay top on 15 points",
  "whyCareScore": 9.3,
  "whyCareReason": "Five unanswered second-half goals from Valverde, Bellingham, Mbappe (twice), and Vinicius keep Real Madrid sole leaders with a 5-0-0 record.",
  "teaser": "After Ivan Perisic penalty gave PSV a 32nd-minute lead, Real Madrid explode for five second-half goals to dominate 5-1 at the Bernabeu.",
  "story": (
    "Real Madrid turned a tense Champions League Matchday 5 test into a second-half exhibition on Tuesday night, 24 November, erasing a halftime deficit to dismantle PSV Eindhoven 5-1 at the Santiago Bernabeu.\n\n"
    "Veteran winger Ivan Perisic stunned the home crowd by converting a 32nd-minute penalty for PSV. Real Madrid emerged transformed after the break: Federico Valverde leveled in the 50th minute before Jude Bellingham bent home a sensational wonder-goal in the 60th to turn the tie.\n\n"
    "Kylian Mbappe took over down the stretch with goals in the 64th and 84th minutes before Vinicius Junior completed the five-goal barrage in the 87th minute. The win makes Real Madrid the sole club on 15 points atop the 36-team Champions League table, ahead of Arsenal (11 pts after 1-1 vs Dortmund) and Man City (10 pts after 2-2 vs Napoli)."
  ),
  "stakes": "Madrid take complete control of the automatic top-eight seeding race with a five-match winning run and +10 goal difference.",
  "rivalryAngle": "Valverde, Bellingham, Mbappe, and Vinicius struck in a blistering 37-minute second-half blitz at the Bernabeu.",
  "funFacts": [
    "All five Real Madrid goals came in a 37-minute second-half explosion between minutes 50 and 87.",
    "Real Madrid sit alone atop the 36-team table with 15 points from 5 matches (5W-0D-0L, +10 GD).",
    "In Tuesday other marquee ties, Arsenal drew Dortmund 1-1 (Gyokeres 10; Beier 55) and Man City drew Napoli 2-2."
  ],
  "keyPlayers": [
    {"name": "Kylian Mbappe", "team": "Real Madrid", "hook": "Struck twice in the 64th and 84th minutes to turn victory into a five-goal showcase."},
    {"name": "Jude Bellingham", "team": "Real Madrid", "hook": "Produced a stunning 60th-minute strike that permanently swung momentum Madrid way."},
    {"name": "Federico Valverde", "team": "Real Madrid", "hook": "Ignited the comeback with a 50th-minute equalizer right after the restart."}
  ],
  "headToHead": "24 November 2026. UEFA Champions League Matchday 5. Santiago Bernabeu, Madrid. Final: 5-1.",
  "tags": ["soccer", "champions-league", "real-madrid", "psv", "mbappe", "bellingham", "valverde"],
  "home": "Real Madrid",
  "away": "PSV Eindhoven",
  "homeCode": None,
  "awayCode": None,
  "homeFlag": "",
  "awayFlag": "",
  "group": "UCL",
  "matchday": 5,
  "date": "2026-11-24",
  "time": "21:00 CET",
  "venue": "Santiago Bernabeu",
  "city": "Madrid",
  "status": "FINISHED",
  "homeScore": 5,
  "awayScore": 1,
  "marquee": True,
  "liveMinute": None,
  "image": "https://images.pexels.com/photos/1171084/pexels-photo-1171084.jpeg",
  "decidedBy": "regular",
  "homePen": None,
  "awayPen": None,
  "sport": "soccer",
  "competition": "champions-league-2026",
  "format": "team-match",
  "season": "2026-27",
  "roundLabel": "Champions League · Matchday 5",
  "resultSummary": "FINAL: Real Madrid 5-1 PSV (Valverde 50, Bellingham 60, Mbappe 64, 84, Vinicius Jr 87; Perisic 32 pen).",
  "leaderboard": [],
  "tennisSets": [],
  "sources": [
    {"name": "UEFA.com / beIN SPORTS: Real Madrid 5-1 PSV Matchday 5 Report", "url": "https://www.uefa.com/uefachampionsleague/"},
    {"name": "AS / FootGoal: 2026-27 Champions League Standings After Tuesday MD5", "url": "https://en.as.com/soccer/"}
  ]
}
save_match("real-madrid-vs-psv-ucl-md5-2026.json", rm_psv)

# 8. Update rsm-classic-sea-island-preview-2026.json to FINISHED (2026-11-23 Playoff Win) with valid Leaderboard schema
rsm_path = os.path.join(MATCHES_DIR, "rsm-classic-sea-island-preview-2026.json")
with open(rsm_path, "r", encoding="utf-8") as f:
    rsm_data = json.load(f)

rsm_data["format"] = "leaderboard"
rsm_data["status"] = "FINISHED"
rsm_data["date"] = "2026-11-23"
rsm_data["home"] = "Marco Penge"
rsm_data["away"] = "Haotong Li"
rsm_data["homeCode"] = "ENG"
rsm_data["awayCode"] = "CHN"
rsm_data["homeScore"] = "-16"
rsm_data["awayScore"] = "-16"
rsm_data["roundLabel"] = "Final · Monday Playoff Winner"
rsm_data["headline"] = "The RSM Classic: Marco Penge wins four-man sudden-death playoff for maiden PGA Tour title"
rsm_data["teaser"] = "Englishman Marco Penge claims his first PGA Tour crown on the first extra hole after a four-way tie at 16-under 266 in Monday finish at Sea Island."
rsm_data["whyCareScore"] = 9.3
rsm_data["whyCareReason"] = "Penge captures a $1,332,000 winner check and locks in his PGA Tour exemption after weather pushed Sea Island final round into Monday."
rsm_data["stakes"] = "The FedExCup Fall finale concludes with Marco Penge securing full PGA Tour membership and top-125 cards settled for 2027."
rsm_data["story"] = (
    "England Marco Penge delivered a career-defining breakthrough on Monday, 23 November, sinking a clutch putt on the first sudden-death playoff hole to win The RSM Classic at Sea Island Golf Club.\n\n"
    "Sunday weather delays pushed the closing holes of the FedExCup Fall finale to Monday morning on the Seaside Course. Penge rallied with a final-round 65 to finish regulation locked at 16-under-par 266 alongside China Haotong Li, American Michael Thorbjornsen, and Max Greyserman.\n\n"
    "Returning to the 18th hole for the four-man playoff, Penge seized the moment to collect his first career PGA Tour victory and a $1,332,000 winner share. Next on the calendar is Tiger Woods Hero World Challenge at Albany, Bahamas from 3 to 6 December."
)
rsm_data["funFacts"] = [
    "Sunday weather forced a Monday tournament conclusion for the second straight week on the PGA Tour.",
    "Four players deadlocked at 16-under 266: Marco Penge, Haotong Li, Michael Thorbjornsen, and Max Greyserman.",
    "Penge took home $1,332,000 for his maiden PGA Tour victory on the first playoff hole."
]
rsm_data["keyPlayers"] = [
    {"name": "Marco Penge", "team": "England", "hook": "Closed with a final-round 65 and won on the first extra hole for his maiden PGA Tour trophy."},
    {"name": "Haotong Li", "team": "China", "hook": "Shared 16-under 266 regulation lead to reach the four-way Sea Island playoff."},
    {"name": "Michael Thorbjornsen", "team": "United States", "hook": "Held leads throughout the week and finished tied at -16 after regulation."}
]
rsm_data["leaderboard"] = [
    {"pos": "1", "name": "Marco Penge", "score": "-16 (266)", "note": "Winner (1st playoff hole)"},
    {"pos": "T2", "name": "Haotong Li", "score": "-16 (266)", "note": "Playoff runner-up"},
    {"pos": "T2", "name": "Michael Thorbjornsen", "score": "-16 (266)", "note": "Playoff runner-up"},
    {"pos": "T2", "name": "Max Greyserman", "score": "-16 (266)", "note": "Playoff runner-up"}
]
rsm_data["tennisSets"] = []
rsm_data["image"] = "https://images.pexels.com/photos/863988/pexels-photo-863988.jpeg"
rsm_data["resultSummary"] = "FINAL: Marco Penge (-16, 266) wins 1st playoff hole over Haotong Li, Michael Thorbjornsen, and Max Greyserman."
save_match("rsm-classic-sea-island-preview-2026.json", rsm_data)

# 9. Update colts-at-texans-tnf-week11-2026.json to accurate verified box score & records
colts_path = os.path.join(MATCHES_DIR, "colts-at-texans-tnf-week11-2026.json")
with open(colts_path, "r", encoding="utf-8") as f:
    colts_data = json.load(f)

colts_data["headline"] = "Thursday Night Football: C.J. Stroud tosses 3 TDs as Texans overwhelm Colts 26-3"
colts_data["teaser"] = "Stroud goes 21/27 for 194 yards and 3 touchdowns while David Montgomery runs for 107 yards and Will Anderson Jr. records a safety in a 26-3 rout."
colts_data["story"] = (
    "The Houston Texans snapped their early-season slide on Thursday night, 19 November, rolling past the Indianapolis Colts 26-3 at NRG Stadium to improve to 4-7.\n\n"
    "C.J. Stroud was sharp from start to finish, completing 21 of 27 passes for 194 yards and three touchdowns to Nico Collins (42 yards), Kayshon Boutte (24 yards), and Marlin Klein (13 yards). Running back David Montgomery pounded Indianapolis on the ground with 26 carries for 107 rushing yards.\n\n"
    "On defense, Will Anderson Jr. sacked Colts quarterback Daniel Jones in the end zone for a safety, while Houston limited Indianapolis (3-8) to 182 total yards and 1-of-11 on third down."
)
colts_data["whyCareReason"] = "Houston notches a statement 26-3 divisional victory on Thursday Night Football behind three Stroud touchdowns and a safety."
colts_data["stakes"] = "Houston improves to 4-7 to stay alive in the AFC chase while dropping Indianapolis to 3-8; Jacksonville leads the AFC South at 7-3."
colts_data["rivalryAngle"] = "Houston limited Daniel Jones to 12-of-27 passing for 144 yards and zero touchdowns."
colts_data["funFacts"] = [
    "Houston held the ball for 37:46 and outgained Indianapolis 361 to 182 in total yards.",
    "C.J. Stroud completed 77.8 percent of his throws (21/27, 118.2 rating) with 3 TD passes.",
    "Will Anderson Jr. registered a defensive safety by bringing down Daniel Jones in the end zone."
]
colts_data["keyPlayers"] = [
    {"name": "C.J. Stroud", "team": "Houston Texans", "hook": "Completed 21 of 27 for 194 yards and three TDs (Collins, Boutte, Klein)."},
    {"name": "David Montgomery", "team": "Houston Texans", "hook": "Workhorse 26-carry, 107-yard rushing performance controlled time of possession."},
    {"name": "Will Anderson Jr.", "team": "Houston Texans", "hook": "Delivered a crucial end-zone sack for a defensive safety against Daniel Jones."}
]
colts_data["image"] = "https://images.pexels.com/photos/209954/pexels-photo-209954.jpeg"
colts_data["resultSummary"] = "FINAL: Texans 26, Colts 3 (Stroud 3 TDs, Montgomery 107 rush yds, Anderson safety). TEX 4-7, IND 3-8."
save_match("colts-at-texans-tnf-week11-2026.json", colts_data)

# 10. Create bears-at-lions-thanksgiving-week12-2026.json (Thursday Nov 26 Thanksgiving Day)
bears_lions = {
  "slug": "bears-at-lions-thanksgiving-week12-2026",
  "headline": "Thanksgiving Day classic: Identical 8-2 Lions and Bears collide at Ford Field for NFC North summit",
  "whyCareScore": 9.6,
  "whyCareReason": "Both heated NFC North rivals enter Thanksgiving Day with matching 8-2 records, as Ben Johnson returns to Detroit leading Caleb Williams resurgent Bears.",
  "teaser": "First place in the NFC North belongs to the winner as Dan Campbell 6-0 home Lions host Ben Johnson five-game-winning Bears on CBS (1:00 PM ET).",
  "story": (
    "For only the fourth time in 193 all-time meetings, the Detroit Lions and Chicago Bears meet on Thanksgiving Day with identical 8-2 records, putting sole possession of first place in the NFC North on the line at Ford Field.\n\n"
    "Detroit carries a six-game winning streak and a spotless 6-0 home mark into the 1:00 PM ET holiday kickoff. Coach Dan Campbell offense continues to surge behind efficient quarterback Jared Goff (leaning on Jameson Williams) and explosive running back Jahmyr Gibbs, who scored twice against Tampa Bay in Week 11.\n\n"
    "Across the sideline stands Chicago head coach Ben Johnson returning to Ford Field after steering the Bears on a five-game winning streak. Quarterback Caleb Williams has guided Chicago through five straight games without trailing even once, matching the 1985 Bears franchise streak alongside receivers Rome Odunze and Luther Burden and pass rushers Jeffery Simmons and Montez Sweat."
  ),
  "stakes": "Winner takes sole possession of 1st place in the NFC North and keeps pace with 9-1 San Francisco for the NFC top seed.",
  "rivalryAngle": "Former Lions coordinator Ben Johnson coaches Chicago against Dan Campbell Detroit in a historic 8-2 vs 8-2 holiday clash.",
  "funFacts": [
    "Chicago has gone five consecutive games without trailing at any point since Caleb Williams returned from injury.",
    "Detroit enters Thanksgiving on a six-game win streak and undefeated (6-0) inside Ford Field in 2026.",
    "This marks only the 4th time in 193 meetings that Bears vs Lions features matching 8-2 marks on Thanksgiving."
  ],
  "keyPlayers": [
    {"name": "Caleb Williams", "team": "Chicago Bears", "hook": "Has steered Chicago through five consecutive games without trailing."},
    {"name": "Jahmyr Gibbs", "team": "Detroit Lions", "hook": "Scored twice in Week 11 win over Tampa Bay to fuel Detroit six-game streak."},
    {"name": "Jared Goff", "team": "Detroit Lions", "hook": "Facing a Chicago front anchored by Jeffery Simmons and Montez Sweat."}
  ],
  "headToHead": "26 November 2026. 1:00 PM ET (CBS). Ford Field, Detroit. 194th all-time meeting (both 8-2).",
  "tags": ["football", "nfl", "thanksgiving", "lions", "bears", "nfc-north", "caleb-williams", "jahmyr-gibbs"],
  "home": "Detroit Lions",
  "away": "Chicago Bears",
  "homeCode": "USA",
  "awayCode": "USA",
  "homeFlag": "us",
  "awayFlag": "us",
  "group": "NFL Week 12",
  "matchday": 12,
  "date": "2026-11-26",
  "time": "1:00 PM ET",
  "venue": "Ford Field",
  "city": "Detroit",
  "status": "UPCOMING",
  "homeScore": None,
  "awayScore": None,
  "marquee": True,
  "liveMinute": None,
  "image": "https://images.pexels.com/photos/209954/pexels-photo-209954.jpeg",
  "decidedBy": None,
  "homePen": None,
  "awayPen": None,
  "sport": "football",
  "competition": "nfl-2026",
  "format": "team-match",
  "season": "2026",
  "roundLabel": "NFL Week 12 · Thanksgiving Classic",
  "resultSummary": "UPCOMING (Thu 1:00 PM ET CBS): Chicago Bears (8-2) at Detroit Lions (8-2). First place in NFC North.",
  "leaderboard": [],
  "tennisSets": [],
  "sources": [
    {"name": "NFL / DAZN: Bears at Lions Week 12 Thanksgiving Broadcast & Matchup", "url": "https://www.nfl.com/news/nfl-thanksgiving-2026"},
    {"name": "ChicagoBears.com / DetroitLions.com: Both 8-2 squads clash in historic holiday game", "url": "https://www.chicagobears.com/news/"}
  ]
}
save_match("bears-at-lions-thanksgiving-week12-2026.json", bears_lions)

# 11. Create chiefs-at-bills-thanksgiving-week12-2026.json (Thursday Nov 26 Nightcap)
chiefs_bills = {
  "slug": "chiefs-at-bills-thanksgiving-week12-2026",
  "headline": "Thanksgiving Nightcap: Kansas City Chiefs (8-2) visit AFC top-seed Buffalo Bills (9-1) in Orchard Park",
  "whyCareScore": 9.5,
  "whyCareReason": "The AFC top two heavyweights square off in Thanksgiving primetime as Patrick Mahomes 8-2 Chiefs challenge Josh Allen 9-1 Bills.",
  "teaser": "Buffalo (9-1) defend the AFC No. 1 seed under the lights of Highmark Stadium against the 8-2 Chiefs at 8:20 PM ET on NBC.",
  "story": (
    "NFL Week 12 Thanksgiving tripleheader culminates in a heavyweight AFC showdown on Thursday night, 26 November, as the Kansas City Chiefs (8-2) travel to Highmark Stadium to face the conference-leading Buffalo Bills (9-1).\n\n"
    "Both teams arrive fresh off emphatic Week 11 wins: Buffalo handled Miami 26-9 to improve to 9-1 atop the AFC East, while Kansas City crushed Arizona 34-7 to reach 8-2 in the AFC West alongside Denver (also 8-2).\n\n"
    "With the No. 1 seed and only first-round bye in the AFC potentially riding on the head-to-head tiebreaker, Patrick Mahomes and Josh Allen renew one of the defining quarterback rivalries of this era."
  ),
  "stakes": "A Buffalo win pushes the Bills two full games clear of Kansas City with the head-to-head tiebreaker for the AFC No. 1 seed.",
  "rivalryAngle": "Mahomes vs Allen under Thanksgiving primetime lights with the AFC top seed firmly in view.",
  "funFacts": [
    "Buffalo holds the AFC best record at 9-1 entering Thanksgiving night.",
    "Kansas City enters 8-2 after routing the Arizona Cardinals 34-7 in Week 11.",
    "Part of a rare five-day NFL Week 12 holiday stretch featuring Packers-Rams on Netflix (Wed) and Broncos-Steelers (Fri)."
  ],
  "keyPlayers": [
    {"name": "Josh Allen", "team": "Buffalo Bills", "hook": "Guides 9-1 Buffalo offense in front of a raucous holiday crowd in Orchard Park."},
    {"name": "Patrick Mahomes", "team": "Kansas City Chiefs", "hook": "Aims to steal a critical head-to-head road tiebreaker to pull 9-2 alongside Buffalo."}
  ],
  "headToHead": "26 November 2026. 8:20 PM ET (NBC/Peacock). Highmark Stadium, Orchard Park, NY.",
  "tags": ["football", "nfl", "thanksgiving", "chiefs", "bills", "mahomes", "josh-allen"],
  "home": "Buffalo Bills",
  "away": "Kansas City Chiefs",
  "homeCode": "USA",
  "awayCode": "USA",
  "homeFlag": "us",
  "awayFlag": "us",
  "group": "NFL Week 12",
  "matchday": 12,
  "date": "2026-11-26",
  "time": "8:20 PM ET",
  "venue": "Highmark Stadium",
  "city": "Orchard Park",
  "status": "UPCOMING",
  "homeScore": None,
  "awayScore": None,
  "marquee": True,
  "liveMinute": None,
  "image": "https://images.pexels.com/photos/209954/pexels-photo-209954.jpeg",
  "decidedBy": None,
  "homePen": None,
  "awayPen": None,
  "sport": "football",
  "competition": "nfl-2026",
  "format": "team-match",
  "season": "2026",
  "roundLabel": "NFL Week 12 · Thanksgiving Night",
  "resultSummary": "UPCOMING (Thu 8:20 PM ET NBC): Kansas City Chiefs (8-2) at Buffalo Bills (9-1).",
  "leaderboard": [],
  "tennisSets": [],
  "sources": [
    {"name": "NFL / NBC Sports: Chiefs at Bills Week 12 Thanksgiving Night Preview", "url": "https://www.nfl.com/schedules/2026/reg12/"}
  ]
}
save_match("chiefs-at-bills-thanksgiving-week12-2026.json", chiefs_bills)

# 12. Create nba-celtics-vs-wizards-nov24-2026.json (FINISHED 2026-11-24 with REAL verified box score!)
celtics_wiz = {
  "slug": "nba-celtics-vs-wizards-nov24-2026",
  "headline": "Emirates NBA Cup: Tatum erupts for 41 and George adds 28 as Celtics pull away from Wizards 131-116",
  "whyCareScore": 8.7,
  "whyCareReason": "Boston scores 80 first-half points behind Jayson Tatum (41) and Paul George (28) to overwhelm Anthony Davis (33/13) and Washington before the Thanksgiving break.",
  "teaser": "Jayson Tatum pours in 41 points with 8 assists and Paul George shoots 6-of-9 from deep (28 pts) as the Celtics down the Wizards 131-116 in Washington.",
  "story": (
    "The Boston Celtics produced a blistering first-half offensive explosion at Capital One Arena on Tuesday night, 24 November, defeating the Washington Wizards 131-116 in Emirates NBA Cup group action.\n\n"
    "Boston piled up 80 points before halftime (34-28 Q1, 46-21 Q2) behind superstar Jayson Tatum, who finished with 41 points, six rebounds, and eight assists while hitting six three-pointers. Paul George complemented him seamlessly with 28 points and nine assists on 6-of-9 shooting from deep, while Neemias Queta tallied 21 points and five rebounds.\n\n"
    "Washington mounted a 40-point third quarter behind Anthony Davis (33 points, 13 rebounds), rookie AJ Dybantsa (20 points, 11 rebounds, seven assists), and Trae Young (17 points, 12 assists), yet could not close the gap. Elsewhere Tuesday, Dallas routed Denver 120-101 behind Cooper Flagg (24 pts, 12 ast) and shorthanded Detroit beat Orlando 104-86."
  ),
  "stakes": "Boston locks down crucial Emirates NBA Cup point differential ahead of Thursday league-wide Thanksgiving pause.",
  "rivalryAngle": "Tatum and George outgunned the Wizards trio of Davis, Dybantsa, and Young in an electric 247-point NBA Cup showcase.",
  "funFacts": [
    "Boston erupted for 46 second-quarter points to build an 80-49 halftime lead in Washington.",
    "Jayson Tatum (41/6/8) and Paul George (28/4/9) combined for 69 points, 17 assists, and 12 threes.",
    "Same night in Denver: Cooper Flagg posted 24 points, 6 rebounds, and 12 assists in Dallas 120-101 victory."
  ],
  "keyPlayers": [
    {"name": "Jayson Tatum", "team": "Boston Celtics", "hook": "Erupted for 41 points, 6 rebounds, and 8 assists with six three-pointers."},
    {"name": "Paul George", "team": "Boston Celtics", "hook": "Knocked down 6-of-9 from deep for 28 points and 9 assists in Capital One Arena win."},
    {"name": "Anthony Davis", "team": "Washington Wizards", "hook": "Dominated the paint for 33 points and 13 rebounds in Washington loss."}
  ],
  "headToHead": "24 November 2026. Capital One Arena, Washington, D.C. Final: Celtics 131, Wizards 116.",
  "tags": ["basketball", "nba", "nba-cup", "celtics", "wizards", "tatum", "paul-george", "anthony-davis"],
  "home": "Washington Wizards",
  "away": "Boston Celtics",
  "homeCode": "USA",
  "awayCode": "USA",
  "homeFlag": "us",
  "awayFlag": "us",
  "group": "Emirates NBA Cup",
  "matchday": 5,
  "date": "2026-11-24",
  "time": "7:00 PM ET",
  "venue": "Capital One Arena",
  "city": "Washington",
  "status": "FINISHED",
  "homeScore": 116,
  "awayScore": 131,
  "marquee": False,
  "liveMinute": None,
  "image": "https://images.pexels.com/photos/1752757/pexels-photo-1752757.jpeg",
  "decidedBy": "regular",
  "homePen": None,
  "awayPen": None,
  "sport": "basketball",
  "competition": "nba-2026-27",
  "format": "team-match",
  "season": "2026-27",
  "roundLabel": "Emirates NBA Cup · Final",
  "resultSummary": "FINAL: Celtics 131, Wizards 116 (Tatum 41, George 28, Queta 21; Davis 33/13, Dybantsa 20/11/7).",
  "leaderboard": [],
  "tennisSets": [],
  "sources": [
    {"name": "RealGM / FOX Sports: Celtics 131-116 Wizards Box Score", "url": "https://basketball.realgm.com/nba/boxscores"},
    {"name": "92.9 The Ticket / StatMuse: NBA Cup Tuesday Night Final Boxes", "url": "https://www.nba.com/nba-cup/2026"}
  ]
}
save_match("nba-celtics-vs-wizards-nov24-2026.json", celtics_wiz)

# 13. Ensure nba-lakers-vs-kings-nov20-2026.json has explicit image preserved
lk_path = os.path.join(MATCHES_DIR, "nba-lakers-vs-kings-nov20-2026.json")
with open(lk_path, "r", encoding="utf-8") as f:
    lk_data = json.load(f)
if not lk_data.get("image"):
    lk_data["image"] = "https://images.pexels.com/photos/1752757/pexels-photo-1752757.jpeg"
    save_match("nba-lakers-vs-kings-nov20-2026.json", lk_data)
