#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verification script for 12 November 2026 MatchTales daily update."""
import json
import os
import re
import sys
import urllib.request

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, os.path.dirname(__file__))

ERRORS = []


def err(msg):
    print("ERROR:", msg)
    ERRORS.append(msg)


FILES_TO_CHECK = [
    "frontend/src/data/sports.ts",
    "frontend/src/data/desk.json",
    "frontend/src/i18n/playground.ts",
    "frontend/src/i18n/names.ts",
    "frontend/src/i18n/messages.ts",
    "frontend/src/i18n/messages-es.ts",
    "frontend/src/i18n/messages-de.ts",
    "frontend/src/i18n/messages-it.ts",
    "frontend/src/i18n/messages-pl.ts",
    "frontend/src/i18n/messages-zh.ts",
    "frontend/src/i18n/messages-ja.ts",
    "frontend/src/i18n/messages-ko.ts",
    "frontend/src/i18n/messages-ar.ts",
    "frontend/src/content/matches/uwcl-juventus-vs-ol-lyonnes-md4-2026.json",
    "frontend/src/content/matches/uwcl-barcelona-vs-arsenal-md4-2026.json",
    "frontend/src/content/matches/england-vs-croatia-nations-league-2026.json",
    "frontend/src/content/matches/nba-cavaliers-at-knicks-nov11-2026.json",
    "frontend/src/content/matches/nba-rockets-vs-warriors-nov11-2026.json",
    "frontend/src/content/matches/commanders-at-giants-tnf-week10-2026.json",
    "frontend/src/content/matches/atp-nitto-finals-2026-turin-draw.json",
    "frontend/src/content/matches/atp-stockholm-open-2026-fritz-vs-rune-qf.json",
    "frontend/src/content/matches/dp-world-tour-championship-dubai-2026.json",
    "frontend/src/content/matches/las-vegas-gp-strip-2026.json",
    "frontend/src/content/stories/uwcl-barcelona-arsenal-camp-nou-ol-lyonnes-6-0-juventus-2026.md",
    "frontend/src/content/stories/nfl-week10-tnf-tonight-daniels-mccarthy-giants-commanders-2026.md",
    "frontend/src/content/stories/nba-harden-32-cavs-knicks-rockets-beat-warriors-curry-injury-2026.md",
    "frontend/src/content/stories/atp-nitto-finals-2026-turin-draw-alcaraz-zverev-fritz-rune-stockholm.md",
    "frontend/src/content/stories/dp-world-tour-championship-2026-luiten-leads-67-mcilroy-69-chacarra-72.md",
    "frontend/src/content/stories/f1-countdown-las-vegas-round-21-five-way-chase-behind-antonelli-2026.md",
]

EMOJI_FLAG_RE = re.compile(r"[\U0001F1E6-\U0001F1FF]")
VALID_FORMATS = {"team-match", "singles", "race", "leaderboard"}

for rel_path in FILES_TO_CHECK:
    full_path = os.path.join(ROOT, rel_path)
    if not os.path.exists(full_path):
        err(f"Missing file: {rel_path}")
        continue
    with open(full_path, "r", encoding="utf-8") as f:
        content = f.read()

    if EMOJI_FLAG_RE.search(content):
        err(f"Emoji flag character found in {rel_path}")

    clean_content = re.sub(r"https?://\S+", "", content)
    if "\u2014" in clean_content:
        err(f"Em-dash found in {rel_path}")
    if "--" in clean_content:
        for idx, line in enumerate(clean_content.splitlines()):
            stripped = line.strip()
            if stripped == "---" or stripped.startswith("//"):
                continue
            if "--" in line:
                err(f"Double-hyphen found in {rel_path}:{idx+1}: {line[:80]}")

# Check AGENTS.md Site clock line
with open(os.path.join(ROOT, "AGENTS.md"), "r", encoding="utf-8") as f:
    agents_lines = f.readlines()
clock_lines = [l for l in agents_lines if "*   **Site clock:**" in l]
if not clock_lines:
    err("Site clock line missing in AGENTS.md")
else:
    cl = clock_lines[0]
    if "`2026-11-12`" not in cl:
        err("AGENTS.md Site clock does not reference 2026-11-12")
    if "\u2014" in cl or "--" in cl:
        err("Disallowed dash in AGENTS.md Site clock line")

# Date checks
with open(os.path.join(ROOT, "frontend/src/data/sports.ts"), "r", encoding="utf-8") as f:
    sports_ts = f.read()
if "SITE_TODAY = '2026-11-12'" not in sports_ts:
    err("sports.ts missing SITE_TODAY = '2026-11-12'")

for rel_story in FILES_TO_CHECK:
    if rel_story.endswith(".md"):
        with open(os.path.join(ROOT, rel_story), "r", encoding="utf-8") as f:
            st = f.read()
        if "pubDate: 2026-11-12" not in st:
            err(f"{rel_story} missing pubDate: 2026-11-12")

# Validate match JSON schema fields & verified facts
for rel in FILES_TO_CHECK:
    if rel.endswith(".json") and "matches" in rel:
        with open(os.path.join(ROOT, rel), "r", encoding="utf-8") as f:
            d = json.load(f)
        if d.get("format") not in VALID_FORMATS:
            err(f"Invalid format in {rel}: {d.get('format')}")
        if not d.get("sources"):
            err(f"Missing sources in {rel}")

