#!/usr/bin/env bash
# Thin wrapper — see extract-figures.py for full CLI.
# Usage: fetch-arxiv-source.sh <arxiv_id> <slug>
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
exec python3 "$SCRIPT_DIR/extract-figures.py" fetch --arxiv "${1:?arxiv id}" --slug "${2:?slug}"
