"""Write sourced multi-sport event JSON files. Scores only from the locked plan.

Run update_stats_sept14.py then update_stats_sept15.py then update_stats_sept16.py after this file so later desk results are not clobbered.
"""
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
        "liveMinute": None,
        "image": IMG[sport],
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

# --- Premier League ---
EVENTS.append(ev(
    slug="hull-city-vs-manchester-united-mw1",
    headline="Hull City 2-0 Manchester United on the night they came back",
    whyCareScore=9.2,
    whyCareReason="A promoted side's first Premier League match in nine years ends with United beaten 2-0. That is a stake, not a cute scoreline.",
    teaser="Semi Ajayi and Nobel Mendy score. Hull, everyone's favourites to go down, punch the season in the mouth.",
    story="Why this one matters: Manchester United are supposed to be the measuring stick. Hull City had not played a Premier League match in nine years. On 22 August at the MKM Stadium the measuring stick fell over.\n\nSemi Ajayi scored in the 17th minute after a scramble from a corner. Nobel Mendy headed in close range in the 38th. Hull 2-0 United. Oli McBurnie ran the show according to The Athletic's opening-weekend notes. The Tigers were everyone's favourites to go down. They left with three points and a clean sheet they still have not given up three weeks later.\n\nUnited will win games this season. They already have. This night is the one the table will keep whispering about.",
    stakes="Opening-day points, a promoted club's first statement, United's first wound.",
    rivalryAngle="New money, old giant. Hull were not supposed to be in this sentence.",
    funFacts=["Hull's first Premier League match in nine years.", "Ajayi 17', Mendy 38'.", "Hull have not conceded in their first three league games."],
    keyPlayers=[{"name": "Semi Ajayi", "team": "Hull City", "hook": "Opened the scoring in the 17th minute."}, {"name": "Nobel Mendy", "team": "Hull City", "hook": "Close-range header, 38th minute, 2-0."}],
    home="Hull City", away="Manchester United", group="PL", date="2026-08-22", time="12:30",
    venue="MKM Stadium", city="Hull", status="FINISHED", homeScore=2, awayScore=0,
    sport="soccer", competition="premier-league-2026-27", season="2026/27", roundLabel="Matchweek 1",
    tags=["premier-league", "hull", "manchester-united"],
    sources=[{"name": "The Athletic: opening weekend", "url": "https://www.nytimes.com/athletic/7535116/2026/08/25/premier-league-winners-losers-gameweek-one/"}, {"name": "theScore: opening weekend analysis", "url": "https://www.thescore.com/epl/news/3583101/analysis-from-opening-weekend-of-new-premier-league-season"}],
))

EVENTS.append(ev(
    slug="arsenal-vs-chelsea-mw3",
    headline="Arsenal 2-1 Chelsea: champions pass the first real test",
    whyCareScore=9.4,
    whyCareReason="Both sides had two wins from two. Only Arsenal still have nine points. Odegaard's winner is an early title marker.",
    teaser="Morgan Rogers scored after 77 seconds. Kai Havertz equalised. Martin Odegaard won it. David Raya saved Estevao late.",
    story="Why this one matters: after three games only Arsenal and Manchester City have nine points. This was the first time both London sides sat on a perfect record and one of them had to blink.\n\nMorgan Rogers volleyed Chelsea ahead after 77 seconds, the third straight Chelsea game with a goal inside five minutes, a Premier League first. Kai Havertz equalised in the 25th minute against his former club. Martin Odegaard finished a flowing move shortly after the break. Estevao was denied a late equaliser by David Raya.\n\nMikel Arteta told Sky it was a joy to watch from start to finish. Xabi Alonso called Chelsea's afternoon suffering. Attendance 60,240 at the Emirates. Referee Chris Kavanagh.",
    stakes="Early title geometry. Nine points versus six.",
    rivalryAngle="London, two perfect records, one left standing.",
    funFacts=["Rogers 2', Havertz 25', Odegaard ~50'.", "Arsenal's first three-win start conceding fewer than two since the Invincibles season, per PremierLeague.com.", "Chelsea had scored inside five minutes in each of their first three games."],
    keyPlayers=[{"name": "Martin Odegaard", "team": "Arsenal", "hook": "Winner shortly after half-time."}, {"name": "Morgan Rogers", "team": "Chelsea", "hook": "Volley after 77 seconds."}],
    home="Arsenal", away="Chelsea", group="PL", date="2026-09-06", time="16:30",
    venue="Emirates Stadium", city="London", status="FINISHED", homeScore=2, awayScore=1,
    sport="soccer", competition="premier-league-2026-27", season="2026/27", roundLabel="Matchweek 3",
    tags=["premier-league", "arsenal", "chelsea"],
    sources=[{"name": "The Independent: Arsenal 2-1 Chelsea", "url": "https://www.independent.co.uk/sport/football/arsenal-chelsea-live-stream-score-premier-league-result-b3044763.html"}, {"name": "PremierLeague.com Sunday wrap", "url": "https://www.premierleague.com/en/news/4706438/sunday-wrap-arsenal-pass-big-early-test-after-late-drama-at-everton"}],
))

EVENTS.append(ev(
    slug="brighton-vs-aston-villa-mw1",
    headline="Brighton 4-0 Aston Villa, and the table looks strange already",
    whyCareScore=8.1,
    whyCareReason="Opening weekend is supposed to be rust. Brighton put four past Villa and sat top of the real table.",
    teaser="Own goal, a first-half red card, a high press that Villa could not play through. 4-0 at the Amex on 23 August.",
    story="Why this one matters: Aston Villa are a European club with European habits. Brighton are the side that keeps teaching the league the same lesson. On 23 August the lesson was 4-0.\n\nThe Athletic's opening-weekend performance table put Brighton near the top and noted Villa's own goal, a first-half red card, and a maddening determination to play out against Brighton's press. Brighton finished matchweek one on top of the actual table too.\n\nThree weeks later Brighton have four points and eight goals. Villa have one point and zero goals. The 4-0 still explains both sentences.",
    stakes="Opening-weekend geometry for two clubs with European ambitions.",
    rivalryAngle="Press versus pride. Villa tried to play through it. They did not.",
    funFacts=["Played 23 August 2026.", "Brighton topped the table after matchweek one.", "Villa have scored zero Premier League goals in three games."],
    keyPlayers=[{"name": "Brighton press", "team": "Brighton", "hook": "The Athletic's note: Villa could not play out against it."}, {"name": "Aston Villa", "team": "Aston Villa", "hook": "Own goal, red card, 4-0."}],
    home="Brighton", away="Aston Villa", group="PL", date="2026-08-23", time="14:00",
    venue="American Express Stadium", city="Brighton", status="FINISHED", homeScore=4, awayScore=0,
    sport="soccer", competition="premier-league-2026-27", season="2026/27", roundLabel="Matchweek 1",
    tags=["premier-league", "brighton", "villa"],
    sources=[{"name": "The Athletic: opening weekend", "url": "https://www.nytimes.com/athletic/7535116/2026/08/25/premier-league-winners-losers-gameweek-one/"}, {"name": "BBC scores", "url": "https://www.bbc.co.uk/sport/football/premier-league/scores-fixtures/2026-08"}],
))

