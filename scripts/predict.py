import os
import torch
import argparse # Xử lý các đối số dòng lệnh
from ultralytics import YOLO

# Tạo trình phân tích cú pháp đối số
parser = argparse.ArgumentParser(description='Predict script')
parser.add_argument('--image_path', type=str, help='Path to the image')

# Phân tích cú pháp đối số
args = parser.parse_args()

# Định nghĩa các tham số
task = "detect"
mode = "predict"
model_path = "E:/NLCS/models/best.pt"
source_path = args.image_path  # Sử dụng đường dẫn hình ảnh từ dòng lệnh
output_path = "E:/NLCS/results"  


# Kiểm tra sự hỗ trợ của CUDA
device = "cuda" if torch.cuda.is_available() else "cpu"

# Tạo lệnh
command = f"yolo task={task} mode={mode} model=\"{model_path}\" source=\"{source_path}\" project=\"{output_path}\" --device={device}"


# Chạy lệnh
os.system(command)

# Đường dẫn đến hình ảnh dự đoán
destination_path = source_path


# Chạy nhận diện lại để lấy ra tên nhãn
model = YOLO(model_path)
names = model.names
result = model.predict(source=destination_path)

for r in result:
    for c in r.boxes.cls:
        print(names[int(c)])
        kq = names[int(c)]      # Lấy ra tên nhãn


loaibenh = ['Algal Leaf Spot', 'Leaf Blight', 'Leaf Spot', 'No Disease']

if 'kq' in globals():
    if kq == loaibenh[0]:
        os.system('python "E:/NLCS/scripts/loaibenh/domrong.py"')
    elif kq == loaibenh[1]:
        os.system('python "E:/NLCS/scripts/loaibenh/chayla.py"')
    elif kq == loaibenh[2]:
        os.system('python "E:/NLCS/scripts/loaibenh/domla.py"')
    elif kq == loaibenh[3]:
        os.system('python "E:/NLCS/scripts/loaibenh/nodisease.py"')
else:
    print("Không nhận dạng được")
    os.system('python "E:/NLCS/scripts/loaibenh/khongtimthay.py"')
