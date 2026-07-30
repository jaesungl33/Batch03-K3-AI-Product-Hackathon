"""Central configuration. All paths and knobs live here."""
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = Path(os.getenv("VLEARN_DATA", ROOT / "data"))
TRANSCRIPT_DIR = DATA_DIR / "transcript"
CHROMA_DIR = Path(os.getenv("VLEARN_CHROMA", ROOT / "chroma_store"))
TICKET_DB = Path(os.getenv("VLEARN_TICKET_DB", DATA_DIR / "teacher_questions.sqlite3"))
COLLECTION = "vlearn_lectures"

# Embedding backend: "st" (sentence-transformers, multilingual, recommended)
# or "tfidf" (zero-download fallback so the project runs anywhere).
EMBED_BACKEND = os.getenv("VLEARN_EMBED", "st")
ST_MODEL = os.getenv("VLEARN_ST_MODEL", "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
TFIDF_DIM = 512

# Generation. If ANTHROPIC_API_KEY is set we synthesize an answer with Claude,
# otherwise we fall back to an extractive summary built from retrieved segments.
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
ANTHROPIC_MODEL = os.getenv("VLEARN_MODEL", "claude-sonnet-4-6")

# Retrieval knobs
LOCATE_K = 8      # tier-1: how many segments to sample when locating the day/topic
CONTEXT_K = 6     # tier-2: how many segments (filtered) to feed the answer
