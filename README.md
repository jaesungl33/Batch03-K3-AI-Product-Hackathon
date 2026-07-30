# VLearn Tutor — RAG cho khoá AI Thực Chiến

Trợ lý ôn tập cho học viên VLearn. Học viên hỏi một kiến thức bất kỳ; hệ thống
**xác định kiến thức đó được dạy ở buổi nào**, **tóm tắt cách nó được giảng trên
lớp**, và **mở đúng đoạn nguồn chi tiết** (mã đoạn `[Txx-NNN]` từ transcript) khi
cần. Lab Coach nạp học liệu qua một giao diện riêng.

Chạy trực tiếp trên dữ liệu thật trong data pack (`data/transcript/` — 6 transcript
bài giảng, ~640 đoạn có mã trích dẫn).

## Hai giao diện (đúng use case đã chốt)

- **🎓 Học viên** — giao diện chat thuần. Hỏi → pipeline 2 tầng chạy → trả lời tóm
  tắt kèm nguồn. Slide/nguồn chi tiết chỉ **pull-up** ở panel bên khi bấm vào.
- **🧑‍🏫 Lab Coach** — bảng điều khiển nạp & embed học liệu, xem pipeline ingest và
  tồn kho học liệu theo buổi/chủ đề.

## Kiến trúc

```
Coach nạp transcript ──► parse [Txx-NNN] ──► gắn metadata (day/topic/section/type)
                                              └► embed ──► ChromaDB (collection: vlearn_lectures)

Học viên hỏi ──► [Tầng 1] tìm toàn bộ, vote ra (day, topic)  ◄── định vị "buổi nào"
             ──► [Tầng 2] tìm lại có filter theo day ──► context đầy đủ
             ──► tóm tắt (Claude nếu có API key, hoặc extractive) + trích mã đoạn
             ──► cross-link: tìm học liệu type=lab cùng buổi
```

Điểm cốt lõi: **retrieval 2 tầng**. Tầng 1 định vị *buổi/chủ đề* từ metadata;
tầng 2 lấy *context đầy đủ* có filter — nên hệ thống "biết" kiến thức nằm ở buổi
nào thay vì trả lời từ một đoạn lẻ.

## Chạy

```bash
cp .env.example .env      # tuỳ chọn: điền ANTHROPIC_API_KEY để Claude viết câu trả lời
./run.sh                  # cài deps, ingest, mở http://localhost:8000
```

Không có API key vẫn chạy đầy đủ: câu trả lời dùng bản tóm tắt extractive từ chính
các đoạn transcript (vẫn grounded, vẫn trích mã đoạn).

Muốn chạy hoàn toàn offline (không tải model): đặt `VLEARN_EMBED=tfidf` trong `.env`.

## Cấu trúc mã

```
backend/
  config.py       # cấu hình, đường dẫn, chọn backend
  embeddings.py   # sentence-transformers (mặc định) | tfidf (offline)
  store.py        # wrapper ChromaDB (lưu embedding + metadata)
  ingest.py       # parse transcript [Txx-NNN] → chunk + metadata → embed
  retrieval.py    # retrieval 2 tầng + cross-link lab
  llm.py          # sinh câu trả lời (Claude | extractive fallback)
  main.py         # FastAPI: /api/chat, /api/ingest, /api/inventory, phục vụ frontend
frontend/
  index.html      # landing chọn vai trò + chat học viên + dashboard coach
data/transcript/  # 6 transcript bài giảng (data pack)
```

## API

| Method | Endpoint | Việc |
|---|---|---|
| POST | `/api/chat` | `{question}` → answer + day + topic + sources[] + lab[] |
| POST | `/api/ingest` | (re)build cơ sở tri thức từ transcript |
| GET | `/api/inventory` | tồn kho học liệu theo buổi/chủ đề |
| GET | `/api/health` | trạng thái, backend embed, số đoạn |
| GET | `/api/questions?status=pending` | danh sách câu hỏi đang chờ giảng viên |
| POST | `/api/questions/{ticket_id}/answer` | lưu câu trả lời đã xác nhận và đóng ticket |

Khi `/api/chat` không tìm thấy căn cứ, backend tạo ticket trong
`data/teacher_questions.sqlite3` và trả `status="escalated"` cùng `ticket_id`.
Giao diện Lab Coach tự tải hàng đợi này; sau khi Coach gửi câu trả lời, ticket
chuyển từ `pending` sang `answered`.

## Mở rộng (roadmap gợi ý cho demo)

- Thêm `slides/` khi ban tổ chức phát hành → thêm `type=slide`, render trang slide
  thật trong panel nguồn thay vì đoạn transcript.
- Thêm học liệu `type=lab` → phần cross-link "bài lab cùng buổi" sẽ có dữ liệu thật.
- Đổi vote tầng 1 sang rerank bằng cross-encoder để định vị buổi chính xác hơn.

## Lưu ý bảo mật dữ liệu

Data pack chỉ dùng trong phạm vi hackathon. Không commit nguyên transcript vào repo
công khai; trích dẫn bằng mã đoạn `[Txx-NNN]`. Xem `data/vlearn-pack/README.md`.
