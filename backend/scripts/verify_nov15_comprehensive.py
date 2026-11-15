"""Comprehensive verification script for MatchTales 15 Nov 2026 update."""
import os
import sys
import json
import re
import urllib.request

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
FRONTEND = os.path.join(ROOT, "frontend")

errors = []

def err(msg):
    print(f"FAIL: {msg}")
    errors.append(msg)

def ok(msg):
    print(f"OK: {msg}")

# 1. Site clock & desk dates
sports_ts = open(os.path.join(FRONTEND, "src", "data", "sports.ts"), "r", encoding="utf-8").read()
if "SITE_TODAY = '2026-11-15'" in sports_ts:
    ok("sports.ts SITE_TODAY is 2026-11-15")
else:
    err("sports.ts SITE_TODAY is not 2026-11-15")

desk_json = json.load(open(os.path.join(FRONTEND, "src", "data", "desk.json"), "r", encoding="utf-8"))
if desk_json.get("asOf") == "2026-11-15":
    ok("desk.json asOf is 2026-11-15")
else:
    err(f"desk.json asOf is {desk_json.get('asOf')}")

agents_md = open(os.path.join(ROOT, "AGENTS.md"), "r", encoding="utf-8").read()
if "2026-11-15" in agents_md:
    ok("AGENTS.md mentions 2026-11-15")
else:
    err("AGENTS.md does not mention 2026-11-15")

# 2. Stories exist for 15 Nov
expected_stories = [
    "dp-world-tour-dubai-hatton-wins-mcilroy-seals-race-to-dubai-2026",
    "atp-finals-turin-zverev-downs-jodar-fritz-takes-stockholm-2026",
    "nations-league-spain-england-metropolitano-denmark-stun-portugal-2026",
    "nfl-munich-lions-lead-patriots-maye-hurt-allianz-arena-2026",
    "nba-heat-drop-pistons-cavaliers-proctor-triple-double-2026",
    "f1-four-days-las-vegas-strip-p2-battle-antonelli-mercedes-2026"
]

stories_dir = os.path.join(FRONTEND, "src", "content", "stories")
story_urls = {}
for slug in expected_stories:
    path = os.path.join(stories_dir, f"{slug}.md")
    if not os.path.exists(path):
        err(f"Story missing: {path}")
        continue
    content = open(path, "r", encoding="utf-8").read()
    if "pubDate: 2026-11-15" not in content and "pubDate: '2026-11-15'" not in content:
        err(f"Story {slug} pubDate is not 2026-11-15")
    # extract image
    m = re.search(r'image:\s*["\']([^"\']+)["\']', content)
    if m:
        story_urls[slug] = m.group(1)
    else:
        err(f"Story {slug} has no image URL")

ok(f"Found all {len(expected_stories)} Nov 15 stories")

# 3. Check for em-dashes and double hyphens
def check_text_for_dashes(label, text):
    if "\u2014" in text:
        err(f"Em-dash (\\u2014) found in {label}")
    # ignore markdown yaml frontmatter boundaries (---)
    lines = text.split("\n")
    for i, line in enumerate(lines, 1):
        if line.strip() == "---":
            continue
        if "--" in line:
            # Check if it's html comment or code
            if "<!--" in line or "-->" in line:
                continue
            err(f"Double-hyphen (--) found in {label} line {i}: {line[:80]}")

for slug in expected_stories:
    content = open(os.path.join(stories_dir, f"{slug}.md"), "r", encoding="utf-8").read()
    check_text_for_dashes(f"Story {slug}", content)

# Check match JSONs for 15 Nov
expected_matches = [
    "dp-world-tour-championship-dubai-2026.json",
    "atp-stockholm-open-2026-fritz-vs-tirante-final.json",
    "atp-nitto-finals-2026-turin-draw.json",
    "spain-vs-england-nations-league-metropolitano-2026.json",
    "patriots-vs-lions-munich-week10-2026.json",
    "nba-heat-vs-pistons-nov14-2026.json",
    "las-vegas-gp-strip-2026.json"
]

matches_dir = os.path.join(FRONTEND, "src", "content", "matches")
for mf in expected_matches:
    path = os.path.join(matches_dir, mf)
    if not os.path.exists(path):
        err(f"Match file missing: {mf}")
        continue
    content = open(path, "r", encoding="utf-8").read()
    check_text_for_dashes(f"Match {mf}", content)

