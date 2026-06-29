#!/usr/bin/env python3
"""
Generate updated stories for matches with corrected results.
Uses Gemini API to write accurate post-match narratives.
"""
import os
import json
import sys
import asyncio
import httpx
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

ROOT = Path(__file__).resolve().parent.parent.parent
SEED_PATH = ROOT / "frontend" / "src" / "data" / "seed.json"
MATCH_DIR = ROOT / "frontend" / "src" / "content" / "matches"

# Load .env
from dotenv import load_dotenv
load_dotenv(Path(__file__).resolve().parent.parent / ".env")

GEMINI_KEY = os.environ.get("GEMINI_API_KEY", "")

VOICE = (
    "You are MatchTales - a brilliant, warm football storyteller who writes like a beloved "
    "newspaper columnist (think The Athletic), NOT a robot. Make casual fans and non-watchers FEEL "
    "why a match matters. Voice: casual, fan-centric, vivid, human, a little cheeky, emotionally intelligent, concrete "
    "(real names, dates, scorelines, places). NEVER sound like an AI: no 'in conclusion', no 'as an AI', "
    "no hedging, no generic filler, no lists in prose. "
    "CRITICAL: Do NOT use em-dashes or double hyphens at all. "
    "Return STRICT valid JSON only - no markdown fences, no commentary."
)

MATCH_JSON_SHAPE = """{
  "headline": "punchy, emotional, <= 9 words",
  "whyCareScore": <number 0-10, one decimal>,
  "whyCareReason": "one vivid sentence justifying the score",
  "teaser": "2 sentences a non-fan would forward to a friend",
  "story": "3 short paragraphs (~190 words total) of warm human prose: history, stakes, human drama. Use \\n\\n between paragraphs.",
  "stakes": "2-3 sentences on qualification/knockout implications",
  "rivalryAngle": "2-3 sentences on the emotional/historical thread",
  "funFacts": ["fact 1", "fact 2", "fact 3"],
  "keyPlayers": [{"name":"...","team":"...","hook":"why they matter here"}, {"name":"...","team":"...","hook":"..."}],
  "headToHead": "1-2 sentences of historical head-to-head flavour",
  "tags": ["3-5 short lowercase tags"]
}"""

# Matches with significantly updated scores that need new stories
MATCHES_TO_REGEN = [
    # Group B  
    "switzerland-vs-bosnia-and-herzegovina-md1",
    "canada-vs-qatar-md1",
    "switzerland-vs-canada-md2",
    "canada-vs-bosnia-and-herzegovina-md3",
    # Group C
    "brazil-vs-morocco-md1",
    "brazil-vs-haiti-md2",
    "brazil-vs-scotland-md3",
    "haiti-vs-morocco-md3",
    # Group D
    "united-states-vs-paraguay-md1",
    "australia-vs-turkiye-md1",
    "united-states-vs-turkiye-md3",
    "australia-vs-paraguay-md3",
    # Group E
    "germany-vs-ivory-coast-md1",
    "curaçao-vs-ecuador-md1",
    "germany-vs-ecuador-md3",
    "curaçao-vs-ivory-coast-md3",
    # Group F
    "netherlands-vs-japan-md2",
    "netherlands-vs-sweden-md3",
    # Group G
    "egypt-vs-iran-md1",
    "belgium-vs-new-zealand-md1",
    # Group H
    "spain-vs-saudi-arabia-md1",
    # Group I
    "norway-vs-iraq-md1",
    "france-vs-senegal-md1",
    "france-vs-iraq-md3",
    "norway-vs-senegal-md3",
    # Group K
    "uzbekistan-vs-colombia-md3",
]

# De-duplicate
MATCHES_TO_REGEN = list(dict.fromkeys(MATCHES_TO_REGEN))

def extract_json(text: str) -> dict:
    t = text.strip()
    if t.startswith("```"):
        t = t.strip("`")
        t = t[t.find("{"):] if "{" in t else t
    s, e = t.find("{"), t.rfind("}")
    return json.loads(t[s:e + 1])

