## QUẢN LÝ GÓI TIN VÀ THAO TÁC ĐỌC, GHI FILE BẰNG COMMAND LINE

### Bài 1
Cập nhật gói phần mềm hiện tại. Sau đó cài đặt gói **figlet**.  
Kiểm tra xem gói **figlet** đã được cài thành công hay không bằng cách sử dụng thử những tính năng của nó.
Sau đó xóa **figlet** ra khỏi hệ thống.  
Kiểm tra **figlet** đã được xóa/gỡ bằng cách thử chạy lại **figlet** và gặp lỗi.


# Cài figlet
sudo apt install -y figlet

# Kiểm tra: in chữ ASCII lớn
figlet "DevOps Lab"

# Gỡ figlet (và xóa cấu hình, cache)
sudo apt remove --purge -y figlet
sudo apt autoremove -y

# Kiểm tra đã gỡ: lệnh này sẽ báo "command not found"
figlet "Test"

---

### Bài 2
a) Cài đặt phần mềm **lolcat**. Kết hợp phần mềm này với **figlet** để biến text thành cầu vồng trên terminal.  
# Cài ruby (nếu chưa có) và lolcat
sudo apt install -y ruby ruby-dev build-essential
sudo gem install lolcat

# Sau khi cài lại figlet (nếu đã gỡ ở Bài 1)
sudo apt install -y figlet

# Tổ hợp
figlet "Rainbow Text" | lolcat

b) Cài đặt phần mềm **cowsay**. Kết hợp **cowsay** với **lolcat** để vẽ hình ảnh có màu trên terminal.  
sudo apt install -y cowsay
cowsay "Hello DevOps" | lolcat

c) Cài đặt phần mềm **fortune-mod**. Kết hợp **fortune-mod** với **lolcat** để tạo ra 1 đoạn danh ngôn có animation trên terminal.  
sudo apt install -y fortune-mod
# In một câu danh ngôn
fortune | lolcat

# Chạy lặp có "animation" (chuỗi output màu)
while true; do fortune | lolcat; sleep 2; done
# Dùng Ctrl+C để dừng

d) Cài đặt phần mềm **sl**. Kết hợp **sl** với **lolcat** và xem kết quả.  
sudo apt install -y sl
# sl in hoạt hình tàu hỏa; kết hợp với lolcat (lưu ý pipe có thể thay đổi xuất)
sl | lolcat

e) Cài đặt phần mềm **text editor** cho Linux Command Line.  
Sử dụng phần mềm đã cài đặt để viết nội dung dưới đây vào file có tên `text.txt`:  
sudo apt install -y nano
nano text.txt
# Dán nội dung đã cho vào, Ctrl+O để lưu, Ctrl+X để thoát

---


### Bài 3
Liệt kê tất cả những **dependencies** và phiên bản của chúng trong quá trình cài đặt những phần mềm trong bài.
# Liệt kê tất cả gói apt đã cài cùng phiên bản
apt list --installed

# Hoặc lọc ra các gói quan tâm (ví dụ figlet, cowsay, fortune-mod, ruby...)
apt list --installed | grep -E "figlet|cowsay|fortune-mod|ruby|lolcat|sl|nano"

# Liệt kê gem (Ruby) đã cài (lolcat)
gem list --local

# Nếu dùng pip (không dùng ở đây) thì: pip list

# Nếu dùng cpanm (Perl modules) để cài Term::Animation, danh sách:
cpanm --list  # hoặc perl -MCPAN -e '...' (tuỳ hệ)

---


### Bài 4
Cài đặt gói phần mềm có tên **Asciiquarium**.  
Kiểm tra kết quả cài đặt bằng cách chạy các câu lệnh của **Asciiquarium** trên terminal.

# Cài các công cụ cần thiết
sudo apt update
sudo apt install -y wget unzip perl cpanminus build-essential

# Tải source từ GitHub
wget https://github.com/cmatsuoka/asciiquarium/archive/refs/heads/master.zip -O asciiquarium.zip
unzip asciiquarium.zip
cd asciiquarium-master

# Copy script vào /usr/local/bin và cấp quyền
sudo cp asciiquarium /usr/local/bin/
sudo chmod +x /usr/local/bin/asciiquarium

# Cài module Perl Term::Animation bằng cpanminus
sudo cpanm Term::Animation
# Nếu cpanm chưa có:
# sudo apt install -y cpanminus
# sudo cpanm Term::Animation

# Kiểm tra module
perl -MTerm::Animation -e1  # không có output là OK

# Chạy asciiquarium
asciiquarium



