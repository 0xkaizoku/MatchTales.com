"""
verify_nov26_comprehensive.py
Comprehensive verification script for MatchTales 26 Nov 2026 daily update.
"""
import os
import sys
import json
import re
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FRONTEND = os.path.join(ROOT, "frontend")

def check(name, condition, details=""):
    if condition:
        print(f"  [PASS] {name}")
        return True
    else:
        print(f"  [FAIL] {name}: {details}")
        return False

def verify_all():
    all_ok = True
    print("\n=== 1. Checking Editorial Dates & Accurate Desk Data (2026-11-26) ===")
    
    agents_path = os.path.join(ROOT, "AGENTS.md")
    with open(agents_path, "r", encoding="utf-8") as f:
        agents_txt = f.read()
    all_ok &= check("AGENTS.md has SITE_TODAY = 2026-11-26", "2026-11-26" in agents_txt)
    
    sports_path = os.path.join(FRONTEND, "src", "data", "sports.ts")
    with open(sports_path, "r", encoding="utf-8") as f:
        sports_txt = f.read()
    all_ok &= check("sports.ts SITE_TODAY = '2026-11-26'", "SITE_TODAY = '2026-11-26'" in sports_txt)
    all_ok &= check("sports.ts football updated (8-2 Bears at Lions)", "8-2 Bears at 8-2 Lions" in sports_txt)
    all_ok &= check("sports.ts soccer updated (Real Madrid 5-1 PSV)", "Real Madrid 5-1 PSV" in sports_txt)
    all_ok &= check("sports.ts f1 updated (Lusail standard weekend)", "Lusail" in sports_txt and "Verstappen" in sports_txt and "Sprint" not in sports_txt)
    all_ok &= check("sports.ts tennis updated (Davis Cup & Musetti)", "Davis Cup" in sports_txt and "Musetti" in sports_txt)
    all_ok &= check("sports.ts golf updated (Marco Penge)", "Marco Penge" in sports_txt)
    all_ok &= check("sports.ts basketball updated (Tatum 41 / Flagg 24)", "Tatum 41" in sports_txt and "Flagg" in sports_txt)

    desk_path = os.path.join(FRONTEND, "src", "data", "desk.json")
    with open(desk_path, "r", encoding="utf-8") as f:
        desk_data = json.load(f)
    all_ok &= check("desk.json asOf is 2026-11-26", desk_data.get("asOf") == "2026-11-26")
    for row in desk_data.get("premierLeagueTable", []):
        all_ok &= check(f"PL math {row['team']}", row["gf"] - row["ga"] == row["gd"] and (row["w"]*3 + row["d"] == row["pts"]) and (row["w"] + row["d"] + row["l"] == row["p"]))

    print("\n=== 2. Checking Match JSONs & Zod Schema Constraints ===")
    matches_expected = [
        ("atp-nitto-finals-2026-turin-draw.json", "FINISHED", "tennis", "singles"),
        ("davis-cup-finals-2026-bologna-knockout.json", "LIVE", "tennis", "team-match"),
        ("davis-cup-britain-vs-germany-nov26-2026.json", "UPCOMING", "tennis", "team-match"),
        ("las-vegas-gp-strip-2026.json", "FINISHED", "f1", "race"),
        ("qatar-gp-lusail-preview-2026.json", "UPCOMING", "f1", "race"),
        ("man-city-vs-fulham-mw11-2026.json", "FINISHED", "soccer", "team-match"),
        ("real-madrid-vs-psv-ucl-md5-2026.json", "FINISHED", "soccer", "team-match"),
        ("rsm-classic-sea-island-preview-2026.json", "FINISHED", "golf", "leaderboard"),
        ("colts-at-texans-tnf-week11-2026.json", "FINISHED", "football", "team-match"),
        ("bears-at-lions-thanksgiving-week12-2026.json", "UPCOMING", "football", "team-match"),
        ("chiefs-at-bills-thanksgiving-week12-2026.json", "UPCOMING", "football", "team-match"),
        ("nba-celtics-vs-wizards-nov24-2026.json", "FINISHED", "basketball", "team-match"),
        ("nba-lakers-vs-kings-nov20-2026.json", "FINISHED", "basketball", "team-match"),
    ]
    matches_dir = os.path.join(FRONTEND, "src", "content", "matches")
    for filename, exp_status, exp_sport, exp_format in matches_expected:
        p = os.path.join(matches_dir, filename)
        if not os.path.exists(p):
            all_ok &= check(f"Match exists: {filename}", False, "File missing")
            continue
        raw = open(p, "r", encoding="utf-8").read()
        m = json.loads(raw)
        all_ok &= check(f"{filename} status={exp_status}", m.get("status") == exp_status, m.get("status"))
        all_ok &= check(f"{filename} sport={exp_sport}", m.get("sport") == exp_sport, m.get("sport"))
        all_ok &= check(f"{filename} format={exp_format}", m.get("format") == exp_format, m.get("format"))
        all_ok &= check(f"{filename} has preview image", bool(m.get("image")))
        for lb in m.get("leaderboard", []):
            ok_lb = isinstance(lb.get("pos"), str) and isinstance(lb.get("name"), str) and isinstance(lb.get("score"), str) and isinstance(lb.get("note", ""), str)
            all_ok &= check(f"{filename} valid leaderboardRow", ok_lb, str(lb))
        all_ok &= check(f"{filename} no em-dash or double-hyphen", "\u2014" not in raw and "--" not in raw)

    print("\n=== 3. Checking Markdown Stories ===")
    story_files = [
        ("nfl-thanksgiving-lions-bears-thanksgiving-clash-week12-2026.md", "bears-at-lions-thanksgiving-week12-2026"),
        ("champions-league-real-madrid-rout-psv-5-1-mbappe-bellingham-2026.md", "real-madrid-vs-psv-ucl-md5-2026"),
        ("f1-qatar-gp-lusail-preview-verstappen-vegas-triumph-norris-battle-2026.md", "qatar-gp-lusail-preview-2026"),
        ("davis-cup-finals-bologna-italy-musetti-alcaraz-turin-glory-2026.md", "davis-cup-finals-2026-bologna-knockout"),
        ("golf-rsm-classic-penge-breakthrough-playoff-victory-sea-island-2026.md", "rsm-classic-sea-island-preview-2026"),
        ("nba-thanksgiving-holiday-break-celtics-pistons-cup-showdowns-2026.md", "nba-celtics-vs-wizards-nov24-2026"),
    ]
    stories_dir = os.path.join(FRONTEND, "src", "content", "stories")
    for s_file, rel_slug in story_files:
        p = os.path.join(stories_dir, s_file)
        if not os.path.exists(p):
            all_ok &= check(f"Story exists: {s_file}", False, "File missing")
            continue
        content = open(p, "r", encoding="utf-8").read()
        all_ok &= check(f"{s_file} pubDate: 2026-11-26", "pubDate: 2026-11-26" in content or "pubDate: '2026-11-26'" in content)
        all_ok &= check(f"{s_file} relatedSlug {rel_slug} exists", os.path.exists(os.path.join(matches_dir, rel_slug + ".json")))
        parts = content.split("---")
        body = "---".join(parts[2:]) if len(parts) >= 3 else content
        all_ok &= check(f"{s_file} no em-dash or body double-hyphen", "\u2014" not in content and "--" not in body)

    print("\n=== 4. Checking 10-Locale Story & UI Translations ===")
    stories_ts_code = open(os.path.join(FRONTEND, "src", "i18n", "stories.ts"), "r", encoding="utf-8").read()
    locales = ["fr", "es", "de", "it", "pl", "zh", "ja", "ko", "ar"]
    for s_file, _ in story_files:
        slug = s_file.replace(".md", "")
        idx = stories_ts_code.find(f'"{slug}":')
        all_ok &= check(f"Story {slug} in stories.ts", idx != -1)
        if idx != -1:
            block = stories_ts_code[idx:idx+18000]
            all_ok &= check(f"{slug} no 8-3 typo across locales", "8-3" not in block)
            for loc in locales:
                all_ok &= check(f"Translation {loc} present for {slug}", f'"{loc}":' in block)

    for fn in ["playground.ts", "messages.ts"] + [f"messages-{loc}.ts" for loc in locales if loc != "fr"]:
        txt = open(os.path.join(FRONTEND, "src", "i18n", fn), "r", encoding="utf-8").read()
        all_ok &= check(f"{fn} no em-dash", "\u2014" not in txt)
        all_ok &= check(f"{fn} no double-hyphen", "--" not in txt)
        all_ok &= check(f"{fn} no 8-3 Bears/Lions error", "8-3" not in txt and "8승 3패" not in txt and "8胜3负" not in txt)

    print("\n=== 5. Checking Pexels Image URLs ===")
    pexels_urls = [
        "https://images.pexels.com/photos/209954/pexels-photo-209954.jpeg",
        "https://images.pexels.com/photos/1171084/pexels-photo-1171084.jpeg",
        "https://images.pexels.com/photos/627678/pexels-photo-627678.jpeg",
        "https://images.pexels.com/photos/1618210/pexels-photo-1618210.jpeg",
        "https://images.pexels.com/photos/863988/pexels-photo-863988.jpeg",
        "https://images.pexels.com/photos/1752757/pexels-photo-1752757.jpeg",
    ]
    for url in pexels_urls:
        try:
            req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=10) as resp:
                all_ok &= check(f"Image reachable {url.split('/')[-1]}", resp.status == 200)
        except Exception as e:
            all_ok &= check(f"Image reachable {url.split('/')[-1]}", False, str(e))

    if all_ok:
        print("\nALL VERIFICATIONS PASSED!")
        return 0
    else:
        print("\nSOME VERIFICATIONS FAILED!")
        return 1

if __name__ == "__main__":
    sys.exit(verify_all())
