"""FastAPI app: serves the RAG API and the single-page frontend."""
from __future__ import annotations
import sqlite3
import uuid
from contextlib import contextmanager
from pathlib import Path
from typing import List, Optional
from fastapi import FastAPI, HTTPException
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
    status: str = "answered"
    ticket_id: Optional[str] = None


class TeacherAnswer(BaseModel):
    answer: str


@contextmanager
def ticket_database():
    config.TICKET_DB.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(config.TICKET_DB)
    connection.row_factory = sqlite3.Row
    try:
        yield connection
        connection.commit()
    finally:
        connection.close()


def init_ticket_database() -> None:
    with ticket_database() as connection:
        connection.execute(
            """CREATE TABLE IF NOT EXISTS questions (
                id TEXT PRIMARY KEY,
                question TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT 'pending',
                answer TEXT,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                answered_at TEXT
            )"""
        )


def create_ticket(question: str) -> str:
    ticket_id = uuid.uuid4().hex[:12]
    with ticket_database() as connection:
        connection.execute(
            "INSERT INTO questions(id, question, status) VALUES (?, ?, 'pending')",
            (ticket_id, question),
        )
    return ticket_id


@app.on_event("startup")
def startup() -> None:
    init_ticket_database()


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
        init_ticket_database()
        ticket_id = create_ticket(req.question.strip())
        return ChatResponse(
            found=False,
            answer=(
                f"{gen['answer']} Câu hỏi đã được chuyển tới giảng viên "
                f"(mã {ticket_id})."
            ),
            grounded=False,
            mode=gen["mode"],
            status="escalated",
            ticket_id=ticket_id,
        )
    lab_src = [SourceOut(segment_code=x["meta"]["segment_code"], section=x["meta"]["section"],
                         source_file=x["meta"]["source_file"], text=x["text"],
                         score=round(x["score"], 3)) for x in retr.get("lab", [])]
    return ChatResponse(
        found=True, answer=gen["answer"], grounded=gen["grounded"], mode=gen["mode"],
        day=retr["day"], day_label=retr["day_label"], topic=retr["topic"],
        sources=[SourceOut(**s) for s in retr["sources"]], lab=lab_src,
    )


@app.get("/api/questions")
def list_questions(status: str = "pending"):
    if status not in {"pending", "answered", "all"}:
        raise HTTPException(400, "Invalid status")
    init_ticket_database()
    query = "SELECT * FROM questions"
    params: tuple = ()
    if status != "all":
        query += " WHERE status = ?"
        params = (status,)
    query += " ORDER BY created_at DESC"
    with ticket_database() as connection:
        return [dict(row) for row in connection.execute(query, params).fetchall()]


@app.post("/api/questions/{ticket_id}/answer")
def answer_question(ticket_id: str, payload: TeacherAnswer):
    answer = payload.answer.strip()
    if len(answer) < 2:
        raise HTTPException(422, "Answer is too short")
    init_ticket_database()
    with ticket_database() as connection:
        row = connection.execute(
            "SELECT status FROM questions WHERE id = ?", (ticket_id,)
        ).fetchone()
        if row is None:
            raise HTTPException(404, "Question not found")
        if row["status"] == "answered":
            raise HTTPException(409, "Question already answered")
        connection.execute(
            """UPDATE questions
               SET answer=?, status='answered', answered_at=CURRENT_TIMESTAMP
               WHERE id=?""",
            (answer, ticket_id),
        )
    return {"ok": True, "ticket_id": ticket_id, "status": "answered"}


@app.post("/api/ingest")
def do_ingest():
    """Coach action: (re)build the knowledge base from transcripts on disk."""
    return ingest_mod.run(reset=True)
