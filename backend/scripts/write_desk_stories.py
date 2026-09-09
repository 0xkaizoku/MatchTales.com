"""Write sourced mini-blogs. No em-dashes. Facts from the locked plan only."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2] / "frontend" / "src" / "content" / "stories"

STORIES = []


def add(slug: str, body: str):
    STORIES.append((slug, body.strip() + "\n"))


add(
    "hull-city-manchester-united-opening-day.md",
    """---
title: "Hull City 2-0 Manchester United, and the season already has a scar"
subtitle: "A promoted side's first Premier League night in nine years. United lose. The table notices."
category: "Mini blog"
excerpt: "Semi Ajayi 17', Nobel Mendy 38'. Hull, everyone's favourites to go down, beat Manchester United 2-0 on 22 August."
image: "https://images.unsplash.com/photo-1574629810360-7efbbe195018?auto=format&fit=crop&w=1200&q=80"
readingTime: 6
pubDate: 2026-08-22
sport: soccer
competition: premier-league-2026-27
relatedSlug: hull-city-vs-manchester-united-mw1
sources:
  - name: "The Athletic: opening weekend"
    url: "https://www.nytimes.com/athletic/7535116/2026/08/25/premier-league-winners-losers-gameweek-one/"
  - name: "theScore opening weekend"
    url: "https://www.thescore.com/epl/news/3583101/analysis-from-opening-weekend-of-new-premier-league-season"
---

## Why this match matters

Promotion stories are supposed to wait. Hull City did not wait. On 22 August, in their first Premier League match in nine years, they beat Manchester United 2-0 at the MKM Stadium. If you care about the 2026/27 season, you care about the night the measuring stick fell over.

## What actually happened

Semi Ajayi scored in the 17th minute after a scramble from a corner. Nobel Mendy headed in close range in the 38th. The Athletic's opening-weekend notes put Oli McBurnie at the centre of Hull's performance. theScore logged the same scorers and the same 2-0.

Hull were billed as everyone's favourites to go down. Three games later they have seven points and have not conceded. United have four points after a 5-2 win over Ipswich and a 2-2 at Everton. The scar from Hull is still in the table.

## What it changes

United will be fine in the way big clubs are fine. Hull have a story the league cannot shrug off. Matchweek 4 sends Chelsea to Hull. That is the next sentence, not a result. The result is 2-0, already in the book.
""",
)

add(
    "premier-league-opening-weekend-2026.md",
    """---
title: "Opening weekend: Hull, Brighton, Brentford, and a league that did not ease in"
subtitle: "Ten matches, 21-24 August. Arsenal start with a 3-0. Chelsea win 3-2 at Fulham. Spurs lose 3-0 at Brentford."
category: "Mini blog"
excerpt: "Brighton 4-0 Villa. Hull 2-0 United. Brentford 3-0 Spurs. Arsenal 3-0 Coventry. The 2026/27 Premier League arrived loud."
image: "https://images.unsplash.com/photo-1522778119026-d647f0596c07?auto=format&fit=crop&w=1200&q=80"
readingTime: 7
pubDate: 2026-08-24
sport: soccer
competition: premier-league-2026-27
sources:
  - name: "The Athletic: opening weekend"
    url: "https://www.nytimes.com/athletic/7535116/2026/08/25/premier-league-winners-losers-gameweek-one/"
  - name: "SportPesa matchweek 1 roundup"
    url: "https://blog.ke.sportpesa.com/2026/08/26/premier-league-2026-27-matchweek1/"
---

## Why this weekend matters

Opening weekends are supposed to be rust. This one was a statement board. If you only watched the World Cup and came back late, here is the league you missed.

## The results we can print

21 August: Arsenal 3-0 Coventry. Havertz, Saka, Odegaard. Champions, home, clean.

22 August: Hull 2-0 Manchester United. Everton 2-0 Crystal Palace (Dewsbury-Hall, Thierno Barry). Ipswich 2-1 Sunderland, Jack Clarke 90'. Nottingham Forest 0-1 Leeds, Anton Stach 88' free-kick. Brentford 3-0 Tottenham.

23 August: Brighton 4-0 Aston Villa. Manchester City 2-1 Bournemouth. Newcastle 2-2 Liverpool, Szoboszlai 99' penalty.

24 August: Fulham 2-3 Chelsea. Xabi Alonso's first league game. Joao Pedro, Morgan Rogers, Cole Palmer.

## What it changes

Brighton sat top. Hull had a scar to sell. Spurs, who spent the summer trying not to repeat last year, opened with a 3-0 loss that theScore called their worst under Roberto De Zerbi. Chelsea won ugly-beautiful. The table after one week already had a personality.
""",
)

add(
    "xabi-alonso-chelsea-first-three.md",
    """---
title: "Alonso's Chelsea: 3-2, 4-3, then 2-1 at the Emirates"
subtitle: "Seven goals in two wins, then a first loss. The start is loud. The defence is the argument."
category: "Mini blog"
excerpt: "Chelsea beat Fulham 3-2 and Brighton 4-3, then lost 2-1 at Arsenal. Rogers scored after 77 seconds in all three? No: inside five minutes in each of the first three."
image: "https://images.unsplash.com/photo-1522778119026-d647f0596c07?auto=format&fit=crop&w=1200&q=80"
readingTime: 6
pubDate: 2026-09-06
sport: soccer
competition: premier-league-2026-27
relatedSlug: arsenal-vs-chelsea-mw3
sources:
  - name: "ESPN: Chelsea 4-3 Brighton"
    url: "https://www.espn.co.uk/football/match/_/gameId/401879317/brighton-hove-albion-chelsea"
  - name: "The Independent: Arsenal 2-1 Chelsea"
    url: "https://www.independent.co.uk/sport/football/arsenal-chelsea-live-stream-score-premier-league-result-b3044763.html"
  - name: "PremierLeague.com Sunday wrap"
    url: "https://www.premierleague.com/en/news/4706438/sunday-wrap-arsenal-pass-big-early-test-after-late-drama-at-everton"
