# LAB 4: QUẢN LÝ TIẾN TRÌNH

## Kiến thức mới trong bài thực hành

### 1. Liệt kê tiến trình
- Lệnh `ps` dùng để liệt kê các tiến trình đang chạy trên hệ thống.
- Tùy chọn:
  - `ps -ef`: hiển thị tất cả tiến trình, không chỉ tiến trình liên quan đến terminal.
  - `ps aux`: hiển thị chi tiết PID, %CPU, %MEM, TTY, thời gian chạy, và lệnh thực thi.
- Kết hợp `more` để phân trang:
  ```bash
  ps -ef | more
  ```

### 2. Xem người dùng
- Lệnh `whoami`: hiển thị tên người dùng hiện tại.
- Lệnh `w`: hiển thị danh sách người dùng đang đăng nhập và các hoạt động của họ.

### 3. Quản lý tiến trình người dùng
- `ps`: hiển thị tiến trình do người dùng đang chạy.
- `ps aux | grep root`: hiển thị tiến trình của người dùng Root.

### 4. Điều chỉnh độ ưu tiên
- Dùng lệnh `renice priority PID` để thay đổi độ ưu tiên của tiến trình.
- Priority (nice value) có giá trị từ **-20 (ưu tiên cao nhất)** đến **19 (thấp nhất)**.
- PID: ID của tiến trình muốn điều chỉnh.

### 5. Xem mức sử dụng CPU và bộ nhớ
- Lệnh `top`: hiển thị danh sách tiến trình cùng mức sử dụng CPU và RAM theo thời gian thực.

### 6. Quản lý tiến trình nền
- Thêm `&` sau lệnh để chạy tiến trình ở nền, ví dụ:
  ```bash
  sleep 100 &
  ```
- Lệnh `jobs`: liệt kê các tiến trình nền.
- Lệnh `bg %n`: chạy tiến trình nền tiếp tục.
- Lệnh `fg %n`: đưa tiến trình nền về foreground.

### 7. Hủy tiến trình
- Dùng `kill PID` để hủy tiến trình.
- Nếu không được, dùng `kill -9 PID` để ép buộc dừng.

---

## Ghi chú
- Các lệnh quản lý tiến trình cần quyền sudo khi thao tác với tiến trình hệ thống hoặc tiến trình của user khác.
- Luôn kiểm tra PID trước khi `kill` để tránh dừng nhầm tiến trình quan trọng.
