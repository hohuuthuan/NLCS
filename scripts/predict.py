from asyncio.windows_events import NULL
import os
import shutil
from pathlib import Path
import argparse
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

# Tạo lệnh
command = f"yolo task={task} mode={mode} model=\"{model_path}\" source=\"{source_path}\" --project=\"{output_path}\""

# Chạy lệnh
os.system(command)

# Tìm thư mục predict mới nhất
source_folder = Path(output_path)
latest_subfolder = max((source_folder / f).resolve() for f in os.listdir(source_folder) if f.startswith('predict'))

# Đường dẫn đến thư mục chứa kết quả dự đoán
destination_path = latest_subfolder


# Load a pretrained YOLOv8n model
model = YOLO(model_path)

names = model.names
result = model.predict(source=destination_path)

for r in result:
    for c in r.boxes.cls:
        print(names[int(c)])
        kq = names[int(c)]


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
