"""
apply_nov15_desk.py
Full automation for MatchTales daily update: Sunday, 15 November 2026.
"""
import os
import re
import json

def update_agents_md():
    path = "AGENTS.md"
    content = open(path, "r", encoding="utf-8").read()
    new_clock = (
        "*   **Site clock:** editorial today is `2026-11-15` in `frontend/src/data/sports.ts` (`SITE_TODAY`). "
        "Soccer: Sunday Spain vs England 19:45 GMT Metropolitano for Group A3; Saturday Nations League Denmark 4-1 Portugal, Sweden 3-2 Bosnia; "
        "Thu UWCL Barcelona 1-1 Arsenal, England 2-1 Croatia (Kane 64 pen on cap 126); PL Arsenal 27, Brighton 22, Man City 21. "
        "Golf: Dubai Finale complete: Hatton wins on -15 (273, 66) by 5 shots; McIlroy (67, -10, 278) seals 8th Race to Dubai title by 125 pts over Chacarra (T3, 279, 68), tying Montgomerie. "
        "Tennis: Turin ATP Finals opens Sunday Zverev d Jodar 6-4, 6-4 in McEnroe Group; Shelton vs Fils tonight; Saturday Stockholm final Fritz d Tirante 6-2, 4-6, 7-6 (3). "
        "Football: Sunday Munich Lions lead Patriots 21-3 in 2nd half (Maye hurt ankle, St. Brown 56-yd TD, Gibbs TD); TNF Commanders 24, Giants 21 (Diggs 32-yd at 0:57). "
        "Basketball: Saturday Heat 137-117 Pistons (Giannis 34, Klay 26), Cavaliers 127-117 Mavericks (Proctor 24/11/10 triple-double); Fri Spurs 123-85 Warriors (11th straight). "
        "Formula 1: Four days to Round 21 Las Vegas (19-21 Nov, 6.201 km Strip), 33 pts separate Verstappen (279) through Norris (246) behind Champion Antonelli (390); "
        "Mercedes 652, Ferrari 510, Red Bull 415, McLaren 398. No Vegas race result."
    )
    content = re.sub(r'\*\s+\*\*Site clock:\*\*.*', new_clock, content)
    open(path, "w", encoding="utf-8", newline="\n").write(content)
    print("AGENTS.md updated.")

