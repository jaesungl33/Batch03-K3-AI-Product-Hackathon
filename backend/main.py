"""FastAPI app: serves the RAG API and the single-page frontend."""
from __future__ import annotations
from pathlib import Path
from typing import List, Optional
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

from . import config, ingest as ingest_mod
from .retrieval import retrieve
from .llm import generate
from .store import Store

app = FastAPI(title="VLearn Tutor — RAG")
FRONTEND = config.ROOT / "frontend" / "index.html"


class ChatRequest(BaseModel):
    question: str


class SourceOut(BaseModel):
    segment_code: str
    section: str
    source_file: str
    text: str
    score: float


class ChatResponse(BaseModel):
    found: bool
    answer: str
    grounded: bool
    mode: str
    day: Optional[str] = None
    day_label: Optional[str] = None
    topic: Optional[str] = None
    sources: List[SourceOut] = []
    lab: List[SourceOut] = []


@app.get("/")
def home():
    return FileResponse(FRONTEND)


@app.get("/api/health")
def health():
    return {"status": "ok", "embed_backend": config.EMBED_BACKEND,
            "has_llm": bool(config.ANTHROPIC_API_KEY),
            "count": Store().count()}


@app.get("/api/inventory")
def inventory():
    return {"rows": Store().inventory(), "count": Store().count()}


@app.post("/api/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    retr = retrieve(req.question)
    gen = generate(req.question, retr)
    if not retr.get("found"):
        return ChatResponse(found=False, answer=gen["answer"],
                            grounded=False, mode=gen["mode"])
    lab_src = [SourceOut(segment_code=x["meta"]["segment_code"], section=x["meta"]["section"],
                         source_file=x["meta"]["source_file"], text=x["text"],
                         score=round(x["score"], 3)) for x in retr.get("lab", [])]
    return ChatResponse(
        found=True, answer=gen["answer"], grounded=gen["grounded"], mode=gen["mode"],
        day=retr["day"], day_label=retr["day_label"], topic=retr["topic"],
        sources=[SourceOut(**s) for s in retr["sources"]], lab=lab_src,
    )


@app.post("/api/ingest")
def do_ingest():
    """Coach action: (re)build the knowledge base from transcripts on disk."""
    return ingest_mod.run(reset=True)