check_text_for_dashes("sports.ts", sports_ts)
check_text_for_dashes("desk.json", json.dumps(desk_json))

# Check i18n stories
stories_ts = open(os.path.join(FRONTEND, "src", "i18n", "stories.ts"), "r", encoding="utf-8").read()
check_text_for_dashes("stories.ts", stories_ts)

# Check i18n messages
i18n_dir = os.path.join(FRONTEND, "src", "i18n")
for f in os.listdir(i18n_dir):
    if f.startswith("messages") and f.endswith(".ts"):
        txt = open(os.path.join(i18n_dir, f), "r", encoding="utf-8").read()
        check_text_for_dashes(f, txt)

ok("No em-dashes or illegal double-hyphens found across all checked files")

# 4. Check translations for the 6 stories in stories.ts
locales = ["fr", "es", "de", "it", "pl", "zh", "ja", "ko", "ar"]
for slug in expected_stories:
    slug_key = f'"{slug}":'
    if slug_key not in stories_ts and f"'{slug}':" not in stories_ts:
        err(f"stories.ts is missing slug key: {slug}")
        continue
    idx = stories_ts.find(slug_key)
    if idx == -1:
        idx = stories_ts.find(f"'{slug}':")
    next_idx = stories_ts.find('\n  "', idx + len(slug) + 10)
    if next_idx == -1:
        next_idx = len(stories_ts)
    block = stories_ts[idx:next_idx]
    for loc in locales:
        if f'"{loc}":' not in block and f"'{loc}':" not in block:
            err(f"Slug {slug} missing locale {loc} in stories.ts")

ok("All 6 stories have complete translations across all 9 non-en locales in stories.ts")

# 5. Check match statuses and specific rules
pats_lions = json.load(open(os.path.join(matches_dir, "patriots-vs-lions-munich-week10-2026.json"), "r", encoding="utf-8"))
if pats_lions.get("status") != "LIVE":
    err(f"Patriots vs Lions Munich must be LIVE, got {pats_lions.get('status')}")
else:
    ok("Patriots vs Lions Munich is LIVE")

spain_england = json.load(open(os.path.join(matches_dir, "spain-vs-england-nations-league-metropolitano-2026.json"), "r", encoding="utf-8"))
if spain_england.get("status") != "UPCOMING":
    err(f"Spain vs England must be UPCOMING, got {spain_england.get('status')}")
else:
    ok("Spain vs England is UPCOMING")

dubai_golf = json.load(open(os.path.join(matches_dir, "dp-world-tour-championship-dubai-2026.json"), "r", encoding="utf-8"))
if dubai_golf.get("status") not in ("FINISHED", "FINAL"):
    err(f"Dubai golf must be FINISHED or FINAL, got {dubai_golf.get('status')}")
else:
    ok(f"Dubai golf is {dubai_golf.get('status')}")

# Check raw emojis in stories and matches
emoji_pattern = re.compile(r'[\U0001F1E6-\U0001F1FF]{2}') # Flag emojis
for slug in expected_stories:
    content = open(os.path.join(stories_dir, f"{slug}.md"), "r", encoding="utf-8").read()
    if emoji_pattern.search(content):
        err(f"Raw flag emoji found in story {slug}")

for mf in expected_matches:
    content = open(os.path.join(matches_dir, mf), "r", encoding="utf-8").read()
    if emoji_pattern.search(content):
        err(f"Raw flag emoji found in match {mf}")

ok("No raw flag emojis in Nov 15 stories or matches")

# 6. Verify image URLs return HTTP 200
headers = {'User-Agent': 'Mozilla/5.0'}
for slug, url in story_urls.items():
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            if resp.status == 200:
                ok(f"Image for {slug} returned HTTP 200")
            else:
                err(f"Image for {slug} returned HTTP {resp.status}")
    except Exception as e:
        err(f"Image for {slug} failed: {e}")

if errors:
    print(f"\nTotal failures: {len(errors)}")
    sys.exit(1)
else:
    print("\nALL COMPREHENSIVE CHECKS PASSED!")
    sys.exit(0)
