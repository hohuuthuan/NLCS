import os
from PIL import Image

data_dir = 'C:/Users/hohuu/Desktop/data thuc te'
output_dir = os.path.join(data_dir, 'hinhanh')

# Tạo thư mục output nếu nó chưa tồn tại
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Duyệt qua tất cả các file trong thư mục data
for filename in os.listdir(data_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        img = Image.open(os.path.join(data_dir, filename))
        # Thay đổi kích thước hình ảnh
        img_resized = img.resize((640, 640))
        # Lưu hình ảnh đã resize vào thư mục hinhanh
        img_resized.save(os.path.join(output_dir, filename))



# import os

# def count_images(directory, prefix):
#     # Lấy danh sách tất cả các file trong thư mục
#     files = os.listdir(directory)

#     # Lọc ra những file có tên bắt đầu bằng prefix
#     images = [file for file in files if file.startswith(prefix) and file.endswith(('.png', '.jpg', '.jpeg'))]

#     # Trả về số lượng ảnh
#     return len(images)

# # Sử dụng hàm, thay đổi đường dẫn thư mục và thay đổi chuỗi cần tìm
# num_images = count_images('E:/NLCS/data/train/images', 'hht')
# print(f"Số lượng ảnh trong thư mục 'ttt' có tên bắt đầu bằng 'hht': {num_images}")