{
  "product": {
    "name": "MatchTales",
    "positioning": "Contextual match storyteller and Why Care hub across soccer, tennis, golf, football, basketball and Formula 1, with a complete World Cup 2026 archive",
    "brand_attributes": [
      "editorial",
      "premium",
      "emotional",
      "fast",
      "minimal",
      "shareable",
      "trustworthy"
    ],
    "north_star_actions": [
      "Open a match and understand why it matters in <30 seconds",
      "Share a viral match card to social",
      "Follow a team storyline across the tournament",
      "Use Live second-screen mode during matches"
    ]
  },

  "visual_personality": {
    "style_fusion": [
      "The Athletic-like editorial reading experience (text-first, calm, premium)",
      "Modern startup minimalism (Vercel-ish spacing, crisp borders, fast UI)",
      "Football pitch cues (deep greens used as accents, not as a wash)",
      "Card-heavy bento grids for scannability"
    ],
    "do_not": [
      "Do not make it scoreboard-first",
      "Do not use loud gradients or neon greens across large areas",
      "Do not center-align the whole app",
      "Do not use purple for AI/chat vibes"
    ]
  },

  "design_tokens": {
    "implementation": {
      "astro_tailwind": "Use CSS variables for tokens in :root and [data-theme='dark'] (or .dark). Tailwind should reference tokens via arbitrary values like bg-[hsl(var(--bg))].",
      "dark_mode": "Toggle sets data-theme on <html> (preferred) and persists in localStorage. Respect prefers-color-scheme on first load."
    },

    "colors": {
      "note": "HSL tokens are recommended for Tailwind + alpha control. Hex provided for reference.",
      "light": {
        "bg": { "hsl": "40 33% 98%", "hex": "#FBFAF7", "usage": "page background (paper)" },
        "fg": { "hsl": "220 18% 12%", "hex": "#171C24", "usage": "primary text" },
        "surface": { "hsl": "0 0% 100%", "hex": "#FFFFFF", "usage": "cards" },
        "surface_2": { "hsl": "40 20% 96%", "hex": "#F5F2EC", "usage": "subtle panels, table header" },
        "border": { "hsl": "220 14% 88%", "hex": "#DCE1EA", "usage": "hairline borders" },
        "muted": { "hsl": "220 10% 45%", "hex": "#6B7280", "usage": "secondary text" },

        "pitch": { "hsl": "158 42% 22%", "hex": "#1F4D3D", "usage": "brand anchor (sparingly)" },
        "pitch_2": { "hsl": "156 38% 30%", "hex": "#2F6B55", "usage": "hover/active states" },
        "accent_lime": { "hsl": "84 78% 45%", "hex": "#7ED321", "usage": "small highlights only (badges, dots)" },
        "accent_coral": { "hsl": "14 86% 60%", "hex": "#F26B4F", "usage": "stakes/heat moments" },
        "accent_sky": { "hsl": "198 88% 45%", "hex": "#12A4E6", "usage": "links, info" },

        "success": { "hsl": "156 55% 34%", "hex": "#2A7A5E" },
        "warning": { "hsl": "38 92% 52%", "hex": "#F5A524" },
        "danger": { "hsl": "0 78% 55%", "hex": "#E5484D" },

        "focus_ring": { "hsl": "198 88% 45%", "hex": "#12A4E6", "usage": "focus outline" }
      },

      "dark": {
        "bg": { "hsl": "220 18% 8%", "hex": "#0F141C", "usage": "page background" },
        "fg": { "hsl": "0 0% 98%", "hex": "#FAFAFA", "usage": "primary text" },
        "surface": { "hsl": "220 18% 11%", "hex": "#141B25", "usage": "cards" },
        "surface_2": { "hsl": "220 16% 14%", "hex": "#1A2230", "usage": "subtle panels" },
        "border": { "hsl": "220 14% 22%", "hex": "#2B3444", "usage": "hairline borders" },
        "muted": { "hsl": "220 10% 70%", "hex": "#A7B0BF", "usage": "secondary text" },

        "pitch": { "hsl": "156 45% 38%", "hex": "#2F8A6A", "usage": "brand anchor (sparingly)" },
        "pitch_2": { "hsl": "156 55% 44%", "hex": "#33A07A", "usage": "hover/active" },
        "accent_lime": { "hsl": "84 78% 45%", "hex": "#7ED321", "usage": "small highlights" },
        "accent_coral": { "hsl": "14 86% 60%", "hex": "#F26B4F" },
        "accent_sky": { "hsl": "198 88% 55%", "hex": "#2BB7F5" },

        "success": { "hsl": "156 55% 44%", "hex": "#33A07A" },
        "warning": { "hsl": "38 92% 58%", "hex": "#FFB224" },
        "danger": { "hsl": "0 78% 60%", "hex": "#F2555A" },

        "focus_ring": { "hsl": "198 88% 55%", "hex": "#2BB7F5" }
      },

      "semantic": {
        "why_care_scale": {
          "0_3": "muted (low stakes)",
          "3_6": "accent_sky (interesting)",
          "6_8": "pitch_2 (big)",
          "8_10": "accent_coral (must-watch)"
        }
      }
    },

    "gradients_and_texture": {
      "allowed_usage": "Only as section background accents (hero top band, not reading areas). Keep under 20% viewport.",
      "hero_bg_gradient": {
        "css": "radial-gradient(900px circle at 20% 10%, hsla(var(--pitch)/0.18), transparent 55%), radial-gradient(700px circle at 80% 0%, hsla(var(--accent-sky)/0.14), transparent 52%)",
        "note": "Mild, airy, no saturated purple/pink."
      },
      "noise_overlay": {
        "css": "background-image: url('data:image/svg+xml,%3Csvg xmlns=\"http://www.w3.org/2000/svg\" width=\"120\" height=\"120\"%3E%3Cfilter id=\"n\"%3E%3CfeTurbulence type=\"fractalNoise\" baseFrequency=\"0.9\" numOctaves=\"3\" stitchTiles=\"stitch\"/%3E%3C/filter%3E%3Crect width=\"120\" height=\"120\" filter=\"url(%23n)\" opacity=\"0.06\"/%3E%3C/svg%3E');",
        "usage": "Apply to hero wrapper or page background via pseudo-element; keep opacity <= 0.06."
      }
    },

    "radius_shadow": {
      "radius": {
        "card": "14px",
        "button": "12px",
        "pill": "999px"
      },
      "shadow": {
        "card": "0 1px 0 rgba(16,24,40,0.06), 0 10px 30px rgba(16,24,40,0.08)",
        "card_dark": "0 1px 0 rgba(0,0,0,0.35), 0 18px 40px rgba(0,0,0,0.35)",
        "focus": "0 0 0 3px hsla(var(--focus-ring)/0.35)"
      },
      "borders": {
        "hairline": "1px solid hsla(var(--border)/1)",
        "divider": "1px solid hsla(var(--border)/0.7)"
      }
    },

    "spacing_grid": {
      "container": {
        "max_width": "1120px",
        "padding": "px-4 sm:px-6 lg:px-8"
      },
      "layout": {
        "section_gap": "py-10 sm:py-14",
        "card_gap": "gap-4 sm:gap-6",
        "bento_columns": "grid-cols-1 md:grid-cols-12"
      }
    }
  },

  "typography": {
    "font_pairing": {
      "headings": {
        "name": "Space Grotesk",
        "google_fonts": "https://fonts.google.com/specimen/Space+Grotesk",
        "usage": "Headlines, scores, badges"
      },
      "body": {
        "name": "Spectral",
        "google_fonts": "https://fonts.google.com/specimen/Spectral",
        "usage": "Long-form editorial reading"
      },
      "mono_optional": {
        "name": "IBM Plex Mono",
        "google_fonts": "https://fonts.google.com/specimen/IBM+Plex+Mono",
        "usage": "timestamps, match IDs, small metadata"
      }
    },
    "scale_tailwind": {
      "h1": "text-4xl sm:text-5xl lg:text-6xl font-semibold tracking-tight",
      "h2": "text-base md:text-lg text-[hsl(var(--muted))]",
      "h3": "text-xl sm:text-2xl font-semibold tracking-tight",
      "body": "text-sm sm:text-base leading-7",
      "small": "text-xs sm:text-sm text-[hsl(var(--muted))]"
    },
    "editorial_rules": [
      "Use serif body for story pages; keep line length ~65–75ch (max-w-prose).",
      "Use short, punchy headlines; avoid ALL CAPS except tiny labels.",
      "Use drop-cap only on long-form stories (optional, CSS-only)."
    ]
  },

  "layout_patterns": {
    "global_shell": {
      "top_nav": "Desktop/tablet: sticky top nav with search + theme toggle.",
      "bottom_nav": "Mobile: fixed bottom nav (4–5 items) with safe-area padding.",
      "reading_layout": "Story pages use max-w-prose + sticky right rail on lg for match facts/why-care meter."
    },
    "homepage": {
      "structure": [
        "Hero tournament banner (feature match + Why Care)",
        "Upcoming matches carousel (touch)",
        "Trending stories grid (bento)",
        "Group standings widget (tabs A–L)",
        "Featured rivalries + iconic moments",
        "Hype notes feed + submit",
        "Newsletter signup"
      ]
    }
  },

  "components": {
    "navbar": {
      "desktop": {
        "layout": "Left: MatchTales wordmark; Center: primary nav; Right: search + theme toggle + newsletter CTA",
        "tailwind": "sticky top-0 z-50 backdrop-blur supports-[backdrop-filter]:bg-[hsl(var(--bg)/0.75)] border-b border-[hsl(var(--border)/0.7)]"
      },
      "mobile_bottom_nav": {
        "items": ["Home", "Fixtures", "Live", "Teams", "Stories"],
        "tailwind": "fixed bottom-0 left-0 right-0 z-50 border-t border-[hsl(var(--border)/0.7)] bg-[hsl(var(--surface))] supports-[backdrop-filter]:bg-[hsl(var(--surface)/0.85)] backdrop-blur",
        "interaction": "Active item shows pitch accent underline + icon fill; inactive is muted."
      },
      "data_testids": {
        "theme_toggle": "theme-toggle",
        "site_search_input": "site-search-input",
        "nav_home_link": "nav-home-link",
        "nav_fixtures_link": "nav-fixtures-link",
        "nav_live_link": "nav-live-link"
      }
    },

    "hero": {
      "goal": "Make the feature match feel like a magazine cover + immediate context.",
      "layout": "Two-column on lg: left editorial headline + dek + CTA; right feature match card with Why Care meter.",
      "tailwind": {
        "wrapper": "relative overflow-hidden rounded-[var(--r-card)] border border-[hsl(var(--border)/0.7)] bg-[hsl(var(--surface))]",
        "bg_accent": "before:absolute before:inset-0 before:pointer-events-none before:opacity-100 before:[background:var(--hero-bg)]",
        "inner": "relative p-6 sm:p-10"
      },
      "micro_interactions": [
        "CTA button hover: translate-y-[-1px] + shadow increase",
        "Feature card hover: subtle lift (translate-y-[-2px])"
      ]
    },

    "match_story_card": {
      "use": "Fixtures list + homepage feed",
      "layout": "Card with: teams row, kickoff time, Why Care badge, headline, teaser, tags, quick actions (save/share)",
      "tailwind": {
        "card": "group rounded-[14px] border border-[hsl(var(--border)/0.8)] bg-[hsl(var(--surface))] p-4 sm:p-5 shadow-[var(--shadow-card)] hover:shadow-[0_1px_0_rgba(16,24,40,0.06),0_18px_50px_rgba(16,24,40,0.12)]",
        "headline": "font-[var(--font-head)] text-lg sm:text-xl leading-snug tracking-tight group-hover:underline decoration-[hsl(var(--pitch))] decoration-2 underline-offset-4",
        "teaser": "mt-2 text-sm sm:text-base text-[hsl(var(--muted))] line-clamp-3"
      },
      "data_testids": {
        "card": "match-story-card",
        "share_button": "match-story-share-button",
        "save_button": "match-story-save-button"
      }
    },

    "why_care_badge_meter": {
      "visual": "A compact badge + a thin meter bar (like a magazine rating).",
      "badge": {
        "format": "Why Care 9.2",
        "tailwind": "inline-flex items-center gap-2 rounded-full border border-[hsl(var(--border))] bg-[hsl(var(--surface_2))] px-3 py-1 text-xs font-medium",
        "dot": "w-2 h-2 rounded-full bg-[hsl(var(--pitch))]"
      },
      "meter": {
        "type": "CSS-only segmented bar (10 segments) OR single bar with gradient-free solid fill",
        "tailwind": {
          "track": "h-2 w-full rounded-full bg-[hsl(var(--border)/0.6)] overflow-hidden",
          "fill": "h-full rounded-full bg-[hsl(var(--pitch))]"
        },
        "logic": "fillWidth = (score/10)*100% ; color switches by thresholds (semantic.why_care_scale)."
      },
      "data_testids": {
        "badge": "why-care-badge",
        "meter": "why-care-meter"
      }
    },

    "upcoming_matches_carousel": {
      "behavior": "Horizontal scroll-snap list (CSS) for zero-JS; optional small JS for arrows.",
      "tailwind": {
        "rail": "flex gap-4 overflow-x-auto snap-x snap-mandatory pb-2 [-webkit-overflow-scrolling:touch]",
        "item": "min-w-[280px] snap-start"
      },
      "data_testids": {
        "carousel": "upcoming-matches-carousel"
      }
    },

    "group_standings_widget": {
      "layout": "Tabs A–L (scrollable on mobile) + compact table.",
      "tailwind": {
        "tabs": "flex gap-2 overflow-x-auto pb-2",
        "tab": "rounded-full border border-[hsl(var(--border))] px-3 py-1 text-xs",
        "table": "w-full text-sm",
        "row": "border-b border-[hsl(var(--border)/0.7)]",
        "qualify_marker": "before:content-[''] before:inline-block before:w-1 before:h-4 before:rounded-full before:bg-[hsl(var(--pitch))]"
      },
      "data_testids": {
        "group_tabs": "group-standings-tabs",
        "group_table": "group-standings-table"
      }
    },

    "rivalry_card": {
      "visual": "Image-led card with a strong rivalry headline + 2–3 bullet context points.",
      "tailwind": {
        "card": "rounded-[14px] overflow-hidden border border-[hsl(var(--border)/0.8)] bg-[hsl(var(--surface))]",
        "image": "aspect-[16/9] w-full object-cover",
        "body": "p-4 sm:p-5"
      },
      "data_testids": {
        "card": "rivalry-card"
      }
    },

    "player_legacy_card": {
      "visual": "Portrait + legacy label + 3 stats chips (caps, goals, iconic moment).",
      "tailwind": {
        "card": "rounded-[14px] border border-[hsl(var(--border)/0.8)] bg-[hsl(var(--surface))] p-4",
        "portrait": "h-12 w-12 rounded-full object-cover ring-2 ring-[hsl(var(--border))]",
        "chip": "rounded-full bg-[hsl(var(--surface_2))] px-2 py-1 text-xs"
      },
      "data_testids": {
        "card": "player-legacy-card"
      }
    },

    "story_article_layout": {
      "reading": {
        "container": "max-w-prose",
        "type": "font-serif leading-8",
        "headings": "font-sans tracking-tight",
        "pullquote": "border-l-2 border-[hsl(var(--pitch))] pl-4 italic text-[hsl(var(--fg))]"
      },
      "match_detail_page_sections": [
        "Hero (match title + Why Care + kickoff + venue)",
        "The Stakes (short bullets)",
        "Rivalry Angle",
        "Fun Facts",
        "Key Players",
        "Head-to-Head",
        "Timeline (iconic moments)",
        "Share Card generator"
      ],
      "data_testids": {
        "article": "story-article",
        "share_card": "share-card"
      }
    },

    "live_second_screen": {
      "goal": "Second-screen companion: glanceable, thumb-friendly, low cognitive load.",
      "layout": "Top: match header + live status; Middle: hype meter + momentum ticks; Bottom: commentary + polls.",
      "widgets": {
        "hype_meter": "Large meter with 0–10 + animated pulse on big events (CSS keyframes, reduced-motion safe).",
        "polls": "Two-option quick polls with big tap targets.",
        "commentary": "Reverse chronological feed with time chips."
      },
      "tailwind": {
        "sticky_header": "sticky top-0 z-40 bg-[hsl(var(--bg)/0.85)] backdrop-blur border-b border-[hsl(var(--border)/0.7)]",
        "event_pulse": "animate-[pulse_1.2s_ease-in-out_1]"
      },
      "data_testids": {
        "live_hype_meter": "live-hype-meter",
        "live_poll": "live-poll",
        "live_commentary_feed": "live-commentary-feed"
      }
    },

    "forms": {
      "newsletter": {
        "layout": "Inline email + submit on desktop; stacked on mobile.",
        "tailwind": {
          "input": "h-11 rounded-[12px] border border-[hsl(var(--border))] bg-[hsl(var(--surface))] px-3 outline-none focus-visible:ring-2 focus-visible:ring-[hsl(var(--focus_ring))]",
          "button": "h-11 rounded-[12px] bg-[hsl(var(--pitch))] text-white px-4 font-medium hover:bg-[hsl(var(--pitch_2))]"
        },
        "data_testids": {
          "email": "newsletter-email-input",
          "submit": "newsletter-submit-button"
        }
      },
      "hype_note_submit": {
        "fields": ["name (optional)", "note", "match (optional)"]
      }
    },

    "footer": {
      "content": [
        "Disclaimer: not official FIFA",
        "Privacy Policy",
        "About",
        "Newsletter"
      ],
      "tailwind": "border-t border-[hsl(var(--border)/0.7)] bg-[hsl(var(--surface))]"
    },

    "404": {
      "concept": "Football-themed: 'Match not found' with a subtle pitch line illustration.",
      "tailwind": "min-h-[60vh] grid place-items-center text-center"
    }
  },

  "motion_microinteractions": {
    "principles": [
      "Prefer CSS-only transitions; Astro view transitions for page navigation.",
      "No transition: all. Only transition colors/shadows/opacity.",
      "Hover lift only on cards/buttons; keep subtle (1–2px).",
      "Respect prefers-reduced-motion: reduce."
    ],
    "tokens": {
      "ease": "cubic-bezier(0.2, 0.8, 0.2, 1)",
      "fast": "120ms",
      "base": "180ms"
    },
    "examples": {
      "button": "transition-colors duration-150",
      "card": "transition-shadow duration-200",
      "icon": "transition-opacity duration-150"
    }
  },

  "seo_share": {
    "og_card_layout": {
      "size": "1200x630",
      "composition": [
        "Top-left: MatchTales wordmark",
        "Center: Match headline (max 2 lines)",
        "Bottom-left: teams + kickoff",
        "Bottom-right: Why Care score badge",
        "Background: subtle pitch texture + mild radial accents"
      ],
      "typography": "Headings in Space Grotesk; metadata in Spectral or mono",
      "contrast": "Ensure text contrast >= 4.5:1"
    },
    "schema": [
      "SportsEvent for matches",
      "Article for stories",
      "BreadcrumbList for navigation"
    ]
  },

  "accessibility": {
    "rules": [
      "All controls must be keyboard reachable and have visible focus ring.",
      "Tap targets >= 44px height on mobile.",
      "Use aria-label for icon-only buttons (share/save/theme).",
      "Color is never the only indicator: add labels/icons for hype/importance.",
      "Use prefers-reduced-motion to disable pulses and view transitions."
    ]
  },

  "images": {
    "image_urls": [
      {
        "category": "hero_background",
        "description": "Cinematic stadium crowd / pitch for hero cover",
        "urls": [
          "https://images.unsplash.com/photo-1550591927-391fccf9934b?crop=entropy&cs=srgb&fm=jpg&ixlib=rb-4.1.0&q=85",
          "https://images.unsplash.com/photo-1646643508957-088fe0eac722?crop=entropy&cs=srgb&fm=jpg&ixlib=rb-4.1.0&q=85"
        ]
      },
      {
        "category": "rivalry_cards",
        "description": "Stadium / crowd / match action imagery",
        "urls": [
          "https://images.unsplash.com/photo-1556152352-8edad147cc21?crop=entropy&cs=srgb&fm=jpg&ixlib=rb-4.1.0&q=85"
        ]
      },
      {
        "category": "player_legacy_portraits",
        "description": "Dramatic portrait placeholders (avoid identifying real players)",
        "urls": [
          "https://images.unsplash.com/photo-1627774250096-25d8c0ece8ba?crop=entropy&cs=srgb&fm=jpg&ixlib=rb-4.1.0&q=85",
          "https://images.unsplash.com/photo-1599828949462-69ccec8ee6a3?crop=entropy&cs=srgb&fm=jpg&ixlib=rb-4.1.0&q=85"
        ]
      },
      {
        "category": "texture",
        "description": "Paper/grain texture for subtle overlays",
        "urls": [
          "https://images.unsplash.com/photo-1705837861201-dd000d929a31?crop=entropy&cs=srgb&fm=jpg&ixlib=rb-4.1.0&q=85"
        ]
      }
    ]
  },

  "component_path": {
    "note": "This project is Astro + Tailwind (no shadcn). Use Astro components and Tailwind utilities. If any React islands exist, keep them minimal and in .js.",
    "astro_components_to_create": [
      "src/components/Nav.astro",
      "src/components/BottomNav.astro",
      "src/components/MatchStoryCard.astro",
      "src/components/WhyCareMeter.astro",
      "src/components/GroupStandingsWidget.astro",
      "src/components/RivalryCard.astro",
      "src/components/PlayerLegacyCard.astro",
      "src/components/NewsletterForm.astro",
      "src/components/HypeNoteForm.astro",
      "src/components/ShareCardPreview.astro"
    ],
    "optional_islands_js": [
      "src/components/islands/ThemeToggle.js",
      "src/components/islands/SearchBox.js",
      "src/components/islands/LiveSecondScreen.js"
    ]
  },

  "instructions_to_main_agent": {
    "theme_tokens_css": {
      "file": "src/styles/tokens.css (or global.css)",
      "snippet": ":root{--bg:40 33% 98%;--fg:220 18% 12%;--surface:0 0% 100%;--surface-2:40 20% 96%;--border:220 14% 88%;--muted:220 10% 45%;--pitch:158 42% 22%;--pitch-2:156 38% 30%;--accent-sky:198 88% 45%;--accent-coral:14 86% 60%;--accent-lime:84 78% 45%;--focus-ring:198 88% 45%;--r-card:14px;--r-btn:12px;--shadow-card:0 1px 0 rgba(16,24,40,0.06),0 10px 30px rgba(16,24,40,0.08);--hero-bg:radial-gradient(900px circle at 20% 10%, hsla(var(--pitch)/0.18), transparent 55%), radial-gradient(700px circle at 80% 0%, hsla(var(--accent-sky)/0.14), transparent 52%);} html[data-theme='dark']{--bg:220 18% 8%;--fg:0 0% 98%;--surface:220 18% 11%;--surface-2:220 16% 14%;--border:220 14% 22%;--muted:220 10% 70%;--pitch:156 45% 38%;--pitch-2:156 55% 44%;--accent-sky:198 88% 55%;--accent-coral:14 86% 60%;--accent-lime:84 78% 45%;--focus-ring:198 88% 55%;--shadow-card:0 1px 0 rgba(0,0,0,0.35),0 18px 40px rgba(0,0,0,0.35);}"
    },
    "tailwind_usage": [
      "Use bg-[hsl(var(--bg))] text-[hsl(var(--fg))] globally.",
      "Cards: bg-[hsl(var(--surface))] border-[hsl(var(--border)/0.8)] rounded-[var(--r-card)] shadow-[var(--shadow-card)].",
      "Links: text-[hsl(var(--accent-sky))] hover:underline underline-offset-4.",
      "Primary CTA: bg-[hsl(var(--pitch))] hover:bg-[hsl(var(--pitch-2))] text-white rounded-[var(--r-btn)] h-11 px-4.",
      "Avoid gradients except hero background accents (<=20% viewport)."
    ],
    "data_testid_rule": "Every interactive element and key informational element must include data-testid in kebab-case (role-based).",
    "performance": [
      "Default to zero JS; use CSS scroll-snap for carousels.",
      "Hydrate only ThemeToggle, SearchBox, LiveSecondScreen.",
      "Use Astro <Image> where possible; set width/height; lazy-load below the fold."
    ],
    "astro_view_transitions": {
      "use": "Enable Astro View Transitions for page navigation; disable under prefers-reduced-motion.",
      "note": "Keep transitions subtle (fade/slide 8–12px)."
    }
  },

  "appendix_general_ui_ux_design_guidelines": "<General UI UX Design Guidelines>  \n    - You must **not** apply universal transition. Eg: `transition: all`. This results in breaking transforms. Always add transitions for specific interactive elements like button, input excluding transforms\n    - You must **not** center align the app container, ie do not add `.App { text-align: center; }` in the css file. This disrupts the human natural reading flow of text\n   - NEVER: use AI assistant Emoji characters like`🤖🧠💭💡🔮🎯📚🎭🎬🎪🎉🎊🎁🎀🎂🍰🎈🎨🎰💰💵💳🏦💎🪙💸🤑📊📈📉💹🔢🏆🥇 etc for icons. Always use **FontAwesome cdn** or **lucid-react** library already installed in the package.json\n\n **GRADIENT RESTRICTION RULE**\nNEVER use dark/saturated gradient combos (e.g., purple/pink) on any UI element.  Prohibited gradients: blue-500 to purple 600, purple 500 to pink-500, green-500 to blue-500, red to pink etc\nNEVER use dark gradients for logo, testimonial, footer etc\nNEVER let gradients cover more than 20% of the viewport.\nNEVER apply gradients to text-heavy content or reading areas.\nNEVER use gradients on small UI elements (<100px width).\nNEVER stack multiple gradient layers in the same viewport.\n\n**ENFORCEMENT RULE:**\n    • Id gradient area exceeds 20% of viewport OR affects readability, **THEN** use solid colors\n\n**How and where to use:**\n   • Section backgrounds (not content backgrounds)\n   • Hero section header content. Eg: dark to light to dark color\n   • Decorative overlays and accent elements only\n   • Hero section with 2-3 mild color\n   • Gradients creation can be done for any angle say horizontal, vertical or diagonal\n\n- For AI chat, voice application, **do not use purple color. Use color like light green, ocean blue, peach orange etc**\n\n</Font Guidelines>\n\n- Every interaction needs micro-animations - hover states, transitions, parallax effects, and entrance animations. Static = dead. \n   \n- Use 2-3x more spacing than feels comfortable. Cramped designs look cheap.\n\n- Subtle grain textures, noise overlays, custom cursors, selection states, and loading animations: separates good from extraordinary.\n   \n- Before generating UI, infer the visual style from the problem statement (palette, contrast, mood, motion) and immediately instantiate it by setting global design tokens (primary, secondary/accent, background, foreground, ring, state colors), rather than relying on any library defaults. Don't make the background dark as a default step, always understand problem first and define colors accordingly\n    Eg: - if it implies playful/energetic, choose a colorful scheme\n           - if it implies monochrome/minimal, choose a black–white/neutral scheme\n\n**Component Reuse:**\n\t- Prioritize using pre-existing components from src/components/ui when applicable\n\t- Create new components that match the style and conventions of existing components when needed\n\t- Examine existing components to understand the project's component patterns before creating new ones\n\n**IMPORTANT**: Do not use HTML based component like dropdown, calendar, toast etc. You **MUST** always use `/app/frontend/src/components/ui/ ` only as a primary components as these are modern and stylish component\n\n**Best Practices:**\n\t- Use Shadcn/UI as the primary component library for consistency and accessibility\n\t- Import path: ./components/[component-name]\n\n**Export Conventions:**\n\t- Components MUST use named exports (export const ComponentName = ...)\n\t- Pages MUST use default exports (export default function PageName() {...})\n\n**Toasts:**\n  - Use `sonner` for toasts\"\n  - Sonner component are located in `/app/src/components/ui/sonner.tsx`\n\nUse 2–4 color gradients, subtle textures/noise overlays, or CSS-based noise to avoid flat visuals.\n</General UI UX Design Guidelines>"
}
