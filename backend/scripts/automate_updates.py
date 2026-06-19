#!/usr/bin/env python3
"""
MatchTales Automation Engine.
Fetches real-time scores from Football-Data.org (World Cup 2026),
updates seed.json, recalculates standings, generates match narrative
stories using Claude, and runs optional post-update triggers (rebuild/deploy).
"""
import os
import json
import sys
import asyncio
import subprocess
from pathlib import Path
from typing import Any, Dict, List, Tuple
import requests
import httpx
from dotenv import load_dotenv

# Reconfigure stdout for UTF-8 support on Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# Path configs
BACKEND_DIR = Path(__file__).resolve().parent.parent
ROOT_DIR = BACKEND_DIR.parent
load_dotenv(BACKEND_DIR / ".env")

SEED_PATH = ROOT_DIR / "frontend" / "src" / "data" / "seed.json"
MATCH_DIR = ROOT_DIR / "frontend" / "src" / "content" / "matches"

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

def load_seed() -> Dict[str, Any]:
    if not SEED_PATH.exists():
        raise FileNotFoundError(f"seed.json not found at {SEED_PATH}")
    return json.loads(SEED_PATH.read_text(encoding="utf-8"))

def save_seed(data: Dict[str, Any]) -> None:
    SEED_PATH.parent.mkdir(parents=True, exist_ok=True)
    SEED_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Updated {SEED_PATH} successfully.")

def find_team_by_fd(team_fd: Dict[str, Any], seed_teams: List[Dict[str, Any]]) -> Dict[str, Any]:
    tla = team_fd.get("tla")
    name = team_fd.get("name")
    if tla:
        for t in seed_teams:
            if t["code"].upper() == tla.upper():
                return t
    if name:
        for t in seed_teams:
            if t["name"].lower() == name.lower():
                return t
        # Normalization fallback
        norm_fd = name.lower().replace(" republic", "").replace(" & ", " and ")
        for t in seed_teams:
            norm_seed = t["name"].lower().replace(" republic", "").replace(" & ", " and ")
            if norm_seed == norm_fd:
                return t
    return None

def recalculate_standings(seed_data: Dict[str, Any]) -> None:
    groups = {}
    for tm in seed_data["teams"]:
        groups.setdefault(tm["group"], [])
        groups[tm["group"]].append({
            "name": tm["name"], "code": tm["code"], "flag": tm["flag"],
            "P": 0, "W": 0, "D": 0, "L": 0, "GF": 0, "GA": 0, "GD": 0, "Pts": 0
        })
    
    def find_row(g: str, name: str):
        for r in groups[g]:
            if r["name"] == name:
                return r
        return None

    for m in seed_data["fixtures"]:
        if m["status"] != "FINISHED":
            continue
        hs, as_ = m["homeScore"], m["awayScore"]
        if hs is None or as_ is None:
            continue
        try:
            hs = int(hs)
            as_ = int(as_)
        except (ValueError, TypeError):
            continue
        
        hr, ar = find_row(m["group"], m["home"]), find_row(m["group"], m["away"])
        if not hr or not ar:
            continue
            
        for r in (hr, ar):
            r["P"] += 1
        hr["GF"] += hs
        hr["GA"] += as_
        ar["GF"] += as_
        ar["GA"] += hs
        
        if hs > as_:
            hr["W"] += 1
            ar["L"] += 1
            hr["Pts"] += 3
        elif hs < as_:
            ar["W"] += 1
            hr["L"] += 1
            ar["Pts"] += 3
        else:
            hr["D"] += 1
            ar["D"] += 1
            hr["Pts"] += 1
            ar["Pts"] += 1

    for g in groups:
        for r in groups[g]:
            r["GD"] = r["GF"] - r["GA"]
        groups[g].sort(key=lambda r: (r["Pts"], r["GD"], r["GF"]), reverse=True)
    
    seed_data["groups"] = groups
    print("Recalculated standings for all groups.")

