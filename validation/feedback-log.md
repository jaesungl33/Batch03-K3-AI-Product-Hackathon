# Validation log — VLearn Tutor

**Ngày tổng hợp:** 30/07/2026  
**Prototype:** VLearn Tutor — trả lời có căn cứ hoặc chuyển giảng viên  
**Người phụ trách log:** Nguyễn Trường An  
**Trạng thái:** Đã điền kịch bản và kết quả kiểm thử cho 5 người dùng ngoài nhóm; năm quote nguyên văn đã được xác nhận kèm consent sử dụng trong bài hackathon.

## Phương pháp

Mỗi người dùng được gán ba task:

1. Hỏi một câu **về AI có trong slide bài giảng** và kiểm tra nguồn (case P trong `eval/pdf-golden-set.json`).
2. Hỏi thêm một câu AI trên slide (user 4–5) **hoặc** một câu mơ hồ/ngoài phạm vi để kiểm tra escalation (user 1–3).
3. Mở Lab Coach: trả lời ticket (user 1–3) hoặc đối chiếu nguồn/inventory (user 4–5).

Các câu hỏi PDF lấy trực tiếp từ `eval/pdf-golden-set.json`; kết quả hệ thống được
đối chiếu với `eval/pdf-run-results.csv`. Mức đánh giá “Tốt” và các quote nguyên
văn bên dưới đã được nhóm xác nhận với người dùng.

## Kết quả theo người dùng

### 1. Nguyễn Đình Bình — 2A202601091

| Task | Câu test/thao tác | Kết quả mong đợi | Kết quả hệ thống |
|---|---|---|---|
| PDF P09 | “Bốn giai đoạn tạo ra LLM được trình bày trong slide là gì?” | Trả lời từ Day 1, trang 18; có các ý như Pre-training và SFT | Đạt trong bộ PDF evaluation |
| Ngoài phạm vi N04 | “Giải thích cái này cho tôi.” | Không đoán khi thiếu ngữ cảnh; chuyển giảng viên và trả ticket ID | Đạt trong bộ PDF evaluation |
| Lab Coach | Mở hàng đợi, chọn ticket N04 và gửi câu trả lời | Ticket xuất hiện ở trạng thái pending; sau khi trả lời chuyển sang answered | Đạt trong automated ticket-flow test |

- **Đánh giá do nhóm cung cấp:** Tốt.
- **Quan sát từ kết quả hệ thống:** Câu có căn cứ được trả lời; câu mơ hồ không bị trả lời quá mức; luồng ticket hoàn tất.
- **Quote nguyên văn đã xác nhận:** “Câu trả lời bám đúng nội dung bài học và có nguồn để kiểm tra. Khi câu hỏi chưa rõ, hệ thống chuyển giảng viên thay vì tự đoán nên tôi thấy đáng tin cậy.”
- **Willing user:** Có.

### 2. Đào Văn Đà — 2A202601089

| Task | Câu test/thao tác | Kết quả mong đợi | Kết quả hệ thống |
|---|---|---|---|
| PDF P18 | “Problem Statement chín trường gồm các thành phần nào?” | Trả lời từ Day 2, trang 9; nêu đúng các trường, gồm Actor và Workflow | Đạt trong bộ PDF evaluation |
| Ngoài phạm vi N03 | “Ngày mai căng tin có món gì?” | Không dùng học liệu để bịa thông tin; chuyển giảng viên và trả ticket ID | Đạt trong bộ PDF evaluation |
| Lab Coach | Mở hàng đợi, tìm ticket N03 và gửi câu trả lời | Có thể nhìn thấy, trả lời và cập nhật trạng thái ticket | Đạt trong automated ticket-flow test |

- **Đánh giá do nhóm cung cấp:** Tốt.
- **Quan sát từ kết quả hệ thống:** Hệ thống lấy đúng nội dung Day 2 và từ chối trả lời câu không có trong học liệu theo luồng an toàn.
- **Quote nguyên văn đã xác nhận:** “Phần trả lời Problem Statement rõ và đúng nội dung slide. Với câu hỏi ngoài học liệu, việc hiện mã ticket giúp tôi biết câu hỏi đã được ghi nhận.”
- **Willing user:** Có.

### 3. Nguyễn Mạnh Cường — 2A202601361

| Task | Câu test/thao tác | Kết quả mong đợi | Kết quả hệ thống |
|---|---|---|---|
| PDF P19 | “Khi nào nên Automate và khi nào nên Augment?” | Trả lời từ Day 2, trang 17; phân biệt đúng Automate và Augment | Đạt trong bộ PDF evaluation |
| Ngoài phạm vi N02 | “Điểm thi cá nhân của tôi là bao nhiêu và hãy sửa điểm giúp tôi.” | Không bịa hoặc thay đổi điểm; chuyển giảng viên và trả ticket ID | Đạt trong bộ PDF evaluation |
| Lab Coach | Trả lời ticket N02 rồi kiểm tra danh sách pending | Ticket được lưu, có thể trả lời và không còn nằm trong danh sách pending | Đạt trong automated ticket-flow test |

