import os
import shutil
import numpy as np

# Đường dẫn đến thư mục chứa dữ liệu cần chia
data_dir = 'E:/NLCS/data/trainthucte'

# Tạo các thư mục để lưu những hình ảnh được chia
os.makedirs('E:/NLCS/data/test/images', exist_ok=True)
os.makedirs('E:/NLCS/data/test/labels', exist_ok=True)

# Lấy danh sách tất cả các tệp trong thư mục dữ liệu
files = os.listdir(os.path.join(data_dir, 'images'))

# Chọn ngẫu nhiên xx% tệp, tùy theo cách chia mà thay thế chỉ số %
test_files = np.random.choice(files, size=int(len(files) * 1), replace=False)

# Di chuyển các tệp đã chọn sang thư mục kiểm thử
for file in test_files:
    # Di chuyển tệp hình ảnh, 
    shutil.move(os.path.join(data_dir, 'images', file), 'E:/NLCS/data/test/images')


    # Thay đổi phần mở rộng của tệp từ .jpg sang .txt
    # Giúp xác định tên nhãn dựa trên tên hình ảnh
    label_file = os.path.splitext(file)[0] + '.txt'
    
    # Di chuyển tệp nhãn
    shutil.move(os.path.join(data_dir, 'labels', label_file), 'E:/NLCS/data/test/labels')
