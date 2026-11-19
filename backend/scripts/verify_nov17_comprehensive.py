"""Comprehensive verification script for 2026-11-17 MatchTales update."""
import os
import re
import json
import urllib.request

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
FRONTEND = os.path.join(ROOT, "frontend")

errors = []

# 1. Verify AGENTS.md
agents_txt = open(os.path.join(ROOT, "AGENTS.md"), "r", encoding="utf-8").read()
if "2026-11-17" not in agents_txt:
    errors.append("AGENTS.md does not contain 2026-11-17")
# Line 67 contains the literal definition `No Em-dashes (`—`)`
agents_without_rule_definition = agents_txt.replace("(`—`)", "")
if "\u2014" in agents_without_rule_definition:
    errors.append("AGENTS.md contains unexpected em-dash")

# 2. Verify sports.ts
sports_txt = open(os.path.join(FRONTEND, "src", "data", "sports.ts"), "r", encoding="utf-8").read()
if "SITE_TODAY = '2026-11-17'" not in sports_txt:
    errors.append("sports.ts does not have SITE_TODAY = '2026-11-17'")
required_exports = ["sportBySlug", "getSport", "sportOf", "isWorldCup", "initials", "SPORTS", "SPORT_SLUGS"]
for exp in required_exports:
    if f"export function {exp}" not in sports_txt and f"export const {exp}" not in sports_txt and f"export type {exp}" not in sports_txt:
        errors.append(f"sports.ts missing export: {exp}")
if "\u2014" in sports_txt:
    errors.append("sports.ts contains em-dash")
if "--" in sports_txt:
    errors.append("sports.ts contains double-hyphen")

# 3. Verify desk.json
desk_json = json.load(open(os.path.join(FRONTEND, "src", "data", "desk.json"), "r", encoding="utf-8"))
if desk_json.get("asOf") != "2026-11-17":
    errors.append(f"desk.json asOf is {desk_json.get('asOf')}, expected 2026-11-17")

# 4. Verify match JSONs
required_matches = [
    ("chargers-at-ravens-mnf-week10-2026.json", "FINISHED", "20", "23"),
    ("germany-vs-netherlands-nations-league-2026.json", "FINISHED", "5", "0"),
    ("atp-nitto-finals-2026-turin-draw.json", "UPCOMING", None, None),
    ("nba-magic-vs-celtics-nov16-2026.json", "FINISHED", "105", "115"),
    ("rsm-classic-sea-island-preview-2026.json", "UPCOMING", None, None),
    ("las-vegas-gp-strip-2026.json", "UPCOMING", None, None),
]

for fname, status, home_sc, away_sc in required_matches:
    p = os.path.join(FRONTEND, "src", "content", "matches", fname)
    if not os.path.exists(p):
        errors.append(f"Match file missing: {fname}")
        continue
    data = json.load(open(p, "r", encoding="utf-8"))
    raw_txt = open(p, "r", encoding="utf-8").read()
    if "\u2014" in raw_txt:
        errors.append(f"Match file {fname} contains em-dash")
    if "--" in raw_txt:
        errors.append(f"Match file {fname} contains double-hyphen")
    if data.get("status") != status:
        errors.append(f"Match {fname} status is {data.get('status')}, expected {status}")
    if home_sc is not None and str(data.get("homeScore")) != home_sc:
        errors.append(f"Match {fname} homeScore is {data.get('homeScore')}, expected {home_sc}")
    if away_sc is not None and str(data.get("awayScore")) != away_sc:
        errors.append(f"Match {fname} awayScore is {data.get('awayScore')}, expected {away_sc}")
    # Verify required keys
    for req_key in ["slug", "headline", "whyCareScore", "whyCareReason", "teaser", "story", "stakes", "rivalryAngle", "funFacts", "keyPlayers"]:
        if req_key not in data:
            errors.append(f"Match {fname} missing required key: {req_key}")