---

## Why this start matters

Xabi Alonso's first three Premier League games scored like a pinball table. Fulham 2-3 Chelsea on 24 August. Chelsea 4-3 Brighton on 30 August. Arsenal 2-1 Chelsea on 6 September. Six points from nine. Eight goals scored, seven conceded. That is a personality, not a plan you put on a slide.

## What actually happened

Against Fulham, Joao Pedro, Morgan Rogers and Cole Palmer scored in Alonso's first league match. Against Brighton, Romeo Lavia 4', Pedro Neto 14', Joao Pedro 32', Cole Palmer 74'. Brighton: Malick Yalcouye 35', a Joao Pedro own goal 63', Pascal Gross 90+6'. ESPN noted Brighton were the first side in 50 years to score three or more in four successive league games against Chelsea. They still lost.

At the Emirates, Rogers volleyed Chelsea ahead after 77 seconds. PremierLeague.com says Chelsea became the first team in Premier League history to score inside the opening five minutes in each of their first three games. Havertz equalised in the 25th. Odegaard won it after the break. Raya saved Estevao late. Alonso used the word suffering.

## What it changes

Chelsea are fourth on six points. Arsenal and City have nine. The attack is not the question. The question is whether a team that concedes seven in three can live in a title sentence. Matchweek 4 is Chelsea vs Hull. Hull have not conceded. That is the next test, not a result.
""",
)

add(
    "premier-league-after-three-weeks.md",
    """---
title: "Three weeks in: City and Arsenal on 9, Hull on 7, Spurs on 1"
subtitle: "The table after 6 September is not a joke. It is three games old and already rude."
category: "Mini blog"
excerpt: "Manchester City 9, Arsenal 9, Hull City 7 with a clean sheet. Tottenham 1 point. Fulham and Coventry 0. Matchweek 4 starts 12 September."
image: "https://images.unsplash.com/photo-1522778119026-d647f0596c07?auto=format&fit=crop&w=1200&q=80"
readingTime: 6
pubDate: 2026-09-07
sport: soccer
competition: premier-league-2026-27
sources:
  - name: "Wikipedia: 2026-27 Premier League table"
    url: "https://en.wikipedia.org/wiki/2026%E2%80%9327_Premier_League"
  - name: "Xinhua standings 6 Sep"
    url: "https://english.news.cn/20260907/3bee8725a60d4c4bbd473dbd20f8d91f/c.html"
---

## Why this table matters

Three games is a small sample. It is also the only sample we have. After 6 September, Manchester City and Arsenal have 9 points. Hull City have 7 and have not conceded a goal. Tottenham have 1 point and 0 goals. Fulham and Coventry have 0 points.

## Matchweek 3, the last data point

Ipswich 0-2 Liverpool (Isak 6', 9'). Newcastle 2-2 Bournemouth. Forest 0-0 Spurs. Fulham 2-3 Crystal Palace. Brentford 1-1 Sunderland. City 1-0 Coventry. Brighton 1-1 Leeds. Hull 0-0 Villa. Everton 2-2 United. Arsenal 2-1 Chelsea.

Liverpool have their first win. Palace have their first win. Hull's clean sheet is now three games old. Arsenal's start is their first three-win opening conceding fewer than two since the Invincibles season, per PremierLeague.com.

## What it changes

Matchweek 4 begins 12 September. Chelsea vs Hull. Sunderland vs Arsenal. Spurs vs Everton. Those are previews. They are not scores. The table above is the last true thing we can print until those matches are played.
""",
)

add(
    "premier-league-matchweek-four-preview.md",
    """---
title: "Why matchweek 4 matters: Hull vs Chelsea, Sunderland vs Arsenal"
subtitle: "From 12 September. No scores. Just the fixtures that can confirm or wreck the three-week table."
category: "Preview"
excerpt: "Chelsea host Hull, the only side without a goal conceded. Sunderland host Arsenal. Spurs host Everton. Nothing has been played."
image: "https://images.unsplash.com/photo-1522778119026-d647f0596c07?auto=format&fit=crop&w=1200&q=80"
readingTime: 5
pubDate: 2026-09-08
sport: soccer
competition: premier-league-2026-27
sources:
  - name: "FBref 2026-27 schedule"
    url: "https://fbref.com/en/comps/9/schedule/Premier-League-Scores-and-Fixtures"
---

## Why this weekend matters

The table after three games is rude. Matchweek 4 is the first chance it has to apologise, or to get ruder.

FBref's fixture list, still unplayed as of 8 September: Saturday 12 September includes Crystal Palace vs Ipswich, Aston Villa vs Nottingham Forest, Liverpool vs Fulham, Chelsea vs Hull City, Bournemouth vs Brentford, Tottenham vs Everton, Sunderland vs Arsenal. Sunday: Coventry vs Brighton, and more to follow on the sheet.

## The two sentences that count

Chelsea vs Hull is a first-place-adjacent side against a promoted club that has not conceded. Sunderland vs Arsenal is a promoted club hosting the champions. Spurs vs Everton is a side with one point and zero goals trying to remember how scoring works.

## What we will not do

We will not invent a 12 September score on 8 September. Come back after the whistle.
""",
)

add(
    "noskova-wimbledon-2026.md",
    """---
title: "Noskova wastes five championship points. Then she wins Wimbledon."
subtitle: "6-2, 5-7, 6-3. All-Czech. Age 21. Youngest women's champion here since Kvitova in 2011."
category: "Mini blog"
excerpt: "Linda Noskova beat Karolina Muchova in an extraordinary Wimbledon final on 11 July. First Slam. Sixth championship point."
image: "https://images.unsplash.com/photo-1554068865-24cecd4e34b8?auto=format&fit=crop&w=1200&q=80"
readingTime: 6
pubDate: 2026-07-11
sport: tennis
competition: wimbledon-2026
relatedSlug: noskova-vs-muchova-wimbledon-final
sources:
  - name: "BBC Wimbledon final"
    url: "https://www.bbc.com/sport/tennis/articles/ce37x57gv49o"
  - name: "The Athletic"
    url: "https://www.nytimes.com/athletic/7437108/2026/07/11/wimbledon-final-karolina-muchova-linda-noskova-result-analysis/"