# --- Tennis ---
EVENTS.append(ev(
    slug="noskova-vs-muchova-wimbledon-final",
    headline="Noskova wastes five championship points, then wins Wimbledon anyway",
    whyCareScore=9.6,
    whyCareReason="A 21-year-old from a village of a thousand people becomes the youngest women's Wimbledon champion since Kvitova in 2011.",
    teaser="Linda Noskova def. Karolina Muchova 6-2, 5-7, 6-3. All-Czech final. First Slam. Converted the sixth championship point.",
    story="Why this one matters: Wimbledon finals are supposed to belong to the names you already know. On 11 July the names were Czech, seeded 9 and 10, and friends.\n\nNoskova led 6-2, 5-2. Muchova won five games in a row, saved five championship points, forced a decider. Noskova reset and won 6-3 in the third, converting a sixth championship point with a service winner after an ace. BBC, The Athletic and CBS all logged the same score: 6-2, 5-7, 6-3.\n\nShe is 21. Youngest women's champion here since Petra Kvitova in 2011. First Slam. She also won Berlin on the grass before she arrived. Prize money around $4.8 million, nearly doubling her career on-court earnings.",
    stakes="A first major, an all-Czech final, a new name on the board.",
    rivalryAngle="Friends, same country, opposite sides of Centre Court.",
    funFacts=["Five championship points missed, sixth converted.", "Youngest women's Wimbledon champion since 2011.", "Noskova also won the Berlin Open in June."],
    keyPlayers=[{"name": "Linda Noskova", "team": "Czechia", "hook": "First Slam, 6-2 5-7 6-3."}, {"name": "Karolina Muchova", "team": "Czechia", "hook": "Saved five championship points, still lost."}],
    home="Linda Noskova", away="Karolina Muchova", group="GS", date="2026-07-11", time="14:00",
    venue="Centre Court", city="Wimbledon", status="FINISHED", format="singles",
    sport="tennis", competition="wimbledon-2026", roundLabel="Women's final",
    resultSummary="Noskova 6-2, 5-7, 6-3 Muchova",
    tennisSets=[{"p1": "6", "p2": "2"}, {"p1": "5", "p2": "7"}, {"p1": "6", "p2": "3"}],
    tags=["wimbledon", "noskova", "muchova"],
    sources=[{"name": "BBC: Noskova beats Muchova", "url": "https://www.bbc.com/sport/tennis/articles/ce37x57gv49o"}, {"name": "The Athletic: Wimbledon women's final", "url": "https://www.nytimes.com/athletic/7437108/2026/07/11/wimbledon-final-karolina-muchova-linda-noskova-result-analysis/"}],
))

EVENTS.append(ev(
    slug="sinner-vs-zverev-wimbledon-final",
    headline="Sinner beats Zverev in four: two tiebreaks, then the champion's weight",
    whyCareScore=9.3,
    whyCareReason="Second straight Wimbledon, fifth major. Zverev had just won Roland Garros. Grass still belonged to Sinner.",
    teaser="Jannik Sinner def. Alexander Zverev 6-7 (7-9), 7-6 (7-2), 6-3, 6-4. Championship point on a 23-shot rally.",
    story="Why this one matters: Alexander Zverev arrived as the reigning French Open champion, looking for a Channel Slam. Jannik Sinner arrived as world No. 1, looking for a second straight Wimbledon and a first major of 2026 after an Australian Open semi loss to Djokovic and a French Open second-round exit with heat exhaustion.\n\nThe score, from CBS: 6-7 (7-9), 7-6 (7-2), 6-3, 6-4. First break of the match at 5-3 in the third. Championship point after a 23-shot rally, Sinner's forehand. He now has 100 major match wins.\n\nThe first two sets were serve. The last two were the favourite remembering who he is.",
    stakes="A fifth Slam versus Zverev's first Wimbledon final.",
    rivalryAngle="The two biggest first-strike games in men's tennis, on grass.",
    funFacts=["Sinner's second straight Wimbledon.", "Fifth major overall, first of 2026.", "First break of the match came at 5-3 in the third set."],
    keyPlayers=[{"name": "Jannik Sinner", "team": "Italy", "hook": "Won the second-set breaker, then broke at 5-3 in the third."}, {"name": "Alexander Zverev", "team": "Germany", "hook": "Took the first-set breaker, could not find a second."}],
    home="Jannik Sinner", away="Alexander Zverev", group="GS", date="2026-07-12", time="14:00",
    venue="Centre Court", city="Wimbledon", status="FINISHED", format="singles",
    sport="tennis", competition="wimbledon-2026", roundLabel="Men's final",
    resultSummary="Sinner 6-7 (7-9), 7-6 (7-2), 6-3, 6-4 Zverev",
    tennisSets=[{"p1": "6", "p2": "7"}, {"p1": "7", "p2": "6"}, {"p1": "6", "p2": "3"}, {"p1": "6", "p2": "4"}],
    tags=["wimbledon", "sinner", "zverev"],
    sources=[{"name": "CBS: Wimbledon 2026 winners", "url": "https://www.cbssports.com/tennis/news/wimbledon-2026-results-winners-jannik-sinner-linda-noskova/live/"}, {"name": "Wikipedia: 2026 in tennis", "url": "https://en.wikipedia.org/wiki/2026_in_tennis"}],
))

