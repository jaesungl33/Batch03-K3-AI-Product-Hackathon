"""FastAPI backend and LangGraph RAG/escalation agent for VLearn."""
from __future__ import annotations

import hashlib
import os
import sqlite3
import uuid
from pathlib import Path
from typing import Literal, TypedDict

import chromadb
from dotenv import load_dotenv
from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from google import genai
from google.genai import types
from langgraph.graph import END, START, StateGraph
from pydantic import BaseModel, Field
from ocr_to_chroma import chunks, embed_documents, ocr_page, pages

ROOT = Path(__file__).parent
DB_PATH = ROOT / "data" / "teacher_questions.sqlite3"
CHROMA_PATH = ROOT / "data" / "chroma_db"
UPLOAD_DIR = ROOT / "data" / "uploads"
SLIDE_COLLECTION = "slides_ocr"
QA_COLLECTION = "teacher_qa"
EMBED_MODEL = "gemini-embedding-001"
EMBED_DIM = 768
ANSWER_MODEL = "gemini-3.5-flash-lite"
MAX_DISTANCE = 0.42

load_dotenv(ROOT / ".env")
if not os.getenv("GEMINI_API_KEY"):
    raise RuntimeError("GEMINI_API_KEY is missing")

ai = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
chroma = chromadb.PersistentClient(path=str(CHROMA_PATH))
slides = chroma.get_or_create_collection(SLIDE_COLLECTION, metadata={"hnsw:space": "cosine"})
teacher_qa = chroma.get_or_create_collection(
    QA_COLLECTION, metadata={"hnsw:space": "cosine", "embedding_model": EMBED_MODEL}
)

app = FastAPI(title="VLearn Tutor Agent")
app.mount("/static", StaticFiles(directory=ROOT / "frontend"), name="static")


class AgentState(TypedDict, total=False):
    question: str
    matches: list[dict]
    best_distance: float
    route: Literal["answer", "escalate"]
    answer: str
    ticket_id: str


class ChatRequest(BaseModel):
    question: str = Field(min_length=2, max_length=2000)


class TeacherAnswer(BaseModel):
    answer: str = Field(min_length=2, max_length=8000)


class RelevanceDecision(BaseModel):
    relevant: bool
    reason: str


def database() -> sqlite3.Connection:
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def init_database() -> None:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    with database() as connection:
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


def embed(text: str, task_type: str) -> list[float]:
    response = ai.models.embed_content(
        model=EMBED_MODEL,
        contents=text,
        config=types.EmbedContentConfig(
            task_type=task_type, output_dimensionality=EMBED_DIM
        ),
    )
    return response.embeddings[0].values


def query_collection(collection, vector: list[float], limit: int, kind: str) -> list[dict]:
    if collection.count() == 0:
        return []
    result = collection.query(
        query_embeddings=[vector], n_results=min(limit, collection.count()),
        include=["documents", "metadatas", "distances"],
    )
    return [
        {"text": doc, "metadata": meta, "distance": float(distance), "kind": kind}
        for doc, meta, distance in zip(
            result["documents"][0], result["metadatas"][0], result["distances"][0]
        )
    ]


def search_knowledge(state: AgentState) -> AgentState:
    """LangGraph search tool: retrieve from slides and teacher-approved Q&A."""
    vector = embed(state["question"], "RETRIEVAL_QUERY")
    matches = query_collection(teacher_qa, vector, 3, "teacher_qa")
    matches += query_collection(slides, vector, 4, "slide")
    matches.sort(key=lambda item: item["distance"])
    matches = matches[:5]
    return {
        "matches": matches,
        "best_distance": matches[0]["distance"] if matches else 1.0,
    }


def decide_route(state: AgentState) -> AgentState:
    """Require both vector similarity and semantic answerability."""
    if not state.get("matches") or state.get("best_distance", 1.0) > MAX_DISTANCE:
        return {"route": "escalate"}
    context = "\n\n".join(item["text"] for item in state["matches"][:3])
    response = ai.models.generate_content(
        model=ANSWER_MODEL,
        contents=f"Câu hỏi: {state['question']}\n\nNgữ cảnh:\n{context}",
        config=types.GenerateContentConfig(
            system_instruction=(
                "Đánh giá nghiêm ngặt liệu ngữ cảnh có chứa đủ thông tin trực tiếp để trả lời "
                "câu hỏi hay không. Liên quan cùng chủ đề nhưng không có đáp án vẫn là false. "
                "Câu hỏi về thông tin thời gian thực, cá nhân, hành chính hoặc ngoài bài học là false."
            ),
            response_mime_type="application/json",
            response_schema=RelevanceDecision,
            temperature=0,
        ),
    )
    decision = response.parsed
    return {"route": "answer" if decision and decision.relevant else "escalate"}


