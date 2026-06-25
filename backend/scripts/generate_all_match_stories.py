import os
import json
import argparse
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
SEED_PATH = ROOT_DIR / "frontend" / "src" / "data" / "seed.json"
MATCH_DIR = ROOT_DIR / "frontend" / "src" / "content" / "matches"
STORY_DIR = ROOT_DIR / "frontend" / "src" / "content" / "stories"

def clean_text(text: str) -> str:
    if not text:
        return ""
    # Standardize spaces around hyphens and replace em-dashes and double hyphens
    return text.replace("—", " - ").replace("--", " - ")

def main():
    parser = argparse.ArgumentParser(description="Generate all match stories from match JSON files")
    parser.add_argument("--force", action="store_true", help="Overwrite existing story files")
    args = parser.parse_args()

    if not SEED_PATH.exists():
        print(f"Error: seed.json not found at {SEED_PATH}")
        return

    try:
        seed_data = json.loads(SEED_PATH.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"Error parsing seed.json: {e}")
        return

    # Find the corresponding story metadata image mapping
    story_meta_by_slug = {s["slug"]: s for s in seed_data.get("storiesMeta", [])}

    fixtures = seed_data.get("fixtures", [])
    print(f"Found {len(fixtures)} fixtures in seed.json.")

    generated_count = 0
    skipped_count = 0

    for fixture in fixtures:
        slug = fixture["slug"]
        story_slug = f"{slug}-story"
        match_json_path = MATCH_DIR / f"{slug}.json"
        story_md_path = STORY_DIR / f"{story_slug}.md"

        PRESERVED_SLUGS = [
            "spain-vs-norway-md3-story",
            "japan-vs-costa-rica-md3-story",
            "italy-vs-egypt-md3-story",
            "turkey-vs-paraguay-md3-story",
            "france-vs-qatar-md3-story",
            "uruguay-vs-dr-congo-md3-story",
            "brazil-vs-ecuador-md3-story",
            "switzerland-vs-cameroon-md3-story",
            "portugal-vs-new-zealand-md3-story",
            "ivory-coast-vs-serbia-md3-story",
            "algeria-vs-jamaica-md3-story",
            "germany-vs-iraq-md3-story"
        ]
        if story_slug in PRESERVED_SLUGS:
            skipped_count += 1
            continue

        if story_md_path.exists() and not args.force:
            skipped_count += 1
            continue

        if not match_json_path.exists():
            print(f"Warning: match JSON not found for {slug} at {match_json_path}")
            continue

        try:
            match_data = json.loads(match_json_path.read_text(encoding="utf-8"))
        except Exception as e:
            print(f"Error parsing match JSON {slug}: {e}")
            continue

        # Get the Unsplash image from seed storyMeta if available, otherwise fallback
        meta_entry = story_meta_by_slug.get(story_slug, {})
        image_url = meta_entry.get("img", "https://images.unsplash.com/photo-1550591927-391fccf9934b?crop=entropy&cs=srgb&fm=jpg&q=85")

        # Formulate variables
        home = match_data.get("home", fixture["home"])
        away = match_data.get("away", fixture["away"])
        date = match_data.get("date", fixture["date"])
        venue = match_data.get("venue", fixture["venue"])
        city = match_data.get("city", fixture["city"])
        
        headline = clean_text(match_data.get("headline", f"{home} vs {away} Match Report"))
        teaser = clean_text(match_data.get("teaser", ""))
        why_care_reason = clean_text(match_data.get("whyCareReason", ""))
        story_body = clean_text(match_data.get("story", ""))
        stakes = clean_text(match_data.get("stakes", ""))
        rivalry_angle = clean_text(match_data.get("rivalryAngle", ""))
        head_to_head = clean_text(match_data.get("headToHead", ""))
        fun_facts = [clean_text(f) for f in match_data.get("funFacts", [])]
        key_players = match_data.get("keyPlayers", [])

        h2h_section = f"### Head-to-Head History\n\n{head_to_head}" if head_to_head else ""
        body_content = f"""## The Showdown at {venue}

On {date}, the footballing world turned its attention to the {venue} in {city} for a memorable group stage encounter between **{home}** and **{away}**. {why_care_reason}

{story_body}

## Stakes & Context

{stakes}

{rivalry_angle}

{h2h_section}

## Key Player Impacts

The match was defined by individual battles and standout performances from:
"""
        for player in key_players:
            p_name = clean_text(player.get("name", ""))
            p_team = clean_text(player.get("team", ""))
            p_hook = clean_text(player.get("hook", ""))
            body_content += f"- **{p_name}** ({p_team}): {p_hook}\n"

        if fun_facts:
            body_content += "\n## Match Facts\n\n"
            for fact in fun_facts:
                body_content += f"- {fact}\n"

        # Formulate YAML frontmatter
        fm = (
            "---\n"
            f"title: {json.dumps(headline)}\n"
            f"subtitle: {json.dumps(teaser)}\n"
            f"category: \"Match Report\"\n"
            f"excerpt: {json.dumps(why_care_reason)}\n"
            f"image: {json.dumps(image_url)}\n"
            f"readingTime: 4\n"
            f"pubDate: {date}\n"
            "---\n\n"
        )

        story_md_path.write_text(fm + body_content, encoding="utf-8")
        generated_count += 1

    print(f"Stories generation completed. Generated: {generated_count}, Skipped: {skipped_count}")

if __name__ == "__main__":
    main()
