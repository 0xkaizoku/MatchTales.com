from __future__ import annotations
import json, re, ssl, urllib.request
from collections import Counter
from pathlib import Path

FRONTEND = Path(__file__).resolve().parents[1]
STORIES = FRONTEND / "src" / "content" / "stories"
MATCHES = FRONTEND / "src" / "content" / "matches"
CTX = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0", "Accept": "image/*"}

def urls():
    out = []
    for p in STORIES.glob("*.md"):
        m = re.search(r'image:\s*"([^"]+)"', p.read_text(encoding="utf-8"))
        out.append(("story", p.stem, m.group(1) if m else ""))
    for p in MATCHES.glob("*.json"):
        d = json.loads(p.read_text(encoding="utf-8"))
        out.append(("match", p.stem, d.get("image") or ""))
    return out

def probe(url: str) -> bool:
    req = urllib.request.Request(url, headers=UA)
    try:
        with urllib.request.urlopen(req, timeout=12, context=CTX) as r:
            ct = (r.headers.get("Content-Type") or "").lower()
            cl = r.headers.get("Content-Length")
            if r.status != 200 or "image" not in ct:
                return False
            if cl and cl.isdigit():
                return int(cl) >= 20000
            return len(r.read(20001)) >= 20000
    except Exception:
        return False

rows = urls()
sim = [u for k, _, u in rows if k == "story"]
mim = [u for k, _, u in rows if k == "match"]
print("stories", len(sim), "unique", len(set(sim)), "blank", sim.count(""))
print("matches", len(mim), "unique", len(set(mim)), "blank", mim.count(""))
print("dup stories", [(u[-40:], n) for u, n in Counter(sim).most_common(3) if n > 1])
sample = []
seen = set()
for _, stem, u in rows:
    if u and u not in seen:
        seen.add(u)
        sample.append((stem, u))
    if len(sample) >= 18:
        break
# always include a picsum tail
for _, stem, u in rows:
    if "picsum.photos" in u:
        sample.append((stem, u))
        break
bad = 0
for stem, u in sample:
    ok = probe(u)
    print(("OK " if ok else "BAD"), stem[:36], u[-70:])
    if not ok:
        bad += 1
print("sample bad", bad, "of", len(sample))
