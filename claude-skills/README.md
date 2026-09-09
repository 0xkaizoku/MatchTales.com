# Claude Code Skills

My personal `~/.claude/skills` directory, under version control.

Clone into place and the skills are live — Claude Code reads this directory directly.

```bash
git clone <this-repo> ~/.claude/skills
cd ~/.claude/skills
./bootstrap.sh
```

## Skills

### Design & frontend
| Skill | What it does |
|---|---|
| `tastemaker`† | Generate on-brand UI instead of generic AI slop |
| `apple-design` | Apple's interface and motion principles, translated for the web |
| `emil-design-eng` | Emil Kowalski's philosophy on UI polish and component design |
| `prototype` | Build several genuinely different versions of a UI piece, side by side |
| `pick-ui-library` | Pick the right library for a frontend task from a curated list |

### Animation
| Skill | What it does |
|---|---|
| `animation-vocabulary` | Reverse-lookup glossary: describe a motion effect, get its real name |
| `find-animation-opportunities` | Find places in a UI that should animate but don't |
| `improve-animations` | Audit a codebase's motion and produce a prioritized roadmap |
| `review-animations` | Review animation code against a high craft bar |

### SEO
| Skill | What it does |
|---|---|
| `seo` | The umbrella skill — full audits, technical checks, schema, GEO |
| `seo-audit` | Full-site audit with parallel subagent delegation |
| `seo-page` | Deep single-page analysis |
| `seo-technical` | Crawlability, indexability, security, Core Web Vitals |
| `seo-content` | Content quality and E-E-A-T |
| `seo-schema` | Detect, validate, and generate Schema.org JSON-LD |
| `seo-geo` | Optimize for AI Overviews, ChatGPT, Perplexity citations |
| `seo-local` | Google Business Profile, NAP consistency, map pack |
| `seo-sitemap` | Analyze or generate XML sitemaps |
| `seo-images` | Alt text, file sizes, formats, lazy loading, CLS |
| `seo-image-gen` | Generate OG/social/hero images for SEO assets |
| `seo-hreflang` | Hreflang and international SEO |
| `seo-programmatic` | Pages generated at scale from data sources |
| `seo-competitor-pages` | "X vs Y" and "alternatives to X" pages |
| `seo-dataforseo` | Live SERP, keyword, and backlink data via DataForSEO |
| `seo-plan` | Strategy, site architecture, content roadmap |

### Writing & research
| Skill | What it does |
|---|---|
| `humanize` | Strip AI-writing tells from prose (41 detected patterns) |
| `sub-reddit-finder`† | Find and vet subreddits to market a product in |
| `learn-ai-faster`† | Build a personalized AI learning path from curated tutorials |

### Engineering & media
| Skill | What it does |
|---|---|
| `systematic-debugging` | Structured debugging before proposing fixes |
| `web-asset-generator` | Favicons, PWA icons, Open Graph images |
| `video-use`† | Edit video by conversation — transcribe, cut, grade, subtitle |

† Lives in its own upstream repo. Not vendored here — `./bootstrap.sh` clones it.

## Not in this repo

**`my-voice`** — personal writing-voice rules, deliberately excluded.

**Plugin skills** — installed from marketplaces, not files I own. Reinstall with:

```bash
claude plugin install marketing-skills@marketingskills
claude plugin install telegram@claude-plugins-official
```

**Virtualenvs** — 521 MB of the original 524 MB was `.venv`. Two skills need one:

```bash
cd seo && python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
```

`video-use` uses `uv sync` and needs its own `.env` (see its `.env.example`).

## Layout

Each skill is a directory with a `SKILL.md` carrying YAML frontmatter (`name`,
`description`) plus a body of instructions. Some add `references/`, `scripts/`,
`assets/`, or `hooks/`. Claude Code loads the frontmatter at startup and pulls
the body in only when a skill actually fires.

## Credits

This is a personal collection, not original work. Most of these skills were
written by other people and are collected here as I actually use them.

- `humanize` — MIT © aasha (license retained in `humanize/LICENSE`)
- `tastemaker` — [codeswithroh/tastemaker](https://github.com/codeswithroh/tastemaker)
- `learn-ai-faster` — [aashaexo/learn-ai-faster](https://github.com/aashaexo/learn-ai-faster)
- `video-use` — [browser-use/video-use](https://github.com/browser-use/video-use)
- The SEO suite and the design/animation skills ship without license metadata;
  they are included as-is and remain the property of their original authors.

If you wrote one of these and want it removed or credited differently, open an
issue and I'll fix it.
