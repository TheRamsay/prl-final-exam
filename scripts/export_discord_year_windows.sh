#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ENV_FILE="$ROOT_DIR/.env"

if [[ -f "$ENV_FILE" ]]; then
  set -a
  # shellcheck disable=SC1090
  source "$ENV_FILE"
  set +a
fi

: "${CHANNEL_ID:?CHANNEL_ID is required}"
: "${USER_TOKEN:?USER_TOKEN is required}"

if ! command -v docker >/dev/null 2>&1; then
  echo "docker is required" >&2
  exit 1
fi

# Discord snowflakes embed the creation timestamp in the upper bits.
created_ms=$(((CHANNEL_ID >> 22) + 1420070400000))
start_year="$(date -u -r "$((created_ms / 1000))" +%Y)"
end_year="$(date -u +%Y)"

mkdir -p "$ROOT_DIR/raw/discord"

for year in $(seq "$start_year" "$end_year"); do
  out_dir="$ROOT_DIR/raw/discord/$year"
  out_file="$out_dir/${CHANNEL_ID}.json"
  after="$year-04-15"
  before="$year-06-16"

  mkdir -p "$out_dir"

  docker run --rm \
    -e DISCORD_TOKEN="$USER_TOKEN" \
    -v "$ROOT_DIR:/work" \
    -w /work \
    tyrrrz/discordchatexporter:latest \
    export \
    --channel "$CHANNEL_ID" \
    --output "/work/raw/discord/$year/${CHANNEL_ID}.json" \
    --format Json \
    --after "$after" \
    --before "$before" \
    --utc
done
