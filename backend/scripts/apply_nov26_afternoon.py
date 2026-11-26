# Afternoon 26 Nov 2026 desk: verified Wednesday/Thursday-morning finals only.
import json
import os
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
MATCHES = os.path.join(ROOT, "frontend", "src", "content", "matches")
STORIES = os.path.join(ROOT, "frontend", "src", "content", "stories")
I18N = os.path.join(ROOT, "frontend", "src", "i18n")


def no_dashes(blob, label):
    if "\u2014" in blob:
        raise SystemExit(f"emdash in {label}")
    if "--" in blob.replace("---", ""):
        raise SystemExit(f"double hyphen in {label}")


def save_match(filename, data):
    raw = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    no_dashes(raw, filename)
    with open(os.path.join(MATCHES, filename), "w", encoding="utf-8") as f:
        f.write(raw)
    print("match", filename, data["status"], data["date"])


def save_story(filename, content):
    no_dashes(content, filename)
    with open(os.path.join(STORIES, filename), "w", encoding="utf-8") as f:
        f.write(content)
    print("story", filename)


def loadm(name):
    with open(os.path.join(MATCHES, name), encoding="utf-8") as f:
        return json.load(f)


# ---------------------------------------------------------------------------
# Matches
# ---------------------------------------------------------------------------
rams = {
    "slug": "packers-at-rams-thanksgiving-eve-week12-2026",
    "headline": "Thanksgiving Eve: Blake Corum runs for 184 as Rams grind past Packers 26-13",
    "whyCareScore": 9.1,
    "whyCareReason": "Los Angeles wins a fifth straight and moves to 7-4 as Green Bay falls to 6-5 after a second-half blanking at SoFi Stadium.",
    "teaser": "Blake Corum (32 carries, 184 yards, 1 TD) and four Brandon McManus field goals power the Rams past Green Bay 26-13 on Netflix Thanksgiving Eve.",
    "story": (
        "The Los Angeles Rams used a relentless ground game to beat the Green Bay Packers 26-13 on Wednesday night, 25 November, in the NFL first Thanksgiving Eve game at SoFi Stadium in Inglewood.\n\n"
        "Blake Corum rushed 32 times for a career-high 184 yards and a 1-yard touchdown. Kyren Williams added a 7-yard scoring run and Brandon McManus kicked four field goals from 43, 41, 40 and 30 yards. The Rams piled up 241 rushing yards and held the ball 40:40 to Green Bay 19:20.\n\n"
        "Matthew Stafford completed 16 of 23 passes for 140 yards with one interception. Jordan Love went 17 of 29 for 198 yards, one touchdown and two interceptions. Christian Watson caught four passes for 65 yards and a score before a helmet-first hit from Kam Kinchens, who was ejected. Watson left with a concussion. Los Angeles is 7-4 on a five-game winning streak. Green Bay is 6-5."
    ),
    "stakes": "The Rams take the head-to-head tiebreaker and a 7-4 mark into the NFC playoff race while Green Bay drops a second straight.",
    "rivalryAngle": "Corum birthday night and a 13-0 second half turned a 6-4 vs 6-4 Netflix showcase into a Rams statement.",
    "funFacts": [
        "Corum 32 carries were the most by a Rams back since Todd Gurley in 2015.",
        "Los Angeles rushed for 241 yards and led time of possession 40:40 to 19:20.",
        "Green Bay managed 16 second-half plays and was shut out after halftime, 13-0."
    ],
    "keyPlayers": [
        {"name": "Blake Corum", "team": "Los Angeles Rams", "hook": "Career-high 184 yards and a touchdown on 32 carries, including 161 yards after halftime."},
        {"name": "Brandon McManus", "team": "Los Angeles Rams", "hook": "Four field goals from 43, 41, 40 and 30 yards."},
        {"name": "Jordan Love", "team": "Green Bay Packers", "hook": "17 of 29 for 198 yards, one touchdown and two interceptions as Green Bay went scoreless after the break."}
    ],
    "headToHead": "25 November 2026. 8:00 PM ET (Netflix). SoFi Stadium, Inglewood. Final: Rams 26, Packers 13.",
    "tags": ["football", "nfl", "thanksgiving", "rams", "packers", "blake-corum", "week-12"],
    "home": "Los Angeles Rams",
    "away": "Green Bay Packers",
    "homeCode": "USA",
    "awayCode": "USA",
    "homeFlag": "us",
    "awayFlag": "us",
    "group": "NFL Week 12",
    "matchday": 12,
    "date": "2026-11-25",
    "time": "8:00 PM ET",
    "venue": "SoFi Stadium",
    "city": "Inglewood",
    "status": "FINISHED",
    "homeScore": 26,
    "awayScore": 13,
    "marquee": True,
    "liveMinute": None,
    "image": "https://images.pexels.com/photos/1618269/pexels-photo-1618269.jpeg",
    "decidedBy": "regular",
    "homePen": None,
    "awayPen": None,
    "sport": "football",
    "competition": "nfl-2026",
    "format": "team-match",
    "season": "2026",
    "roundLabel": "NFL Week 12 · Thanksgiving Eve",
    "resultSummary": "FINAL: Rams 26, Packers 13 (Corum 32-184-1, McManus 4 FGs; Love 17/29, 198, 1 TD, 2 INT). LAR 7-4, GB 6-5.",
    "leaderboard": [],
    "tennisSets": [],
    "sources": [
        {"name": "CBS Sports: Corum rushes for 184 as Rams power past Packers 26-13", "url": "https://www.cbssports.com/nfl/news/blake-corum-rushes-for-184-yards-as-rams-power-past-packers-26-13/"},
        {"name": "packers.com: Game recap from Packers loss to Rams Week 12", "url": "https://www.packers.com/news/game-recap-5-takeaways-from-packers-loss-to-rams-week-12-2026"},
        {"name": "Sky Sports: Rams beat Packers 26-13 on Thanksgiving Eve", "url": "https://www.skysports.com/nfl/news/13616629/nfl-los-angeles-rams-beat-green-bay-packers-26-13-in-thanksgiving-eve-clash-for-fifth-straight-win-in-playoff-push"}
    ]
}
save_match("packers-at-rams-thanksgiving-eve-week12-2026.json", rams)

