# Reflection cá nhân — Vũ Đức Duy

**Họ và tên:** Vũ Đức Duy  
**Mã học viên:** 2A202601023  
**Nhóm:** VLearn Tutor  
**Vai trò:** Agent, backend, vector database và tích hợp AI

## 1. Phần tôi phụ trách

Trong dự án, tôi phụ trách phần kỹ thuật chính của prototype:

- Xây dựng backend FastAPI và các API phục vụ luồng hỏi đáp.
- Thiết kế agent có hai hướng xử lý: trả lời khi có đủ căn cứ hoặc chuyển câu hỏi cho giảng viên khi không chắc chắn.
- Tích hợp ChromaDB để lưu và truy xuất nội dung slide cùng các câu trả lời đã được giảng viên xác nhận.
- Tích hợp Gemini cho embedding, đánh giá semantic relevance, sinh câu trả lời có căn cứ và OCR tài liệu.
- Xây dựng luồng giảng viên trả lời ticket và đưa Q&A đã duyệt trở lại kho tri thức.
- Phối hợp kiểm tra các case ngoài phạm vi, input mơ hồ và câu hỏi có chi phí sai cao.

Quyết định kỹ thuật quan trọng nhất của tôi là không chỉ dựa vào cosine similarity. Hệ thống kết hợp ngưỡng vector với semantic relevance gate; nếu context chỉ gần nghĩa nhưng không chứa câu trả lời trực tiếp, hệ thống phải chuyển giảng viên.

## 2. AI đã hỗ trợ tôi như thế nào

Tôi sử dụng AI như một công cụ hỗ trợ lập trình và phản biện thiết kế, không giao toàn bộ quyết định cho AI. AI hỗ trợ tôi:

- Đề xuất cấu trúc LangGraph cho flow `search → relevance gate → answer/escalate`.
- Gợi ý cách tổ chức schema của ChromaDB và SQLite ticket queue.
- Viết nháp prompt cho relevance gate và grounded answer.
- Phát hiện các trường hợp biên cần kiểm thử như câu hỏi realtime, dữ liệu cá nhân, prompt injection và input thiếu ngữ cảnh.
- Hỗ trợ tạo runner đánh giá, đọc kết quả fail và nhóm lỗi theo nguyên nhân.
- Kiểm tra lỗi code, trong đó có lỗi batching embedding sử dụng biến delay chưa được truyền đúng.

Tôi vẫn phải tự kiểm tra output, chạy test và đối chiếu với dữ liệu thật. Những đề xuất của AI chỉ được giữ lại khi vượt qua golden set hoặc có bằng chứng từ prototype.

## 3. Case fail đáng nhớ

Case fail có ảnh hưởng lớn nhất là câu:

> “Giải thích cái này cho tôi.”

Ở phiên bản đầu, retrieval tìm được các đoạn có similarity đủ cao và semantic gate cho phép trả lời. Tutor tự chọn Transformer làm chủ đề rồi trả lời dài, dù người dùng không hề cung cấp “cái này” đang chỉ nội dung nào.

Đây không phải lỗi kiến thức đơn thuần. Hệ thống đã tự lấp phần thông tin còn thiếu và tạo cảm giác rất tự tin. Nếu hành vi này xảy ra với deadline, điểm số hoặc kiến thức quan trọng, học viên có thể tin một câu trả lời không đúng ý định.

Nhóm sửa lỗi bằng ba lớp:

1. Thêm preflight guard nhận diện đại từ không có tham chiếu như “nó”, “cái này”, “cái đó”.
2. Siết prompt relevance: cùng chủ đề hoặc trùng vài từ chưa đủ để trả lời.
3. Yêu cầu grounded-answer prompt chỉ được đưa ra claim có nguồn hỗ trợ trực tiếp.

Sau thay đổi, case trên được chuyển sang luồng escalation. Bộ transcript tăng từ 27/36 lên 36/36, còn bộ PDF đạt 24/24.

## 4. Bài học cá nhân

Bài học lớn nhất của tôi là similarity không đồng nghĩa với answerability. Một đoạn tài liệu có thể rất gần chủ đề nhưng vẫn không chứa dữ kiện cần để trả lời câu hỏi. Vì vậy, sản phẩm RAG cần đánh giá riêng hai việc: “tìm thấy nội dung liên quan” và “nội dung đó có đủ để trả lời hay không”.

Tôi cũng học được rằng biết từ chối đúng lúc là một tính năng sản phẩm, không phải lỗi. Với trợ lý học tập, một ticket rõ ràng và có đường chuyển người thật tốt hơn một câu trả lời trôi chảy nhưng không có căn cứ.

Cuối cùng, evaluation phải được thiết kế trước khi tối ưu. Golden set có case mơ hồ, ngoài phạm vi và domain high-cost đã giúp nhóm phát hiện vấn đề mà happy path không thể cho thấy. Việc giữ lại kết quả fail và phân tích nguyên nhân giúp tôi hiểu hệ thống sâu hơn so với chỉ cố đạt một con số đẹp.

## 5. Nếu có thêm thời gian

Tôi sẽ ưu tiên:

- Thay các rule preflight hiện tại bằng intent/scope classifier được đánh giá trên tập dữ liệu lớn hơn.
- Version hóa Q&A giảng viên để tránh câu trả lời cũ mâu thuẫn với tài liệu mới.
- Thêm authentication và authorization thật cho hai vai trò học viên–giảng viên.
- Đo groundedness bằng người chấm độc lập thay vì chỉ dùng keyword và source presence.
- Theo dõi false escalation để bảo đảm hệ thống an toàn nhưng không từ chối quá nhiều.