---

## Why this final matters

Wimbledon finals are supposed to be appointments with names you already know. On 11 July the names were Czech, seeded 9 and 10, and friends. Linda Noskova is 21. She is now a Grand Slam champion. That sentence did not exist in June.

## What actually happened

She led 6-2, 5-2. Karolina Muchova won five games in a row and saved five championship points. The second set went 7-5 to Muchova. In the third, Noskova served for it again, hit an ace to set up a sixth championship point, and converted with a service winner. Score: 6-2, 5-7, 6-3.

BBC, The Athletic and CBS logged the same numbers. Youngest women's Wimbledon champion since Petra Kvitova in 2011. First Slam. She had already won Berlin on the grass. Sportico put the prize money around $4.8 million, nearly doubling her career on-court earnings.

## What it changes

On 8 September she met Aryna Sabalenka in the US Open quarter-finals and lost 7-6 (7-1), 3-6, 7-6 (10-7). Wimbledon was the first plot twist. New York ended in a tie-break.
""",
)

add(
    "sinner-zverev-wimbledon-final-2026.md",
    """---
title: "Sinner's fifth major: two tiebreaks, then the champion's weight"
subtitle: "6-7 (7-9), 7-6 (7-2), 6-3, 6-4. Zverev had Roland Garros. Sinner still had Wimbledon."
category: "Mini blog"
excerpt: "Jannik Sinner beat Alexander Zverev in four sets on 12 July for a second straight Wimbledon and a fifth Slam."
image: "https://images.unsplash.com/photo-1554068865-24cecd4e34b8?auto=format&fit=crop&w=1200&q=80"
readingTime: 6
pubDate: 2026-07-12
sport: tennis
competition: wimbledon-2026
relatedSlug: sinner-vs-zverev-wimbledon-final
sources:
  - name: "CBS Wimbledon winners"
    url: "https://www.cbssports.com/tennis/news/wimbledon-2026-results-winners-jannik-sinner-linda-noskova/live/"
  - name: "Wikipedia: 2026 in tennis"
    url: "https://en.wikipedia.org/wiki/2026_in_tennis"
---

## Why this final matters

Alexander Zverev won Roland Garros. The Channel Slam is the sentence people reach for when a clay champion walks onto Centre Court. Jannik Sinner had not won a major in 2026 yet: Djokovic took him out in the Australian Open semis, heat exhaustion took him out in the French Open second round. Wimbledon was the argument that he is still the best player in the world.

## What actually happened

CBS: 6-7 (7-9), 7-6 (7-2), 6-3, 6-4. First break of the match at 5-3 in the third, Zverev long in rallies. Championship point after a 23-shot rally, Sinner's forehand. One hundred major match wins. Second straight Wimbledon. Fifth Slam.

The first two sets were serve. The last two were the favourite remembering the job.

## What it changes

Sinner has the grass. Zverev has the clay. The hard-court year is still open. The US Open, as of 8 September, has not named a men's champion. Sinner's name is not on that draw's last eight in the pieces we locked. The Wimbledon trophy is.
""",
)

add(
    "muchova-mensik-us-open-mixed.md",
    """---
title: "Muchova and Mensik take the mixed doubles million"
subtitle: "6-3, 1-6, [10-6] over Bencic and Cobolli. First Slam title for both. 26 August, Arthur Ashe."
category: "Mini blog"
excerpt: "The all-Czech pair won the 2026 US Open mixed doubles, saving match points in the semis, then rolling the final tiebreak."
image: "https://images.unsplash.com/photo-1554068865-24cecd4e34b8?auto=format&fit=crop&w=1200&q=80"
readingTime: 5
pubDate: 2026-08-26
sport: tennis
competition: us-open-2026
sources:
  - name: "usopen.org mixed doubles final"
    url: "https://www.usopen.org/en_US/news/articles/2026-08-26/muchova-mensik_win_2026_us_open_mixed_doubles_title.html"
---

## Why this one matters

The US Open now plays mixed doubles as a two-day, million-dollar event that starts the tournament. On 26 August the trophy went to Karolina Muchova and Jakub Mensik, an all-Czech pair, 6-3, 1-6, [10-6] over Belinda Bencic and Flavio Cobolli.

## What actually happened

They saved two match points from 7-9 in the semi-final tiebreak against Mirra Andreeva and Andrey Rublev, then won the last four points of that match. In the final they rolled three straight from 1-1 in the match tiebreak. Mensik closed with an ace on a third championship point. First Slam title in any discipline for both. Prize money $1 million.

Muchova had just played a Wimbledon final in July and lost it. New York gave her a title anyway, in a different key.

## What it changes

Mensik called it his first time standing there. The singles tournament was only beginning. As of 8 September the singles trophies are still unclaimed. This one is in the cabinet.
""",
)

add(
    "us-open-2026-draw-cracks.md",
    """---
title: "Alcaraz's wrist, Djokovic's Monday, the draw cracking open"
subtitle: "The defending champion is back from four months out. Novak Djokovic lost in round one. New York noticed both."
category: "Mini blog"
excerpt: "US Open 2026, 30 August to 13 September. Alcaraz returned. Djokovic went out Monday. No singles champion yet."
image: "https://images.unsplash.com/photo-1554068865-24cecd4e34b8?auto=format&fit=crop&w=1200&q=80"
readingTime: 6
pubDate: 2026-09-01
sport: tennis
competition: us-open-2026
sources:
  - name: "usopen.org Monday recap"
    url: "https://www.usopen.org/en_US/news/articles/2026-08-31/who_won_on_monday_at_the_2026_us_open_results_and_highlights.html"
  - name: "Wikipedia: 2026 US Open"
    url: "https://en.wikipedia.org/wiki/2026_US_Open_(tennis)"