EVENTS.append(ev(
    slug="alcaraz-vs-shelton-uso-qf",
    headline="Alcaraz vs Shelton: the US Open quarter that New York wanted",
    whyCareScore=9.5,
    whyCareReason="A defending champion back from a four-month wrist layoff against a home lefty on Ashe. No 2026 champion yet.",
    teaser="Quarter-final, 8-9 September. Alcaraz beat Tommy Paul 6-4, 6-3, 6-4. Shelton beat Tsitsipas 6-2, 6-3, 6-4. They meet next.",
    story="Why this one matters: the US Open is still live. Do not write a champion. Write the match that sits in front of you.\n\nCarlos Alcaraz is the defending champion, back from a right-wrist injury that kept him out about four months. He opened against Roman Safiullin 6-4, 6-4, 6-4 and then beat Tommy Paul 6-4, 6-3, 6-4. Ben Shelton, the eighth seed, beat Stefanos Tsitsipas 6-2, 6-3, 6-4 and called Alcaraz's return superhuman. Fireworks on Tuesday night, he said.\n\nIf Alcaraz wins he likely sees Tiafoe or Michelsen in a semi. The American men have not had a Slam champion since Andy Roddick here in 2003. That is the air in the building. The match is the thing.",
    stakes="A quarter-final that can send a favourite into an American semi, or send New York into orbit.",
    rivalryAngle="Defending champion versus home thunder.",
    funFacts=["Alcaraz missed about four months with a right wrist injury.", "Shelton beat Tsitsipas 6-2, 6-3, 6-4.", "No 2026 US Open singles champion as of 8 September."],
    keyPlayers=[{"name": "Carlos Alcaraz", "team": "Spain", "hook": "Defending champion, injury return, through Paul in straights."}, {"name": "Ben Shelton", "team": "USA", "hook": "Eighth seed, home Ashe, Tsitsipas in straights."}],
    home="Carlos Alcaraz", away="Ben Shelton", group="GS", date="2026-09-08", time="19:00",
    venue="Arthur Ashe Stadium", city="New York", status="UPCOMING", format="singles",
    sport="tennis", competition="us-open-2026", roundLabel="Men's quarter-final",
    tags=["us-open", "alcaraz", "shelton"],
    sources=[{"name": "Reuters: Alcaraz-Shelton QF", "url": "https://www.reuters.com/sports/tennis/shelton-next-up-alcaraz-tackles-all-american-gauntlet-path-us-open-final-2026-09-07/"}, {"name": "usopen.org: Sunday winners", "url": "https://www.usopen.org/en_US/news/articles/2026-09-06/who_won_on_sunday_at_the_2026_us_open_results_and_highlights.html"}],
))

EVENTS.append(ev(
    slug="tiafoe-vs-michelsen-uso-qf",
    headline="Tiafoe vs Michelsen: two sets each, fifth set live on Ashe",
    whyCareScore=9.6,
    whyCareReason="An all-American quarter-final that was two sets to love, then two-all, now a fifth. No winner. Do not invent one.",
    teaser="LIVE on Arthur Ashe. Tiafoe 5-7, 3-6, 7-5, 6-3, 3-4 Michelsen. Michelsen serving. The American Slam drought since Roddick in 2003 is still the air in the building.",
    story="Why this one matters: three American men reached the last eight. This is the all-American quarter, and it has gone the distance.\n\nBBC has it live on Ashe. Alex Michelsen took the first two sets 7-5, 6-3. Frances Tiafoe, the eleventh seed, took the next two 7-5, 6-3. In the fifth it is 3-4, Michelsen serving. That is the score. That is not a result.\n\nTiafoe beat Daniil Medvedev to get here. Michelsen is in his first Slam quarter-final. The United States has not had a men's major champion since Andy Roddick on this court in 2003. Write the fifth set. Do not write a finalist.",
    stakes="A semi-final against Alcaraz or Shelton. One American goes through. One goes home. Not decided.",
    rivalryAngle="Two Americans, one court, a drought that is 23 years old and still unsolved tonight.",
    funFacts=["All-American men's quarter-final on Ashe.", "Michelsen took the first two sets. Tiafoe took the next two.", "No winner. Fifth set in progress."],
    keyPlayers=[{"name": "Frances Tiafoe", "team": "USA", "hook": "Eleventh seed. Beat Medvedev to get here. Trailed two sets to love."}, {"name": "Alex Michelsen", "team": "USA", "hook": "First Slam quarter-final. Took the first two sets, serving in the fifth."}],
    home="Frances Tiafoe", away="Alex Michelsen", group="GS", date="2026-09-08", time="13:00",
    venue="Arthur Ashe Stadium", city="New York", status="LIVE", format="singles",
    sport="tennis", competition="us-open-2026", roundLabel="Men's quarter-final",
    liveMinute="5th set",
    homeScore=2, awayScore=2,
    resultSummary="LIVE: Tiafoe 5-7, 3-6, 7-5, 6-3, 3-4 Michelsen (fifth set)",
    tennisSets=[{"p1": "5", "p2": "7"}, {"p1": "3", "p2": "6"}, {"p1": "7", "p2": "5"}, {"p1": "6", "p2": "3"}, {"p1": "3", "p2": "4"}],
    tags=["us-open", "tiafoe", "michelsen"],
    sources=[{"name": "BBC Sport scores: US Open 8 September", "url": "https://www.bbc.com/sport/tennis/scores-and-schedule/2026-09-08"}, {"name": "ESPN tennis scoreboard 8 September", "url": "https://www.espn.com/tennis/scoreboard/_/date/20260908"}],
))

