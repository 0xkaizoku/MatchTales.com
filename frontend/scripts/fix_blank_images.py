"""Unique working photo per story. Related match reuses that photo. Never blank."""
from __future__ import annotations

import json
import re
import ssl
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

FRONTEND = Path(__file__).resolve().parents[1]
STORIES = FRONTEND / "src" / "content" / "stories"
MATCHES = FRONTEND / "src" / "content" / "matches"
CTX = ssl.create_default_context()
UA = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
    ),
    "Accept": "image/avif,image/webp,image/apng,image/*,*/*;q=0.8",
}
MIN_BYTES = 20000

UNSPLASH = {
    "soccer": [
        "1574629810360-7efbbe195018",
        "1522778119026-d647f0596c20",
        "1579952363873-27f3bade9f55",
        "1431324155629-1a6deb1dec8d",
        "1486286701208-1d58e9338013",
        "1529900748604-07564a03e7a6",
        "1459865264687-595d652de67e",
        "1560272564-c83b66b1ad12",
        "1518843025960-d60217f226f5",
        "1551958219-acbc608c6377",
        "1627774250096-25d8c0ece8ba",
        "1471295253337-3ceaaedca402",
        "1489944440615-453fc2b6a9a9",
        "1543351611-58f69d7c1781",
        "1522778526097-ce0a22ceb253",
        "1517747614396-d21a78b850e8",
        "1430232324554-8f4aebd06683",
        "1569531955323-33c6b2dca44b",
        "1629217855633-79a6925d6c47",
        "1599158150601-1417ebbaafdd",
        "1434648957308-5e6a859697e8",
        "1577223625816-7546f13df25d",
        "1606925797300-0b35e9d1a5ba",
        "1543326727-cf6c39e8f84c",
        "1599474924187-334a4ae5bd3c",
        "1486262715619-67b85e0b08d3",
        "1558618666-fcd25c85cd64",
        "1550565118-3a14e8d0386f",
        "1551244072-5d12893278ab",
        "1531415074968-036ba1b575da",
    ],
    "tennis": [
        "1554068865-24cecd4e34b8",
        "1534158914592-062992fbe900",
        "1595432840542-29b2bc8db9ec",
        "1612872087720-bb876e2e67d1",
        "1526888971786-7bb7cbb88b76",
        "1551775903-6729a6f7c22a",
        "1622163642998-8624d836c0e8",
        "1622272378473-38dc3fd16435",
    ],
    "football": [
        "1566577739112-5184e6ac4a4e",
        "1508098682722-e99c43a406b2",
        "1504609813442-a8924e83f76e",
        "1606107557195-0e29a4b5b4aa",
        "1489944440615-453fc2b6a9a9",
        "1577223625816-7546f13df25d",
    ],
    "f1": [
        "1568605117036-5fe5e7bab0b7",
        "1503376780353-7e6692767b70",
        "1492144534655-90442d86c47a",
        "1493238796260-08dfe3c3a4ee",
        "1511919884226-fd3cad546e63",
        "1542362567-b31e875e327e",
        "1517949906194-22d54be27c4e",
        "1507219948519-32417ffbbd4a",
        "1632249507339-eda158bbb99a",
        "1541447272258-dfb640c7d8d1",
    ],
    "golf": [
        "1535131749006-b7f58c99034b",
        "1530541932291-6bbcce53def2",
        "1592919505851-80cd04ba2f22",
        "1535132011086-b89b06c5cf1e",
        "1596720426673-6e1f8eacbd0d",
        "1500932838584-8d6b5dd2dca2",
    ],
    "basketball": [
        "1546519638-68e109498ffc",
        "1504450758481-7338eba7524a",
        "1515523110804-941d73b543ea",
        "1521412644187-c49fa049e84d",
        "1608245444352-0d32cef0e6b4",
    ],
}

