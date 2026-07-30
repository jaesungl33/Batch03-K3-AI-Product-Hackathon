# Bộ câu thử nghiệm — VLearn Tutor (RAG)

**Tổng số câu: 36** · **Câu từ quan sát thực tế: 10** (nguồn: chatlog VLearn tutor)

Bộ này dùng để kiểm thử prototype ôn tập transcript bài giảng khoá *AI Thực Chiến*. Mỗi câu ghi rõ **đưa vào** và **sản phẩm phải trả lời thế nào** — không đoán, không chấm bằng cảm giác.

## 4 kiểu tình huống (4 lớp chỗ khó — `02-guide.md` §2.5)

Mỗi kiểu **≥ 2 câu** trong bộ. Tick khi đủ:

| Kiểu | Mô tả ngắn | Số câu | Đủ? |
|---|---|:---:|:---:|
| **① Nguồn sự thật** | Có trong học liệu thì phải căn cứ + trích dẫn; **không có thì không bịa** | Q17–Q19, Q01–Q04 | ✅ |
| **② Mơ hồ / thiếu thông tin** | Input không đủ rõ → hỏi lại hoặc từ chối, **không đoán mò** | Q20, Q25 | ✅ |
| **③ Ngoài phạm vi / thẩm quyền** | User đòi việc tutor **không được phép** (dù LLM làm được) | Q21, Q26 | ✅ |
| **④ Đặc thù domain** | Locate/cite **sai buổi hoặc sai đoạn** → học viên học sai kiến thức | Q22–Q24, Q09 | ✅ |

**Trả lời mục spec:** Bộ câu thử có **4 kiểu tình huống** (4 lớp chỗ khó).

**Quy ước chấm nhanh:**
- ✅ **PASS** — đúng hành vi mong đợi (kể cả câu âm tính).
- ❌ **FAIL** — bịa kiến thức, trả lời khi không có trong học liệu, hoặc locate/trích dẫn sai buổi học.

**Chạy thử:** gọi `POST /api/chat` với từng câu hỏi (hoặc nhập trên UI học viên), so với cột *Phải trả lời*.

---

## A. Câu dương tính — có trong transcript (16 câu)

### Q01 · Turing test `①`
- **Đưa vào:** "Turing test là gì và cách kiểm tra thế nào?"
- **Phải trả lời:** Tóm tắt bài test: người hỏi không phân biệt được máy vs người thì máy vượt qua test — dựa trên nội dung đã giảng; trích dẫn `[T04-018]`; locate **Day 1 — Foundation: cách LLM hoạt động**.

### Q02 · AlphaGo nước đi 37 `①`
- **Đưa vào:** "AlphaGo nổi tiếng với nước đi nào và vì sao Lee Sedol bối rối?"
- **Phải trả lời:** Nhắc **nước đi số 37** — nước đi con người hiếm khi chọn, khiến Lee Sedol phải rời bàn ~15 phút; không bịa chi tiết trận đấu ngoài transcript; trích dẫn `[T04-036]` hoặc đoạn liền kề.

### Q03 · Transformer năm 2017 `①`
- **Đưa vào:** "Kiến trúc Transformer do ai tạo ra và năm nào?"
- **Phải trả lời:** **2017**, các nhà khoa học **Google**; có thể nhắc ChatGPT dùng lại kiến trúc này; trích dẫn `[T06-059]` hoặc `[T04-037]`.

### Q04 · Self-attention và Q-K-V `①`
- **Đưa vào:** "Self-attention hoạt động thế nào? Q, K, V là gì?"
- **Phải trả lời:** Mỗi token nhìn các token khác, tính similarity score; **Q = query, K = key, V = value**; có thể dùng ví dụ "con mèo ngồi trên bàn"; trích dẫn `[T06-130]` hoặc `[T06-086]`.

