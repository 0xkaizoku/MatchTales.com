from fastapi import FastAPI, APIRouter, HTTPException, Query
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
import os
import logging
import time
from pathlib import Path
from pydantic import BaseModel, Field, ConfigDict, EmailStr
from typing import List, Optional
import uuid
from datetime import datetime, timezone
import httpx
import asyncio
import sys

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def get_script_path(script_name: str) -> str:
    path = ROOT_DIR / "scripts" / script_name
    return str(path)

# MongoDB connection
mongo_url = os.environ.get('MONGO_URL', 'mongodb://localhost:27017')
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ.get('DB_NAME', 'matchtales')]

FOOTBALL_API_KEY = os.environ.get('FOOTBALL_DATA_API_KEY', '')
FOOTBALL_BASE = "https://api.football-data.org/v4"

app = FastAPI(title="MatchTales API")
api_router = APIRouter(prefix="/api")

# Simple in-memory cache for football-data responses (reduce rate-limit hits)
_cache: dict = {}
_CACHE_TTL = 60  # seconds
# Unique sentinel so callers can use identity comparison (`is`) to detect a cache
# miss unambiguously, even when a legitimately cached value happens to be falsy.
_CACHE_MISS: object = object()


def cache_get(key: str) -> object:
    item = _cache.get(key)
    if item and (time.time() - item[0] < _CACHE_TTL):
        return item[1]
    return _CACHE_MISS


def cache_set(key: str, value: object) -> None:
    _cache[key] = (time.time(), value)


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


# ---------------- Models ----------------
class StatusCheck(BaseModel):
    model_config = ConfigDict(extra="ignore")
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    client_name: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class StatusCheckCreate(BaseModel):
    client_name: str


class NewsletterCreate(BaseModel):
    email: EmailStr
    name: Optional[str] = None


class HypeNoteCreate(BaseModel):
    name: Optional[str] = Field(default="Anonymous", max_length=40)
    matchSlug: Optional[str] = None
    matchLabel: Optional[str] = None
    text: str = Field(min_length=3, max_length=400)


class HypeNote(BaseModel):
    model_config = ConfigDict(extra="ignore")
    id: str
    name: str
    matchSlug: Optional[str] = None
    matchLabel: Optional[str] = None
    text: str
    likes: int = 0
    createdAt: str


# ---------------- Routes ----------------
@api_router.get("/")
async def root():
    return {"message": "MatchTales API live", "service": "matchtales"}


@api_router.post("/status", response_model=StatusCheck)
async def create_status_check(input: StatusCheckCreate):
    status_obj = StatusCheck(**input.model_dump())
    doc = status_obj.model_dump()
    doc['timestamp'] = doc['timestamp'].isoformat()
    await db.status_checks.insert_one(doc)
    return status_obj


# ---- Newsletter ----
@api_router.post("/newsletter")
async def subscribe_newsletter(payload: NewsletterCreate):
    email = payload.email.lower().strip()
    existing = await db.newsletter.find_one({"email": email})
    if existing:
        return {"ok": True, "message": "You're already on the list — see you on matchday!", "already": True}
    doc = {
        "id": str(uuid.uuid4()),
        "email": email,
        "name": payload.name,
        "createdAt": now_iso(),
    }
    await db.newsletter.insert_one(doc)
    
    # Send a welcome email via Resend if RESEND_API_KEY is configured
    resend_key = os.environ.get("RESEND_API_KEY")
    if resend_key:
        try:
            async with httpx.AsyncClient() as cx:
                email_body = f"""
                <div style="font-family: sans-serif; max-width: 600px; margin: 0 auto; padding: 20px; border: 1px solid #e2e8f0; border-radius: 8px;">
                    <h2 style="color: #0f172a;">Welcome to MatchTales! ⚽</h2>
                    <p>Hi {payload.name or "football fan"},</p>
                    <p>Thanks for subscribing to MatchTales! We'll send you editorial match stories, Why-Care insights, and tournament hype notes directly to your inbox for the FIFA World Cup 2026.</p>
                    <p>See you on matchday!</p>
                    <hr style="border: 0; border-top: 1px solid #e2e8f0; margin: 20px 0;">
                    <p style="font-size: 12px; color: #64748b;">You are receiving this because you signed up on MatchTales.</p>
                </div>
                """
                res = await cx.post(
                    "https://api.resend.com/emails",
                    headers={
                        "Authorization": f"Bearer {resend_key}",
                        "Content-Type": "application/json",
                    },
                    json={
                        "from": "MatchTales <onboarding@resend.dev>",
                        "to": [email],
                        "subject": "Welcome to MatchTales! ⚽",
                        "html": email_body,
                    }
                )
                if res.status_code != 200:
                    logger.error(f"Resend welcome email failed: {res.text}")
        except Exception as e:
            logger.error(f"Resend welcome email connection error: {e}")
            
    return {"ok": True, "message": "You're in! Match stories incoming.", "already": False}


