"""
MatchTales content generator.
Reads seed.json and uses Claude (claude-sonnet-4-6) via emergentintegrations to write:
  - src/content/matches/<slug>.json   (per-fixture story package)
  - src/content/stories/<slug>.mdx     (long-form editorial)
  - src/content/teams/<slug>.json      (team dossier enrichment)
Idempotent: skips files that already exist (delete to regenerate). Concurrency-limited.
Run: python3 scripts/generate_content.py [--only matches|stories|teams] [--force]
"""
import os, json, asyncio, sys, re
from pathlib import Path
from typing import Any, Coroutine, Dict, List
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")
EMERGENT_KEY = os.environ.get("EMERGENT_LLM_KEY", "")

FE = ROOT.parent / "frontend" / "src"
SEED = json.loads((FE / "data" / "seed.json").read_text(encoding="utf-8"))
MATCH_DIR = FE / "content" / "matches"
STORY_DIR = FE / "content" / "stories"
TEAM_DIR = FE / "content" / "teams"
for d in (MATCH_DIR, STORY_DIR, TEAM_DIR):
    d.mkdir(parents=True, exist_ok=True)

FORCE = "--force" in sys.argv
ONLY = None
if "--only" in sys.argv:
    ONLY = sys.argv[sys.argv.index("--only") + 1]

SEM = asyncio.Semaphore(5)

VOICE = (
    "You are MatchTales — a brilliant, warm football storyteller who writes like a beloved "
    "newspaper columnist (think The Athletic), NOT a robot. Make casual fans and non-watchers FEEL "
    "why a match matters. Voice: vivid, human, a little cheeky, emotionally intelligent, concrete "
    "(real names, dates, scorelines, places). NEVER sound like an AI: no 'in conclusion', no 'as an AI', "
    "no hedging, no generic filler, no listy stiffness in prose, no em-dash overuse. "
    "Return STRICT valid JSON only when asked for JSON — no markdown fences, no commentary."
)


def teams_index() -> Dict[str, Any]:
    return {t["name"]: t for t in SEED["teams"]}


TI = teams_index()


def extract_json(text: str) -> Dict[str, Any]:
    t = text.strip()
    if t.startswith("```"):
        t = t.strip("`")
        t = t[t.find("{"):] if "{" in t else t
    s, e = t.find("{"), t.rfind("}")
    return json.loads(t[s:e + 1])


async def claude(session: str, prompt: str, max_tokens: int = 2200) -> str:
    import httpx
    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key:
        # Fallback to mock generation if no Anthropic key is present
        if "fixtures" in prompt or "match" in prompt:
            return json.dumps({
                "headline": "Mock Hype Headline",
                "whyCareScore": 8.2,
                "whyCareReason": "This is a mock why-care reason for this match.",
                "teaser": "Mock teaser sentence. Another mock teaser sentence.",
                "story": "Mock paragraph one.\n\nMock paragraph two.\n\nMock paragraph three.",
                "stakes": "Mock stakes description here.",
                "rivalryAngle": "Mock rivalry details.",
                "funFacts": ["Mock fact A", "Mock fact B", "Mock fact C"],
                "keyPlayers": [{"name": "Player A", "team": "Team A", "hook": "why they matter"}, {"name": "Player B", "team": "Team B", "hook": "why they matter"}]
            })
        elif "story" in prompt or "editorial" in prompt:
            return json.dumps({
                "subtitle": "A mock editorial subtitle",
                "body": "## Section Heading\n\nMock body paragraph for story."
            })
        else:
            return json.dumps({
                "dossier": "Mock team dossier paragraph one.\n\nMock team dossier paragraph two.",
                "whatToWatch": "Mock watch reason details.",
                "xFactor": "Mock x-factor player details.",
                "verdict": "Mock tournament verdict prediction.",
                "funFacts": ["Mock extra fact 1", "Mock extra fact 2"]
            })

    headers = {
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json",
    }
    data = {
        "model": "claude-3-5-sonnet-20241022",
        "max_tokens": max_tokens,
        "system": VOICE,
        "messages": [{"role": "user", "content": prompt}],
    }
    async with SEM:
        async with httpx.AsyncClient(timeout=60.0) as client:
            resp = await client.post("https://api.anthropic.com/v1/messages", headers=headers, json=data)
            resp.raise_for_status()
            return resp.json()["content"][0]["text"]


