"""Answer generation.

If ANTHROPIC_API_KEY is set, Claude summarizes the retrieved lecture context
into a grounded answer. Otherwise we return an honest extractive summary built
from the top segments, so the project still runs end-to-end with zero keys.
"""
from __future__ import annotations
from typing import Dict, Any, List

from . import config

SYSTEM = (
    "Bạn là VLearn Tutor, trợ lý ôn tập cho khoá 'AI Thực Chiến'. "
    "Chỉ trả lời dựa trên đoạn transcript bài giảng được cung cấp. "
    "Tóm tắt cách kiến thức được giảng trên lớp, ngắn gọn, bằng tiếng Việt. "
    "Luôn trích dẫn mã đoạn [Txx-NNN] tương ứng. Nếu context không đủ, nói rõ."
)


def _context_block(sources: List[Dict[str, Any]]) -> str:
    return "\n".join(f"[{s['segment_code']}] ({s['section']}) {s['text']}" for s in sources)


def _extractive(retr: Dict[str, Any]) -> str:
    src = retr["sources"][:3]
    lead = (f"Kiến thức này được giảng ở {retr['day_label']} — chủ đề \"{retr['topic']}\". "
            f"Trên lớp, giảng viên trình bày như sau:")
    body = "\n".join(f"• {s['text']}  [{s['segment_code']}]" for s in src)
    return f"{lead}\n{body}"


def generate(question: str, retr: Dict[str, Any]) -> Dict[str, Any]:
    if not retr.get("found"):
        return {"answer": "Mình chưa tìm thấy kiến thức này trong học liệu đã nạp.",
                "grounded": False, "mode": "none"}

    if not config.ANTHROPIC_API_KEY:
        return {"answer": _extractive(retr), "grounded": True, "mode": "extractive"}

    try:
        import anthropic
        client = anthropic.Anthropic(api_key=config.ANTHROPIC_API_KEY)
        ctx = _context_block(retr["sources"])
        msg = client.messages.create(
            model=config.ANTHROPIC_MODEL,
            max_tokens=600,
            system=SYSTEM,
            messages=[{"role": "user", "content":
                f"Câu hỏi của học viên: {question}\n\n"
                f"Kiến thức được xác định ở {retr['day_label']} — {retr['topic']}.\n"
                f"Các đoạn transcript liên quan:\n{ctx}\n\n"
                f"Hãy tóm tắt cách kiến thức này được dạy, kèm mã đoạn trích dẫn."}],
        )
        text = "".join(b.text for b in msg.content if getattr(b, "type", "") == "text")
        return {"answer": text.strip(), "grounded": True, "mode": "claude"}
    except Exception as e:
        # graceful fallback if the API call fails
        return {"answer": _extractive(retr), "grounded": True,
                "mode": "extractive", "note": f"LLM fallback: {e}"}