barca = {
    "slug": "sabah-vs-barcelona-ucl-md5-2026",
    "headline": "Champions League MD5: Gordon double sends Barcelona past Sabah 4-1 in Baku",
    "whyCareScore": 8.8,
    "whyCareReason": "Anthony Gordon scores twice as Barcelona take a fourth win from five and sit on 12 points; Liverpool also win 3-0 at Club Brugge.",
    "teaser": "Gordon 31 and 51, Adeyemi 55 and Jesus 60 sink Sabah 4-1. Mickels replies on 63. Liverpool beat Club Brugge 3-0 the same night.",
    "story": (
        "Barcelona cruised to a 4-1 Champions League win at Sabah on Wednesday, 25 November, at the Baku Olympic Stadium as Hansi Flick side posted a fourth victory from five league-phase matches.\n\n"
        "Anthony Gordon opened on 31 minutes and doubled the lead on 51. Karim Adeyemi scored on 55 and Gabriel Jesus made it 4-0 on 60. Joy-Lance Mickels pulled one back on 63. Gordon was player of the match.\n\n"
        "The same night Liverpool won 3-0 at Club Brugge: Alexander Isak scored in the 13th minute and added a late chip, with Florian Wirtz striking on 79. After five matchdays Real Madrid remain first on 15 points, PSG sit second on 13, and Barcelona and Liverpool are among the 12-point group. Premier League after MW11 is unchanged: Arsenal 28, Brighton 22, Manchester City 22, Liverpool 21."
    ),
    "stakes": "Barcelona keep a top-eight automatic path on 12 points from five; Real Madrid still lead the 36-team table on 15.",
    "rivalryAngle": "Flick rotated without Lamine Yamal and still produced a three-goal burst in nine second-half minutes in Baku.",
    "funFacts": [
        "Gordon scored on 31 and 51 minutes; Adeyemi 55 and Jesus 60 completed a 4-0 burst before Mickels 63.",
        "Liverpool won 3-0 at Club Brugge (Isak 13 and late, Wirtz 79) to reach 12 points.",
        "Table after MD5: Real Madrid 15, PSG 13, Barcelona 12, Liverpool 12. Arsenal 11, City 10 from Tuesday."
    ],
    "keyPlayers": [
        {"name": "Anthony Gordon", "team": "Barcelona", "hook": "Two goals in Baku (31, 51) as player of the match."},
        {"name": "Karim Adeyemi", "team": "Barcelona", "hook": "Set up the opener and scored the third on 55 minutes."},
        {"name": "Alexander Isak", "team": "Liverpool", "hook": "Scored twice in a 3-0 win at Club Brugge, including a 13th-minute opener."}
    ],
    "headToHead": "25 November 2026. UEFA Champions League Matchday 5. Baku Olympic Stadium. Final: Sabah 1-4 Barcelona.",
    "tags": ["soccer", "champions-league", "barcelona", "sabah", "gordon", "liverpool", "isak"],
    "home": "Sabah",
    "away": "Barcelona",
    "homeCode": None,
    "awayCode": None,
    "homeFlag": "",
    "awayFlag": "",
    "group": "UCL",
    "matchday": 5,
    "date": "2026-11-25",
    "time": "18:45 CET",
    "venue": "Baku Olympic Stadium",
    "city": "Baku",
    "status": "FINISHED",
    "homeScore": 1,
    "awayScore": 4,
    "marquee": True,
    "liveMinute": None,
    "image": "https://images.pexels.com/photos/274506/pexels-photo-274506.jpeg",
    "decidedBy": "regular",
    "homePen": None,
    "awayPen": None,
    "sport": "soccer",
    "competition": "champions-league-2026",
    "format": "team-match",
    "season": "2026-27",
    "roundLabel": "Champions League · Matchday 5",
    "resultSummary": "FINAL: Sabah 1-4 Barcelona (Gordon 31, 51; Adeyemi 55; Jesus 60; Mickels 63). Same night: Club Brugge 0-3 Liverpool (Isak 13, Wirtz 79, Isak late).",
    "leaderboard": [],
    "tennisSets": [],
    "sources": [
        {"name": "Reuters: Gordon double helps Barcelona cruise past Sabah 4-1", "url": "https://www.reuters.com/sports/soccer/gordon-double-helps-barcelona-cruise-past-sabah-4-1-champions-league-2026-11-25/"},
        {"name": "Liverpool FC: Isak and Wirtz strike in 3-0 win at Club Brugge", "url": "https://www.liverpoolfc.com/news/match-report-liverpool-brugge-champions-league-isak-wirtz"},
        {"name": "UEFA Champions League: Matchday 5 reports", "url": "https://www.uefa.com/uefachampionsleague/"}
    ]
}
save_match("sabah-vs-barcelona-ucl-md5-2026.json", barca)

