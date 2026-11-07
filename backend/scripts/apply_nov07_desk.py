#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Apply verified 7 November 2026 desk: matches, stories, sports.ts, desk.json, AGENTS.md."""
import json
import os
import re
import urllib.request

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
MATCHES = os.path.join(ROOT, "frontend/src/content/matches")
STORIES = os.path.join(ROOT, "frontend/src/content/stories")

IMG = {
    "nfl": "https://images.pexels.com/photos/209954/pexels-photo-209954.jpeg?auto=compress&cs=tinysrgb&w=1600&h=900&fit=crop",
    "nba": "https://images.pexels.com/photos/248547/pexels-photo-248547.jpeg?auto=compress&cs=tinysrgb&w=1600&h=900&fit=crop",
    "ten": "https://images.pexels.com/photos/1618210/pexels-photo-1618210.jpeg?auto=compress&cs=tinysrgb&w=1600&h=900&fit=crop",
    "f1": "https://images.pexels.com/photos/627678/pexels-photo-627678.jpeg?auto=compress&cs=tinysrgb&w=1600&h=900&fit=crop",
    "golf": "https://images.pexels.com/photos/863988/pexels-photo-863988.jpeg?auto=compress&cs=tinysrgb&w=1600&h=900&fit=crop",
    "soc": "https://images.pexels.com/photos/1171084/pexels-photo-1171084.jpeg?auto=compress&cs=tinysrgb&w=1600&h=900&fit=crop",
}


def dump(path, obj):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print("wrote", path)


def get_ok(url):
    req = urllib.request.Request(url, method="GET", headers={"User-Agent": "Mozilla/5.0 MatchTales"})
    with urllib.request.urlopen(req, timeout=20) as r:
        code = r.status
        if code != 200:
            raise SystemExit("image GET %s -> %s" % (url, code))
        print("GET 200", url.split("?")[0])


for u in IMG.values():
    get_ok(u)

nfl = {
    "slug": "bengals-at-falcons-madrid-week9-2026",
    "headline": "NFL Week 9 Madrid: Bengals visit Falcons at Bernabeu on Sunday, 9:30 a.m. ET",
    "whyCareScore": 9.4,
    "whyCareReason": "Joe Burrow takes 5-2 Cincinnati to Spain against 3-5 Atlanta in the NFL's second regular-season game at Santiago Bernabeu. Saturday has no NFL game. TNF still stands: Jaguars 33, Ravens 10.",
    "teaser": "UPCOMING Sunday 8 Nov, 9:30 a.m. ET / 3:30 p.m. local, NFL Network. Bengals 5-2, Falcons 3-5. Designated home: Atlanta. No score. Pittsburgh and Tennessee are on bye.",
    "story": "The Cincinnati Bengals play the Atlanta Falcons on Sunday, 8 November, at Santiago Bernabeu Stadium in Madrid in NFL Week 9. Kickoff is 9:30 a.m. ET, 3:30 p.m. local, on NFL Network. Atlanta is the designated home team. Cincinnati is 5-2 after a three-game winning streak and a 43-36 overtime win over Tennessee. Atlanta is 3-5 after a loss to Tampa Bay. Bengals.com lists Burrow as the NFL leader in completion percentage (73.0), passing touchdowns (20) and passing yards per game (302.1), with at least four touchdown passes in each of the past three games. Bijan Robinson leads the league with 780 rushing yards at 5.2 yards per carry. Saturday 7 November has no NFL game. The last finished board remains Thursday Night Football on 5 November: Jacksonville 33, Baltimore 10. Steelers stay 6-2 atop the AFC North on a Week 9 bye. Sunday's other Week 9 scores are unpublished.",
    "stakes": "A Bengals win would put Cincinnati at 6-2, matching Pittsburgh before they meet on 15 November. Falcons remain in the NFC South race at 3-5.",
    "rivalryAngle": "International window at Real Madrid's stadium: Burrow and Ja'Marr Chase against Robinson and a Falcons side still hunting a .500 record.",
    "funFacts": [
        "Kickoff is 9:30 a.m. ET, 3:30 p.m. in Madrid, exclusive on NFL Network.",
        "The Bengals are 0-1-1 in two previous international games, both at Wembley.",
        "Pittsburgh and Tennessee are on bye in Week 9. TNF still stands: Jaguars 33, Ravens 10."
    ],
    "keyPlayers": [
        {"name": "Joe Burrow", "team": "Cincinnati Bengals", "hook": "NFL lead in completion percentage, passing TDs and yards per game entering Madrid."},
        {"name": "Bijan Robinson", "team": "Atlanta Falcons", "hook": "League-leading 780 rushing yards at 5.2 yards per carry."},
        {"name": "Trevor Lawrence", "team": "Jacksonville Jaguars", "hook": "Last NFL final: 242 yards and a 50-yard TD in Jacksonville's 33-10 TNF win."}
    ],
    "headToHead": "Sunday 8 November 2026. Santiago Bernabeu, Madrid. Status UPCOMING. No score.",
    "tags": ["football", "nfl", "bengals", "falcons", "madrid", "international", "week9"],
    "home": "Atlanta Falcons",
    "away": "Cincinnati Bengals",
    "homeCode": "USA",
    "awayCode": "USA",
    "homeFlag": "us",
    "awayFlag": "us",
    "group": "NFL Week 9",
    "matchday": 9,
    "date": "2026-11-08",
    "time": "09:30",
    "venue": "Santiago Bernabeu Stadium",
    "city": "Madrid",
    "status": "UPCOMING",
    "homeScore": None,
    "awayScore": None,
    "marquee": True,
    "liveMinute": None,
    "image": IMG["nfl"],
    "decidedBy": None,
    "homePen": None,
    "awayPen": None,
    "sport": "football",
    "competition": "nfl-2026",
    "format": "team-match",
    "season": "2026",
    "roundLabel": "Week 9 Madrid",
    "resultSummary": "UPCOMING: Bengals at Falcons, Sunday 8 Nov, 9:30 a.m. ET, Bernabeu. CIN 5-2, ATL 3-5. No score.",
    "leaderboard": [],
    "tennisSets": [],
    "sources": [
        {"name": "NFL.com: Bengals vs Falcons Week 9 Madrid preview", "url": "https://www.nfl.com/news/bengals-vs-falcons-preview-week-9-madrid-game"},
        {"name": "Bengals.com: What to watch in Madrid", "url": "https://www.bengals.com/news/game-preview-2026-week-9-bengals-falcons"},
        {"name": "Bengals international Madrid hub", "url": "https://www.bengals.com/international-madrid-2026/"}
    ]
}

