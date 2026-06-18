#!/usr/bin/env python3
"""
MatchTales Daily Cloud Automation Engine.
Runs completely in the cloud on a schedule:
1. Scrapes the web (DuckDuckGo) for World Cup 2026 scores and highlights.
2. Uses Claude to parse the raw text and map it to seed.json fixtures.
3. Recalculates group standings.
4. Generates post-match story narratives for finished fixtures.
5. Queries MongoDB Atlas for newsletter subscribers.
6. Uses Claude to write an editorial daily newsletter and sends it via Resend API.
7. Automatically commits updates back to Git (triggering Vercel rebuilds).
"""
import os
import json
import sys
import asyncio
import subprocess
from pathlib import Path
from typing import Any, Dict, List, Tuple
from datetime import datetime, timezone
import httpx
import urllib.parse
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
    print("Recalculated group standings.")

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

# --- Scraper ---
def scrape_web_info(query: str) -> str:
    print(f"Scraping web search for: '{query}'...")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    }
    encoded_query = urllib.parse.quote_plus(query)
    url = f"https://html.duckduckgo.com/html/?q={encoded_query}"
    
    try:
        r = httpx.get(url, headers=headers, timeout=20.0)
        if r.status_code == 200:
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(r.text, "html.parser")
            snippets = []
            for item in soup.find_all("a", class_="result__snippet"):
                snippets.append(item.get_text().strip())
            
            text_result = "\n\n".join(snippets[:12])
            if text_result:
                print(f"Scraped {len(snippets)} snippets.")
                return text_result
            else:
                print("DuckDuckGo returned no snippets. Blocked or empty page.")
        else:
            print(f"DuckDuckGo search returned status code {r.status_code}")
    except Exception as e:
        print(f"Error scraping web search: {e}")
    
    return ""

# --- LLM API Call ---
async def call_llm(prompt: str, system_instruction: str = VOICE, max_tokens: int = 2200) -> str:
    anthropic_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if anthropic_key:
        headers = {
            "x-api-key": anthropic_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json",
        }
        payload = {
            "model": "claude-3-5-sonnet-20241022",
            "max_tokens": max_tokens,
            "system": system_instruction,
            "messages": [{"role": "user", "content": prompt}],
        }
        async with httpx.AsyncClient(timeout=60.0) as client:
            resp = await client.post("https://api.anthropic.com/v1/messages", headers=headers, json=payload)
            resp.raise_for_status()
            return resp.json()["content"][0]["text"]
            
    gemini_key = os.environ.get("GEMINI_API_KEY", "")
    if gemini_key:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={gemini_key}"
        headers = {
            "Content-Type": "application/json"
        }
        payload = {
            "contents": [
                {
                    "parts": [
                        {"text": prompt}
                    ]
                }
            ],
            "generationConfig": {
                "maxOutputTokens": max_tokens
            }
        }
        if system_instruction:
            payload["systemInstruction"] = {
                "parts": [
                    {"text": system_instruction}
                ]
            }
        async with httpx.AsyncClient(timeout=60.0) as client:
            resp = await client.post(url, headers=headers, json=payload)
            resp.raise_for_status()
            data = resp.json()
            try:
                return data["candidates"][0]["content"]["parts"][0]["text"]
            except (KeyError, IndexError) as e:
                raise ValueError(f"Failed to parse Gemini API response: {data}") from e
                
    zai_key = os.environ.get("ZAI_API_KEY", "")
    if zai_key:
        url = "https://api.z.ai/api/paas/v4/chat/completions"
        headers = {
            "Authorization": f"Bearer {zai_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "glm-4-flash",
            "messages": [
                {"role": "system", "content": system_instruction},
                {"role": "user", "content": prompt}
            ],
            "max_tokens": max_tokens
        }
        async with httpx.AsyncClient(timeout=60.0) as client:
            resp = await client.post(url, headers=headers, json=payload)
            resp.raise_for_status()
            data = resp.json()
            try:
                return data["choices"][0]["message"]["content"]
            except (KeyError, IndexError) as e:
                raise ValueError(f"Failed to parse Z.ai API response: {data}") from e
                
    raise ValueError("Neither ANTHROPIC_API_KEY, GEMINI_API_KEY, nor ZAI_API_KEY is configured.")



