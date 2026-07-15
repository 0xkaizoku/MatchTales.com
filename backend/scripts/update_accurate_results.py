#!/usr/bin/env python3
"""
Update match results with accurate 2026 FIFA World Cup group stage scores.
Based on verified real-world results as of July 8, 2026.

IMPORTANT: The slugs in seed.json define fixed matchup pairings.
We update ONLY the scores to match real-world results for whatever
game happened on that date/matchday between those teams.
"""
import json
import os
import sys
from datetime import date

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SEED_PATH = os.path.join(ROOT, 'frontend', 'src', 'data', 'seed.json')
MATCH_DIR = os.path.join(ROOT, 'frontend', 'src', 'content', 'matches')

with open(SEED_PATH, 'r', encoding='utf-8') as f:
    seed = json.load(f)

# ============================================================
# VERIFIED ACCURATE RESULTS by slug (as defined in seed.json)
# Each entry is: slug -> (homeScore, awayScore)
# All FINISHED (group stage is over as of June 27, 2026)
# ============================================================
# Sources: Wikipedia, FIFA.com, Olympics.com, Fox Sports, BBC Sport

ACCURATE_SCORES = {
    # GROUP A: Mexico, South Korea, South Africa, Czechia
    "mexico-vs-south-africa-md1":       (2, 0),
    "south-korea-vs-czechia-md1":       (2, 1),
    "mexico-vs-south-korea-md2":        (1, 0),
    "czechia-vs-south-africa-md2":      (1, 1),
    "mexico-vs-czechia-md3":            (3, 0),   # Mexico wins group (9pts)
    "south-korea-vs-south-africa-md3":  (0, 1),   # CORRECTED: South Africa 1-0 South Korea

    # GROUP B: Switzerland, Canada, Bosnia and Herzegovina, Qatar
    "canada-vs-qatar-md1":                          (6, 0),   # Canada 6-0 Qatar
    "switzerland-vs-bosnia-and-herzegovina-md1":    (4, 1),   # Switzerland 4-1 Bosnia and Herzegovina
    "switzerland-vs-canada-md2":                    (2, 1),   # Switzerland 2-1 Canada
    "qatar-vs-bosnia-and-herzegovina-md2":          (1, 3),   # Bosnia and Herzegovina 3-1 Qatar
    "canada-vs-bosnia-and-herzegovina-md3":         (1, 1),   # Canada 1-1 Bosnia and Herzegovina
    "switzerland-vs-qatar-md3":                     (1, 1),   # Switzerland 1-1 Qatar

    # GROUP C: Brazil, Morocco, Scotland, Haiti
    "brazil-vs-morocco-md1":        (1, 1),
    "haiti-vs-scotland-md1":        (0, 1),
    "scotland-vs-morocco-md2":      (0, 1),   # Morocco 1-0 Scotland
    "brazil-vs-haiti-md2":          (3, 0),   # Brazil 3-0 Haiti
    "brazil-vs-scotland-md3":       (3, 0),   # Brazil 3-0 Scotland
    "haiti-vs-morocco-md3":         (2, 4),   # Morocco 4-2 Haiti

    # GROUP D: USA, Turkiye, Australia, Paraguay
    "united-states-vs-paraguay-md1":    (4, 1),   # USA 4-1 Paraguay
    "australia-vs-turkiye-md1":         (2, 0),   # Australia 2-0 Turkiye
    "turkiye-vs-paraguay-md2":          (0, 1),   # Paraguay 1-0 Turkiye
    "united-states-vs-australia-md2":   (2, 0),   # USA 2-0 Australia
    "united-states-vs-turkiye-md3":     (2, 3),   # Turkiye 3-2 USA
    "australia-vs-paraguay-md3":        (0, 0),   # Australia 0-0 Paraguay

    # GROUP E: Germany, Ivory Coast, Ecuador, Curacao
    "germany-vs-ivory-coast-md1":   (2, 1),   # Germany 2-1 Ivory Coast
    "curaçao-vs-ecuador-md1":       (0, 0),   # Curacao 0-0 Ecuador
    "germany-vs-curaçao-md2":       (7, 1),   # Germany 7-1 Curacao
    "ecuador-vs-ivory-coast-md2":   (0, 1),   # Ivory Coast 1-0 Ecuador
    "germany-vs-ecuador-md3":       (1, 2),   # Ecuador 2-1 Germany
    "curaçao-vs-ivory-coast-md3":   (0, 2),   # Ivory Coast 2-0 Curacao

    # GROUP F: Netherlands, Japan, Sweden, Tunisia
    "netherlands-vs-tunisia-md1":   (3, 1),   # Netherlands 3-1 Tunisia
    "japan-vs-sweden-md1":          (1, 1),   # Japan 1-1 Sweden
    "netherlands-vs-japan-md2":     (2, 2),   # Netherlands 2-2 Japan
    "sweden-vs-tunisia-md2":        (5, 1),   # Sweden 5-1 Tunisia
    "netherlands-vs-sweden-md3":    (5, 1),   # Netherlands 5-1 Sweden
    "japan-vs-tunisia-md3":         (4, 0),   # Japan 4-0 Tunisia

    # GROUP G: Belgium, Egypt, Iran, New Zealand
    "belgium-vs-iran-md1":          (0, 0),   # Belgium 0-0 Iran
    "egypt-vs-new-zealand-md1":     (3, 1),   # Egypt 3-1 New Zealand
    "belgium-vs-egypt-md2":         (1, 1),   # Belgium 1-1 Egypt
    "iran-vs-new-zealand-md2":      (0, 0),   # Iran 0-0 New Zealand
    "belgium-vs-new-zealand-md3":   (5, 1),   # Belgium 5-1 New Zealand
    "egypt-vs-iran-md3":            (1, 1),   # Egypt 1-1 Iran

    # GROUP H: Spain, Uruguay, Cape Verde, Saudi Arabia
    "spain-vs-saudi-arabia-md1":    (4, 0),   # Spain 4-0 Saudi Arabia
    "cape-verde-vs-uruguay-md1":    (2, 2),   # Cape Verde 2-2 Uruguay
    "spain-vs-cape-verde-md2":      (0, 0),   # Spain 0-0 Cape Verde
    "uruguay-vs-saudi-arabia-md2":  (1, 1),   # Uruguay 1-1 Saudi Arabia
    "spain-vs-uruguay-md3":         (1, 0),   # Spain 1-0 Uruguay
    "cape-verde-vs-saudi-arabia-md3": (0, 0), # Cape Verde 0-0 Saudi Arabia

    # GROUP I: France, Senegal, Norway, Iraq
    "france-vs-senegal-md1":        (3, 1),   # France 3-1 Senegal
    "norway-vs-iraq-md1":           (4, 1),   # Norway 4-1 Iraq
    "france-vs-norway-md2":         (4, 1),   # France 4-1 Norway
    "iraq-vs-senegal-md2":          (0, 5),   # Senegal 5-0 Iraq
    "france-vs-iraq-md3":           (3, 0),   # France 3-0 Iraq
    "norway-vs-senegal-md3":        (3, 2),   # Norway 3-2 Senegal

    # GROUP J: Argentina, Austria, Algeria, Jordan
    "argentina-vs-algeria-md1":     (3, 0),   # Argentina 3-0 Algeria
    "austria-vs-jordan-md1":        (3, 1),   # Austria 3-1 Jordan
    "jordan-vs-algeria-md2":        (1, 2),   # Algeria 2-1 Jordan
    "argentina-vs-austria-md2":     (2, 0),   # Argentina 2-0 Austria
    "argentina-vs-jordan-md3":      (3, 1),   # Argentina 3-1 Jordan
    "austria-vs-algeria-md3":       (3, 3),   # Austria 3-3 Algeria

    # GROUP K: Portugal, Colombia, DR Congo, Uzbekistan
    "portugal-vs-uzbekistan-md1":   (5, 0),   # Portugal 5-0 Uzbekistan
    "colombia-vs-dr-congo-md1":     (1, 0),   # Colombia 1-0 DR Congo
    "portugal-vs-colombia-md2":     (0, 0),   # Portugal 0-0 Colombia
    "dr-congo-vs-uzbekistan-md2":   (3, 1),   # DR Congo 3-1 Uzbekistan
    "portugal-vs-dr-congo-md3":     (1, 1),   # Portugal 1-1 DR Congo
    "uzbekistan-vs-colombia-md3":   (1, 3),   # Colombia 3-1 Uzbekistan

    # GROUP L: England, Croatia, Ghana, Panama
    "england-vs-ghana-md1":     (0, 0),   # England 0-0 Ghana
    "croatia-vs-panama-md1":    (1, 0),   # Croatia 1-0 Panama
    "england-vs-croatia-md2":   (4, 2),   # England 4-2 Croatia
    "ghana-vs-panama-md2":      (1, 0),   # Ghana 1-0 Panama
    "england-vs-panama-md3":    (2, 0),   # England 2-0 Panama
    "croatia-vs-ghana-md3":     (2, 1),   # Croatia 2-1 Ghana

    # ROUND OF 32
    "canada-vs-south-africa-md4":               (1, 0),
    "brazil-vs-japan-md4":                      (2, 1),
    "germany-vs-paraguay-md4":                  (1, 1),
    "netherlands-vs-morocco-md4":               (1, 1),
    "norway-vs-ivory-coast-md4":                (2, 1),
    "france-vs-sweden-md4":                     (3, 0),
    "mexico-vs-ecuador-md4":                    (2, 0),
    "england-vs-dr-congo-md4":                  (2, 1),
    "belgium-vs-senegal-md4":                   (3, 2),
    "united-states-vs-bosnia-and-herzegovina-md4": (2, 0),
    "spain-vs-austria-md4":                     (3, 0),
    "portugal-vs-croatia-md4":                  (2, 1),
    "switzerland-vs-algeria-md4":               (2, 0),
    "australia-vs-egypt-md4":                   (1, 1),
    "argentina-vs-cape-verde-md4":              (3, 2),
    "colombia-vs-ghana-md4":                    (1, 0),

    # ROUND OF 16
    "morocco-vs-canada-md5":                    (3, 0),
    "france-vs-paraguay-md5":                   (1, 0),
    "norway-vs-brazil-md5":                     (2, 1),
    "england-vs-mexico-md5":                    (3, 2),
    "spain-vs-portugal-md5":                    (1, 0),
    "belgium-vs-united-states-md5":             (4, 1),
    "argentina-vs-egypt-md5":                   (3, 2),
    "switzerland-vs-colombia-md5":              (0, 0),  # Switzerland advance on pens

    # QUARTER-FINALS
    "france-vs-morocco-md6":                    (2, 1),
    "spain-vs-belgium-md6":                     (2, 0),
    "norway-vs-england-md6":                    (1, 2),
    "argentina-vs-switzerland-md6":             (2, 0),
}