nba = {
    "slug": "nba-lakers-vs-blazers-doncic-53-2026",
    "headline": "NBA: Luka Doncic scores 53 as Lakers rally past Trail Blazers 124-118",
    "whyCareScore": 9.7,
    "whyCareReason": "Doncic's 11th career 50-point game, a 62-foot heave at the half and a jumper with 28 seconds left carry Los Angeles to a fourth straight win in NBA Cup Group C.",
    "teaser": "FINAL: Lakers 124, Trail Blazers 118. Doncic 53 (17-33 FG, 5-15 3PT), Reaves 25, Kessler 16 and 12. Avdija 22-9-11, Lillard 22.",
    "story": "Luka Doncic scored 53 points and hit a jumper in the lane with 28 seconds left as the Los Angeles Lakers beat the Portland Trail Blazers 124-118 on Friday, 6 November, at Crypto.com Arena. Associated Press and Reuters recorded his 11th career 50-point game and his fourth with Los Angeles. He went 17 of 33 from the field and 5 of 15 from three, added five rebounds and five assists, and drained a 62-foot heave at the halftime buzzer after Portland had led by as many as 16. Austin Reaves scored 25. Walker Kessler had 16 points and 12 rebounds. Deni Avdija posted 22 points, nine rebounds and 11 assists. Damian Lillard scored 22. Quarters ran 20-33-34-37 for the Lakers and 29-31-15-43 for Portland. The Lakers are on a four-game winning streak and 1-1 in NBA Cup group play. Other Friday finals: Spurs 124, Kings 109 (Wembanyama 30 points, 14 rebounds; San Antonio 7-2 on a seventh straight win); Cavaliers 119, 76ers 95 (Mitchell 23, Mobley 22; Cleveland 5-4, Philadelphia 8-2); Celtics 119, Hornets 80 (Tatum 34). Saturday NBA games are unpublished.",
    "stakes": "Lakers take a fourth straight win and even NBA Cup Group C at 1-1. Portland falls to 0-1 in group play after a three-game winning streak.",
    "rivalryAngle": "Doncic answers Portland's 136-129 win in Los Angeles on 27 October with 53 points in the NBA Cup rematch.",
    "funFacts": [
        "Doncic's 53 is the highest single-game total in the NBA this season.",
        "He has six 40-point games in the Lakers' first stretch, including four in a row.",
        "Portland's 43-point fourth quarter cut a 12-point Lakers lead to four before Doncic and Reaves closed it."
    ],
    "keyPlayers": [
        {"name": "Luka Doncic", "team": "Los Angeles Lakers", "hook": "53 points, 17 of 33, 5 of 15 from three, jumper with 28 seconds left."},
        {"name": "Austin Reaves", "team": "Los Angeles Lakers", "hook": "25 points beside Doncic in the 124-118 win."},
        {"name": "Deni Avdija", "team": "Portland Trail Blazers", "hook": "22 points, 9 rebounds, 11 assists in the loss."}
    ],
    "headToHead": "Friday 6 November 2026. Crypto.com Arena, Los Angeles. Final: LAL 124, POR 118.",
    "tags": ["basketball", "nba", "lakers", "blazers", "doncic", "reaves", "nba-cup"],
    "home": "Los Angeles Lakers",
    "away": "Portland Trail Blazers",
    "homeCode": "USA",
    "awayCode": "USA",
    "homeFlag": "us",
    "awayFlag": "us",
    "group": "NBA Regular Season",
    "matchday": 10,
    "date": "2026-11-06",
    "time": "22:00",
    "venue": "Crypto.com Arena",
    "city": "Los Angeles",
    "status": "FINISHED",
    "homeScore": 124,
    "awayScore": 118,
    "marquee": True,
    "liveMinute": None,
    "image": IMG["nba"],
    "decidedBy": "points",
    "homePen": None,
    "awayPen": None,
    "sport": "basketball",
    "competition": "nba-2026-27",
    "format": "team-match",
    "season": "2026-27",
    "roundLabel": "Regular Season / NBA Cup",
    "resultSummary": "FINAL: Lakers 124, Trail Blazers 118. Doncic 53 pts; Reaves 25; Kessler 16-12; Avdija 22-9-11; Lillard 22.",
    "leaderboard": [],
    "tennisSets": [],
    "sources": [
        {"name": "NBA.com: Doncic scores 53, Lakers beat Blazers 124-118", "url": "https://www.nba.com/game/por-vs-lal-0022600032"},
        {"name": "Reuters: Doncic pours in 53 as Lakers rally past Blazers", "url": "https://www.reuters.com/sports/basketball/luka-doncic-pours-53-lakers-rally-past-blazers--flm-2026-11-07/"},
        {"name": "AP via NBA recap", "url": "https://apnews.com/article/lakers-trail-blazers-doncic-reaves-nba-bb443859434a2393d510a4db8d84795c"}
    ]
}

ten = {
    "slug": "atp-paris-masters-2026-shelton-vs-van-assche-sf",
    "headline": "Rolex Paris Masters SF: Ben Shelton beats Luca Van Assche 5-7, 6-3, 6-4 to reach the final",
    "whyCareScore": 9.6,
    "whyCareReason": "Third seed Shelton rallies from a break down in the decider to become the first American Paris Masters finalist since Jack Sock in 2017. Alcaraz vs Ruud is unpublished.",
    "teaser": "FINAL: Shelton def. Van Assche 5-7, 6-3, 6-4. First American in the Bercy final since Sock 2017. Alcaraz vs Ruud later Saturday is unpublished.",
    "story": "Ben Shelton beat Luca Van Assche 5-7, 6-3, 6-4 on Saturday, 7 November, in the Rolex Paris Masters semi-finals at Accor Arena. Associated Press and Reuters record a three-set win in which the unseeded Frenchman took the opener and broke for 3-1 in the third before Shelton won four straight games and served it out. Shelton is the first American to reach the Paris final since Jack Sock won the title in 2017. It is his third ATP Masters 1000 final and his first outside Canada. Van Assche, ranked 47th, was in his first Masters semi-final. Friday quarter-finals still stand: Shelton d Paul 6-4, 4-6, 6-3; Alcaraz d Fritz 6-7(10), 7-5, 6-3 after saving two match points; Ruud d Borges 7-6(5), 6-4; Van Assche d Hijikata 6-4, 6-7(4), 7-5. The second Saturday semi-final, Alcaraz vs Ruud, is unpublished as unfinished. Sunday's final is unpublished.",
    "stakes": "Shelton plays for a third Masters 1000 title on Sunday against Alcaraz or Ruud. Van Assche's home run ends in the last four.",
    "rivalryAngle": "American third seed vs the last Frenchman in the draw on Court Central, with a hometown crowd behind Van Assche.",
    "funFacts": [
        "Shelton is the first American Paris Masters finalist since Jack Sock in 2017.",
        "Van Assche broke for 3-1 in the third set before Shelton won the next four games.",
        "Friday: Alcaraz saved two match points to beat Fritz 6-7(10), 7-5, 6-3."
    ],
    "keyPlayers": [
        {"name": "Ben Shelton", "team": "United States", "hook": "Won 5-7, 6-3, 6-4 after trailing 3-1 in the third; first Paris final since Sock 2017."},
        {"name": "Luca Van Assche", "team": "France", "hook": "Took the first set 7-5 and broke for 3-1 in the third in his first Masters semi-final."}
    ],
    "headToHead": "Saturday 7 November 2026. Accor Arena, Paris. Final: Shelton 5-7, 6-3, 6-4.",
    "tags": ["tennis", "atp", "paris-masters", "rolex-paris-masters", "shelton", "van-assche", "bercy"],
    "home": "Ben Shelton",
    "away": "Luca Van Assche",
    "homeCode": "USA",
    "awayCode": "FRA",
    "homeFlag": "us",
    "awayFlag": "fr",
    "group": "Rolex Paris Masters",
    "matchday": 6,
    "date": "2026-11-07",
    "time": "14:30",
    "venue": "Accor Arena",
    "city": "Paris",
    "status": "FINISHED",
    "homeScore": "2",
    "awayScore": "1",
    "marquee": True,
    "liveMinute": None,
    "image": IMG["ten"],
    "decidedBy": "sets",
    "homePen": None,
    "awayPen": None,
    "sport": "tennis",
    "competition": "atp-1000-paris-2026",
    "format": "singles",
    "season": "2026",
    "roundLabel": "Semi-final",
    "resultSummary": "FINAL: Ben Shelton def. Luca Van Assche 5-7, 6-3, 6-4. Alcaraz vs Ruud unpublished.",
    "leaderboard": [],
    "tennisSets": [{"p1": "5", "p2": "7"}, {"p1": "6", "p2": "3"}, {"p1": "6", "p2": "4"}],
    "sources": [
        {"name": "AP: Shelton rallies to reach Paris Masters final", "url": "https://apnews.com/article/paris-masters-alcaraz-shelton-ruud-van-assche-3d7b1f4f30531b1424f2539089383f73"},
        {"name": "Reuters via Straits Times: Shelton outwits Van Assche", "url": "https://www.straitstimes.com/sport/tennis/shelton-outwits-hometown-hope-van-assche-to-reach-paris-masters-final"},
        {"name": "ATP Paris results", "url": "https://www.atptour.com/en/scores/current/paris/352/results"}
    ]
}

