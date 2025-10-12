import os

folder_name = "data_folder"

if not os.path.exists(folder_name):
    os.makedirs(folder_name)
    print(f"Đã tạo thư mục: {folder_name}")
else:
    print(f"Thư mục '{folder_name}' đã tồn tại.")
