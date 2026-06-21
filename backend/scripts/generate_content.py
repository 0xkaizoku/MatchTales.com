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
STORY_FALLBACKS = {
    "lamine-yamal-new-tiki-taka": {
        "subtitle": "How a teenage sensation and a direct style are reinventing La Roja's historical identity.",
        "body": """## The Boy Who Bypassed the Academy

Lamine Yamal is not playing by the historical rules of Spanish development. While the previous generation of midfielders was drilled to value possession above all else, Yamal plays with the direct, street-football instinct of someone who grew up playing on concrete courts in Rocafonda. He doesn't want to pass sideways; he wants to look the defender in the eye and run at them.

At just a teenager, he carries the weight of a nation on his slender shoulders, but you wouldn't know it from the way he plays. There is a playground joy in his movements, a casual insolence that makes even the most experienced defenders look clumsy.

## Reinventing Tiki-Taka

Spain's historic tiki-taka was beautiful but could occasionally devolve into sterile dominance—thousands of passes with no penetration. This new-look Spain under Luis de la Fuente has kept the technical precision but added rocket fuel to the wings. With Yamal on one flank and Nico Williams on the other, La Roja are suddenly direct, vertical, and terrifying.

It is a style designed to exploit space rather than just control it. When Pedri wins the ball in midfield, he is no longer looking for a five-yard sideways retention pass; he is looking to release Yamal into open grass.

## A Legacy in the Making

What we are witnessing is the birth of a new era. Spain's footballing identity has always been fluid, adapting to the talent at its disposal. In Yamal, they have a player who forces them to adapt. If he can maintain this astronomical trajectory, the 2026 World Cup won't just be a tournament he played in—it will be the tournament he defined.
"""
    },
    "norways-golden-duo-haaland-odegaard": {
        "subtitle": "After 28 years in the wilderness, Norway return powered by two of the world's finest talents.",
        "body": """## The Long Wait

For nearly three decades, Norwegian football fans have had to watch the World Cup from the sidelines, dreaming of the days of Flo and Rekdal. Year after year, qualification campaigns ended in near-misses and heartbreak. But the arrival of two singular talents has transformed Norway from a nostalgic underdog into one of the most intriguing sides in the tournament.

Erling Haaland and Martin Ødegaard represent the perfect marriage of raw power and artistic grace. One is a destructive force of nature; the other is a cerebral orchestrator of space.

## The Artist and the Viking

To watch Norway play is to watch a study in contrast. Ødegaard floats between the lines, constantly scanning the pitch, measuring passes to the millimeter, and dictating the tempo. He is the quiet conductor.

Then there is Haaland. He does not float; he storms. He is a vertical threat who occupies two defenders at all times, stretching the pitch and creating the very space that Ødegaard thrives in. When they click, it is footballing poetry of the highest order.

## Redefining a Nation's Vibe

Norway's challenge has always been supporting their superstars with a cohesive squad. In 2026, the supporting cast has finally stepped up, allowing Haaland and Ødegaard to play their natural game. They are no longer just trying to qualify; they are here to make noise. The long wait is over, and the golden duo is ready to write a new chapter.
"""
    },
    "african-heavyweights-senegal-morocco": {
        "subtitle": "Who will carry Africa furthest in the new 48-team era?",
        "body": """## The Historic Pioneers

Morocco's magical run to the semi-finals in Qatar 2022 shattered a historical glass ceiling, proving that African teams could compete at the very highest level of the game. Senegal, meanwhile, have been the continent's most consistent heavyweight, combining physical dominance with tactical organization.

As the tournament expands to 48 teams, the spotlight on African football is brighter than ever. The question is no longer whether an African team can reach the semi-finals, but who will go even further.

## Tactical Discipline vs Flamboyant Attack

The Atlas Lions of Morocco built their 2022 success on an impenetrable defensive block and lightning-fast transitions. Under Walid Regragui, they remain a side that is incredibly difficult to break down, anchored by Achraf Hakimi's tireless runs.

Senegal, under the leadership of Pape Matar Sarr and Nicolas Jackson, play with a more expansive, aggressive style. They look to dominate the midfield and overwhelm opponents with physical power and direct wing play. It is a clash of two very different footballing philosophies.

## A Continent's Dream

Every time Morocco or Senegal steps onto the pitch, they carry the hopes of an entire continent. The rivalry between these two giants is built on mutual respect and a shared desire to put African football on top of the world. In 2026, both are primed to prove that Qatar was not a one-off, but the start of a permanent shift in power.
"""
    }
}


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
        print(f"API failed for story {s['slug']} ({e}). Falling back to dynamic mock generation.")
        try:
            if s['slug'] in STORY_FALLBACKS:
                data = STORY_FALLBACKS[s['slug']]
            else:
                data = {
                    "subtitle": s['excerpt'],
                    "body": f"## {s['title']}\n\nThis is a beautiful fallback article body for {s['title']}. It covers legacy, tactics, and the incredible human stories of the World Cup."
                }
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
            return f"OK   story {s['slug']} (fallback)"
        except Exception as fallback_err:
            return f"FAIL story {s['slug']}: {str(e)[:80]} | fallback: {str(fallback_err)[:80]}"


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