def route_edge(state: AgentState) -> str:
    return state["route"]


def answer_from_context(state: AgentState) -> AgentState:
    context = "\n\n".join(
        f"SOURCE {index + 1} [{item['kind']}, distance={item['distance']:.3f}]\n{item['text']}"
        for index, item in enumerate(state["matches"])
    )
    response = ai.models.generate_content(
        model=ANSWER_MODEL,
        contents=f"Câu hỏi: {state['question']}\n\nNgữ cảnh:\n{context}",
        config=types.GenerateContentConfig(
            system_instruction=(
                "Bạn là trợ giảng VLearn. Chỉ trả lời từ ngữ cảnh được cung cấp. "
                "Nếu ngữ cảnh không thực sự trả lời câu hỏi, hãy nói không đủ dữ kiện. "
                "Trả lời rõ ràng, ngắn gọn bằng tiếng Việt."
            ),
            temperature=0,
        ),
    )
    return {"answer": (response.text or "Không đủ dữ kiện để trả lời.").strip()}


def send_to_teacher(state: AgentState) -> AgentState:
    """LangGraph escalation tool: persist a question for a teacher."""
    ticket_id = uuid.uuid4().hex[:12]
    with database() as connection:
        connection.execute(
            "INSERT INTO questions(id, question, status) VALUES (?, ?, 'pending')",
            (ticket_id, state["question"]),
        )
    return {
        "ticket_id": ticket_id,
        "answer": "Câu hỏi này nằm ngoài phạm vi kiến thức hiện có hoặc kết quả tìm kiếm chưa đủ tin cậy. Mình đã chuyển trực tiếp tới giảng viên.",
    }


builder = StateGraph(AgentState)
builder.add_node("search_tool", search_knowledge)
builder.add_node("relevance_gate", decide_route)
builder.add_node("answer", answer_from_context)
builder.add_node("send_teacher_tool", send_to_teacher)
builder.add_edge(START, "search_tool")
builder.add_edge("search_tool", "relevance_gate")
builder.add_conditional_edges(
    "relevance_gate", route_edge, {"answer": "answer", "escalate": "send_teacher_tool"}
)
builder.add_edge("answer", END)
builder.add_edge("send_teacher_tool", END)
agent = builder.compile()


@app.on_event("startup")
def startup() -> None:
    init_database()


@app.get("/")
def index() -> FileResponse:
    return FileResponse(ROOT / "frontend" / "index.html")


@app.post("/api/chat")
def chat(payload: ChatRequest) -> dict:
    result = agent.invoke({"question": payload.question.strip()})
    sources = [
        {
            "text": item["text"],
            "score": round(1 - item["distance"], 3),
            "source_file": item["metadata"].get("relative_source", "Giảng viên trả lời"),
            "segment_code": (
                f"Trang {item['metadata'].get('page', '?')}"
                if item["kind"] == "slide" else "Q&A giảng viên"
            ),
            "section": "Slide bài giảng" if item["kind"] == "slide" else "Giảng viên xác nhận",
        }
        for item in result.get("matches", [])[:3]
    ]
    escalated = result.get("route") == "escalate"
    return {
        "found": not escalated,
        "status": "escalated" if escalated else "answered",
        "answer": result["answer"],
        "ticket_id": result.get("ticket_id"),
        "confidence": round(1 - result.get("best_distance", 1.0), 3),
        "sources": sources if not escalated else [],
    }


@app.get("/api/questions")
def list_questions(status: str = "pending") -> list[dict]:
    if status not in {"pending", "answered", "all"}:
        raise HTTPException(400, "Invalid status")
    sql = "SELECT * FROM questions"
    params: tuple = ()
    if status != "all":
        sql += " WHERE status = ?"
        params = (status,)
    sql += " ORDER BY created_at DESC"
    with database() as connection:
        return [dict(row) for row in connection.execute(sql, params).fetchall()]