# ---------------- MATCHES ----------------
MATCH_JSON_SHAPE = """{
  "headline": "punchy, emotional, <= 9 words",
  "whyCareScore": <number 0-10, one decimal>,
  "whyCareReason": "one vivid sentence justifying the score",
  "teaser": "2 sentences a non-fan would forward to a friend",
  "story": "3 short paragraphs (~190 words total) of warm human prose: history, stakes, human drama. Use \\n\\n between paragraphs.",
  "stakes": "2-3 sentences on qualification/knockout implications",
  "rivalryAngle": "2-3 sentences on the emotional/historical thread (or the storyline if no rivalry)",
  "funFacts": ["fact 1", "fact 2", "fact 3"],
  "keyPlayers": [{"name":"...","team":"...","hook":"why they matter here"}, {"name":"...","team":"...","hook":"..."}],
  "headToHead": "1-2 sentences of historical head-to-head flavour",
  "tags": ["3-5 short lowercase tags"]
}"""


def _match_prompt(m: Dict[str, Any], h: Dict[str, Any], a: Dict[str, Any]) -> str:
    """Build the Claude prompt for a single fixture."""
    played = m["status"] == "FINISHED"
    score = f"{m['homeScore']}-{m['awayScore']}" if played else "not played yet"
    ctx = {
        "home": m["home"], "away": m["away"], "group": m["group"], "matchday": m["matchday"],
        "date": m["date"], "venue": m["venue"], "city": m["city"], "status": m["status"], "score": score,
        "homeNick": h.get("nick"), "awayNick": a.get("nick"),
        "homeKeyPlayers": h.get("keyPlayers"), "awayKeyPlayers": a.get("keyPlayers"),
        "homeStory": h.get("story"), "awayStory": a.get("story"),
    }
    spoiler_rule = (
        "This match has FINISHED with score " + score + ". Write the story as a post-match reflection "
        "that references the result naturally but stays narrative and emotional."
        if played else
        "This match has NOT been played yet. Write a SPOILER-FREE pre-match hype piece. Never invent a result."
    )
    return (
        "Write the MatchTales story package for this 2026 World Cup fixture as STRICT JSON.\n\n"
        f"CONTEXT:\n{json.dumps(ctx, indent=2, ensure_ascii=False)}\n\n"
        f"{spoiler_rule}\n\n"
        f"Return EXACTLY this JSON shape (no extra keys):\n{MATCH_JSON_SHAPE}"
    )


def _match_record(m: Dict[str, Any], h: Dict[str, Any], a: Dict[str, Any], data: Dict[str, Any]) -> Dict[str, Any]:
    """Merge fixture metadata into the AI-generated story package."""
    data.update({
        "slug": m["slug"], "home": m["home"], "away": m["away"],
        "homeCode": h.get("code"), "awayCode": a.get("code"),
        "homeFlag": h.get("flag"), "awayFlag": a.get("flag"),
        "group": m["group"], "matchday": m["matchday"], "date": m["date"], "time": m["time"],
        "venue": m["venue"], "city": m["city"], "status": m["status"],
        "homeScore": m["homeScore"], "awayScore": m["awayScore"],
        "marquee": m.get("marquee", False), "liveMinute": m.get("liveMinute"),
    })
    data["whyCareScore"] = round(float(data["whyCareScore"]), 1)
    return data


async def gen_match(m: Dict[str, Any]) -> str:
    out = MATCH_DIR / f"{m['slug']}.json"
    if out.exists() and not FORCE:
        return f"skip {m['slug']}"
    h, a = TI.get(m["home"], {}), TI.get(m["away"], {})
    try:
        resp = await claude(f"match-{m['slug']}", _match_prompt(m, h, a))
        data = _match_record(m, h, a, extract_json(resp))
        out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        return f"OK   {m['slug']} (wc {data['whyCareScore']})"
    except Exception as e:
        return f"FAIL {m['slug']}: {str(e)[:160]}"