# ---- Hype notes ----
@api_router.post("/hype-notes", response_model=HypeNote)
async def create_hype_note(payload: HypeNoteCreate):
    name = (payload.name or "Anonymous").strip() or "Anonymous"
    text = payload.text.strip()
    # naive profanity / spam guard placeholder (moderation hook)
    banned = ["http://", "https://", "www."]
    if any(b in text.lower() for b in banned):
        raise HTTPException(status_code=400, detail="Links aren't allowed in hype notes.")
    doc = {
        "id": str(uuid.uuid4()),
        "name": name[:40],
        "matchSlug": payload.matchSlug,
        "matchLabel": payload.matchLabel,
        "text": text,
        "likes": 0,
        "approved": True,  # moderation placeholder
        "createdAt": now_iso(),
    }
    await db.hype_notes.insert_one(doc)
    return HypeNote(**doc)


@api_router.get("/hype-notes", response_model=List[HypeNote])
async def list_hype_notes(limit: int = Query(default=30, le=100), matchSlug: Optional[str] = None):
    q = {"approved": True}
    if matchSlug:
        q["matchSlug"] = matchSlug
    notes = await db.hype_notes.find(q, {"_id": 0}).sort("createdAt", -1).to_list(limit)
    return notes


@api_router.post("/hype-notes/{note_id}/like")
async def like_hype_note(note_id: str):
    res = await db.hype_notes.update_one({"id": note_id}, {"$inc": {"likes": 1}})
    if res.matched_count == 0:
        raise HTTPException(status_code=404, detail="Hype note not found")
    note = await db.hype_notes.find_one({"id": note_id}, {"_id": 0})
    return {"ok": True, "likes": note.get("likes", 0)}


# ---- Football-Data proxy (server-side, key hidden) ----
@api_router.get("/live-scores")
async def live_scores():
    """Return matches for available competitions (mocked for manual management or real proxy)."""
    if not FOOTBALL_API_KEY:
        return {
            "competitions": [
                {
                    "id": 2001,
                    "name": "FIFA World Cup 2026",
                    "code": "WC",
                    "area": "North America",
                    "emblem": None,
                    "currentMatchday": 1
                },
                {
                    "id": 2002,
                    "name": "Premier League",
                    "code": "PL",
                    "area": "England",
                    "emblem": None,
                    "currentMatchday": 38
                },
                {
                    "id": 2003,
                    "name": "La Liga",
                    "code": "PD",
                    "area": "Spain",
                    "emblem": None,
                    "currentMatchday": 38
                }
            ],
            "fetchedAt": now_iso()
        }

    cache_key = "live_scores_comps"
    cached = cache_get(cache_key)
    if cached is not _CACHE_MISS:
        return cached

    try:
        headers = {"X-Auth-Token": FOOTBALL_API_KEY}
        async with httpx.AsyncClient() as client:
            resp = await client.get(f"{FOOTBALL_BASE}/competitions", headers=headers, timeout=10)
            if resp.status_code == 200:
                data = resp.json()
                comps = []
                for c in data.get("competitions", []):
                    comps.append({
                        "id": c.get("id"),
                        "name": c.get("name"),
                        "code": c.get("code"),
                        "area": c.get("area", {}).get("name"),
                        "emblem": c.get("emblem"),
                        "currentMatchday": c.get("currentSeason", {}).get("currentMatchday", 1)
                    })
                out = {
                    "competitions": comps,
                    "fetchedAt": now_iso()
                }
                cache_set(cache_key, out)
                return out
            else:
                logger.error(f"Error fetching comps from Football-Data: {resp.status_code} - {resp.text}")
    except Exception as e:
        logger.error(f"Exception fetching comps from Football-Data: {e}")

    return {
        "competitions": [
            {"id": 2001, "name": "FIFA World Cup 2026", "code": "WC", "area": "North America", "emblem": None, "currentMatchday": 1}
        ],
        "fetchedAt": now_iso()
    }


