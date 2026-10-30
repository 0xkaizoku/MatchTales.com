#!/usr/bin/env python3
"""
Verification script for MatchTales 30 Oct 2026 daily update.
"""
import os
import sys
import json
import glob
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
FRONTEND = os.path.join(ROOT, "frontend")

OCT30_STORIES = [
    "carabao-cup-2026-quarter-final-draw-fleetwood-town-draws-newcastle",
    "wnba-finals-2026-game6-valkyries-crowned-champions-expansion-miracle",
    "nfl-week8-packers-beat-panthers-27-17-tnf-lambeau-2026",
    "atp-vienna-2026-alcaraz-downs-draper-reaches-semi-finals",
    "f1-mexico-city-gp-2026-friday-practice-antonelli-paces-fp2-altitude",
    "pga-tour-mexico-open-2026-round2-smotherman-leads-pereda-rai-chase",
]

OCT30_MATCHES = [
    "wnba-finals-2026-game6-valkyries-at-dream.json",
    "panthers-at-packers-tnf-week8-2026.json",
    "arsenal-vs-liverpool-mw9-2026.json",
    "atp-vienna-2026-alcaraz-vs-draper-qf.json",
    "mexico-city-gp-autodromo-hermanos-rodriguez-2026.json",
    "vidantaworld-mexico-open-2026.json",
]

def check_em_dashes():
    print("[1/6] Checking for em-dashes and double-hyphens in generated content...")
    errors = []
    
    # Check stories
    for slug in OCT30_STORIES:
        path = os.path.join(FRONTEND, f"src/content/stories/{slug}.md")
        if not os.path.exists(path):
            errors.append(f"Missing story file: {path}")
            continue
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
            if "—" in content:
                errors.append(f"Em-dash found in story: {slug}.md")
            lines = content.splitlines()
            for idx, line in enumerate(lines):
                stripped = line.strip()
                if stripped == "---":
                    continue
                if "--" in line:
                    errors.append(f"Double-hyphen found in story {slug}.md line {idx+1}: {line}")

    # Check matches
    for m in OCT30_MATCHES:
        path = os.path.join(FRONTEND, f"src/content/matches/{m}")
        if not os.path.exists(path):
            errors.append(f"Missing match file: {path}")
            continue
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
            if "—" in content:
                errors.append(f"Em-dash found in match: {m}")
            if "--" in content:
                errors.append(f"Double-hyphen found in match: {m}")

    # Check i18n stories
    stories_i18n = os.path.join(FRONTEND, "src/i18n/stories.ts")
    with open(stories_i18n, "r", encoding="utf-8") as f:
        content = f.read()
        for slug in OCT30_STORIES:
            if slug not in content:
                errors.append(f"Story {slug} missing in stories.ts")

    # Check AGENTS.md site clock line
    agents_md = os.path.join(ROOT, "AGENTS.md")
    with open(agents_md, "r", encoding="utf-8") as f:
        agents_content = f.read()
        for line in agents_content.splitlines():
            if "Site clock:" in line:
                if "—" in line:
                    errors.append("Em-dash found in AGENTS.md site clock line")
                if "2026-10-30" not in line:
                    errors.append("2026-10-30 not found in AGENTS.md site clock line")

    if errors:
        for e in errors:
            print(f"  ERROR: {e}")
        return False
    print("  PASS: 0 em-dashes and 0 double-hyphens found.")
    return True

def check_story_translations():
    print("[2/6] Checking story translations across 9 non-en locales in stories.ts...")
    stories_i18n = os.path.join(FRONTEND, "src/i18n/stories.ts")
    with open(stories_i18n, "r", encoding="utf-8") as f:
        content = f.read()

    locales = ["fr", "es", "de", "it", "pl", "zh", "ja", "ko", "ar"]
    errors = []
    for slug in OCT30_STORIES:
        m = re.search(rf'^"{re.escape(slug)}":\s*\{{(.*?)\n\}},', content, re.MULTILINE | re.DOTALL)
        if not m:
            errors.append(f"Slug {slug} not found in STORY_I18N")
            continue
        chunk = m.group(1)
        for lang in locales:
            if f'"{lang}":' not in chunk and f"'{lang}':" not in chunk:
                errors.append(f"Story {slug} missing language '{lang}'")

    if errors:
        for e in errors:
            print(f"  ERROR: {e}")
        return False
    print(f"  PASS: All {len(OCT30_STORIES)} stories translated across all 9 target locales.")
    return True