italy = loadm("davis-cup-finals-2026-bologna-knockout.json")
italy.update({
    "headline": "Davis Cup Bologna: Italy beat South Korea 2-1; Czechia already through",
    "whyCareScore": 9.0,
    "whyCareReason": "Defending champions Italy survive Kwon beating Cobolli and close the tie in doubles, joining Czechia in the last four.",
    "teaser": "Musetti d Hong 6-0, 7-6(5); Kwon d Cobolli 3-6, 7-6(3), 7-6(5); Berrettini and Vavassori d Chung and Kwon 7-6(2), 7-6(11).",
    "story": (
        "Italy beat South Korea 2-1 in the Davis Cup Final 8 quarterfinals on Wednesday, 25 November, at SuperTennis Arena in Bologna.\n\n"
        "Lorenzo Musetti opened with a 6-0, 7-6(5) win over Seongchan Hong. Soonwoo Kwon leveled the tie by beating Flavio Cobolli 3-6, 7-6(3), 7-6(5). Matteo Berrettini and Andrea Vavassori then won the doubles 7-6(2), 7-6(11) over Hyeon Chung and Kwon.\n\n"
        "Czechia had already booked a semifinal by beating Canada 2-0 on Tuesday. Great Britain later beat Germany 2-1 on Thursday. Austria vs Spain at 17:00 CET on Thursday remains unpublished. Italy meet Czechia in Friday semifinals (16:00 CET)."
    ),
    "stakes": "Italy join Czechia in the last four and meet them on Friday in Bologna.",
    "rivalryAngle": "Home doubles from Berrettini and Vavassori rescued the title defense after Kwon leveled the singles.",
    "funFacts": [
        "Musetti won the opener 6-0, 7-6(5) before Kwon leveled against Cobolli in two tiebreaks.",
        "Berrettini and Vavassori closed 7-6(2), 7-6(11) in the decisive doubles.",
        "Czechia swept Canada 2-0 on Tuesday; Italy vs Czechia is Friday at 16:00 CET."
    ],
    "keyPlayers": [
        {"name": "Lorenzo Musetti", "team": "Italy", "hook": "Beat Seongchan Hong 6-0, 7-6(5) for Italy opening point."},
        {"name": "Matteo Berrettini", "team": "Italy", "hook": "Won the decisive doubles with Andrea Vavassori 7-6(2), 7-6(11)."},
        {"name": "Soonwoo Kwon", "team": "South Korea", "hook": "Leveled the tie by beating Flavio Cobolli 3-6, 7-6(3), 7-6(5)."}
    ],
    "headToHead": "25 November 2026. SuperTennis Arena, BolognaFiere. Final: Italy 2-1 South Korea.",
    "status": "FINISHED",
    "homeScore": 2,
    "awayScore": 1,
    "marquee": True,
    "liveMinute": None,
    "decidedBy": "regular",
    "resultSummary": "FINAL: Italy 2-1 South Korea (Musetti d Hong 6-0, 7-6(5); Kwon d Cobolli 3-6, 7-6(3), 7-6(5); Berrettini/Vavassori d Chung/Kwon 7-6(2), 7-6(11)).",
})
save_match("davis-cup-finals-2026-bologna-knockout.json", italy)

