# Mô tả dự án
Dự án gồm các cửa sổ:
    1. Giao diện cửa sổ chính: chọn hình ảnh, chọn lại hình ảnh, OK(chạy chương trình), Cancel(tắt chương trình)
    2. Giao diện các cửa sổ hiển thị loại bệnh tương ứng dự đoán: Algal Leaf Spot, Leaf Blight, Leaf Spot, No desease
    3. Giao diện không nhận diện được

##### Lưu ý #####
Cần cài đặt thư viện Ultralytis và Torch cùng với CUDA để có thể thực hiện nhận dạng trên ảnh

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