EVENTS.append(ev(
    slug="sabalenka-vs-noskova-uso-qf",
    headline="Sabalenka survives Noskova 7-6, 3-6, 7-6 and keeps the three-peat alive",
    whyCareScore=9.4,
    whyCareReason="The two-time defending champion dropped a set for the first time here, trailed in the third, and still reached a sixth straight US Open semi-final.",
    teaser="Aryna Sabalenka def. Linda Noskova 7-6 (7-1), 3-6, 7-6 (10-7) on Ashe. She thought the title defence was over. Then she hit a second-serve ace.",
    story="Why this one matters: a three-peat at Flushing Meadows does not survive a quiet afternoon. Sabalenka, chasing a third straight US Open, met Linda Noskova, the new Wimbledon champion, in the quarter-finals and had to go the distance for the first time this fortnight.\n\nBBC logged the score as 7-6 (7-1), 3-6, 7-6 (10-7), a little under two and a half hours. Sabalenka led 5-2 in the first, got broken serving for the set, then ran the breaker 7-1. Noskova took the second 6-3 after a Sabalenka double fault at 30-40. In the third, Noskova held to love for 4-2. Sabalenka won the next three games, then trailed 2-0 in the deciding tie-break before closing it with a second-serve ace. It was her tenth successive tie-break win at this tournament, a run dating to 2021.\n\nShe called herself speechless. Nineteen consecutive wins here. First woman since Serena Williams in 2016 to reach six successive US Open semi-finals. Next is Jessica Pegula or Emma Navarro. Noskova hit more winners, made fewer unforced errors, and saved seven of nine break points. Her eleven-match Grand Slam singles streak ends in New York.",
    stakes="A three-peat stays alive. Wimbledon's new champion goes home. The women's champion is still unwritten.",
    rivalryAngle="The favourite who thought she was done versus the grass-court shock who had the match at 4-2 in the third.",
    funFacts=["Sabalenka's 19th consecutive win at the US Open.", "First woman since Serena Williams in 2016 to reach six successive US Open semi-finals.", "Closed the match with a second-serve ace in a 10-7 third-set tie-break."],
    keyPlayers=[{"name": "Aryna Sabalenka", "team": "Belarus", "hook": "Two-time defending champion. Survived a first dropped set of the tournament."}, {"name": "Linda Noskova", "team": "Czechia", "hook": "Reigning Wimbledon champion. Hit more winners, still lost in three."}],
    home="Aryna Sabalenka", away="Linda Noskova", group="GS", date="2026-09-08", time="11:30",
    venue="Arthur Ashe Stadium", city="New York", status="FINISHED", format="singles",
    sport="tennis", competition="us-open-2026", roundLabel="Women's quarter-final",
    resultSummary="Sabalenka 7-6 (7-1), 3-6, 7-6 (10-7) Noskova",
    tennisSets=[{"p1": "7", "p2": "6"}, {"p1": "3", "p2": "6"}, {"p1": "7", "p2": "6"}],
    tags=["us-open", "sabalenka", "noskova"],
    sources=[{"name": "BBC: Sabalenka beats Noskova", "url": "https://www.bbc.com/sport/tennis/articles/c3v43p9r2qdo"}, {"name": "BBC Sport scores: US Open 8 September", "url": "https://www.bbc.com/sport/tennis/scores-and-schedule"}],
))

# --- Golf ---
EVENTS.append(ev(
    slug="the-open-2026-royal-birkdale",
    headline="Ryan Fox birdies the 18th and steals the Claret Jug",
    whyCareScore=9.4,
    whyCareReason="A 39-year-old New Zealander shoots 62-68 on the weekend, birdies the hardest hole on the property, and becomes the third Kiwi to win a men's major.",
    teaser="Fox 270 (-10), Young 271, Burns 272. Royal Birkdale, 16-19 July. Birdie on 18. $3.2 million.",
    story="Why this one matters: majors are supposed to belong to the names on the world ranking. Ryan Fox began Sunday two shots behind Sam Burns, tied Young with a birdie at 16, then birdied the 18th, the hardest hole of the week, from about 12 feet.\n\nRounds: 72-68-62-68 = 270, ten under. Cameron Young 64 on Sunday for 271. Burns 272. Tommy Fleetwood and Scottie Scheffler tied fourth at 273. The 62 on Saturday tied the men's major record for lowest round. CBS called the 36-hole comeback the largest by position to win a men's major.\n\nThird New Zealander to win a men's major. Purse $17.75 million, winner $3.2 million. Par 70, 7,223 yards, cut 141 (+1).",
    stakes="The last men's major of 2026.",
    rivalryAngle="Fox versus a leaderboard that included Scheffler, Fleetwood, Young, Burns.",
    funFacts=["Fox 72-68-62-68 = 270.", "Young finished one back after a Sunday 64.", "18th played 161 over par for the field."],
    keyPlayers=[{"name": "Ryan Fox", "team": "New Zealand", "hook": "Birdie on 18 to win by one."}, {"name": "Cameron Young", "team": "USA", "hook": "Sunday 64, clubhouse lead, second by one."}],
    home="Ryan Fox", away="Cameron Young", group="OPEN", date="2026-07-19", time="18:00",
    venue="Royal Birkdale", city="Southport", status="FINISHED", format="leaderboard",
    sport="golf", competition="the-open-2026", roundLabel="154th Open Championship",
    resultSummary="Fox 270 (-10), Young 271, Burns 272",
    leaderboard=[
        {"pos": "1", "name": "Ryan Fox", "score": "270 (-10)", "note": "72-68-62-68"},
        {"pos": "2", "name": "Cameron Young", "score": "271 (-9)", "note": "67-67-73-64"},
        {"pos": "3", "name": "Sam Burns", "score": "272 (-8)", "note": "73-62-65-72"},
        {"pos": "T4", "name": "Tommy Fleetwood", "score": "273 (-7)", "note": ""},
        {"pos": "T4", "name": "Scottie Scheffler", "score": "273 (-7)", "note": ""},
    ],
    tags=["the-open", "fox", "birkdale"],
    sources=[{"name": "Wikipedia: 2026 Open Championship", "url": "https://en.wikipedia.org/wiki/2026_Open_Championship"}, {"name": "CBS: Fox wins Claret Jug", "url": "https://www.cbssports.com/golf/news/open-2026-leaderboard-live-updates-round-4-scores-results/live/"}],
))

