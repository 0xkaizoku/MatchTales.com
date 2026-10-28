# -*- coding: utf-8 -*-
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent

# 1. Verify markdown stories
stories = [
    "carabao-cup-2026-fleetwood-town-stun-arsenal-shootout-miracle.md",
    "wnba-finals-2026-game5-valkyries-edge-dream-nba-opening-night-wembanyama.md",
    "nfl-week7-wrap-cowboys-blow-out-eagles-packers-panthers-tnf-2026.md",
    "atp-vienna-2026-alcaraz-subdues-khachanov-zverev-survives-epic-tiebreak.md",
    "f1-mexico-city-gp-2026-preview-antonelli-threshold-youngest-title.md",
    "pga-tour-mexico-open-2026-preview-smotherman-momentum-vidantavallarta.md"
]

print("=== 1. Checking 6 Stories ===")
for s in stories:
    p = ROOT / "frontend" / "src" / "content" / "stories" / s
    assert p.exists(), f"Story missing: {s}"
    text = p.read_text(encoding="utf-8")
    assert "—" not in text, f"Em-dash in {s}"
    # check frontmatter and body without YAML delimiters
    parts = text.split("---")
    assert len(parts) >= 3, f"Bad frontmatter in {s}"
    assert "--" not in parts[1], f"Double-hyphen in frontmatter of {s}"
    assert "--" not in "---".join(parts[2:]), f"Double-hyphen in body of {s}"
    print(f"PASS: {s}")

# 2. Verify matches
matches = [
    "cowboys-at-eagles-mnf-week7-2026.json",
    "wnba-finals-2026-game5-valkyries-vs-dream.json",
    "atp-vienna-2026-alcaraz-vs-khachanov.json",
    "fleetwood-town-vs-arsenal-carabao-cup-2026.json",
    "mexico-city-gp-autodromo-hermanos-rodriguez-2026.json",
    "vidantaworld-mexico-open-2026.json",
    "panthers-at-packers-tnf-week8-2026.json",
    "spurs-vs-kings-nba-opening-night-2026.json",
    "atp-vienna-2026-zverev-vs-landaluce.json"
]

print("\n=== 2. Checking Matches ===")
for m in matches:
    p = ROOT / "frontend" / "src" / "content" / "matches" / m
    assert p.exists(), f"Match missing: {m}"
    with open(p, "r", encoding="utf-8") as f:
        data = json.load(f)
    raw = json.dumps(data, ensure_ascii=False)
    assert "—" not in raw, f"Em-dash in {m}"
    assert "--" not in raw, f"Double-hyphen in {m}"
    # check flags
    for k in ["homeFlag", "awayFlag"]:
        v = data.get(k, "")
        if v:
            # ensure no emoji
            assert all(ord(c) < 128 for c in v), f"Non-ascii flag code in {m}.{k}: {v}"
    # check image
    img = data.get("image", "")
    assert img.startswith("http"), f"Invalid image URL in {m}: {img}"
    print(f"PASS: {m} (status={data.get('status')}, image ok, flags ok)")

# 3. Verify desk.json and sports.ts
print("\n=== 3. Checking desk.json and sports.ts ===")
desk_path = ROOT / "frontend" / "src" / "data" / "desk.json"
with open(desk_path, "r", encoding="utf-8") as f:
    desk = json.load(f)
assert desk["asOf"] == "2026-10-28", f"desk asOf not 2026-10-28: {desk['asOf']}"
assert "—" not in json.dumps(desk, ensure_ascii=False)
assert "--" not in json.dumps(desk, ensure_ascii=False)
print("PASS: desk.json asOf is 2026-10-28 and free of em-dashes")

sports_path = ROOT / "frontend" / "src" / "data" / "sports.ts"
sports_code = sports_path.read_text(encoding="utf-8")
assert "SITE_TODAY = '2026-10-28';" in sports_code, "SITE_TODAY not set to 2026-10-28"
assert "—" not in sports_code
assert "--" not in sports_code
print("PASS: sports.ts SITE_TODAY is 2026-10-28 and free of em-dashes")

# 4. Verify stories.ts injection
print("\n=== 4. Checking stories.ts translations ===")
stories_ts = (ROOT / "frontend" / "src" / "i18n" / "stories.ts").read_text(encoding="utf-8")
for s in stories:
    slug = s.replace(".md", "")
    assert f'"{slug}":' in stories_ts, f"Slug {slug} missing from stories.ts"
print("PASS: All 6 stories present in stories.ts")

print("\nALL VERIFICATIONS PASSED SUCCESSFULLY!")