---

## Why this fortnight matters

A Grand Slam is a draw that pretends it is fair. The 2026 US Open opened with two facts that are not fair at all: Carlos Alcaraz had not played a match in about four months because of a right wrist injury, and Novak Djokovic lost in the first round for only the third time at a major in his career.

## What actually happened

Alcaraz beat Roman Safiullin 6-4, 6-4, 6-4 on Monday and said he forgot how match day looks. His body felt great after. Sabalenka opened a bid for a third straight title 6-2, 6-4 against Camila Osorio. Stefanos Tsitsipas upset Cincinnati champion Arthur Fils. Stan Wawrinka's Grand Slam career ended against Matteo Berrettini.

Djokovic's Monday is the line that will follow the tournament even if he is gone. Wikipedia logged it as only the third opening-round major loss of his career.

## What it changes

By 8 September Alcaraz is in the quarter-finals against Ben Shelton. The American men have a gauntlet. The women's three-peat is still alive. The champion is not named. That is the honest version of New York today.
""",
)

add(
    "us-open-quarterfinals-why-tuesday-matters.md",
    """---
title: "Why Tuesday in New York matters"
subtitle: "Alcaraz-Shelton. Tiafoe-Michelsen. Sabalenka-Noskova. Pegula-Navarro. The US Open is still live."
category: "Preview"
excerpt: "Quarter-finals as of 7-8 September 2026. No 2026 singles champion. The American men have not had a Slam title since Roddick in 2003."
image: "https://images.unsplash.com/photo-1554068865-24cecd4e34b8?auto=format&fit=crop&w=1200&q=80"
readingTime: 6
pubDate: 2026-09-08
sport: tennis
competition: us-open-2026
relatedSlug: alcaraz-vs-shelton-uso-qf
sources:
  - name: "Reuters QF preview"
    url: "https://www.reuters.com/sports/tennis/shelton-next-up-alcaraz-tackles-all-american-gauntlet-path-us-open-final-2026-09-07/"
  - name: "NBC: American men in the quarters"
    url: "https://www.nbcsports.com/tennis/news/shelton-tiafoe-and-michelsen-win-at-the-us-open-as-american-men-aim-to-end-a-grand-slam-drought"
---

## Why these four matches matter

The US Open ends 13 September. On 8 September it is still a quarter-final tournament. That is the most honest thing we can print.

Men: Carlos Alcaraz vs Ben Shelton. Frances Tiafoe vs Alex Michelsen. Women: Aryna Sabalenka vs Linda Noskova. Jessica Pegula vs Emma Navarro. Reuters put Alcaraz-Shelton in the Ashe night session. Sabalenka-Noskova and Tiafoe-Michelsen in the day.

## The American sentence

The United States has not had a men's major champion since Andy Roddick here in 2003. Three American men are in the last eight. Tiafoe beat 2021 champion Daniil Medvedev 7-6 (1), 6-4, 7-6 (6). Shelton beat Tsitsipas 6-2, 6-3, 6-4. Michelsen reached his first Slam quarter. As of the day session, Tiafoe-Michelsen is live in a fifth set: 5-7, 3-6, 7-5, 6-3, 3-4. That is a score, not a winner.

## The women's sentence

Sabalenka is through: 7-6 (7-1), 3-6, 7-6 (10-7) over Noskova, the Wimbledon champion. Pegula and Navarro are still an all-American quarter. Do not pick that winner. Pick a chair.
""",
)

add(
    "ryan-fox-open-championship-2026.md",
    """---
title: "Ryan Fox birdies the 18th and the Claret Jug changes hands"
subtitle: "72-68-62-68 = 270. One shot ahead of Cameron Young. Third New Zealander to win a men's major."
category: "Mini blog"
excerpt: "The 154th Open at Royal Birkdale, 16-19 July. Fox, 39, birdied the hardest hole of the week to win by one."
image: "https://images.unsplash.com/photo-1535131749006-b7f58c99034b?auto=format&fit=crop&w=1200&q=80"
readingTime: 6
pubDate: 2026-07-19
sport: golf
competition: the-open-2026
relatedSlug: the-open-2026-royal-birkdale
sources:
  - name: "Wikipedia: 2026 Open Championship"
    url: "https://en.wikipedia.org/wiki/2026_Open_Championship"
  - name: "CBS Open recap"
    url: "https://www.cbssports.com/golf/news/open-2026-leaderboard-live-updates-round-4-scores-results/live/"
---

## Why this major matters

Majors are supposed to belong to the names on the world ranking. On 19 July a 39-year-old from New Zealand birdied the 18th at Royal Birkdale and became Champion Golfer of the Year. Ryan Fox is the third Kiwi to win a men's major. That is not a cute fact. That is the story.

## What actually happened

Rounds: 72-68-62-68 = 270, ten under. Cameron Young 271 after a Sunday 64. Sam Burns 272. Tommy Fleetwood and Scottie Scheffler tied fourth at 273. The Saturday 62 tied the men's major record for lowest round. CBS called the 36-hole comeback the largest by position to win a men's major.

He began Sunday two behind Burns. He birdied 16 to tie Young at nine under. The 18th had played 161 strokes over par for the field. Fox hit the fairway, the approach to about 12 feet, and the putt. Purse $17.75 million, winner $3.2 million.

## What it changes

The last men's major of 2026 has a new name on it. Scheffler still had the FedEx Cup to play for in August. Fox had the jug. Both sentences are true.
""",
)

add(
    "scheffler-fedex-cup-2026.md",
    """---
