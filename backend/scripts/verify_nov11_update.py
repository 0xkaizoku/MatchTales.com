#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verification script for 11 November 2026 MatchTales daily update."""
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
    "frontend/src/content/matches/bills-at-vikings-mnf-week9-2026.json",
    "frontend/src/content/matches/sao-paulo-gp-interlagos-2026.json",
    "frontend/src/content/matches/wwt-championship-diamante-cabo-2026.json",
    "frontend/src/content/matches/nba-celtics-vs-76ers-george-36-2026.json",
    "frontend/src/content/matches/nba-cavaliers-at-knicks-nov11-2026.json",
    "frontend/src/content/matches/commanders-at-giants-tnf-week10-2026.json",
    "frontend/src/content/matches/uwcl-psg-vs-bayern-munich-md4-2026.json",
    "frontend/src/content/matches/uwcl-juventus-vs-ol-lyonnes-md4-2026.json",
    "frontend/src/content/matches/atp-stockholm-open-2026-musetti-vs-samuel-r16.json",
    "frontend/src/content/matches/dp-world-tour-championship-dubai-2026.json",
    "frontend/src/content/matches/las-vegas-gp-strip-2026.json",
    "frontend/src/content/stories/nba-celtics-123-76ers-101-paul-george-revenge-return-2026.md",
    "frontend/src/content/stories/nfl-week10-tnf-commanders-at-giants-whiteout-rematch-2026.md",
    "frontend/src/content/stories/uwcl-md4-bayern-beat-psg-real-madrid-cruises-2026.md",
    "frontend/src/content/stories/atp-stockholm-open-2026-musetti-rune-advance-turin-draw-next.md",
    "frontend/src/content/stories/dp-world-tour-championship-2026-mcilroy-chacarra-dubai-preview.md",
    "frontend/src/content/stories/f1-sao-paulo-aftermath-verstappen-charge-las-vegas-preview-2026.md",
]

EMOJI_FLAG_RE = re.compile(r"[\U0001F1E6-\U0001F1FF]")

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
    if "`2026-11-11`" not in cl:
        err("AGENTS.md Site clock does not reference 2026-11-11")
    if "\u2014" in cl or "--" in cl:
        err("Disallowed dash in AGENTS.md Site clock line")

# Date checks
with open(os.path.join(ROOT, "frontend/src/data/sports.ts"), "r", encoding="utf-8") as f:
    sports_ts = f.read()
if "SITE_TODAY = '2026-11-11'" not in sports_ts:
    err("sports.ts missing SITE_TODAY = '2026-11-11'")

for rel_story in FILES_TO_CHECK:
    if rel_story.endswith(".md"):
        with open(os.path.join(ROOT, rel_story), "r", encoding="utf-8") as f:
            st = f.read()
        if "pubDate: 2026-11-11" not in st:
            err(f"{rel_story} missing pubDate: 2026-11-11")

# desk.json checks
with open(os.path.join(ROOT, "frontend/src/data/desk.json"), "r", encoding="utf-8") as f:
    desk = json.load(f)

if desk.get("asOf") != "2026-11-11":
    err(f"desk.asOf is {desk.get('asOf')}, expected 2026-11-11")

pl = desk.get("premierLeagueTable", [])
if len(pl) != 10 or pl[0]["team"] != "Arsenal" or pl[0]["pts"] != 27 or pl[1]["team"] != "Brighton" or pl[1]["pts"] != 22 or pl[2]["team"] != "Manchester City" or pl[2]["pts"] != 21:
    err(f"desk.premierLeagueTable top 3 mismatch: {pl[:3]}")

for row in desk.get("f1Drivers", []):
    if not row.get("team"):
        err(f"Missing 'team' in f1Drivers row: {row}")

f1_c = desk.get("f1Constructors", [])
if [c["pts"] for c in f1_c] != [652, 510, 415, 398]:
    err(f"desk.f1Constructors points mismatch: {f1_c}")

nfl_notes = desk.get("nflWeek1", [])
mnf_rows = [n for n in nfl_notes if n.get("date") == "2026-11-09" and "Vikings" in n.get("home", "")]
if not mnf_rows or "Wentz" not in mnf_rows[0]["note"] or "Darnold" in mnf_rows[0]["note"] or "BUF 7-1" not in mnf_rows[0]["note"]:
    err(f"desk.nflWeek1 Nov 9 MNF note not fixed: {mnf_rows}")

tnf_rows = [n for n in nfl_notes if n.get("date") == "2026-11-12" and "Giants" in n.get("home", "")]
if not tnf_rows:
    err("Missing Nov 12 Week 10 TNF row in desk.nflWeek1")

# Verify corrected Nov 9-10 match JSONs
with open(os.path.join(ROOT, "frontend/src/content/matches/bills-at-vikings-mnf-week9-2026.json"), "r", encoding="utf-8") as f:
    bills_txt = f.read()
if "Darnold" in bills_txt or "Kincaid" in bills_txt or "7-2" in bills_txt:
    err("Stale Darnold/Kincaid/7-2 reference remains in bills-at-vikings-mnf-week9-2026.json")

with open(os.path.join(ROOT, "frontend/src/content/matches/wwt-championship-diamante-cabo-2026.json"), "r", encoding="utf-8") as f:
    wwt = json.load(f)
if wwt.get("homeScore") != "-23" or wwt["leaderboard"][2]["name"] != "Michael Kim":
    err("WWT Championship match JSON corrections incomplete")

with open(os.path.join(ROOT, "frontend/src/content/matches/sao-paulo-gp-interlagos-2026.json"), "r", encoding="utf-8") as f:
    sp = json.load(f)
if sp["leaderboard"][0]["score"] != "1:35:23.504" or sp["leaderboard"][1]["score"] != "+14.602s" or sp["leaderboard"][5]["name"] != "Oscar Piastri (McLaren)":
    err("Sao Paulo GP match JSON corrections incomplete")

# Translation checks in stories.ts
from add_nov11_translations import NOV11_STORIES

with open(os.path.join(ROOT, "frontend/src/i18n/stories.ts"), "r", encoding="utf-8") as f:
    stories_ts = f.read()

for slug in NOV11_STORIES:
    if f'"{slug}":' not in stories_ts:
        err(f"Slug {slug} missing in stories.ts")
    for lang in ["fr", "es", "de", "it", "pl", "zh", "ja", "ko", "ar"]:
        title = NOV11_STORIES[slug][lang]["title"]
        if "\u2014" in title or "--" in title:
            err(f"Disallowed dash in stories.ts entry {slug}.{lang}")

# Verify HomePage.astro & LivePage.astro top priority
for view in ["frontend/src/views/HomePage.astro", "frontend/src/views/LivePage.astro"]:
    with open(os.path.join(ROOT, view), "r", encoding="utf-8") as f:
        vt = f.read()
    if "'nba-celtics-vs-76ers-george-36-2026'" not in vt:
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

print("\nALL VERIFICATION CHECKS PASSED CLEANLY (0 errors).")