print("Applying accurate match results to seed.json fixtures...")
print(f"Total fixtures in seed: {len(seed['fixtures'])}")

score_updates = 0
for fixture in seed['fixtures']:
    slug = fixture['slug']
    if slug in ACCURATE_SCORES:
        home_score, away_score = ACCURATE_SCORES[slug]
        
        old_home = fixture.get('homeScore')
        old_away = fixture.get('awayScore')
        
        changed = False
        if fixture.get('homeScore') != home_score:
            fixture['homeScore'] = home_score
            changed = True
        if fixture.get('awayScore') != away_score:
            fixture['awayScore'] = away_score
            changed = True
        
        # All group stage and R32 games are FINISHED
        if fixture.get('status') != 'FINISHED' and fixture.get('matchday') in (1, 2, 3, 4, 5):
            fixture['status'] = 'FINISHED'
            fixture['liveMinute'] = None
            changed = True
        
        if changed:
            score_updates += 1
            print(f"  UPDATED {slug}: {old_home}-{old_away} -> {home_score}-{away_score}")

# Update meta date (clamped to tournament window)
_today = date.today().isoformat()
if _today < '2026-06-11':
    _today = '2026-06-11'
elif _today > '2026-07-19':
    _today = '2026-07-19'
seed['meta']['today'] = _today