title: "Scheffler at East Lake: second FedEx Cup, and the Tiger earnings line"
subtitle: "264, 16 under, three clear of Hovland. $10 million. World No. 1, again, with receipts."
category: "Mini blog"
excerpt: "Scottie Scheffler won the 2026 Tour Championship on 30 August, his second FedEx Cup in three years, and passed Tiger Woods in PGA Tour career earnings."
image: "https://images.unsplash.com/photo-1535131749006-b7f58c99034b?auto=format&fit=crop&w=1200&q=80"
readingTime: 6
pubDate: 2026-08-30
sport: golf
competition: fedex-cup-2026
relatedSlug: tour-championship-2026-east-lake
sources:
  - name: "Sky Sports Tour Championship"
    url: "https://www.skysports.com/golf/news/12176/13578960/tour-championship-scottie-scheffler-holds-off-viktor-hovland-to-claim-fedexcup-title-and-break-more-pga-tour-records"
  - name: "AP via OCR"
    url: "https://www.ocregister.com/2026/08/30/scottie-scheffler-wins-2nd-fedex-cup-tops-tiger-woods-in-pga-tour-career-earnings/"
---

## Why this one matters

People spent a summer asking if Scottie Scheffler had loosened his grip. He won one regular-season event, then won the FedEx St. Jude Championship, watched Wyndham Clark take the BMW, and closed East Lake from three back on Sunday.

## What actually happened

65-67-66-66 = 264, 16 under. Viktor Hovland 13 under. Ryan Gerard 12 under. Scheffler a 5-iron to 2 inches on the second hole, a 25-foot birdie on the fourth, the lead on the 13th. First time he posted the low 72-hole score at the Tour Championship. In 2024 he started with a two-shot lead under the old starting-strokes format.

AP: he moved past Tiger Woods for most PGA Tour career earnings. $10 million first prize. Second FedEx Cup (2024 and 2026). Rory McIlroy still has the most titles with three. Scheffler and Tiger have two.

## What it changes

The PGA Tour season, January to August, has a champion. The Presidents Cup is 25-28 September. That is preview, not a score. This score is 16 under, Scheffler.
""",
)

add(
    "presidents-cup-2026-preview.md",
    """---
title: "The next thing on the golf calendar is the Presidents Cup"
subtitle: "25-28 September. No result. The FedEx Cup is in Scheffler's bag. This is the team event that comes next."
category: "Preview"
excerpt: "Preview only. The 2026 Presidents Cup has not been played. Do not invent a winner."
image: "https://images.unsplash.com/photo-1535131749006-b7f58c99034b?auto=format&fit=crop&w=1200&q=80"
readingTime: 4
pubDate: 2026-09-08
sport: golf
competition: presidents-cup-2026
sources:
  - name: "Fox Sports AU Tour Championship note"
    url: "https://www.foxsports.com.au/golf/pga-tour-2026-tour-championship-final-round-leaderboard-world-no1-scottie-scheffler-wins-tour-championship-for-a-second-time-min-woo-lee-registers-top-five-finish-adam-scott-falls-away-scores-report-video/news-story/ecad67f78fe82a43c3638f592edb6da6"
---

## Why this preview matters

Golf seasons do not end when the FedEx Cup trophy is in the photo. They tilt toward team events. The Presidents Cup is scheduled 25-28 September 2026. As of 8 September it has not been played. That is the whole honest paragraph.

## What we can print

Scottie Scheffler is the FedEx Cup champion. Ryan Fox has the Claret Jug. 2026 majors, from Sky Sports' season recap: Masters McIlroy, PGA Championship Aaron Rai, US Open Wyndham Clark, The Open Fox. Those are completed. The Presidents Cup is not.

Fox Sports Australia, wrapping East Lake, pointed Australian eyes toward next month's Presidents Cup. We will do the same, without a fake flag on a fake scoreboard.

## What we will not print

A winner. A session score. A Sunday collapse. Come back after 28 September.
""",
)

add(
    "seahawks-super-bowl-lx.md",
    """---
title: "Super Bowl LX was 29-13. That is why Wednesday night is a rematch."
subtitle: "Seahawks beat Patriots on 8 February at Levi's Stadium. Kenneth Walker III, MVP. The 2026 season opens with the same two teams."
category: "Mini blog"
excerpt: "Seattle 29, New England 13. Walker 135 rush yards. Myers five field goals. Maye sacked six times. Second Seahawks title."
image: "https://images.unsplash.com/photo-1566577739112-5184e6ac4a4e?auto=format&fit=crop&w=1200&q=80"
readingTime: 6
pubDate: 2026-02-09
sport: football
competition: nfl-2026
relatedSlug: patriots-at-seahawks-kickoff-2026
sources:
  - name: "Wikipedia: Super Bowl LX"
    url: "https://en.wikipedia.org/wiki/Super_Bowl_LX"
  - name: "ESPN Super Bowl LX"
    url: "https://www.espn.com/nfl/story/_/id/47872705/seahawks-stifle-drake-maye-patriots-capture-super-bowl-lx"
  - name: "NFL.com Super Bowl hub"
    url: "https://www.nfl.com/super-bowl"
---

## Why this game still matters in September

The NFL season has not started. The Super Bowl already happened. That is not a paradox. That is why Patriots at Seahawks on 9 September is the only Week 1 game that arrives pre-loaded.

## What actually happened on 8 February

Levi's Stadium, Santa Clara. Seahawks 29, Patriots 13. Kenneth Walker III 27 carries, 135 yards, Super Bowl MVP, first running back to win it since Terrell Davis in 1998. Jason Myers five field goals, a Super Bowl record, first 200-point scorer in NFL history. Sam Darnold 19/38, 202 yards, 1 TD (AJ Barner), 0 INT. Drake Maye 27/43, 295 yards, 2 TD, 2 INT, sacked six times. Uchenna Nwosu returned a fumble 45 yards for a touchdown. Score by quarter: 3-0, 9-0, 12-0, 29-13.

Mike Macdonald, second-year head coach. Dark Side defence. Seattle's second title, the first since Super Bowl XLVIII. A rematch of Super Bowl XLIX, which New England won. The script flipped.

## What it changes