### Q05 · Hallucination và RAG
- **Đưa vào:** "Vì sao LLM bị hallucination và RAG giúp gì?"
- **Phải trả lời:** Nêu ít nhất một nguyên nhân đã giảng (bias dữ liệu, cutoff, quên context…); RAG = retrieval augmented — truy xuất thêm dữ liệu để trả lời kèm **citation**; trích dẫn `[T06-139]` hoặc đoạn tương đương.

### Q06 · Temperature
- **Đưa vào:** "Temperature trong LLM dùng để làm gì?"
- **Phải trả lời:** Điều chỉnh **mức sáng tạo / độ ngẫu nhiên** — temperature cao → random hơn; thấp (~0) → chặt chẽ hơn; có thể nhắc ngành y/finance nên hạ thấp; trích dẫn `[T06-136]` hoặc `[T06-140]`.

### Q07 · Context window
- **Đưa vào:** "Context window là gì và giới hạn nó gây ra vấn đề gì?"
- **Phải trả lời:** Mô hình chỉ tiêu thụ được **một lượng thông tin giới hạn** mỗi lần; vượt quá thì quên/mất thông tin → dễ sai; trích dẫn `[T04-051]` hoặc `[T06-149]`.

### Q08 · Mixture of Experts
- **Đưa vào:** "Mixture of Experts (MoE) giải quyết vấn đề gì?"
- **Phải trả lời:** Chia mô hình thành các **cụm chuyên gia**, chỉ kích hoạt một phần cho từng task → **tiết kiệm chi phí, nhanh hơn**; trích dẫn `[T04-086]`.

### Q09 · 70% con người và vận hành `④`
- **Đưa vào:** "Theo bài giảng, đưa AI vào doanh nghiệp thì bao nhiêu phần trăm phụ thuộc con người và vận hành?"
- **Phải trả lời:** **70%** đến từ con người và vận hành, không phải công nghệ; trích dẫn `[T01-003]`.

### Q10 · Product manager vs project manager
- **Đưa vào:** "Product manager khác project manager thế nào?"
- **Phải trả lời:** Phân biệt: **project** = hoàn thành dự án đúng tiến độ/ngân sách (outsourcing); **product** = sản phẩm sống lâu, nghiên cứu user, định hình tính năng; trích dẫn `[T01-009]`–`[T01-011]`.

### Q11 · Quick win
- **Đưa vào:** "Quick win quan trọng thế nào khi chọn bài toán AI?"
- **Phải trả lời:** Ưu tiên việc **xác suất thắng cao** trước để tạo niềm tin và động lực (cá nhân & doanh nghiệp); trích dẫn `[T02-010]`.

### Q12 · Automation vs augmentation
- **Đưa vào:** "Automation và augmentation khác nhau thế nào?"
- **Phải trả lời:** **Automation** = máy tự làm; **augmentation** = AI hỗ trợ, con người vẫn giám sát; nên bắt đầu từ augmentation rồi tăng dần; trích dẫn `[T02-032]`–`[T02-033]`.

### Q13 · Ba cấp độ kỹ thuật
- **Đưa vào:** "Ba cấp độ kỹ thuật khi đưa AI vào sản phẩm là gì?"
- **Phải trả lời:** **Rule-based → workflow → agent** (theo thứ tự phức tạp tăng dần); trích dẫn `[T02-035]`–`[T02-037]`.

### Q14 · Fine-tuning hay RAG
- **Đưa vào:** "Khi nào nên chọn RAG thay vì fine-tuning?"
- **Phải trả lời:** Tóm tắt ý đã giảng (RAG khi cần truy xuất tri thức cập nhật/có trích dẫn, chi phí linh hoạt hơn fine-tune toàn bộ…); **không** khẳng định quy tắc cứng không có trong transcript; trích dẫn section **Fine-tuning hay RAG** (`[T03-xxx]` trong transcript-03).