f1 = {
    "slug": "sao-paulo-gp-interlagos-2026",
    "headline": "Sao Paulo GP FP3: Max Verstappen leads Kimi Antonelli by 0.025s at Interlagos",
    "whyCareScore": 9.4,
    "whyCareReason": "Verstappen posts 1:11.622 in final practice, 0.025s clear of newly crowned champion Antonelli. Qualifying is unpublished. No Sprint this weekend. Mercedes 630, Ferrari 504.",
    "teaser": "FP3 COMPLETE: Verstappen 1:11.622; Antonelli +0.025s; Norris +0.131s; Russell +0.184s; Leclerc +0.274s. Qualifying unpublished.",
    "story": "Max Verstappen finished fastest in Free Practice 3 for the Grande Premio de Sao Paulo on Saturday, 7 November, at Autodromo Jose Carlos Pace. The FIA classification lists Verstappen in 1:11.622 from 19 laps, Kimi Antonelli second at 1:11.647 (+0.025s), Lando Norris third (+0.131s), George Russell fourth (+0.184s), Charles Leclerc fifth (+0.274s) and Oscar Piastri sixth (+0.313s). Arvid Lindblad was seventh, Liam Lawson eighth, Isack Hadjar ninth, Gabriel Bortoleto and Pierre Gasly tenth and 11th on identical +1.022s. Lewis Hamilton was 12th after seven laps. Friday still stands: FP1 Norris 1:11.717 from Antonelli and Verstappen; FP2 Antonelli 1:10.763, Norris +0.253s, Verstappen +0.259s, Russell +0.273s, Piastri +0.321s, Hamilton +0.450s. There is no Sprint. Qualifying on Saturday afternoon is unpublished as unfinished. After Mexico, standings are unchanged: Antonelli 380, Verstappen 261, Hamilton 259, Russell 250, Leclerc 245, Norris 221. Constructors: Mercedes 630, Ferrari 504, Red Bull 382, McLaren 365.",
    "stakes": "Mercedes can clinch the constructors' championship this weekend with a 126-point lead over Ferrari. Drivers' title is already settled. Qualifying and the race are unpublished.",
    "rivalryAngle": "Verstappen's Red Bull vs champion Mercedes vs Norris's McLaren in the last practice before an unpublished qualifying hour.",
    "funFacts": [
        "There is no Sprint in Sao Paulo in 2026: FP1, FP2, FP3, qualifying, race.",
        "Antonelli was 0.025 seconds off Verstappen after topping Friday FP2 in 1:10.763.",
        "Hamilton completed only seven FP3 laps and finished 12th."
    ],
    "keyPlayers": [
        {"name": "Max Verstappen", "team": "Red Bull", "hook": "FP3 fastest in 1:11.622 from 19 laps."},
        {"name": "Kimi Antonelli", "team": "Mercedes", "hook": "Second, +0.025s, world champion on 380 points."},
        {"name": "Lando Norris", "team": "McLaren", "hook": "Third in FP3 at +0.131s after leading FP1 on Friday."}
    ],
    "headToHead": "Saturday 7 November 2026. Autodromo Jose Carlos Pace, Sao Paulo. FP3 complete. Qualifying unpublished.",
    "tags": ["f1", "formula-1", "sao-paulo-gp", "interlagos", "verstappen", "antonelli", "norris", "fp3"],
    "home": "Max Verstappen",
    "away": "Kimi Antonelli",
    "homeCode": "NED",
    "awayCode": "ITA",
    "homeFlag": "nl",
    "awayFlag": "it",
    "group": "Formula 1",
    "matchday": 21,
    "date": "2026-11-07",
    "time": "12:30",
    "venue": "Autodromo Jose Carlos Pace",
    "city": "Sao Paulo",
    "status": "FINISHED",
    "homeScore": "P1",
    "awayScore": "P2",
    "marquee": True,
    "liveMinute": None,
    "image": IMG["f1"],
    "decidedBy": "time",
    "homePen": None,
    "awayPen": None,
    "sport": "f1",
    "competition": "f1-2026",
    "format": "race",
    "season": "2026",
    "roundLabel": "Free Practice 3",
    "resultSummary": "FP3: Verstappen 1:11.622; Antonelli +0.025s; Norris +0.131s. Qualifying unpublished. No Sprint.",
    "leaderboard": [
        {"pos": "1", "name": "Max Verstappen (Red Bull)", "score": "1:11.622", "note": "FP3 fastest"},
        {"pos": "2", "name": "Kimi Antonelli (Mercedes)", "score": "+0.025s", "note": "World Champion"},
        {"pos": "3", "name": "Lando Norris (McLaren)", "score": "+0.131s", "note": "P3"},
        {"pos": "4", "name": "George Russell (Mercedes)", "score": "+0.184s", "note": "P4"},
        {"pos": "5", "name": "Charles Leclerc (Ferrari)", "score": "+0.274s", "note": "P5"},
        {"pos": "6", "name": "Oscar Piastri (McLaren)", "score": "+0.313s", "note": "P6"}
    ],
    "tennisSets": [],
    "sources": [
        {"name": "FIA FP3 classification, Sao Paulo 2026", "url": "https://www.fia.com/system/files/decision-document/2026_sao_paulo_grand_prix_-_free_practice_3_classification.pdf"},
        {"name": "ESPN F1 Sao Paulo weekend results", "url": "https://www.espn.com/f1/results/_/id/600057448"},
        {"name": "ESPN F1 2026 drivers standings", "url": "https://www.espn.com/f1/standings"}
    ]
}