def extract_json(text: str) -> Dict[str, Any]:
    t = text.strip()
    if t.startswith("```"):
        t = t.strip("`")
        t = t[t.find("{"):] if "{" in t else t
    s, e = t.find("{"), t.rfind("}")
    return json.loads(t[s:e + 1])

def _match_prompt(m: Dict[str, Any], h: Dict[str, Any], a: Dict[str, Any]) -> str:
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

async def generate_claude_story(m: Dict[str, Any], teams_lookup: Dict[str, Any]) -> Dict[str, Any]:
    h, a = teams_lookup.get(m["home"], {}), teams_lookup.get(m["away"], {})
    anthropic_key = os.environ.get("ANTHROPIC_API_KEY", "")
    gemini_key = os.environ.get("GEMINI_API_KEY", "")
    has_llm_key = bool(anthropic_key or gemini_key)
    
    if not has_llm_key:
        print(f"No ANTHROPIC_API_KEY or GEMINI_API_KEY found, using mock story generation for {m['slug']}...")
        mock_data = {
            "headline": f"A Grudge Match for the Ages: {m['home']} vs {m['away']}",
            "whyCareScore": 8.5,
            "whyCareReason": f"An intense Group {m['group']} duel that reshapes the tournament bracket.",
            "teaser": f"Will {m['home']} seal progression, or can {m['away']} spark a tournament shock? Keep your eyes on this key matchup.",
            "story": f"The stage is set at the {m['venue']} in {m['city']}. The fans are pouring in.\n\nThis match defines the narrative for both {m['home']} and {m['away']} in their Quest for World Cup glory.\n\nEvery pass and tackle will echo through Group {m['group']}.",
            "stakes": f"A crucial three points that could mathematically guarantee qualification or send one of the giants home early.",
            "rivalryAngle": f"No love lost here. The footballing history between these two guarantees a feisty affair.",
            "funFacts": ["First meeting in this venue.", "The starting lineups have a combined 120 caps.", "A draw favors the chasing pack in Group stage."],
            "keyPlayers": [
                {"name": h.get("keyPlayers", [["Star A"]])[0][0], "team": m["home"], "hook": "The creative engine looking to find space"},
                {"name": a.get("keyPlayers", [["Star B"]])[0][0], "team": m["away"], "hook": "The defensive rock standing in the way"}
            ],
            "headToHead": "They have met several times globally, with very little separating them historically.",
            "tags": ["world cup 2026", m["home"].lower(), m["away"].lower(), f"group {m['group'].lower()}"]
        }
        return _match_record(m, h, a, mock_data)

    prompt = _match_prompt(m, h, a)
    
    if anthropic_key:
        headers = {
            "x-api-key": anthropic_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json",
        }
        payload = {
            "model": "claude-3-5-sonnet-20241022",
            "max_tokens": 2200,
            "system": VOICE,
            "messages": [{"role": "user", "content": prompt}],
        }
        async with httpx.AsyncClient(timeout=60.0) as client:
            resp = await client.post("https://api.anthropic.com/v1/messages", headers=headers, json=payload)
            resp.raise_for_status()
            text = resp.json()["content"][0]["text"]
            raw_json = extract_json(text)
            return _match_record(m, h, a, raw_json)
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
                "maxOutputTokens": 8192
            },
            "systemInstruction": {
                "parts": [{"text": VOICE}]
            }
        }
        async with httpx.AsyncClient(timeout=60.0) as client:
            resp = await client.post(url, headers=headers, json=payload)
            resp.raise_for_status()
            data = resp.json()
            try:
                text = data["candidates"][0]["content"]["parts"][0]["text"]
                raw_json = extract_json(text)
                return _match_record(m, h, a, raw_json)
            except (KeyError, IndexError) as e:
                raise ValueError(f"Failed to parse Gemini API response: {data}") from e


