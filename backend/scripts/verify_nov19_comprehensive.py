"""Comprehensive verification script for 2026-11-19 MatchTales update."""
import os
import re
import json
import urllib.request

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
FRONTEND = os.path.join(ROOT, "frontend")

errors = []

# 1. Verify AGENTS.md
agents_txt = open(os.path.join(ROOT, "AGENTS.md"), "r", encoding="utf-8").read()
if "2026-11-19" not in agents_txt:
    errors.append("AGENTS.md does not contain 2026-11-19")
agents_without_rule_definition = agents_txt.replace("(`—`)", "")
if "\u2014" in agents_without_rule_definition:
    errors.append("AGENTS.md contains unexpected em-dash")

# 2. Verify sports.ts
sports_txt = open(os.path.join(FRONTEND, "src", "data", "sports.ts"), "r", encoding="utf-8").read()
if "SITE_TODAY = '2026-11-19'" not in sports_txt:
    errors.append("sports.ts does not have SITE_TODAY = '2026-11-19'")
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
if desk_json.get("asOf") != "2026-11-19":
    errors.append(f"desk.json asOf is {desk_json.get('asOf')}, expected 2026-11-19")

# 4. Verify match JSONs
required_matches = [
    ("colts-at-texans-tnf-week11-2026.json", "UPCOMING", None, None),
    ("atp-nitto-finals-2026-turin-draw.json", "UPCOMING", None, None),
    ("las-vegas-gp-strip-2026.json", "UPCOMING", None, None),
    ("rsm-classic-sea-island-preview-2026.json", "LIVE", "-5", "-4"),
    ("nba-heat-vs-bucks-nov18-2026.json", "FINISHED", "137", "130"),
    ("norway-vs-denmark-nations-league-2026.json", "FINISHED", "2", "3"),
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
    for req_key in ["slug", "headline", "whyCareScore", "whyCareReason", "teaser", "story", "stakes", "rivalryAngle", "funFacts", "keyPlayers"]:
        if req_key not in data:
            errors.append(f"Match {fname} missing required key: {req_key}")

# 5. Verify 6 new stories
expected_story_slugs = [
    "atp-finals-turin-shelton-fils-zverev-mcenroe-deciders-2026",
    "nfl-tnf-colts-visit-texans-stroud-richardson-week11-2026",
    "f1-las-vegas-gp-thursday-practice-opens-strip-showdown-2026",
    "golf-rsm-classic-round1-live-sea-island-thompson-bubble-cards-2026",
    "nba-giannis-masterclass-downs-bucks-heat-sixth-straight-2026",
    "nations-league-haaland-fires-norway-past-denmark-3-2-parken-2026"
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
        if "pubDate: 2026-11-19" not in fm:
            errors.append(f"Story {slug} missing pubDate: 2026-11-19")

# 6. Verify translations in stories.ts
stories_ts_txt = open(os.path.join(FRONTEND, "src", "i18n", "stories.ts"), "r", encoding="utf-8").read()
locales_9 = ["fr", "es", "de", "it", "pl", "zh", "ja", "ko", "ar"]

for slug in expected_story_slugs:
    if f'"{slug}":' not in stories_ts_txt:
        errors.append(f"Story translation missing in stories.ts for: {slug}")
        continue
    slug_idx = stories_ts_txt.find(f'"{slug}":')
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
    "https://images.pexels.com/photos/1618210/pexels-photo-1618210.jpeg",
    "https://images.pexels.com/photos/209954/pexels-photo-209954.jpeg",
    "https://images.pexels.com/photos/627678/pexels-photo-627678.jpeg",
    "https://images.pexels.com/photos/863988/pexels-photo-863988.jpeg",
    "https://images.pexels.com/photos/1752757/pexels-photo-1752757.jpeg",
    "https://images.pexels.com/photos/1171084/pexels-photo-1171084.jpeg"
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

# 9. Check raw emojis in new/modified files
emoji_pattern = re.compile(r'[\U0001F1E6-\U0001F1FF]{2}|[\U0001F300-\U0001F9FF]')
targets = [
    os.path.join(FRONTEND, "src", "content", "matches", fname) for fname, _, _, _ in required_matches
] + [
    os.path.join(FRONTEND, "src", "content", "stories", f"{slug}.md") for slug in expected_story_slugs
]
for t in targets:
    if os.path.exists(t):
        txt = open(t, "r", encoding="utf-8").read()
        m = emoji_pattern.search(txt)
        if m:
            errors.append(f"Emoji found in {os.path.basename(t)}: {m.group(0)}")

print(f"Verification complete. Total errors found: {len(errors)}")
if errors:
    for e in errors:
        print(f"  [ERROR] {e}")
    exit(1)
else:
    print("ALL 9 VERIFICATION CHECKS PASSED PERFECTLY!")