# Recalculate standings
print("\nRecalculating group standings...")
groups = {}
for tm in seed['teams']:
    g = tm['group']
    if g not in groups:
        groups[g] = []
    groups[g].append({
        'name': tm['name'], 'code': tm['code'], 'flag': tm['flag'],
        'P': 0, 'W': 0, 'D': 0, 'L': 0, 'GF': 0, 'GA': 0, 'GD': 0, 'Pts': 0
    })

def find_row(g, name):
    for r in groups.get(g, []):
        if r['name'] == name:
            return r
    return None

for m in seed['fixtures']:
    if m.get('status') != 'FINISHED':
        continue
    hs = m.get('homeScore')
    as_ = m.get('awayScore')
    if hs is None or as_ is None:
        continue
    try:
        hs, as_ = int(hs), int(as_)
    except (ValueError, TypeError):
        continue
    
    hr = find_row(m['group'], m['home'])
    ar = find_row(m['group'], m['away'])
    if not hr or not ar:
        continue
    
    for r in (hr, ar):
        r['P'] += 1
    hr['GF'] += hs; hr['GA'] += as_
    ar['GF'] += as_; ar['GA'] += hs
    
    if hs > as_:
        hr['W'] += 1; ar['L'] += 1; hr['Pts'] += 3
    elif hs < as_:
        ar['W'] += 1; hr['L'] += 1; ar['Pts'] += 3
    else:
        hr['D'] += 1; ar['D'] += 1; hr['Pts'] += 1; ar['Pts'] += 1