EVENTS.append(ev(
    slug="tour-championship-2026-east-lake",
    headline="Scheffler wins East Lake, a second FedEx Cup, and passes Tiger's PGA earnings",
    whyCareScore=8.8,
    whyCareReason="World No. 1 starts Sunday three back of Hovland, shoots 66, wins by three at 16 under, and takes the $10 million.",
    teaser="Scheffler 264 (-16), Hovland -13, Ryan Gerard -12. Second FedEx Cup in three years. Career PGA earnings past Tiger Woods.",
    story="Why this one matters: people spent a summer asking if Scottie Scheffler had loosened his grip. He answered across three playoff events: St. Jude, a miss at the BMW (Wyndham Clark won that), then East Lake.\n\nFinal rounds 65-67-66-66 = 264, 16 under. Viktor Hovland 267. Ryan Gerard 268. Scheffler made up three shots in four holes on Sunday, a 5-iron to 2 inches on the second, a 25-foot birdie on the fourth. First time he posted the low 72-hole score at the Tour Championship. When he won in 2024 he started with a two-shot lead under the old starting-strokes format.\n\n$10 million first prize from a $40 million purse. AP: he moved past Tiger Woods for most PGA Tour career earnings. Second FedEx Cup (2024, 2026). Rory McIlroy still has the most titles with three.",
    stakes="Season-long trophy, Player of the Year geometry, the earnings line.",
    rivalryAngle="Scheffler versus Hovland on a Sunday at East Lake.",
    funFacts=["Scheffler 264 (-16), three clear of Hovland.", "Second FedEx Cup in three years.", "Passed Tiger Woods in PGA Tour career earnings, per AP."],
    keyPlayers=[{"name": "Scottie Scheffler", "team": "USA", "hook": "Sunday 66 from three back."}, {"name": "Viktor Hovland", "team": "Norway", "hook": "Led Sunday, finished three back."}],
    home="Scottie Scheffler", away="Viktor Hovland", group="PGA", date="2026-08-30", time="18:00",
    venue="East Lake Golf Club", city="Atlanta", status="FINISHED", format="leaderboard",
    sport="golf", competition="fedex-cup-2026", roundLabel="Tour Championship",
    resultSummary="Scheffler 264 (-16), Hovland 267, Gerard 268",
    leaderboard=[
        {"pos": "1", "name": "Scottie Scheffler", "score": "-16", "note": "65-67-66-66"},
        {"pos": "2", "name": "Viktor Hovland", "score": "-13", "note": ""},
        {"pos": "3", "name": "Ryan Gerard", "score": "-12", "note": ""},
    ],
    tags=["fedex-cup", "scheffler", "east-lake"],
    sources=[{"name": "Sky Sports: Tour Championship", "url": "https://www.skysports.com/golf/news/12176/13578960/tour-championship-scottie-scheffler-holds-off-viktor-hovland-to-claim-fedexcup-title-and-break-more-pga-tour-records"}, {"name": "AP via OCR: Scheffler FedEx Cup", "url": "https://www.ocregister.com/2026/08/30/scottie-scheffler-wins-2nd-fedex-cup-tops-tiger-woods-in-pga-tour-career-earnings/"}],
))

# --- NFL ---
EVENTS.append(ev(
    slug="patriots-at-seahawks-kickoff-2026",
    headline="Patriots at Seahawks: Super Bowl LX, again, and the season has not started",
    whyCareScore=9.7,
    whyCareReason="Wednesday 9 September, 8:20 p.m. ET, NBC. The only NFL game that exists yet. It is a rematch of a 29-13 beating.",
    teaser="Seattle won Super Bowl LX 29-13 on 8 February. Kenneth Walker III was MVP. Tomorrow night they host New England again.",
    story="Why this one matters: as of 8 September 2026 the NFL regular season has not kicked a ball. Preseason ended 29 August. The first snap is tomorrow in Seattle, and it is the Super Bowl again.\n\nSuper Bowl LX, 8 February, Levi's Stadium: Seahawks 29-13 Patriots. Walker 135 rushing yards, first running-back MVP since Terrell Davis in 1998. Jason Myers five field goals, a Super Bowl record, first 200-point scorer in NFL history. Sam Darnold 19/38, 202 yards, 1 TD, 0 INT. Drake Maye 27/43, 295, 2 TD, 2 INT, sacked six times. Uchenna Nwosu returned a fumble 45 yards for a touchdown. Seattle's second title, Mike Macdonald's second-year team, the Dark Side defence.\n\nKickoff is Wednesday because Labor Day fell as late as it can. That is the calendar. The story is the rematch.",
    stakes="Week 1, a Super Bowl rematch, the first snap of 2026.",
    rivalryAngle="Seattle 29-13 in February. New England gets a first reply in September.",
    funFacts=["Kickoff Wednesday 9 September, 8:20 p.m. ET, NBC.", "SB LX: Seahawks 29-13, Walker MVP, Myers five FGs.", "No 2026 regular-season games have been played as of 8 September."],
    keyPlayers=[{"name": "Kenneth Walker III", "team": "Seahawks", "hook": "Super Bowl MVP, 135 rush yards."}, {"name": "Drake Maye", "team": "Patriots", "hook": "Sacked six times in the Super Bowl. Gets a first reply."}],
    home="Seattle Seahawks", away="New England Patriots", group="NFL", date="2026-09-09", time="20:20",
    venue="Lumen Field", city="Seattle", status="UPCOMING",
    sport="football", competition="nfl-2026", season="2026", roundLabel="Week 1 kickoff",
    tags=["nfl", "seahawks", "patriots", "kickoff"],
    sources=[{"name": "FOX: 2026 Week 1 schedule", "url": "https://www.foxsports.com/stories/nfl/when-does-2026-nfl-season-start-complete-week-1-schedule"}, {"name": "Wikipedia: Super Bowl LX", "url": "https://en.wikipedia.org/wiki/Super_Bowl_LX"}, {"name": "NFL.com Super Bowl LX hub", "url": "https://www.nfl.com/super-bowl"}],
))

