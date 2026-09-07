from pathlib import Path
import re
from collections import Counter

DIST = Path(__file__).resolve().parents[1] / "dist"
pages = [
    DIST / "index.html",
    DIST / "stories" / "index.html",
    DIST / "sport" / "tennis" / "index.html",
    DIST / "sport" / "football" / "index.html",
    DIST / "sport" / "f1" / "index.html",
    DIST / "sport" / "soccer" / "index.html",
    DIST / "sport" / "golf" / "index.html",
    DIST / "sport" / "basketball" / "index.html",
]
img_re = re.compile(r'<img[^>]+src="([^"]+)"', re.I)
photo_re = re.compile(r"unsplash|pexels|picsum", re.I)
id_re = re.compile(r"(?:photo-|photos/|picsum\.photos/id/)([A-Za-z0-9_-]+)")

for page in pages:
    html = page.read_text(encoding="utf-8", errors="ignore")
    srcs = [s.replace("&amp;", "&") for s in img_re.findall(html) if photo_re.search(s)]
    ids = []
    for s in srcs:
        m = id_re.search(s)
        ids.append(m.group(1) if m else s)
    c = Counter(ids)
    dups = [(i, n) for i, n in c.items() if n > 1]
    print(page.relative_to(DIST), "photos", len(srcs), "unique", len(set(ids)), "dups", dups or "none")
