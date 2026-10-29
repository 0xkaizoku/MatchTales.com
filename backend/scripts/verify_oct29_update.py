# -*- coding: utf-8 -*-
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent

# 1. Verify markdown stories
stories = [
    "carabao-cup-2026-city-liverpool-advance-quarter-finals-draw.md",
    "wnba-finals-2026-game6-preview-valkyries-title-brink-dream-atlanta.md",
    "nfl-week8-tnf-preview-packers-host-panthers-lambeau-prime-time.md",
    "atp-vienna-2026-alcaraz-sweeps-berrettini-reaches-quarter-finals.md",
    "f1-mexico-city-gp-2026-media-day-antonelli-confirms-car-12-altitude.md",
    "pga-tour-mexico-open-2026-round1-pereda-leads-smotherman-shoots-66.md"
]

print("=== 1. Checking 6 Stories ===")
for s in stories:
    p = ROOT / "frontend" / "src" / "content" / "stories" / s
    assert p.exists(), f"Story missing: {s}"
    text = p.read_text(encoding="utf-8")
    assert "—" not in text, f"Em-dash in {s}"
    parts = text.split("---")
    assert len(parts) >= 3, f"Bad frontmatter in {s}"
    assert "--" not in parts[1], f"Double-hyphen in frontmatter of {s}"
    assert "--" not in "---".join(parts[2:]), f"Double-hyphen in body of {s}"
    print(f"PASS: {s}")

# 2. Verify matches
matches = [
    "man-city-vs-brighton-carabao-cup-2026.json",
    "liverpool-vs-chelsea-carabao-cup-2026.json",
    "wnba-finals-2026-game6-valkyries-at-dream.json",
    "thunder-vs-nuggets-nba-opening-week-2026.json",
    "panthers-at-packers-tnf-week8-2026.json",
    "atp-vienna-2026-alcaraz-vs-berrettini.json",
    "mexico-city-gp-autodromo-hermanos-rodriguez-2026.json",
    "vidantaworld-mexico-open-2026.json"
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
    for k in ["homeFlag", "awayFlag"]:
        v = data.get(k, "")
        if v:
            assert all(ord(c) < 128 for c in v), f"Non-ascii flag code in {m}.{k}: {v}"
    img = data.get("image", "")
    assert img.startswith("http"), f"Invalid image URL in {m}: {img}"
    print(f"PASS: {m} (status={data.get('status')}, image ok, flags ok)")

# 3. Verify desk.json and sports.ts
print("\n=== 3. Checking desk.json and sports.ts ===")
desk_path = ROOT / "frontend" / "src" / "data" / "desk.json"
with open(desk_path, "r", encoding="utf-8") as f:
    desk = json.load(f)
assert desk["asOf"] == "2026-10-29", f"desk asOf not 2026-10-29: {desk['asOf']}"
assert "—" not in json.dumps(desk, ensure_ascii=False)
assert "--" not in json.dumps(desk, ensure_ascii=False)
print("PASS: desk.json asOf is 2026-10-29 and free of em-dashes")

sports_path = ROOT / "frontend" / "src" / "data" / "sports.ts"
sports_code = sports_path.read_text(encoding="utf-8")
assert "SITE_TODAY = '2026-10-29';" in sports_code, "SITE_TODAY not set to 2026-10-29"
assert "—" not in sports_code
assert "--" not in sports_code
print("PASS: sports.ts SITE_TODAY is 2026-10-29 and free of em-dashes")

# 4. Verify stories.ts injection
print("\n=== 4. Checking stories.ts translations ===")
stories_ts = (ROOT / "frontend" / "src" / "i18n" / "stories.ts").read_text(encoding="utf-8")
for s in stories:
    slug = s.replace(".md", "")
    assert f'"{slug}":' in stories_ts, f"Slug {slug} missing from stories.ts"
print("PASS: All 6 stories present in stories.ts")

# 5. Check no em-dashes or double-hyphens in playground.ts and messages files
print("\n=== 5. Checking i18n files for dashes ===")
pg_path = ROOT / "frontend" / "src" / "i18n" / "playground.ts"
pg_text = pg_path.read_text(encoding="utf-8")
assert "—" not in pg_text, "Em-dash in playground.ts"
assert "--" not in pg_text, "Double-hyphen in playground.ts"
print("PASS: playground.ts free of em-dashes and double-hyphens")

msg_files = [ROOT / "frontend" / "src" / "i18n" / "messages.ts"] + list((ROOT / "frontend" / "src" / "i18n").glob("messages-*.ts"))
for mf in msg_files:
    mt = mf.read_text(encoding="utf-8")
    assert "—" not in mt, f"Em-dash in {mf.name}"
    assert "--" not in mt, f"Double-hyphen in {mf.name}"
    print(f"PASS: {mf.name} free of em-dashes and double-hyphens")

print("\nALL VERIFICATIONS PASSED SUCCESSFULLY!")
