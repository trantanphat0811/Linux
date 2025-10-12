# LAB5 - LẬP TRÌNH SHELL TRÊN LINUX

## Cách làm việc với máy ảo Linux và Nano
1. Mở Terminal và di chuyển đến thư mục làm việc:
   ```bash
   cd /home/ubuntu/iDragonCloud

## BÀI TẬP 1: Tự động kiểm tra và tạo thư mục nếu chưa tồn tại
import os
folder = "data_folder"
if not os.path.exists(folder):
    os.mkdir(folder)
    print("Đã tạo thư mục:", folder)
else:
    print("Thư mục đã tồn tại.")

## BÀI TẬP 2: Tính tổng các số chẵn từ 1 đến N
N = int(input("Nhập N: "))
tong = sum(i for i in range(1, N+1) if i % 2 == 0)
print("Tổng các số chẵn là:", tong)

## BÀI TẬP 3: In bảng cửu chương
for i in range(1, 10):
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
    print("-" * 15)

## BÀI TẬP 4: Tính giai thừa (Đệ quy)
def giaithua(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * giaithua(n-1)
print(giaithua(int(input("Nhập N: "))))


## BÀI TẬP 5: In dãy Fibonacci đến N
N = int(input("Nhập N: "))
fib = [0,1]
for i in range(2, N):
    fib.append(fib[-1] + fib[-2])
print(fib[:N])

## BÀI TẬP 6: Tìm số lớn nhất trong danh sách
nums = list(map(int, input("Nhập danh sách số: ").split()))
print("Số lớn nhất là:", max(nums))


## BÀI TẬP 7: Kiểm tra số hoàn hảo
n = int(input("Nhập số: "))
tong = sum(i for i in range(1, n) if n % i == 0)
print("Hoàn hảo" if tong == n else "Không hoàn hảo")

## BÀI TẬP 8: Kiểm tra số Armstrong
n = int(input("Nhập số: "))
digits = [int(d) for d in str(n)]
if sum(d**3 for d in digits) == n:
    print("Là số Armstrong")
else:
    print("Không phải số Armstrong")

## BÀI TẬP 9: Kiểm tra cấp số cộng
nums = list(map(int, input("Nhập dãy số: ").split()))
hieu = nums[1] - nums[0]
if all(nums[i+1] - nums[i] == hieu for i in range(len(nums)-1)):
    print("Là cấp số cộng")
else:
    print("Không phải cấp số cộng")

## BÀI TẬP 10: Kiểm tra số Palindrome (vòng lặp)
n = input("Nhập số: ")
dao = ""
for ch in n:
    dao = ch + dao
print("Palindrome" if n == dao else "Không phải Palindrome")