EVENTS.append(ev(
    slug="49ers-vs-rams-melbourne-2026",
    headline="49ers vs Rams in Melbourne: the league leaves home on night two",
    whyCareScore=8.4,
    whyCareReason="The NFL's first regular-season game in Australia, 24 hours after kickoff, on Netflix, at the MCG.",
    teaser="Thursday 10 September, 8:35 p.m. ET. San Francisco versus Los Angeles at Melbourne Cricket Ground. Local kickoff Friday 10:35 a.m. AEST.",
    story="Why this one matters: the league spent a century pretending the map stopped at the ocean. Week 1 of 2026 puts an NFC West rivalry in a cricket ground on Netflix.\n\n49ers versus Rams, Melbourne Cricket Ground, Thursday 10 September 8:35 p.m. ET, Friday morning in Melbourne. It is the NFL's first regular-season game in Australia. It is also night two of a season that opened with a Super Bowl rematch.\n\nNo score yet. Do not invent one. The stake is the place.",
    stakes="A franchise rivalry in a new country, on a streaming app, 24 hours after kickoff.",
    rivalryAngle="NFC West, twice a year, once on the other side of the world.",
    funFacts=["First NFL regular-season game in Australia.", "Netflix, 8:35 p.m. ET Thursday.", "Local kickoff 10:35 a.m. AEST Friday."],
    keyPlayers=[{"name": "San Francisco 49ers", "team": "49ers", "hook": "NFC West, travelling the farthest for Week 1."}, {"name": "Los Angeles Rams", "team": "Rams", "hook": "Listed as the home side in Melbourne."}],
    home="Los Angeles Rams", away="San Francisco 49ers", group="NFL", date="2026-09-10", time="20:35",
    venue="Melbourne Cricket Ground", city="Melbourne", status="UPCOMING",
    sport="football", competition="nfl-2026", season="2026", roundLabel="Week 1 · Australia",
    tags=["nfl", "49ers", "rams", "melbourne"],
    sources=[{"name": "FOX Week 1 schedule", "url": "https://www.foxsports.com/stories/nfl/when-does-2026-nfl-season-start-complete-week-1-schedule"}, {"name": "CBS Week 1 times", "url": "https://www.cbssports.com/nfl/news/2026-nfl-schedule-dates-times/"}],
))

# --- Basketball ---
EVENTS.append(ev(
    slug="nba-finals-2026-knicks-spurs",
    headline="Knicks 4-1: 53 years, Brunson 45, a 29-point Game 4",
    whyCareScore=9.8,
    whyCareReason="New York's first title since 1973. Jalen Brunson Finals MVP. Game 5 in San Antonio, 94-90, 45 points.",
    teaser="Knicks beat the Spurs 4-1, 3-13 June. Game 4: 107-106 from 29 down, OG Anunoby 1.2 seconds. Game 5: Brunson 45 on the road.",
    story="Why this one matters: 53 years is long enough that people in the building had never seen the last one. The Knicks beat the San Antonio Spurs 4-1 in June and the city remembered how to throw a parade.\n\nThe series, from Wikipedia and NBA.com: Game 1 Knicks 105-95 in San Antonio. Game 2 Knicks 105-104. Game 3 Spurs 115-111 at MSG. Game 4 Knicks 107-106, largest Finals comeback on record, 29 points, Anunoby tip-in with 1.2 seconds left. Game 5 Knicks 94-90 in San Antonio, Brunson 45, tying Michael Jordan for most points on the road in a series-clinching Finals game.\n\nMike Brown's Knicks. Mitch Johnson's Spurs, who had just beaten Oklahoma City 4-3 in the West. First Finals since 1995 in which a team won two straight road games to open. First since 1993 in which the road team won the first three.",
    stakes="A city that had waited since 1973.",
    rivalryAngle="New York versus the Spurs' new era, Wembanyama's first Finals trip ending in five.",
    funFacts=["Brunson 45 in Game 5.", "29-point comeback in Game 4, Anunoby 1.2s.", "First Knicks title since 1973."],
    keyPlayers=[{"name": "Jalen Brunson", "team": "Knicks", "hook": "Finals MVP. 45 in the clincher."}, {"name": "OG Anunoby", "team": "Knicks", "hook": "Tip-in, 1.2 seconds, Game 4."}],
    home="New York Knicks", away="San Antonio Spurs", group="NBA", date="2026-06-13", time="20:30",
    venue="Frost Bank Center", city="San Antonio", status="FINISHED", homeScore=94, awayScore=90,
    sport="basketball", competition="nba-finals-2026", season="2025-26", roundLabel="NBA Finals Game 5",
    resultSummary="Knicks win series 4-1. Game 5: 94-90.",
    tags=["nba", "knicks", "spurs", "finals"],
    sources=[{"name": "Wikipedia: 2026 NBA Finals", "url": "https://en.wikipedia.org/wiki/2026_NBA_Finals"}, {"name": "NBA.com Finals recap", "url": "https://www.nba.com/watch/list/collection/2026-nba-finals-game-recap-videos"}],
))

EVENTS.append(ev(
    slug="wnba-2026-playoff-field",
    headline="The WNBA field is set: Lynx 31-9, playoffs 27 September",
    whyCareScore=8.6,
    whyCareReason="September basketball in 2026 is the women's game. Eight teams, a 27 September start, Minnesota on top.",
    teaser="Seeds: Lynx 31-9, Valkyries 29-11, Aces 27-13, Dream 26-14, Fever 26-14, Liberty 24-16, Mystics 24-16, Wings 24-16.",
    story="Why this one matters: the NBA is in its offseason. The WNBA just locked an eight-team field and the playoffs begin 27 September. If you want basketball that still has a scoreboard in September, this is it.\n\nWNBA.com standings: Minnesota Lynx 31-9, Golden State Valkyries 29-11, Las Vegas Aces 27-13, Atlanta Dream 26-14, Indiana Fever 26-14, New York Liberty 24-16, Washington Mystics 24-16, Dallas Wings 24-16. First round is best of three. Semifinals best of five. Finals best of seven for the second time.\n\nThe Aces are the defending champions from 2025. The Lynx have the one-seed. The Valkyries, in year two, have the two-seed. Do not invent a 2026 champion. The games have not started.",
    stakes="Home court, a one-seed, a 27 September start.",
    rivalryAngle="Lynx versus a field that includes last year's champions and a second-year Valkyries side.",
    funFacts=["Playoffs begin 27 September 2026.", "Lynx 31-9, best record.", "Four teams tied at 24-16 for seeds 6 through 8."],
    keyPlayers=[{"name": "Minnesota Lynx", "team": "Lynx", "hook": "31-9, one-seed, clinched 9 August."}, {"name": "Golden State Valkyries", "team": "Valkyries", "hook": "29-11, two-seed in year two."}],
    home="Minnesota Lynx", away="Playoff field", group="WNBA", date="2026-09-27", time="19:00",
    venue="Target Center", city="Minneapolis", status="UPCOMING",
    sport="basketball", competition="wnba-2026", season="2026", roundLabel="Playoffs preview",
    tags=["wnba", "lynx", "playoffs"],
    sources=[{"name": "WNBA.com standings", "url": "https://www.wnba.com/standings"}, {"name": "Wikipedia: 2026 WNBA playoffs", "url": "https://en.wikipedia.org/wiki/2026_WNBA_playoffs"}],
))