Kickoff is tomorrow night, 8:20 p.m. ET, NBC, Lumen Field. No 2026 regular-season score exists yet. This 29-13 is the only football result that belongs on the desk.
""",
)

add(
    "patriots-seahawks-kickoff-2026.md",
    """---
title: "Why Patriots at Seahawks is the only NFL game that exists yet"
subtitle: "Wednesday 9 September, 8:20 p.m. ET, NBC. Labor Day was as late as it can be. The rematch is the opener."
category: "Preview"
excerpt: "Week 1 has not been played. The opener is Super Bowl LX again. That is the stake."
image: "https://images.unsplash.com/photo-1566577739112-5184e6ac4a4e?auto=format&fit=crop&w=1200&q=80"
readingTime: 5
pubDate: 2026-09-08
sport: football
competition: nfl-2026
relatedSlug: patriots-at-seahawks-kickoff-2026
sources:
  - name: "FOX Week 1 schedule"
    url: "https://www.foxsports.com/stories/nfl/when-does-2026-nfl-season-start-complete-week-1-schedule"
  - name: "CBS Week 1 times"
    url: "https://www.cbssports.com/nfl/news/2026-nfl-schedule-dates-times/"
---

## Why tomorrow night matters

There is no Monday Night Football on 8 September. There is no Sunday slate in the book yet. There is a Wednesday opener because Labor Day 2026 fell on 7 September, as late as the calendar allows. The league put the Super Bowl rematch there.

Patriots at Seahawks, 8:20 p.m. ET, NBC. Seattle are defending champions. New England are the defending AFC champions. The last time they shared a field, it was 29-13 in Santa Clara.

## What comes after

Thursday: 49ers vs Rams at the Melbourne Cricket Ground, Netflix, 8:35 p.m. ET. Sunday 13 September: the rest of Week 1. Monday 14 September: Broncos at Chiefs, 8:15 p.m. ET, ESPN/ABC.

None of those have scores. Tomorrow has a kickoff time. That is enough.
""",
)

add(
    "49ers-rams-melbourne-2026.md",
    """---
title: "49ers vs Rams in Melbourne: the league leaves home on night two"
subtitle: "First NFL regular-season game in Australia. MCG. Netflix. 10 September."
category: "Preview"
excerpt: "Thursday 8:35 p.m. ET, Friday 10:35 a.m. AEST. NFC West, a cricket ground, a streaming app."
image: "https://images.unsplash.com/photo-1566577739112-5184e6ac4a4e?auto=format&fit=crop&w=1200&q=80"
readingTime: 4
pubDate: 2026-09-08
sport: football
competition: nfl-2026
relatedSlug: 49ers-vs-rams-melbourne-2026
sources:
  - name: "FOX Week 1"
    url: "https://www.foxsports.com/stories/nfl/when-does-2026-nfl-season-start-complete-week-1-schedule"
---

## Why this game matters

The NFL spent a century pretending the map stopped at the ocean. Week 1 of 2026 puts San Francisco and Los Angeles in a cricket ground on Netflix, 24 hours after a Super Bowl rematch.

Melbourne Cricket Ground. Thursday 10 September, 8:35 p.m. ET. Local Friday 10:35 a.m. AEST. First regular-season NFL game in Australia. The Rams are listed as the home side.

## What we will not print

A score. A quarterback rating. A winner. The game has not been played. The stake is the place.
""",
)

add(
    "knicks-nba-finals-2026.md",
    """---
title: "Knicks 4-1: 53 years, Brunson 45, a 29-point Game 4"
subtitle: "New York's first title since 1973. The series ran 3-13 June. The city remembered how to throw a parade."
category: "Mini blog"
excerpt: "Knicks beat the Spurs in five. Game 4: 107-106 from 29 down, OG Anunoby 1.2 seconds. Game 5: 94-90, Brunson 45 on the road."
image: "https://images.unsplash.com/photo-1546519638-68e109498ffc?auto=format&fit=crop&w=1200&q=80"
readingTime: 7
pubDate: 2026-06-14
sport: basketball
competition: nba-finals-2026
relatedSlug: nba-finals-2026-knicks-spurs
sources:
  - name: "Wikipedia: 2026 NBA Finals"
    url: "https://en.wikipedia.org/wiki/2026_NBA_Finals"
  - name: "NBA.com Finals recaps"
    url: "https://www.nba.com/watch/list/collection/2026-nba-finals-game-recap-videos"
---

## Why this series matters

Fifty-three years is long enough that people in the building had never seen the last one. The New York Knicks beat the San Antonio Spurs 4-1 in June. Jalen Brunson was Finals MVP. The wait ended.

## What actually happened

Game 1, 3 June: Knicks 105-95 in San Antonio. Game 2, 5 June: Knicks 105-104. Game 3, 8 June: Spurs 115-111 at MSG. Game 4, 10 June: Knicks 107-106, largest Finals comeback on record, 29 points in the second half, OG Anunoby tip-in with 1.2 seconds left. Game 5, 13 June: Knicks 94-90 in San Antonio, Brunson 45, tying Michael Jordan for most points on the road in a series-clinching Finals game.

Mike Brown's Knicks had swept Cleveland in the East. Mitch Johnson's Spurs had beaten Oklahoma City 4-3 in the West. First Finals since 1995 to open with two straight road wins. First since 1993 in which the road team won the first three.

## What it changes

September basketball is not the NBA. Training camp is still ahead. The title is in New York. That is the only basketball sentence the men's league gets on this desk until October.
""",
)

add(
    "wnba-playoff-picture-2026.md",
    """---
title: "The WNBA field is set: Lynx 31-9, playoffs 27 September"
subtitle: "Eight teams. A second-year Valkyries side on the two-seed. Defending champion Aces on the three. No 2026 champion yet."
category: "Mini blog"
excerpt: "Minnesota, Golden State, Las Vegas, Atlanta, Indiana, New York, Washington, Dallas. First round best of three. Finals best of seven."
image: "https://images.unsplash.com/photo-1546519638-68e109498ffc?auto=format&fit=crop&w=1200&q=80"
readingTime: 6
pubDate: 2026-09-08
sport: basketball
competition: wnba-2026
relatedSlug: wnba-2026-playoff-field
sources:
  - name: "WNBA.com standings"
    url: "https://www.wnba.com/standings"
  - name: "Wikipedia: 2026 WNBA playoffs"
    url: "https://en.wikipedia.org/wiki/2026_WNBA_playoffs"