golf = {
    "slug": "wwt-championship-diamante-cabo-2026",
    "headline": "WWT Championship Round 2: Ben James shoots 64 to lead at 15 under at El Cardonal",
    "whyCareScore": 9.2,
    "whyCareReason": "James runs off five straight birdies around the turn and posts 65-64=129 to lead Peter Malnati by one. Round 3 is unpublished as final.",
    "teaser": "R2 COMPLETE: James 129 (-15) leads Malnati 130, Blair 132, T4 Jaeger and McCarthy 133. Kirk 63-72=135. Cut 5-under 139. Round 3 unpublished.",
    "story": "Ben James posted an 8-under 64 on Friday, 6 November, to take a one-shot lead after 36 holes at the World Wide Technology Championship. Associated Press and PGA Tour copy say he ran off five straight birdies around the turn and finished with a birdie after an aggressive tee shot, reaching 15-under 129 at El Cardonal at Diamante (par 72, 7,452 yards). Peter Malnati shot 66-64=130. Zac Blair had 64-68=132. Tied for fourth at 133: Stephan Jaeger and Denny McCarthy. Chris Kirk, the round-one leader after a bogey-free 63, shot 72 and sits 135. The cut fell at 5-under 139. The purse is $6 million. Round 3 on Saturday is in progress and is not published as a finished 54-hole board.",
    "stakes": "Fall Series card race continues on the Baja coast. Winner takes the $6 million purse event. 54-hole and 72-hole boards are unpublished.",
    "rivalryAngle": "James, already locked for a 2027 PGA Tour card from PGA Tour University, vs Malnati chasing a weekend lead after years of grinding.",
    "funFacts": [
        "James hit every fairway in the second round, per OpenGolf's recap of the PGA Tour notes.",
        "Kirk opened 63 and followed with 72 to drop from the lead to 135.",
        "The 36-hole cut was 5-under 139."
    ],
    "keyPlayers": [
        {"name": "Ben James", "team": "United States", "hook": "65-64=129, 15 under, one-shot 36-hole lead."},
        {"name": "Peter Malnati", "team": "United States", "hook": "66-64=130, one shot back after a Friday 64."},
        {"name": "Chris Kirk", "team": "United States", "hook": "Round-one leader with 63, then 72, now 135."}
    ],
    "headToHead": "Friday 6 November 2026. El Cardonal at Diamante, Los Cabos. Round 2 complete. Round 3 unpublished.",
    "tags": ["golf", "pga-tour", "wwt-championship", "los-cabos", "el-cardonal", "diamante", "ben-james"],
    "home": "Ben James",
    "away": "Peter Malnati",
    "homeCode": "USA",
    "awayCode": "USA",
    "homeFlag": "us",
    "awayFlag": "us",
    "group": "PGA Tour",
    "matchday": 6,
    "date": "2026-11-06",
    "time": "08:00",
    "venue": "El Cardonal at Diamante",
    "city": "Los Cabos",
    "status": "FINISHED",
    "homeScore": "-15",
    "awayScore": "-14",
    "marquee": False,
    "liveMinute": None,
    "image": IMG["golf"],
    "decidedBy": "score",
    "homePen": None,
    "awayPen": None,
    "sport": "golf",
    "competition": "pga-tour-2026",
    "format": "leaderboard",
    "season": "2026",
    "roundLabel": "Round 2",
    "resultSummary": "R2: Ben James 129 (-15) leads Peter Malnati 130. Blair 132. Cut 139. Round 3 unpublished.",
    "leaderboard": [
        {"pos": "1", "name": "Ben James", "score": "-15 (65-64)", "note": "36-hole leader"},
        {"pos": "2", "name": "Peter Malnati", "score": "-14 (66-64)", "note": "One back"},
        {"pos": "3", "name": "Zac Blair", "score": "-12 (64-68)", "note": "P3"},
        {"pos": "T4", "name": "Stephan Jaeger", "score": "-11 (133)", "note": "T4"},
        {"pos": "T4", "name": "Denny McCarthy", "score": "-11 (133)", "note": "T4"},
        {"pos": "T16", "name": "Chris Kirk", "score": "-9 (63-72)", "note": "R1 leader"}
    ],
    "tennisSets": [],
    "sources": [
        {"name": "AP/CBS: James fires 64 to take one-shot lead", "url": "https://www.cbssports.com/golf/leaderboard/pga-tour/31000136/world-wide-technology-championship/recap/"},
        {"name": "AP News WWT Championship", "url": "https://apnews.com/article/golf-3c730f124aa1ce9bd091b57cb2bc60fd"},
        {"name": "PGA Tour WWT Championship recap", "url": "https://www.pgatour.com/article/news/daily-wrapup/2026/11/05/round-1-world-wide-technology-championship-recap-el-cardonal-scores-leaderboard-results"}
    ]
}

soccer = {
    "slug": "leeds-vs-tottenham-mw10-2026",
    "headline": "Premier League MW10: Noah Okafor winner as Leeds beat Tottenham 1-0",
    "whyCareScore": 9.5,
    "whyCareReason": "Okafor scores 97 seconds after replacing Lukas Nmecha, a 79th-minute finish that ends Leeds' five-match winless run and Spurs' three-match winning run.",
    "teaser": "FINAL: Leeds 1-0 Tottenham. Okafor 79'. Attendance 36,921. Friday: Everton 3-1 Coventry (Gboho 52, Barry 56, 61, Dewsbury-Hall 81). Arsenal vs Hull unpublished.",
    "story": "Noah Okafor scored in the 79th minute as Leeds United beat Tottenham Hotspur 1-0 on Saturday, 7 November, at Elland Road. ESPN, Opta and PA report that Okafor needed 97 seconds after replacing Lukas Nmecha, finishing after Harry Wilson kept a long throw alive. It was Leeds' first substitute goal of the Premier League season and ended a five-match winless run. Tottenham's three-match winning run ended. Attendance: 36,921. Referee: John Brooks. Friday still stands: Everton 3-1 Coventry at Hill Dickinson Stadium, Yann Gboho 52, Thierno Barry 56 and 61, Kiernan Dewsbury-Hall 81, attendance 52,395, referee Stuart Attwell. David Moyes equalled Harry Catterick's club record of 592 games. Conservative Premier League table after those two finished MW10 matches only: Arsenal 24 from 9, Manchester City 21 from 9, Brighton 19 from 9, Chelsea 16 from 9, Everton 16 from 10, Liverpool 15 from 9, Brentford 14 from 9, Leeds 14 from 10. Arsenal vs Hull, Fulham vs Newcastle and the rest of Saturday's round are unpublished as unfinished.",
    "stakes": "Leeds climb to 14 points from 10 matches. Tottenham drop to 12 from 10. Everton sit fifth on 16 from 10 after Friday. Arsenal remain on 24 from 9 until Hull is finished.",
    "rivalryAngle": "Elland Road under Daniel Farke vs Roberto De Zerbi's Tottenham, with Okafor's first touch after a long throw deciding a tight game.",
    "funFacts": [
        "Okafor scored 97 seconds after coming on, the fastest substitute goal in the Premier League this season.",
        "Everton came from 0-1 down on Friday as Barry scored twice and assisted Dewsbury-Hall.",
        "Arsenal vs Hull is not published with a full-time score on this desk."
    ],
    "keyPlayers": [
        {"name": "Noah Okafor", "team": "Leeds United", "hook": "79th-minute winner, 97 seconds after replacing Nmecha."},
        {"name": "Thierno Barry", "team": "Everton", "hook": "Two goals and an assist in Friday's 3-1 win over Coventry."},
        {"name": "Harry Wilson", "team": "Leeds United", "hook": "Helped keep the long throw alive for Okafor's finish."}
    ],
    "headToHead": "Saturday 7 November 2026. Elland Road, Leeds. Final: Leeds 1-0 Tottenham.",
    "tags": ["soccer", "premier-league", "leeds", "tottenham", "okafor", "everton", "mw10"],
    "home": "Leeds United",
    "away": "Tottenham Hotspur",
    "homeCode": None,
    "awayCode": None,
    "homeFlag": "",
    "awayFlag": "",
    "group": "Premier League",
    "matchday": 10,
    "date": "2026-11-07",
    "time": "15:00",
    "venue": "Elland Road",
    "city": "Leeds",
    "status": "FINISHED",
    "homeScore": 1,
    "awayScore": 0,
    "marquee": True,
    "liveMinute": None,
    "image": IMG["soc"],
    "decidedBy": None,
    "homePen": None,
    "awayPen": None,
    "sport": "soccer",
    "competition": "premier-league-2026-27",
    "format": "team-match",
    "season": "2026/27",
    "roundLabel": "Premier League · Matchweek 10",
    "resultSummary": "FINAL: Leeds 1-0 Tottenham (Okafor 79). Friday: Everton 3-1 Coventry. Arsenal vs Hull unpublished.",
    "leaderboard": [],
    "tennisSets": [],
    "sources": [
        {"name": "ESPN: Leeds 1-0 Tottenham, Okafor winner", "url": "https://www.espn.co.uk/football/match/_/gameId/401878758/tottenham-hotspur-leeds-united"},
        {"name": "Opta Analyst: Okafor 97 seconds after coming on", "url": "https://theanalyst.com/articles/leeds-1-0-tottenham-stats-premier-league-11-2026"},
        {"name": "Everton FC: Barry double in 3-1 vs Coventry", "url": "https://www.evertonfc.com/news/2026/november/06/coventry-report/"}
    ]
}