# ---------------- STORIES ----------------
async def gen_story(s: Dict[str, Any]) -> str:
    out = STORY_DIR / f"{s['slug']}.md"
    if out.exists() and not FORCE:
        return f"skip {s['slug']}"
    prompt = f"""Write a long-form MatchTales editorial article.

TITLE: {s['title']}
CATEGORY: {s['category']}
ANGLE: {s['excerpt']}

Write ~600-750 words of gorgeous, human, emotionally-rich football journalism. Use 3-5 short sections.
Return STRICT JSON:
{{
  "subtitle": "one-line dek under the title",
  "body": "the full article in Markdown. Use ## for section headings and blank lines between paragraphs. No top-level H1."
}}"""
    try:
        resp = await claude(f"story-{s['slug']}", prompt, max_tokens=3000)
        data = extract_json(resp)
        body = data["body"].replace("\r\n", "\n")
        fm = (
            "---\n"
            f"title: {json.dumps(s['title'])}\n"
            f"subtitle: {json.dumps(data.get('subtitle',''))}\n"
            f"category: {json.dumps(s['category'])}\n"
            f"excerpt: {json.dumps(s['excerpt'])}\n"
            f"image: {json.dumps(s['img'])}\n"
            f"readingTime: {s['read']}\n"
            f"pubDate: 2026-06-16\n"
            "---\n\n"
        )
        out.write_text(fm + body, encoding="utf-8")
        return f"OK   story {s['slug']}"
    except Exception as e:
        return f"FAIL story {s['slug']}: {str(e)[:160]}"


# ---------------- TEAMS ----------------
async def gen_team(t: Dict[str, Any]) -> str:
    out = TEAM_DIR / f"{t['slug']}.json"
    if out.exists() and not FORCE:
        return f"skip {t['slug']}"
    prompt = f"""Write a MatchTales team dossier for {t['name']} ({t['nick']}) at the 2026 World Cup.

CONTEXT: rank #{t['rank']}, confederation {t['conf']}, best finish: {t['best']}, titles: {t['titles']}.
Key players: {json.dumps(t['keyPlayers'])}. Known fact: {t['funFact']}.

Return STRICT JSON:
{{
  "dossier": "3 warm paragraphs (~200 words) on their World Cup history, identity and 2026 hopes. Use \\n\\n between paragraphs.",
  "whatToWatch": "2 sentences on the must-watch reason for casual fans",
  "xFactor": "the one player who could change everything + why (1 sentence)",
  "verdict": "one punchy sentence predicting their tournament vibe (no exact placement)",
  "funFacts": ["extra fact 1", "extra fact 2"]
}}"""
    try:
        resp = await claude(f"team-{t['slug']}", prompt, max_tokens=1600)
        data = extract_json(resp)
        data["slug"] = t["slug"]
        data["name"] = t["name"]
        out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        return f"OK   team {t['slug']}"
    except Exception as e:
        return f"FAIL team {t['slug']}: {str(e)[:160]}"


async def main():
    tasks = []
    if ONLY in (None, "matches"):
        tasks += [gen_match(m) for m in SEED["fixtures"]]
    if ONLY in (None, "stories"):
        tasks += [gen_story(s) for s in SEED["storiesMeta"]]
    if ONLY in (None, "teams"):
        tasks += [gen_team(t) for t in SEED["teams"]]
    print(f"Generating {len(tasks)} items (force={FORCE}, only={ONLY})...")
    results = await asyncio.gather(*tasks)
    ok = sum(1 for r in results if r.startswith("OK"))
    skip = sum(1 for r in results if r.startswith("skip"))
    fail = [r for r in results if r.startswith("FAIL")]
    for r in results:
        if not r.startswith("skip"):
            print(" ", r)
    print(f"\nDONE: ok={ok} skip={skip} fail={len(fail)}")
    if fail:
        print("FAILURES:")
        for f in fail:
            print("  ", f)


if __name__ == "__main__":
    asyncio.run(main())