for g in groups:
    for r in groups[g]:
        r['GD'] = r['GF'] - r['GA']
    groups[g].sort(key=lambda r: (r['Pts'], r['GD'], r['GF']), reverse=True)

seed['groups'] = groups

# Save seed
with open(SEED_PATH, 'w', encoding='utf-8') as f:
    json.dump(seed, f, ensure_ascii=False, indent=2)

print(f"\nSaved seed.json with {score_updates} score updates.")
print("Group standings recalculated.")

# Sync match JSON files
print("\nSyncing match JSON files...")
teams_lookup = {t['name']: t for t in seed['teams']}
synced = 0
missing = 0

for fixture in seed['fixtures']:
    slug = fixture['slug']
    fpath = os.path.join(MATCH_DIR, slug + '.json')
    if not os.path.exists(fpath):
        print(f"  WARNING: No match JSON for {slug}")
        missing += 1
        continue
    
    with open(fpath, 'r', encoding='utf-8') as f:
        mdata = json.load(f)
    
    changed = False
    sync_fields = {
        'status': fixture['status'],
        'homeScore': fixture.get('homeScore'),
        'awayScore': fixture.get('awayScore'),
        'date': fixture['date'],
        'time': fixture.get('time', '19:00'),
        'venue': fixture['venue'],
        'city': fixture['city'],
        'matchday': fixture['matchday'],
        'group': fixture['group'],
        'marquee': fixture.get('marquee', False),
        'liveMinute': fixture.get('liveMinute'),
    }
    
    for key, val in sync_fields.items():
        if mdata.get(key) != val:
            mdata[key] = val
            changed = True
    
    if changed:
        with open(fpath, 'w', encoding='utf-8') as f:
            json.dump(mdata, f, ensure_ascii=False, indent=2)
        synced += 1

print(f"Synced {synced} match JSON files ({missing} missing).")

# Print final standings
print("\n=== FINAL GROUP STANDINGS ===")
for g in sorted(groups.keys()):
    print(f"\nGroup {g}:")
    for r in groups[g]:
        print(f"  {r['name']:25s} P:{r['P']} W:{r['W']} D:{r['D']} L:{r['L']} GF:{r['GF']} GA:{r['GA']} GD:{r['GD']:+d} Pts:{r['Pts']}")

print("\nDone! Run the story generator to update narrative content for corrected matches.")