gb = loadm("davis-cup-britain-vs-germany-nov26-2026.json")
gb.update({
    "headline": "Davis Cup: Great Britain beat Germany 2-1 to reach first semifinal since 2019",
    "whyCareScore": 9.2,
    "whyCareReason": "Patten and Skupski win the decisive doubles after Norrie beats Struff and Zverev levels against Fery.",
    "teaser": "Norrie d Struff 6-3, 3-6, 6-2; Zverev d Fery 6-3, 6-2; Patten and Skupski d Krawietz and Puetz 6-2, 7-6(6).",
    "story": (
        "Great Britain beat Germany 2-1 in the Davis Cup Final 8 quarterfinals on Thursday, 26 November, at SuperTennis Arena in Bologna and reached a first semifinal since 2019.\n\n"
        "Cameron Norrie beat Jan-Lennard Struff 6-3, 3-6, 6-2, saving four break points at 2-2 in the third set. World No. 1 Alexander Zverev leveled the tie by beating Arthur Fery 6-3, 6-2.\n\n"
        "Henry Patten and Neal Skupski then beat Kevin Krawietz and Tim Puetz 6-2, 7-6(6) in the decisive doubles. Great Britain will meet Austria or Spain on Saturday. Austria vs Spain at 17:00 CET on Thursday is unpublished as a final."
    ),
    "stakes": "Great Britain are into a first Davis Cup Final 4 since 2019 and wait on Austria vs Spain for a Saturday opponent.",
    "rivalryAngle": "A new Patten-Skupski pairing closed a 1-1 tie against Germany experienced doubles pair.",
    "funFacts": [
        "Norrie saved four break points at 2-2 in the third set against Struff.",
        "Zverev leveled 6-3, 6-2 over Fery before the British doubles pair closed it.",
        "Patten and Skupski won 6-2, 7-6(6) for a first GB semifinal since 2019."
    ],
    "keyPlayers": [
        {"name": "Cameron Norrie", "team": "Great Britain", "hook": "Beat Jan-Lennard Struff 6-3, 3-6, 6-2 to put GB 1-0 up."},
        {"name": "Henry Patten", "team": "Great Britain", "hook": "Won the decisive doubles with Neal Skupski 6-2, 7-6(6)."},
        {"name": "Alexander Zverev", "team": "Germany", "hook": "Leveled the tie 6-3, 6-2 over Arthur Fery."}
    ],
    "headToHead": "26 November 2026. 10:00 CET. SuperTennis Arena, Bologna. Final: Great Britain 2-1 Germany.",
    "homeFlag": "gb-eng",
    "awayFlag": "de",
    "status": "FINISHED",
    "homeScore": 2,
    "awayScore": 1,
    "marquee": True,
    "liveMinute": None,
    "decidedBy": "regular",
    "image": "https://images.pexels.com/photos/2291006/pexels-photo-2291006.jpeg",
    "resultSummary": "FINAL: Great Britain 2-1 Germany (Norrie d Struff 6-3, 3-6, 6-2; Zverev d Fery 6-3, 6-2; Patten/Skupski d Krawietz/Puetz 6-2, 7-6(6)). Austria vs Spain 17:00 CET unpublished.",
    "sources": [
        {"name": "BBC Sport: Great Britain beat Germany to reach Davis Cup semi-finals", "url": "https://www.bbc.co.uk/sport/tennis/articles/c5m2lvevrk1mo"},
        {"name": "LTA: Great Britain 2-1 Germany results", "url": "https://www.lta.org.uk/fan-zone/davis-cup/news/final-8-great-britain-vs-germany-results-updates"},
        {"name": "Davis Cup official: Final 8 Bologna", "url": "https://www.daviscup.com/"}
    ]
})
save_match("davis-cup-britain-vs-germany-nov26-2026.json", gb)

