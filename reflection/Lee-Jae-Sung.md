# Reflection cá nhân — Lee Jae Sung

**Họ và tên:** Lee Jae Sung  
**Mã học viên:** 2A202601731  
**Nhóm:** VLearn Tutor  
**Vai trò:** Frontend hai vai trò và điều phối validation

## 1. Phần tôi phụ trách

Trong dự án, tôi phụ trách lớp giao diện và vòng kiểm thử với người dùng thật:

- Thiết kế và implement `frontend/index.html`: landing chọn vai trò, không gian chat học viên và bảng điều khiển Lab Coach.
- Xây luồng chat học viên gọi `POST /api/chat`, hiển thị pipeline 2 tầng (định vị buổi → lấy context → tóm tắt) và panel nguồn chi tiết khi bấm vào mã đoạn `[Txx-NNN]`.
- Xây màn Coach: nút nạp/embed học liệu, bảng tồn kho theo buổi/chủ đề, và **hàng đợi câu hỏi chờ giảng viên** (`GET /api/questions`, `POST /api/questions/{id}/answer`).
- Điều phối validation CP5: mời 3 willing users ngoài nhóm (Nguyễn Đình Bình, Đào Văn Đà, Nguyễn Mạnh Cường), phối hợp gán task test theo kịch bản trong `eval/pdf-golden-set.json` và đối chiếu kết quả với bộ PDF evaluation.

Quyết định thiết kế quan trọng nhất của tôi là tách rõ hai không gian làm việc thay vì gom chung một màn hình. Học viên chỉ thấy chat và nguồn; Coach thấy ingest, inventory và ticket queue. Mục tiêu là giảm nhầm vai trò khi demo và giúp người test hiểu luồng “trả lời có căn cứ hoặc chuyển giảng viên”.

## 2. AI đã hỗ trợ tôi như thế nào

Tôi dùng AI như công cụ viết UI nhanh và phản biện trải nghiệm, không giao toàn bộ quyết định sản phẩm. AI hỗ trợ tôi:

- Phác thảo layout hai vai trò, bảng màu và component chat/pipeline animation.
- Gợi ý cách render danh sách nguồn, drawer trích transcript và bảng inventory Coach.
- Viết nháp JavaScript gọi API, xử lý trạng thái loading và refresh hàng đợi ticket sau khi Coach trả lời.
- Soạn checklist task validation (câu có căn cứ PDF, câu mơ hồ/ngoài phạm vi, thao tác Lab Coach) để nhóm ghi log thống nhất.
- Đọc kết quả eval fail và chỉ ra chỗ UI đang “làm đẹp” câu trả lời sai — ví dụ badge xanh “Tìm thấy” khi backend vẫn trả `found=true` cho câu ngoài phạm vi.

Tôi vẫn tự kiểm tra bằng cách chạy prototype local, bấm thử từng luồng và đối chiếu với golden set. Phần AI gợi ý chỉ được giữ khi tôi giải thích được hành vi trên màn hình và khi nó khớp feedback từ willing users.

## 3. Case fail đáng nhớ

Case fail có ảnh hưởng lớn nhất đối với phần frontend là câu:

> “Công thức nấu phở bò Hà Nội chuẩn là gì?” (Q17)

Ở phiên bản đầu, backend vẫn trả `found=true` với câu trả lời extractive từ chunk không liên quan. Giao diện của tôi luôn hiển thị badge xanh **“✓ Tìm thấy ở …”** kèm danh sách nguồn — trông rất đáng tin dù nội dung không trả lời câu hỏi.

Đây là lỗi sản phẩm kép: logic backend chưa từ chối đúng, và UI chưa phân biệt “có chunk gần nghĩa” với “trả lời được câu hỏi”. Với học viên, một câu trả lời dài có nguồn trích dẫn tạo cảm giác đúng hơn một câu “không biết” — đặc biệt nguy hiểm với câu hỏi ngoài học liệu.

Nhóm xử lý theo hai hướng:

1. Backend thêm guardrail/preflight (nhóm Duy) để các câu ngoài phạm vi trả `found=false` hoặc `escalated` kèm ticket.
2. Frontend cần hiển thị rõ trạng thái từ chối/chuyển giảng viên — không dùng badge xanh cho mọi phản hồi có `sources`.

Sau khi backend đạt 36/36 transcript và 24/24 PDF, tôi rút ra rằng UI phải phản ánh **routing decision**, không chỉ mirror output của retrieval.

## 4. Bài học cá nhân

Bài học lớn nhất của tôi là giao diện không trung lập: nó có thể làm câu trả lời sai trông đúng. Badge màu, animation pipeline và danh sách nguồn đều là tín hiệu tin cậy. Với tutor học tập, thiết kế an toàn quan trọng không kém logic AI.

Tôi cũng học được giá trị của validation sớm. Ba willing users giúp nhóm phát hiện điều mà golden set số liệu chưa nói hết: họ quan tâm **ticket ID**, khả năng mở Coach trả lời, và việc hệ thống không tự đoán khi câu hỏi mơ hồ. Quote trong `validation/feedback-log.md` xác nhận điều này — ví dụ “khi câu hỏi chưa rõ, hệ thống chuyển giảng viên thay vì tự đoán”.

Cuối cùng, phân vai rõ (Học viên vs Coach) giúp demo và kiểm thử nhất quán hơn, nhưng đòi hỏi tôi hiểu cả contract API backend, không chỉ HTML/CSS. Vibe-coding rule của hackathon nhắc tôi phải giải thích được từng luồng tôi build — từ `ask()` tới `loadQuestions()` và `answerQuestion()`.

## 5. Nếu có thêm thời gian

Tôi sẽ ưu tiên:

- Hiển thị rõ ba trạng thái trên UI học viên: **answered**, **declined**, **escalated** (kèm mã ticket copy được).
- Thêm trạng thái loading/error thống nhất và empty state rõ ràng cho hàng đợi Coach.
- Thu thập thêm ≥2 willing users để đủ ≥5 feedback theo rubric validation.
- Ghi thời điểm test và consent trong log ngay tại UI hoặc form Coach.
- Thử nghiệm A/B ngắn: badge xanh vs thông báo trung tính khi confidence thấp, đo mức tin cậy người dùng.
