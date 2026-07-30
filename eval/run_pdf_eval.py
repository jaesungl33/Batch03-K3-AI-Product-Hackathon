"""Run questions grounded in the two supplied PDFs through the Gemini slide agent."""
from __future__ import annotations

import csv
import argparse
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

import app as vlearn  # noqa: E402

EVAL_DIR = Path(__file__).parent
CASES_FILE = EVAL_DIR / "pdf-golden-set.json"
SOURCE_ALIASES = {
    "d1-slide-hackathon.pdf": ("d1-slide-hackathon.pdf", "day01-slide-blue-v1.pdf"),
    "d2-slide-hackathon.pdf": (
        "d2-slide-hackathon.pdf",
        "Day02 - Xác định bài toán kinh doanh - Teacher.pdf",
    ),
}


def cleanup(tickets: list[str]) -> None:
    if not tickets:
        return
    marks = ",".join("?" for _ in tickets)
    with vlearn.database() as connection:
        connection.execute(f"DELETE FROM questions WHERE id IN ({marks})", tickets)


def arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, default=1)
    parser.add_argument("--end", type=int)
    parser.add_argument("--delay", type=float, default=9.0)
    parser.add_argument("--suffix", default="")
    return parser.parse_args()


def main() -> None:
    args = arguments()
    cases = json.loads(CASES_FILE.read_text(encoding="utf-8"))
    cases = cases[args.start - 1 : args.end]
    vlearn.init_database()
    rows = []
    tickets: list[str] = []
    try:
        for index, case in enumerate(cases, 1):
            started = time.perf_counter()
            error = ""
            try:
                result = vlearn.chat(vlearn.ChatRequest(question=case["question"]))
            except Exception as exc:
                result = {"status": "error", "answer": "", "sources": []}
                error = f"{type(exc).__name__}: {exc}"
            latency = round((time.perf_counter() - started) * 1000)
            if result.get("ticket_id"):
                tickets.append(result["ticket_id"])

            answer = result.get("answer", "")
            sources = result.get("sources", [])
            status_ok = result.get("status") == case["expected_status"]
            keyword_ok = all(
                keyword.casefold() in answer.casefold() for keyword in case["keywords"]
            )
            if case["expected_status"] == "answered":
                pdf_ok = any(
                    source.get("source_file", "").casefold()
                    in {alias.casefold() for alias in SOURCE_ALIASES[case["pdf"]]}
                    for source in sources
                )
                source_ok = bool(sources) and pdf_ok
            else:
                source_ok = not sources
            passed = status_ok and keyword_ok and source_ok and not error
            rows.append(
                {
                    "id": case["id"],
                    "question": case["question"],
                    "expected_status": case["expected_status"],
                    "actual_status": result.get("status"),
                    "pass": passed,
                    "status_ok": status_ok,
                    "keyword_ok": keyword_ok,
                    "source_ok": source_ok,
                    "expected_pdf": case["pdf"] or "",
                    "expected_page": case["page"] or "",
                    "sources": "; ".join(
                        f"{s.get('source_file')} {s.get('segment_code')}"
                        for s in sources
                    ),
                    "confidence": result.get("confidence"),
                    "latency_ms": latency,
                    "answer_preview": answer[:300].replace("\n", " "),
                    "error": error,
                }
            )
            print(
                f"[{index:02d}/{len(cases)}] {case['id']} "
                f"{'PASS' if passed else 'FAIL'} {result.get('status')} {latency}ms",
                flush=True,
            )
            if index < len(cases):
                time.sleep(args.delay)
    finally:
        cleanup(tickets)

    passed = sum(row["pass"] for row in rows)
    total = len(rows)
    suffix = f"-{args.suffix}" if args.suffix else ""
    output_csv = EVAL_DIR / f"pdf-run-results{suffix}.csv"
    with output_csv.open("w", newline="", encoding="utf-8") as target:
        writer = csv.DictWriter(
            target, fieldnames=rows[0].keys(), lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(rows)

    lines = [
        "# Kết quả golden set theo PDF",
        "",
        f"**Thời điểm:** {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}  ",
        f"**Kết quả:** **{passed}/{total} ({100 * passed / total:.1f}%)**  ",
        "**Nguồn dương tính:** `d1-slide-hackathon.pdf`, `d2-slide-hackathon.pdf`  ",
        "**Agent:** Gemini embedding + semantic relevance gate + grounded answer",
        "",
        "| ID | Kỳ vọng | Thực tế | PDF nguồn đúng | Keyword đúng | Kết quả | Latency |",
        "|---|---|---|:---:|:---:|:---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| {row['id']} | {row['expected_status']} | {row['actual_status']} | "
            f"{'✅' if row['source_ok'] else '❌'} | "
            f"{'✅' if row['keyword_ok'] else '❌'} | "
            f"{'✅' if row['pass'] else '❌'} | {row['latency_ms']} ms |"
        )
    failed = [row for row in rows if not row["pass"]]
    lines += ["", "## Case chưa đạt", ""]
    if not failed:
        lines.append("Không có.")
    for row in failed:
        lines += [
            f"### {row['id']}",
            f"- Câu hỏi: {row['question']}",
            f"- Lỗi: {row['error'] or 'Sai route/source/keyword'}",
            f"- Sources: {row['sources'] or '(none)'}",
            f"- Answer: {row['answer_preview']}",
            "",
        ]
    (EVAL_DIR / f"pdf-run-results{suffix}.md").write_text(
        "\n".join(lines) + "\n", encoding="utf-8"
    )
    print(f"==> {passed}/{total}", flush=True)


if __name__ == "__main__":
    main()