matches = [nfl, nba, ten, f1, golf, soccer]
for m in matches:
    dump(os.path.join(MATCHES, m["slug"] + ".json"), m)

stories = {
"nfl-week9-saturday-madrid-bengals-falcons-preview-2026.md": f"""---
title: "NFL Week 9 Madrid: Bengals visit Falcons at Bernabeu on Sunday, 9:30 a.m. ET"
subtitle: "Saturday has no NFL game. Cincinnati 5-2 meets Atlanta 3-5 in Spain. Last final remains Jaguars 33, Ravens 10 on TNF."
category: "Desk"
excerpt: "The Cincinnati Bengals play the Atlanta Falcons on Sunday at Santiago Bernabeu Stadium. Kickoff is 9:30 a.m. ET on NFL Network. No score."
image: "{IMG['nfl']}"
readingTime: 5
pubDate: 2026-11-07
sport: football
competition: nfl-2026
relatedSlug: bengals-at-falcons-madrid-week9-2026
sources:
  - name: "NFL.com: Bengals vs Falcons Week 9 Madrid preview"
    url: "https://www.nfl.com/news/bengals-vs-falcons-preview-week-9-madrid-game"
  - name: "Bengals.com: What to watch in Madrid"
    url: "https://www.bengals.com/news/game-preview-2026-week-9-bengals-falcons"
  - name: "Bengals international Madrid hub"
    url: "https://www.bengals.com/international-madrid-2026/"
---

## No Saturday NFL game, Madrid on Sunday

Saturday 7 November has no NFL game. The next board is Sunday: Cincinnati Bengals at Atlanta Falcons, Santiago Bernabeu Stadium, Madrid, 9:30 a.m. ET (3:30 p.m. local) on NFL Network. Atlanta is the designated home team. This desk publishes no score.

Cincinnati is 5-2 on a three-game winning streak after a 43-36 overtime win over Tennessee. Atlanta is 3-5 after a loss to Tampa Bay. Bengals.com lists Joe Burrow as the NFL leader in completion percentage (73.0), passing touchdowns (20) and passing yards per game (302.1). Bijan Robinson leads the league with 780 rushing yards at 5.2 yards per carry.

## Last final still stands

Thursday 5 November at M&T Bank Stadium remains the last finished NFL result: Jacksonville Jaguars 33, Baltimore Ravens 10. Trevor Lawrence threw for 242 yards and a 50-yard touchdown. Cam Little made four field goals. Joe Fagnano threw two interceptions. Jaguars 6-2, Ravens 4-5. Pittsburgh is 6-2 atop the AFC North on a Week 9 bye with Tennessee. Sunday's other Week 9 scores are unpublished.
""",
"nba-doncic-53-lakers-beat-blazers-124-118-2026.md": f"""---
title: "NBA: Luka Doncic scores 53 as Lakers rally past Trail Blazers 124-118"
subtitle: "Eleventh career 50-point game, a 62-foot heave at the half, and a jumper with 28 seconds left. Lakers fourth straight win."
category: "Desk"
excerpt: "Luka Doncic scored 53 points as the Los Angeles Lakers beat the Portland Trail Blazers 124-118 on Friday night at Crypto.com Arena."
image: "{IMG['nba']}"
readingTime: 5
pubDate: 2026-11-07
sport: basketball
competition: nba-2026-27
relatedSlug: nba-lakers-vs-blazers-doncic-53-2026
sources:
  - name: "NBA.com: Doncic scores 53, Lakers beat Blazers 124-118"
    url: "https://www.nba.com/game/por-vs-lal-0022600032"
  - name: "Reuters: Doncic pours in 53 as Lakers rally past Blazers"
    url: "https://www.reuters.com/sports/basketball/luka-doncic-pours-53-lakers-rally-past-blazers--flm-2026-11-07/"
  - name: "AP via NBA recap"
    url: "https://apnews.com/article/lakers-trail-blazers-doncic-reaves-nba-bb443859434a2393d510a4db8d84795c"
---

## Fifty-three in Los Angeles

Luka Doncic scored 53 points as the Los Angeles Lakers beat the Portland Trail Blazers 124-118 on Friday, 6 November, at Crypto.com Arena. The Associated Press listed his 11th career 50-point game and his fourth in a Lakers uniform. He shot 17 of 33 from the field and 5 of 15 from three, with five rebounds and five assists.

Portland led by as many as 16 in the first half. Doncic's 62-foot heave at the buzzer made it 60-53 at the break. He scored 20 in the third quarter. A late 12-point Lakers lead shrank to four before Doncic's jumper with 28 seconds left and Austin Reaves' finishing points. Reaves scored 25. Walker Kessler had 16 points and 12 rebounds. Deni Avdija had 22 points, nine rebounds and 11 assists. Damian Lillard scored 22.

## Other Friday boards

San Antonio beat Sacramento 124-109. Victor Wembanyama had 30 points and 14 rebounds. The Spurs are 7-2 on a seventh straight win. Cleveland beat Philadelphia 119-95 (Donovan Mitchell 23, Evan Mobley 22). Cavaliers are 5-4. 76ers are 8-2. Boston beat Charlotte 119-80 (Jayson Tatum 34). Saturday NBA games are unpublished.
""",
"atp-paris-masters-2026-shelton-beats-van-assche-reaches-final.md": f"""---
title: "Rolex Paris Masters SF: Ben Shelton beats Luca Van Assche 5-7, 6-3, 6-4 to reach the final"
subtitle: "First American Bercy finalist since Jack Sock in 2017. Alcaraz vs Ruud is unpublished."
category: "Desk"
excerpt: "Ben Shelton rallied from a break down in the third set to beat Luca Van Assche 5-7, 6-3, 6-4 and reach the Rolex Paris Masters final."
image: "{IMG['ten']}"
readingTime: 5
pubDate: 2026-11-07
sport: tennis
competition: atp-1000-paris-2026
relatedSlug: atp-paris-masters-2026-shelton-vs-van-assche-sf
sources:
  - name: "AP: Shelton rallies to reach Paris Masters final"
    url: "https://apnews.com/article/paris-masters-alcaraz-shelton-ruud-van-assche-3d7b1f4f30531b1424f2539089383f73"
  - name: "Reuters via Straits Times: Shelton outwits Van Assche"
    url: "https://www.straitstimes.com/sport/tennis/shelton-outwits-hometown-hope-van-assche-to-reach-paris-masters-final"
  - name: "ATP Paris results"
    url: "https://www.atptour.com/en/scores/current/paris/352/results"
---

## Shelton through to Sunday

Ben Shelton beat Luca Van Assche 5-7, 6-3, 6-4 on Saturday, 7 November, at Accor Arena. The Associated Press says the third seed recovered from a 3-1 deficit in the deciding set, winning four straight games before serving out the match. Shelton is the first American to reach the Paris Masters final since Jack Sock won the title in 2017. It is his third ATP Masters 1000 final and his first outside Canada.

Van Assche, ranked 47th, was in his first Masters semi-final and took the opening set 7-5 in front of a home crowd.

## Friday quarter-finals, second semi unpublished

Friday still stands: Shelton d Tommy Paul 6-4, 4-6, 6-3; Carlos Alcaraz d Taylor Fritz 6-7(10), 7-5, 6-3 after saving two match points; Casper Ruud d Nuno Borges 7-6(5), 6-4; Van Assche d Rinky Hijikata 6-4, 6-7(4), 7-5. Alcaraz vs Ruud later Saturday is unpublished as unfinished. Sunday's final is unpublished.
""",
"f1-sao-paulo-gp-2026-fp3-verstappen-leads-antonelli.md": f"""---
title: "Sao Paulo GP FP3: Max Verstappen leads Kimi Antonelli by 0.025s at Interlagos"
subtitle: "Final practice complete. Qualifying is unpublished. No Sprint this weekend. Mercedes 630, Ferrari 504."
category: "Desk"
excerpt: "Max Verstappen set 1:11.622 in Saturday FP3 at Interlagos, 0.025 seconds ahead of world champion Kimi Antonelli. Qualifying is unpublished."
image: "{IMG['f1']}"
readingTime: 5
pubDate: 2026-11-07
sport: f1
competition: f1-2026
relatedSlug: sao-paulo-gp-interlagos-2026
sources:
  - name: "FIA FP3 classification, Sao Paulo 2026"
    url: "https://www.fia.com/system/files/decision-document/2026_sao_paulo_grand_prix_-_free_practice_3_classification.pdf"
  - name: "ESPN F1 Sao Paulo weekend results"
    url: "https://www.espn.com/f1/results/_/id/600057448"
  - name: "ESPN F1 2026 drivers standings"
    url: "https://www.espn.com/f1/standings"
---

## Verstappen by twenty-five thousandths

Max Verstappen topped Free Practice 3 on Saturday, 7 November, at Autodromo Jose Carlos Pace in 1:11.622. The FIA sheet lists Kimi Antonelli 0.025 seconds behind, Lando Norris +0.131s, George Russell +0.184s, Charles Leclerc +0.274s and Oscar Piastri +0.313s. Lewis Hamilton completed seven laps and finished 12th.

Friday still stands. FP1: Norris 1:11.717, Antonelli +0.082s, Verstappen +0.236s. FP2: Antonelli 1:10.763, Norris +0.253s, Verstappen +0.259s.

## Qualifying is not this desk

There is no Sprint in Sao Paulo in 2026. Saturday qualifying is unpublished as unfinished. Championship standings after Mexico are unchanged: Antonelli 380, Verstappen 261, Hamilton 259, Russell 250, Leclerc 245, Norris 221. Constructors: Mercedes 630, Ferrari 504, Red Bull 382, McLaren 365.
""",
"pga-tour-wwt-championship-2026-round2-james-leads-malnati.md": f"""---
title: "WWT Championship Round 2: Ben James shoots 64 to lead at 15 under at El Cardonal"
subtitle: "James 65-64=129 leads Peter Malnati by one. Chris Kirk follows 63 with 72. Round 3 unpublished as final."
category: "Desk"
excerpt: "Ben James posted a 64 on Friday to reach 15-under 129 and lead the World Wide Technology Championship after 36 holes in Los Cabos."
image: "{IMG['golf']}"
readingTime: 5
pubDate: 2026-11-07
sport: golf
competition: pga-tour-2026
relatedSlug: wwt-championship-diamante-cabo-2026
sources:
  - name: "AP/CBS: James fires 64 to take one-shot lead"
    url: "https://www.cbssports.com/golf/leaderboard/pga-tour/31000136/world-wide-technology-championship/recap/"
  - name: "AP News WWT Championship"
    url: "https://apnews.com/article/golf-3c730f124aa1ce9bd091b57cb2bc60fd"
  - name: "PGA Tour WWT Championship"
    url: "https://www.pgatour.com/tournaments/2026/world-wide-technology-championship/R2026018"
---

## James in front after 36 holes

Ben James shot an 8-under 64 on Friday, 6 November, and leads the World Wide Technology Championship at 15-under 129. Associated Press copy says he ran off five straight birdies around the turn at El Cardonal at Diamante (par 72, 7,452 yards) and finished with one more birdie. Peter Malnati is one back at 130 after 66-64. Zac Blair is at 132. Stephan Jaeger and Denny McCarthy share fourth at 133.

Chris Kirk led after a bogey-free 63 on Thursday, then shot 72 and sits at 135. The cut was 5-under 139. The purse is $6 million.

## Round 3 is not the desk

Saturday's third round is in progress and is not published as a finished 54-hole board. Live widgets that move James or Malnati during round 3 are not treated as a closed leaderboard.
""",
"pl-mw10-leeds-1-0-tottenham-okafor-2026.md": f"""---
title: "Premier League MW10: Noah Okafor winner as Leeds beat Tottenham 1-0"
subtitle: "Okafor scores 97 seconds after coming on. Friday: Everton 3-1 Coventry. Arsenal vs Hull unpublished."
category: "Desk"
excerpt: "Noah Okafor scored in the 79th minute as Leeds United beat Tottenham Hotspur 1-0 at Elland Road on Saturday."
image: "{IMG['soc']}"
readingTime: 5
pubDate: 2026-11-07
sport: soccer
competition: premier-league-2026-27
relatedSlug: leeds-vs-tottenham-mw10-2026
sources:
  - name: "ESPN: Leeds 1-0 Tottenham, Okafor winner"
    url: "https://www.espn.co.uk/football/match/_/gameId/401878758/tottenham-hotspur-leeds-united"
  - name: "Opta Analyst: Okafor 97 seconds after coming on"
    url: "https://theanalyst.com/articles/leeds-1-0-tottenham-stats-premier-league-11-2026"
  - name: "Everton FC: Barry double in 3-1 vs Coventry"
    url: "https://www.evertonfc.com/news/2026/november/06/coventry-report/"
---

## One touch, one point swing at Elland Road

Leeds United beat Tottenham Hotspur 1-0 on Saturday, 7 November, at Elland Road. Noah Okafor scored in the 79th minute, 97 seconds after replacing Lukas Nmecha. ESPN and Opta say Harry Wilson helped keep a long throw alive before Okafor finished past Antonin Kinsky. Attendance: 36,921. Referee: John Brooks. The result ended Leeds' five-match winless run and Tottenham's three-match winning run.

## Friday and the unpublished rest

Friday 6 November: Everton 3-1 Coventry at Hill Dickinson Stadium. Yann Gboho 52, Thierno Barry 56 and 61, Kiernan Dewsbury-Hall 81. Attendance 52,395. Referee Stuart Attwell. David Moyes equalled Harry Catterick's 592 games in charge.

Conservative table after those two finished MW10 matches only: Arsenal 24 from 9, Manchester City 21 from 9, Brighton 19, Chelsea 16, Everton 16 from 10, Liverpool 15, Brentford 14, Leeds 14 from 10. Arsenal vs Hull, Fulham vs Newcastle and the rest of Saturday's round are unpublished as unfinished.
""",
}