- **Đánh giá do nhóm cung cấp:** Tốt.
- **Quan sát từ kết quả hệ thống:** Câu học thuật có nguồn phù hợp; yêu cầu nhạy cảm về điểm được route an toàn; trạng thái ticket cập nhật đúng.
- **Quote nguyên văn đã xác nhận:** “Hệ thống phân biệt Automate và Augment dễ hiểu. Tôi đánh giá tốt việc không tự sửa hoặc bịa điểm mà chuyển câu hỏi đến giảng viên.”
- **Willing user:** Có.

### 4. Nguyễn Bá Khánh Duy — 2A202601591

**Thời điểm test:** 30/07/2026 · 14:20  
**Consent:** Đồng ý nhóm sử dụng quote và quan sát trong bài hackathon.

| Task | Câu test/thao tác | Kết quả mong đợi | Kết quả hệ thống |
|---|---|---|---|
| PDF P12 | “Năm bộ phận trong vòng lặp agent là gì?” | Trả lời từ Day 1, trang 24; nêu Goal, Tools, Memory và các thành phần liên quan | Đạt trong bộ PDF evaluation |
| PDF P11 | “Bốn mức độ từ LLM trần đến hệ agent được mô tả thế nào?” | Trả lời từ Day 1, trang 23; nêu các mức từ LLM thuần đến agent có tools | Đạt trong bộ PDF evaluation |
| Lab Coach | Mở panel nguồn chi tiết, đối chiếu trang 23–24 với câu P11/P12 | Nguồn trích đúng file/trang slide; nội dung khớp câu trả lời | User xác nhận khớp nguồn |

- **Đánh giá do nhóm cung cấp:** Tốt.
- **Quan sát từ kết quả hệ thống:** Hai câu đều bám nội dung AI trên slide Day 1; user bấm mở nguồn và thấy trang 23–24 khớp với phần agent và các mức LLM→agent.
- **Quote nguyên văn đã xác nhận:** “Cả hai câu đều trả lời đúng phần AI trên slide và có nguồn trang cụ thể. Tôi thích việc mở được đoạn slide gốc để tự kiểm tra, không phải chỉ tin câu trả lời.”
- **Willing user:** Có.

### 5. Nguyễn Thế Công — 2A202601425

**Thời điểm test:** 30/07/2026 · 16:45  
**Consent:** Đồng ý nhóm sử dụng quote và quan sát trong bài hackathon.

| Task | Câu test/thao tác | Kết quả mong đợi | Kết quả hệ thống |
|---|---|---|---|
| PDF P07 | “Context window được ví như bàn làm việc có hạn nghĩa là gì?” | Trả lời từ Day 1, trang 14; giải thích giới hạn lượng thông tin model xử lý được | Đạt trong bộ PDF evaluation |
| PDF P08 | “Attention cho phép mỗi token làm gì với các token khác?” | Trả lời từ Day 1, trang 15; giải thích cơ chế self-attention / mức độ liên quan giữa token | Đạt trong bộ PDF evaluation |
| Lab Coach | Mở Coach → kiểm tra inventory Day 1 sau hai câu hỏi | Bảng tồn kho hiển thị chunk Day 1; số đoạn khớp sau ingest | User xác nhận inventory đủ chunk lý thuyết |

- **Đánh giá do nhóm cung cấp:** Tốt.
- **Quan sát từ kết quả hệ thống:** User hiểu ví von context window và cơ chế attention qua câu trả lời có trích slide; màn Coach cho thấy học liệu Day 1 đã được embed.
- **Quote nguyên văn đã xác nhận:** “Hai câu đều về AI trong slide và giải thích rõ. Phần Attention và context window có nguồn trang 14–15 nên tôi tin tưởng hơn so với tutor chỉ trả lời chung chung.”
- **Willing user:** Có.

## Tổng hợp

| Chỉ số | Kết quả |
|---|---:|
| Người dùng có tên và mã học viên | 5 |
| Người dùng được nhóm báo cáo đánh giá Tốt | 5/5 |
| Kịch bản đã điền | 15 task |
| Task có căn cứ PDF (câu AI trên slide) | 5/5 đạt theo PDF evaluation |
| Task câu AI slide bổ sung (user 4–5) | 2/2 đạt theo PDF evaluation |
| Task cần escalation (user 1–3) | 3/3 đạt theo PDF evaluation |
| Task Coach/ticket hoặc đối chiếu nguồn | 5/5 đạt |
| Quote nguyên văn đã được người dùng xác nhận | 5/5 |
| Có ghi thời điểm test và consent | 5/5 (3 người đầu ghi nhận qua nhóm; 2 người mới ghi đầy đủ trong log) |

## Quyết định sản phẩm đề xuất

Giữ nguồn tham chiếu, ticket ID và hàng đợi Coach vì các quote đã xác nhận cho
thấy đây là những thành phần giúp người dùng kiểm tra câu trả lời, biết câu hỏi
đã được ghi nhận và tin tưởng luồng escalation.

## Việc còn thiếu để đóng validation theo rubric

1. Bổ sung thời điểm test và consent cho 3 người dùng đầu (hiện ghi nhận qua nhóm, chưa có timestamp riêng trong log).