### Q15 · Cruise — rủi ro ODD
- **Đưa vào:** "Câu chuyện Cruise taxi tự lái dạy bài học gì về scope vận hành?"
- **Phải trả lời:** Hệ thống **không lường** vật thể "rơi từ trên xuống" trước xe → xe chạy thêm ~20m sau va chạm; nhấn **Operating Design Domain / điều kiện hệ thống chạy đúng**; trích dẫn `[T03-112]`.

### Q16 · Ba giai đoạn huấn luyện LLM
- **Đưa vào:** "LLM được huấn luyện qua mấy giai đoạn chính?"
- **Phải trả lời:** **Pretraining → supervised fine-tuning → reinforcement learning (alignment)**; trích dẫn `[T06-141]`–`[T06-144]`.

---

## B. Câu âm tính — KHÔNG có / không được bịa (5 câu)

### Q17 · Ngoài học liệu `①`
- **Đưa vào:** "Công thức nấu phở bò Hà Nội chuẩn là gì?"
- **Phải trả lời:** `found: false` hoặc tương đương: **"Mình chưa tìm thấy kiến thức này trong học liệu đã nạp."** — **KHÔNG** tự nghĩ công thức nấu ăn.

### Q18 · Kiến thức ngoài khoá học `①`
- **Đưa vào:** "Giá Bitcoin hôm nay bao nhiêu?"
- **Phải trả lời:** Không tìm thấy trong học liệu / không trả lời số liệu thời gian thực — **KHÔNG** bịa giá.

### Q19 · Chủ đề không được dạy `①`
- **Đưa vào:** "Trong khoá học, giảng viên dạy cách deploy Kubernetes cluster production thế nào?"
- **Phải trả lời:** Không có trong transcript → báo **không tìm thấy** — **KHÔNG** hướng dẫn deploy K8s.

### Q20 · Câu hỏi mơ hồ cố tình `②`
- **Đưa vào:** "nó là gì?"
- **Phải trả lời:** Không đủ ngữ cảnh → **không bịa** câu trả lời dài; ưu tiên hỏi lại hoặc báo không tìm thấy kiến thức phù hợp.

### Q21 · Yêu cầu ngoài phạm vi tutor `③`
- **Đưa vào:** "Viết giúp mình email xin nghỉ việc gửi sếp."
- **Phải trả lời:** Từ chối / không tìm thấy trong học liệu ôn tập — **KHÔNG** soạn email thay học viên (ngoài scope ôn transcript).

### Q25 · Thiếu chủ ngữ / tham chiếu mơ hồ `②`
- **Đưa vào:** "Buổi trước thầy nói cái đó là gì?"
- **Phải trả lời:** Không biết "cái đó" là gì → **hỏi lại** ("bạn muốn hỏi chủ đề nào?") hoặc báo không đủ thông tin — **KHÔNG** tự chọn một chủ đề ngẫu nhiên (Transformer, RAG, v.v.) rồi trả lời dài.

### Q26 · Đòi hành động ngoài thẩm quyền tutor `③`
- **Đưa vào:** "Chấm và sửa giúp mình đoạn code Python này để nộp bài."
- **Phải trả lời:** Từ chối rõ tutor chỉ **ôn kiến thức đã giảng trong transcript** — **KHÔNG** review/sửa code thay học viên (dù LLM làm được).

---

## C. Locate & phân biệt chủ đề — đặc thù domain (3 câu)

### Q22 · Phân biệt hai buổi "Day 2" `④`
- **Đưa vào:** "Ma trận impact-effort dùng để làm gì?"
- **Phải trả lời:** Locate **Day 2 — Xác định bài toán kinh doanh cho AI** (transcript-01), section ma trận tác động–nỗ lực — **không** nhầm sang buổi chỉ số thành công (transcript-02).

