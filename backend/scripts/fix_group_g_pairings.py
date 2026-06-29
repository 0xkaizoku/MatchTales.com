#!/usr/bin/env python3
"""Fix Group G MD3 team pairings and retry failed stories."""
import json
import os
import asyncio
import httpx
from pathlib import Path

import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

ROOT = Path(__file__).resolve().parent.parent.parent
SEED_PATH = ROOT / "frontend" / "src" / "data" / "seed.json"
MATCH_DIR = ROOT / "frontend" / "src" / "content" / "matches"

from dotenv import load_dotenv
load_dotenv(Path(__file__).resolve().parent.parent / ".env")
GEMINI_KEY = os.environ.get("GEMINI_API_KEY", "")

with open(SEED_PATH, 'r', encoding='utf-8') as f:
    seed = json.load(f)

teams_lookup = {t['name']: t for t in seed['teams']}

# Fix Group G MD3 - correct the team assignments to match real world pairings
# Real MD3: Belgium 5-1 New Zealand, Egypt 1-1 Iran
for fx in seed['fixtures']:
    if fx['slug'] == 'belgium-vs-iran-md3':
        fx['home'] = 'Belgium'
        fx['away'] = 'New Zealand'
        fx['homeCode'] = teams_lookup['Belgium']['code']
        fx['awayCode'] = teams_lookup['New Zealand']['code']
        fx['homeFlag'] = teams_lookup['Belgium']['flag']
        fx['awayFlag'] = teams_lookup['New Zealand']['flag']
        fx['homeScore'] = 5
        fx['awayScore'] = 1
        print('Fixed belgium-vs-iran-md3 -> Belgium 5-1 New Zealand')
    elif fx['slug'] == 'egypt-vs-new-zealand-md3':
        fx['home'] = 'Egypt'
        fx['away'] = 'Iran'
        fx['homeCode'] = teams_lookup['Egypt']['code']
        fx['awayCode'] = teams_lookup['Iran']['code']
        fx['homeFlag'] = teams_lookup['Egypt']['flag']
        fx['awayFlag'] = teams_lookup['Iran']['flag']
        fx['homeScore'] = 1
        fx['awayScore'] = 1
        print('Fixed egypt-vs-new-zealand-md3 -> Egypt 1-1 Iran')

# Recalculate standings
groups = {}
for tm in seed['teams']:
    g = tm['group']
    if g not in groups:
        groups[g] = []
    groups[g].append({'name': tm['name'],'code': tm['code'],'flag': tm['flag'],
                      'P':0,'W':0,'D':0,'L':0,'GF':0,'GA':0,'GD':0,'Pts':0})

def find_row(g, name):
    for r in groups.get(g, []):
        if r['name'] == name: return r
    return None

for m in seed['fixtures']:
    if m.get('status') != 'FINISHED': continue
    hs = m.get('homeScore')
    as_ = m.get('awayScore')
    if hs is None or as_ is None: continue
    try: hs, as_ = int(hs), int(as_)
    except: continue
    hr = find_row(m['group'], m['home'])
    ar = find_row(m['group'], m['away'])
    if not hr or not ar: continue
    for r in (hr, ar): r['P'] += 1
    hr['GF'] += hs; hr['GA'] += as_
    ar['GF'] += as_; ar['GA'] += hs
    if hs > as_: hr['W'] += 1; ar['L'] += 1; hr['Pts'] += 3
    elif hs < as_: ar['W'] += 1; hr['L'] += 1; ar['Pts'] += 3
    else: hr['D'] += 1; ar['D'] += 1; hr['Pts'] += 1; ar['Pts'] += 1

for g in groups:
    for r in groups[g]: r['GD'] = r['GF'] - r['GA']
    groups[g].sort(key=lambda r: (r['Pts'], r['GD'], r['GF']), reverse=True)

seed['groups'] = groups
with open(SEED_PATH, 'w', encoding='utf-8') as f:
    json.dump(seed, f, ensure_ascii=False, indent=2)
print('Seed saved with corrected standings!')

print('\nGroup G Final Standings:')
for r in groups['G']:
    print(f"  {r['name']}: {r['Pts']}pts W:{r['W']} D:{r['D']} L:{r['L']} GF:{r['GF']} GA:{r['GA']} GD:{r['GD']:+d}")

# Update match JSON files for corrected fixtures
for fx in seed['fixtures']:
    if fx['slug'] in ('belgium-vs-iran-md3', 'egypt-vs-new-zealand-md3'):
        fpath = MATCH_DIR / (fx['slug'] + '.json')
        if fpath.exists():
            with open(fpath, 'r', encoding='utf-8') as f:
                mdata = json.load(f)
            for k in ('home', 'away', 'homeCode', 'awayCode', 'homeFlag', 'awayFlag',
                      'homeScore', 'awayScore', 'status'):
                mdata[k] = fx.get(k)
            with open(fpath, 'w', encoding='utf-8') as f:
                json.dump(mdata, f, ensure_ascii=False, indent=2)
            print(f'Updated match JSON: {fx["slug"]}')
        else:
            print(f'Match JSON missing: {fx["slug"]}')

print('\nAll Group G MD3 fixes applied!')
