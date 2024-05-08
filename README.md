# Mô tả dự án
Dự án gồm các cửa sổ:
    1. Giao diện cửa sổ chính: chọn hình ảnh, chọn lại hình ảnh, OK(chạy chương trình), Cancel(tắt chương trình)
    2. Giao diện các cửa sổ hiển thị loại bệnh tương ứng dự đoán: Algal Leaf Spot, Leaf Blight, Leaf Spot, No desease
    3. Giao diện không nhận diện được

##### Lưu ý #####
Cần cài đặt thư viện Ultralytis và Torch cùng với CUDA để có thể thực hiện nhận dạng trên ảnh

# Lệnh trên terminal, cpu hoặc gpu
yolo task=detect mode=predict model="best.pt" source="image.jpg" --device=cpu


# Hướng dẫn sử dụng
Download thư mục NLCS
    Cách 1:
        Mở thư mục double click vào file main.exe
        Giao diện hiển thị và sử dụng
        Các chức năng: Chọn hình ảnh, chọn lại hình ảnh khác, OK(Thực hiện dự đoán), Cancel(Tắt chương trình)
    Cách 2:
        Mở phần mềm soạn thảo Visual Studio Code
        Vào thư mục scripts
        Chọn file main.py và thực thi file này
        Giao diện hiển thị và sử dụng
        Các chức năng: Chọn hình ảnh, chọn lại hình ảnh khác, OK(Thực hiện dự đoán), Cancel(Tắt chương trình)


# Cài đặt các thư viện cần thiết
Phiên bản tensorflow: 2.13.0    pip install tensorflow
Phiên bản OpenCV: 4.7.0         pip install opencv-python
Phiên bản Python: 3.8.18        Tải trên website
Phiên bản CUDA: 12.3.2          Tải trên website NVIDIA
Phiên bản Torch: 2.1.2+cu121    install torch torchvision
Phiên bản Ultralytics: 8.1.5    pip install ultralytics

# Cài đặt phần mềm Qt designer
pip install pyqt6
pip install pyqt6-tools
pip install pyqt5designer

# Chuyển dối file .ui sang .py
pyuic6 -x tênfile.ui -o tênfile.py

# Chuyển thành file thực thi để dễ sử dụng
pyinstaller --onefile --icon="icon.ico" --clean main.py


# Thông tin tập dữ liệu thực tế
    train:  48 ảnh
    valid:  10 ảnh
    test:   11 ảnh


# Các chỉ số đánh giá
Class, Images, Instances, Box(P), R, mAP50, mAP50-95: Đây là các chỉ số đánh giá hiệu suất của mô hình:

Class: Lớp mà mô hình đang dự đoán.

Images: Số lượng hình ảnh được sử dụng để kiểm tra mô hình.

Instances: Số lượng thực thể của một lớp cụ thể xuất hiện trong tập kiểm tra.

Box(P): Độ chính xác (Precision) của mô hình trong việc dự đoán hộp giới hạn (bounding box) cho mỗi lớp.
Độ chính xác là tỷ lệ giữa số lượng dự đoán đúng và tổng số lượng dự đoán.

R: Độ nhớ lại (Recall) của mô hình cho mỗi lớp. 
Độ nhớ lại là tỷ lệ giữa số lượng dự đoán đúng và tổng số lượng thực thể thực sự của lớp đó trong tập kiểm tra.

mAP50: Độ chính xác trung bình (Mean Average Precision) tại ngưỡng IoU (Intersection over Union) là 0.5. 
        Đây là một chỉ số đánh giá chất lượng của mô hình dựa trên cả độ chính xác và độ nhớ lại.
        
mAP50-95: Độ chính xác trung bình tại các ngưỡng IoU từ 0.5 đến 0.95 với bước là 0.05. 
        Đây là một chỉ số đánh giá chất lượng của mô hình trong việc xử lý các tình huống khác nhau về kích thước và vị trí của đối tượng.