---

## Why this field matters

If you want basketball with a scoreboard in September 2026, you want the WNBA. The regular season is complete. The playoffs begin 27 September. The one-seed is the Minnesota Lynx at 31-9.

## The eight

1 Lynx 31-9. 2 Golden State Valkyries 29-11. 3 Las Vegas Aces 27-13. 4 Atlanta Dream 26-14. 5 Indiana Fever 26-14. 6 New York Liberty 24-16. 7 Washington Mystics 24-16. 8 Dallas Wings 24-16.

First round best of three. Semifinals best of five. Finals best of seven for the second time in league history. The Aces are the defending champions from a 2025 sweep of Phoenix. The Valkyries, in year two, have the two-seed. The Lynx clinched a playoff berth on 9 August.

## What we will not print

A 2026 WNBA champion. The games start on 27 September. The table is the story until then.
""",
)

add(
    "september-belongs-to-the-wnba.md",
    """---
title: "September basketball is the women's game"
subtitle: "The Knicks are champions in June. The WNBA is the league that still has games. That is not a slight. That is a calendar."
category: "Mini blog"
excerpt: "NBA Finals ended 13 June. WNBA playoffs begin 27 September. If you came here for basketball this month, you came for the Lynx, the Valkyries, the Aces."
image: "https://images.unsplash.com/photo-1546519638-68e109498ffc?auto=format&fit=crop&w=1200&q=80"
readingTime: 5
pubDate: 2026-09-08
sport: basketball
competition: wnba-2026
sources:
  - name: "WNBA.com standings"
    url: "https://www.wnba.com/standings"
  - name: "Wikipedia: 2026 NBA Finals"
    url: "https://en.wikipedia.org/wiki/2026_NBA_Finals"
---

## Why this month matters

Sports desks love to talk about basketball in June and then forget the sport exists until October. That is a men's calendar. The WNBA just finished a 40-game season. Playoffs start 27 September. The NBA is in its offseason, title already hanging in New York.

## Two true things

The Knicks won the 2026 NBA Finals 4-1 over the Spurs, Brunson 45 in Game 5, 13 June. That series is archive.

The Lynx are 31-9. The Valkyries are 29-11. The Aces are 27-13 and still the defending champions until someone takes the trophy. That series has not started.

## What it changes

MatchTales will not pretend training-camp rumours are games. We will print the WNBA table until the WNBA games arrive. That is the honest basketball desk in September.
""",
)

add(
    "leclerc-silverstone-2026.md",
    """---
title: "Leclerc wins Silverstone. The championship leader finishes 15th from pole."
subtitle: "5 July. Ferrari first and third. Antonelli starts first and banks nothing. Title races find weather."
category: "Mini blog"
excerpt: "Charles Leclerc 1:27:11.335. Russell +0.427. Hamilton +0.772. Kimi Antonelli pole, classified 15th."
image: "https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?auto=format&fit=crop&w=1200&q=80"
readingTime: 5
pubDate: 2026-07-05
sport: f1
competition: f1-2026
relatedSlug: british-gp-2026
sources:
  - name: "Sky Sports F1 results"
    url: "https://www.skysports.com/f1/results"
  - name: "Sky: Antonelli results"
    url: "https://www.skysports.com/f1/drivers/kimi-antonelli/results"
---

## Why this race matters

A championship leader starting on pole at Silverstone is supposed to leave with 25 points. Kimi Antonelli left with a 15th and a dent. Charles Leclerc won the British Grand Prix in 1:27:11.335. George Russell was 0.427 behind. Lewis Hamilton 0.772 behind. Ferrari 1-3, Mercedes in the sandwich, the leader nowhere.

## What actually happened

Sky Sports' 2026 results board: Leclerc, Russell, Hamilton. Antonelli's driver page: Great Britain, grid 1st, finish 15th. That is the whole wreck. The new-regulations year had been a Mercedes year since China. Silverstone was the first Sunday that looked like a plot.

## What it changes

Seven days later Antonelli won Spa. The dent was not fatal. It was loud. Silverstone belongs to Leclerc.
""",
)

add(
    "antonelli-spa-2026.md",
    """---
title: "Antonelli wins Spa: sixth of the season, the lead grows again"
subtitle: "19 July. 1:24:42.479. Leclerc second. Verstappen third. The Silverstone dent gets an answer."
category: "Mini blog"
excerpt: "Kimi Antonelli's sixth win of 2026, a week after finishing 15th from pole in Britain."
image: "https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?auto=format&fit=crop&w=1200&q=80"
readingTime: 5
pubDate: 2026-07-19
sport: f1
competition: f1-2026
relatedSlug: belgian-gp-2026
sources:
  - name: "Sky Sports F1 results"
    url: "https://www.skysports.com/f1/results"
  - name: "RaceFans Belgian GP"
    url: "https://www.racefans.net/category/race-results"
---

## Why this race matters

Title races are not won at Silverstone when you finish 15th. They are not lost there either if you win Spa seven days later. Kimi Antonelli won the Belgian Grand Prix in 1:24:42.479. Charles Leclerc was 1.952 behind. Max Verstappen 11.586 behind. Sixth win of 2026.

## What actually happened

RaceFans logged the victory as another extension of the championship lead. Sky Sports has the same podium: Antonelli, Leclerc, Verstappen. The 2026 regulations were billed as the biggest changes ever. Mercedes has been the answer. Antonelli has been the name on the answers.

## What it changes

Hungary would go to Norris. Zandvoort would go to Norris. Monza would go to Antonelli from 19th. Spa is the Sunday that made Silverstone a dent instead of a collapse.
""",
)

add(
    "norris-hungary-zandvoort-2026.md",
    """---