# --- Database ---
async def fetch_subscribers() -> List[Dict[str, Any]]:
    mongo_url = os.environ.get("MONGO_URL")
    db_name = os.environ.get("DB_NAME", "matchtales")
    if not mongo_url:
        print("No MONGO_URL configured. Skipping database lookup (using mock subscribers).")
        return [{"email": "demo@matchtales.com", "name": "Demo Fan"}]
        
    try:
        from motor.motor_asyncio import AsyncIOMotorClient
        client = AsyncIOMotorClient(mongo_url)
        db = client[db_name]
        cursor = db.newsletter.find({}, {"_id": 0, "email": 1, "name": 1})
        subscribers = await cursor.to_list(length=1000)
        client.close()
        print(f"Retrieved {len(subscribers)} subscribers from MongoDB Atlas.")
        return subscribers
    except Exception as e:
        print(f"Error fetching subscribers from Mongo: {e}")
        return [{"email": "demo@matchtales.com", "name": "Demo Fan"}]

# --- Resend Dispatcher ---
async def send_newsletter(email: str, name: str, subject: str, html_body: str) -> bool:
    resend_key = os.environ.get("RESEND_API_KEY")
    if not resend_key:
        print(f"No RESEND_API_KEY set. (Mock) Emailed {email} with subject: '{subject}'")
        return True
        
    url = "https://api.resend.com/emails"
    headers = {
        "Authorization": f"Bearer {resend_key}",
        "Content-Type": "application/json",
    }
    
    body = f"""
    <div style="font-family: sans-serif; max-width: 600px; margin: 0 auto; padding: 20px; border: 1px solid #e2e8f0; border-radius: 8px;">
        <h1 style="color: #0f172a; border-bottom: 2px solid #0284c7; padding-bottom: 10px; font-size: 24px;">⚽ MatchTales Daily Digest</h1>
        <p>Hi {name or "Football Fan"},</p>
        {html_body}
        <hr style="border: 0; border-top: 1px solid #e2e8f0; margin: 20px 0;">
        <p style="font-size: 11px; color: #64748b; text-align: center;">
            You are receiving this because you signed up on MatchTales.<br>
            <a href="https://www.matchtales.com" style="color: #0284c7;">Visit MatchTales</a> | 
            <a href="#" style="color: #64748b;">Unsubscribe</a>
        </p>
    </div>
    """
    
    payload = {
        "from": "MatchTales <updates@resend.dev>",
        "to": [email],
        "subject": subject,
        "html": body
    }
    
    try:
        async with httpx.AsyncClient() as client:
            res = await client.post(url, headers=headers, json=payload, timeout=10.0)
            if res.status_code == 200:
                print(f"Successfully sent email to {email}")
                return True
            else:
                print(f"Failed to send email to {email}: {res.status_code} - {res.text}")
                return False
    except Exception as e:
        print(f"Connection error sending email to {email}: {e}")
        return False

# --- Git Integration ---
def commit_changes():
    print("Staging and pushing changes to Git...")
    try:
        subprocess.run(["git", "status"], check=True, stdout=subprocess.DEVNULL)
        subprocess.run(["git", "add", str(SEED_PATH), str(MATCH_DIR)], check=True)
        
        status_res = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True, check=True)
        if not status_res.stdout.strip():
            print("No new data to commit. Repository is clean.")
            return
            
        subprocess.run(["git", "commit", "-m", "Daily automated scores update and narratives [skip ci]"], check=True)
        subprocess.run(["git", "push"], check=True)
        print("Pushed changes back to main branch successfully.")
    except Exception as e:
        print(f"Git commit/push failed: {e}")

