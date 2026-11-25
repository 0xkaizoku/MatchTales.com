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
    print("\n=== 1. Checking Editorial Dates (2026-11-26) ===")
    
    # AGENTS.md
    agents_path = os.path.join(ROOT, "AGENTS.md")
    with open(agents_path, "r", encoding="utf-8") as f:
        agents_txt = f.read()
    all_ok &= check("AGENTS.md has SITE_TODAY = 2026-11-26", "2026-11-26" in agents_txt, "2026-11-26 not found")
    
    # sports.ts
    sports_path = os.path.join(FRONTEND, "src", "data", "sports.ts")
    with open(sports_path, "r", encoding="utf-8") as f:
        sports_txt = f.read()
    all_ok &= check("sports.ts SITE_TODAY = '2026-11-26'", "SITE_TODAY = '2026-11-26'" in sports_txt, "Date constant mismatch")
    all_ok &= check("sports.ts football updated", "Thanksgiving" in sports_txt and "Lions" in sports_txt)
    all_ok &= check("sports.ts soccer updated", "Real Madrid 5-1 PSV" in sports_txt)
    all_ok &= check("sports.ts f1 updated", "Lusail" in sports_txt and "Verstappen" in sports_txt)
    all_ok &= check("sports.ts tennis updated", "Davis Cup" in sports_txt and "Musetti" in sports_txt)
    all_ok &= check("sports.ts golf updated", "Marco Penge" in sports_txt)
    all_ok &= check("sports.ts basketball updated", "Celtics 131" in sports_txt)

    # desk.json
    desk_path = os.path.join(FRONTEND, "src", "data", "desk.json")
    with open(desk_path, "r", encoding="utf-8") as f:
        desk_data = json.load(f)
    all_ok &= check("desk.json asOf is 2026-11-26", desk_data.get("asOf") == "2026-11-26", str(desk_data.get("asOf")))

    print("\n=== 2. Checking Match JSONs ===")
    match_slugs = [
        ("atp-nitto-finals-2026-turin-draw.json", "FINISHED", "tennis"),
        ("davis-cup-finals-2026-bologna-knockout.json", "LIVE", "tennis"),
        ("las-vegas-gp-strip-2026.json", "FINISHED", "f1"),
        ("qatar-gp-lusail-preview-2026.json", "UPCOMING", "f1"),
        ("man-city-vs-fulham-mw11-2026.json", "FINISHED", "soccer"),
        ("real-madrid-vs-psv-ucl-md5-2026.json", "FINISHED", "soccer"),
        ("rsm-classic-sea-island-preview-2026.json", "FINISHED", "golf"),
        ("bears-at-lions-thanksgiving-week12-2026.json", "UPCOMING", "football"),
        ("nba-celtics-vs-wizards-nov24-2026.json", "FINISHED", "basketball"),
    ]
    matches_dir = os.path.join(FRONTEND, "src", "content", "matches")
    for filename, expected_status, expected_sport in match_slugs:
        p = os.path.join(matches_dir, filename)
        if not os.path.exists(p):
            all_ok &= check(f"Match exists: {filename}", False, "File missing")
            continue
        with open(p, "r", encoding="utf-8") as f:
            content = f.read()
            m = json.loads(content)
        all_ok &= check(f"{filename} status is {expected_status}", m.get("status") == expected_status, m.get("status"))
        all_ok &= check(f"{filename} sport is {expected_sport}", m.get("sport") == expected_sport, m.get("sport"))
        # Check no em-dash or double-hyphen
        all_ok &= check(f"{filename} has no em-dash", "\u2014" not in content, "Em-dash found")
        all_ok &= check(f"{filename} has no double-hyphen", "--" not in content, "Double-hyphen found")

    print("\n=== 3. Checking Markdown Stories ===")
    story_slugs = [
        "nfl-thanksgiving-lions-bears-thanksgiving-clash-week12-2026.md",
        "champions-league-real-madrid-rout-psv-5-1-mbappe-bellingham-2026.md",
        "f1-qatar-gp-lusail-preview-verstappen-vegas-triumph-norris-battle-2026.md",
        "davis-cup-finals-bologna-italy-musetti-alcaraz-turin-glory-2026.md",
        "golf-rsm-classic-penge-breakthrough-playoff-victory-sea-island-2026.md",
        "nba-thanksgiving-holiday-break-celtics-pistons-cup-showdowns-2026.md",
    ]
    stories_dir = os.path.join(FRONTEND, "src", "content", "stories")
    for s_file in story_slugs:
        p = os.path.join(stories_dir, s_file)
        if not os.path.exists(p):
            all_ok &= check(f"Story exists: {s_file}", False, "File missing")
            continue
        with open(p, "r", encoding="utf-8") as f:
            content = f.read()
        all_ok &= check(f"{s_file} pubDate: 2026-11-26", "pubDate: '2026-11-26'" in content or "pubDate: 2026-11-26" in content)
        # Check no em-dash
        all_ok &= check(f"{s_file} no em-dash", "\u2014" not in content, "Em-dash found")
        # Check double-hyphen outside frontmatter
        parts = content.split("---")
        body = "---".join(parts[2:]) if len(parts) >= 3 else content
        all_ok &= check(f"{s_file} no double-hyphen in body", "--" not in body, "Double-hyphen found in body")

    print("\n=== 4. Checking 10-Locale Story Translations ===")
    stories_ts_path = os.path.join(FRONTEND, "src", "i18n", "stories.ts")
    with open(stories_ts_path, "r", encoding="utf-8") as f:
        stories_ts_code = f.read()
    
    locales = ["fr", "es", "de", "it", "pl", "zh", "ja", "ko", "ar"]
    base_slugs = [s.replace(".md", "") for s in story_slugs]
    
    for slug in base_slugs:
        slug_present = f'"{slug}":' in stories_ts_code or f"'{slug}':" in stories_ts_code
        all_ok &= check(f"Story {slug} present in stories.ts", slug_present)
        if slug_present:
            slug_idx = stories_ts_code.find(f'"{slug}":')
            if slug_idx == -1:
                slug_idx = stories_ts_code.find(f"'{slug}':")
            slice_code = stories_ts_code[slug_idx:slug_idx+16000]
            for loc in locales:
                loc_present = f'"{loc}":' in slice_code or f"'{loc}':" in slice_code
                all_ok &= check(f"Translation {loc} present for {slug}", loc_present)

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
                all_ok &= check(f"Image reachable {url.split('/')[-1]}", resp.status == 200, f"Status {resp.status}")
        except Exception as e:
            all_ok &= check(f"Image reachable {url.split('/')[-1]}", False, str(e))

    print("\n=== 6. Checking HomePage and LivePage updates ===")
    home_page = os.path.join(FRONTEND, "src", "views", "HomePage.astro")
    with open(home_page, "r", encoding="utf-8") as f:
        hp_content = f.read()
    all_ok &= check("HomePage features bears-at-lions", "bears-at-lions-thanksgiving-week12-2026" in hp_content)
    all_ok &= check("HomePage features real-madrid", "real-madrid-vs-psv-ucl-md5-2026" in hp_content)

    live_page = os.path.join(FRONTEND, "src", "views", "LivePage.astro")
    with open(live_page, "r", encoding="utf-8") as f:
        lp_content = f.read()
    all_ok &= check("LivePage prioritizes bears-at-lions", "bears-at-lions-thanksgiving-week12-2026" in lp_content)
    all_ok &= check("LivePage prioritizes davis-cup", "davis-cup-finals-2026-bologna-knockout" in lp_content)

    if all_ok:
        print("\nALL VERIFICATIONS PASSED!")
        return 0
    else:
        print("\nSOME VERIFICATIONS FAILED!")
        return 1

if __name__ == "__main__":
    sys.exit(verify_all())