for name, body in stories.items():
    path = os.path.join(STORIES, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(body)
    print("wrote", path)

# sports.ts
sports_path = os.path.join(ROOT, "frontend/src/data/sports.ts")
with open(sports_path, "r", encoding="utf-8") as f:
    st = f.read()
st = st.replace("export const SITE_TODAY = '2026-11-06';", "export const SITE_TODAY = '2026-11-07';")
replacements = {
    "NFL Week 9 TNF: Jaguars thrash depleted Ravens 33-10 behind Lawrence, four Little field goals.":
    "NFL Week 9 Madrid: Bengals visit Falcons at Bernabeu on Sunday, 9:30 a.m. ET. Saturday has no NFL game.",
    "Final in Baltimore: Jaguars 33, Ravens 10. Lawrence 242 yds, 50-yd TD; Little 4 FGs; Fagnano 2 INT. Jaguars 6-2, Ravens 4-5.":
    "UPCOMING Sunday in Madrid: Bengals (5-2) at Falcons (3-5), 9:30 a.m. ET, NFL Network. Last final: Jaguars 33, Ravens 10. No Saturday game.",
    "NFL WEEK 9 TNF: JACKSONVILLE JAGUARS THRASH RAVENS 33-10; JAGUARS 6-2, RAVENS 4-5":
    "NFL WEEK 9 MADRID: BENGALS AT FALCONS SUNDAY 9:30 A.M. ET; LAST FINAL JAGUARS 33-10",
    "NBA: Wembanyama posts 52 points, 24 rebounds, 8 blocks as Spurs edge Mavericks 112-111.":
    "NBA: Luka Doncic scores 53 as Lakers rally past Trail Blazers 124-118.",
    "Final in San Antonio: Spurs 112, Mavericks 111. Wembanyama 52-24-8; winning FT 24.2s. Spurs 6-2. Cavs are 4-4.":
    "Final in Los Angeles: Lakers 124, Trail Blazers 118. Doncic 53; Reaves 25. Spurs 7-2. Cavs are 5-4.",
    "NBA: WEMBANYAMA 52-24-8 AS SPURS EDGE MAVERICKS 112-111 FOR SIXTH STRAIGHT":
    "NBA: DONCIC 53 AS LAKERS BEAT TRAIL BLAZERS 124-118; SPURS 7-2, CAVS 5-4",
    "UCL MD4: Haaland winner as Manchester City edge RB Leipzig 3-2. Arsenal lead Premier League on 24 points.":
    "Premier League MW10: Noah Okafor winner as Leeds beat Tottenham 1-0. Arsenal still 24 from 9.",
    "Final in Leipzig: RB Leipzig 2-3 Manchester City (Lukeba OG 37, Baku 49, Fernandez 58, Nusa 61, Haaland 78). City 3-1, 7th in UCL.":
    "Final at Elland Road: Leeds 1-0 Tottenham (Okafor 79). Friday: Everton 3-1 Coventry. Arsenal vs Hull unpublished.",
    "UCL MD4: HAALAND 78TH-MINUTE WINNER LIFTS CITY PAST LEIPZIG 3-2; ARSENAL LEAD PL ON 24":
    "PREMIER LEAGUE MW10: OKAFOR 79TH-MINUTE WINNER LIFTS LEEDS PAST TOTTENHAM 1-0",
    "Rolex Paris Masters QF: Ben Shelton beats Tommy Paul 6-4, 4-6, 6-3 to reach first Bercy semi-final.":
    "Rolex Paris Masters SF: Ben Shelton beats Luca Van Assche 5-7, 6-3, 6-4 to reach the final.",
    "Paris Masters QF: Shelton def. Paul 6-4, 4-6, 6-3 in 1h46m, 19 aces. Tiafoe qualifies for Turin; Paul is out.":
    "Paris Masters SF: Shelton def. Van Assche 5-7, 6-3, 6-4. First American finalist since Sock 2017. Alcaraz vs Ruud unpublished.",
    "ROLEX PARIS MASTERS: BEN SHELTON BEATS TOMMY PAUL TO REACH FIRST BERCY SEMI-FINAL":
    "ROLEX PARIS MASTERS: BEN SHELTON BEATS VAN ASSCHE TO REACH THE BERCY FINAL",
    "São Paulo GP FP1: Lando Norris leads Kimi Antonelli and Max Verstappen at Interlagos.":
    "Sao Paulo GP FP3: Max Verstappen leads Kimi Antonelli by 0.025s at Interlagos.",
    "FP1: Norris 1:11.717, Antonelli +0.082s, Verstappen +0.236s. No Sprint. Mercedes 630, Ferrari 504 after Mexico.":
    "FP3: Verstappen 1:11.622, Antonelli +0.025s, Norris +0.131s. Qualifying unpublished. Mercedes 630, Ferrari 504.",
    "F1 INTERLAGOS FP1: NORRIS LEADS ANTONELLI; NO SPRINT; MERCEDES 630, FERRARI 504":
    "F1 INTERLAGOS FP3: VERSTAPPEN LEADS ANTONELLI BY 0.025S; QUALIFYING UNPUBLISHED",
    "WWT Championship Round 1: Chris Kirk fires bogey-free 63 to lead by one at El Cardonal.":
    "WWT Championship Round 2: Ben James shoots 64 to lead at 15 under at El Cardonal.",
    "R1 complete: Kirk 63 leads Dunlap and Blair 64. Purse $6 million. Round 2 in progress, unpublished as final.":
    "R2 complete: James 129 (-15) leads Malnati 130. Kirk 135. Cut 139. Round 3 unpublished as final.",
    "PGA TOUR CABO R1: CHRIS KIRK 63 LEADS WWT CHAMPIONSHIP; FEDEXCUP FALL CARDS ON THE LINE":
    "PGA TOUR CABO R2: BEN JAMES 129 LEADS WWT CHAMPIONSHIP; ROUND 3 UNPUBLISHED",
}
for old, new in replacements.items():
    if old not in st:
        print("WARN sports.ts missing:", old[:80])
    st = st.replace(old, new)
with open(sports_path, "w", encoding="utf-8") as f:
    f.write(st)
print("updated sports.ts")

# desk.json
desk_path = os.path.join(ROOT, "frontend/src/data/desk.json")
with open(desk_path, "r", encoding="utf-8") as f:
    desk = json.load(f)
desk["asOf"] = "2026-11-07"
desk["premierLeagueTable"] = [
    {"pos": 1, "team": "Arsenal", "p": 9, "w": 8, "d": 0, "l": 1, "gf": 14, "ga": 5, "gd": 9, "pts": 24},
    {"pos": 2, "team": "Manchester City", "p": 9, "w": 7, "d": 0, "l": 2, "gf": 20, "ga": 10, "gd": 10, "pts": 21},
    {"pos": 3, "team": "Brighton", "p": 9, "w": 6, "d": 1, "l": 2, "gf": 24, "ga": 7, "gd": 17, "pts": 19},
    {"pos": 4, "team": "Chelsea", "p": 9, "w": 5, "d": 1, "l": 3, "gf": 19, "ga": 15, "gd": 4, "pts": 16},
    {"pos": 5, "team": "Everton", "p": 10, "w": 4, "d": 4, "l": 2, "gf": 12, "ga": 10, "gd": 2, "pts": 16},
    {"pos": 6, "team": "Liverpool", "p": 9, "w": 4, "d": 3, "l": 2, "gf": 11, "ga": 9, "gd": 2, "pts": 15},
    {"pos": 7, "team": "Brentford", "p": 9, "w": 3, "d": 5, "l": 1, "gf": 16, "ga": 9, "gd": 7, "pts": 14},
    {"pos": 8, "team": "Leeds United", "p": 10, "w": 3, "d": 5, "l": 2, "gf": 10, "ga": 8, "gd": 2, "pts": 14},
    {"pos": 9, "team": "Bournemouth", "p": 9, "w": 3, "d": 3, "l": 3, "gf": 14, "ga": 13, "gd": 1, "pts": 12},
    {"pos": 10, "team": "Tottenham Hotspur", "p": 10, "w": 3, "d": 3, "l": 4, "gf": 10, "ga": 11, "gd": -1, "pts": 12},
    {"pos": 11, "team": "Aston Villa", "p": 9, "w": 3, "d": 3, "l": 3, "gf": 10, "ga": 13, "gd": -3, "pts": 12},
    {"pos": 12, "team": "Hull City", "p": 9, "w": 2, "d": 5, "l": 2, "gf": 11, "ga": 10, "gd": 1, "pts": 11},
    {"pos": 13, "team": "Newcastle United", "p": 9, "w": 3, "d": 2, "l": 4, "gf": 12, "ga": 15, "gd": -3, "pts": 11},
    {"pos": 14, "team": "Ipswich", "p": 9, "w": 3, "d": 2, "l": 4, "gf": 14, "ga": 18, "gd": -4, "pts": 11},
    {"pos": 15, "team": "Fulham", "p": 9, "w": 2, "d": 3, "l": 4, "gf": 9, "ga": 11, "gd": -2, "pts": 9},
    {"pos": 16, "team": "Coventry", "p": 10, "w": 3, "d": 0, "l": 7, "gf": 10, "ga": 19, "gd": -9, "pts": 9},
    {"pos": 17, "team": "Manchester United", "p": 9, "w": 1, "d": 4, "l": 4, "gf": 10, "ga": 15, "gd": -5, "pts": 7},
    {"pos": 18, "team": "Crystal Palace", "p": 9, "w": 2, "d": 1, "l": 6, "gf": 9, "ga": 21, "gd": -12, "pts": 7},
    {"pos": 19, "team": "Nottingham Forest", "p": 9, "w": 1, "d": 3, "l": 5, "gf": 6, "ga": 12, "gd": -6, "pts": 6},
    {"pos": 20, "team": "Sunderland", "p": 9, "w": 1, "d": 2, "l": 6, "gf": 7, "ga": 17, "gd": -10, "pts": 5},
]
desk["nflWeek1"].append({
    "date": "2026-11-08",
    "time": "9:30 a.m. ET",
    "home": "Atlanta Falcons",
    "away": "Cincinnati Bengals",
    "note": "UPCOMING: Bengals at Falcons, Santiago Bernabeu, Madrid. NFL Network. CIN 5-2, ATL 3-5. No score. Saturday 7 Nov has no NFL game. Last final: Jaguars 33, Ravens 10."
})
desk["usOpenQF"].append({
    "draw": "Paris QF",
    "p1": "Carlos Alcaraz",
    "p2": "Taylor Fritz",
    "status": "Alcaraz 6-7(10), 7-5, 6-3"
})
desk["usOpenQF"].append({
    "draw": "Paris QF",
    "p1": "Casper Ruud",
    "p2": "Nuno Borges",
    "status": "Ruud 7-6(5), 6-4"
})
desk["usOpenQF"].append({
    "draw": "Paris QF",
    "p1": "Luca Van Assche",
    "p2": "Rinky Hijikata",
    "status": "Van Assche 6-4, 6-7(4), 7-5"
})
desk["usOpenQF"].append({
    "draw": "Paris SF",
    "p1": "Ben Shelton",
    "p2": "Luca Van Assche",
    "status": "Shelton 5-7, 6-3, 6-4"
})
with open(desk_path, "w", encoding="utf-8") as f:
    json.dump(desk, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("updated desk.json, PL rows", len(desk["premierLeagueTable"]))

# AGENTS.md clock
agents = os.path.join(ROOT, "AGENTS.md")
with open(agents, "r", encoding="utf-8") as f:
    ag = f.read()
old_clock = "*   **Site clock:** editorial today is `2026-11-06`"
idx = ag.find(old_clock)
if idx == -1:
    print("WARN AGENTS clock line not found")
else:
    end = ag.find("\n\n---", idx)
    new_clock = (
        "*   **Site clock:** editorial today is `2026-11-07` in `frontend/src/data/sports.ts` (`SITE_TODAY`). "
        "Football: Saturday 7 Nov has no NFL game. Sunday Madrid preview: Cincinnati Bengals at Atlanta Falcons, 9:30 a.m. ET at Santiago Bernabeu, NFL Network, CIN 5-2, ATL 3-5, unpublished as a score. Last NFL final remains Thursday 5 Nov: Jaguars 33, Ravens 10. Steelers 6-2 on a Week 9 bye. "
        "Basketball: Luka Doncic scores 53 as Los Angeles Lakers beat Portland Trail Blazers 124-118 on 6 Nov; Lakers on a four-game streak. Spurs 7-2. Cavaliers are 5-4. 76ers 8-2. "
        "Soccer: Noah Okafor 79th-minute winner as Leeds beat Tottenham 1-0 on 7 Nov. Friday: Everton 3-1 Coventry. Conservative PL after those two MW10 finals: Arsenal 24 from 9, City 21, Brighton 19, Chelsea 16, Everton 16 from 10, Leeds 14 from 10. Arsenal vs Hull unpublished. "
        "Tennis: Ben Shelton beats Luca Van Assche 5-7, 6-3, 6-4 in the Rolex Paris Masters semi-finals on 7 Nov; first American finalist since Sock 2017. Alcaraz vs Ruud unpublished. "
        "Formula 1: Max Verstappen leads Sao Paulo GP FP3 in 1:11.622 from Antonelli (+0.025s) and Norris. No Sprint. Qualifying unpublished. After Mexico, Antonelli is champion on 380; Mercedes 630, Ferrari 504. "
        "Golf: Ben James 65-64=129 leads WWT Championship after round 2 at El Cardonal; Malnati 130, Blair 132. Kirk 63-72=135. Cut 139. Round 3 unpublished as final."
    )
    ag = ag[:idx] + new_clock + ag[end:]
    with open(agents, "w", encoding="utf-8") as f:
        f.write(ag)
    print("updated AGENTS.md")

# Homepage / LivePage featured fallback
for rel in ["frontend/src/views/HomePage.astro", "frontend/src/views/LivePage.astro"]:
    path = os.path.join(ROOT, rel)
    with open(path, "r", encoding="utf-8") as f:
        txt = f.read()
    needle = "matches.find((m) => m.slug === 'jaguars-at-ravens-tnf-week9-2026') ||"
    insert = "matches.find((m) => m.slug === 'nba-lakers-vs-blazers-doncic-53-2026') ||\n  " + needle
    if "nba-lakers-vs-blazers-doncic-53-2026" not in txt:
        if needle not in txt:
            print("WARN featured needle missing in", rel)
        else:
            txt = txt.replace(needle, insert, 1)
            with open(path, "w", encoding="utf-8") as f:
                f.write(txt)
            print("featured slug added in", rel)

# dash lint (skip YAML fences and URLs)
def lint_text(s):
    s = re.sub(r"https?://\S+", "", s)
    s = s.replace("---", "")
    if "—" in s or "--" in s:
        raise SystemExit("em-dash or double-hyphen found: " + s[max(0, s.find("--")-40):s.find("--")+40] if "--" in s else s[max(0, s.find("—")-40):s.find("—")+40])

for m in matches:
    lint_text(json.dumps(m, ensure_ascii=False))
for body in stories.values():
    lint_text(body)
print("dash lint ok")

print("apply_nov07_desk.py done")
