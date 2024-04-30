import os
import shutil
import numpy as np

# Đường dẫn đến thư mục chứa dữ liệu cần chia
data_dir = 'E:/NIÊN LUẬN CƠ SỞ/code backup/NIEN_LUAN_CO_SO/data/test'

# Tạo các thư mục để lưu những hình ảnh được chia
os.makedirs('E:/NIÊN LUẬN CƠ SỞ/code backup/NIEN_LUAN_CO_SO/data/valid/images', exist_ok=True)
os.makedirs('E:/NIÊN LUẬN CƠ SỞ/code backup/NIEN_LUAN_CO_SO/data/valid/labels', exist_ok=True)

# Lấy danh sách tất cả các tệp trong thư mục dữ liệu
files = os.listdir(os.path.join(data_dir, 'images'))

# Chọn ngẫu nhiên xx% tệp, tùy theo cách chia mà thay thế chỉ số %
test_files = np.random.choice(files, size=int(len(files) * 0.5), replace=False)

# Di chuyển các tệp đã chọn sang thư mục kiểm thử
for file in test_files:
    # Di chuyển tệp hình ảnh, 
    shutil.move(os.path.join(data_dir, 'images', file), 'E:/NIÊN LUẬN CƠ SỞ/code backup/NIEN_LUAN_CO_SO/data/valid/images')


    # Thay đổi phần mở rộng của tệp từ .jpg sang .txt
    # Giúp xác định tên nhãn dựa trên tên hình ảnh
    label_file = os.path.splitext(file)[0] + '.txt'
    
    # Di chuyển tệp nhãn
    shutil.move(os.path.join(data_dir, 'labels', label_file), 'E:/NIÊN LUẬN CƠ SỞ/code backup/NIEN_LUAN_CO_SO/data/valid/labels')