PEXELS = {
    "soccer": [
        274506, 114296, 399187, 1884574, 3148452, 3621104, 3651674, 945471,
        1171084, 1374064, 2444852, 274422, 2834917, 3074920, 3074924, 3184395,
        3628912, 3651672, 3764012, 41257, 863988, 894163, 935985, 6078303,
        6340493, 6985001, 220574, 3041175, 3448250, 3775147, 3621106, 3184291,
        3074922, 1080884,
    ],
    "tennis": [
        209977, 209969, 1103829, 1619860, 1263348, 1619858, 6295878, 209975,
        5739193, 5739188, 5739198, 5739200,
    ],
    "football": [248547, 1618200, 2570139, 3764014, 3764011, 2570138, 1618201, 248548],
    "f1": [12801, 210019, 627678, 3593922, 244206, 3608542, 1413413, 2127733, 3802510, 3593925, 12802, 12795],
    "golf": [54123, 1325735, 1325662, 1325664, 8471888, 6578824, 1325660, 54124, 2744220, 1325736],
    "basketball": [1752757, 945471, 358042, 2834917, 1080882, 1332237, 2834914, 3760259, 1752758, 358043, 1080883],
}


def unsplash_url(pid: str) -> str:
    return f"https://images.unsplash.com/photo-{pid}?auto=format&fit=crop&w=1600&h=900&q=80"


def pexels_url(pid: int) -> str:
    return (
        f"https://images.pexels.com/photos/{pid}/pexels-photo-{pid}.jpeg"
        f"?auto=compress&cs=tinysrgb&w=1600&h=900&fit=crop"
    )


def picsum_url(pid: int) -> str:
    return f"https://picsum.photos/id/{pid}/1600/900"


def get_json(url: str):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=20, context=CTX) as r:
        return json.loads(r.read().decode("utf-8"))


def probe(url: str) -> tuple[str, bool]:
    req = urllib.request.Request(url, headers=UA)
    try:
        with urllib.request.urlopen(req, timeout=14, context=CTX) as r:
            ct = (r.headers.get("Content-Type") or "").lower()
            if r.status != 200 or "image" not in ct or "svg" in ct:
                return url, False
            cl = r.headers.get("Content-Length")
            if cl and cl.isdigit() and int(cl) >= MIN_BYTES:
                return url, True
            buf = r.read(MIN_BYTES + 1)
            return url, len(buf) >= MIN_BYTES
    except Exception:
        return url, False


def probe_many(urls: list[str]) -> set[str]:
    good: set[str] = set()
    with ThreadPoolExecutor(max_workers=10) as ex:
        futs = [ex.submit(probe, u) for u in urls]
        for i, fut in enumerate(as_completed(futs), 1):
            u, ok = fut.result()
            if ok:
                good.add(u)
            if i % 20 == 0 or not ok:
                print(f"  {i}/{len(urls)} {'OK' if ok else 'BAD'} {u[-70:]}")
    return good