@api_router.get("/live-scores/{competition_code}")
async def competition_matches(competition_code: str):
    """Return matches for a competition (mocked or real proxy)."""
    if not FOOTBALL_API_KEY:
        return {
            "competition": competition_code,
            "matches": [
                {
                    "id": 1,
                    "utcDate": now_iso(),
                    "status": "IN_PLAY",
                    "matchday": 1,
                    "home": "United States",
                    "away": "Mexico",
                    "homeCrest": None,
                    "awayCrest": None,
                    "homeScore": 2,
                    "awayScore": 1
                },
                {
                    "id": 2,
                    "utcDate": now_iso(),
                    "status": "TIMED",
                    "matchday": 1,
                    "home": "Canada",
                    "away": "Honduras",
                    "homeCrest": None,
                    "awayCrest": None,
                    "homeScore": None,
                    "awayScore": None
                }
            ],
            "fetchedAt": now_iso()
        }

    cache_key = f"live_scores_matches_{competition_code}"
    cached = cache_get(cache_key)
    if cached is not _CACHE_MISS:
        return cached

    try:
        headers = {"X-Auth-Token": FOOTBALL_API_KEY}
        async with httpx.AsyncClient() as client:
            resp = await client.get(f"{FOOTBALL_BASE}/competitions/{competition_code}/matches", headers=headers, timeout=10)
            if resp.status_code == 200:
                data = resp.json()
                matches = []
                for m in data.get("matches", []):
                    matches.append({
                        "id": m.get("id"),
                        "utcDate": m.get("utcDate"),
                        "status": m.get("status"),
                        "matchday": m.get("matchday"),
                        "home": m.get("homeTeam", {}).get("name"),
                        "away": m.get("awayTeam", {}).get("name"),
                        "homeCrest": m.get("homeTeam", {}).get("crest"),
                        "awayCrest": m.get("awayTeam", {}).get("crest"),
                        "homeScore": m.get("score", {}).get("fullTime", {}).get("home"),
                        "awayScore": m.get("score", {}).get("fullTime", {}).get("away"),
                    })
                out = {
                    "competition": competition_code,
                    "matches": matches,
                    "fetchedAt": now_iso()
                }
                cache_set(cache_key, out)
                return out
            else:
                logger.error(f"Error fetching matches from Football-Data: {resp.status_code} - {resp.text}")
    except Exception as e:
        logger.error(f"Exception fetching matches from Football-Data: {e}")

    return {
        "competition": competition_code,
        "matches": [],
        "fetchedAt": now_iso()
    }



# ---- Match poll (second-screen) ----
class PollVote(BaseModel):
    matchSlug: str
    option: str  # 'home' | 'draw' | 'away'