# --- F1 ---
EVENTS.append(ev(
    slug="british-gp-2026",
    headline="Leclerc wins Silverstone. The championship leader finishes 15th from pole.",
    whyCareScore=8.9,
    whyCareReason="Charles Leclerc's Ferrari wins the British Grand Prix. Kimi Antonelli started first and finished 15th. That is a title race finding weather.",
    teaser="5 July, Silverstone. Leclerc 1:27:11.335. Russell second by 0.427, Hamilton third by 0.772. Antonelli pole, P15.",
    story="Why this one matters: a championship leader starting on pole at Silverstone is supposed to bank 25 points. Antonelli banked none that counted. Leclerc won in 1:27:11.335. George Russell was 0.427 behind. Lewis Hamilton 0.772 behind. A Ferrari 1-3 with a Mercedes in the sandwich.\n\nAntonelli's Sky Sports driver page lists Great Britain: grid 1st, finish 15th. The lead he had been building since China suddenly had a dent. Russell closed. Hamilton, already a winner in Barcelona, stood on another podium in red.\n\nFive days later Belgium would restore the kid. This Sunday belongs to Leclerc.",
    stakes="A home-soil weekend for Russell, a first 2026 win for Leclerc, a dent in Antonelli's march.",
    rivalryAngle="Mercedes pole to 15th. Ferrari first and third.",
    funFacts=["Leclerc race time 1:27:11.335.", "Russell +0.427, Hamilton +0.772.", "Antonelli pole, classified 15th."],
    keyPlayers=[{"name": "Charles Leclerc", "team": "Ferrari", "hook": "Won Silverstone, 5 July."}, {"name": "Kimi Antonelli", "team": "Mercedes", "hook": "Pole. Finished 15th."}],
    home="Charles Leclerc", away="George Russell", group="F1", date="2026-07-05", time="15:00",
    venue="Silverstone", city="Silverstone", status="FINISHED", format="race",
    sport="f1", competition="f1-2026", season="2026", roundLabel="British Grand Prix",
    resultSummary="1 Leclerc, 2 Russell +0.427, 3 Hamilton +0.772. Antonelli P15 from pole.",
    leaderboard=[
        {"pos": "1", "name": "Charles Leclerc", "score": "1:27:11.335", "note": "Ferrari"},
        {"pos": "2", "name": "George Russell", "score": "+0.427", "note": "Mercedes"},
        {"pos": "3", "name": "Lewis Hamilton", "score": "+0.772", "note": "Ferrari"},
        {"pos": "15", "name": "Kimi Antonelli", "score": "P15", "note": "Mercedes, started P1"},
    ],
    tags=["f1", "silverstone", "leclerc"],
    sources=[{"name": "Sky Sports F1 2026 results", "url": "https://www.skysports.com/f1/results"}, {"name": "Sky: Antonelli results", "url": "https://www.skysports.com/f1/drivers/kimi-antonelli/results"}],
))

EVENTS.append(ev(
    slug="belgian-gp-2026",
    headline="Antonelli wins Spa: sixth of the season, the lead grows again",
    whyCareScore=8.5,
    whyCareReason="A week after Silverstone's 15th, the championship leader wins Belgium. Mercedes in the new-rules year keeps answering.",
    teaser="19 July, Spa. Antonelli 1:24:42.479. Leclerc +1.952, Verstappen +11.586. Sixth win of 2026.",
    story="Why this one matters: title races are not won at Silverstone when you finish 15th. They are not lost there either if you win Spa seven days later.\n\nKimi Antonelli won the Belgian Grand Prix in 1:24:42.479. Charles Leclerc was 1.952 behind. Max Verstappen 11.586 behind. RaceFans logged it as his sixth victory of 2026 and another extension of the championship lead.\n\nThe 2026 regulations were billed as the biggest changes ever. Mercedes has been the answer. Antonelli has been the name on the answers.",
    stakes="Restoring a championship lead after a home-soil wreck at Silverstone.",
    rivalryAngle="Antonelli versus Leclerc, one week after the Ferrari win in Britain.",
    funFacts=["Antonelli's sixth win of 2026.", "Race time 1:24:42.479.", "Leclerc second, Verstappen third."],
    keyPlayers=[{"name": "Kimi Antonelli", "team": "Mercedes", "hook": "Won Spa, sixth of the year."}, {"name": "Charles Leclerc", "team": "Ferrari", "hook": "Second, 1.952 behind."}],
    home="Kimi Antonelli", away="Charles Leclerc", group="F1", date="2026-07-19", time="14:00",
    venue="Spa-Francorchamps", city="Spa", status="FINISHED", format="race",
    sport="f1", competition="f1-2026", season="2026", roundLabel="Belgian Grand Prix",
    resultSummary="1 Antonelli, 2 Leclerc +1.952, 3 Verstappen +11.586",
    leaderboard=[
        {"pos": "1", "name": "Kimi Antonelli", "score": "1:24:42.479", "note": "Mercedes"},
        {"pos": "2", "name": "Charles Leclerc", "score": "+1.952", "note": "Ferrari"},
        {"pos": "3", "name": "Max Verstappen", "score": "+11.586", "note": "Red Bull"},
    ],
    tags=["f1", "spa", "antonelli"],
    sources=[{"name": "Sky Sports F1 results", "url": "https://www.skysports.com/f1/results"}, {"name": "RaceFans Belgian GP", "url": "https://www.racefans.net/category/race-results"}],
))

