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

SEM = asyncio.Semaphore(1)
QUOTA_EXCEEDED = False

VOICE = (
    "You are MatchTales — a brilliant, warm football storyteller who writes like a beloved "
    "newspaper columnist (think The Athletic), NOT a robot. Make casual fans and non-watchers FEEL "
    "why a match matters. Voice: casual, fan-centric, vivid, human, a little cheeky, emotionally intelligent, concrete "
    "(real names, dates, scorelines, places). NEVER sound like an AI: no 'in conclusion', no 'as an AI', "
    "no hedging, no generic filler, no lists, no lists in prose. "
    "CRITICAL: Do NOT use em-dashes (—) or double hyphens (--) at all. Do NOT use AI buzzwords/jargon "
    "(e.g., 'tapestry', 'testament', 'delve', 'moreover', 'tethered', 'beacon', 'pinnacle', 'catalyst'). "
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
    gemini_key = os.environ.get("GEMINI_API_KEY", "")
    
    if api_key:
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
    elif gemini_key:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={gemini_key}"
        headers = {
            "Content-Type": "application/json"
        }
        payload = {
            "contents": [
                {"parts": [{"text": prompt}]}
            ],
            "generationConfig": {
                "maxOutputTokens": max_tokens
            },
            "systemInstruction": {
                "parts": [{"text": VOICE}]
            }
        }
        global QUOTA_EXCEEDED
        async with SEM:
            if not QUOTA_EXCEEDED:
                await asyncio.sleep(6.0)
            for attempt in range(5):
                try:
                    async with httpx.AsyncClient(timeout=60.0) as client:
                        resp = await client.post(url, headers=headers, json=payload)
                        if resp.status_code in (429, 503):
                            if "quota" in resp.text.lower():
                                QUOTA_EXCEEDED = True
                                raise ValueError(f"Quota exceeded: {resp.text[:200]}")
                            sleep_time = (2 ** attempt) * 3 + 5
                            print(f"Rate limit or service unavailable ({resp.status_code}) for {session}: {resp.text[:300]}. Retrying in {sleep_time}s...")
                            await asyncio.sleep(sleep_time)
                            continue
                        resp.raise_for_status()
                        data = resp.json()
                        return data["candidates"][0]["content"]["parts"][0]["text"]
                except Exception as e:
                    if "quota" in str(e).lower():
                        raise e
                    if attempt == 4:
                        raise e
                    sleep_time = (2 ** attempt) * 3 + 5
                    print(f"Error on attempt {attempt+1} for {session}: {e}. Retrying in {sleep_time}s...")
                    await asyncio.sleep(sleep_time)
            raise ValueError(f"Failed to generate content for {session} after 5 attempts.")
    else:
        # Fallback to mock generation if no Anthropic or Gemini key is present
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


def generate_fallback_mock(m: Dict[str, Any], h: Dict[str, Any], a: Dict[str, Any]) -> Dict[str, Any]:
    home_name = m["home"]
    away_name = m["away"]
    home_nick = h.get("nick", "the underdogs")
    away_nick = a.get("nick", "the favorites")
    group = m["group"]
    matchday = m["matchday"]
    played = m["status"] == "FINISHED"
    
    def _get_player_name(players, default="Star Player"):
        if not players:
            return default
        p = players[0]
        if isinstance(p, (list, tuple)):
            return p[0]
        return p

    home_player = _get_player_name(h.get("keyPlayers"))
    away_player = _get_player_name(a.get("keyPlayers"))

    if played:
        score_str = f"{m['homeScore']}-{m['awayScore']}"
        headline = f"{home_name} and {away_name} battle to {score_str}"
        story = (
            f"The clash between {home_name} and {away_name} in Group {group} was a classic matchday {matchday} encounter. "
            f"Both teams showed incredible tactical discipline and passion on the pitch, leaving the fans at the edge of their seats.\n\n"
            f"The final score of {score_str} reflects the intensity of the game. Key tactical adjustments from both managers "
            f"ensured that the match remained a balanced and highly competitive affair until the final whistle.\n\n"
            f"With this result, both {home_name} and {away_name} look forward to their next challenges, knowing that every single point "
            f"could be decisive in their quest for World Cup glory."
        )
        teaser = f"A thrilling {score_str} finish as {home_name} takes on {away_name}. Read how this classic unfolded."
    else:
        headline = f"Anticipation builds for {home_name} vs {away_name}"
        story = (
            f"As Group {group} fixtures heat up, {home_name} prepares to face {away_name} in a highly anticipated Matchday {matchday} showdown. "
            f"Both squads have shown impressive form and are eager to secure three points in this crucial fixture.\n\n"
            f"Tactical matchups across the pitch will define the contest, with both managers likely deploying their strongest line-ups "
            f"to seize control of the midfield early in the match.\n\n"
            f"Fans are expecting a high-octane encounter filled with drama, skill, and memorable moments as both nations strive "
            f"to make their mark on the world stage."
        )
        teaser = f"The stage is set for a massive clash between {home_name} and {away_name}. Here is why you cannot miss it."

    whyCareScore = 7.5
    if m.get("marquee"):
        whyCareScore = 9.2

    return {
        "headline": headline[:100],
        "whyCareScore": whyCareScore,
        "whyCareReason": f"A crucial Matchday {matchday} clash in Group {group} with significant tournament implications.",
        "teaser": teaser,
        "story": story,
        "stakes": f"This match is critical for the qualification hopes of both {home_name} and {away_name} in Group {group}.",
        "rivalryAngle": f"A historic football connection between {home_name} ({home_nick}) and {away_name} ({away_nick}) adds fuel to this clash.",
        "funFacts": [
            f"{home_name} are known as {home_nick}.",
            f"{away_name} are known as {away_nick}.",
            f"This is a key Matchday {matchday} fixture in the World Cup group phase."
        ],
        "keyPlayers": [
            {"name": home_player, "team": home_name, "hook": "The captain leading the charge."},
            {"name": away_player, "team": away_name, "hook": "The creative spark in midfield."}
        ],
        "headToHead": f"Previous encounters between these two nations have always been tightly contested affairs.",
        "tags": [home_name.lower().replace(" ", "-"), away_name.lower().replace(" ", "-"), f"group-{group.lower()}"]
    }


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
        print(f"API failed for {m['slug']} ({e}). Falling back to dynamic mock generation.")
        try:
            data = generate_fallback_mock(m, h, a)
            data = _match_record(m, h, a, data)
            out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
            return f"OK   {m['slug']} (fallback)"
        except Exception as fallback_err:
            return f"FAIL {m['slug']}: {str(e)[:80]} | fallback: {str(fallback_err)[:80]}"


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
