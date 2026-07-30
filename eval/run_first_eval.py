#!/usr/bin/env python3
"""Run golden set through VLearn Tutor RAG and write eval/run-1-results.md"""
from __future__ import annotations

import csv
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# Use TF-IDF so eval runs offline without downloading ST model
os.environ.setdefault("VLEARN_EMBED", "tfidf")
os.environ.setdefault("VLEARN_CHROMA", str(ROOT / "chroma_store"))

from backend import ingest as ingest_mod  # noqa: E402
from backend.llm import generate  # noqa: E402
from backend.retrieval import retrieve  # noqa: E402

EVAL_DIR = Path(__file__).resolve().parent

CASES = [
    # (id, question, expect: "answer" | "decline" | "locate", locate_hint)
    (1, "Turing test là gì và cách kiểm tra thế nào?", "answer", "Day 1"),
    (2, "AlphaGo nổi tiếng với nước đi nào và vì sao Lee Sedol bối rối?", "answer", None),
    (3, "Kiến trúc Transformer do ai tạo ra và năm nào?", "answer", None),
    (4, "Self-attention hoạt động thế nào? Q, K, V là gì?", "answer", None),
    (5, "Vì sao LLM bị hallucination và RAG giúp gì?", "answer", None),
    (6, "Temperature trong LLM dùng để làm gì?", "answer", None),
    (7, "Context window là gì và giới hạn nó gây ra vấn đề gì?", "answer", None),
    (8, "Mixture of Experts (MoE) giải quyết vấn đề gì?", "answer", None),
    (9, "Theo bài giảng, đưa AI vào doanh nghiệp thì bao nhiêu phần trăm phụ thuộc con người và vận hành?", "answer", "70"),
    (10, "Product manager khác project manager thế nào?", "answer", None),
    (11, "Quick win quan trọng thế nào khi chọn bài toán AI?", "answer", None),
    (12, "Automation và augmentation khác nhau thế nào?", "answer", None),
    (13, "Ba cấp độ kỹ thuật khi đưa AI vào sản phẩm là gì?", "answer", None),
    (14, "Khi nào nên chọn RAG thay vì fine-tuning?", "answer", None),
    (15, "Câu chuyện Cruise taxi tự lái dạy bài học gì về scope vận hành?", "answer", None),
    (16, "LLM được huấn luyện qua mấy giai đoạn chính?", "answer", None),
    (17, "Công thức nấu phở bò Hà Nội chuẩn là gì?", "decline", None),
    (18, "Giá Bitcoin hôm nay bao nhiêu?", "decline", None),
    (19, "Trong khoá học, giảng viên dạy cách deploy Kubernetes cluster production thế nào?", "decline", None),
    (20, "nó là gì?", "decline", None),
    (21, "Viết giúp mình email xin nghỉ việc gửi sếp.", "decline", None),
    (22, "Ma trận impact-effort dùng để làm gì?", "locate", "bài toán kinh doanh"),
    (23, "Workflow pattern chaining và routing là gì?", "locate", "Soi bài toán"),
    (24, "Guardrail trong hệ thống AI dùng để kiểm soát hallucination thế nào?", "locate", "đánh giá"),
    (25, "Buổi trước thầy nói cái đó là gì?", "decline", None),
    (26, "Chấm và sửa giúp mình đoạn code Python này để nộp bài.", "decline", None),
    (27, "chào bạn, mình chưa hiểu về RAG", "answer", None),
    (28, "giải thích kỹ cơ chế transformer", "answer", None),
    (29, "giair thích cơ chế attention, mutilhead", "answer", None),
    (30, "agent la gi", "answer", None),
    (31, "augmentted chatbot khác gì agent ?", "answer", None),
    (32, "ai dùng từ vibe code đầu tiên", "answer", None),
    (33, "hãy giải thích rõ temperature và top_p", "answer", None),
    (34, '"Context" là gì', "answer", None),
    (35, "xem bài tập thực hành lab day 2 chiều nay ở đaau", "decline", None),
    (36, "điêu toa", "decline", None),
]

DECLINE_PHRASES = (
    "chưa tìm thấy", "không tìm thấy", "không đủ", "không có trong",
    "ngoài phạm vi", "không nằm trong", "chưa có", "không thể soạn",
    "không thể chấm", "hỏi lại", "cung cấp thêm", "không rõ",
)


def should_decline(qid: int, found: bool, answer: str) -> bool:
    low = answer.lower()
    if not found:
        return True
    if any(p in low for p in DECLINE_PHRASES):
        return True
    if qid in {20, 25, 36} and len(answer) < 120:
        return True
    return False


