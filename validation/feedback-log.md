# Validation log — VLearn Tutor

**Ngày tổng hợp:** 30/07/2026  
**Prototype:** VLearn Tutor — trả lời có căn cứ hoặc chuyển giảng viên  
**Người phụ trách log:** Nguyễn Trường An  
**Trạng thái:** Đã điền kịch bản và kết quả kiểm thử cho 3 người dùng do nhóm cung cấp; ba quote nguyên văn đã được xác nhận.

## Phương pháp

Mỗi người dùng được gán ba task:

1. Hỏi một câu có đáp án thực sự trong PDF và kiểm tra nguồn.
2. Hỏi một câu mơ hồ/ngoài phạm vi và kiểm tra việc tạo ticket.
3. Mở Lab Coach, kiểm tra ticket và thử luồng trả lời.

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

## Tổng hợp

| Chỉ số | Kết quả |
|---|---:|
| Người dùng có tên và mã học viên | 3 |
| Người dùng được nhóm báo cáo đánh giá Tốt | 3/3 |
| Kịch bản đã điền | 9 task |
| Task có căn cứ PDF | 3/3 đạt theo PDF evaluation |
| Task cần escalation | 3/3 đạt theo PDF evaluation |
| Task Coach/ticket | 3/3 đạt theo automated ticket-flow test |
| Quote nguyên văn đã được người dùng xác nhận | 3/3 |

## Quyết định sản phẩm đề xuất

Giữ nguồn tham chiếu, ticket ID và hàng đợi Coach vì các quote đã xác nhận cho
thấy đây là những thành phần giúp người dùng kiểm tra câu trả lời, biết câu hỏi
đã được ghi nhận và tin tưởng luồng escalation.

## Việc còn thiếu để đóng validation theo rubric

1. Mời thêm ít nhất 2 người ngoài nhóm để đủ ≥5 feedback từ ≥5 người.
2. Ghi thời điểm test và consent sử dụng feedback trong bài hackathon.
