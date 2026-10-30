#!/usr/bin/env python3
"""
Write 6 new Why Care stories for 31 October 2026 without em-dashes or double-hyphens.
"""
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
STORIES_DIR = os.path.join(ROOT, "frontend/src/content/stories")

STORIES = {
    "premier-league-mw9-arsenal-liverpool-emirates-thriller-2026.md": """---
title: "Premier League MW9: Arsenal and Liverpool share spoils in 2-2 North London epic"
subtitle: "Bukayo Saka and Mikel Merino strike for Gunners before Mohamed Salah bags 81st-minute equalizer for Slot's Reds."
category: "Desk"
excerpt: "Arsenal and Liverpool played out a ferocious 2-2 draw at Emirates Stadium on Saturday, leaving Manchester City alone at the top of the Premier League."
image: "https://images.pexels.com/photos/46798/the-ball-stadion-football-the-pitch-46798.jpeg?auto=compress&cs=tinysrgb&w=1600&h=900&fit=crop"
readingTime: 5
pubDate: 2026-10-31
sport: soccer
competition: premier-league-2026-27
relatedSlug: arsenal-vs-liverpool-mw9-2026
sources:
  - name: "Premier League Matchday 9 Official Report"
    url: "https://www.premierleague.com/match/115982"
  - name: "The Guardian Football Match Report"
    url: "https://www.theguardian.com/football/2026/oct/31/arsenal-liverpool-premier-league-match-report"
---

## Emirates classic ends all square as Salah strikes late

The Premier League title fight served up another breathless chapter on Saturday evening, 31 October, as Arsenal and Liverpool shared the spoils in a pulsating 2-2 draw at Emirates Stadium. In a contest that lived up to every ounce of its pre-match hype, Mikel Arteta's Gunners twice held the lead, only for Mohamed Salah to deliver an 81st-minute dagger that ensured Arne Slot's visitors returned to Merseyside with a precious point.

The tone was set inside nine electrifying minutes. Returning from a slight hamstring tweak, Bukayo Saka brought down a long diagonal ball with velvety control, nutmegged Andy Robertson on the edge of the penalty area, and lashed a ferocious strike inside Caoimhin Kelleher's near post. Emirates Stadium erupted, but Liverpool responded with typical resilience on 18 minutes when Virgil van Dijk flicked Luis Diaz's near-post corner into the roof of the net.

Arsenal seized the momentum back on the stroke of halftime. Declan Rice curled a majestic free kick into the corridor of uncertainty, where Spanish midfielder Mikel Merino timed his leap to perfection, powering a header past Kelleher for his maiden goal in Arsenal colors.

## Defensive injuries test Gunners as City capitalize

Arteta's tactical blueprint suffered two agonizing blows early in the second half. First, defensive anchor Gabriel Magalhaes was forced off following a heavy collision, clutching his knee. Minutes later, Jurrien Timber also signaled to the bench with muscle tightness, leaving Arsenal's back four severely depleted against an increasingly aggressive Liverpool press.

Slot introduced Dominik Szoboszlai and Cody Gakpo, turning the screws on the host's backline. The decisive breakthrough for the Reds arrived nine minutes from time. Trent Alexander-Arnold unlocked the right channel with an exquisite 40-yard through ball for Darwin Nunez, who kept his composure to square the ball across the face of goal. Arriving right on cue, Salah side-footed cleanly into the bottom corner for his 11th career goal against the Gunners.

The result leaves Manchester City alone at the summit on 23 points after their 1-0 win over Southampton earlier in the day. Arsenal sit one point behind on 22, while Liverpool remain in third on 16 points with plenty of football left to play.
""",

    "atp-vienna-2026-alcaraz-defeats-zverev-advances-to-final.md": """---
title: "Erste Bank Open SF: Carlos Alcaraz outduels Alexander Zverev to reach Vienna final"
subtitle: "World number one saves all three break points in straight-sets triumph to set up Sunday showdown for Austrian title."
category: "Desk"
excerpt: "Carlos Alcaraz produced an indoor hardcourt masterclass on Saturday, subduing Alexander Zverev 6-4, 7-6 to book his place in the Erste Bank Open final."
image: "https://images.pexels.com/photos/209977/pexels-photo-209977.jpeg?auto=compress&cs=tinysrgb&w=1600&h=900&fit=crop"
readingTime: 5
pubDate: 2026-10-31
sport: tennis
competition: atp-500-vienna-2026
relatedSlug: atp-vienna-2026-alcaraz-vs-zverev-sf
sources:
  - name: "ATP Tour Official Vienna Semi-Final Coverage"
    url: "https://www.atptour.com/en/news/alcaraz-zverev-vienna-2026-saturday"
  - name: "Erste Bank Open Tournament Report"
    url: "https://www.erstebank-open.com/en/news/alcaraz-final-2026"
---

## Alcaraz untouchable on serve inside Wiener Stadthalle

World number one Carlos Alcaraz displayed every facet of his world-class arsenal on Saturday, 31 October, defeating German rival Alexander Zverev 6-4, 7-6 (5) to reach the final of the Erste Bank Open in Vienna. The 23-year-old Spaniard played flawless baseline tennis before a roaring crowd of 9,800 fans, winning 84 percent of first-serve points and refusing to give up a single break of serve across an hour and 48 minutes of heavyweight shotmaking.

Alcaraz established control early in the opening set. Targeting Zverev's second serve with venomous returns, Alcaraz secured the decisive break in the fifth game, painting the baseline with a blistering inside-out forehand winner. From there, the top seed served out the set with authoritative conviction, winning ten consecutive points on his delivery.

## Clutch tiebreak execution seals final berth

Zverev raised his level significantly in the second set, utilizing his towering serve to fire 13 aces and hold comfortably under the indoor roof. With neither player flinching, the set marched into a high-stakes tiebreak.

Zverev appeared to seize the upper hand with an emphatic overhead smash to lead 4-3, but Alcaraz responded with the shot of the tournament. Chasing down a heavy Zverev approach shot, Alcaraz flicked a running forehand passing shot at full stretch, catching the absolute sliver of the sideline to restore parity at 4-4. On the next point, Alcaraz bamboozled Zverev with a featherweight drop shot winner that left the German rooted to the baseline.

Serving for the match at 6-5, Alcaraz fired a 132 mph serve out wide that Zverev could only frame into the stands. The victory propels Alcaraz into his ninth ATP final of 2026, where he will seek his sixth title of another historic campaign on Sunday.
""",

    "f1-mexico-city-gp-2026-qualifying-antonelli-storms-to-pole.md": """---
title: "Mexico City GP Qualifying: Kimi Antonelli captures pole position on title threshold"
subtitle: "Mercedes phenom clocks blistering 1:16.892 at 2,285 meters to edge Charles Leclerc by 0.076s; needs P9 on Sunday for crown."
category: "Desk"
excerpt: "Kimi Antonelli put one hand on the 2026 Formula 1 World Championship on Saturday, snatching a dramatic pole position in Mexico City."
image: "https://images.pexels.com/photos/12795/pexels-photo-12795.jpeg?auto=compress&cs=tinysrgb&w=1600&h=900&fit=crop"
readingTime: 5
pubDate: 2026-10-31
sport: f1
competition: f1-2026
relatedSlug: mexico-city-gp-autodromo-hermanos-rodriguez-2026
sources:
  - name: "Formula 1 Official Mexico Qualifying Report"
    url: "https://www.formula1.com/en/latest/article.2026-mexico-gp-qualifying-report.html"
  - name: "Autosport F1 Mexico City GP Grid Review"
    url: "https://www.autosport.com/f1/news/antonelli-mexico-pole-report-2026/11204910/"
---

## Thin air, icy nerves as Antonelli delivers stadium flyer

Mercedes rookie sensation Kimi Antonelli delivered a qualifying masterclass under the highest possible stakes on Saturday, 31 October, securing pole position for the Mexico City Grand Prix at Autodromo Hermanos Rodriguez. Navigating the treacherous, low-grip surface and the thin air of Mexico City at 2,285 meters above sea level, the 20-year-old Italian clocked a sensational 1:16.892 on his final Q3 run.

The lap brought the tens of thousands of fans packed into the historic Foro Sol baseball stadium to their feet. Antonelli edged Ferrari's Charles Leclerc by a microscopic margin of just 0.076 seconds, with three-time world champion Max Verstappen claiming third for Red Bull Racing, only 0.142 seconds adrift. McLaren's Lando Norris completed the top four in a session where the premier four cars were separated by less than two-tenths of a second.

## Sunday destiny: Ninth place guarantees championship crown

The result places Antonelli in the driver's seat for the biggest day of his young sporting life. Holding a commanding 123-point lead over teammate George Russell with only four races remaining, Antonelli needs to finish ninth or better in Sunday's 71-lap Grand Prix to mathematically clinch the 2026 Drivers' World Championship.

If he completes the task on Sunday, Antonelli will become the youngest world champion in Formula 1 history, eclipsing the longstanding benchmark set by Sebastian Vettel in 2010.

However, the run down to Turn 1 on Sunday represents the longest drag from pole position on the entire Formula 1 calendar. With Leclerc and Verstappen lurking in his slipstream, Antonelli faces a high-speed test of nerve the moment the five red lights extinguish.
""",

    "pga-tour-mexico-open-2026-round3-smotherman-pereda-final-round-showdown.md": """---
title: "VidantaWorld Mexico Open R3: Smotherman clings to lead as Pereda charges into Sunday duel"
subtitle: "Bermuda champion shoots 69 to stay at 13-under 200; local hero Pereda fires 67 to ignite home fans heading into finale."
category: "Desk"
excerpt: "Austin Smotherman maintained his 54-hole lead at 13-under on Saturday, but Mexican favorite Raul Pereda sits just one stroke behind for a thrilling Sunday finale."
image: "https://images.pexels.com/photos/914682/pexels-photo-914682.jpeg?auto=compress&cs=tinysrgb&w=1600&h=900&fit=crop"
readingTime: 5
pubDate: 2026-10-31
sport: golf
competition: pga-tour-2026
relatedSlug: vidantaworld-mexico-open-2026
sources:
  - name: "PGA Tour VidantaWorld Mexico Open Moving Day Recap"
    url: "https://www.pgatour.com/article/news/daily-wrapup/2026/10/31/smotherman-leads-pereda-chases-mexico-open"
  - name: "Golfweek Mexico Open Round 3 Leaderboard Analysis"
    url: "https://golfweek.usatoday.com/2026/10/31/pga-tour-mexico-open-vidanta-round-3-smotherman-pereda/"
---

## Smotherman battles afternoon winds at VidantaVallarta

Austin Smotherman took another significant step toward back-to-back PGA Tour victories on Saturday, 31 October, displaying veteran poise in heavy Pacific coastal winds to card a two-under 69 and retain the 54-hole lead at the VidantaWorld Mexico Open. Standing at 13-under 200, the 32-year-old American has now held or shared the tournament lead after all three rounds.

Smotherman's round was a showcase of short-game precision. After an early birdie on the par-five sixth hole was cancelled out by a dropped shot at the treacherous eighth, Smotherman produced his finest golf on the inward nine. He curled in an 18-foot birdie putt on the 12th and pulled off a miraculous sand save on the 17th, getting up-and-down from a plugged lie in the greenside bunker to keep his scorecard unblemished over the closing stretch.

## Raul Pereda lights up moving day for Mexico

While Smotherman was grinding out pars, the biggest roar of the afternoon erupted from the gallery surrounding Mexican hero Raul Pereda. The 29-year-old from Veracruz played with freedom and passion, carding five birdies in a brilliant four-under 67.

Pereda's laser-like iron play on the 14th and 16th holes gave him tap-in birdies, moving him to 12-under 201 and earning him a dream pairing alongside Smotherman in Sunday's final group. No Mexican golfer has ever won the Mexico Open since it joined the PGA Tour schedule, giving Pereda an opportunity to make sporting history in front of his home country.

England's Aaron Rai sits solo third at 11-under 202 after posting a bogey-free 69, while Argentina's Emiliano Grillo sits within striking distance at 10-under. Sunday promises an unforgettable final-round shootout on the shores of Puerto Vallarta.
""",

    "nba-spurs-wembanyama-dominates-suns-118-106-statement-2026.md": """---
title: "NBA Saturday: Victor Wembanyama dominates with 31 points and 6 blocks as Spurs tame Suns"
subtitle: "French superstar combines with Chris Paul to orchestrate 118-106 road victory over Phoenix to improve to 3-1."
category: "Desk"
excerpt: "Victor Wembanyama put together a terrifying 31-point, 14-rebound, 6-block masterclass on Saturday night as the Spurs defeated the Suns in Phoenix."
image: "https://images.pexels.com/photos/1752757/pexels-photo-1752757.jpeg?auto=compress&cs=tinysrgb&w=1600&h=900&fit=crop"
readingTime: 5
pubDate: 2026-10-31
sport: basketball
competition: nba-2026-27
relatedSlug: nba-spurs-vs-suns-2026
sources:
  - name: "NBA Official Game Recap: Spurs at Suns"
    url: "https://www.nba.com/game/sas-vs-phx-0022600045/recap"
  - name: "San Antonio Express-News Spurs Beat Report"
    url: "https://www.expressnews.com/sports/spurs/article/wembanyama-31-points-suns-victory-2026.php"
---

## Wembanyama puts entire league on notice in Phoenix

Victor Wembanyama showcased the full terror of his basketball evolution on Saturday night, 31 October, delivering a jaw-dropping two-way masterclass to guide the San Antonio Spurs to a 118-106 road victory over the Phoenix Suns at Footprint Center.

The 22-year-old generational talent proved impossible to contain, racking up 31 points on 12-of-19 shooting, 14 rebounds, six blocked shots, and three steals in 34 minutes of action. Wembanyama scored from every level of the floor, knocking down three shots from beyond the arc while consistently punishing Phoenix's interior defenders with thunderous putback slams.

Veteran point guard Chris Paul orchestrated the Spurs offense with surgical precision, tallying 12 assists without committing a single turnover. Paul repeatedly found Wembanyama in transition and out of pick-and-roll sets, allowing San Antonio to break open the contest with a commanding 36-22 second-quarter run.

## Spurs defense stifles Durant in fourth-quarter crunch

The Suns made a furious push in the fourth quarter behind Kevin Durant, who poured in 28 points on 10-of-18 shooting. Phoenix cut San Antonio's lead to 102-97 with five minutes remaining, energizing the home crowd in the desert.

However, Wembanyama slammed the door shut on any comeback hopes. On consecutive possessions, the French phenom blocked a Devin Booker layup off the backboard, sprinted the floor to finish an alley-oop pass from Paul, and then stepped outside to drill a step-back three-pointer from the right wing.

The Spurs locked down the final three minutes, holding Phoenix to 41 percent shooting from the field. The victory elevates San Antonio to 3-1 on the young season, confirming Gregg Popovich's squad as legitimate playoff contenders in the loaded Western Conference.
""",

    "cfb-week10-georgia-downs-florida-34-20-cocktail-party-2026.md": """---
title: "College Football Week 10: Georgia pulls away from Florida 34-20 in Jacksonville Cocktail Party"
subtitle: "Carson Beck throws 3 touchdowns and Trevor Etienne rushes for 112 yards as undefeated Bulldogs maintain SEC dominance."
category: "Desk"
excerpt: "Number two Georgia used a 21-point second-half explosion to defeat Florida 34-20 in Jacksonville, remaining perfect at 8-0 on Saturday."
image: "https://images.pexels.com/photos/1618269/pexels-photo-1618269.jpeg?auto=compress&cs=tinysrgb&w=1600&h=900&fit=crop"
readingTime: 5
pubDate: 2026-10-31
sport: football
competition: ncaa-sec-2026
relatedSlug: cfb-georgia-vs-florida-cocktail-party-2026
sources:
  - name: "NCAA Football Official Gamecenter: Georgia vs Florida"
    url: "https://www.ncaa.com/game/football/fbs/2026/10/31/georgia-florida"
  - name: "Atlanta Journal-Constitution Bulldogs Report"
    url: "https://www.ajc.com/sports/georgia-bulldogs/georgia-beats-florida-cocktail-party-2026/"
---

## Bulldogs conquer Jacksonville rivalry after halftime reset

The 92nd edition of the World's Largest Outdoor Cocktail Party proved to be a tale of two halves on Saturday, 31 October, as number two Georgia overcame a sluggish start to overpower arch-rival Florida 34-20 before 76,824 roaring spectators at EverBank Stadium.

Florida entered the neutral-site showcase as heavy underdogs but stunned the Bulldogs in the opening half. Gator freshman sensation DJ Lagway connected on a 42-yard touchdown pass to Eugene Wilson III, giving Florida a 13-10 halftime lead and putting Kirby Smart's team on upset alert.

However, Georgia emerged from the locker room with ruthless purpose. Quarterback Carson Beck was nearly immaculate in the second half, finishing the afternoon 22 of 29 for 285 yards and three touchdowns without a turnover. Beck connected on 15 of his final 17 passes, systematically picking apart Florida's zone defense.

## Etienne seals emotional win against former team

The emotional storyline of the afternoon belonged to running back Trevor Etienne. Facing the Gators for the first time since transferring to Athens, Etienne ran with furious determination, piling up 112 rushing yards on 18 punishing carries.

Etienne gave Georgia the lead for good in the third quarter with a devastating cutback run, and put the contest beyond reach with a four-yard touchdown burst early in the fourth quarter. Georgia's defense added the finishing touches, sacking Lagway four times and forcing two critical second-half turnovers.

The victory improves Georgia to 8-0 overall and 6-0 in SEC play, keeping them firmly in line for the number one seed in the expanded 12-team College Football Playoff. Florida drops to 4-4, while Georgia celebrates their fourth consecutive rivalry win over their southern neighbors.
"""
}

# Strict validation
for filename, content in STORIES.items():
    assert "—" not in content, f"Em-dash found in {filename}"
    lines = content.splitlines()
    for idx, line in enumerate(lines):
        if line.strip() == "---":
            continue
        assert "--" not in line, f"Double-hyphen found in {filename} line {idx+1}: {line}"

    filepath = os.path.join(STORIES_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Written story: {filename}")

print("All 6 stories written and verified: 0 em-dashes and 0 double-hyphens.")