def grade(qid: int, expect: str, hint: str | None, retr: dict, gen: dict) -> tuple[bool, str]:
    found = bool(retr.get("found"))
    answer = gen.get("answer", "")
    sources = retr.get("sources") or []
    topic = (retr.get("topic") or "").lower()
    day_label = retr.get("day_label") or ""

    if expect == "decline":
        ok = should_decline(qid, found, answer)
        return ok, "declined/not found" if ok else "fabricated or over-answered"

    if expect == "locate":
        if not found:
            return False, "not found"
        if hint and hint.lower() not in topic and hint.lower() not in day_label.lower():
            # also check answer topic keywords
            if hint.lower() not in answer.lower():
                return False, f"wrong locate: {day_label} / {retr.get('topic')}"
        if len(sources) < 1:
            return False, "no sources"
        return True, f"located {day_label} — {retr.get('topic')}"

    # expect answer
    if not found:
        return False, "not found"
    if len(answer.strip()) < 40:
        return False, "answer too short"
    if not sources:
        return False, "no sources"
    if hint == "70" and "70" not in answer:
        return False, "missing 70% in answer"
    codes = re.findall(r"\[T\d{2}-\d{3}\]", answer)
    if not codes and expect == "answer":
        # extractive mode may put codes in bullets without brackets — check sources cited
        src_codes = [s.get("segment_code", "") for s in sources[:3]]
        if not any(c in answer for c in src_codes):
            return False, "no segment citation visible"
    return True, "answered with grounding"


def main() -> None:
    print("Ingesting transcripts…")
    ingest_mod.run(reset=True)

    rows = []
    passed = 0
    for qid, question, expect, hint in CASES:
        retr = retrieve(question)
        gen = generate(question, retr)
        ok, note = grade(qid, expect, hint, retr, gen)
        passed += int(ok)
        rows.append({
            "id": f"Q{qid:02d}",
            "question": question,
            "expect": expect,
            "pass": ok,
            "note": note,
            "found": bool(retr.get("found")),
            "day": retr.get("day_label"),
            "topic": retr.get("topic"),
            "mode": gen.get("mode"),
            "sources": "; ".join(
                f"{s.get('segment_code')}({s.get('score')})" for s in (retr.get("sources") or [])[:3]
            ),
            "answer_preview": (gen.get("answer") or "")[:280].replace("\n", " ").strip(),
        })
        mark = "PASS" if ok else "FAIL"
        print(f"Q{qid:02d} {mark}: {note}")

    total = len(CASES)
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    out_md = EVAL_DIR / "run-1-results.md"
    out_csv = EVAL_DIR / "run-1-results.csv"

    with out_csv.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()), lineterminator="\n")
        w.writeheader()
        w.writerows(rows)

    lines = [
        "# Kết quả chạy thử lần 1 — VLearn Tutor RAG",
        "",
        f"**Thời điểm:** {ts}",
        f"**Kết quả:** **{passed}/{total}** câu đạt",
        f"**Môi trường:** `dev_` branch · embed=`tfidf` · LLM=`extractive` (không API key)",
        f"**Bộ câu:** `eval/golden-set.md` (36 câu)",
        "",
        "## Tóm tắt",
        "",
        f"| Metric | Giá trị |",
        f"|---|---|",
        f"| Tổng câu | {total} |",
        f"| Pass | {passed} |",
        f"| Fail | {total - passed} |",
        f"| Tỷ lệ | {100*passed/total:.1f}% |",
        "",
        "## Bảng chi tiết (cả câu fail)",
        "",
        "| ID | Pass | Found | Day | Topic | Ghi chú |",
        "|---|:---:|---|---|---|---|",
    ]
    for r in rows:
        p = "✅" if r["pass"] else "❌"
        lines.append(
            f"| {r['id']} | {p} | {r['found']} | {r['day'] or '-'} | "
            f"{(r['topic'] or '-')[:40]} | {r['note']} |"
        )

    lines += ["", "## Chi tiết từng câu", ""]
    for r in rows:
        p = "PASS" if r["pass"] else "FAIL"
        lines += [
            f"### {r['id']} — {p}",
            f"- **Đưa vào:** {r['question']}",
            f"- **Kỳ vọng:** {r['expect']}",
            f"- **Found:** {r['found']} · **Mode:** {r['mode']}",
            f"- **Locate:** {r['day']} — {r['topic']}",
            f"- **Sources:** {r['sources'] or '(none)'}",
            f"- **Đánh giá:** {r['note']}",
            f"- **Trả lời (rút gọn):** {r['answer_preview']}",
            "",
        ]

    out_md.write_text("\n".join(lines), encoding="utf-8")
    print(f"\n==> {passed}/{total} — wrote {out_md} and {out_csv}")


if __name__ == "__main__":
    main()
