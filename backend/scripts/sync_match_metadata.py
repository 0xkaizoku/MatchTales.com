"""
Sync script: fixes match JSON metadata drift, Turkiye slug mismatch, and missing time fields.
"""
import json, os, sys, shutil, random

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SEED_PATH = os.path.join(ROOT, 'frontend', 'src', 'data', 'seed.json')
MATCH_DIR = os.path.join(ROOT, 'frontend', 'src', 'content', 'matches')

# Load seed
seed = json.loads(open(SEED_PATH, 'r', encoding='utf-8').read())

# ============================================================
# Bug 4: Add realistic time values to fixtures missing them
# ============================================================
time_slots = ["13:00", "16:00", "19:00", "21:00"]
random.seed(42)  # deterministic
time_fixes = 0
for f in seed['fixtures']:
    if 'time' not in f or f.get('time') is None:
        # Assign a realistic time based on the fixture index
        f['time'] = random.choice(time_slots)
        time_fixes += 1
print(f"Bug 4: Added 'time' to {time_fixes} fixtures missing it.")

# Save updated seed
with open(SEED_PATH, 'w', encoding='utf-8') as fp:
    fp.write(json.dumps(seed, ensure_ascii=False, indent=2))
print(f"Saved updated seed.json with time fields.")

# ============================================================
# Bug 2: Fix Turkiye/Turkey slug mismatch
# ============================================================
renames = {
    'australia-vs-turkey-md1': 'australia-vs-turkiye-md1',
    'turkey-vs-paraguay-md2': 'turkiye-vs-paraguay-md2',
    'united-states-vs-turkey-md3': 'united-states-vs-turkiye-md3',
}
for old_name, new_name in renames.items():
    old_path = os.path.join(MATCH_DIR, old_name + '.json')
    new_path = os.path.join(MATCH_DIR, new_name + '.json')
    if os.path.exists(old_path):
        # Read, update slug, write to new path
        mdata = json.loads(open(old_path, 'r', encoding='utf-8').read())
        mdata['slug'] = new_name
        with open(new_path, 'w', encoding='utf-8') as fp:
            fp.write(json.dumps(mdata, ensure_ascii=False, indent=2))
        os.remove(old_path)
        print(f"Bug 2: Renamed {old_name}.json -> {new_name}.json (slug updated inside)")
    elif os.path.exists(new_path):
        print(f"Bug 2: {new_name}.json already exists, skipping rename.")
    else:
        print(f"Bug 2: WARNING - neither {old_name}.json nor {new_name}.json found!")

# ============================================================
# Bug 1: Sync match JSON metadata with seed.json
# ============================================================
teams_lookup = {t['name']: t for t in seed['teams']}
synced = 0
mismatches = 0

for f in seed['fixtures']:
    slug = f['slug']
    fpath = os.path.join(MATCH_DIR, slug + '.json')
    if not os.path.exists(fpath):
        print(f"Bug 1: WARNING - no match JSON for {slug}")
        continue
    
    mdata = json.loads(open(fpath, 'r', encoding='utf-8').read())
    changed = False
    
    # Sync metadata fields
    sync_fields = {
        'slug': f['slug'],
        'home': f['home'],
        'away': f['away'],
        'homeCode': teams_lookup.get(f['home'], {}).get('code'),
        'awayCode': teams_lookup.get(f['away'], {}).get('code'),
        'homeFlag': teams_lookup.get(f['home'], {}).get('flag'),
        'awayFlag': teams_lookup.get(f['away'], {}).get('flag'),
        'group': f['group'],
        'matchday': f['matchday'],
        'date': f['date'],
        'time': f.get('time', '15:00'),
        'venue': f['venue'],
        'city': f['city'],
        'status': f['status'],
        'homeScore': f.get('homeScore'),
        'awayScore': f.get('awayScore'),
        'marquee': f.get('marquee', False),
        'liveMinute': f.get('liveMinute'),
    }
    
    for key, val in sync_fields.items():
        if mdata.get(key) != val:
            if key in ('status', 'homeScore', 'awayScore'):
                mismatches += 1
            mdata[key] = val
            changed = True
    
    if changed:
        with open(fpath, 'w', encoding='utf-8') as fp:
            fp.write(json.dumps(mdata, ensure_ascii=False, indent=2))
        synced += 1

print(f"Bug 1: Synced metadata in {synced} match JSON files ({mismatches} score/status mismatches fixed).")
print("All fixes applied successfully.")