# --- Main Automation Loop ---
async def main():
    import argparse
    parser = argparse.ArgumentParser(description="MatchTales Daily Cloud Automation Engine")
    parser.add_argument("--dry-run", action="store_true", help="Scrape and build daily newsletter without writing files or emailing")
    parser.add_argument("--write", action="store_true", help="Write changes to static files and generate stories")
    parser.add_argument("--commit", action="store_true", help="Automatically commit changes to Git and push")
    args = parser.parse_args()

    # Load environment variables checks
    has_llm_key = bool(os.environ.get("ANTHROPIC_API_KEY") or os.environ.get("GEMINI_API_KEY") or os.environ.get("ZAI_API_KEY"))
    resend_key = os.environ.get("RESEND_API_KEY", "")
    
    print("Starting MatchTales Daily Automated cloud pipeline...")
    
    # 1. Load current seed
    try:
        seed_data = load_seed()
    except Exception as e:
        print(f"Error loading seed dataset: {e}")
        sys.exit(1)
        
    teams_lookup = {t["name"]: t for t in seed_data["teams"]}
    
    # 2. Perform Web Search Scrape
    today_str = datetime.now().strftime("%Y-%m-%d")
    search_query = f"FIFA World Cup 2026 matches results scores overview highlights date {today_str}"
    scraped_text = scrape_web_info(search_query)
    
    if not scraped_text:
        print("No search info retrieved from web scraper. Using simulated matches...")
        scraped_text = "Simulated update cycle: No matches completed today."

    # 3. Use Claude to parse results and identify updates
    updated_fixtures = []
    
    if not has_llm_key:
        print("\n[WARNING] No ANTHROPIC_API_KEY or GEMINI_API_KEY configured. Simulating match update.")
        # Find first upcoming match to mock
        upcoming = [f for f in seed_data["fixtures"] if f["status"] == "UPCOMING"]
        if not upcoming:
            upcoming = [seed_data["fixtures"][0]]
            upcoming[0]["status"] = "UPCOMING"
        target = upcoming[0]
        target["status"] = "FINISHED"
        target["homeScore"] = 1
        target["awayScore"] = 0
        target["liveMinute"] = None
        updated_fixtures.append(target)
        print(f"Mocked finished match: {target['home']} {target['homeScore']}-{target['awayScore']} {target['away']}")
        
        newsletter_subject = "Daily World Cup MatchTales: Hype & Overviews"
        newsletter_html = "<p>Here is your daily digest of World Cup 2026 action! Stay tuned for more match details.</p>"
    else:
        print("Extracting match updates from scraped text using LLM...")
        
        # Build list of active tournament matches for the context
        fixtures_context = []
        for f in seed_data["fixtures"]:
            fixtures_context.append({
                "slug": f["slug"], "home": f["home"], "away": f["away"],
                "status": f["status"], "homeScore": f["homeScore"], "awayScore": f["awayScore"]
            })
            
        parser_prompt = f"""
        Analyze the following scraped search engine snippets about the World Cup 2026 matches for date {today_str}:
        
        SCRAPED TEXT:
        {scraped_text}
        
        CURRENT SEED FIXTURES:
        {json.dumps(fixtures_context, indent=2)}
        
        For each match in the CURRENT SEED FIXTURES list:
        Identify if there are any new match scores, status changes (e.g. from UPCOMING to LIVE or FINISHED), or live minutes reported in the scraped text.
        
        Respond with STRICT VALID JSON only. Do not include markdown fences, comments or surrounding text.
        Your response shape must be:
        {{
          "updates": [
             {{
                "slug": "match-slug",
                "status": "FINISHED" or "LIVE" or "UPCOMING",
                "homeScore": <int or null>,
                "awayScore": <int or null>,
                "liveMinute": <int or null>
             }}
          ]
        }}
        If no updates are detected, return an empty "updates" list.
        """
        
        try:
            raw_resp = await call_llm(parser_prompt)
            parsed_updates = extract_json(raw_resp)
            updates_list = parsed_updates.get("updates", [])
            
            for update in updates_list:
                for f in seed_data["fixtures"]:
                    if f["slug"] == update["slug"]:
                        # Check if changed
                        if (f["status"] != update["status"] or 
                            f["homeScore"] != update["homeScore"] or 
                            f["awayScore"] != update["awayScore"]):
                            f["status"] = update["status"]
                            f["homeScore"] = update["homeScore"]
                            f["awayScore"] = update["awayScore"]
                            f["liveMinute"] = update.get("liveMinute")
                            updated_fixtures.append(f)
                            print(f"Updated match from LLM: {f['home']} vs {f['away']} | Status: {f['status']} | Score: {f['homeScore']}-{f['awayScore']}")
        except Exception as e:
            print(f"Error parsing LLM updates: {e}")
            
    # 4. Generate narrative packages for finished matches and update standing files
    if updated_fixtures and (args.write or not args.dry_run):
        recalculate_standings(seed_data)
        if args.write:
            save_seed(seed_data)
            
        for uf in updated_fixtures:
            print(f"Generating narrative package for: {uf['slug']}")
            if not has_llm_key:
                # Mock story package
                mock_data = {
                    "headline": f"Drama in Guadalajara: {uf['home']} vs {uf['away']}",
                    "whyCareScore": 8.1,
                    "whyCareReason": "A tightly contested group matchup.",
                    "teaser": "The game lived up to expectations with clinical play.",
                    "story": "It was a tense night.\n\nFans witnessed key strategies paying off.\n\nGroup stages remain wide open.",
                    "stakes": "Crucial points gained here.",
                    "rivalryAngle": "These sides share a rich legacy of footballing.",
                    "funFacts": ["Fact 1", "Fact 2", "Fact 3"],
                    "keyPlayers": [{"name": "Key Player", "team": uf["home"], "hook": "made the difference"}],
                    "headToHead": "Even history.",
                    "tags": ["world cup 2026"]
                }
                # Enrich with _match_record
                h = teams_lookup.get(uf["home"], {})
                a = teams_lookup.get(uf["away"], {})
                story_pkg = _match_record(uf, h, a, mock_data)
            else:
                prompt = _match_prompt(uf, teams_lookup.get(uf["home"], {}), teams_lookup.get(uf["away"], {}))
                try:
                    raw_story = await call_llm(prompt)
                    h = teams_lookup.get(uf["home"], {})
                    a = teams_lookup.get(uf["away"], {})
                    story_pkg = _match_record(uf, h, a, extract_json(raw_story))
                except Exception as e:
                    print(f"Error calling Claude for story: {e}")
                    continue
                    
            if args.write:
                out_path = MATCH_DIR / f"{uf['slug']}.json"
                out_path.write_text(json.dumps(story_pkg, ensure_ascii=False, indent=2), encoding="utf-8")
                print(f"Wrote generated story at {out_path.name}")
                
    # 5. Retrieve subscribers from DB
    subscribers = await fetch_subscribers()
    
    # 6. Generate daily newsletter summary
    if has_llm_key:
        print("Drafting daily digest newsletter via LLM...")
        recent_matches_txt = json.dumps(updated_fixtures, indent=2)
        newsletter_prompt = f"""
        You are the chief editorial writer for MatchTales. Draft a warm, human-sounding daily newsletter summarizing today's action.
        
        RECENT MATCH UPDATES AND SCORES:
        {recent_matches_txt}
        
        Write 3 short, beautiful paragraphs in HTML format.
        
        CRITICAL STYLE RULES:
        - The tone must be casual, highly fan-centric, accurate, and emotional.
        - Absolutely do NOT use em-dashes (—) or double hyphens (--) under any circumstances.
        - Never use AI jargon/fillers (like 'testament', 'delve', 'tapestry', 'tethered', 'beacon').
        - You must include at least one relevant, high-quality image in the HTML (such as a header/banner or story-relevant action shot). Use this URL:
          `<img src="https://images.unsplash.com/photo-1508098682722-e99c43a406b2?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=600" alt="World Cup Football" style="width: 100%; height: auto; border-radius: 6px; margin: 15px 0;" />`
          Place this image between the first and second paragraphs.
        
        Paragraph 1: Catchy summary of the day's narrative and how group standings shifted.
        Paragraph 2: Focus on the significance, drama, and overview of matches played.
        Paragraph 3: Look ahead to tomorrow's key matchups (what's upcoming) and why fans should care.
        
        Include natural links inside the paragraphs like `<a href="https://www.matchtales.com/match/match-slug" style="color: #0284c7; text-decoration: underline;">Read Full Match Tale</a>` for any matches we updated.
        Do not output top-level HTML structural tags (like `<html>` or `<body>`). Just return the raw HTML body paragraphs.
        
        Also provide a subject line as the very first line of your response in this format:
        SUBJECT: <your subject line>
        """
        try:
            newsletter_draft = await call_llm(newsletter_prompt, max_tokens=1500)
            if "SUBJECT:" in newsletter_draft:
                lines = newsletter_draft.split("\n")
                subject_line = lines[0].replace("SUBJECT:", "").strip()
                newsletter_subject = subject_line if subject_line else "Daily World Cup MatchTales Update"
                newsletter_html = "\n".join(lines[1:]).strip()
            else:
                newsletter_subject = "Daily World Cup MatchTales Digest"
                newsletter_html = newsletter_draft
        except Exception as e:
            print(f"Error drafting newsletter: {e}")
            newsletter_subject = "Daily World Cup MatchTales Digest"
            newsletter_html = "<p>Here is your daily digest of World Cup 2026 action! Stay tuned for more match details.</p>"
            
    # 7. Dispatch emails to all subscribers
    if subscribers and not args.dry_run:
        print(f"Dispatching daily emails to {len(subscribers)} subscribers...")
        for sub in subscribers:
            await send_newsletter(sub["email"], sub.get("name", ""), newsletter_subject, newsletter_html)
    else:
        print("\n--- DAILY NEWSLETTER PREVIEW ---")
        print(f"Subject: {newsletter_subject}")
        print(f"Body:\n{newsletter_html}\n")
        
    # 8. Git automation
    if args.commit and not args.dry_run:
        commit_changes()
        
    print("MatchTales Daily Automated Cloud run completed.")

if __name__ == "__main__":
    asyncio.run(main())