EVENTS.append(ev(
    slug="dutch-gp-2026",
    headline="Norris wins Zandvoort. McLaren's counter finally has a double.",
    whyCareScore=8.3,
    whyCareReason="Lando Norris followed Hungary with the Dutch Grand Prix. Two in a row. Antonelli still left with the lead, and second place.",
    teaser="23 August. Norris 2:04:44.859 from pole. Antonelli second, Russell third. Verstappen DNF at home.",
    story="Why this one matters: McLaren needed a stretch that looked like a challenge, not a cameo. Norris won Hungary on 26 July (1:39:56.180, Verstappen second, Antonelli third). He then won Zandvoort from pole in 2:04:44.859. Antonelli second, Russell third.\n\nMax Verstappen did not finish his home race. ESPN's 2026 recap lists him DNF at Zandvoort. The orange crowd did not get the story it came for. It got a McLaren one.\n\nAntonelli still left the Netherlands with the championship lead. Two weeks later he would win Monza from 19th. The counter was real. So was the leader.",
    stakes="A McLaren double after the summer break, and a home DNF for Verstappen.",
    rivalryAngle="Norris on a heater versus a Mercedes 2-3.",
    funFacts=["Norris won Hungary and the Netherlands back to back.", "Dutch GP time 2:04:44.859.", "Verstappen DNF at Zandvoort."],
    keyPlayers=[{"name": "Lando Norris", "team": "McLaren", "hook": "Pole and win at Zandvoort."}, {"name": "Kimi Antonelli", "team": "Mercedes", "hook": "Second, lead intact."}],
    home="Lando Norris", away="Kimi Antonelli", group="F1", date="2026-08-23", time="14:00",
    venue="Circuit Zandvoort", city="Zandvoort", status="FINISHED", format="race",
    sport="f1", competition="f1-2026", season="2026", roundLabel="Dutch Grand Prix",
    resultSummary="1 Norris, 2 Antonelli +11.536, 3 Russell +15.906. Verstappen DNF.",
    leaderboard=[
        {"pos": "1", "name": "Lando Norris", "score": "2:04:44.859", "note": "McLaren"},
        {"pos": "2", "name": "Kimi Antonelli", "score": "+11.536", "note": "Mercedes"},
        {"pos": "3", "name": "George Russell", "score": "+15.906", "note": "Mercedes"},
    ],
    tags=["f1", "zandvoort", "norris"],
    sources=[{"name": "Sky Sports F1 results", "url": "https://www.skysports.com/f1/results"}, {"name": "ESPN 2026 race recap", "url": "https://www.espn.com/f1/story/_/id/49535228/formula-1-2026-results-kimi-antonelli-lewis-hamilton-george-russell-winners-podium-final-positions-every-race"}],
))

EVENTS.append(ev(
    slug="italian-gp-2026",
    headline="Antonelli wins Monza from 19th. First Italian home win since 1966.",
    whyCareScore=9.9,
    whyCareReason="Grid 19, chequered flag 1. Pierre Gasly's first pole. A Mercedes one-two. A 66-point lead. History in the grandstands.",
    teaser="6 September. Antonelli 1:51:15.281 from P19. Russell +3.857, Verstappen +14.718. First Italian Monza winner since Ludovico Scarfiotti.",
    story="Why this one matters: home races are supposed to go wrong. This one went from nineteenth to first, and Italy had not done that at Monza since Ludovico Scarfiotti in 1966. No one had won from as far back as 19th since John Watson from 22nd at Long Beach in 1983.\n\nPierre Gasly took Alpine's first pole. Russell led by lap two. Antonelli climbed through a race that lasted 1:51:15.281 and passed his teammate late. Russell second by 3.857. Verstappen third by 14.718. Norris fourth, Piastri fifth, Hamilton sixth. Leclerc, Alonso and Stroll did not finish. Fastest lap Antonelli, 1:23.504. BBC, Wikipedia and ESPN agree on the classified order.\n\nChampionship: Antonelli 267, Russell 201, Hamilton 191, Norris 171, Leclerc 155. Constructors: Mercedes 468, Ferrari 346, McLaren 287. Seventh win of the season. Next is Madrid, a new circuit, 11-13 September.",
    stakes="A home win, a 66-point lead, a constructors grip, a new track next week.",
    rivalryAngle="Teammates at the front. Ferrari in the gravel. Italy in the grandstands.",
    funFacts=["Started 19th, won.", "First Italian Monza winner since 1966.", "Drivers' lead 66 points after the race."],
    keyPlayers=[{"name": "Kimi Antonelli", "team": "Mercedes", "hook": "P19 to P1, seventh win, 267 points."}, {"name": "Pierre Gasly", "team": "Alpine", "hook": "First career pole, finished seventh."}],
    home="Kimi Antonelli", away="George Russell", group="F1", date="2026-09-06", time="14:00",
    venue="Monza", city="Monza", status="FINISHED", format="race",
    sport="f1", competition="f1-2026", season="2026", roundLabel="Italian Grand Prix",
    resultSummary="1 Antonelli (P19), 2 Russell +3.857, 3 Verstappen +14.718. Lead 267-201.",
    leaderboard=[
        {"pos": "1", "name": "Kimi Antonelli", "score": "1:51:15.281", "note": "Mercedes, started P19"},
        {"pos": "2", "name": "George Russell", "score": "+3.857", "note": "Mercedes"},
        {"pos": "3", "name": "Max Verstappen", "score": "+14.718", "note": "Red Bull"},
        {"pos": "4", "name": "Lando Norris", "score": "+19.056", "note": "McLaren"},
        {"pos": "5", "name": "Oscar Piastri", "score": "+19.253", "note": "McLaren"},
        {"pos": "6", "name": "Lewis Hamilton", "score": "+24.655", "note": "Ferrari"},
    ],
    tags=["f1", "monza", "antonelli"],
    sources=[{"name": "BBC Italian GP results", "url": "https://www.bbc.co.uk/sport/formula1/2026/italian-grand-prix/results"}, {"name": "Wikipedia: 2026 Italian Grand Prix", "url": "https://en.wikipedia.org/wiki/2026_Italian_Grand_Prix"}, {"name": "ESPN 2026 results recap", "url": "https://www.espn.com/f1/story/_/id/49535228/formula-1-2026-results-kimi-antonelli-lewis-hamilton-george-russell-winners-podium-final-positions-every-race"}],
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
