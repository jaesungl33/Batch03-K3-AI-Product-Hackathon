# Kết quả chạy thử lần 1 — VLearn Tutor RAG

**Thời điểm:** 2026-07-30 10:09 UTC
**Kết quả:** **36/36** câu đạt
**Môi trường:** `dev_` branch · embed=`tfidf` · LLM=`extractive` (không API key)
**Bộ câu:** `eval/golden-set.md` (36 câu)

## Tóm tắt

| Metric | Giá trị |
|---|---|
| Tổng câu | 36 |
| Pass | 36 |
| Fail | 0 |
| Tỷ lệ | 100.0% |

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
| Q17 | ✅ | False | - | - | declined/not found |
| Q18 | ✅ | False | - | - | declined/not found |
| Q19 | ✅ | False | - | - | declined/not found |
| Q20 | ✅ | False | - | - | declined/not found |
| Q21 | ✅ | False | - | - | declined/not found |
| Q22 | ✅ | True | Day 2 | Xác định bài toán kinh doanh cho AI | located Day 2 — Xác định bài toán kinh doanh cho AI |
| Q23 | ✅ | True | Day 2 | Soi bài toán các nhóm · tự động hoá & rà | located Day 2 — Soi bài toán các nhóm · tự động hoá & ràng buộc |
| Q24 | ✅ | True | Chưa gắn buổi | Buổi về bài toán · đánh giá · dữ liệu | located Chưa gắn buổi — Buổi về bài toán · đánh giá · dữ liệu |
| Q25 | ✅ | False | - | - | declined/not found |
| Q26 | ✅ | False | - | - | declined/not found |
| Q27 | ✅ | True | Chưa gắn buổi | Buổi Foundation: transformer & attention | answered with grounding |
| Q28 | ✅ | True | Chưa gắn buổi | Buổi Foundation: transformer & attention | answered with grounding |
| Q29 | ✅ | True | Chưa gắn buổi | Buổi Foundation: transformer & attention | answered with grounding |
| Q30 | ✅ | True | Day 2 | Chỉ số thành công & mức tự động hoá (phầ | answered with grounding |
| Q31 | ✅ | True | Day 2 | Soi bài toán các nhóm · tự động hoá & rà | answered with grounding |
| Q32 | ✅ | True | Chưa gắn buổi | Buổi Foundation: transformer & attention | answered with grounding |
| Q33 | ✅ | True | Day 1 | Foundation: cách LLM hoạt động (transfor | answered with grounding |
| Q34 | ✅ | True | Chưa gắn buổi | Buổi Foundation: transformer & attention | answered with grounding |
| Q35 | ✅ | False | - | - | declined/not found |
| Q36 | ✅ | False | - | - | declined/not found |

## Chi tiết từng câu

### Q01 — PASS
- **Đưa vào:** Turing test là gì và cách kiểm tra thế nào?
- **Kỳ vọng:** answer
- **Found:** True · **Mode:** extractive
- **Locate:** Day 2 — Soi bài toán các nhóm · tự động hoá & ràng buộc
- **Sources:** T03-063(0.334); T03-142(0.295); T03-064(0.279)
- **Đánh giá:** answered with grounding
- **Trả lời (rút gọn):** Kiến thức này được giảng ở Day 2 — chủ đề "Soi bài toán các nhóm · tự động hoá & ràng buộc". Trên lớp, giảng viên trình bày như sau: • **Giảng viên:** Thế em ngồi em đọc, kiểm tra trước rồi em làm đúng không? Ok, cũng là một ý tưởng táo bạo đấy. Còn bạn nào?  [T03-063] • Nãy mình

### Q02 — PASS
- **Đưa vào:** AlphaGo nổi tiếng với nước đi nào và vì sao Lee Sedol bối rối?
- **Kỳ vọng:** answer
- **Found:** True · **Mode:** extractive
- **Locate:** Day 1 — Foundation: cách LLM hoạt động (transformer, attention, agent)
- **Sources:** T04-036(0.777); T04-035(0.239); T04-018(0.181)
- **Đánh giá:** answered with grounding
- **Trả lời (rút gọn):** Kiến thức này được giảng ở Day 1 — chủ đề "Foundation: cách LLM hoạt động (transformer, attention, agent)". Trên lớp, giảng viên trình bày như sau: • Vấn đề ở đây: cờ vây là một bộ môn có cực kỳ nhiều tổ hợp có thể xảy ra trên bàn cờ. Thực ra các chuyên gia chơi cờ vây phải qua r

### Q03 — PASS
- **Đưa vào:** Kiến trúc Transformer do ai tạo ra và năm nào?
- **Kỳ vọng:** answer
- **Found:** True · **Mode:** extractive
- **Locate:** Chưa gắn buổi — Buổi Foundation: transformer & attention
- **Sources:** T06-059(0.337); T06-075(0.315); T06-083(0.26)
- **Đánh giá:** answered with grounding
- **Trả lời (rút gọn):** Kiến thức này được giảng ở Chưa gắn buổi — chủ đề "Buổi Foundation: transformer & attention". Trên lớp, giảng viên trình bày như sau: • Thế thì ý mình nói rằng là cái lịch sử thì nó đi rất là dài, nhưng trong lịch sử này có mấy cái điểm nhấn. Khoảng năm 1970 cho đến năm 1990 được

### Q04 — PASS
- **Đưa vào:** Self-attention hoạt động thế nào? Q, K, V là gì?
- **Kỳ vọng:** answer
- **Found:** True · **Mode:** extractive
- **Locate:** Chưa gắn buổi — Buổi Foundation: transformer & attention
- **Sources:** T06-086(0.628); T06-161(0.458); T06-075(0.328)
- **Đánh giá:** answered with grounding
- **Trả lời (rút gọn):** Kiến thức này được giảng ở Chưa gắn buổi — chủ đề "Buổi Foundation: transformer & attention". Trên lớp, giảng viên trình bày như sau: • Cái self-attention bản chất là mỗi một token sẽ nhìn các token khác trong ngữ cảnh đang đặt ra. Thứ hai là multi-head attention: sẽ có nhiều góc

### Q05 — PASS
- **Đưa vào:** Vì sao LLM bị hallucination và RAG giúp gì?
- **Kỳ vọng:** answer
- **Found:** True · **Mode:** extractive
- **Locate:** Chưa gắn buổi — Buổi về bài toán · đánh giá · dữ liệu
- **Sources:** T06-025(0.584); T05-080(0.344); T05-056(0.332)
- **Đánh giá:** answered with grounding
- **Trả lời (rút gọn):** Kiến thức này được giảng ở Chưa gắn buổi — chủ đề "Buổi về bài toán · đánh giá · dữ liệu". Trên lớp, giảng viên trình bày như sau: • Có đúng không? Vì sao?  [T06-025] • Ví dụ nhá. Theo các bạn, cái việc công ty SpaceX — tất cả các bạn đều biết đúng không — quyết định đưa con ngườ

### Q06 — PASS
- **Đưa vào:** Temperature trong LLM dùng để làm gì?
- **Kỳ vọng:** answer
- **Found:** True · **Mode:** extractive
- **Locate:** Chưa gắn buổi — Buổi Foundation: transformer & attention
- **Sources:** T06-023(0.323); T05-047(0.237); T06-049(0.212)
- **Đánh giá:** answered with grounding
- **Trả lời (rút gọn):** Kiến thức này được giảng ở Chưa gắn buổi — chủ đề "Buổi Foundation: transformer & attention". Trên lớp, giảng viên trình bày như sau: • Đầu tiên, nếu các bạn được yêu cầu khoanh vùng AI là gì — bây giờ mình hỏi: giả sử cái máy tính Casio, cái máy tính học sinh hay dùng để làm toá

### Q07 — PASS
- **Đưa vào:** Context window là gì và giới hạn nó gây ra vấn đề gì?
- **Kỳ vọng:** answer
- **Found:** True · **Mode:** extractive
- **Locate:** Chưa gắn buổi — Buổi Foundation: transformer & attention
- **Sources:** T06-149(0.558); T06-150(0.501); T06-157(0.305)
- **Đánh giá:** answered with grounding
- **Trả lời (rút gọn):** Kiến thức này được giảng ở Chưa gắn buổi — chủ đề "Buổi Foundation: transformer & attention". Trên lớp, giảng viên trình bày như sau: • Giới hạn thứ hai là hallucination — nói rồi. Cái thứ ba là context window: mô hình chỉ nhìn được một lượng nhất định, và đây cũng là cái thách t

### Q08 — PASS
- **Đưa vào:** Mixture of Experts (MoE) giải quyết vấn đề gì?
- **Kỳ vọng:** answer
- **Found:** True · **Mode:** extractive
- **Locate:** Day 2 — Xác định bài toán kinh doanh cho AI
- **Sources:** T01-045(0.576); T01-058(0.509); T01-004(0.375)
- **Đánh giá:** answered with grounding
- **Trả lời (rút gọn):** Kiến thức này được giảng ở Day 2 — chủ đề "Xác định bài toán kinh doanh cho AI". Trên lớp, giảng viên trình bày như sau: • Rồi, ông Don Norman — tác giả cuốn The Design of Everyday Things — có một câu rất nổi tiếng: "Do not solve the problem I'm asked to solve." Tức là tôi sẽ khô

### Q09 — PASS
- **Đưa vào:** Theo bài giảng, đưa AI vào doanh nghiệp thì bao nhiêu phần trăm phụ thuộc con người và vận hành?
- **Kỳ vọng:** answer
- **Found:** True · **Mode:** extractive
- **Locate:** Day 2 — Xác định bài toán kinh doanh cho AI
- **Sources:** T01-003(0.549); T02-018(0.382); T01-001(0.35)
- **Đánh giá:** answered with grounding
- **Trả lời (rút gọn):** Kiến thức này được giảng ở Day 2 — chủ đề "Xác định bài toán kinh doanh cho AI". Trên lớp, giảng viên trình bày như sau: • Thực tế có những nghiên cứu, những thống kê trên thế giới nói rằng việc đưa AI vào ứng dụng, đặc biệt trong doanh nghiệp, thì 70% của nó đến từ con người và

### Q10 — PASS
- **Đưa vào:** Product manager khác project manager thế nào?
- **Kỳ vọng:** answer
- **Found:** True · **Mode:** extractive
- **Locate:** Day 2 — Xác định bài toán kinh doanh cho AI
- **Sources:** T01-008(0.668); T01-011(0.586); T01-009(0.427)
- **Đánh giá:** answered with grounding
- **Trả lời (rút gọn):** Kiến thức này được giảng ở Day 2 — chủ đề "Xác định bài toán kinh doanh cho AI". Trên lớp, giảng viên trình bày như sau: • Bây giờ trong một team có bạn product owner, product manager. PM ở đây mình nói P là product nhá, không phải project — nó khác nhau. Có ai định nghĩa được nó

### Q11 — PASS
- **Đưa vào:** Quick win quan trọng thế nào khi chọn bài toán AI?
- **Kỳ vọng:** answer
- **Found:** True · **Mode:** extractive
- **Locate:** Day 2 — Chỉ số thành công & mức tự động hoá (phần sau buổi)
- **Sources:** T02-010(0.684); T03-068(0.243); T01-079(0.226)
- **Đánh giá:** answered with grounding
- **Trả lời (rút gọn):** Kiến thức này được giảng ở Day 2 — chủ đề "Chỉ số thành công & mức tự động hoá (phần sau buổi)". Trên lớp, giảng viên trình bày như sau: • Bài tập ngắn này để mọi người thử việc phân loại, tìm ra cái việc đáng để làm trước. Sau đấy thực ra mình sẽ còn rất nhiều vấn đề khác nữa, n

### Q12 — PASS
- **Đưa vào:** Automation và augmentation khác nhau thế nào?
- **Kỳ vọng:** answer
- **Found:** True · **Mode:** extractive
- **Locate:** Day 2 — Chỉ số thành công & mức tự động hoá (phần sau buổi)
- **Sources:** T02-032(0.771); T02-034(0.505); T02-033(0.37)
- **Đánh giá:** answered with grounding
- **Trả lời (rút gọn):** Kiến thức này được giảng ở Day 2 — chủ đề "Chỉ số thành công & mức tự động hoá (phần sau buổi)". Trên lớp, giảng viên trình bày như sau: • Bước thứ hai là chọn mức độ tự động hoá. Ở đây có hai thang: automation hay augmentation. Automation nghĩa là tự động, augmentation là tăng c

### Q13 — PASS
- **Đưa vào:** Ba cấp độ kỹ thuật khi đưa AI vào sản phẩm là gì?
- **Kỳ vọng:** answer
- **Found:** True · **Mode:** extractive
- **Locate:** Day 2 — Chỉ số thành công & mức tự động hoá (phần sau buổi)
- **Sources:** T02-035(0.658); T02-014(0.332); T02-036(0.324)
- **Đánh giá:** answered with grounding
- **Trả lời (rút gọn):** Kiến thức này được giảng ở Day 2 — chủ đề "Chỉ số thành công & mức tự động hoá (phần sau buổi)". Trên lớp, giảng viên trình bày như sau: • Còn một thang nữa: khi AI tham gia vào rồi, đánh giá mức độ của AI — của công nghệ nói chung — thì còn có các mức độ liên quan đến kỹ thuật.

### Q14 — PASS
- **Đưa vào:** Khi nào nên chọn RAG thay vì fine-tuning?
- **Kỳ vọng:** answer
- **Found:** True · **Mode:** extractive
- **Locate:** Day 2 — Soi bài toán các nhóm · tự động hoá & ràng buộc
- **Sources:** T03-119(0.616); T03-036(0.263); T02-041(0.249)
- **Đánh giá:** answered with grounding
- **Trả lời (rút gọn):** Kiến thức này được giảng ở Day 2 — chủ đề "Soi bài toán các nhóm · tự động hoá & ràng buộc". Trên lớp, giảng viên trình bày như sau: • Cũng là kinh nghiệm cho các bạn: các bạn cũng đừng quá [không nghe rõ] cái kỹ thuật gọi là fine-tuning nhá. Tại vì để sử dụng được kỹ thuật fine-

### Q15 — PASS
- **Đưa vào:** Câu chuyện Cruise taxi tự lái dạy bài học gì về scope vận hành?
- **Kỳ vọng:** answer
- **Found:** True · **Mode:** extractive
- **Locate:** Chưa gắn buổi — Buổi về bài toán · đánh giá · dữ liệu
- **Sources:** T05-130(0.422); T05-124(0.306); T05-126(0.306)
- **Đánh giá:** answered with grounding
- **Trả lời (rút gọn):** Kiến thức này được giảng ở Chưa gắn buổi — chủ đề "Buổi về bài toán · đánh giá · dữ liệu". Trên lớp, giảng viên trình bày như sau: • [Khách mời]: Bây giờ nó đang hot, nhưng không chỉ hot kiểu ngày xưa — ngày xưa hot theo kiểu hype, nghĩa là có thể nó fail. Bây giờ nếu nhìn thấy c

### Q16 — PASS
- **Đưa vào:** LLM được huấn luyện qua mấy giai đoạn chính?
- **Kỳ vọng:** answer
- **Found:** True · **Mode:** extractive
- **Locate:** Chưa gắn buổi — Buổi Foundation: transformer & attention
- **Sources:** T06-141(0.535); T06-143(0.438); T06-139(0.256)
- **Đánh giá:** answered with grounding
- **Trả lời (rút gọn):** Kiến thức này được giảng ở Chưa gắn buổi — chủ đề "Buổi Foundation: transformer & attention". Trên lớp, giảng viên trình bày như sau: • Nói một chút nữa là cái LLM được tạo ra như thế nào. Đầu tiên là giai đoạn training: nó đọc hết tất cả các ngôn ngữ và kiến thức trên thế giới.

### Q17 — PASS
- **Đưa vào:** Công thức nấu phở bò Hà Nội chuẩn là gì?
- **Kỳ vọng:** decline
- **Found:** False · **Mode:** none
- **Locate:** None — None
- **Sources:** (none)
- **Đánh giá:** declined/not found
- **Trả lời (rút gọn):** Mình chưa tìm thấy kiến thức này trong học liệu đã nạp.

### Q18 — PASS
- **Đưa vào:** Giá Bitcoin hôm nay bao nhiêu?
- **Kỳ vọng:** decline
- **Found:** False · **Mode:** none
- **Locate:** None — None
- **Sources:** (none)
- **Đánh giá:** declined/not found
- **Trả lời (rút gọn):** Mình chưa tìm thấy kiến thức này trong học liệu đã nạp.

### Q19 — PASS
- **Đưa vào:** Trong khoá học, giảng viên dạy cách deploy Kubernetes cluster production thế nào?
- **Kỳ vọng:** decline
- **Found:** False · **Mode:** none
- **Locate:** None — None
- **Sources:** (none)
- **Đánh giá:** declined/not found
- **Trả lời (rút gọn):** Mình chưa tìm thấy kiến thức này trong học liệu đã nạp.

### Q20 — PASS
- **Đưa vào:** nó là gì?
- **Kỳ vọng:** decline
- **Found:** False · **Mode:** none
- **Locate:** None — None
- **Sources:** (none)
- **Đánh giá:** declined/not found
- **Trả lời (rút gọn):** Mình chưa tìm thấy kiến thức này trong học liệu đã nạp.

### Q21 — PASS
- **Đưa vào:** Viết giúp mình email xin nghỉ việc gửi sếp.
- **Kỳ vọng:** decline
- **Found:** False · **Mode:** none
- **Locate:** None — None
- **Sources:** (none)
- **Đánh giá:** declined/not found
- **Trả lời (rút gọn):** Mình chưa tìm thấy kiến thức này trong học liệu đã nạp.

### Q22 — PASS
- **Đưa vào:** Ma trận impact-effort dùng để làm gì?
- **Kỳ vọng:** locate
- **Found:** True · **Mode:** extractive
- **Locate:** Day 2 — Xác định bài toán kinh doanh cho AI
- **Sources:** T01-079(0.539); T01-088(0.465); T01-074(0.34)
- **Đánh giá:** located Day 2 — Xác định bài toán kinh doanh cho AI
- **Trả lời (rút gọn):** Kiến thức này được giảng ở Day 2 — chủ đề "Xác định bài toán kinh doanh cho AI". Trên lớp, giảng viên trình bày như sau: • Để các bạn có thể hình dung thêm nhá, nó sẽ kiểu như này: các bạn có thể vẽ một cái bảng — trục ngang, trục dọc — sau đấy để hết nó lên và sắp xếp vào các cu

### Q23 — PASS
- **Đưa vào:** Workflow pattern chaining và routing là gì?
- **Kỳ vọng:** locate
- **Found:** True · **Mode:** extractive
- **Locate:** Day 2 — Soi bài toán các nhóm · tự động hoá & ràng buộc
- **Sources:** T03-131(0.434); T03-132(0.326); T02-037(0.25)
- **Đánh giá:** located Day 2 — Soi bài toán các nhóm · tự động hoá & ràng buộc
- **Trả lời (rút gọn):** Kiến thức này được giảng ở Day 2 — chủ đề "Soi bài toán các nhóm · tự động hoá & ràng buộc". Trên lớp, giảng viên trình bày như sau: • Đây là vài cái workflow pattern — dĩ nhiên trên thế giới cũng có nhiều — nói chung là những cái basic, các bạn có thể xem như những khối Lego blo

### Q24 — PASS
- **Đưa vào:** Guardrail trong hệ thống AI dùng để kiểm soát hallucination thế nào?
- **Kỳ vọng:** locate
- **Found:** True · **Mode:** extractive
- **Locate:** Chưa gắn buổi — Buổi về bài toán · đánh giá · dữ liệu
- **Sources:** T05-113(0.451); T05-109(0.313); T05-149(0.293)
- **Đánh giá:** located Chưa gắn buổi — Buổi về bài toán · đánh giá · dữ liệu
- **Trả lời (rút gọn):** Kiến thức này được giảng ở Chưa gắn buổi — chủ đề "Buổi về bài toán · đánh giá · dữ liệu". Trên lớp, giảng viên trình bày như sau: • Hôm nay chúng ta nói đến planning phức tạp — lập kế hoạch để tạo ra personalize cho khách du lịch chẳng hạn — đấy là việc nhiều bước. Rồi chúng ta

### Q25 — PASS
- **Đưa vào:** Buổi trước thầy nói cái đó là gì?
- **Kỳ vọng:** decline
- **Found:** False · **Mode:** none
- **Locate:** None — None
- **Sources:** (none)
- **Đánh giá:** declined/not found
- **Trả lời (rút gọn):** Mình chưa tìm thấy kiến thức này trong học liệu đã nạp.

### Q26 — PASS
- **Đưa vào:** Chấm và sửa giúp mình đoạn code Python này để nộp bài.
- **Kỳ vọng:** decline
- **Found:** False · **Mode:** none
- **Locate:** None — None
- **Sources:** (none)
- **Đánh giá:** declined/not found
- **Trả lời (rút gọn):** Mình chưa tìm thấy kiến thức này trong học liệu đã nạp.

### Q27 — PASS
- **Đưa vào:** chào bạn, mình chưa hiểu về RAG
- **Kỳ vọng:** answer
- **Found:** True · **Mode:** extractive
- **Locate:** Chưa gắn buổi — Buổi Foundation: transformer & attention
- **Sources:** T06-005(0.289); T05-065(0.28); T06-077(0.249)
- **Đánh giá:** answered with grounding
- **Trả lời (rút gọn):** Kiến thức này được giảng ở Chưa gắn buổi — chủ đề "Buổi Foundation: transformer & attention". Trên lớp, giảng viên trình bày như sau: • [học viên]: Vâng, chào thầy. Em đi làm đến năm nay là 18 năm.  [T06-005] • Nhân chuyện này thì mình muốn nhắc các bạn một thói quen các bạn nên

### Q28 — PASS
- **Đưa vào:** giải thích kỹ cơ chế transformer
- **Kỳ vọng:** answer
- **Found:** True · **Mode:** extractive
- **Locate:** Chưa gắn buổi — Buổi Foundation: transformer & attention
- **Sources:** T06-137(0.32); T06-075(0.317); T06-022(0.304)
- **Đánh giá:** answered with grounding
- **Trả lời (rút gọn):** Kiến thức này được giảng ở Chưa gắn buổi — chủ đề "Buổi Foundation: transformer & attention". Trên lớp, giảng viên trình bày như sau: • Một cái rất quan trọng nữa là cơ chế autoregressive: output token sẽ trở thành input token — cái feed forward mình vừa nói. Sau khi nó đoán ra t

### Q29 — PASS
- **Đưa vào:** giair thích cơ chế attention, mutilhead
- **Kỳ vọng:** answer
- **Found:** True · **Mode:** extractive
- **Locate:** Chưa gắn buổi — Buổi Foundation: transformer & attention
- **Sources:** T06-161(0.418); T06-137(0.401); T06-022(0.329)
- **Đánh giá:** answered with grounding
- **Trả lời (rút gọn):** Kiến thức này được giảng ở Chưa gắn buổi — chủ đề "Buổi Foundation: transformer & attention". Trên lớp, giảng viên trình bày như sau: • Để access vào bài lab này, mọi người vào cái slide mình đã gửi trong channel welcome-and-rules; ở slide thứ sáu mọi người sẽ thấy "live demo sel

### Q30 — PASS
- **Đưa vào:** agent la gi
- **Kỳ vọng:** answer
- **Found:** True · **Mode:** extractive
- **Locate:** Day 2 — Chỉ số thành công & mức tự động hoá (phần sau buổi)
- **Sources:** T02-038(0.636); T03-134(0.363); T03-034(0.288)
- **Đánh giá:** answered with grounding
- **Trả lời (rút gọn):** Kiến thức này được giảng ở Day 2 — chủ đề "Chỉ số thành công & mức tự động hoá (phần sau buổi)". Trên lớp, giảng viên trình bày như sau: • Phía dưới thì bạn sẽ cần những cái phức tạp hơn — ví dụ xây dựng hẳn một đội agent, sub-agent để làm việc với nhau: có một agent chia việc, s

### Q31 — PASS
- **Đưa vào:** augmentted chatbot khác gì agent ?
- **Kỳ vọng:** answer
- **Found:** True · **Mode:** extractive
- **Locate:** Day 2 — Soi bài toán các nhóm · tự động hoá & ràng buộc
- **Sources:** T03-134(0.49); T02-038(0.473); T01-030(0.234)
- **Đánh giá:** answered with grounding
- **Trả lời (rút gọn):** Kiến thức này được giảng ở Day 2 — chủ đề "Soi bài toán các nhóm · tự động hoá & ràng buộc". Trên lớp, giảng viên trình bày như sau: • Mấy cái này các bạn có thể về bảo con AI, hay tìm cái video giải thích thì nó cũng dễ hiểu hơn — nó cũng không có gì khác đâu. Loanh quanh vẫn ch

### Q32 — PASS
- **Đưa vào:** ai dùng từ vibe code đầu tiên
- **Kỳ vọng:** answer
- **Found:** True · **Mode:** extractive
- **Locate:** Chưa gắn buổi — Buổi Foundation: transformer & attention
- **Sources:** T06-015(0.563); T06-016(0.541); T06-011(0.419)
- **Đánh giá:** answered with grounding
- **Trả lời (rút gọn):** Kiến thức này được giảng ở Chưa gắn buổi — chủ đề "Buổi Foundation: transformer & attention". Trên lớp, giảng viên trình bày như sau: • [học viên]: Chào thầy và các bạn. Về việc vibe code thì nó có thể đúng với những sản phẩm dùng cho cá nhân. Còn về một sản phẩm dùng cho một lượ

### Q33 — PASS
- **Đưa vào:** hãy giải thích rõ temperature và top_p
- **Kỳ vọng:** answer
- **Found:** True · **Mode:** extractive
- **Locate:** Day 1 — Foundation: cách LLM hoạt động (transformer, attention, agent)
- **Sources:** T04-095(0.615); T04-094(0.383); T04-072(0.37)
- **Đánh giá:** answered with grounding
- **Trả lời (rút gọn):** Kiến thức này được giảng ở Day 1 — chủ đề "Foundation: cách LLM hoạt động (transformer, attention, agent)". Trên lớp, giảng viên trình bày như sau: • Các đáp án được giải thích trong quiz:  [T04-095] • Trong phần quiz, một [học viên] đang top 1 được mời giới thiệu và giải thích v

### Q34 — PASS
- **Đưa vào:** "Context" là gì
- **Kỳ vọng:** answer
- **Found:** True · **Mode:** extractive
- **Locate:** Chưa gắn buổi — Buổi Foundation: transformer & attention
- **Sources:** T06-150(0.338); T05-144(0.316); T06-149(0.313)
- **Đánh giá:** answered with grounding
- **Trả lời (rút gọn):** Kiến thức này được giảng ở Chưa gắn buổi — chủ đề "Buổi Foundation: transformer & attention". Trên lớp, giảng viên trình bày như sau: • Các mô hình, ví dụ bên [không nghe rõ], người ta tiếp cận theo hướng context window của nó 512K thôi; còn bên Google thì lên 1 triệu, thậm chí b

### Q35 — PASS
- **Đưa vào:** xem bài tập thực hành lab day 2 chiều nay ở đaau
- **Kỳ vọng:** decline
- **Found:** False · **Mode:** none
- **Locate:** None — None
- **Sources:** (none)
- **Đánh giá:** declined/not found
- **Trả lời (rút gọn):** Mình chưa tìm thấy kiến thức này trong học liệu đã nạp.

### Q36 — PASS
- **Đưa vào:** điêu toa
- **Kỳ vọng:** decline
- **Found:** False · **Mode:** none
- **Locate:** None — None
- **Sources:** (none)
- **Đánh giá:** declined/not found
- **Trả lời (rút gọn):** Mình chưa tìm thấy kiến thức này trong học liệu đã nạp.