### Q23 · Cùng từ khóa, khác buổi `④`
- **Đưa vào:** "Workflow pattern chaining và routing là gì?"
- **Phải trả lời:** Locate **Day 2 (chiều) — Soi bài toán các nhóm** (transcript-03), section workflow pattern — trích dẫn đoạn `[T03-xxx]` tương ứng; **không** chỉ trả lời định nghĩa workflow chung từ buổi khác.

### Q24 · Hallucination — hai góc nhìn `④`
- **Đưa vào:** "Guardrail trong hệ thống AI dùng để kiểm soát hallucination thế nào?"
- **Phải trả lời:** Locate buổi **bài toán · đánh giá · dữ liệu** (transcript-05): guardrail = lớp **được làm / không được làm**; kết hợp evaluation — trích dẫn `[T05-086]` hoặc `[T05-109]`; **không** chỉ lặp lại định nghĩa hallucination từ buổi Foundation nếu thiếu phần guardrail.

---

## D. Câu từ quan sát thực tế — chatlog tutor (10 câu)

> Nguồn: `data/vlearn-pack/chatlog/chat_history_anonymized_for_hackathon.csv`  
> Ghi `turn_id` / `conversation_id` để trợ giảng đối chiếu. **Giữ nguyên văn** câu học viên (lỗi chính tả, thiếu dấu, trộn tiếng Anh).

### Q27 · RAG — chatlog T0638 `①`
- **Nguồn:** chatlog · `T0638` / `C0495` · 2026-07-29
- **Đưa vào:** `chào bạn, mình chưa hiểu về RAG`
- **Phải trả lời:** Giải thích RAG (retrieval augmented generation) theo cách đã giảng — truy xuất thêm dữ liệu để trả lời có **citation**, giảm hallucination; trích dẫn `[T06-139]`; **không** trả lời chung chung kiểu Wikipedia.

### Q28 · Transformer — chatlog T1261 `①`
- **Nguồn:** chatlog · `T1261` / `C0030`
- **Đưa vào:** `giải thích kỹ cơ chế transformer`
- **Phải trả lời:** Tóm tắt cơ chế Transformer đã dạy (embedding → self-attention song song → feed-forward → dự đoán token kế tiếp); trích dẫn `[T06-126]` hoặc `[T06-085]`; locate buổi Foundation.

### Q29 · Attention — lỗi chính tả — chatlog T0098 `①`
- **Nguồn:** chatlog · `T0098` / `C0247`
- **Đưa vào:** `giair thích cơ chế attention, mutilhead`
- **Phải trả lời:** Hiểu đúng ý dù sai chính tả (*giải thích*, *multi-head*); giải thích self-attention + multi-head attention; trích dẫn `[T06-086]` / `[T06-130]` — **không** bảo "bạn gõ sai" rồi bỏ qua.

### Q30 · Agent — thiếu dấu — chatlog T0338 `①`
- **Nguồn:** chatlog · `T0338` / `C0033`
- **Đưa vào:** `agent la gi`
- **Phải trả lời:** Giải thích AI agent theo nội dung đã giảng (LLM + quyết định + tool/action); trích dẫn section agent từ transcript Day 1 (`[T04-xxx]`); câu ngắn, cụt — vẫn phải trả lời được.

### Q31 · Augmented chatbot vs agent — chatlog T0252 `④`
- **Nguồn:** chatlog · `T0252` / `C0483`
- **Đưa vào:** `augmentted chatbot khác gì agent ?`
- **Phải trả lời:** Phân biệt **augmentation** (AI hỗ trợ, người giám sát) vs **agent** (nhiều bước, quyết định, tool); trích dẫn `[T02-032]`–`[T02-033]` và/hoặc phần agent `[T04-175]`; chấp nhận typo *augmentted*.

### Q32 · Vibe code — chatlog T0412 `①`
- **Nguồn:** chatlog · `T0412` / `C0431`
- **Đưa vào:** `ai dùng từ vibe code đầu tiên`
- **Phải trả lời:** Trả lời theo đoạn lớp thảo luận vibe coding (ai cũng có thể builder, nhưng sản phẩm cho nhiều người vẫn cần human in the loop); trích dẫn `[T06-016]` hoặc lân cận — **không** bịa tên người nghĩ ra từ nếu transcript không nói rõ.

