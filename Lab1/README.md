#  README -- Bài tập Linux cơ bản

## Bài 1: Tạo cấu trúc thư mục và file

Yêu cầu:\
Tạo cấu trúc sau, nội dung file copy từ `/etc/passwd`:

    /
    |-- lab
    |   |-- data
    |   |   |-- file1.txt
    |   |   `-- file2.txt
    |   `-- project

👉 Lệnh thực hiện:

``` bash
# Tạo cấu trúc thư mục
mkdir -p lab/data lab/project

# Tạo file có nội dung từ /etc/passwd
cp /etc/passwd lab/data/file1.txt
cp /etc/passwd lab/data/file2.txt

# Kiểm tra
tree lab
```

------------------------------------------------------------------------

## Bài 2: Xóa, di chuyển, sao chép file và thư mục

Yêu cầu:\
1. Sao chép thư mục `lab` thành `backup` (chưa tồn tại).\
2. Tạo thêm:\
- `lab/project/more1.txt` (giống `file1.txt`)\
- `lab/data/more2.txt` (giống `file2.txt`)\
3. Lại sao chép `lab` sang `backup`, ghi đè trực tiếp.\
4. Xóa thư mục `lab`.

👉 Lệnh thực hiện:

``` bash
# Sao chép lab -> backup
cp -r lab backup

# Tạo file more1.txt và more2.txt
cp lab/data/file1.txt lab/project/more1.txt
cp lab/data/file2.txt lab/data/more2.txt

# Ghi đè lab vào backup
cp -rf lab backup

# Xóa lab
rm -rf lab

# Kiểm tra backup
tree backup
```

------------------------------------------------------------------------

## Bài 3: Tập hợp, nén, giải nén thư mục

Yêu cầu:\
- Tạo file nén `backup.tar.bz2` từ thư mục `backup`.\
- Giải nén thành thư mục `lab` với cấu trúc giống `backup`.

👉 Lệnh thực hiện:

``` bash
# Nén thư mục backup
tar -cjf backup.tar.bz2 backup

# Giải nén ra thư mục lab
tar -xjf backup.tar.bz2 -C .
mv backup lab

# Kiểm tra
tree lab
```

------------------------------------------------------------------------

## Bài 4: Lọc dữ liệu đơn giản

### 1. Liệt kê toàn bộ file/thư mục từ `/` rồi lọc file `.txt`

``` bash
ls -R / 2>/dev/null | grep '\.txt$'
```

### 2. Liệt kê toàn bộ rồi lọc file bắt đầu bằng `dat`

``` bash
ls -R / 2>/dev/null | grep '^dat'
```

💡 Gợi ý cách làm chính xác hơn với `find`:

``` bash
find / -type f -name "*.txt" 2>/dev/null
find / -type f -name "dat*" 2>/dev/null
```

------------------------------------------------------------------------

📌 Như vậy, toàn bộ 4 bài đã được gom thành một quy trình hoàn chỉnh
trong README.
