#!/usr/bin/env bash
# Restore the skills that live in their own upstream repos.
# Run from inside ~/.claude/skills after cloning this repo.
set -euo pipefail

cd "$(dirname "$0")"

clone() {
  local name="$1" url="$2"
  if [ -e "$name" ]; then
    echo "skip   $name (already present)"
  else
    echo "clone  $name"
    git clone --quiet "$url" "$name"
  fi
}

clone tastemaker        https://github.com/codeswithroh/tastemaker
clone learn-ai-faster   https://github.com/aashaexo/learn-ai-faster
clone sub-reddit-finder https://github.com/unknownking07/sub-reddit-finder.git
clone video-use         https://github.com/browser-use/video-use

echo
echo "Done. Two skills need a Python env before use:"
echo "  seo/        -> python3 -m venv .venv && .venv/bin/pip install -r requirements.txt"
echo "  video-use/  -> uv sync   (also needs a .env, see video-use/.env.example)"
