# Kết quả chạy thử lần 1 — VLearn Tutor RAG

**Thời điểm:** 2026-07-30 08:57 UTC  
**Kết quả:** **27/36** câu đạt  
**Môi trường:** `dev_` branch · embed=`tfidf` · LLM=`extractive` (không API key)  
**Bộ câu:** `eval/golden-set.md` (36 câu)

## Tóm tắt

| Metric | Giá trị |
|---|---|
| Tổng câu | 36 |
| Pass | 27 |
| Fail | 9 |
| Tỷ lệ | 75.0% |

## Bảng chi tiết (cả câu fail)

| ID | Pass | Found | Day | Topic | Ghi chú |
|---|:---:|---|---|---|---|
| Q01 | ✅ | True | Day 2 | Soi bài toán các nhóm · tự động hoá & rà | answered with grounding |
| Q02 | ✅ | True | Day 1 | Foundation: cách LLM hoạt động (transfor | answered with grounding |
| Q03 | ✅ | True | Chưa gắn buổi | Buổi Foundation: transformer & attention | answered with grounding |
| Q04 | ✅ | True | Chưa gắn buổi | Buổi Foundation: transformer & attention | answered with grounding |
| Q05 | ✅ | True | Chưa gắn buổi | Buổi về bài toán · đánh giá · dữ liệu | answered with grounding |
| Q06 | ✅ | True | Chưa gắn buổi | Buổi Foundation: transformer & attention | answered with grounding |
| Q07 | ✅ | True | Chưa gắn buổi | Buổi Foundation: transformer & attention | answered with grounding |
| Q08 | ✅ | True | Day 2 | Xác định bài toán kinh doanh cho AI | answered with grounding |
| Q09 | ✅ | True | Day 2 | Xác định bài toán kinh doanh cho AI | answered with grounding |
| Q10 | ✅ | True | Day 2 | Xác định bài toán kinh doanh cho AI | answered with grounding |
| Q11 | ✅ | True | Day 2 | Chỉ số thành công & mức tự động hoá (phầ | answered with grounding |
| Q12 | ✅ | True | Day 2 | Chỉ số thành công & mức tự động hoá (phầ | answered with grounding |
| Q13 | ✅ | True | Day 2 | Chỉ số thành công & mức tự động hoá (phầ | answered with grounding |
| Q14 | ✅ | True | Day 2 | Soi bài toán các nhóm · tự động hoá & rà | answered with grounding |
| Q15 | ✅ | True | Chưa gắn buổi | Buổi về bài toán · đánh giá · dữ liệu | answered with grounding |
| Q16 | ✅ | True | Chưa gắn buổi | Buổi Foundation: transformer & attention | answered with grounding |
| Q17 | ❌ | True | Day 2 | Soi bài toán các nhóm · tự động hoá & rà | fabricated or over-answered |
| Q18 | ❌ | True | Day 2 | Xác định bài toán kinh doanh cho AI | fabricated or over-answered |
| Q19 | ❌ | True | Day 2 | Soi bài toán các nhóm · tự động hoá & rà | fabricated or over-answered |
| Q20 | ❌ | True | Chưa gắn buổi | Buổi Foundation: transformer & attention | fabricated or over-answered |
| Q21 | ❌ | True | Chưa gắn buổi | Buổi Foundation: transformer & attention | fabricated or over-answered |
| Q22 | ✅ | True | Day 2 | Xác định bài toán kinh doanh cho AI | located Day 2 — Xác định bài toán kinh doanh cho AI |
| Q23 | ✅ | True | Day 2 | Soi bài toán các nhóm · tự động hoá & rà | located Day 2 — Soi bài toán các nhóm · tự động hoá & ràng buộc |
| Q24 | ✅ | True | Chưa gắn buổi | Buổi về bài toán · đánh giá · dữ liệu | located Chưa gắn buổi — Buổi về bài toán · đánh giá · dữ liệu |
| Q25 | ❌ | True | Chưa gắn buổi | Buổi Foundation: transformer & attention | fabricated or over-answered |
| Q26 | ❌ | True | Chưa gắn buổi | Buổi về bài toán · đánh giá · dữ liệu | fabricated or over-answered |
| Q27 | ✅ | True | Chưa gắn buổi | Buổi Foundation: transformer & attention | answered with grounding |
| Q28 | ✅ | True | Chưa gắn buổi | Buổi Foundation: transformer & attention | answered with grounding |
| Q29 | ✅ | True | Chưa gắn buổi | Buổi Foundation: transformer & attention | answered with grounding |
| Q30 | ✅ | True | Day 2 | Chỉ số thành công & mức tự động hoá (phầ | answered with grounding |
| Q31 | ✅ | True | Day 2 | Soi bài toán các nhóm · tự động hoá & rà | answered with grounding |
| Q32 | ✅ | True | Chưa gắn buổi | Buổi Foundation: transformer & attention | answered with grounding |
| Q33 | ✅ | True | Day 1 | Foundation: cách LLM hoạt động (transfor | answered with grounding |
| Q34 | ✅ | True | Chưa gắn buổi | Buổi Foundation: transformer & attention | answered with grounding |
| Q35 | ❌ | True | Chưa gắn buổi | Buổi về bài toán · đánh giá · dữ liệu | fabricated or over-answered |
| Q36 | ❌ | True | Day 2 | Soi bài toán các nhóm · tự động hoá & rà | fabricated or over-answered |

## Chi tiết từng câu

### Q01 — PASS
- **Đưa vào:** Turing test là gì và cách kiểm tra thế nào?
- **Kỳ vọng:** answer
- **Found:** True · **Mode:** extractive
- **Locate:** Day 2 — Soi bài toán các nhóm · tự động hoá & ràng buộc
- **Sources:** T03-063(0.328); T03-142(0.298); T03-064(0.282)
- **Đánh giá:** answered with grounding
- **Trả lời (rút gọn):** Kiến thức này được giảng ở Day 2 — chủ đề "Soi bài toán các nhóm · tự động hoá & ràng buộc". Trên lớp, giảng viên trình bày như sau: • **Giảng viên:** Thế em ngồi em đọc, kiểm tra trước rồi em làm đúng không? Ok, cũng là một ý tưởng táo bạo đấy. Còn bạn nào?  [T03-063] • Nãy mình

### Q02 — PASS
- **Đưa vào:** AlphaGo nổi tiếng với nước đi nào và vì sao Lee Sedol bối rối?
- **Kỳ vọng:** answer
- **Found:** True · **Mode:** extractive
- **Locate:** Day 1 — Foundation: cách LLM hoạt động (transformer, attention, agent)
- **Sources:** T04-036(0.764); T04-035(0.234); T04-018(0.191)
- **Đánh giá:** answered with grounding
- **Trả lời (rút gọn):** Kiến thức này được giảng ở Day 1 — chủ đề "Foundation: cách LLM hoạt động (transformer, attention, agent)". Trên lớp, giảng viên trình bày như sau: • Vấn đề ở đây: cờ vây là một bộ môn có cực kỳ nhiều tổ hợp có thể xảy ra trên bàn cờ. Thực ra các chuyên gia chơi cờ vây phải qua r

### Q03 — PASS
- **Đưa vào:** Kiến trúc Transformer do ai tạo ra và năm nào?
- **Kỳ vọng:** answer
- **Found:** True · **Mode:** extractive
- **Locate:** Chưa gắn buổi — Buổi Foundation: transformer & attention
- **Sources:** T06-059(0.336); T06-075(0.319); T05-104(0.253)
- **Đánh giá:** answered with grounding
- **Trả lời (rút gọn):** Kiến thức này được giảng ở Chưa gắn buổi — chủ đề "Buổi Foundation: transformer & attention". Trên lớp, giảng viên trình bày như sau: • Thế thì ý mình nói rằng là cái lịch sử thì nó đi rất là dài, nhưng trong lịch sử này có mấy cái điểm nhấn. Khoảng năm 1970 cho đến năm 1990 được

### Q04 — PASS
- **Đưa vào:** Self-attention hoạt động thế nào? Q, K, V là gì?
- **Kỳ vọng:** answer
- **Found:** True · **Mode:** extractive
- **Locate:** Chưa gắn buổi — Buổi Foundation: transformer & attention
- **Sources:** T06-086(0.674); T06-161(0.432); T06-075(0.32)
- **Đánh giá:** answered with grounding
- **Trả lời (rút gọn):** Kiến thức này được giảng ở Chưa gắn buổi — chủ đề "Buổi Foundation: transformer & attention". Trên lớp, giảng viên trình bày như sau: • Cái self-attention bản chất là mỗi một token sẽ nhìn các token khác trong ngữ cảnh đang đặt ra. Thứ hai là multi-head attention: sẽ có nhiều góc

### Q05 — PASS
- **Đưa vào:** Vì sao LLM bị hallucination và RAG giúp gì?
- **Kỳ vọng:** answer
- **Found:** True · **Mode:** extractive
- **Locate:** Chưa gắn buổi — Buổi về bài toán · đánh giá · dữ liệu
- **Sources:** T06-025(0.576); T05-080(0.356); T05-056(0.335)
- **Đánh giá:** answered with grounding
- **Trả lời (rút gọn):** Kiến thức này được giảng ở Chưa gắn buổi — chủ đề "Buổi về bài toán · đánh giá · dữ liệu". Trên lớp, giảng viên trình bày như sau: • Có đúng không? Vì sao?  [T06-025] • Ví dụ nhá. Theo các bạn, cái việc công ty SpaceX — tất cả các bạn đều biết đúng không — quyết định đưa con ngườ

### Q06 — PASS
- **Đưa vào:** Temperature trong LLM dùng để làm gì?
- **Kỳ vọng:** answer
- **Found:** True · **Mode:** extractive
- **Locate:** Chưa gắn buổi — Buổi Foundation: transformer & attention
- **Sources:** T06-023(0.315); T06-049(0.235); T05-047(0.228)
- **Đánh giá:** answered with grounding
- **Trả lời (rút gọn):** Kiến thức này được giảng ở Chưa gắn buổi — chủ đề "Buổi Foundation: transformer & attention". Trên lớp, giảng viên trình bày như sau: • Đầu tiên, nếu các bạn được yêu cầu khoanh vùng AI là gì — bây giờ mình hỏi: giả sử cái máy tính Casio, cái máy tính học sinh hay dùng để làm toá

### Q07 — PASS
- **Đưa vào:** Context window là gì và giới hạn nó gây ra vấn đề gì?
- **Kỳ vọng:** answer
- **Found:** True · **Mode:** extractive
- **Locate:** Chưa gắn buổi — Buổi Foundation: transformer & attention
- **Sources:** T06-149(0.559); T06-150(0.489); T06-157(0.296)
- **Đánh giá:** answered with grounding
- **Trả lời (rút gọn):** Kiến thức này được giảng ở Chưa gắn buổi — chủ đề "Buổi Foundation: transformer & attention". Trên lớp, giảng viên trình bày như sau: • Giới hạn thứ hai là hallucination — nói rồi. Cái thứ ba là context window: mô hình chỉ nhìn được một lượng nhất định, và đây cũng là cái thách t

### Q08 — PASS
- **Đưa vào:** Mixture of Experts (MoE) giải quyết vấn đề gì?
- **Kỳ vọng:** answer
- **Found:** True · **Mode:** extractive
- **Locate:** Day 2 — Xác định bài toán kinh doanh cho AI
- **Sources:** T01-045(0.557); T01-058(0.503); T01-004(0.385)
- **Đánh giá:** answered with grounding
- **Trả lời (rút gọn):** Kiến thức này được giảng ở Day 2 — chủ đề "Xác định bài toán kinh doanh cho AI". Trên lớp, giảng viên trình bày như sau: • Rồi, ông Don Norman — tác giả cuốn The Design of Everyday Things — có một câu rất nổi tiếng: "Do not solve the problem I'm asked to solve." Tức là tôi sẽ khô

### Q09 — PASS
- **Đưa vào:** Theo bài giảng, đưa AI vào doanh nghiệp thì bao nhiêu phần trăm phụ thuộc con người và vận hành?
- **Kỳ vọng:** answer
- **Found:** True · **Mode:** extractive
- **Locate:** Day 2 — Xác định bài toán kinh doanh cho AI
- **Sources:** T01-003(0.601); T02-018(0.37); T01-001(0.334)
- **Đánh giá:** answered with grounding
- **Trả lời (rút gọn):** Kiến thức này được giảng ở Day 2 — chủ đề "Xác định bài toán kinh doanh cho AI". Trên lớp, giảng viên trình bày như sau: • Thực tế có những nghiên cứu, những thống kê trên thế giới nói rằng việc đưa AI vào ứng dụng, đặc biệt trong doanh nghiệp, thì 70% của nó đến từ con người và 

### Q10 — PASS
- **Đưa vào:** Product manager khác project manager thế nào?
- **Kỳ vọng:** answer
- **Found:** True · **Mode:** extractive
- **Locate:** Day 2 — Xác định bài toán kinh doanh cho AI
- **Sources:** T01-008(0.678); T01-011(0.587); T01-009(0.42)
- **Đánh giá:** answered with grounding
- **Trả lời (rút gọn):** Kiến thức này được giảng ở Day 2 — chủ đề "Xác định bài toán kinh doanh cho AI". Trên lớp, giảng viên trình bày như sau: • Bây giờ trong một team có bạn product owner, product manager. PM ở đây mình nói P là product nhá, không phải project — nó khác nhau. Có ai định nghĩa được nó

### Q11 — PASS
- **Đưa vào:** Quick win quan trọng thế nào khi chọn bài toán AI?
- **Kỳ vọng:** answer
- **Found:** True · **Mode:** extractive
- **Locate:** Day 2 — Chỉ số thành công & mức tự động hoá (phần sau buổi)
- **Sources:** T02-010(0.69); T03-068(0.242); T03-069(0.221)
- **Đánh giá:** answered with grounding
- **Trả lời (rút gọn):** Kiến thức này được giảng ở Day 2 — chủ đề "Chỉ số thành công & mức tự động hoá (phần sau buổi)". Trên lớp, giảng viên trình bày như sau: • Bài tập ngắn này để mọi người thử việc phân loại, tìm ra cái việc đáng để làm trước. Sau đấy thực ra mình sẽ còn rất nhiều vấn đề khác nữa, n

### Q12 — PASS
- **Đưa vào:** Automation và augmentation khác nhau thế nào?
- **Kỳ vọng:** answer
- **Found:** True · **Mode:** extractive
- **Locate:** Day 2 — Chỉ số thành công & mức tự động hoá (phần sau buổi)
- **Sources:** T02-032(0.771); T02-034(0.517); T02-033(0.36)
- **Đánh giá:** answered with grounding
- **Trả lời (rút gọn):** Kiến thức này được giảng ở Day 2 — chủ đề "Chỉ số thành công & mức tự động hoá (phần sau buổi)". Trên lớp, giảng viên trình bày như sau: • Bước thứ hai là chọn mức độ tự động hoá. Ở đây có hai thang: automation hay augmentation. Automation nghĩa là tự động, augmentation là tăng c

### Q13 — PASS
- **Đưa vào:** Ba cấp độ kỹ thuật khi đưa AI vào sản phẩm là gì?
- **Kỳ vọng:** answer
- **Found:** True · **Mode:** extractive
- **Locate:** Day 2 — Chỉ số thành công & mức tự động hoá (phần sau buổi)
- **Sources:** T02-035(0.642); T02-014(0.333); T02-036(0.326)
- **Đánh giá:** answered with grounding
- **Trả lời (rút gọn):** Kiến thức này được giảng ở Day 2 — chủ đề "Chỉ số thành công & mức tự động hoá (phần sau buổi)". Trên lớp, giảng viên trình bày như sau: • Còn một thang nữa: khi AI tham gia vào rồi, đánh giá mức độ của AI — của công nghệ nói chung — thì còn có các mức độ liên quan đến kỹ thuật. 

### Q14 — PASS
- **Đưa vào:** Khi nào nên chọn RAG thay vì fine-tuning?
- **Kỳ vọng:** answer
- **Found:** True · **Mode:** extractive
- **Locate:** Day 2 — Soi bài toán các nhóm · tự động hoá & ràng buộc
- **Sources:** T03-119(0.617); T03-036(0.27); T02-041(0.241)
- **Đánh giá:** answered with grounding
- **Trả lời (rút gọn):** Kiến thức này được giảng ở Day 2 — chủ đề "Soi bài toán các nhóm · tự động hoá & ràng buộc". Trên lớp, giảng viên trình bày như sau: • Cũng là kinh nghiệm cho các bạn: các bạn cũng đừng quá [không nghe rõ] cái kỹ thuật gọi là fine-tuning nhá. Tại vì để sử dụng được kỹ thuật fine-

### Q15 — PASS
- **Đưa vào:** Câu chuyện Cruise taxi tự lái dạy bài học gì về scope vận hành?
- **Kỳ vọng:** answer
- **Found:** True · **Mode:** extractive
- **Locate:** Chưa gắn buổi — Buổi về bài toán · đánh giá · dữ liệu
- **Sources:** T05-130(0.436); T05-133(0.306); T05-126(0.291)
- **Đánh giá:** answered with grounding
- **Trả lời (rút gọn):** Kiến thức này được giảng ở Chưa gắn buổi — chủ đề "Buổi về bài toán · đánh giá · dữ liệu". Trên lớp, giảng viên trình bày như sau: • [Khách mời]: Bây giờ nó đang hot, nhưng không chỉ hot kiểu ngày xưa — ngày xưa hot theo kiểu hype, nghĩa là có thể nó fail. Bây giờ nếu nhìn thấy c

### Q16 — PASS
- **Đưa vào:** LLM được huấn luyện qua mấy giai đoạn chính?
- **Kỳ vọng:** answer
- **Found:** True · **Mode:** extractive
- **Locate:** Chưa gắn buổi — Buổi Foundation: transformer & attention
- **Sources:** T06-141(0.468); T06-143(0.438); T06-043(0.261)
- **Đánh giá:** answered with grounding
- **Trả lời (rút gọn):** Kiến thức này được giảng ở Chưa gắn buổi — chủ đề "Buổi Foundation: transformer & attention". Trên lớp, giảng viên trình bày như sau: • Nói một chút nữa là cái LLM được tạo ra như thế nào. Đầu tiên là giai đoạn training: nó đọc hết tất cả các ngôn ngữ và kiến thức trên thế giới. 

### Q17 — FAIL
- **Đưa vào:** Công thức nấu phở bò Hà Nội chuẩn là gì?
- **Kỳ vọng:** decline
- **Found:** True · **Mode:** extractive
- **Locate:** Day 2 — Soi bài toán các nhóm · tự động hoá & ràng buộc
- **Sources:** T01-014(0.534); T03-071(0.297); T03-078(0.209)
- **Đánh giá:** fabricated or over-answered
- **Trả lời (rút gọn):** Kiến thức này được giảng ở Day 2 — chủ đề "Soi bài toán các nhóm · tự động hoá & ràng buộc". Trên lớp, giảng viên trình bày như sau: • Nếu ngay trong Việt Nam thôi thì văn hoá làm product mình thấy trong Sài Gòn tốt hơn ở Hà Nội. Mọi người để ý mà xem, các công ty công nghệ lớn đ

### Q18 — FAIL
- **Đưa vào:** Giá Bitcoin hôm nay bao nhiêu?
- **Kỳ vọng:** decline
- **Found:** True · **Mode:** extractive
- **Locate:** Day 2 — Xác định bài toán kinh doanh cho AI
- **Sources:** T02-018(0.443); T01-078(0.375); T01-022(0.37)
- **Đánh giá:** fabricated or over-answered
- **Trả lời (rút gọn):** Kiến thức này được giảng ở Day 2 — chủ đề "Xác định bài toán kinh doanh cho AI". Trên lớp, giảng viên trình bày như sau: • Và cái quan trọng nhất — việc này nãy các bạn cũng vừa làm thử — là chúng ta phải định lượng được bài toán đấy. Bởi vì cái này mới giúp chúng ta đánh giá đượ

### Q19 — FAIL
- **Đưa vào:** Trong khoá học, giảng viên dạy cách deploy Kubernetes cluster production thế nào?
- **Kỳ vọng:** decline
- **Found:** True · **Mode:** extractive
- **Locate:** Day 2 — Soi bài toán các nhóm · tự động hoá & ràng buộc
- **Sources:** T03-053(0.347); T03-039(0.262); T03-061(0.261)
- **Đánh giá:** fabricated or over-answered
- **Trả lời (rút gọn):** Kiến thức này được giảng ở Day 2 — chủ đề "Soi bài toán các nhóm · tự động hoá & ràng buộc". Trên lớp, giảng viên trình bày như sau: • **Giảng viên:** Thế nó có được quyền sáng tác thêm cách giải không?  [T03-053] • Tại vì trong khoá học này các bạn cũng sẽ được chia nhóm vào buổ

### Q20 — FAIL
- **Đưa vào:** nó là gì?
- **Kỳ vọng:** decline
- **Found:** True · **Mode:** extractive
- **Locate:** Chưa gắn buổi — Buổi Foundation: transformer & attention
- **Sources:** T05-144(0.387); T06-104(0.312); T05-010(0.287)
- **Đánh giá:** fabricated or over-answered
- **Trả lời (rút gọn):** Kiến thức này được giảng ở Chưa gắn buổi — chủ đề "Buổi Foundation: transformer & attention". Trên lớp, giảng viên trình bày như sau: • Mình nhấn mạnh lại, với trải nghiệm cá nhân của mình: bất kể công việc của bạn là gì, bất kể sau này bạn là gì, thì bạn bắt buộc phải rất tốt tr

### Q21 — FAIL
- **Đưa vào:** Viết giúp mình email xin nghỉ việc gửi sếp.
- **Kỳ vọng:** decline
- **Found:** True · **Mode:** extractive
- **Locate:** Chưa gắn buổi — Buổi Foundation: transformer & attention
- **Sources:** T06-009(0.304); T06-102(0.261); T06-010(0.241)
- **Đánh giá:** fabricated or over-answered
- **Trả lời (rút gọn):** Kiến thức này được giảng ở Chưa gắn buổi — chủ đề "Buổi Foundation: transformer & attention". Trên lớp, giảng viên trình bày như sau: • [học viên]: Vị trí gần nhất em làm là IT manager. Ở bên đấy thì hiện tại em đã nghỉ rồi, mới nghỉ để đi học khóa này.  [T06-009] • [Học viên]: E

### Q22 — PASS
- **Đưa vào:** Ma trận impact-effort dùng để làm gì?
- **Kỳ vọng:** locate
- **Found:** True · **Mode:** extractive
- **Locate:** Day 2 — Xác định bài toán kinh doanh cho AI
- **Sources:** T01-079(0.526); T01-088(0.463); T01-074(0.343)
- **Đánh giá:** located Day 2 — Xác định bài toán kinh doanh cho AI
- **Trả lời (rút gọn):** Kiến thức này được giảng ở Day 2 — chủ đề "Xác định bài toán kinh doanh cho AI". Trên lớp, giảng viên trình bày như sau: • Để các bạn có thể hình dung thêm nhá, nó sẽ kiểu như này: các bạn có thể vẽ một cái bảng — trục ngang, trục dọc — sau đấy để hết nó lên và sắp xếp vào các cu

### Q23 — PASS
- **Đưa vào:** Workflow pattern chaining và routing là gì?
- **Kỳ vọng:** locate
- **Found:** True · **Mode:** extractive
- **Locate:** Day 2 — Soi bài toán các nhóm · tự động hoá & ràng buộc
- **Sources:** T03-131(0.435); T03-132(0.325); T02-037(0.245)
- **Đánh giá:** located Day 2 — Soi bài toán các nhóm · tự động hoá & ràng buộc
- **Trả lời (rút gọn):** Kiến thức này được giảng ở Day 2 — chủ đề "Soi bài toán các nhóm · tự động hoá & ràng buộc". Trên lớp, giảng viên trình bày như sau: • Đây là vài cái workflow pattern — dĩ nhiên trên thế giới cũng có nhiều — nói chung là những cái basic, các bạn có thể xem như những khối Lego blo

### Q24 — PASS
- **Đưa vào:** Guardrail trong hệ thống AI dùng để kiểm soát hallucination thế nào?
- **Kỳ vọng:** locate
- **Found:** True · **Mode:** extractive
- **Locate:** Chưa gắn buổi — Buổi về bài toán · đánh giá · dữ liệu
- **Sources:** T05-113(0.449); T05-109(0.316); T05-074(0.297)
- **Đánh giá:** located Chưa gắn buổi — Buổi về bài toán · đánh giá · dữ liệu
- **Trả lời (rút gọn):** Kiến thức này được giảng ở Chưa gắn buổi — chủ đề "Buổi về bài toán · đánh giá · dữ liệu". Trên lớp, giảng viên trình bày như sau: • Hôm nay chúng ta nói đến planning phức tạp — lập kế hoạch để tạo ra personalize cho khách du lịch chẳng hạn — đấy là việc nhiều bước. Rồi chúng ta 

### Q25 — FAIL
- **Đưa vào:** Buổi trước thầy nói cái đó là gì?
- **Kỳ vọng:** decline
- **Found:** True · **Mode:** extractive
- **Locate:** Chưa gắn buổi — Buổi Foundation: transformer & attention
- **Sources:** T06-119(0.414); T06-104(0.32); T05-007(0.271)
- **Đánh giá:** fabricated or over-answered
- **Trả lời (rút gọn):** Kiến thức này được giảng ở Chưa gắn buổi — chủ đề "Buổi Foundation: transformer & attention". Trên lớp, giảng viên trình bày như sau: • Slide thì thầy dùng cái bản basic thôi. Sau đó thầy sẽ có một bản doc để cho các bạn tự đọc. Thế là giải quyết số một là slide nhá: thầy dùng bả

### Q26 — FAIL
- **Đưa vào:** Chấm và sửa giúp mình đoạn code Python này để nộp bài.
- **Kỳ vọng:** decline
- **Found:** True · **Mode:** extractive
- **Locate:** Chưa gắn buổi — Buổi về bài toán · đánh giá · dữ liệu
- **Sources:** T06-090(0.321); T05-009(0.317); T05-147(0.274)
- **Đánh giá:** fabricated or over-answered
- **Trả lời (rút gọn):** Kiến thức này được giảng ở Chưa gắn buổi — chủ đề "Buổi về bài toán · đánh giá · dữ liệu". Trên lớp, giảng viên trình bày như sau: • Code thì 4 năm rồi để AI code. Còn mình vẫn làm trong ngạch, vẫn xây dựng hệ thống, vẫn làm sản phẩm — tức là giờ không code, để cho AI code thôi, 

### Q27 — PASS
- **Đưa vào:** chào bạn, mình chưa hiểu về RAG
- **Kỳ vọng:** answer
- **Found:** True · **Mode:** extractive
- **Locate:** Chưa gắn buổi — Buổi Foundation: transformer & attention
- **Sources:** T06-005(0.289); T05-065(0.287); T06-077(0.245)
- **Đánh giá:** answered with grounding
- **Trả lời (rút gọn):** Kiến thức này được giảng ở Chưa gắn buổi — chủ đề "Buổi Foundation: transformer & attention". Trên lớp, giảng viên trình bày như sau: • [học viên]: Vâng, chào thầy. Em đi làm đến năm nay là 18 năm.  [T06-005] • Nhân chuyện này thì mình muốn nhắc các bạn một thói quen các bạn nên 

### Q28 — PASS
- **Đưa vào:** giải thích kỹ cơ chế transformer
- **Kỳ vọng:** answer
- **Found:** True · **Mode:** extractive
- **Locate:** Chưa gắn buổi — Buổi Foundation: transformer & attention
- **Sources:** T06-137(0.324); T06-075(0.322); T06-022(0.311)
- **Đánh giá:** answered with grounding
- **Trả lời (rút gọn):** Kiến thức này được giảng ở Chưa gắn buổi — chủ đề "Buổi Foundation: transformer & attention". Trên lớp, giảng viên trình bày như sau: • Một cái rất quan trọng nữa là cơ chế autoregressive: output token sẽ trở thành input token — cái feed forward mình vừa nói. Sau khi nó đoán ra t

### Q29 — PASS
- **Đưa vào:** giair thích cơ chế attention, mutilhead
- **Kỳ vọng:** answer
- **Found:** True · **Mode:** extractive
- **Locate:** Chưa gắn buổi — Buổi Foundation: transformer & attention
- **Sources:** T06-161(0.414); T06-137(0.398); T06-022(0.334)
- **Đánh giá:** answered with grounding
- **Trả lời (rút gọn):** Kiến thức này được giảng ở Chưa gắn buổi — chủ đề "Buổi Foundation: transformer & attention". Trên lớp, giảng viên trình bày như sau: • Để access vào bài lab này, mọi người vào cái slide mình đã gửi trong channel welcome-and-rules; ở slide thứ sáu mọi người sẽ thấy "live demo sel

### Q30 — PASS
- **Đưa vào:** agent la gi
- **Kỳ vọng:** answer
- **Found:** True · **Mode:** extractive
- **Locate:** Day 2 — Chỉ số thành công & mức tự động hoá (phần sau buổi)
- **Sources:** T02-038(0.628); T03-134(0.356); T03-034(0.294)
- **Đánh giá:** answered with grounding
- **Trả lời (rút gọn):** Kiến thức này được giảng ở Day 2 — chủ đề "Chỉ số thành công & mức tự động hoá (phần sau buổi)". Trên lớp, giảng viên trình bày như sau: • Phía dưới thì bạn sẽ cần những cái phức tạp hơn — ví dụ xây dựng hẳn một đội agent, sub-agent để làm việc với nhau: có một agent chia việc, s

### Q31 — PASS
- **Đưa vào:** augmentted chatbot khác gì agent ?
- **Kỳ vọng:** answer
- **Found:** True · **Mode:** extractive
- **Locate:** Day 2 — Soi bài toán các nhóm · tự động hoá & ràng buộc
- **Sources:** T03-134(0.483); T02-038(0.456); T01-030(0.236)
- **Đánh giá:** answered with grounding
- **Trả lời (rút gọn):** Kiến thức này được giảng ở Day 2 — chủ đề "Soi bài toán các nhóm · tự động hoá & ràng buộc". Trên lớp, giảng viên trình bày như sau: • Mấy cái này các bạn có thể về bảo con AI, hay tìm cái video giải thích thì nó cũng dễ hiểu hơn — nó cũng không có gì khác đâu. Loanh quanh vẫn ch

### Q32 — PASS
- **Đưa vào:** ai dùng từ vibe code đầu tiên
- **Kỳ vọng:** answer
- **Found:** True · **Mode:** extractive
- **Locate:** Chưa gắn buổi — Buổi Foundation: transformer & attention
- **Sources:** T06-015(0.565); T06-016(0.537); T06-011(0.407)
- **Đánh giá:** answered with grounding
- **Trả lời (rút gọn):** Kiến thức này được giảng ở Chưa gắn buổi — chủ đề "Buổi Foundation: transformer & attention". Trên lớp, giảng viên trình bày như sau: • [học viên]: Chào thầy và các bạn. Về việc vibe code thì nó có thể đúng với những sản phẩm dùng cho cá nhân. Còn về một sản phẩm dùng cho một lượ

### Q33 — PASS
- **Đưa vào:** hãy giải thích rõ temperature và top_p
- **Kỳ vọng:** answer
- **Found:** True · **Mode:** extractive
- **Locate:** Day 1 — Foundation: cách LLM hoạt động (transformer, attention, agent)
- **Sources:** T04-095(0.587); T04-072(0.375); T04-094(0.374)
- **Đánh giá:** answered with grounding
- **Trả lời (rút gọn):** Kiến thức này được giảng ở Day 1 — chủ đề "Foundation: cách LLM hoạt động (transformer, attention, agent)". Trên lớp, giảng viên trình bày như sau: • Các đáp án được giải thích trong quiz:  [T04-095] • Temperature hoạt động theo kiểu: nếu temperature bằng 0, mô hình sẽ luôn luôn 

### Q34 — PASS
- **Đưa vào:** "Context" là gì
- **Kỳ vọng:** answer
- **Found:** True · **Mode:** extractive
- **Locate:** Chưa gắn buổi — Buổi Foundation: transformer & attention
- **Sources:** T06-150(0.327); T05-144(0.326); T06-149(0.313)
- **Đánh giá:** answered with grounding
- **Trả lời (rút gọn):** Kiến thức này được giảng ở Chưa gắn buổi — chủ đề "Buổi Foundation: transformer & attention". Trên lớp, giảng viên trình bày như sau: • Các mô hình, ví dụ bên [không nghe rõ], người ta tiếp cận theo hướng context window của nó 512K thôi; còn bên Google thì lên 1 triệu, thậm chí b

### Q35 — FAIL
- **Đưa vào:** xem bài tập thực hành lab day 2 chiều nay ở đaau
- **Kỳ vọng:** decline
- **Found:** True · **Mode:** extractive
- **Locate:** Chưa gắn buổi — Buổi về bài toán · đánh giá · dữ liệu
- **Sources:** T05-009(0.439); T05-002(0.319); T05-140(0.307)
- **Đánh giá:** fabricated or over-answered
- **Trả lời (rút gọn):** Kiến thức này được giảng ở Chưa gắn buổi — chủ đề "Buổi về bài toán · đánh giá · dữ liệu". Trên lớp, giảng viên trình bày như sau: • Nội dung bài học chiều nay, nói lại, là chúng ta sẽ đi qua bảy phần như vậy. Khi nào các bạn thấy nó boring quá thì các bạn kêu nhé. Mình còn có cá

### Q36 — FAIL
- **Đưa vào:** điêu toa
- **Kỳ vọng:** decline
- **Found:** True · **Mode:** extractive
- **Locate:** Day 2 — Soi bài toán các nhóm · tự động hoá & ràng buộc
- **Sources:** T01-033(0.0); T01-036(0.0); T01-073(0.0)
- **Đánh giá:** fabricated or over-answered
- **Trả lời (rút gọn):** Kiến thức này được giảng ở Day 2 — chủ đề "Soi bài toán các nhóm · tự động hoá & ràng buộc". Trên lớp, giảng viên trình bày như sau: • Có những việc, ví dụ như có những bài toán mỗi tuần sẽ phải làm cái report một lần. Hỏi: làm một tuần một lần, mất bao lâu để làm việc đấy? Các b
