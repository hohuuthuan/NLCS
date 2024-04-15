from PyQt6 import QtCore, QtGui, QtWidgets
import subprocess
import os
import glob
from pathlib import Path
import time

class ProcessingDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Đang xử lý")
        self.setGeometry(100, 100, 150, 40)
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
        self.label.setGeometry(QtCore.QRect(280, 120, 261, 71))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 220, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

          # Thêm nút chọn hình ảnh
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 230, 100, 30))
        self.pushButton.setText("Chọn hình ảnh")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.open_image_dialog)

        # Thêm nút chọn hình ảnh khác và ẩn nó khi khởi tạo
        self.pushButton2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(500, 230, 150, 30))  # Điều chỉnh vị trí và kích thước theo ý muốn
        self.pushButton2.setText("Chọn hình ảnh khác")
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton2.clicked.connect(self.open_image_dialog)
        self.pushButton2.hide()  # Ẩn QPushButton2 khi khởi tạo

        # Thêm QLabel để hiển thị hình ảnh
        self.imageLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.imageLabel.setGeometry(QtCore.QRect(220, 230, 240, 240))  # Điều chỉnh vị trí và kích thước theo ý muốn
        self.imageLabel.setObjectName("imageLabel")
        self.imageLabel.hide()  # Ẩn QLabel khi khởi tạo


        self.buttonBox = QtWidgets.QDialogButtonBox(parent=self.centralwidget)
        self.buttonBox.setGeometry(QtCore.QRect(580, 470, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.buttonBox.setFont(font)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.rejected.connect(MainWindow.close)
        self.buttonBox.accepted.connect(self.handle_ok_button) 

        self.timeEdit = QtWidgets.QTimeEdit(parent=self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(10, 10, 118, 22))
        self.timeEdit.setObjectName("timeEdit")

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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "DỰ ĐOÁN BỆNH"))
        self.label_2.setText(_translate("MainWindow", "Chọn hình ảnh:"))
    
     
    def open_image_dialog(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "", "JPEG Files (*.jpg)")
        if fileName:
            pixmap = QtGui.QPixmap(fileName)
            pixmap = pixmap.scaled(240, 240, QtCore.Qt.AspectRatioMode.IgnoreAspectRatio)
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
        subprocess.Popen(["python", "E:/NIEN_LUAN_CO_SO/scripts/predict.py", "--image_path", self.image_path])
        
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
    MainWindow.show()
    sys.exit(app.exec())
    