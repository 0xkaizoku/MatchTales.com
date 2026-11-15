"""
apply_nov15_matches.py
Updates and creates match JSON files for 15 Nov 2026.
"""
import json
import os

def run():
    matches_dir = "frontend/src/content/matches"

    # 1. dp-world-tour-championship-dubai-2026.json
    p_golf = os.path.join(matches_dir, "dp-world-tour-championship-dubai-2026.json")
    golf_data = json.load(open(p_golf, "r", encoding="utf-8"))
    golf_data["status"] = "FINISHED"
    golf_data["roundLabel"] = "Final Round"
    golf_data["matchday"] = 4
    golf_data["homeScore"] = "-15 (273)"
    golf_data["awayScore"] = "-10 (278)"
    golf_data["headline"] = "Dubai Finale: Hatton fires 66 to win by 5 at -15; McIlroy seals 8th Race to Dubai"
    golf_data["teaser"] = "Tyrrell Hatton cards a closing 66 to finish 15 under (273) and win the DP World Tour Championship by 5 strokes. Rory McIlroy (67, 278, -10) holds off Eugenio Chacarra by 125 points to capture his eighth Race to Dubai title, equalling Colin Montgomerie."
    golf_data["leaderboard"] = [
        {"pos": 1, "name": "Tyrrell Hatton", "score": "-15", "thru": "F", "today": "-6", "r1": "70", "r2": "69", "r3": "68", "r4": "66", "total": "273"},
        {"pos": 2, "name": "Rory McIlroy", "score": "-10", "thru": "F", "today": "-5", "r1": "69", "r2": "70", "r3": "72", "r4": "67", "total": "278"},
        {"pos": "T3", "name": "Eugenio Chacarra", "score": "-9", "thru": "F", "today": "-4", "r1": "72", "r2": "71", "r3": "68", "r4": "68", "total": "279"},
        {"pos": "T3", "name": "Oliver Lindell", "score": "-9", "thru": "F", "today": "-3", "r1": "71", "r2": "70", "r3": "69", "r4": "69", "total": "279"},
        {"pos": 5, "name": "Victor Perez", "score": "-8", "thru": "F", "today": "E", "r1": "71", "r2": "70", "r3": "67", "r4": "72", "total": "280"},
        {"pos": 6, "name": "Mikael Lindberg", "score": "-7", "thru": "F", "today": "-1", "r1": "71", "r2": "70", "r3": "69", "r4": "71", "total": "281"},
        {"pos": "T7", "name": "Jon Rahm", "score": "-5", "thru": "F", "today": "-2", "r1": "72", "r2": "70", "r3": "71", "r4": "70", "total": "283"}
    ]
    golf_data["sources"] = [
        {"name": "European Tour Official", "url": "https://www.europeantour.com/dpworld-tour/tournaments/dp-world-tour-championship/leaderboard"},
        {"name": "Associated Press", "url": "https://apnews.com/hub/golf"},
        {"name": "The Guardian", "url": "https://www.theguardian.com/sport/golf"}
    ]
    open(p_golf, "w", encoding="utf-8", newline="\n").write(json.dumps(golf_data, indent=2, ensure_ascii=False) + "\n")
    print("Updated golf match JSON.")

    # 2. atp-stockholm-open-2026-fritz-vs-tirante-final.json
    p_tennis_stockholm = os.path.join(matches_dir, "atp-stockholm-open-2026-fritz-vs-tirante-final.json")
    tennis_stockholm = json.load(open(p_tennis_stockholm, "r", encoding="utf-8"))
    tennis_stockholm["status"] = "FINISHED"
    tennis_stockholm["headline"] = "Stockholm Final: Taylor Fritz outlasts Thiago Agustin Tirante 6-2, 4-6, 7-6 (3)"
    tennis_stockholm["teaser"] = "Top seed Taylor Fritz captures his second Stockholm Open crown, surviving a fierce fightback from first-time ATP finalist Thiago Agustin Tirante in a deciding third-set tiebreak."
    tennis_stockholm["homeScore"] = "2"
    tennis_stockholm["awayScore"] = "1"
    tennis_stockholm["tennisSets"] = [
        {"set": 1, "home": "6", "away": "2"},
        {"set": 2, "home": "4", "away": "6"},
        {"set": 3, "home": "7", "away": "6", "tiebreak": "7-3"}
    ]
    open(p_tennis_stockholm, "w", encoding="utf-8", newline="\n").write(json.dumps(tennis_stockholm, indent=2, ensure_ascii=False) + "\n")
    print("Updated Stockholm final tennis match JSON.")

    # 3. atp-nitto-finals-2026-turin-draw.json
    p_turin = os.path.join(matches_dir, "atp-nitto-finals-2026-turin-draw.json")
    turin_data = json.load(open(p_turin, "r", encoding="utf-8"))
    turin_data["status"] = "FINISHED"
    turin_data["headline"] = "Nitto ATP Finals: Zverev sweeps Jodar 6-4, 6-4; Shelton vs Fils tonight in Turin"
    turin_data["teaser"] = "World No. 1 Alexander Zverev opens his Turin campaign with a clinical 6-4, 6-4 victory over Spanish teenager Rafael Jodar in 87 minutes. Ben Shelton meets Arthur Fils in the evening session."
    turin_data["homeScore"] = "2"
    turin_data["awayScore"] = "0"
    turin_data["tennisSets"] = [
        {"set": 1, "home": "6", "away": "4"},
        {"set": 2, "home": "6", "away": "4"}
    ]
    open(p_turin, "w", encoding="utf-8", newline="\n").write(json.dumps(turin_data, indent=2, ensure_ascii=False) + "\n")
    print("Updated Turin ATP match JSON.")

    # 4. spain-vs-england-nations-league-metropolitano-2026.json
    p_soccer = os.path.join(matches_dir, "spain-vs-england-nations-league-metropolitano-2026.json")
    soccer_data = {
        "slug": "spain-vs-england-nations-league-metropolitano-2026",
        "sport": "soccer",
        "competition": "uefa-nations-league",
        "format": "team-match",
        "home": "Spain",
        "away": "England",
        "homeCode": "ESP",
        "awayCode": "ENG",
        "date": "2026-11-15",
        "time": "19:45 GMT",
        "status": "UPCOMING",
        "roundLabel": "Matchday 6",
        "group": "A3",
        "venue": "Riyadh Air Metropolitano, Madrid",
        "city": "Madrid",
        "homeScore": None,
        "awayScore": None,
        "whyCareScore": 9,
        "headline": "Nations League: Spain host England in winner-take-all Group A3 decider in Madrid",
        "teaser": "European champions Spain need only a point at the Metropolitano to lock up first place in Group A3, while Thomas Tuchel's England require an away triumph to claim top seeding.",
        "story": "European champions Spain welcome England to the Riyadh Air Metropolitano in Madrid on Sunday night, 15 November, for the decisive Matchday 6 showdown in UEFA Nations League Group A3.\n\nSpain enter atop the group with 13 points, having won four and drawn one of their five fixtures, including a 2-0 win over Czechia on Thursday. England, revitalized under manager Thomas Tuchel, sit on 12 points following their 2-1 victory over Croatia at Wembley, where Harry Kane converted a decisive penalty on his record-extending 126th cap.\n\nA draw secures first place and seeded quarter-final status for Luis de la Fuente's side, while England must secure a rare away win in Madrid to leapfrog the hosts in front of 68,000 supporters.",
        "whyCareReason": "The rematch of the Euro 2024 final decides top seed in UEFA Nations League Group A3 with global football supremacy on the line.",
        "stakes": "First place in Group A3 earns home advantage in the two-legged quarter-finals in March 2027.",
        "tags": ["soccer", "uefa-nations-league", "spain", "england", "metropolitano", "tuchel", "kane", "yamal"],
        "sources": [
            {"name": "UEFA Official", "url": "https://www.uefa.com/uefanationsleague/match/spain-vs-england-2026/"},
            {"name": "Reuters", "url": "https://www.reuters.com/sports/soccer/spain-england-nations-league-decider-madrid-2026-11-15/"},
            {"name": "The Guardian", "url": "https://www.theguardian.com/football/live/2026/nov/15/spain-v-england-nations-league"}
        ]
    }
    open(p_soccer, "w", encoding="utf-8", newline="\n").write(json.dumps(soccer_data, indent=2, ensure_ascii=False) + "\n")
    print("Created spain-vs-england match JSON.")

    # 5. patriots-vs-lions-munich-week10-2026.json
    p_nfl = os.path.join(matches_dir, "patriots-vs-lions-munich-week10-2026.json")
    nfl_data = {
        "slug": "patriots-vs-lions-munich-week10-2026",
        "sport": "football",
        "competition": "nfl",
        "format": "team-match",
        "home": "New England Patriots",
        "away": "Detroit Lions",
        "homeCode": None,
        "awayCode": None,
        "date": "2026-11-15",
        "time": "9:30 a.m. ET",
        "status": "LIVE",
        "roundLabel": "Week 10 · Munich International Game",
        "group": "NFL",
        "venue": "Allianz Arena, Munich",
        "city": "Munich",
        "homeScore": "3",
        "awayScore": "21",
        "whyCareScore": 8,
        "headline": "NFL Munich Live: Lions lead Patriots 21-3 at half; Drake Maye exits with ankle injury",
        "teaser": "Detroit explodes for three first-half touchdowns at Allianz Arena via St. Brown, TeSlaa, and Gibbs, while New England starter Drake Maye is ruled out after an Aidan Hutchinson sack.",
        "story": "The Detroit Lions surged to a 21-3 halftime lead over the New England Patriots in the NFL Week 10 international contest at Allianz Arena in Munich on Sunday, 15 November.\n\nDan Campbell's offense dominated early proceedings, with Jared Goff finding Amon-Ra St. Brown on a 56-yard touchdown bomb and Isaac TeSlaa on a 12-yard strike before Jahmyr Gibbs plunged in from 5 yards out. New England answered only with Andy Borregales' 33-yard field goal.\n\nThe Patriots suffered a devastating blow when rookie quarterback Drake Maye injured his ankle during an Aidan Hutchinson sack in the opening quarter. Maye was helped to the locker room and ruled out, turning the offense over to backup Tommy DeVito as the second half gets underway.",
        "whyCareReason": "The final European fixture of the 2026 NFL international series features Detroit chasing NFC North supremacy against a reeling Patriots squad.",
        "stakes": "Detroit (7-2) aims to keep pace atop the NFC, while New England fights to salvage its playoff hopes.",
        "tags": ["nfl", "munich", "detroit-lions", "new-england-patriots", "drake-maye", "amon-ra-st-brown", "jahmyr-gibbs"],
        "sources": [
            {"name": "NFL.com", "url": "https://www.nfl.com/games/patriots-at-lions-2026-reg-10"},
            {"name": "FOX Sports", "url": "https://www.foxsports.com/nfl/patriots-vs-lions-game-boxscore-2026-11-15"},
            {"name": "Associated Press", "url": "https://apnews.com/article/patriots-lions-munich-game-2026"}
        ]
    }
    open(p_nfl, "w", encoding="utf-8", newline="\n").write(json.dumps(nfl_data, indent=2, ensure_ascii=False) + "\n")
    print("Created patriots-vs-lions match JSON.")

    # 6. nba-heat-vs-pistons-nov14-2026.json
    p_nba = os.path.join(matches_dir, "nba-heat-vs-pistons-nov14-2026.json")
    nba_data = {
        "slug": "nba-heat-vs-pistons-nov14-2026",
        "sport": "basketball",
        "competition": "nba",
        "format": "team-match",
        "home": "Miami Heat",
        "away": "Detroit Pistons",
        "homeCode": None,
        "awayCode": None,
        "date": "2026-11-14",
        "time": "8:00 PM ET",
        "status": "FINISHED",
        "roundLabel": "Regular Season",
        "group": "NBA",
        "venue": "Kaseya Center, Miami",
        "city": "Miami",
        "homeScore": "137",
        "awayScore": "117",
        "whyCareScore": 7,
        "headline": "NBA: Giannis drops 34 and Klay returns with 26 as Heat pull away from Pistons 137-117",
        "teaser": "Miami puts on a second-half offensive clinic at Kaseya Center as Giannis Antetokounmpo posts 34 points, 14 rebounds, and 8 assists, overpowering Cade Cunningham's 33 points for Detroit.",
        "story": "The Miami Heat delivered an offensive masterpiece on Saturday night, 14 November, pulling away from the Detroit Pistons for a 137-117 victory at Kaseya Center.\n\nGiannis Antetokounmpo paced the Heat with 34 points, 14 rebounds, and 8 assists, shooting 13 of 19 from the field. Sharpshooter Klay Thompson returned after missing two games with stiffness, catching fire from the perimeter to hit 7 three-pointers on his way to 26 points.\n\nDetroit fought courageously behind guard Cade Cunningham, who finished with 33 points and 8 assists, but Miami's bench outscored Detroit's reserves 48-28 to secure the comfortable home victory.",
        "whyCareReason": "Giannis and Klay power a resurgent Miami offense while Cunningham continues his torrid November scoring streak.",
        "stakes": "Miami improves to 8-4 in the Eastern Conference, while Detroit falls to 6-6.",
        "tags": ["nba", "miami-heat", "detroit-pistons", "giannis-antetokounmpo", "klay-thompson", "cade-cunningham"],
        "sources": [
            {"name": "NBA.com", "url": "https://www.nba.com/game/det-vs-mia-20261114/box-score"},
            {"name": "Associated Press", "url": "https://apnews.com/article/heat-pistons-nba-recap-20261114"},
            {"name": "CBS Sports", "url": "https://www.cbssports.com/nba/gametracker/recap/NBA_20261114_DET@MIA/"}
        ]
    }
    open(p_nba, "w", encoding="utf-8", newline="\n").write(json.dumps(nba_data, indent=2, ensure_ascii=False) + "\n")
    print("Created nba-heat-vs-pistons match JSON.")

    # 7. las-vegas-gp-strip-2026.json
    p_f1 = os.path.join(matches_dir, "las-vegas-gp-strip-2026.json")
    f1_data = json.load(open(p_f1, "r", encoding="utf-8"))
    f1_data["headline"] = "Four days to Round 21 Las Vegas: 33 points still split Verstappen (279) to Norris (246)"
    f1_data["teaser"] = "With Kimi Antonelli and Mercedes crowned world champions, the neon-lit 6.201 km Strip circuit hosts an epic fight for second place between Verstappen, Russell, Hamilton, Leclerc, and Norris."
    open(p_f1, "w", encoding="utf-8", newline="\n").write(json.dumps(f1_data, indent=2, ensure_ascii=False) + "\n")
    print("Updated las-vegas-gp match JSON.")

if __name__ == "__main__":
    run()

