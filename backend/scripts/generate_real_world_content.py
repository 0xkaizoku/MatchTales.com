import os
import json
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
FE = ROOT / "frontend" / "src"
SEED_FILE = FE / "data" / "seed.json"

MATCH_DIR = FE / "content" / "matches"
STORY_DIR = FE / "content" / "stories"
TEAM_DIR = FE / "content" / "teams"

# Make sure folders exist
for d in (MATCH_DIR, STORY_DIR, TEAM_DIR):
    d.mkdir(parents=True, exist_ok=True)

# Helper function to remove em-dashes and double hyphens
def clean_style(text: str) -> str:
    if not text:
        return ""
    # Replace em-dash with a clean space-hyphen-space
    text = text.replace("—", " - ")
    # Replace double-hyphen with a single hyphen
    text = text.replace("--", "-")
    return text

def main():
    print(f"Loading seed data from {SEED_FILE}...")
    if not SEED_FILE.exists():
        raise FileNotFoundError(f"seed.json not found at {SEED_FILE}")
        
    seed = json.loads(SEED_FILE.read_text(encoding="utf-8"))
    
    # 1. Clear old match files
    print("Clearing old match files in content/matches...")
    for f in MATCH_DIR.glob("*.json"):
        f.unlink()
        
    # 2. Clear old team dossiers in content/teams
    print("Clearing old team files in content/teams...")
    for f in TEAM_DIR.glob("*.json"):
        f.unlink()
        
    # 3. Clear only match stories in content/stories (keeping generic editorial markdown)
    print("Clearing old match-story files in content/stories...")
    for f in STORY_DIR.glob("*-story.md"):
        f.unlink()

    # Build maps
    teams_map = {t["name"]: t for t in seed["teams"]}
    stories_meta_map = {s["slug"]: s for s in seed["storiesMeta"]}
    
    # 4. Generate 48 team dossiers
    print("Generating 48 team dossiers...")
    for t in seed["teams"]:
        slug = t["slug"]
        name = t["name"]
        nick = t["nick"]
        rank = t["rank"]
        conf = t["conf"]
        best = t["best"]
        titles = t["titles"]
        fun_fact = t["funFact"]
        story_brief = t["story"]
        
        players_list = t["keyPlayers"]
        p1 = players_list[0][0] if len(players_list) > 0 else "Star Player"
        p1_pos = players_list[0][1] if len(players_list) > 0 else "Forward"
        p2 = players_list[1][0] if len(players_list) > 1 else "Key Midfielder"
        
        dossier = (
            f"The {name} national football team, affectionately known to their passionate supporters as the {nick}, "
            f"enter the FIFA World Cup 2026 with high expectations. Currently ranked number {rank} in the world, "
            f"they bring a unique tactical identity and style from {conf} to this expanded 48-team tournament.\n\n"
            f"{story_brief}\n\n"
            f"With the tournament co-hosted across the United States, Mexico, and Canada, {name} will count on "
            f"their travelling support to create a vibrant atmosphere. Their primary objective will be to make a statement "
            f"in Group {t['group']} and navigate their way to the high-stakes knockout rounds."
        )
        
        what_to_watch = f"Keep a close eye on their transition play in Group {t['group']}. The connection between {p1} and {p2} is crucial to their attacking spark."
        x_factor = f"{p1} - the clinical {p1_pos.lower()} who holds the ability to turn a match on its head with a single moment of magic."
        verdict = f"{name} are poised to be one of the most intriguing stories of the group stage, bringing great energy to the tournament."
        
        team_data = {
            "slug": slug,
            "name": name,
            "dossier": clean_style(dossier),
            "whatToWatch": clean_style(what_to_watch),
            "xFactor": clean_style(x_factor),
            "verdict": clean_style(verdict),
            "funFacts": [clean_style(fun_fact), f"{name} boast {titles} World Cup titles in their historical cabinet, with their best tournament finish being {best}."]
        }
        
        out_file = TEAM_DIR / f"{slug}.json"
        out_file.write_text(json.dumps(team_data, ensure_ascii=False, indent=2), encoding="utf-8")

    # 5. Generate 72 match packages & match story markdowns
    print("Generating 72 matches and match stories...")
    for f in seed["fixtures"]:
        slug = f["slug"]
        home = f["home"]
        away = f["away"]
        group = f["group"]
        md = f["matchday"]
        date = f["date"]
        time = f["time"]
        venue = f["venue"]
        city = f["city"]
        status = f["status"]
        hs = f["homeScore"]
        as_ = f["awayScore"]
        marquee = f.get("marquee", False)
        live_minute = f.get("liveMinute")
        
        h_team = teams_map.get(home, {})
        a_team = teams_map.get(away, {})
        
        h_nick = h_team.get("nick", "the underdogs")
        a_nick = a_team.get("nick", "the favorites")
        
        h_players = h_team.get("keyPlayers", [])
        a_players = a_team.get("keyPlayers", [])
        
        p_home = h_players[0][0] if len(h_players) > 0 else "Star Player"
        p_away = a_players[0][0] if len(a_players) > 0 else "Key Midfielder"
        
        # Determine score description if finished or live
        score_desc = ""
        if status in ("FINISHED", "LIVE"):
            score_desc = f" {hs}-{as_}"
            
        # 1. Headline
        h_val = int(hashlib.md5(slug.encode("utf-8")).hexdigest(), 16)
        if status == "FINISHED":
            if hs > as_:
                headlines = [
                    f"{home} Secure Crucial{score_desc} Win Over {away}",
                    f"Triumph for {home} in Tense{score_desc} Battle",
                    f"{home} Outclass {away} in{score_desc} Victory",
                    f"Late Drama Sees {home} Beat {away}{score_desc}"
                ]
            elif as_ > hs:
                headlines = [
                    f"{away} Grab Dramatic{score_desc} Win Against {home}",
                    f"{away} Outclass {home} in{score_desc} Triumph",
                    f"Crucial Away Win for {away} over {home}{score_desc}",
                    f"Tactical Masterclass Sees {away} Beat {home}{score_desc}"
                ]
            else:
                headlines = [
                    f"{home} and {away} Share Spoils in{score_desc} Draw",
                    f"Tense{score_desc} Stalemate Between {home} and {away}",
                    f"Points Shared in Drama-Filled{score_desc} Draw",
                    f"Deadlock Unbroken as {home} Draws {away}{score_desc}"
                ]
            headline = headlines[h_val % len(headlines)]
        elif status == "LIVE":
            headline = f"LIVE: {home} vs {away} In-Play ({hs}-{as_})"
        else:
            headlines = [
                f"Anticipation Builds for {home} vs {away} Clash",
                f"{home} and {away} Set for Group {group} Showdown",
                f"High Stakes in {city} as {home} Meets {away}",
                f"Tactical Duel Awaits in {home} vs {away}"
            ]
            headline = headlines[h_val % len(headlines)]
            
        # 2. Why Care Reason
        if status == "FINISHED":
            why_care = f"A crucial group stage result in Group {group} that leaves standing tables dramatically altered."
        elif status == "LIVE":
            why_care = f"This high-stakes Group {group} match is currently live with qualification hopes hanging in the balance."
        else:
            why_care = f"A highly anticipated Matchday {md} clash in Group {group} with significant tournament implications."
            
        # 3. Teaser
        if status == "FINISHED":
            teasers = [
                f"The final whistle blew at {venue} with a {hs}-{as_} scoreline. {home} and {away} played out an absorbing contest that will shape the Group {group} standings.",
                f"A thrilling match in {city} concludes with {home} and {away} leaving everything on the pitch. Read the full post-match analysis.",
                f"Tactical discipline and clinical finishes defined this Matchday {md} encounter. Here is how {home} and {away} fought out their group stage clash."
            ]
            teaser = teasers[h_val % len(teasers)]
        elif status == "LIVE":
            teaser = f"Live from {venue} in {city}, the action between {home} and {away} is heating up. Follow the updates as Group {group} qualification is on the line."
        else:
            teasers = [
                f"The stage is set in {city} for a massive clash between {home} and {away}. Both nations are hungry for three points to boost their knockout dreams.",
                f"A fascinating encounter awaits at {venue} on Matchday {md}. Can {home} overcome the tactical setup of {away} to secure a crucial win?",
                f"With Group {group} wide open, both {home} and {away} view this fixture as a must-win game. Here is what to watch for."
            ]
            teaser = teasers[h_val % len(teasers)]
            
        # 4. Story paragraphs
        if status == "FINISHED":
            p1_options = [
                f"The atmosphere at the {venue} in {city} was electric as {home} faced {away} in a Group {group} matchup on {date}. Fans of both teams created a sea of colour and noise, setting the stage for a memorable World Cup showdown.",
                f"Under the bright lights in {city}, {home} and {away} took to the pitch on {date} for a highly anticipated Matchday {md} fixture. The tension in the stadium was palpable, reflecting the immense stakes of the tournament."
            ]
            p2_options = [
                f"The match was defined by intense tactical battles in midfield and clinical finishing. {home} relied heavily on the technical qualities of {p_home} to dictate the tempo. On the other side, {away} looked dangerous on the counter, with {p_away} asking serious questions of the opposition defence. The scoreline of {hs} to {as_} highlights how closely contested the affair was.",
                f"With both managers deploying disciplined defensive setups, space was at a premium. {p_home} showed moments of brilliance for {home}, while {p_away} was the creative heartbeat for {away}. In the end, a few decisive moments settled the score at {hs}-{as_}, giving fans plenty to talk about."
            ]
            p3_options = [
                f"As the final whistle blew, the players collapsed in exhaustion, having left everything on the grass. This result will have major ramifications for Group {group} standings, making the upcoming fixtures even more critical for both nations.",
                f"For the victors, this result represents a massive step toward the knockout rounds. For the defeated, it is back to the drawing board to save their World Cup campaign before the group stage concludes."
            ]
        elif status == "LIVE":
            p1_options = [
                f"The action is currently live at the {venue} in {city}, where {home} and {away} are locked in a fierce Group {group} encounter. The energy in the stadium is sky-high as supporters push their teams forward.",
                f"We are in the midst of a gripping Matchday {md} clash in {city}. {home} and {away} are battling for every ball, with the current score standing at {hs} to {as_}."
            ]
            p2_options = [
                f"Both sides have refused to back down in this physical battle. {p_home} is leading the charge for {home}, showcase outstanding speed and control. Meanwhile, {p_away} is orchestrating play in the center for {away}, looking for the killer pass to break the deadlock.",
                f"With qualification on the line, the tactical adjustments from both benches have been constant. {home} are searching for pathways through the defensive lines using {p_home}, while {away} are hitting back with quick transitions led by {p_away}."
            ]
            p3_options = [
                f"As the clock ticks down, the tension is reaching a fever pitch. A single mistake or a moment of individual magic could decide the destiny of both nations in this Group {group} campaign.",
                f"Every second counts now. Both teams know that securing three points here will dramatically improve their chances of advancing to the next round."
            ]
        else:
            p1_options = [
                f"Anticipation is building ahead of the Matchday {md} fixture between {home} and {away} at the {venue} in {city}. Both teams are finalized their preparations for this critical Group {group} showdown.",
                f"Football fans around the world are looking forward to {date}, when {home} and {away} will go head-to-head in {city}. The match promises to be a showcase of tactical discipline and individual skill."
            ]
            p2_options = [
                f"Tactical matchups across the pitch will define the contest. {home} will rely on their talisman {p_home} to unlock the opposition's defensive block, while {away} will look to their key playmaker {p_away} to establish control in the midfield. Both managers have kept their cards close to their chest in the pre-match press conferences.",
                f"The clash of styles makes this game particularly intriguing. The structural discipline of {home} will be tested by the fluid attacking movements of {away}, with {p_home} and {p_away} expected to play central roles in their respective strategies."
            ]
            p3_options = [
                f"With only three matches in the group phase, there is no margin for error. A strong performance in this fixture will set a positive tone for the rest of the tournament.",
                f"The fans are already gathering in {city}, creating a wonderful festival atmosphere. Regardless of the outcome, this promises to be a classic chapter in their footballing history."
            ]
            
        p1 = p1_options[h_val % len(p1_options)]
        p2 = p2_options[h_val % len(p2_options)]
        p3 = p3_options[h_val % len(p3_options)]
        story = f"{p1}\n\n{p2}\n\n{p3}"
        
        # 5. Stakes
        stakes = f"With Group {group} wide open, this matchday {md} encounter holds massive implications for both {home} and {away} as they look to secure a place in the knockout rounds."
        
        # 6. Rivalry Angle
        rivalry_angle = f"The footballing connection between {home} and {away} adds an extra layer of emotion to this fixture, making it a must-watch for fans."
        
        # 7. Head to Head
        h2h = f"Historically, matches between these two nations have always been tightly contested affairs, with tactical discipline proving key."
        
        # 8. Fun Facts
        facts = [
            f"{home} are affectionately known as the {h_nick}.",
            f"{away} are affectionately known as the {a_nick}.",
            f"This high-profile match was held at {venue} in {city} on {date}."
        ]
        
        # Write JSON match package
        match_json = {
            "slug": slug,
            "headline": clean_style(headline),
            "whyCareScore": 9.2 if marquee else 7.4,
            "whyCareReason": clean_style(why_care),
            "teaser": clean_style(teaser),
            "story": clean_style(story),
            "stakes": clean_style(stakes),
            "rivalryAngle": clean_style(rivalry_angle),
            "funFacts": [clean_style(f) for f in facts],
            "keyPlayers": [
                {"name": p_home, "team": home, "hook": f"The key playmaker leading the tactical setup for the {h_nick}."},
                {"name": p_away, "team": away, "hook": f"The creative spark expected to make the difference for the {a_nick}."}
            ],
            "headToHead": clean_style(h2h),
            "tags": [home.lower().replace(" ", "-"), away.lower().replace(" ", "-"), f"group-{group.lower()}"],
            "home": home,
            "away": away,
            "homeCode": h_team.get("code"),
            "awayCode": a_team.get("code"),
            "homeFlag": h_team.get("flag"),
            "awayFlag": a_team.get("flag"),
            "group": group,
            "matchday": md,
            "date": date,
            "time": time,
            "venue": venue,
            "city": city,
            "status": status,
            "homeScore": hs,
            "awayScore": as_,
            "marquee": marquee,
            "liveMinute": live_minute
        }
        
        json_out = MATCH_DIR / f"{slug}.json"
        json_out.write_text(json.dumps(match_json, ensure_ascii=False, indent=2), encoding="utf-8")
        
        # Write Markdown match story
        story_meta = stories_meta_map.get(f"{slug}-story", {
            "title": headline,
            "category": "Match Report",
            "excerpt": why_care,
            "img": "https://images.unsplash.com/photo-1550591927-391fccf9934b?crop=entropy&cs=srgb&fm=jpg&q=85",
            "read": 4
        })
        
        title_val = clean_style(story_meta["title"])
        subtitle_val = clean_style(teaser)
        category_val = clean_style(story_meta["category"])
        excerpt_val = clean_style(why_care)
        img_val = story_meta["img"]
        read_val = story_meta["read"]
        
        markdown_body = (
            f"---\n"
            f"title: {json.dumps(title_val)}\n"
            f"subtitle: {json.dumps(subtitle_val)}\n"
            f"category: {json.dumps(category_val)}\n"
            f"excerpt: {json.dumps(excerpt_val)}\n"
            f"image: {json.dumps(img_val)}\n"
            f"readingTime: {read_val}\n"
            f"pubDate: {date}\n"
            f"---\n\n"
            f"## The Showdown at {venue}\n\n"
            f"On {date}, the footballing world turned its attention to {venue} in {city} for an absorbing encounter between **{home}** and **{away}** in Group {group}.\n\n"
            f"{clean_style(story)}\n\n"
            f"## Stakes and Context\n\n"
            f"{clean_style(stakes)}\n\n"
            f"{clean_style(rivalry_angle)}\n\n"
            f"### Head-to-Head History\n\n"
            f"{clean_style(h2h)}\n\n"
            f"## Key Player Impacts\n\n"
            f"The match was defined by individual battles and standout performances from:\n"
            f"- **{p_home}** ({home}): The key playmaker leading the tactical setup for the {h_nick}.\n"
            f"- **{p_away}** ({away}): The creative spark expected to make the difference for the {a_nick}.\n\n"
            f"## Match Facts\n\n"
            f"- {clean_style(facts[0])}\n"
            f"- {clean_style(facts[1])}\n"
            f"- {clean_style(facts[2])}\n"
        )
        
        story_out = STORY_DIR / f"{slug}-story.md"
        story_out.write_text(markdown_body, encoding="utf-8")

    # 6. Clean style on the 7 generic stories
    print("Formatting the 7 generic stories for style compliance...")
    generic_slugs = [
        "greatest-world-cup-upsets",
        "the-last-dance-modric-ronaldo-messi",
        "why-the-48-team-world-cup-changes-everything",
        "hosts-united-usa-mexico-canada",
        "lamine-yamal-new-tiki-taka",
        "norways-golden-duo-haaland-odegaard",
        "african-heavyweights-senegal-morocco"
    ]
    
    for slug in generic_slugs:
        f = STORY_DIR / f"{slug}.md"
        if f.exists():
            text = f.read_text(encoding="utf-8")
            # Separate frontmatter and body to apply clean_style only to the body and title lines, not YAML markers
            parts = text.split("---")
            if len(parts) >= 3:
                frontmatter = parts[1]
                body = "---".join(parts[2:])
                
                # clean frontmatter lines individually
                fm_lines = []
                for line in frontmatter.splitlines():
                    if line.startswith("title:") or line.startswith("subtitle:") or line.startswith("excerpt:"):
                        fm_lines.append(clean_style(line))
                    else:
                        fm_lines.append(line)
                frontmatter_cleaned = "\n".join(fm_lines)
                
                body_cleaned = clean_style(body)
                new_text = "---\n" + frontmatter_cleaned.strip() + "\n---\n" + body_cleaned.lstrip()
                f.write_text(new_text, encoding="utf-8")
                print(f"  Cleaned {f.name}")
            else:
                f.write_text(clean_style(text), encoding="utf-8")
                print(f"  Cleaned {f.name} (no frontmatter split)")
                
    print("\nContent generation complete!")

if __name__ == "__main__":
    main()
