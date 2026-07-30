"""OCR PDF/image files with Gemini, embed their text, and persist in ChromaDB."""
from __future__ import annotations

import argparse
import hashlib
import json
import mimetypes
import os
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import chromadb
import fitz
from dotenv import load_dotenv
from google import genai
from google.genai import types

SUPPORTED = {".png", ".jpg", ".jpeg", ".webp", ".tif", ".tiff", ".bmp", ".pdf"}
OCR_PROMPT = """Transcribe all visible text in this slide/document image accurately.
Preserve the natural reading order, headings, bullet points, formulas, and table rows.
Keep the original language and spelling. Do not summarize, explain, or wrap the result
in Markdown code fences. Return only the transcription. If no text is visible, return
an empty string."""


@dataclass(frozen=True)
class Page:
    source: Path
    page_number: int
    data: bytes
    mime_type: str


def arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=Path("data/slides"))
    parser.add_argument("--db", type=Path, default=Path("data/chroma_db"))
    parser.add_argument("--ocr-output", type=Path, default=Path("data/ocr"))
    parser.add_argument("--collection", default="slides_ocr")
    parser.add_argument("--ocr-model", default="gemini-2.5-flash")
    parser.add_argument("--embedding-model", default="gemini-embedding-001")
    parser.add_argument("--embedding-dim", type=int, default=768)
    parser.add_argument("--chunk-size", type=int, default=1200)
    parser.add_argument("--chunk-overlap", type=int, default=200)
    parser.add_argument("--pdf-dpi", type=int, default=160)
    parser.add_argument("--batch-size", type=int, default=50)
    parser.add_argument("--retries", type=int, default=3)
    parser.add_argument("--resume", action="store_true", help="Reuse completed OCR JSON files")
    return parser.parse_args()


def find_files(folder: Path) -> list[Path]:
    return sorted(p for p in folder.rglob("*") if p.is_file() and p.suffix.lower() in SUPPORTED)


def pages(path: Path, pdf_dpi: int) -> Iterable[Page]:
    if path.suffix.lower() != ".pdf":
        mime = mimetypes.guess_type(path.name)[0] or "image/png"
        yield Page(path, 1, path.read_bytes(), mime)
        return
    scale = pdf_dpi / 72
    with fitz.open(path) as document:
        for index, pdf_page in enumerate(document):
            pixmap = pdf_page.get_pixmap(matrix=fitz.Matrix(scale, scale), alpha=False)
            yield Page(path, index + 1, pixmap.tobytes("png"), "image/png")


def chunks(text: str, size: int, overlap: int) -> list[str]:
    if size <= overlap or overlap < 0:
        raise ValueError("chunk-size must be greater than chunk-overlap >= 0")
    result, start = [], 0
    while start < len(text):
        end = min(len(text), start + size)
        if end < len(text):
            boundary = max(text.rfind(mark, start + size // 2, end) for mark in ("\n", ". ", " "))
            if boundary >= 0:
                end = boundary + 1
        value = text[start:end].strip()
        if value:
            result.append(value)
        if end >= len(text):
            break
        start = max(start + 1, end - overlap)
    return result


def retry(call, retries: int):
    for attempt in range(retries + 1):
        try:
            return call()
        except Exception:
            if attempt == retries:
                raise
            time.sleep(2**attempt)


def ocr_page(client: genai.Client, page: Page, model: str, retries: int) -> str:
    response = retry(
        lambda: client.models.generate_content(
            model=model,
            contents=[OCR_PROMPT, types.Part.from_bytes(data=page.data, mime_type=page.mime_type)],
            config=types.GenerateContentConfig(temperature=0),
        ), retries,
    )
    return (response.text or "").strip()


def embed_documents(client, documents, model, dimension, batch_size, retries):
    vectors = []
    for start in range(0, len(documents), batch_size):
        batch = documents[start:start + batch_size]
        response = retry(
            lambda: client.models.embed_content(
                model=model, contents=batch,
                config=types.EmbedContentConfig(
                    task_type="RETRIEVAL_DOCUMENT", output_dimensionality=dimension
                ),
            ), retries,
        )
        vectors.extend(embedding.values for embedding in response.embeddings)
    return vectors


def main() -> None:
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    args = arguments()
    load_dotenv()
    if not os.getenv("GEMINI_API_KEY"):
        raise SystemExit("GEMINI_API_KEY is missing. Add it to .env or the environment.")
    files = find_files(args.input)
    if not files:
        raise SystemExit(f"No supported PDF/image files found in {args.input}")
    if args.embedding_dim <= 0 or args.batch_size <= 0:
        raise SystemExit("embedding-dim and batch-size must be positive")

    args.db.mkdir(parents=True, exist_ok=True)
    args.ocr_output.mkdir(parents=True, exist_ok=True)
    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    collection = chromadb.PersistentClient(path=str(args.db)).get_or_create_collection(
        name=args.collection,
        metadata={"hnsw:space": "cosine", "embedding_model": args.embedding_model},
    )
    ids, documents, metadatas = [], [], []
    for path in files:
        relative = path.relative_to(args.input).as_posix()
        output_stem = hashlib.sha1(relative.encode("utf-8")).hexdigest()[:10] + "-" + path.stem
        json_path = args.ocr_output / f"{output_stem}.json"
        if args.resume and json_path.exists():
            page_results = json.loads(json_path.read_text(encoding="utf-8"))["pages"]
            print(f"RESUME: {relative} ({len(page_results)} pages)", flush=True)
        else:
            page_results = []
            for page in pages(path, args.pdf_dpi):
                print(f"OCR: {relative} (page {page.page_number})", flush=True)
                text = ocr_page(client, page, args.ocr_model, args.retries)
                page_results.append({"page": page.page_number, "text": text})
        for page_result in page_results:
            text = page_result["text"]
            page_number = page_result["page"]
            for index, chunk in enumerate(chunks(text, args.chunk_size, args.chunk_overlap)):
                identity = f"{relative}:{page_number}:{index}:{chunk}"
                ids.append(hashlib.sha256(identity.encode("utf-8")).hexdigest())
                documents.append(chunk)
                metadatas.append({
                    "source": path.as_posix(), "relative_source": relative,
                    "filename": path.name, "page": page_number,
                    "chunk_index": index, "ocr_model": args.ocr_model,
                })
        output_stem = hashlib.sha1(relative.encode("utf-8")).hexdigest()[:10] + "-" + path.stem
        (args.ocr_output / f"{output_stem}.txt").write_text(
            "\n\n".join(item["text"] for item in page_results), encoding="utf-8"
        )
        (args.ocr_output / f"{output_stem}.json").write_text(
            json.dumps({"source": path.as_posix(), "pages": page_results}, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
    if not documents:
        raise SystemExit("OCR completed but no text was detected.")
    print(f"Embedding {len(documents)} chunks with {args.embedding_model}", flush=True)
    vectors = embed_documents(
        client, documents, args.embedding_model, args.embedding_dim, args.batch_size, args.retries
    )
    collection.upsert(ids=ids, documents=documents, metadatas=metadatas, embeddings=vectors)
    print(f"Done: {len(files)} files, {len(documents)} chunks, collection '{args.collection}' at {args.db}")


if __name__ == "__main__":
    main()
