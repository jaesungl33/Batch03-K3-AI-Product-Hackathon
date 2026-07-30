"""Query the slides Chroma collection directly or through a Gemini tool-using agent."""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

import chromadb
from dotenv import load_dotenv
from google import genai
from google.genai import types


def arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", help="Question or semantic search query")
    parser.add_argument("--db", type=Path, default=Path("data/chroma_db"))
    parser.add_argument("--collection", default="slides_ocr")
    parser.add_argument("--embedding-model", default="gemini-embedding-001")
    parser.add_argument("--embedding-dim", type=int, default=768)
    parser.add_argument("--top-k", type=int, default=4)
    parser.add_argument("--agent", action="store_true", help="Let Gemini call the search tool and answer")
    parser.add_argument("--agent-model", default="gemini-2.5-flash")
    return parser.parse_args()


def query_embedding(client: genai.Client, query: str, model: str, dimension: int) -> list[float]:
    response = client.models.embed_content(
        model=model,
        contents=query,
        config=types.EmbedContentConfig(
            task_type="RETRIEVAL_QUERY", output_dimensionality=dimension
        ),
    )
    return response.embeddings[0].values


def search_collection(client, collection, query, model, dimension, top_k):
    vector = query_embedding(client, query, model, dimension)
    result = collection.query(
        query_embeddings=[vector],
        n_results=top_k,
        include=["documents", "metadatas", "distances"],
    )
    return [
        {
            "text": document,
            "source": metadata["relative_source"],
            "page": metadata["page"],
            "distance": round(distance, 4),
        }
        for document, metadata, distance in zip(
            result["documents"][0], result["metadatas"][0], result["distances"][0]
        )
    ]


def main() -> None:
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    args = arguments()
    load_dotenv()
    if not os.getenv("GEMINI_API_KEY"):
        raise SystemExit("GEMINI_API_KEY is missing")
    if args.top_k <= 0:
        raise SystemExit("top-k must be positive")

    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    collection = chromadb.PersistentClient(path=str(args.db)).get_collection(args.collection)

    def search_slides(query: str) -> list[dict]:
        """Search course slides for passages relevant to the user's question.

        Args:
            query: A focused Vietnamese or English semantic search query.
        """
        print(f"[tool] search_slides(query={query!r})", flush=True)
        matches = search_collection(
            client, collection, query, args.embedding_model, args.embedding_dim, args.top_k
        )
        for index, match in enumerate(matches, 1):
            print(
                f"  [{index}] distance={match['distance']} source={match['source']} page={match['page']}",
                flush=True,
            )
        return matches

    if not args.agent:
        for index, match in enumerate(search_slides(args.query), 1):
            print(f"\n--- Result {index} ---")
            print(match["text"])
        return

    response = client.models.generate_content(
        model=args.agent_model,
        contents=args.query,
        config=types.GenerateContentConfig(
            system_instruction=(
                "Bạn là trợ lý hỏi đáp slide. Luôn gọi search_slides trước khi trả lời. "
                "Chỉ dùng dữ kiện từ kết quả tool; nếu không đủ dữ kiện, nói rõ. "
                "Trả lời ngắn gọn bằng tiếng Việt và nêu source/page."
            ),
            tools=[search_slides],
            temperature=0,
        ),
    )
    print("\n[agent answer]")
    print(response.text)


if __name__ == "__main__":
    main()