sixers = {
    "slug": "nba-sixers-vs-heat-nov25-2026",
    "headline": "Emirates NBA Cup: LeBron posts first Sixers triple-double in 111-104 win over Heat",
    "whyCareScore": 8.9,
    "whyCareReason": "LeBron James records 25 points, 10 rebounds and 12 assists in Philadelphia first Sixers triple-double, snapping Miami seven-game streak.",
    "teaser": "LeBron 25/10/12 and Maxey 30 beat Giannis 32/14 as the Sixers win 111-104. Portland beat San Antonio 116-111, Wembanyama 44 and 16.",
    "story": (
        "The Philadelphia 76ers beat the Miami Heat 111-104 on Wednesday, 25 November, in Emirates NBA Cup play, then the league paused for Thanksgiving rest on Thursday.\n\n"
        "LeBron James posted 25 points, 10 rebounds and 12 assists for his first triple-double in a Sixers uniform. Tyrese Maxey scored 30. Giannis Antetokounmpo had 32 points and 14 rebounds in the loss. Philadelphia moved to 15-4 and ended Miami seven-game winning streak.\n\n"
        "The same night Portland beat San Antonio 116-111: Deni Avdija scored 33 with 12 rebounds and 7 assists, Damian Lillard added 29 points on 10-of-10 free throws, and Victor Wembanyama had 44 points and 16 rebounds. Tuesday still stands: Mavericks 120-101 Nuggets, Celtics 131-116 Wizards, Pistons 104-86 Magic."
    ),
    "stakes": "Philadelphia sit 15-4 heading into the Thanksgiving pause after snapping Miami seven-game run.",
    "rivalryAngle": "LeBron first Sixers triple-double came against a Heat team that had won seven in a row.",
    "funFacts": [
        "LeBron James: 25 points, 10 rebounds, 12 assists, first triple-double as a Sixer.",
        "Tyrese Maxey scored 30; Giannis Antetokounmpo had 32 and 14 in the Heat loss.",
        "Portland 116-111 San Antonio: Wembanyama 44 and 16; Avdija 33/12/7; Lillard 29."
    ],
    "keyPlayers": [
        {"name": "LeBron James", "team": "Philadelphia 76ers", "hook": "25 points, 10 rebounds, 12 assists in his first Sixers triple-double."},
        {"name": "Tyrese Maxey", "team": "Philadelphia 76ers", "hook": "Scored 30 points in the 111-104 Cup win."},
        {"name": "Victor Wembanyama", "team": "San Antonio Spurs", "hook": "44 points and 16 rebounds in a 116-111 loss at Portland."}
    ],
    "headToHead": "25 November 2026. Emirates NBA Cup. Final: 76ers 111, Heat 104.",
    "tags": ["basketball", "nba", "nba-cup", "sixers", "heat", "lebron", "maxey"],
    "home": "Philadelphia 76ers",
    "away": "Miami Heat",
    "homeCode": "USA",
    "awayCode": "USA",
    "homeFlag": "us",
    "awayFlag": "us",
    "group": "Emirates NBA Cup",
    "matchday": 6,
    "date": "2026-11-25",
    "time": "Evening ET",
    "venue": "Wells Fargo Center",
    "city": "Philadelphia",
    "status": "FINISHED",
    "homeScore": 111,
    "awayScore": 104,
    "marquee": True,
    "liveMinute": None,
    "image": "https://images.pexels.com/photos/1752757/pexels-photo-1752757.jpeg",
    "decidedBy": "regular",
    "homePen": None,
    "awayPen": None,
    "sport": "basketball",
    "competition": "nba-2026-27",
    "format": "team-match",
    "season": "2026-27",
    "roundLabel": "Emirates NBA Cup · Wednesday",
    "resultSummary": "FINAL: 76ers 111, Heat 104 (LeBron 25/10/12, Maxey 30; Giannis 32/14). Also: Blazers 116-111 Spurs (Wemby 44/16).",
    "leaderboard": [],
    "tennisSets": [],
    "sources": [
        {"name": "NBA.com / ESPN: 76ers 111-104 Heat box", "url": "https://www.nba.com/"},
        {"name": "NBA.com: Trail Blazers 116-111 Spurs", "url": "https://www.nba.com/games"}
    ]
}
save_match("nba-sixers-vs-heat-nov25-2026.json", sixers)