def update_sports_ts():
    path = "frontend/src/data/sports.ts"
    content = open(path, "r", encoding="utf-8").read()
    content = re.sub(r"export const SITE_TODAY = '[^']+';", "export const SITE_TODAY = '2026-11-15';", content)

    # Replace sports blocks
    football_repl = (
        "    slug: 'football',\n"
        "    label: 'Football',\n"
        "    short: 'NFL',\n"
        "    href: '/sport/football',\n"
        "    tagline: \"NFL Munich Live: Lions lead Patriots 21-3 at half; Drake Maye exits with ankle injury.\",\n"
        "    liveNow: \"LIVE Munich: Lions 21, Patriots 3 (St. Brown 56-yd TD, Gibbs TD, Borregales 33-yd FG). Maye hurt ankle. 2nd half in progress.\",\n"
        "    accent: 'coral',\n"
        "    hue: '14 86% 60%',\n"
        "    pulse: \"NFL MUNICH LIVE: LIONS LEAD PATRIOTS 21-3 AT HALF; DRAKE MAYE RULED OUT WITH ANKLE INJURY\",\n"
        "    board: 'Open the field',\n"
        "    span: 'hero',"
    )
    content = re.sub(r"slug:\s*'football',[^}]+span:\s*'hero',", football_repl, content, flags=re.DOTALL)

    soccer_repl = (
        "    slug: 'soccer',\n"
        "    label: 'Soccer',\n"
        "    short: 'Soccer',\n"
        "    href: '/sport/soccer',\n"
        "    tagline: \"Spain host England tonight in Madrid (19:45 GMT) for Group A3; Denmark stun Portugal 4-1.\",\n"
        "    liveNow: \"Tonight: Spain vs England, 19:45 GMT Metropolitano. Sat: Denmark 4-1 Portugal; Sweden 3-2 Bosnia. PL: Arsenal 27, Brighton 22, City 21.\",\n"
        "    accent: 'pitch',\n"
        "    hue: '158 42% 22%',\n"
        "    pulse: \"SPAIN VS ENGLAND TONIGHT IN MADRID; DENMARK STUN PORTUGAL 4-1 IN NATIONS LEAGUE\",\n"
        "    board: 'Open the pitch',\n"
        "    span: 'side',"
    )
    content = re.sub(r"slug:\s*'soccer',[^}]+span:\s*'side',", soccer_repl, content, flags=re.DOTALL)

    basketball_repl = (
        "    slug: 'basketball',\n"
        "    label: 'Basketball',\n"
        "    short: 'Hoops',\n"
        "    href: '/sport/basketball',\n"
        "    tagline: \"Giannis 34 leads Heat 137-117 over Pistons; Proctor triple-double powers short-handed Cavs 127-117.\",\n"
        "    liveNow: \"Sat: Heat 137-117 Pistons (Giannis 34, Klay 26, Cade 33); Cavs 127-117 Mavs (Proctor 24/11/10). Fri: Spurs 123-85 Warriors (11 straight).\",\n"
        "    accent: 'coral',\n"
        "    hue: '24 90% 48%',\n"
        "    pulse: \"NBA SATURDAY: HEAT 137-117 PISTONS, GIANNIS 34; PROCTOR TRIPLE-DOUBLE LEADS CAVS OVER MAVS\",\n"
        "    board: 'Open the floor',\n"
        "    span: 'half',"
    )
    content = re.sub(r"slug:\s*'basketball',[^}]+span:\s*'half',", basketball_repl, content, flags=re.DOTALL)

    golf_repl = (
        "    slug: 'golf',\n"
        "    label: 'Golf',\n"
        "    short: 'Golf',\n"
        "    href: '/sport/golf',\n"
        "    tagline: \"Dubai Finale Complete: Tyrrell Hatton fires 66 to win by 5 at -15; Rory McIlroy seals 8th Race to Dubai title.\",\n"
        "    liveNow: \"Dubai Final: 1. Tyrrell Hatton -15 (273, 66); 2. Rory McIlroy -10 (278, 67, Race to Dubai champion); T3. Chacarra -9 (279), Lindell -9. Final.\",\n"
        "    accent: 'lime',\n"
        "    hue: '84 55% 38%',\n"
        "    pulse: \"DUBAI FINALE: HATTON WINS ON 273 (-15); MCILROY (278, -10) SEALS EIGHTH RACE TO DUBAI CROWN\",\n"
        "    board: 'Open the course',\n"
        "    span: 'half',"
    )
    content = re.sub(r"slug:\s*'golf',[^}]+span:\s*'half',", golf_repl, content, flags=re.DOTALL)

    tennis_repl = (
        "    slug: 'tennis',\n"
        "    label: 'Tennis',\n"
        "    short: 'Tennis',\n"
        "    href: '/sport/tennis',\n"
        "    tagline: \"Turin ATP Finals: Zverev sweeps Jodar 6-4, 6-4; Fritz outlasts Tirante in Stockholm final.\",\n"
        "    liveNow: \"Turin Sun: Zverev d Jodar 6-4, 6-4; Shelton vs Fils tonight (20:30 CET). Stockholm Sat Final: Fritz d Tirante 6-2, 4-6, 7-6 (3).\",\n"
        "    accent: 'sky',\n"
        "    hue: '198 88% 45%',\n"
        "    pulse: \"TURIN ATP FINALS OPEN: ZVEREV SWEEPS JODAR 6-4, 6-4; FRITZ WINS STOCKHOLM IN DECIDING TIEBREAK\",\n"
        "    board: 'Open the court',\n"
        "    span: 'half',"
    )
    content = re.sub(r"slug:\s*'tennis',[^}]+span:\s*'half',", tennis_repl, content, flags=re.DOTALL)

    f1_repl = (
        "    slug: 'f1',\n"
        "    label: 'Formula 1',\n"
        "    short: 'F1',\n"
        "    href: '/sport/f1',\n"
        "    tagline: \"Four days to Round 21 Las Vegas: 33 points still split Verstappen to Norris. No Strip race yet.\",\n"
        "    liveNow: \"Drivers P2 race unchanged: Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246 (Antonelli 390; Mercedes 652). Round 21: 19-21 Nov.\",\n"
        "    accent: 'sky',\n"
        "    hue: '210 90% 48%',\n"
        "    pulse: \"FOUR DAYS TO VEGAS: VERSTAPPEN TO NORRIS STILL 33 PTS BEHIND CHAMPION ANTONELLI\",\n"
        "    board: 'Open the grid',\n"
        "    span: 'half',"
    )
    content = re.sub(r"slug:\s*'f1',[^}]+span:\s*'half',", f1_repl, content, flags=re.DOTALL)

    open(path, "w", encoding="utf-8", newline="\n").write(content)
    print("sports.ts updated.")

def update_desk_json():
    path = "frontend/src/data/desk.json"
    data = json.load(open(path, "r", encoding="utf-8"))
    data["asOf"] = "2026-11-15"
    open(path, "w", encoding="utf-8", newline="\n").write(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print("desk.json updated.")

if __name__ == "__main__":
    update_agents_md()
    update_sports_ts()
    update_desk_json()