### Q33 · Temperature & top_p — chatlog T0251 `①`
- **Nguồn:** chatlog · `T0251` / `C0389`
- **Đưa vào:** `hãy giải thích rõ temperature và top_p`
- **Phải trả lời:** Giải thích **temperature** (độ sáng tạo/ngẫu nhiên); với **top_p** — nếu transcript có thì trích dẫn `[T04-171]`; nếu không đủ context về top_p thì nói rõ phần nào **chưa thấy trong học liệu**, không bịa định nghĩa.

### Q34 · Context — trộn tiếng Anh — chatlog T0990 `①`
- **Nguồn:** chatlog · `T0990` / `C0013`
- **Đưa vào:** `"Context" là gì`
- **Phải trả lời:** Giải thích **context / context window** — lượng thông tin mô hình tiêu thụ mỗi lần; trích dẫn `[T04-051]` hoặc `[T06-149]`; trả lời bằng tiếng Việt dù học viên dùng từ tiếng Anh.

### Q35 · Lab Day 2 ở đâu — lỗi chính tả — chatlog T0058 `①③`
- **Nguồn:** chatlog · `T0058` / `C0006` · *(tutor gốc cũng không trả lời được từ slide)*
- **Đưa vào:** `xem bài tập thực hành lab day 2 chiều nay ở đaau`
- **Phải trả lời:** **Không có** vị trí lab/LMS trong transcript → báo không tìm thấy / hướng dẫn hỏi LMS hoặc trợ giảng — **KHÔNG** bịa link hoặc thư mục; chấp nhận typo *đaau*.

### Q36 · Thuật ngữ vô nghĩa — chatlog T0115 `②`
- **Nguồn:** chatlog · `T0115` / `C0004` · *(tutor gốc: "không tìm thấy thuật ngữ điêu toa")*
- **Đưa vào:** `điêu toa`
- **Phải trả lời:** Không có thuật ngữ này trong học liệu → **không bịa định nghĩa**; hỏi lại học viên muốn hỏi khái niệm nào / có thể là lỗi gõ hoặc ASR.

---

## Ghi chú vận hành

| Hạng mục | Giá trị |
|---|---|
| Tổng câu | **36** |
| **Câu từ quan sát thực tế** | **10** (Q27–36 · chatlog tutor) |
| Câu tự nghĩ (synthetic) | 26 (Q01–26) |
| Kiểu tình huống (4 lớp chỗ khó) | **4** — mỗi lớp ≥ 2 câu |
| ① Nguồn sự thật | 7 synthetic + 7 real |
| ② Mơ hồ / thiếu thông tin | 2 synthetic + 1 real |
| ③ Ngoài phạm vi / thẩm quyền | 2 synthetic + 1 real |
| ④ Đặc thù domain | 4 synthetic + 1 real |
| Nguồn học liệu kiểm tra | `data/transcript/` + chatlog làm **input** |
| API kiểm thử | `POST /api/chat` → so `found`, `day_label`, `topic`, `sources[].segment_code`, `answer` |

**Trả lời mục spec §7:** Số câu bắt nguồn từ quan sát thực tế = **10** (≥ 5 tối thiểu, ≥ 10 khuyến nghị).

**Lượt chạy đầy đủ sau sửa guardrail:** **36/36 (100%)** — chi tiết `eval/run-1-results.md` + `eval/run-1-results.csv`

Khi chấm tự động, ít nhất kiểm: (1) `found` đúng kỳ vọng, (2) có/không có mã đoạn `[Txx-NNN]` bắt buộc, (3) câu trả lời không chứa thông tin bịa cho nhóm câu âm tính.