title: "Norris wins Hungary, then Zandvoort. McLaren's counter has a double."
subtitle: "26 July and 23 August. Two in a row. Antonelli still left the Netherlands with the lead, and second place."
category: "Mini blog"
excerpt: "Lando Norris 1:39:56.180 at the Hungaroring, then 2:04:44.859 from pole at Zandvoort. Verstappen DNF at home."
image: "https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?auto=format&fit=crop&w=1200&q=80"
readingTime: 6
pubDate: 2026-08-23
sport: f1
competition: f1-2026
relatedSlug: dutch-gp-2026
sources:
  - name: "Sky Sports F1 results"
    url: "https://www.skysports.com/f1/results"
  - name: "ESPN 2026 race recap"
    url: "https://www.espn.com/f1/story/_/id/49535228/formula-1-2026-results-kimi-antonelli-lewis-hamilton-george-russell-winners-podium-final-positions-every-race"
---

## Why this stretch matters

McLaren needed a stretch that looked like a challenge, not a cameo. Lando Norris won the Hungarian Grand Prix on 26 July in 1:39:56.180, Verstappen second, Antonelli third. He then won the Dutch Grand Prix from pole on 23 August in 2:04:44.859, Antonelli second, Russell third.

## What actually happened

ESPN's 2026 recap lists Verstappen as a DNF at Zandvoort, his home race. The orange crowd did not get the story it came for. It got a McLaren one. Sky Sports has Norris's two wins in sequence, summer break in the middle.

Antonelli still left the Netherlands with the championship lead. Two weeks later he would win Monza from 19th. The counter was real. So was the leader.

## What it changes

A Mercedes year with a McLaren subplot is more interesting than a Mercedes year alone. Norris has two trophies in a row. Antonelli still has the points. Madrid is next.
""",
)

add(
    "antonelli-monza-from-nineteenth.md",
    """---
title: "Antonelli wins Monza from 19th. Italy had not done that since 1966."
subtitle: "Grid 19, flag 1. Gasly's first pole. Mercedes one-two. A 66-point lead. 6 September."
category: "Mini blog"
excerpt: "Kimi Antonelli 1:51:15.281. Russell +3.857. Verstappen +14.718. First Italian Monza winner since Ludovico Scarfiotti."
image: "https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?auto=format&fit=crop&w=1200&q=80"
readingTime: 7
pubDate: 2026-09-06
sport: f1
competition: f1-2026
relatedSlug: italian-gp-2026
sources:
  - name: "BBC Italian GP results"
    url: "https://www.bbc.co.uk/sport/formula1/2026/italian-grand-prix/results"
  - name: "Wikipedia: 2026 Italian Grand Prix"
    url: "https://en.wikipedia.org/wiki/2026_Italian_Grand_Prix"
---

## Why this race matters

Home races are supposed to go wrong. This one went from nineteenth to first, and Italy had not won its own Grand Prix since Ludovico Scarfiotti in 1966. No one had won from as far back as 19th since John Watson from 22nd at Long Beach in 1983. Kimi Antonelli did it in 1:51:15.281 at Monza on 6 September.

## What actually happened

Pierre Gasly took Alpine's first pole. Russell led by lap two. Antonelli climbed through a 53-lap race, passed his teammate late, and took the flag. Russell second by 3.857. Verstappen third by 14.718. Norris fourth, Piastri fifth, Hamilton sixth. Leclerc, Alonso and Stroll did not finish. Fastest lap Antonelli, 1:23.504. BBC, Wikipedia and ESPN agree on the classified order.

Championship after the race: Antonelli 267, Russell 201, Hamilton 191, Norris 171, Leclerc 155. Constructors: Mercedes 468, Ferrari 346, McLaren 287. Seventh win of the season.

## What it changes

Madrid is 11-13 September, a new circuit, the Madring. Ten races still sit on the board after that. A 66-point lead is not a title. It is a problem for everyone else. Italy has a home winner again. That sentence had been waiting 60 years.
""",
)

add(
    "f1-madrid-preview-2026.md",
    """---
title: "Why Madrid week matters: 66 points, a new circuit, ten races left"
subtitle: "Tag Heuer Spanish GP, Madring, 11-13 September. No result. Antonelli leads. The track is new."
category: "Preview"
excerpt: "Preview only. The 2026 Spanish Grand Prix in Madrid has not been run. Do not invent a winner."
image: "https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?auto=format&fit=crop&w=1200&q=80"
readingTime: 4
pubDate: 2026-09-08
sport: f1
competition: f1-2026
sources:
  - name: "ESPN F1 calendar"
    url: "https://www.espn.co.uk/f1/schedule"
  - name: "Wikipedia Italian GP standings"
    url: "https://en.wikipedia.org/wiki/2026_Italian_Grand_Prix"
---

## Why this preview matters

Formula 1 is putting a Grand Prix on a new Madrid circuit five days after Monza. New tracks scramble the form book. A 66-point lead does not. Kimi Antonelli has 267. George Russell has 201. Lewis Hamilton has 191. That is the championship as of 6 September.

## What we can print

The Tag Heuer Spanish GP is 11-13 September at the Madring. ESPN's calendar lists it as the next round. Wikipedia's Italian GP page says the same. Bahrain and Saudi Arabia were cancelled earlier in the year. The season still has a long tail: Baku, a rearranged Bahrain in Malaysia on some calendars, Singapore, Austin, Mexico, Sao Paulo, Las Vegas, Qatar, Abu Dhabi.

## What we will not print

A Madrid winner. A pole. A safety car. Come back after Sunday.
""",
)


def main():
    ROOT.mkdir(parents=True, exist_ok=True)
    for slug, body in STORIES:
        path = ROOT / slug
        path.write_text(body, encoding="utf-8")
        print("wrote", slug)
    print("total", len(STORIES))


if __name__ == "__main__":
    main()

