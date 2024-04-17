from PyQt6 import QtCore, QtGui, QtWidgets
import subprocess
import os
import glob
from pathlib import Path
import time

class ProcessingDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("ĐANG XỬ LÝ, VUI LÒNG CHỜ...")
        self.setGeometry(100, 100, 230, 10)
        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QGuiApplication.primaryScreen().geometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

class Ui_MainWindow(object):
    def __init__(self):
        self.image_selected = False
        self.image_path = None 
          
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 40, 600, 71))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 220, 151, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(710, 3, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        
        
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(695, 20, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(280, 10, 261, 71))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")


        # Thêm nút chọn hình ảnh
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(63, 260, 100, 30))
        self.pushButton.setText("Chọn hình ảnh")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.open_image_dialog)

        # Thêm nút chọn hình ảnh khác và ẩn nó khi khởi tạo
        self.pushButton2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(185, 230, 150, 30))  # Điều chỉnh vị trí và kích thước theo ý muốn
        self.pushButton2.setText("Chọn hình ảnh khác")
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton2.clicked.connect(self.open_image_dialog)
        self.pushButton2.hide()  # Ẩn QPushButton2 khi khởi tạo

        # Thêm QLabel để hiển thị hình ảnh
        self.imageLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.imageLabel.setGeometry(QtCore.QRect(60, 265, 300, 300))  # Điều chỉnh vị trí và kích thước theo ý muốn
        self.imageLabel.setObjectName("imageLabel")
        self.imageLabel.hide()  # Ẩn QLabel khi khởi tạo

        
        # Tạo một QLabel mới để logo
        self.logoLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.logoLabel.setGeometry(QtCore.QRect(10, 10, 200, 100))  # Điều chỉnh vị trí và kích thước theo ý muốn
        # Tải hình ảnh logo và đặt nó cho QLabel
        logo = QtGui.QPixmap("C:/Users/hohuu/Pictures/lá.png")
        logo = logo.scaled(200, 100, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.logoLabel.setPixmap(logo)
        

        # Tạo một QLabel mới để logo
        self.logoLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.logoLabel.setGeometry(QtCore.QRect(350, 110, 400, 400))  # Điều chỉnh vị trí và kích thước theo ý muốn
        # Tải hình ảnh logo và đặt nó cho QLabel
        logo = QtGui.QPixmap("C:/Users/hohuu/Pictures/robo-tree.png")
        logo = logo.scaled(400, 400, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.logoLabel.setPixmap(logo)
        
        

        # # Chèn ảnh nền
        # palette = QtGui.QPalette()
        # # Tải hình ảnh và tạo một QBrush
        # image = QtGui.QImage("C:/Users/hohuu/Pictures/OIG3.jpg")
        # brush = QtGui.QBrush(image)
        # # Thiết lập brush như một bức tranh nền cho palette
        # palette.setBrush(QtGui.QPalette.ColorRole.Window, brush)
        # # Áp dụng palette cho MainWindow
        # MainWindow.setPalette(palette)



        self.buttonBox = QtWidgets.QDialogButtonBox(parent=self.centralwidget)
        self.buttonBox.setGeometry(QtCore.QRect(580, 530, 201, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.buttonBox.setFont(font)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.rejected.connect(MainWindow.close)
        self.buttonBox.accepted.connect(self.handle_ok_button) 


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DỰ ĐOÁN BỆNH TRÊN CÂY SẦU RIÊNG"))
        self.label.setText(_translate("MainWindow", "DỰ ĐOÁN BỆNH TRÊN CÂY SẦU RIÊNG"))
        self.label_2.setText(_translate("MainWindow", "Chọn hình ảnh:"))
        self.label_3.setText(_translate("MainWindow", "B2107182"))
        self.label_4.setText(_translate("MainWindow", "Hồ Hữu Thuận"))
        self.label_5.setText(_translate("MainWindow", "NIÊN LUẬN CƠ SỞ"))
    def open_image_dialog(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "", "JPEG Files (*.jpg)")
        if fileName:
            pixmap = QtGui.QPixmap(fileName)
            pixmap = pixmap.scaled(300, 300, QtCore.Qt.AspectRatioMode.IgnoreAspectRatio)
            self.imageLabel.setPixmap(pixmap)
            self.pushButton.hide()
            self.pushButton2.show()
            self.imageLabel.show()
            self.image_selected = True
            self.image_path = fileName
            
    def handle_ok_button(self):
        if not self.image_selected:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText("Hãy chọn hình ảnh")
            msg.setWindowTitle("Thông báo")
            msg.exec()
        else:
            self.run_prediction()

    def run_prediction(self):
        # Hiển thị cửa sổ thông báo đang xử lý
        self.processing_dialog = ProcessingDialog()
        self.processing_dialog.show()

        # Gọi đoạn mã predict.py với đường dẫn hình ảnh làm đối số
        subprocess.Popen(["python", "E:/NLCS/scripts/predict.py", "--image_path", self.image_path])
        
        # Kiểm tra đến khi nào có thư mục predict mới xuất hiện
        source_folder = Path("C:/Users/hohuu/runs/detect")
        old_folders = [f for f in os.listdir(source_folder) if f.startswith('predict')]
        while True:
            new_folders = [f for f in os.listdir(source_folder) if f.startswith('predict')]
            if len(new_folders) > len(old_folders):
                break
            time.sleep(1)  # Đợi 1 giây trước khi kiểm tra lại

        # Tắt cửa sổ thông báo đang xử lý
        self.processing_dialog.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setFixedSize(800, 600)
    MainWindow.show()
    sys.exit(app.exec())
    