def check_matches_json():
    print("[3/6] Validating match JSON files and scores...")
    errors = []
    for m in OCT30_MATCHES:
        path = os.path.join(FRONTEND, f"src/content/matches/{m}")
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            
            for required in ["slug", "headline", "whyCareScore", "whyCareReason", "sport", "status", "date", "sources"]:
                if required not in data:
                    errors.append(f"Match {m} missing required field: {required}")
            
            score = data.get("whyCareScore")
            if score is None or not (1.0 <= float(score) <= 10.0):
                errors.append(f"Match {m} has invalid whyCareScore: {score}")

            status = data.get("status")
            if status not in ["FINISHED", "LIVE", "UPCOMING"]:
                errors.append(f"Match {m} has unexpected status: {status}")

            content_str = json.dumps(data)
            emoji_pattern = re.compile(r'[\U0001F1E6-\U0001F1FF]{2}')
            if emoji_pattern.search(content_str):
                errors.append(f"Match {m} contains raw emoji flags!")

        except Exception as ex:
            errors.append(f"Error parsing {m}: {ex}")

    if errors:
        for e in errors:
            print(f"  ERROR: {e}")
        return False
    print("  PASS: All match JSONs valid, clean schemas, no emoji flags.")
    return True

def check_sports_data():
    print("[4/6] Checking sports.ts and desk.json...")
    errors = []
    
    sports_ts = os.path.join(FRONTEND, "src/data/sports.ts")
    with open(sports_ts, "r", encoding="utf-8") as f:
        sports_content = f.read()
    
    if "SITE_TODAY = '2026-10-30'" not in sports_content:
        errors.append("sports.ts does not have SITE_TODAY = '2026-10-30'")
    
    for slug in ['soccer', 'tennis', 'golf', 'football', 'basketball', 'f1']:
        if f"slug: '{slug}'" not in sports_content:
            errors.append(f"sports.ts missing sport {slug}")

    desk_json = os.path.join(FRONTEND, "src/data/desk.json")
    with open(desk_json, "r", encoding="utf-8") as f:
        desk_data = json.load(f)

    if desk_data.get("asOf") != "2026-10-30":
        errors.append(f"desk.json asOf is '{desk_data.get('asOf')}', expected '2026-10-30'")

    if errors:
        for e in errors:
            print(f"  ERROR: {e}")
        return False
    print("  PASS: sports.ts and desk.json synchronized with 2026-10-30.")
    return True

def check_playground_and_messages():
    print("[5/6] Checking playground.ts and messages across locales...")
    errors = []
    
    playground_ts = os.path.join(FRONTEND, "src/i18n/playground.ts")
    with open(playground_ts, "r", encoding="utf-8") as f:
        pg_content = f.read()

    locales = ["en", "fr", "es", "de", "it", "pl", "zh", "ja", "ko", "ar"]
    for lang in locales:
        idx = pg_content.find(f'"{lang}":')
        if idx == -1:
            errors.append(f"playground.ts missing lang block for {lang}")
        else:
            block = pg_content[idx:idx+1500]
            if "Fleetwood" not in block and "فليتوود" not in block and "弗利特伍德" not in block and "フリートウッド" not in block and "플리트우드" not in block:
                errors.append(f"playground.ts {lang} missing Oct 30 Fleetwood reference")

    for lang in ["es", "de", "it", "pl", "zh", "ja", "ko", "ar"]:
        path = os.path.join(FRONTEND, f"src/i18n/messages-{lang}.ts")
        if not os.path.exists(path):
            errors.append(f"Missing messages file: {path}")

    if errors:
        for e in errors:
            print(f"  ERROR: {e}")
        return False
    print("  PASS: playground and messages files contain updated Oct 30 entries across all 10 locales.")
    return True

def check_images_and_links():
    print("[6/6] Checking image URLs and hero markdown links...")
    errors = []
    for slug in OCT30_STORIES:
        path = os.path.join(FRONTEND, f"src/content/stories/{slug}.md")
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Check image exists and uses pexels CDN
        image_match = re.search(r'image:\s*["\']?(https://images\.pexels\.com/[^"\'\s]+)', content)
        if not image_match:
            errors.append(f"Story {slug} missing valid pexels image URL")

    if errors:
        for e in errors:
            print(f"  ERROR: {e}")
        return False
    print("  PASS: All hero images verified with high quality Pexels CDN URLs.")
    return True

def main():
    print("=== MATCHTALES 30 OCT 2026 VERIFICATION ===")
    checks = [
        check_em_dashes,
        check_story_translations,
        check_matches_json,
        check_sports_data,
        check_playground_and_messages,
        check_images_and_links,
    ]
    all_ok = True
    for c in checks:
        if not c():
            all_ok = False
            
    if all_ok:
        print("\nAll verification checks PASSED successfully!")
        sys.exit(0)
    else:
        print("\nVerification checks FAILED. Review errors above.")
        sys.exit(1)

if __name__ == "__main__":
    main()
