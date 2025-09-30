# LINUX LAB3: QUẢN LÝ NGƯỜI DÙNG TRONG LINUX

# 1. Tạo Người Dùng và Nhóm


## Tạo user mới tên student
sudo useradd -m -s /bin/bash student

## Đặt mật khẩu cho user student
sudo passwd student

## Tạo nhóm class
sudo groupadd class

## Thêm user student vào nhóm class
sudo usermod -aG class student

## Kiểm tra
cat /etc/passwd | grep student
cat /etc/group | grep class

# 2. Thực hiện phân quyền
## Tạo thư mục documents
mkdir documents

## Đổi chủ sở hữu thư mục documents cho user student và nhóm class
sudo chown student:class documents

## Gán quyền đọc/ghi cho owner (student) và group (class)
sudo chmod 770 documents

## Kiểm tra
ls -ld documents

# 3. Quản lý mật khẩu
## Đặt mật khẩu mới cho student
sudo passwd student

# 4. Xoá người dùng va nhóm
## Xóa user student (kèm thư mục home nếu có)
sudo userdel -r student

## Xóa nhóm class
sudo groupdel class

## Kiểm tra
cat /etc/passwd | grep student
cat /etc/group | grep class

# 5. Bổ sung nhiều người dùng vào nhóm
## Tạo user mới tên user2
sudo useradd -m -s /bin/bash user2
sudo passwd user2

## Tạo nhóm class lại (nếu đã xóa)
sudo groupadd class

## Tạo thêm nhóm mới tên team
sudo groupadd team

## Thêm user2 vào cả nhóm class và team
sudo usermod -aG class,team user2

## Kiểm tra
groups user2