madrid = loadm("real-madrid-vs-psv-ucl-md5-2026.json")
madrid["story"] = madrid["story"].replace("in the 60th", "in the 59th").replace("Bellingham 60", "Bellingham 59")
madrid["keyPlayers"][1]["hook"] = "Produced a 59th-minute strike that swung momentum Madrid's way."
madrid["resultSummary"] = "FINAL: Real Madrid 5-1 PSV (Valverde 50, Bellingham 59, Mbappe 64, 84, Vinicius Jr 87; Perisic 32 pen)."
madrid["funFacts"][0] = "All five Real Madrid goals came in a second-half burst between minutes 50 and 87."
save_match("real-madrid-vs-psv-ucl-md5-2026.json", madrid)

# ---------------------------------------------------------------------------
# Stories
# ---------------------------------------------------------------------------
save_story("rams-packers-thanksgiving-eve-week12-2026.md", '''---
title: "Thanksgiving Eve: Corum 184-yard night lifts Rams past Packers 26-13 at SoFi"
subtitle: "Los Angeles wins a fifth straight and moves to 7-4 as Green Bay falls to 6-5 after a 13-0 second half on Netflix."
category: "football"
excerpt: "Blake Corum rushed 32 times for 184 yards and a touchdown as the Rams beat the Packers 26-13 in the NFL first Thanksgiving Eve game."
image: "https://images.pexels.com/photos/1618269/pexels-photo-1618269.jpeg"
readingTime: 5
pubDate: 2026-11-26
sport: "football"
competition: "nfl-2026"
relatedSlug: "packers-at-rams-thanksgiving-eve-week12-2026"
sources:
  - name: "CBS Sports: Rams 26-13 Packers recap"
    url: "https://www.cbssports.com/nfl/news/blake-corum-rushes-for-184-yards-as-rams-power-past-packers-26-13/"
  - name: "packers.com: Five takeaways from Packers loss to Rams"
    url: "https://www.packers.com/news/game-recap-5-takeaways-from-packers-loss-to-rams-week-12-2026"
  - name: "Sky Sports: Rams beat Packers 26-13 on Thanksgiving Eve"
    url: "https://www.skysports.com/nfl/news/13616629/nfl-los-angeles-rams-beat-green-bay-packers-26-13-in-thanksgiving-eve-clash-for-fifth-straight-win-in-playoff-push"
---

The NFL opened Thanksgiving week on Wednesday night, 25 November, with its first Thanksgiving Eve game on Netflix, and the Los Angeles Rams used the ground to beat the Green Bay Packers 26-13 at SoFi Stadium.

Blake Corum, on his 26th birthday, carried 32 times for a career-high 184 yards and a 1-yard touchdown, including 161 yards after halftime. Kyren Williams added a 7-yard scoring run. Brandon McManus kicked four field goals from 43, 41, 40 and 30 yards. The Rams rushed for 241 yards, snapped 71 plays to 44, and held the ball 40 minutes 40 seconds to Green Bay 19:20.

Matthew Stafford completed 16 of 23 passes for 140 yards and one interception. Jordan Love went 17 of 29 for 198 yards, a touchdown and two interceptions. Christian Watson had four catches for 65 yards and a score before a helmet-first hit from Kam Kinchens, who was ejected; Watson left with a concussion. Los Angeles is 7-4 on a five-game winning streak. Green Bay is 6-5. Thursday Thanksgiving remains unpublished as a final: Bears (8-2) at Lions (8-2) 1:00 PM ET CBS, Eagles (3-7) at Cowboys (5-6) 4:30 PM FOX, Chiefs (8-2) at Bills (9-1) 8:20 PM NBC.
''')

