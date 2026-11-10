#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verification script for 10 November 2026 MatchTales daily update."""
import json
import os
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
ERRORS = []

def err(msg):
    print("ERROR:", msg)
    ERRORS.append(msg)

# 1. Em-dash & double-hyphen check
FILES_TO_CHECK = [
    "frontend/src/data/sports.ts",
    "frontend/src/data/desk.json",
    "frontend/src/i18n/playground.ts",
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
    "frontend/src/content/matches/nba-warriors-vs-pelicans-curry-milestone-2026.json",
    "frontend/src/content/matches/atp-paris-masters-2026-alcaraz-vs-shelton-final.json",
    "frontend/src/content/matches/sao-paulo-gp-interlagos-2026.json",
    "frontend/src/content/matches/wwt-championship-diamante-cabo-2026.json",
    "frontend/src/content/matches/arsenal-vs-hull-city-mw10-2026.json",
    "frontend/src/content/stories/nfl-week9-mnf-bills-23-6-vikings-cook-allen-defense-2026.md",
    "frontend/src/content/stories/f1-sao-paulo-gp-2026-norris-wins-mercedes-clinch-constructors.md",
    "frontend/src/content/stories/atp-paris-masters-2026-alcaraz-downs-shelton-ninth-masters.md",
    "frontend/src/content/stories/pga-tour-wwt-championship-2026-final-blades-brown-playoff-win.md",
    "frontend/src/content/stories/pl-mw10-arsenal-1-0-hull-odegaard-six-clear-2026.md",
    "frontend/src/content/stories/nba-warriors-crush-pelicans-138-87-curry-milestone-2026.md",
]

for rel_path in FILES_TO_CHECK:
    full_path = os.path.join(ROOT, rel_path)
    if not os.path.exists(full_path):
        err(f"Missing file: {rel_path}")
        continue
    with open(full_path, "r", encoding="utf-8") as f:
        content = f.read()
    # Strip URL query params which may have hyphens
    clean_content = re.sub(r'https?://\S+', '', content)
    # Check for em-dash or double-hyphen
    if "—" in clean_content:
        err(f"Em-dash found in {rel_path}")
    if "--" in clean_content:
        # Note: markdown frontmatter uses --- as delimiter. We allow '---' on its own line.
        lines = [l for l in clean_content.splitlines() if l.strip() != '---']
        for idx, line in enumerate(lines):
            if "--" in line:
                err(f"Double-hyphen found in {rel_path}:{idx+1}: {line[:80]}")

# Specifically check AGENTS.md line 14 (Site clock line)
with open(os.path.join(ROOT, "AGENTS.md"), "r", encoding="utf-8") as f:
    agents_lines = f.readlines()
clock_line = [l for l in agents_lines if "*   **Site clock:**" in l]
if not clock_line:
    err("Site clock line missing in AGENTS.md")
else:
    cl = clock_line[0]
    if "—" in cl:
        err("Em-dash found in AGENTS.md site clock line")
    if "--" in cl:
        err("Double-hyphen found in AGENTS.md site clock line")


# 2. Date checks
with open(os.path.join(ROOT, "frontend/src/data/sports.ts"), "r", encoding="utf-8") as f:
    sports_content = f.read()
if "SITE_TODAY = '2026-11-10'" not in sports_content:
    err("sports.ts does not have SITE_TODAY = '2026-11-10'")

with open(os.path.join(ROOT, "frontend/src/data/desk.json"), "r", encoding="utf-8") as f:
    desk_json = json.load(f)
if desk_json.get("asOf") != "2026-11-10":
    err("desk.json does not have asOf = '2026-11-10'")

with open(os.path.join(ROOT, "AGENTS.md"), "r", encoding="utf-8") as f:
    agents_txt = f.read()
if "`2026-11-10`" not in agents_txt:
    err("AGENTS.md does not reference `2026-11-10`")

# 3. Translation check in stories.ts
from add_nov10_translations import NOV10_STORIES

with open(os.path.join(ROOT, "frontend/src/i18n/stories.ts"), "r", encoding="utf-8") as f:
    stories_ts = f.read()

for slug in NOV10_STORIES.keys():
    if f'"{slug}":' not in stories_ts:
        err(f"Slug {slug} missing in stories.ts")
    for lang in ["fr", "es", "de", "it", "pl", "zh", "ja", "ko", "ar"]:
        if f'"{lang}":' not in stories_ts:
            err(f"Locale {lang} missing in stories.ts")

# 4. JSON Schema check for matches
MATCH_FILES = [
    "bills-at-vikings-mnf-week9-2026.json",
    "nba-warriors-vs-pelicans-curry-milestone-2026.json",
    "atp-paris-masters-2026-alcaraz-vs-shelton-final.json",
    "sao-paulo-gp-interlagos-2026.json",
    "wwt-championship-diamante-cabo-2026.json",
    "arsenal-vs-hull-city-mw10-2026.json",
]

EMOJI_REGEX = re.compile(r"[\U0001F1E6-\U0001F1FF]{2}")

for mf in MATCH_FILES:
    p = os.path.join(ROOT, "frontend/src/content/matches", mf)
    with open(p, "r", encoding="utf-8") as f:
        m = json.load(f)
    if not isinstance(m.get("whyCareScore"), (int, float)) or m.get("whyCareScore") <= 0:
        err(f"{mf}: invalid whyCareScore")
    if not m.get("headline"):
        err(f"{mf}: missing headline")
    if not m.get("story"):
        err(f"{mf}: missing story")
    if not m.get("sources") or len(m["sources"]) == 0:
        err(f"{mf}: missing sources")
    if not m.get("image") or not m["image"].startswith("https://"):
        err(f"{mf}: invalid image url")
    # Flag checks
    h_flag = m.get("homeFlag", "")
    a_flag = m.get("awayFlag", "")
    if EMOJI_REGEX.search(str(h_flag)) or EMOJI_REGEX.search(str(a_flag)):
        err(f"{mf}: raw emoji flag detected")

if ERRORS:
    print(f"\nVerification FAILED with {len(ERRORS)} errors.")
    exit(1)
else:
    print("\nAll verifications PASSED! 0 em-dashes, full translations, schemas valid, dates matched.")