async def generate_gemini_story(fixture: dict, teams_lookup: dict) -> dict:
    h = teams_lookup.get(fixture['home'], {})
    a = teams_lookup.get(fixture['away'], {})
    
    score = f"{fixture['homeScore']}-{fixture['awayScore']}"
    ctx = {
        "home": fixture['home'],
        "away": fixture['away'],
        "group": fixture['group'],
        "matchday": fixture['matchday'],
        "date": fixture['date'],
        "venue": fixture['venue'],
        "city": fixture['city'],
        "status": fixture['status'],
        "score": score,
        "homeNick": h.get("nick"),
        "awayNick": a.get("nick"),
        "homeKeyPlayers": h.get("keyPlayers"),
        "awayKeyPlayers": a.get("keyPlayers"),
        "homeStory": h.get("story"),
        "awayStory": a.get("story"),
    }
    
    spoiler_rule = (
        f"This match has FINISHED with score {score}. Write the story as a post-match reflection "
        f"that references the result naturally but stays narrative and emotional."
    )
    
    prompt = (
        "Write the MatchTales story package for this 2026 World Cup fixture as STRICT JSON.\n\n"
        f"CONTEXT:\n{json.dumps(ctx, indent=2, ensure_ascii=False)}\n\n"
        f"{spoiler_rule}\n\n"
        f"Return EXACTLY this JSON shape (no extra keys):\n{MATCH_JSON_SHAPE}"
    )
    
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={GEMINI_KEY}"
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"maxOutputTokens": 8192},
        "systemInstruction": {"parts": [{"text": VOICE}]}
    }
    
    raw = None
    for attempt in range(6):
        try:
            async with httpx.AsyncClient(timeout=60.0) as client:
                resp = await client.post(url, headers={"Content-Type": "application/json"}, json=payload)
                if resp.status_code in (429, 503):
                    sleep_time = (2 ** attempt) * 5 + 5
                    print(f"      Rate limited ({resp.status_code}). Retrying in {sleep_time}s...")
                    await asyncio.sleep(sleep_time)
                    continue
                resp.raise_for_status()
                data = resp.json()
                text = data["candidates"][0]["content"]["parts"][0]["text"]
                raw = extract_json(text)
                break
        except Exception as e:
            if attempt == 5:
                raise e
            sleep_time = (2 ** attempt) * 5 + 5
            print(f"      Error ({e}). Retrying in {sleep_time}s...")
            await asyncio.sleep(sleep_time)
    
    if not raw:
        raise ValueError(f"Failed to generate story for {fixture['slug']} after all attempts.")
        
    # Merge with fixture metadata
    raw.update({
        "slug": fixture['slug'],
        "home": fixture['home'],
        "away": fixture['away'],
        "homeCode": h.get("code"),
        "awayCode": a.get("code"),
        "homeFlag": h.get("flag"),
        "awayFlag": a.get("flag"),
        "group": fixture['group'],
        "matchday": fixture['matchday'],
        "date": fixture['date'],
        "time": fixture.get('time', '19:00'),
        "venue": fixture['venue'],
        "city": fixture['city'],
        "status": fixture['status'],
        "homeScore": fixture['homeScore'],
        "awayScore": fixture['awayScore'],
        "marquee": fixture.get('marquee', False),
        "liveMinute": fixture.get('liveMinute'),
    })
    raw["whyCareScore"] = round(float(raw["whyCareScore"]), 1)
    return raw

async def main():
    seed = json.loads(SEED_PATH.read_text(encoding='utf-8'))
    fixtures_lookup = {f['slug']: f for f in seed['fixtures']}
    teams_lookup = {t['name']: t for t in seed['teams']}
    
    if not GEMINI_KEY:
        print("ERROR: No GEMINI_API_KEY found in .env!")
        sys.exit(1)
    
    print(f"Regenerating stories for {len(MATCHES_TO_REGEN)} corrected matches...")
    print(f"Using Gemini API key: {GEMINI_KEY[:20]}...")
    
    success = 0
    failed = []
    
    for slug in MATCHES_TO_REGEN:
        fixture = fixtures_lookup.get(slug)
        if not fixture:
            print(f"  SKIP: {slug} - not found in seed.json")
            continue
        
        print(f"  Generating: {slug} ({fixture['home']} {fixture['homeScore']}-{fixture['awayScore']} {fixture['away']})...")
        
        try:
            story = await generate_gemini_story(fixture, teams_lookup)
            out_path = MATCH_DIR / f"{slug}.json"
            out_path.write_text(json.dumps(story, ensure_ascii=False, indent=2), encoding='utf-8')
            print(f"    OK: {story['headline']}")
            success += 1
        except Exception as e:
            print(f"    FAILED: {e}")
            failed.append(slug)
        
        # Brief pause to avoid rate limiting (5 seconds to respect 12 RPM limits)
        await asyncio.sleep(5)
    
    print(f"\nCompleted: {success} stories generated, {len(failed)} failed.")
    if failed:
        print(f"Failed slugs: {failed}")

if __name__ == "__main__":
    asyncio.run(main())