save_story("champions-league-md5-wednesday-barcelona-liverpool-2026.md", '''---
title: "Champions League Wednesday: Barcelona 4-1 at Sabah, Liverpool 3-0 at Club Brugge"
subtitle: "Gordon scores twice in Baku and Isak leads Liverpool to 12 points, with Real Madrid still first on 15 after Tuesday 5-1 over PSV."
category: "soccer"
excerpt: "Anthony Gordon scored on 31 and 51 minutes as Barcelona beat Sabah 4-1. Liverpool won 3-0 at Club Brugge through Isak and Wirtz."
image: "https://images.pexels.com/photos/274506/pexels-photo-274506.jpeg"
readingTime: 5
pubDate: 2026-11-26
sport: "soccer"
competition: "champions-league-2026"
relatedSlug: "sabah-vs-barcelona-ucl-md5-2026"
sources:
  - name: "Reuters: Gordon double helps Barcelona cruise past Sabah 4-1"
    url: "https://www.reuters.com/sports/soccer/gordon-double-helps-barcelona-cruise-past-sabah-4-1-champions-league-2026-11-25/"
  - name: "Liverpool FC official: Isak and Wirtz in 3-0 win at Club Brugge"
    url: "https://www.liverpoolfc.com/news/match-report-liverpool-brugge-champions-league-isak-wirtz"
  - name: "UEFA Champions League Matchday 5"
    url: "https://www.uefa.com/uefachampionsleague/"
---

Champions League Matchday 5 closed on Wednesday, 25 November, with Barcelona and Liverpool both collecting wins that keep them in the automatic top-eight conversation.

In Baku, Anthony Gordon scored on 31 and 51 minutes, Karim Adeyemi added a 55th-minute goal, and Gabriel Jesus made it 4-0 on 60 before Joy-Lance Mickels replied on 63. Hansi Flick side, without injured Lamine Yamal, took a fourth win from five and 12 points. Gordon was player of the match.

Liverpool won 3-0 at Club Brugge. Alexander Isak scored in the 13th minute and added a late chip over Yann Sommer. Florian Wirtz struck on 79 minutes from Rio Ngumoha pass. After five matchdays Real Madrid remain first on 15 points (5-0-0) from Tuesday 5-1 over PSV (Valverde 50, Bellingham 59, Mbappe 64 and 84, Vinicius 87; Perisic 32 pen). PSG sit on 13 after 2-2 with Roma. Barcelona and Liverpool are on 12. Premier League after MW11 is unchanged: Arsenal 28, Brighton 22, Manchester City 22, Liverpool 21.
''')

