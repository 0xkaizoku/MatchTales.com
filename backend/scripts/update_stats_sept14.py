#!/usr/bin/env python3
"""Write sourced 14 September 2026 desk events. Scores only from named reports."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2] / "frontend" / "src" / "content" / "matches"

IMG = {
    "soccer": "https://images.unsplash.com/photo-1574629810360-7efbbe195018?auto=format&fit=crop&w=1200&q=80",
    "tennis": "https://images.unsplash.com/photo-1554068865-24cecd4e34b8?auto=format&fit=crop&w=1200&q=80",
    "golf": "https://images.unsplash.com/photo-1535131749006-b7f58c99034b?auto=format&fit=crop&w=1200&q=80",
    "football": "https://images.unsplash.com/photo-1566577739112-5184e6ac4a4e?auto=format&fit=crop&w=1200&q=80",
    "basketball": "https://images.unsplash.com/photo-1546519638-68e109498ffc?auto=format&fit=crop&w=1200&q=80",
    "f1": "https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?auto=format&fit=crop&w=1200&q=80",
}


def ev(**kwargs):
    sport = kwargs["sport"]
    base = {
        "funFacts": kwargs.pop("funFacts"),
        "keyPlayers": kwargs.pop("keyPlayers"),
        "headToHead": kwargs.pop("headToHead", ""),
        "tags": kwargs.pop("tags", []),
        "homeCode": kwargs.pop("homeCode", None),
        "awayCode": kwargs.pop("awayCode", None),
        "homeFlag": "",
        "awayFlag": "",
        "matchday": kwargs.pop("matchday", 0),
        "marquee": True,
        "liveMinute": kwargs.pop("liveMinute", None),
        "image": kwargs.pop("image", IMG[sport]),
        "decidedBy": kwargs.pop("decidedBy", None),
        "homePen": None,
        "awayPen": None,
        "season": kwargs.pop("season", ""),
        "roundLabel": kwargs.pop("roundLabel", ""),
        "resultSummary": kwargs.pop("resultSummary", ""),
        "leaderboard": kwargs.pop("leaderboard", []),
        "tennisSets": kwargs.pop("tennisSets", []),
        "sources": kwargs.pop("sources", []),
        "format": kwargs.pop("format", "team-match"),
        "homeScore": kwargs.pop("homeScore", None),
        "awayScore": kwargs.pop("awayScore", None),
    }
    base.update(kwargs)
    return base


EVENTS = []

EVENTS.append(ev(
    slug="tiafoe-vs-michelsen-uso-qf",
    headline="Tiafoe from two sets down, then 0-3 in the fifth, then a semi-final",
    whyCareScore=9.7,
    whyCareReason="Michelsen served for the match at 5-4 in the third. Tiafoe won 7-6 (10-6) in the fifth after 4 hours 38 minutes.",
    teaser="Tiafoe 5-7, 3-6, 7-5, 6-3, 7-6 (10-6) Michelsen. Two sets down. 0-3 in the fifth. A hug at the net.",
    story="Why this one matters: an all-American quarter-final on Ashe was supposed to end in the third set. It ended in a 10-point tie-break, with Alex Michelsen crying on Frances Tiafoe's shoulder.\n\nATP logged the score as 5-7, 3-6, 7-5, 6-3, 7-6 (10-6), 4 hours 38 minutes. Michelsen had not dropped a set in the tournament. He served for the match at 5-4 in the third and double-faulted twice. Tiafoe, the eleventh seed, took that set 7-5, the fourth 6-3, then trailed 0-3 in the fifth. The match tie-break went 10-6 on a Tiafoe forehand down the line.\n\nBBC, ATP and USOpen.org agree on the same numbers. Tiafoe reaches a third US Open semi-final. Michelsen finished with more total points, 173-170, and still lost. The next sentence was Shelton.",
    stakes="A first American men's semi-final pairing at this Open. One of them had already beaten Alcaraz.",
    rivalryAngle="Friends, same country, one court, a 23-year drought still unsolved.",
    funFacts=["Michelsen served for the match at 5-4 in the third.", "Tiafoe trailed 0-3 in the fifth.", "ATP: 4 hours 38 minutes, 40 break points, both broke eight times."],
    keyPlayers=[{"name": "Frances Tiafoe", "team": "USA", "hook": "Eleventh seed. Two sets down. Third US Open semi-final."}, {"name": "Alex Michelsen", "team": "USA", "hook": "First Slam quarter-final. Led two sets, 5-4 in the third, 3-0 in the fifth."}],
    home="Frances Tiafoe", away="Alex Michelsen", group="GS", date="2026-09-08", time="13:00",
    venue="Arthur Ashe Stadium", city="New York", status="FINISHED", format="singles",
    homeScore=3, awayScore=2,
    sport="tennis", competition="us-open-2026", roundLabel="Men's quarter-final",
    resultSummary="Tiafoe 5-7, 3-6, 7-5, 6-3, 7-6 (10-6) Michelsen",
    tennisSets=[{"p1": "5", "p2": "7"}, {"p1": "3", "p2": "6"}, {"p1": "7", "p2": "5"}, {"p1": "6", "p2": "3"}, {"p1": "7", "p2": "6"}],
    image="https://images.pexels.com/photos/209977/pexels-photo-209977.jpeg?auto=compress&cs=tinysrgb&w=1600&h=900&fit=crop",
    tags=["us-open", "tiafoe", "michelsen"],
    sources=[{"name": "ATP: Tiafoe rallies past Michelsen", "url": "https://www.atptour.com/en/news/michelsen-tiafoe-us-open-2026-qf-tuesday"}, {"name": "BBC: Tiafoe beats Michelsen", "url": "https://www.bbc.co.uk/sport/tennis/articles/c33k6zl5m87o"}],
))

EVENTS.append(ev(
    slug="alcaraz-vs-shelton-uso-qf",
    headline="Shelton beats Alcaraz at 3:33 a.m., the latest finish in US Open history",
    whyCareScore=9.8,
    whyCareReason="Defending champion, four months out with a wrist, out in five. A 146 mph ace closed a 10-7 match tie-break.",
    teaser="Shelton 6-7 (5), 6-1, 6-3, 1-6, 7-6 (10-7) Alcaraz. Four hours 28 minutes. Record late finish.",
    story="Why this one matters: Carlos Alcaraz came back from a right-wrist layoff to defend a US Open. Ben Shelton ended it after 3:33 a.m. in New York, the latest finish in tournament history.\n\nATP logged 6-7 (5), 6-1, 6-3, 1-6, 7-6 (10-7). BBC printed the same sets and the 10-7 match tie-break. Alcaraz took the first breaker 7-5. Shelton ran nine games in a row through the second and third. Alcaraz took the fourth 6-1. In the fifth-set tie-break Alcaraz led 5-3. Shelton won seven of the next nine points and closed with a 146 mph ace.\n\nIt was Shelton's first win over a top-three player. Alcaraz made 53 unforced errors to Shelton's 35, per Bleacher Report. The next match was Tiafoe. The American drought since Roddick in 2003 still had a finalist.",
    stakes="A defending champion gone. An American in the final four. A record clock.",
    rivalryAngle="Home lefty versus the favourite who had not lost to an American at a Slam.",
    funFacts=["Finished 3:33 a.m. ET, latest US Open finish on record.", "Alcaraz led 5-3 in the match tie-break.", "Shelton's first Top-3 win."],
    keyPlayers=[{"name": "Ben Shelton", "team": "USA", "hook": "Eighth seed. 146 mph ace to close it."}, {"name": "Carlos Alcaraz", "team": "Spain", "hook": "Defending champion, wrist return, 53 unforced errors."}],
    home="Carlos Alcaraz", away="Ben Shelton", group="GS", date="2026-09-08", time="19:00",
    venue="Arthur Ashe Stadium", city="New York", status="FINISHED", format="singles",
    homeScore=2, awayScore=3,
    sport="tennis", competition="us-open-2026", roundLabel="Men's quarter-final",
    resultSummary="Shelton 6-7 (5), 6-1, 6-3, 1-6, 7-6 (10-7) Alcaraz",
    tennisSets=[{"p1": "7", "p2": "6"}, {"p1": "1", "p2": "6"}, {"p1": "3", "p2": "6"}, {"p1": "6", "p2": "1"}, {"p1": "6", "p2": "7"}],
    image="https://images.pexels.com/photos/209969/pexels-photo-209969.jpeg?auto=compress&cs=tinysrgb&w=1600&h=900&fit=crop",
    tags=["us-open", "alcaraz", "shelton"],
    sources=[{"name": "ATP: Shelton upsets Alcaraz", "url": "https://www.atptour.com/en/news/alcaraz-shelton-us-open-2026-qf"}, {"name": "BBC: Shelton beats Alcaraz", "url": "https://www.bbc.com/sport/tennis/articles/c20v6pgz7nmo"}],
))

EVENTS.append(ev(
    slug="zverev-vs-shelton-uso-final",
    headline="Zverev beats Shelton in four: second Slam of 2026, first US Open",
    whyCareScore=9.9,
    whyCareReason="A first two majors in the same season. Shelton took the third set. Zverev took the title 6-2 in the fourth.",
    teaser="Zverev 6-3, 7-6 (2), 5-7, 6-2 Shelton. 3 hours 33 minutes. Roland Garros, then New York.",
    story="Why this one matters: Alexander Zverev already had Roland Garros. On 13 September he added the US Open, 6-3, 7-6 (2), 5-7, 6-2 over Ben Shelton, and became the fourth man in the Open Era to win his first two Grand Slam titles in the same calendar year.\n\nATP: Shelton double-faulted on break points in the first set. Zverev ran the second-set tie-break 7-2 after a 5-0 start in it. Shelton broke in the 12th game of the third for 7-5. Zverev took the fourth 6-2. Official US Open scores list the same four sets. Duration 3:33.\n\nShelton had beaten Alcaraz and Tiafoe to get here. The American men's Slam drought since Andy Roddick in 2003 is still the drought. Zverev is 25-2 at majors this year, per ATP.",
    stakes="A second major of 2026 versus a first American men's finalist in a generation.",
    rivalryAngle="World No. 1 versus home thunder that had already removed the defending champion.",
    funFacts=["Zverev's second Slam of 2026 after Roland Garros.", "Fourth man in the Open Era to win first two majors in one season.", "Shelton took the third set 7-5."],
    keyPlayers=[{"name": "Alexander Zverev", "team": "Germany", "hook": "First US Open. Second Slam of 2026."}, {"name": "Ben Shelton", "team": "USA", "hook": "First Slam final. Beat Alcaraz and Tiafoe to get here."}],
    home="Alexander Zverev", away="Ben Shelton", group="GS", date="2026-09-13", time="14:00",
    venue="Arthur Ashe Stadium", city="New York", status="FINISHED", format="singles",
    homeScore=3, awayScore=1,
    sport="tennis", competition="us-open-2026", roundLabel="Men's final",
    resultSummary="Zverev 6-3, 7-6 (2), 5-7, 6-2 Shelton",
    tennisSets=[{"p1": "6", "p2": "3"}, {"p1": "7", "p2": "6"}, {"p1": "5", "p2": "7"}, {"p1": "6", "p2": "2"}],
    tags=["us-open", "zverev", "shelton"],
    sources=[{"name": "ATP: Zverev wins US Open", "url": "https://www.atptour.com/en/news/zverev-shelton-us-open-2026-final-report"}, {"name": "US Open live scores", "url": "https://www.usopen.org/en_US/scores/index.html"}],
))

EVENTS.append(ev(
    slug="rybakina-vs-sabalenka-uso-final",
    headline="Rybakina dethrones Sabalenka 6-4, 5-7, 6-2 and takes No. 1 with it",
    whyCareScore=9.8,
    whyCareReason="A three-peat dies in the third set. Third major for Rybakina. First US Open. New world No. 1.",
    teaser="Rybakina 6-4, 5-7, 6-2 Sabalenka. Closed with an ace. $5.5 million. Sabalenka smashed a racket.",
    story="Why this one matters: Aryna Sabalenka had won this tournament in 2024 and 2025. A third straight would have put her with Serena Williams and Chris Evert. Elena Rybakina ended that on Saturday, 6-4, 5-7, 6-2, and replaced her at world No. 1.\n\nReuters, CBS and ABC logged the same score. Rybakina broke early in the third and again at 5-2. She dropped three points on serve in that set, per CBS, and closed with her 12th ace after a double fault on the first championship point. UPI: 12-6 in aces, 36-32 in winners, 2 hours 21 minutes. Prize $5.5 million.\n\nIt is Rybakina's third Slam after Wimbledon 2022 and the Australian Open earlier in 2026. Sabalenka's Flushing Meadows streak ends at 19 or 20 consecutive wins depending on the count you use. Reuters called it 20. UPI called it 19. The final score is not in dispute.",
    stakes="A three-peat denied. A new No. 1. A first US Open for Kazakhstan.",
    rivalryAngle="The two biggest first-strike games in women's tennis, both already Slam champions this decade.",
    funFacts=["Rybakina's third major, first US Open.", "Closed the match with a 12th ace.", "Sabalenka finishes 2026 without a Slam, first time since 2022, per GB News."],
    keyPlayers=[{"name": "Elena Rybakina", "team": "Kazakhstan", "hook": "New world No. 1. 6-4, 5-7, 6-2."}, {"name": "Aryna Sabalenka", "team": "Belarus", "hook": "Two-time defending champion. Three-peat stopped."}],
    home="Elena Rybakina", away="Aryna Sabalenka", group="GS", date="2026-09-12", time="16:00",
    venue="Arthur Ashe Stadium", city="New York", status="FINISHED", format="singles",
    homeScore=2, awayScore=1,
    sport="tennis", competition="us-open-2026", roundLabel="Women's final",
    resultSummary="Rybakina 6-4, 5-7, 6-2 Sabalenka",
    tennisSets=[{"p1": "6", "p2": "4"}, {"p1": "5", "p2": "7"}, {"p1": "6", "p2": "2"}],
    tags=["us-open", "rybakina", "sabalenka"],
    sources=[{"name": "Reuters: Rybakina beats Sabalenka", "url": "https://www.reuters.com/sports/tennis/rybakina-beats-sabalenka-first-us-open-title-2026-09-12/"}, {"name": "CBS: US Open women's final", "url": "https://www.cbssports.com/tennis/news/2026-us-open-results-elena-rybakina-aryna-sabalenka-womens-final/"}],
))

EVENTS.append(ev(
    slug="patriots-at-seahawks-kickoff-2026",
    headline="Seahawks 13, Patriots 10: three Maye interceptions, a Super Bowl rematch that stayed ugly",
    whyCareScore=9.4,
    whyCareReason="The opener was the Super Bowl again. New England led 10-0. Seattle scored the last 13 and left with the first win of 2026.",
    teaser="FINAL: Seahawks 13, Patriots 10. Darnold left injured. Drew Lock finished it. Maye threw three fourth-quarter interceptions.",
    story="Why this one matters: Super Bowl LX was 29-13 Seattle in February. The rematch on 9 September was 13-10, and it was not pretty.\n\nESPN: Patriots 0-7-3-0, Seahawks 0-0-3-10. New England led 10-0 through the middle of the third. Seattle scored 13 unanswered. Sam Darnold left injured. Drew Lock came in and threw for 187 yards. Drake Maye threw three interceptions. Jaxon Smith-Njigba had 122 receiving yards. Jadarian Price led Seattle with 52 rushing yards.\n\nSporting News and ESPN agree on 13-10. Wikipedia's 2026 season page lists Seattle as the Kickoff Game winner. The Dark Side defence, not the Super Bowl offence, won the night.",
    stakes="Week 1, a Super Bowl rematch, the first result of 2026.",
    rivalryAngle="Seattle 29-13 in February. Seattle 13-10 in September. New England still looking for the reply.",
    funFacts=["Maye three interceptions.", "Darnold left the game injured. Lock 187 passing yards.", "JSN 122 receiving yards."],
    keyPlayers=[{"name": "Drew Lock", "team": "Seahawks", "hook": "Relieved Darnold, 187 passing yards, finished a 13-10 win."}, {"name": "Drake Maye", "team": "Patriots", "hook": "Three interceptions. Patriots led 10-0 and lost."}],
    home="Seattle Seahawks", away="New England Patriots", group="NFL", date="2026-09-09", time="20:20",
    venue="Lumen Field", city="Seattle", status="FINISHED", homeScore=13, awayScore=10,
    sport="football", competition="nfl-2026", season="2026", roundLabel="Week 1 kickoff",
    resultSummary="Seahawks 13, Patriots 10",
    image="https://images.unsplash.com/photo-1606107557195-0e29a4b5b4aa?auto=format&fit=crop&w=1600&h=900&q=80",
    tags=["nfl", "seahawks", "patriots", "kickoff"],
    sources=[{"name": "ESPN: Seahawks pick off Maye three times", "url": "https://www.espn.com/nfl/scoreboard"}, {"name": "Wikipedia: 2026 NFL season", "url": "https://en.wikipedia.org/wiki/2026_NFL_season"}],
))

EVENTS.append(ev(
    slug="49ers-vs-rams-melbourne-2026",
    headline="49ers 27, Rams 7: first NFL game in Australia, Purdy three touchdowns",
    whyCareScore=8.8,
    whyCareReason="100,021 at the MCG. Stafford pulled late. San Francisco enjoyed the week and the scoreboard.",
    teaser="FINAL: 49ers 27, Rams 7. Purdy 205 yards, three TDs. First regular-season NFL game in Australia.",
    story="Why this one matters: the league had never played a regular-season game in Australia. On 10 September (11 September local) it did, and San Francisco won it 27-7.\n\nESPN: 49ers 3-7-7-10, Rams 0-7-0-0. Brock Purdy 205 passing yards, three touchdowns. Christian McCaffrey 68 rushing yards. Puka Nacua 74 receiving yards. Matthew Stafford was pulled late. Wikipedia's International Series table lists attendance 100,021 at Melbourne Cricket Ground.\n\nThe stake was the place. The result is 27-7. Night two of Week 1 already had a blowout.",
    stakes="A franchise rivalry on a new continent, decided by three Purdy touchdowns.",
    rivalryAngle="NFC West, once a year on the other side of the world.",
    funFacts=["Crowd 100,021.", "Purdy three touchdown passes.", "Stafford pulled late."],
    keyPlayers=[{"name": "Brock Purdy", "team": "49ers", "hook": "205 yards, three touchdowns."}, {"name": "Matthew Stafford", "team": "Rams", "hook": "Pulled late in a 27-7 loss."}],
    home="Los Angeles Rams", away="San Francisco 49ers", group="NFL", date="2026-09-10", time="20:35",
    venue="Melbourne Cricket Ground", city="Melbourne", status="FINISHED", homeScore=7, awayScore=27,
    sport="football", competition="nfl-2026", season="2026", roundLabel="Week 1 · Australia",
    resultSummary="49ers 27, Rams 7",
    image="https://images.unsplash.com/photo-1504609813442-a8924e83f76e?auto=format&fit=crop&w=1600&h=900&q=80",
    tags=["nfl", "49ers", "rams", "melbourne"],
    sources=[{"name": "ESPN: 49ers rout Rams in Australia", "url": "https://www.espn.com/nfl/scoreboard"}, {"name": "Wikipedia: NFL International Series", "url": "https://en.wikipedia.org/wiki/NFL_International_Series"}],
))

EVENTS.append(ev(
    slug="broncos-at-chiefs-mnf-2026",
    headline="Broncos at Chiefs: Monday night, Week 1 still has one snap left",
    whyCareScore=9.1,
    whyCareReason="Arrowhead, 8:15 p.m. ET, ESPN/ABC. The last game of Week 1 has not been played. Do not invent a score.",
    teaser="Monday 14 September. Denver at Kansas City. The early Sunday window is in the book. This one is not.",
    story="Why this one matters: Week 1 already has a Super Bowl rematch, an Australia game, a 59-37 in Charlotte, and a 31-30 overtime in Detroit. It does not yet have a Monday night result.\n\nBroncos at Chiefs, Arrowhead Stadium, 8:15 p.m. ET, ESPN and ABC. ESPN's scoreboard on 13 September listed both clubs 0-0 with kickoff still to come. That is the honest line on 14 September before the ball is snapped.\n\nPrint the time. Print the channel. Do not print a winner.",
    stakes="The last result of Week 1, in a building that has lived on them.",
    rivalryAngle="AFC West, a Sunday leftover on Monday night.",
    funFacts=["Kickoff 8:15 p.m. ET, ESPN/ABC.", "Both teams 0-0 until this game.", "Week 1 already has Seahawks 13-10 and 49ers 27-7."],
    keyPlayers=[{"name": "Kansas City Chiefs", "team": "Chiefs", "hook": "Home, Monday night, Week 1 still open."}, {"name": "Denver Broncos", "team": "Broncos", "hook": "Road, 8:15 p.m. ET. No score yet."}],
    home="Kansas City Chiefs", away="Denver Broncos", group="NFL", date="2026-09-14", time="20:15",
    venue="Arrowhead Stadium", city="Kansas City", status="UPCOMING",
    sport="football", competition="nfl-2026", season="2026", roundLabel="Week 1 · MNF",
    tags=["nfl", "chiefs", "broncos", "mnf"],
    sources=[{"name": "ESPN NFL scoreboard", "url": "https://www.espn.com/nfl/scoreboard"}, {"name": "FOX Week 1 schedule", "url": "https://www.foxsports.com/stories/nfl/when-does-2026-nfl-season-start-complete-week-1-schedule"}],
))

EVENTS.append(ev(
    slug="chelsea-vs-hull-mw4",
    headline="Chelsea 2-2 Hull: Belloumi twice, and the clean sheet is gone",
    whyCareScore=8.6,
    whyCareReason="Hull had not conceded in three league games. They scored twice at Stamford Bridge and still left with a point.",
    teaser="Rogers 7', Pedro 66'; Bachir Belloumi 28', 34'. Hull unbeaten. Chelsea on 7.",
    story="Why this one matters: Hull City arrived at Stamford Bridge with seven points and no goals conceded. They left with eight points and two goals conceded, and they scored twice themselves.\n\nFootball Web Pages: Morgan Rogers 7', Joao Pedro 66' for Chelsea. Bachir Belloumi 28' and 34' for Hull. Attendance 39,352. Match XI and Squawka both put Hull third on 8 points after the draw.\n\nThe Tigers are still unbeaten. The clean sheet that survived United, Villa and matchweek 3 did not survive London. That is still a sentence the table has to live with.",
    stakes="A promoted side's unbeaten start against a side that had already lost in north London.",
    rivalryAngle="New money versus a club that was supposed to be the measuring stick.",
    funFacts=["Belloumi scored twice in six minutes.", "Hull's first league goals conceded this season.", "Chelsea 2-1-1, 7 points."],
    keyPlayers=[{"name": "Bachir Belloumi", "team": "Hull City", "hook": "28' and 34' at Stamford Bridge."}, {"name": "Morgan Rogers", "team": "Chelsea", "hook": "Opened after 7 minutes."}],
    home="Chelsea", away="Hull City", group="PL", date="2026-09-12", time="15:00",
    venue="Stamford Bridge", city="London", status="FINISHED", homeScore=2, awayScore=2,
    sport="soccer", competition="premier-league-2026-27", season="2026/27", roundLabel="Matchweek 4",
    tags=["premier-league", "chelsea", "hull"],
    sources=[{"name": "Football Web Pages: Chelsea 2-2 Hull", "url": "https://www.footballwebpages.co.uk/premier-league/fixtures-results"}, {"name": "Squawka table", "url": "https://www.squawka.com/us/epl-standings/"}],
))

EVENTS.append(ev(
    slug="sunderland-vs-arsenal-mw4",
    headline="Arsenal 2-0 at Sunderland: four from four, Guimaraes then Saka",
    whyCareScore=8.9,
    whyCareReason="The champions go to a promoted ground and leave with 12 points. Nobody else has a perfect record except City.",
    teaser="Guimaraes 58', Saka 90+7' penalty. Sunderland 0-2 Arsenal. Arsenal 8-1 on goal difference.",
    story="Why this one matters: matchweek 4 was the first chance the table had to apologise. Arsenal did not let it. Sunderland 0-2 Arsenal, Bruno Guimaraes 58', Bukayo Saka 90+7' penalty, per Football Web Pages.\n\nAFP after Sunday: Arsenal 4 4 0 0, 8 1, 12 points. Same line on Squawka and NBC Sports. City also have 12 after Old Trafford. Goal difference is the split: Arsenal +7, City +6.\n\nA promoted club hosted the champions. The champions left with the same 100 per cent they brought.",
    stakes="Twelve points from four. A title start that now has a road win in it.",
    rivalryAngle="Promoted host, champion guest, one result.",
    funFacts=["Arsenal 4-0-0, 12 points.", "Saka penalty 90+7'.", "Arsenal 8 scored, 1 conceded."],
    keyPlayers=[{"name": "Bruno Guimaraes", "team": "Arsenal", "hook": "Opened the scoring in the 58th minute."}, {"name": "Bukayo Saka", "team": "Arsenal", "hook": "Penalty, 90+7', 2-0."}],
    home="Sunderland", away="Arsenal", group="PL", date="2026-09-12", time="17:30",
    venue="Stadium of Light", city="Sunderland", status="FINISHED", homeScore=0, awayScore=2,
    sport="soccer", competition="premier-league-2026-27", season="2026/27", roundLabel="Matchweek 4",
    tags=["premier-league", "arsenal", "sunderland"],
    sources=[{"name": "Football Web Pages: Sunderland 0-2 Arsenal", "url": "https://www.footballwebpages.co.uk/premier-league/fixtures-results"}, {"name": "AFP table 13 September", "url": "https://www.nampa.org/text/23014907"}],
))

EVENTS.append(ev(
    slug="manchester-united-vs-manchester-city-mw4",
    headline="Haaland 63': ten-man City win 1-0 at Old Trafford",
    whyCareScore=9.3,
    whyCareReason="City stay perfect. United stay on 4 points. The derby is already a scar.",
    teaser="Manchester United 0-1 Manchester City. Haaland 63'. Attendance 74,161. City 4-0-0.",
    story="Why this one matters: two clubs with different Septembers met at Old Trafford and the table did not blink. City had nine points. United had four. After 90 minutes City have 12 and United still have four.\n\nFootball Web Pages: Braut Haaland 63', attendance 74,161. AFP's match wrap is titled around ten-man City. Match XI, Squawka and NBC all put City second on 12 points, 8-2 on goals, +6.\n\nArsenal are first on goal difference. That is the only thing between the two perfect records. United have a derby loss to sit with the Hull wound.",
    stakes="Four wins from four for City. A derby that keeps United in mid-table geometry.",
    rivalryAngle="Old Trafford, a derby, a 1-0 that the table already understood.",
    funFacts=["Haaland 63'.", "City 4-0-0, 12 points.", "United 1-1-2, 4 points."],
    keyPlayers=[{"name": "Erling Haaland", "team": "Manchester City", "hook": "Winner, 63rd minute, Old Trafford."}, {"name": "Manchester United", "team": "Manchester United", "hook": "Home derby, 0-1, four points from four games."}],
    home="Manchester United", away="Manchester City", group="PL", date="2026-09-13", time="16:30",
    venue="Old Trafford", city="Manchester", status="FINISHED", homeScore=0, awayScore=1,
    sport="soccer", competition="premier-league-2026-27", season="2026/27", roundLabel="Matchweek 4",
    tags=["premier-league", "manchester-united", "manchester-city"],
    sources=[{"name": "Football Web Pages: United 0-1 City", "url": "https://www.footballwebpages.co.uk/premier-league/fixtures-results"}, {"name": "AFP: Haaland, 10-man City", "url": "https://www.nampa.org/text/23014907"}],
))

EVENTS.append(ev(
    slug="leeds-vs-newcastle-mw4",
    headline="Leeds vs Newcastle: the last matchweek 4 fixture has not been played",
    whyCareScore=7.8,
    whyCareReason="Both clubs have 5 points from 3 games. Elland Road, Monday 8 p.m. UK. No score yet.",
    teaser="14 September, 8 p.m. Leeds United vs Newcastle United. The rest of matchweek 4 is in the book. This is not.",
    story="Why this one matters: the table after Sunday is rude and incomplete. Leeds and Newcastle are the two clubs still on three games. Both have 5 points. Both can jump the mid-table pile with a win at Elland Road.\n\nFootball Web Pages lists Monday 14 September, 8 p.m. Match XI has the same kickoff as unplayed. Squawka's table, last updated after Saturday in one crawl and after Sunday in another, still has both on 3 played.\n\nPrint the fixture. Do not print a 14 September score on the morning of 14 September.",
    stakes="Five points each, a chance to make matchweek 4 look finished.",
    rivalryAngle="Two sides with European noise in recent memory, one Monday night.",
    funFacts=["Both on 3 played, 5 points.", "Kickoff 8 p.m. UK.", "Arsenal and City already have 12."],
    keyPlayers=[{"name": "Leeds United", "team": "Leeds United", "hook": "Home, 1-2-0, +1, 5 points."}, {"name": "Newcastle United", "team": "Newcastle United", "hook": "Away, 1-2-0, +2, 5 points."}],
    home="Leeds United", away="Newcastle United", group="PL", date="2026-09-14", time="20:00",
    venue="Elland Road", city="Leeds", status="UPCOMING",
    sport="soccer", competition="premier-league-2026-27", season="2026/27", roundLabel="Matchweek 4",
    tags=["premier-league", "leeds", "newcastle"],
    sources=[{"name": "Football Web Pages fixtures", "url": "https://www.footballwebpages.co.uk/premier-league/fixtures-results"}, {"name": "Match XI 2026-27", "url": "https://matchxi.com/seasons/2026-27"}],
))

EVENTS.append(ev(
    slug="spanish-gp-2026",
    headline="Antonelli wins Madrid: Norris pole, VSC, Hamilton out with no brakes",
    whyCareScore=9.6,
    whyCareReason="Eighth win of 2026. Lead 292-211. First Spanish Grand Prix at the Madring. Norris led until the virtual safety car.",
    teaser="Antonelli 1:34:23.754. Verstappen +4.351. Norris +5.089. Hamilton DNF, brakes, lap 6.",
    story="Why this one matters: a new circuit is supposed to scramble a championship. Madrid scrambled Lando Norris, not Kimi Antonelli.\n\nFormula1.com: Antonelli 1:34:23.754, Verstappen +4.351, Norris +5.089, Leclerc +29.116, Russell +29.829. Norris started on pole in 1:31.824. The Athletic: Norris led by 6.2 seconds on lap 14 when Lance Stroll stopped and the virtual safety car came out. Norris was too far around to pit. Antonelli was not. Hamilton reported no brakes, fell from fourth, retired on lap 6 with a brake failure. Wikipedia matches the classified order and the DNF list.\n\nDrivers after the race: Antonelli 292, Russell 211, Hamilton 191, Norris 186, Leclerc 167. Constructors: Mercedes 503, Ferrari 358, McLaren 306. Eighth win. Next is Baku, 24-26 September.",
    stakes="An 81-point lead, a new track in the books, nine races left.",
    rivalryAngle="Norris from pole versus a championship leader who inherited the strategy.",
    funFacts=["Norris pole 1:31.824.", "Hamilton retired lap 6, brakes.", "Antonelli eighth win, lead 81 points."],
    keyPlayers=[{"name": "Kimi Antonelli", "team": "Mercedes", "hook": "Won from P2 after the VSC. 292 points."}, {"name": "Lando Norris", "team": "McLaren", "hook": "Pole. Led. VSC. Third."}],
    home="Kimi Antonelli", away="Lando Norris", group="F1", date="2026-09-13", time="15:00",
    venue="Madring", city="Madrid", status="FINISHED", format="race",
    sport="f1", competition="f1-2026", season="2026", roundLabel="Spanish Grand Prix",
    resultSummary="1 Antonelli, 2 Verstappen +4.351, 3 Norris +5.089. Hamilton DNF.",
    leaderboard=[
        {"pos": "1", "name": "Kimi Antonelli", "score": "1:34:23.754", "note": "Mercedes, started P2"},
        {"pos": "2", "name": "Max Verstappen", "score": "+4.351", "note": "Red Bull"},
        {"pos": "3", "name": "Lando Norris", "score": "+5.089", "note": "McLaren, pole"},
        {"pos": "4", "name": "Charles Leclerc", "score": "+29.116", "note": "Ferrari"},
        {"pos": "5", "name": "George Russell", "score": "+29.829", "note": "Mercedes, fastest lap 1:35.587"},
        {"pos": "DNF", "name": "Lewis Hamilton", "score": "Lap 6", "note": "Ferrari, brakes"},
    ],
    tags=["f1", "madrid", "antonelli"],
    sources=[{"name": "Formula1.com race result", "url": "https://www.formula1.com/en/results/2026/races/1294/spain/race-result"}, {"name": "Wikipedia: 2026 Spanish Grand Prix", "url": "https://en.wikipedia.org/wiki/2026_Spanish_Grand_Prix"}, {"name": "The Athletic: Spanish GP briefing", "url": "https://www.nytimes.com/athletic/7589661/2026/09/13/f1-spanish-grand-prix-results/"}],
))


def main():
    ROOT.mkdir(parents=True, exist_ok=True)
    for e in EVENTS:
        path = ROOT / f"{e['slug']}.json"
        path.write_text(json.dumps(e, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
        print("wrote", path.name)
    print("total", len(EVENTS))


if __name__ == "__main__":
    main()