def uniq(seq: list[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for x in seq:
        if x and x not in seen:
            seen.add(x)
            out.append(x)
    return out


def fm_sport(text: str) -> str | None:
    m = re.search(r"^sport:\s*([a-z0-9-]+)\s*$", text, re.M)
    return m.group(1).strip() if m else None


def story_sport(text: str) -> str:
    s = fm_sport(text)
    return s or "soccer"


def match_sport(data: dict) -> str:
    s = (data.get("sport") or "").strip().lower()
    if s:
        return s
    g = (data.get("group") or "").upper()
    if g == "F1":
        return "f1"
    if g == "NFL":
        return "football"
    if g in ("ATP", "WTA", "GS"):
        return "tennis"
    if g in ("PGA", "OPEN"):
        return "golf"
    if g in ("NBA", "WNBA"):
        return "basketball"
    return "soccer"


def related_slug(text: str, stem: str) -> str:
    m = re.search(r"^relatedSlug:\s*([a-z0-9-]+)\s*$", text, re.M)
    if m:
        return m.group(1).strip()
    if stem.endswith("-story"):
        return stem[: -len("-story")]
    return stem


def is_report(text: str) -> bool:
    return bool(re.search(r'^category:\s*"?Match Report"?\s*$', text, re.M))


def set_story(path: Path, url: str) -> None:
    text = path.read_text(encoding="utf-8")
    text2, n = re.subn(r'^image:\s*"[^"]*"', f'image: "{url}"', text, count=1, flags=re.M)
    if n != 1:
        raise SystemExit(f"story image replace failed: {path.name}")
    path.write_text(text2, encoding="utf-8")


def set_match(path: Path, url: str) -> None:
    data = json.loads(path.read_text(encoding="utf-8"))
    data["image"] = url
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def picsum_catalog() -> list[str]:
    urls: list[str] = []
    for page in range(1, 12):
        try:
            items = get_json(f"https://picsum.photos/v2/list?page={page}&limit=100")
        except Exception as e:
            print("picsum list fail", page, e)
            break
        if not items:
            break
        for item in items:
            try:
                urls.append(picsum_url(int(item["id"])))
            except Exception:
                continue
        print("  picsum page", page, "n", len(urls))
    return uniq(urls)


def main() -> None:
    stories = sorted(STORIES.glob("*.md"))
    matches = sorted(MATCHES.glob("*.json"))
    print("stories", len(stories), "matches", len(matches))

    themed: dict[str, list[str]] = {k: [] for k in UNSPLASH}
    candidates: list[str] = []
    for sport, ids in UNSPLASH.items():
        for pid in uniq(ids):
            u = unsplash_url(pid)
            themed[sport].append(u)
            candidates.append(u)
    for sport, ids in PEXELS.items():
        for pid in uniq([str(i) for i in ids]):
            u = pexels_url(int(pid))
            themed[sport].append(u)
            candidates.append(u)

    print("probing", len(uniq(candidates)), "themed urls")
    good = probe_many(uniq(candidates))
    print("themed working", len(good))

    pools = {sport: [u for u in uniq(urls) if u in good] for sport, urls in themed.items()}
    for sport, urls in pools.items():
        print(f"  {sport} {len(urls)}")
    all_themed = uniq([u for urls in pools.values() for u in urls])

    print("picsum catalog")
    picsum_pool = picsum_catalog()
    print("picsum", len(picsum_pool))

    used: set[str] = set()

    def next_url(sport: str) -> str:
        # Stay in-sport first. Do not put tennis photos on soccer cards.
        for pool in (pools.get(sport) or [], picsum_pool):
            for u in pool:
                if u not in used:
                    used.add(u)
                    return u
        raise SystemExit("ran out of unique images")

    desk: list[Path] = []
    reports: list[Path] = []
    for p in stories:
        (reports if is_report(p.read_text(encoding="utf-8")) else desk).append(p)

    story_by_event: dict[str, str] = {}
    print("assign stories", len(desk), "desk", len(reports), "reports")
    for p in desk + reports:
        text = p.read_text(encoding="utf-8")
        sport = story_sport(text)
        url = next_url(sport)
        set_story(p, url)
        story_by_event[p.stem] = url
        rel = related_slug(text, p.stem)
        story_by_event.setdefault(rel, url)
        story_by_event.setdefault(f"{rel}-story", url)
        print("story", sport, p.stem[:42], url[-58:])

    print("assign matches", len(matches))
    for p in matches:
        data = json.loads(p.read_text(encoding="utf-8"))
        url = story_by_event.get(f"{p.stem}-story") or story_by_event.get(p.stem)
        if not url:
            url = next_url(match_sport(data))
        set_match(p, url)
        print("match", match_sport(data), p.stem[:42], url[-58:])

    sim = []
    for p in stories:
        m = re.search(r'image:\s*"([^"]+)"', p.read_text(encoding="utf-8"))
        sim.append(m.group(1) if m else "MISSING")
    mim = [json.loads(p.read_text(encoding="utf-8")).get("image") or "MISSING" for p in matches]
    print("RESULT stories", len(sim), "unique", len(set(sim)), "missing", sim.count("MISSING"))
    print("RESULT matches", len(mim), "unique-or-shared-ok", len(set(mim)), "missing", mim.count("MISSING"))
    print("RESULT union unique", len(set(sim) | set(mim)))


if __name__ == "__main__":
    main()