save_story("davis-cup-finals-bologna-italy-musetti-alcaraz-turin-glory-2026.md", '''---
title: "Davis Cup Bologna: Italy 2-1 Korea and Great Britain 2-1 Germany reach the last four"
subtitle: "Berrettini and Vavassori close Italy title defense; Patten and Skupski send Great Britain to a first semifinal since 2019."
category: "tennis"
excerpt: "Italy beat South Korea 2-1 on Wednesday and Great Britain beat Germany 2-1 on Thursday in Bologna. Austria vs Spain at 17:00 CET is unpublished."
image: "https://images.pexels.com/photos/1618210/pexels-photo-1618210.jpeg"
readingTime: 5
pubDate: 2026-11-26
sport: "tennis"
competition: "davis-cup-2026"
relatedSlug: "davis-cup-britain-vs-germany-nov26-2026"
sources:
  - name: "BBC Sport: Great Britain beat Germany to reach Davis Cup semi-finals"
    url: "https://www.bbc.co.uk/sport/tennis/articles/c5m2lvevrk1mo"
  - name: "LTA: Great Britain 2-1 Germany"
    url: "https://www.lta.org.uk/fan-zone/davis-cup/news/final-8-great-britain-vs-germany-results-updates"
  - name: "Davis Cup official: Bologna Final 8"
    url: "https://www.daviscup.com/"
---

The Davis Cup Final 8 in Bologna now has three quarterfinals in the book and one still to play.

On Wednesday, Italy beat South Korea 2-1. Lorenzo Musetti defeated Seongchan Hong 6-0, 7-6(5). Soonwoo Kwon leveled by beating Flavio Cobolli 3-6, 7-6(3), 7-6(5). Matteo Berrettini and Andrea Vavassori then won the doubles 7-6(2), 7-6(11) over Hyeon Chung and Kwon. Czechia had already swept Canada 2-0 on Tuesday (Machac d Draxl 6-2, 3-6, 6-2; Lehecka d Auger-Aliassime 7-6(4), 6-2). Italy meet Czechia on Friday at 16:00 CET.

On Thursday, Great Britain beat Germany 2-1 for a first semifinal since 2019. Cameron Norrie beat Jan-Lennard Struff 6-3, 3-6, 6-2. Alexander Zverev leveled 6-3, 6-2 over Arthur Fery. Henry Patten and Neal Skupski closed 6-2, 7-6(6) against Kevin Krawietz and Tim Puetz. Austria vs Spain at 17:00 CET remains unpublished. Carlos Alcaraz Turin title still stands: 6-2, 7-6(7) over Zverev on 22 November, unbeaten 5-0.
''')

save_story("nba-sixers-heat-lebron-triple-double-2026.md", '''---
title: "NBA Cup Wednesday: LeBron first Sixers triple-double beats Heat 111-104"
subtitle: "James posts 25 points, 10 rebounds and 12 assists as Philadelphia snap Miami seven-game streak before Thanksgiving rest."
category: "basketball"
excerpt: "LeBron James records his first 76ers triple-double and Tyrese Maxey scores 30 in a 111-104 win. Portland beat San Antonio 116-111, Wembanyama 44 and 16."
image: "https://images.pexels.com/photos/1752757/pexels-photo-1752757.jpeg"
readingTime: 5
pubDate: 2026-11-26
sport: "basketball"
competition: "nba-2026-27"
relatedSlug: "nba-sixers-vs-heat-nov25-2026"
sources:
  - name: "NBA.com: 76ers 111-104 Heat"
    url: "https://www.nba.com/"
  - name: "NBA.com: Trail Blazers 116-111 Spurs"
    url: "https://www.nba.com/games"
---

Emirates NBA Cup play closed Wednesday, 25 November, before a league-wide Thanksgiving rest day on Thursday.

The Philadelphia 76ers beat the Miami Heat 111-104. LeBron James finished with 25 points, 10 rebounds and 12 assists, his first triple-double in a Sixers uniform. Tyrese Maxey scored 30. Giannis Antetokounmpo had 32 points and 14 rebounds for Miami. Philadelphia moved to 15-4 and ended the Heat seven-game winning streak.

Portland beat San Antonio 116-111. Deni Avdija scored 33 with 12 rebounds and 7 assists. Damian Lillard added 29 points, 10 of 10 from the line. Victor Wembanyama had 44 points and 16 rebounds in the loss. Tuesday results still stand: Dallas 120-101 Denver (Cooper Flagg 24/6/12), Boston 131-116 Washington (Jayson Tatum 41, Paul George 28; Anthony Davis 33/13), Detroit 104-86 Orlando (Isaiah Joe 21).
''')

print("desk files written")