with open(os.path.join(ROOT, "frontend/src/content/matches/uwcl-juventus-vs-ol-lyonnes-md4-2026.json"), "r", encoding="utf-8") as f:
    jv = json.load(f)
if jv.get("status") != "FINISHED" or jv.get("homeScore") != 0 or jv.get("awayScore") != 6:
    err("Juventus vs OL Lyonnes score/status mismatch")

with open(os.path.join(ROOT, "frontend/src/content/matches/nba-cavaliers-at-knicks-nov11-2026.json"), "r", encoding="utf-8") as f:
    ck = json.load(f)
if ck.get("status") != "FINISHED" or ck.get("homeScore") != 107 or ck.get("awayScore") != 115:
    err("Cavs at Knicks score/status mismatch")

with open(os.path.join(ROOT, "frontend/src/content/matches/nba-rockets-vs-warriors-nov11-2026.json"), "r", encoding="utf-8") as f:
    rw = json.load(f)
if rw.get("status") != "FINISHED" or rw.get("homeScore") != 115 or rw.get("awayScore") != 108:
    err("Rockets vs Warriors score/status mismatch")

with open(os.path.join(ROOT, "frontend/src/content/matches/dp-world-tour-championship-dubai-2026.json"), "r", encoding="utf-8") as f:
    db = json.load(f)
if db.get("status") != "FINISHED" or db["leaderboard"][0]["name"] != "Joost Luiten" or db["leaderboard"][0]["score"] != "-5 (67)":
    err("Dubai R1 leaderboard mismatch")

with open(os.path.join(ROOT, "frontend/src/content/matches/las-vegas-gp-strip-2026.json"), "r", encoding="utf-8") as f:
    lv = json.load(f)
if lv.get("matchday") != 21:
    err(f"Las Vegas matchday expected 21, got {lv.get('matchday')}")

# desk.json checks
with open(os.path.join(ROOT, "frontend/src/data/desk.json"), "r", encoding="utf-8") as f:
    desk = json.load(f)

if desk.get("asOf") != "2026-11-12":
    err(f"desk.asOf is {desk.get('asOf')}, expected 2026-11-12")

for row in desk.get("f1Drivers", []):
    if not row.get("team"):
        err(f"Missing 'team' in f1Drivers row: {row}")

tnf_rows = [n for n in desk.get("nflWeek1", []) if n.get("date") == "2026-11-12" and "Giants" in n.get("home", "")]
if not tnf_rows or "Jayden Daniels" not in tnf_rows[0]["note"] or "Lucas Patrick" not in tnf_rows[0]["note"]:
    err(f"desk.nflWeek1 Nov 12 TNF injury update missing: {tnf_rows}")

tennis_draws = [x.get("draw") for x in desk.get("usOpenQF", [])]
if "Turin McEnroe Group" not in tennis_draws or "Turin Lendl Group" not in tennis_draws or "Stockholm QF" not in tennis_draws:
    err(f"desk.usOpenQF Turin/Stockholm Nov 12 rows missing: {tennis_draws}")

# Translation checks in stories.ts
from add_nov12_translations import NOV12_STORIES

with open(os.path.join(ROOT, "frontend/src/i18n/stories.ts"), "r", encoding="utf-8") as f:
    stories_ts = f.read()

for slug in NOV12_STORIES:
    if f'"{slug}":' not in stories_ts:
        err(f"Slug {slug} missing in stories.ts")
    for lang in ["fr", "es", "de", "it", "pl", "zh", "ja", "ko", "ar"]:
        title = NOV12_STORIES[slug][lang]["title"]
        if "\u2014" in title or "--" in title:
            err(f"Disallowed dash in stories.ts entry {slug}.{lang}")

# Verify HomePage.astro & LivePage.astro top priority
for view in ["frontend/src/views/HomePage.astro", "frontend/src/views/LivePage.astro"]:
    with open(os.path.join(ROOT, view), "r", encoding="utf-8") as f:
        vt = f.read()
    if "'uwcl-barcelona-vs-arsenal-md4-2026'" not in vt:
        err(f"Top priority slug missing in {view}")

# Verify preview image URLs return HTTP 200
img_urls = set()
for rel in FILES_TO_CHECK:
    if rel.endswith(".json") and "matches" in rel:
        with open(os.path.join(ROOT, rel), "r", encoding="utf-8") as f:
            d = json.load(f)
            if d.get("image"):
                img_urls.add(d["image"])

for url in sorted(img_urls):
    try:
        req = urllib.request.Request(url, method="GET", headers={"User-Agent": "Mozilla/5.0 MatchTalesVerify"})
        with urllib.request.urlopen(req, timeout=20) as r:
            if r.status != 200:
                err(f"Image returned HTTP {r.status}: {url}")
            else:
                print(f"OK 200 {url.split('?')[0]}")
    except Exception as ex:
        err(f"Image fetch failed {url}: {ex}")

if ERRORS:
    print(f"\nFAILED with {len(ERRORS)} error(s).")
    sys.exit(1)

print("\nALL NOV 12 VERIFICATION CHECKS PASSED CLEANLY (0 errors).")

