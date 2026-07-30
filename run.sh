#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
[ -d .venv ] || python3 -m venv .venv
source .venv/bin/activate
pip install -q -r requirements.txt
[ -f .env ] && export $(grep -v '^#' .env | xargs) || true
echo "== Building knowledge base from transcripts =="
python -m backend.ingest
echo "== Starting VLearn Tutor at http://localhost:8000 =="
python -m uvicorn backend.main:app --port 8000 --reload
