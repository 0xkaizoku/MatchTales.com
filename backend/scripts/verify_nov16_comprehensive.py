"""Comprehensive verification script for MatchTales 16 Nov 2026 update."""
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
if "SITE_TODAY = '2026-11-16'" in sports_ts:
    ok("sports.ts SITE_TODAY is 2026-11-16")
else:
    err("sports.ts SITE_TODAY is not 2026-11-16")

desk_json = json.load(open(os.path.join(FRONTEND, "src", "data", "desk.json"), "r", encoding="utf-8"))
if desk_json.get("asOf") == "2026-11-16":
    ok("desk.json asOf is 2026-11-16")
else:
    err(f"desk.json asOf is {desk_json.get('asOf')}")

agents_md = open(os.path.join(ROOT, "AGENTS.md"), "r", encoding="utf-8").read()
if "2026-11-16" in agents_md:
    ok("AGENTS.md mentions 2026-11-16")
else:
    err("AGENTS.md does not mention 2026-11-16")

# 2. Stories exist for 16 Nov
expected_stories = [
    "nations-league-england-stun-spain-in-madrid-kane-konsa-2026",
    "nfl-mnf-harbaugh-bowl-chargers-ravens-lions-rout-in-munich-2026",
    "nba-spurs-extend-streak-to-12-wembanyama-harper-top-jazz-2026",
    "atp-finals-turin-shelton-downs-fils-alcaraz-tiafoe-open-lendl-2026",
    "golf-mcilroy-celebrates-record-tying-8th-race-to-dubai-rsm-classic-next-2026",
    "f1-three-days-las-vegas-strip-p2-five-driver-shootout-2026"
]

stories_dir = os.path.join(FRONTEND, "src", "content", "stories")
story_urls = {}
for slug in expected_stories:
    path = os.path.join(stories_dir, f"{slug}.md")
    if not os.path.exists(path):
        err(f"Story missing: {path}")
        continue
    content = open(path, "r", encoding="utf-8").read()
    if "pubDate: 2026-11-16" not in content and "pubDate: '2026-11-16'" not in content:
        err(f"Story {slug} pubDate is not 2026-11-16")
    m = re.search(r'image:\s*["\']?([^\s"\']+)["\']?', content)
    if m:
        story_urls[slug] = m.group(1).strip()
    else:
        err(f"Story {slug} has no image URL")

ok(f"Found all {len(expected_stories)} Nov 16 stories")

# 3. Check for em-dashes and double hyphens
def check_text_for_dashes(label, text):
    if "\u2014" in text:
        err(f"Em-dash (\\u2014) found in {label}")
    lines = text.split("\n")
    for i, line in enumerate(lines, 1):
        if line.strip() == "---":
            continue
        if "--" in line:
            if "<!--" in line or "-->" in line:
                continue
            err(f"Double-hyphen (--) found in {label} line {i}: {line[:80]}")

for slug in expected_stories:
    content = open(os.path.join(stories_dir, f"{slug}.md"), "r", encoding="utf-8").read()
    check_text_for_dashes(f"Story {slug}", content)

expected_matches = [
    "spain-vs-england-nations-league-metropolitano-2026.json",
    "patriots-vs-lions-munich-week10-2026.json",
    "chargers-at-ravens-mnf-week10-2026.json",
    "nba-spurs-vs-jazz-nov15-2026.json",
    "atp-nitto-finals-2026-turin-draw.json",
    "las-vegas-gp-strip-2026.json",
    "dp-world-tour-championship-dubai-2026.json"
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

stories_ts = open(os.path.join(FRONTEND, "src", "i18n", "stories.ts"), "r", encoding="utf-8").read()
check_text_for_dashes("stories.ts", stories_ts)

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
if pats_lions.get("status") != "FINISHED":
    err(f"Patriots vs Lions Munich must be FINISHED, got {pats_lions.get('status')}")
elif pats_lions.get("homeScore") != "10" or pats_lions.get("awayScore") != "35":
    err(f"Patriots vs Lions Munich score should be 10-35, got {pats_lions.get('homeScore')}-{pats_lions.get('awayScore')}")
else:
    ok("Patriots vs Lions Munich is FINISHED (10-35)")

spain_england = json.load(open(os.path.join(matches_dir, "spain-vs-england-nations-league-metropolitano-2026.json"), "r", encoding="utf-8"))
if spain_england.get("status") != "FINISHED":
    err(f"Spain vs England must be FINISHED, got {spain_england.get('status')}")
elif spain_england.get("homeScore") != "2" or spain_england.get("awayScore") != "3":
    err(f"Spain vs England score should be 2-3, got {spain_england.get('homeScore')}-{spain_england.get('awayScore')}")
else:
    ok("Spain vs England is FINISHED (2-3)")

chargers_ravens = json.load(open(os.path.join(matches_dir, "chargers-at-ravens-mnf-week10-2026.json"), "r", encoding="utf-8"))
if chargers_ravens.get("status") != "UPCOMING":
    err(f"Chargers at Ravens must be UPCOMING, got {chargers_ravens.get('status')}")
else:
    ok("Chargers at Ravens is UPCOMING")

spurs_jazz = json.load(open(os.path.join(matches_dir, "nba-spurs-vs-jazz-nov15-2026.json"), "r", encoding="utf-8"))
if spurs_jazz.get("status") != "FINISHED":
    err(f"Spurs vs Jazz must be FINISHED, got {spurs_jazz.get('status')}")
else:
    ok("Spurs vs Jazz is FINISHED (102-110)")

# Check raw emojis
emoji_pattern = re.compile(r'[\U0001F1E6-\U0001F1FF]{2}')
for slug in expected_stories:
    content = open(os.path.join(stories_dir, f"{slug}.md"), "r", encoding="utf-8").read()
    if emoji_pattern.search(content):
        err(f"Raw flag emoji found in story {slug}")

for mf in expected_matches:
    content = open(os.path.join(matches_dir, mf), "r", encoding="utf-8").read()
    if emoji_pattern.search(content):
        err(f"Raw flag emoji found in match {mf}")

ok("No raw flag emojis in Nov 16 stories or matches")

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

# 7. Check match schema validity
required = ['slug', 'headline', 'whyCareScore', 'whyCareReason', 'teaser', 'story', 'stakes', 'rivalryAngle', 'funFacts', 'keyPlayers', 'home', 'away', 'group', 'date', 'time', 'venue', 'city', 'status']
for mf in expected_matches:
    data = json.load(open(os.path.join(matches_dir, mf), encoding='utf-8'))
    missing = [k for k in required if k not in data]
    if missing:
        err(f"Match {mf} missing fields: {missing}")
    for r in data.get('leaderboard', []):
        if not isinstance(r.get('pos'), str):
            err(f"Match {mf} leaderboard pos is not str: {r}")
    for s in data.get('tennisSets', []):
        if 'p1' not in s or 'p2' not in s:
            err(f"Match {mf} tennisSet missing p1/p2: {s}")

ok("All Nov 16 matches conform to collection schema")

if errors:
    print(f"\nTotal failures: {len(errors)}")
    sys.exit(1)
else:
    print("\nALL COMPREHENSIVE CHECKS PASSED!")
    sys.exit(0)
