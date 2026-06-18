"""
POC Core script for MatchTales.
Validates:
  1) Football-Data.org API connectivity (supplemental live widget).
  2) Claude (claude-sonnet-4-6) match storytelling via emergentintegrations
     -> human-sounding, non-AI prose + structured JSON (whyCareScore, funFacts...).
Run: python3 scripts/poc_core.py
"""
import os
import json
import sys
import asyncio
import requests
from pathlib import Path
from dotenv import load_dotenv

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

FOOTBALL_KEY = os.environ.get("FOOTBALL_DATA_API_KEY")
EMERGENT_KEY = os.environ.get("EMERGENT_LLM_KEY")


def test_football_data():
    print("\n========== TEST 1: Football-Data.org ==========")
    r = requests.get(
        "https://api.football-data.org/v4/competitions",
        headers={"X-Auth-Token": FOOTBALL_KEY},
        timeout=20,
    )
    print("Status:", r.status_code)
    assert r.status_code == 200, f"Football-Data failed: {r.text[:300]}"
    data = r.json()
    comps = data.get("competitions", [])
    print(f"Competitions available: {len(comps)}")
    for c in comps[:5]:
        print(f"  - {c['name']} ({c['code']}) | area={c['area']['name']} | season {c['currentSeason']['startDate']}")
    print("TEST 1 PASSED ✅")
    return True


async def test_claude_story():
    print("\n========== TEST 2: Claude match storytelling ==========")
    from emergentintegrations.llm.chat import LlmChat, UserMessage

    system_message = (
        "You are MatchTales — a brilliant, warm football storyteller who writes like a beloved "
        "newspaper columnist, not a robot. Your job: make casual fans and non-watchers FEEL why a "
        "World Cup match matters. Voice: vivid, human, a little cheeky, emotionally intelligent, "
        "concrete (names, dates, scorelines). NEVER sound like an AI: no 'in conclusion', no "
        "'as an AI', no hedging, no generic filler, no bullet-point stiffness in prose. "
        "Always return STRICT valid JSON only — no markdown fences, no commentary."
    )

    match_ctx = {
        "home": "England",
        "away": "Croatia",
        "competition": "FIFA World Cup 2026",
        "stage": "Group F",
        "date": "2026-06-19",
        "venue": "MetLife Stadium, New Jersey",
        "backstory": "Rematch of the heartbreaking 2018 semi-final where Croatia beat England 2-1 in extra time.",
    }

    prompt = f"""Write the MatchTales story package for this fixture as STRICT JSON.

MATCH CONTEXT:
{json.dumps(match_ctx, indent=2)}

Return EXACTLY this JSON shape:
{{
  "headline": "punchy, emotional, <= 9 words",
  "whyCareScore": <number 0-10, one decimal allowed>,
  "whyCareReason": "one sentence justifying the score",
  "teaser": "2 sentences, spoiler-free hook a non-fan would forward to a friend",
  "story": "3 short paragraphs (~180 words total) of warm human prose: the history, the stakes, the human drama",
  "stakes": "what qualification/knockout implications ride on this",
  "rivalryAngle": "the emotional rivalry/revenge thread",
  "funFacts": ["fact 1", "fact 2", "fact 3"],
  "keyPlayers": [{{"name": "...", "team": "...", "hook": "why they matter here"}}]
}}"""

    chat = LlmChat(
        api_key=EMERGENT_KEY,
        session_id="poc-matchtales-story",
        system_message=system_message,
    ).with_model("anthropic", "claude-sonnet-4-6")

    resp = await chat.send_message(UserMessage(text=prompt))
    print("\n--- RAW RESPONSE ---\n", resp[:1500])

    # Clean potential code fences just in case
    text = resp.strip()
    if text.startswith("```"):
        text = text.strip("`")
        text = text[text.find("{"):]
    text = text[text.find("{"): text.rfind("}") + 1]

    parsed = json.loads(text)
    # Basic schema validation
    for key in ["headline", "whyCareScore", "teaser", "story", "stakes", "rivalryAngle", "funFacts", "keyPlayers"]:
        assert key in parsed, f"Missing key: {key}"
    assert isinstance(parsed["funFacts"], list) and len(parsed["funFacts"]) >= 3, "Need 3 fun facts"
    assert 0 <= float(parsed["whyCareScore"]) <= 10, "Score out of range"

    print("\n--- PARSED & VALIDATED ---")
    print("Headline:", parsed["headline"])
    print("WhyCareScore:", parsed["whyCareScore"], "->", parsed["whyCareReason"])
    print("Teaser:", parsed["teaser"])
    print("Story:\n", parsed["story"])
    print("Fun facts:", parsed["funFacts"])
    print("TEST 2 PASSED ✅")
    return True


async def main():
    test_football_data()
    await test_claude_story()
    print("\n🎉 ALL POC TESTS PASSED")


if __name__ == "__main__":
    asyncio.run(main())