@app.post("/api/questions/{ticket_id}/answer")
def answer_question(ticket_id: str, payload: TeacherAnswer) -> dict:
    with database() as connection:
        row = connection.execute("SELECT * FROM questions WHERE id = ?", (ticket_id,)).fetchone()
        if row is None:
            raise HTTPException(404, "Question not found")
        if row["status"] == "answered":
            raise HTTPException(409, "Question already answered")
        answer = payload.answer.strip()
        connection.execute(
            "UPDATE questions SET answer=?, status='answered', answered_at=CURRENT_TIMESTAMP WHERE id=?",
            (answer, ticket_id),
        )
    document = f"Câu hỏi học viên: {row['question']}\nCâu trả lời đã được giảng viên xác nhận: {answer}"
    vector = embed(document, "RETRIEVAL_DOCUMENT")
    doc_id = hashlib.sha256(f"teacher:{ticket_id}".encode()).hexdigest()
    teacher_qa.upsert(
        ids=[doc_id], documents=[document], embeddings=[vector],
        metadatas=[{"ticket_id": ticket_id, "source_type": "teacher_answer", "approved": True}],
    )
    return {"ok": True, "ticket_id": ticket_id, "stored_in": QA_COLLECTION}



@app.post("/api/ingest")
def ingest_pdf(file: UploadFile = File(...)) -> dict:
    """OCR an uploaded PDF with Gemini and store its chunks in ChromaDB."""
    original_name = Path(file.filename or "document.pdf").name
    if file.content_type != "application/pdf" and not original_name.lower().endswith(".pdf"):
        raise HTTPException(415, "Chỉ hỗ trợ file PDF")
    payload = file.file.read(25 * 1024 * 1024 + 1)
    if len(payload) > 25 * 1024 * 1024:
        raise HTTPException(413, "PDF vượt quá giới hạn 25 MB")
    if not payload.startswith(b"%PDF-"):
        raise HTTPException(400, "File không phải PDF hợp lệ")

    digest = hashlib.sha256(payload).hexdigest()
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
    stored_path = UPLOAD_DIR / f"{digest[:20]}.pdf"
    stored_path.write_bytes(payload)

    documents: list[str] = []
    ids: list[str] = []
    metadatas: list[dict] = []
    page_count = 0
    try:
        for page in pages(stored_path, 160):
            page_count = page.page_number
            text = ocr_page(ai, page, ANSWER_MODEL, retries=3)
            for chunk_index, chunk in enumerate(chunks(text, 1200, 200)):
                ids.append(hashlib.sha256(
                    f"pdf:{digest}:{page.page_number}:{chunk_index}".encode()
                ).hexdigest())
                documents.append(chunk)
                metadatas.append({
                    "source": stored_path.relative_to(ROOT).as_posix(),
                    "relative_source": original_name,
                    "filename": original_name,
                    "page": page.page_number,
                    "chunk_index": chunk_index,
                    "ocr_model": ANSWER_MODEL,
                    "source_type": "teacher_pdf_upload",
                    "file_sha256": digest,
                })
    except Exception as exc:
        raise HTTPException(422, f"Không thể OCR PDF: {exc}") from exc
    if not documents:
        raise HTTPException(422, "OCR hoàn tất nhưng không tìm thấy văn bản")

    vectors = embed_documents(
        ai, documents, EMBED_MODEL, EMBED_DIM, batch_size=50, retries=3
    )
    slides.upsert(ids=ids, documents=documents, metadatas=metadatas, embeddings=vectors)
    return {
        "ok": True,
        "filename": original_name,
        "pages": page_count,
        "chunks": len(documents),
        "backend": "Gemini OCR + Gemini Embedding",
        "collection": SLIDE_COLLECTION,
        "count_in_store": slides.count(),
    }

@app.get("/api/inventory")
def inventory() -> dict:
    with database() as connection:
        pending = connection.execute(
            "SELECT COUNT(*) FROM questions WHERE status='pending'"
        ).fetchone()[0]
    return {
        "count": slides.count() + teacher_qa.count(),
        "pending_questions": pending,
        "rows": [
            {"day_label": "Slides OCR", "topic": "Bài giảng", "type": "theory", "chunks": slides.count()},
            {"day_label": "Giảng viên", "topic": "Q&A đã duyệt", "type": "qa", "chunks": teacher_qa.count()},
        ],
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=False)