@api_router.post("/poll/vote")
async def poll_vote(vote: PollVote):
    if vote.option not in ("home", "draw", "away"):
        raise HTTPException(status_code=400, detail="Invalid option")
    await db.polls.update_one(
        {"matchSlug": vote.matchSlug},
        {"$inc": {f"votes.{vote.option}": 1}},
        upsert=True,
    )
    doc = await db.polls.find_one({"matchSlug": vote.matchSlug}, {"_id": 0})
    return {"ok": True, "votes": doc.get("votes", {})}


@api_router.get("/poll/{matchSlug}")
async def poll_results(matchSlug: str):
    doc = await db.polls.find_one({"matchSlug": matchSlug}, {"_id": 0})
    votes = (doc or {}).get("votes", {})
    return {"matchSlug": matchSlug, "votes": {"home": votes.get("home", 0), "draw": votes.get("draw", 0), "away": votes.get("away", 0)}}


app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=False,
    allow_origins=os.environ.get('CORS_ORIGINS', '*').split(','),
    allow_methods=["*"],
    allow_headers=["*"],
)




# ---- Automation Endpoints & Background Loop ----
async def run_automation_loop():
    interval_mins = int(os.environ.get("AUTOMATION_INTERVAL_MINUTES", "30"))
    interval_seconds = interval_mins * 60
    logger.info(f"Background automation loop started. Runs every {interval_mins} minutes.")
    
    script_name = "daily_automated_run.py" if os.environ.get("AUTOMATION_TYPE", "daily") == "daily" else "automate_updates.py"
    script_path = get_script_path(script_name)
    
    while True:
        await asyncio.sleep(interval_seconds)
        try:
            logger.info(f"Executing scheduled periodic MatchTales updates using {script_name}...")
            cmd = [sys.executable, script_path, "--write"]
            if os.environ.get("AUTO_COMMIT") == "true":
                cmd.append("--commit")
            
            process = await asyncio.create_subprocess_exec(
                *cmd,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            stdout, stderr = await process.communicate()
            if process.returncode == 0:
                logger.info(f"Scheduled updates completed successfully:\n{stdout.decode('utf-8', errors='ignore')}")
            else:
                logger.error(f"Scheduled updates failed (code {process.returncode}):\n{stderr.decode('utf-8', errors='ignore')}")
        except Exception as e:
            logger.error(f"Exception in scheduled updates: {e}")


@api_router.post("/automate/trigger")
async def trigger_automation():
    """Manually trigger the sync and content generation (standard API scores)."""
    script_path = get_script_path("automate_updates.py")
    cmd = [sys.executable, script_path, "--write"]
    if os.environ.get("AUTO_COMMIT") == "true":
        cmd.append("--commit")
        
    try:
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        out_log = stdout.decode('utf-8', errors='ignore')
        err_log = stderr.decode('utf-8', errors='ignore')
        
        if process.returncode == 0:
            return {"ok": True, "message": "Automation triggered successfully", "output": out_log}
        else:
            raise HTTPException(status_code=500, detail={
                "message": f"Automation script failed with exit code {process.returncode}",
                "error": err_log,
                "output": out_log
            })
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to execute automation script: {str(e)}")


@api_router.post("/automate/daily-run")
async def trigger_daily_run():
    """Manually trigger the daily web scraping and newsletter run."""
    script_path = get_script_path("daily_automated_run.py")
    cmd = [sys.executable, script_path, "--write"]
    if os.environ.get("AUTO_COMMIT") == "true":
        cmd.append("--commit")
        
    try:
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        out_log = stdout.decode('utf-8', errors='ignore')
        err_log = stderr.decode('utf-8', errors='ignore')
        
        if process.returncode == 0:
            return {"ok": True, "message": "Daily automation run triggered successfully", "output": out_log}
        else:
            raise HTTPException(status_code=500, detail={
                "message": f"Daily automation script failed with exit code {process.returncode}",
                "error": err_log,
                "output": out_log
            })
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to execute daily automation script: {str(e)}")


@app.on_event("startup")
async def startup_event():
    if os.environ.get("AUTOMATION_ENABLED") == "true":
        asyncio.create_task(run_automation_loop())


@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()