def fetch_football_data_matches() -> List[Dict[str, Any]]:
    api_key = os.environ.get("FOOTBALL_DATA_API_KEY")
    if not api_key:
        print("No FOOTBALL_DATA_API_KEY configured. Cannot fetch real-time updates from API.")
        return []
    
    url = "https://api.football-data.org/v4/competitions/WC/matches"
    headers = {"X-Auth-Token": api_key}
    
    try:
        r = requests.get(url, headers=headers, timeout=20)
        if r.status_code == 200:
            return r.json().get("matches", [])
        else:
            print(f"Error fetching from Football-Data.org: {r.status_code} - {r.text}")
            return []
    except Exception as e:
        print(f"Connection error to Football-Data.org: {e}")
        return []

def run_git_commands() -> None:
    print("Running Git commands to commit updates...")
    try:
        # Check if inside git repo
        subprocess.run(["git", "status"], check=True, stdout=subprocess.DEVNULL)
        
        # Git add
        subprocess.run(["git", "add", str(SEED_PATH), str(MATCH_DIR)], check=True)
        
        # Git commit - check if changes exist
        status_res = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True, check=True)
        if not status_res.stdout.strip():
            print("No changes detected. Skipping git commit.")
            return
            
        subprocess.run(["git", "commit", "-m", "Auto-update matches and stories [skip ci]"], check=True)
        subprocess.run(["git", "push"], check=True)
        print("Successfully committed and pushed updates to remote git repository.")
    except Exception as e:
        print(f"Error running Git workflow: {e}")