# 5. Verify 6 new stories
expected_story_slugs = [
    "nations-league-germany-crush-netherlands-5-0-wirtz-brace-2026",
    "nfl-mnf-chargers-edge-ravens-in-harbaugh-bowl-herbert-hampton-2026",
    "nba-magic-fourth-quarter-rally-snaps-celtics-six-game-streak-2026",
    "atp-finals-turin-alcaraz-cruises-zverev-faces-shelton-tuesday-2026",
    "golf-rsm-classic-fedexcup-fall-finale-sea-island-bubble-cards-2026",
    "f1-two-days-las-vegas-strip-shootout-p2-verstappen-norris-2026"
]

for slug in expected_story_slugs:
    p = os.path.join(FRONTEND, "src", "content", "stories", f"{slug}.md")
    if not os.path.exists(p):
        errors.append(f"Story missing: {slug}.md")
        continue
    txt = open(p, "r", encoding="utf-8").read()
    if "\u2014" in txt:
        errors.append(f"Story {slug} contains em-dash")
    parts = txt.split("---")
    if len(parts) < 3:
        errors.append(f"Story {slug} invalid frontmatter structure")
    else:
        body = "---".join(parts[2:])
        fm = parts[1]
        if "--" in body:
            errors.append(f"Story {slug} body contains double-hyphen")
        if "--" in fm:
            errors.append(f"Story {slug} frontmatter contains double-hyphen")
        if "pubDate: 2026-11-17" not in fm:
            errors.append(f"Story {slug} missing pubDate: 2026-11-17")

# 6. Verify translations in stories.ts
stories_ts_txt = open(os.path.join(FRONTEND, "src", "i18n", "stories.ts"), "r", encoding="utf-8").read()
locales_9 = ["fr", "es", "de", "it", "pl", "zh", "ja", "ko", "ar"]

for slug in expected_story_slugs:
    if f'"{slug}":' not in stories_ts_txt:
        errors.append(f"Story translation missing in stories.ts for: {slug}")
        continue
    # Check that all 9 locales exist under this slug
    slug_idx = stories_ts_txt.find(f'"{slug}":')
    # find next slug or end of dict
    next_slug_idx = stories_ts_txt.find('",\n  "', slug_idx + 1)
    if next_slug_idx == -1:
        next_slug_idx = stories_ts_txt.find('};\n', slug_idx)
    slug_block = stories_ts_txt[slug_idx:next_slug_idx] if next_slug_idx != -1 else stories_ts_txt[slug_idx:slug_idx+15000]
    for loc in locales_9:
        if f'"{loc}":' not in slug_block:
            errors.append(f"Missing locale {loc} for story {slug} in stories.ts")

# 7. Verify no em-dash in playground.ts and messages files
for mf in ["playground.ts", "messages.ts", "messages-es.ts", "messages-de.ts", "messages-it.ts", "messages-pl.ts", "messages-zh.ts", "messages-ja.ts", "messages-ko.ts", "messages-ar.ts"]:
    mpath = os.path.join(FRONTEND, "src", "i18n", mf)
    mtxt = open(mpath, "r", encoding="utf-8").read()
    if "\u2014" in mtxt:
        errors.append(f"{mf} contains em-dash")
    if "--" in mtxt:
        errors.append(f"{mf} contains double-hyphen")

# 8. Check image URLs for the 6 stories
images = [
    "https://images.pexels.com/photos/1171084/pexels-photo-1171084.jpeg",
    "https://images.pexels.com/photos/209954/pexels-photo-209954.jpeg",
    "https://images.pexels.com/photos/1752757/pexels-photo-1752757.jpeg",
    "https://images.pexels.com/photos/1618210/pexels-photo-1618210.jpeg",
    "https://images.pexels.com/photos/863988/pexels-photo-863988.jpeg",
    "https://images.pexels.com/photos/627678/pexels-photo-627678.jpeg"
]

print("Checking image URLs...")
for img in images:
    try:
        req = urllib.request.Request(img, headers={"User-Agent": "Mozilla/5.0"})
        resp = urllib.request.urlopen(req, timeout=10)
        if resp.status != 200:
            errors.append(f"Image HTTP status {resp.status}: {img}")
    except Exception as e:
        errors.append(f"Image fetch failed: {img} ({e})")

print(f"Verification complete. Total errors found: {len(errors)}")
if errors:
    for e in errors:
        print(f"  [ERROR] {e}")
    exit(1)
else:
    print("ALL 8 VERIFICATION CHECKS PASSED PERFECTLY!")