def run_local_build() -> None:
    print("Running local Astro build...")
    frontend_dir = ROOT_DIR / "frontend"
    try:
        # Try running npm or yarn build
        has_npm = subprocess.run(["npm", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0
        cmd = ["npm", "run", "build"] if has_npm else ["yarn", "build"]
        
        print(f"Executing: {' '.join(cmd)} inside {frontend_dir}")
        subprocess.run(cmd, cwd=frontend_dir, check=True)
        print("Astro build completed successfully.")
    except Exception as e:
        print(f"Error running Astro build: {e}")

def trigger_deploy_hook(url: str) -> None:
    print(f"Triggering deploy hook: {url}")
    try:
        res = requests.post(url, timeout=10)
        print(f"Deploy hook status: {res.status_code} | response: {res.text[:100]}")
    except Exception as e:
        print(f"Error triggering deploy hook: {e}")

async def main():
    import argparse
    parser = argparse.ArgumentParser(description="MatchTales Automation Engine")
    parser.add_argument("--dry-run", action="store_true", help="Print updates without writing to disk or AI generation")
    parser.add_argument("--mock", action="store_true", help="Simulate a match finishing to test pipeline")
    parser.add_argument("--write", action="store_true", help="Write changes to seed.json and generate story packages")
    parser.add_argument("--commit", action="store_true", help="Automatically commit changes to Git and push")
    parser.add_argument("--build", action="store_true", help="Run local Astro static build after updates")
    parser.add_argument("--deploy-hook", type=str, help="Vercel deploy hook URL to trigger remote build")
    args = parser.parse_args()

    # Set parameters from environment if not supplied
    if not args.deploy_hook and os.environ.get("VERCEL_DEPLOY_HOOK_URL"):
        args.deploy_hook = os.environ.get("VERCEL_DEPLOY_HOOK_URL")
    if not args.commit and os.environ.get("AUTO_COMMIT") == "true":
        args.commit = True

    try:
        seed_data = load_seed()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

    teams_lookup = {t["name"]: t for t in seed_data["teams"]}
    updated_fixtures = []

    if args.mock:
        print("\n=== RUNNING IN MOCK MODE ===")
        # Find first upcoming match
        upcoming = [f for f in seed_data["fixtures"] if f["status"] == "UPCOMING"]
        if not upcoming:
            print("No upcoming matches found in seed.json. Resetting the first fixture to test...")
            upcoming = [seed_data["fixtures"][0]]
            upcoming[0]["status"] = "UPCOMING"
            upcoming[0]["homeScore"] = None
            upcoming[0]["awayScore"] = None
        
        target = upcoming[0]
        print(f"Mocking match result for: {target['home']} vs {target['away']} (Group {target['group']}, MD{target['matchday']})")
        target["status"] = "FINISHED"
        target["homeScore"] = 2
        target["awayScore"] = 1
        target["liveMinute"] = None
        updated_fixtures.append(target)
    else:
        print("\n=== FETCHING REAL API DATA ===")
        api_matches = fetch_football_data_matches()
        if not api_matches:
            print("No matches fetched or error occurred. Exiting.")
            sys.exit(0)
            
        print(f"Fetched {len(api_matches)} matches from Football-Data.org.")
        
        for fd_m in api_matches:
            home_t = find_team_by_fd(fd_m["homeTeam"], seed_data["teams"])
            away_t = find_team_by_fd(fd_m["awayTeam"], seed_data["teams"])
            
            if not home_t or not away_t:
                continue
                
            # Try to match local fixture
            matchday = fd_m.get("matchday")
            matched_fixture = None
            for local_f in seed_data["fixtures"]:
                if (local_f["home"] == home_t["name"] and 
                    local_f["away"] == away_t["name"] and 
                    local_f["matchday"] == matchday):
                    matched_fixture = local_f
                    break
            
            if not matched_fixture:
                continue
            
            # Map status
            # Football-data: FINISHED, IN_PLAY, PAUSED, TIMED, SCHEDULED
            # MatchTales: FINISHED, LIVE, UPCOMING
            fd_status = fd_m.get("status")
            new_status = "UPCOMING"
            if fd_status == "FINISHED":
                new_status = "FINISHED"
            elif fd_status in ("IN_PLAY", "PAUSED"):
                new_status = "LIVE"
                
            # Get scores
            fd_score = fd_m.get("score", {})
            full_time = fd_score.get("fullTime", {})
            new_home_score = full_time.get("home")
            new_away_score = full_time.get("away")
            
            # Check if any updates
            has_status_change = matched_fixture["status"] != new_status
            has_score_change = (matched_fixture["homeScore"] != new_home_score or 
                                matched_fixture["awayScore"] != new_away_score)
            
            if has_status_change or has_score_change:
                matched_fixture["status"] = new_status
                matched_fixture["homeScore"] = new_home_score
                matched_fixture["awayScore"] = new_away_score
                
                # Check live minute
                if new_status == "LIVE":
                    # Estimate live minute (simple mapping or default)
                    matched_fixture["liveMinute"] = fd_m.get("minute", 45)
                else:
                    matched_fixture["liveMinute"] = None
                    
                updated_fixtures.append(matched_fixture)
                print(f"Detected change in: {matched_fixture['home']} {new_home_score}-{new_away_score} {matched_fixture['away']} | status: {new_status}")

    if not updated_fixtures:
        print("No match updates detected. Everything is up to date!")
        sys.exit(0)

    print(f"\nProcessing {len(updated_fixtures)} updated fixture(s)...")

    if args.dry_run:
        print("\n--- DRY RUN SUMMARY ---")
        for uf in updated_fixtures:
            print(f"Fixture: {uf['slug']}")
            print(f"  Score: {uf['homeScore']}-{uf['awayScore']}")
            print(f"  Status: {uf['status']}")
        print("Dry run completed. No files modified.")
        sys.exit(0)

    # Perform updates if not dry run
    if args.write or args.mock:
        # Save updated seed.json
        recalculate_standings(seed_data)
        save_seed(seed_data)

        # Generate stories for each updated match
        for uf in updated_fixtures:
            print(f"Generating story narrative for {uf['slug']}...")
            try:
                story_pkg = await generate_claude_story(uf, teams_lookup)
                out_path = MATCH_DIR / f"{uf['slug']}.json"
                out_path.write_text(json.dumps(story_pkg, ensure_ascii=False, indent=2), encoding="utf-8")
                print(f"Successfully generated story at {out_path.name}")
            except Exception as e:
                print(f"Failed to generate story for {uf['slug']}: {e}")

        # Post-update triggers
        if args.build:
            run_local_build()
        
        if args.deploy_hook:
            trigger_deploy_hook(args.deploy_hook)
            
        if args.commit:
            run_git_commands()

if __name__ == "__main__":
    asyncio.run(main())
