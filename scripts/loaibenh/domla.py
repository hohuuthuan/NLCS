from PyQt6 import QtCore, QtGui, QtWidgets
import os
import glob

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(891, 600)
        
        # Tạo một đối tượng QIcon
        icon = QtGui.QIcon('E:/NLCS/GUI_image/lá.png')
        # Đặt biểu tượng cho cửa sổ
        MainWindow.setWindowIcon(icon)
        
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 110, 271, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(500, 110, 271, 51))
        
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(320, 170, 571, 221))
        self.textEdit.setObjectName("textEdit")
        
        
        # Logo
        self.logoLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.logoLabel.setGeometry(QtCore.QRect(10, 10, 200, 100))  # Điều chỉnh vị trí và kích thước theo ý muốn
        # Tải hình ảnh logo và đặt nó cho QLabel
        logo = QtGui.QPixmap("E:/NLCS/GUI_image/lá.png")
        logo = logo.scaled(100, 70, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.logoLabel.setPixmap(logo)
        
        
        # Tên dự án
        self.label__1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label__1.setGeometry(QtCore.QRect(335, 10, 261, 71))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label__1.setFont(font)
        self.label__1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label__1.setObjectName("label__1")
        
        self.label__2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label__2.setGeometry(QtCore.QRect(170, 40, 600, 71))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label__2.setFont(font)
        self.label__2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label__2.setObjectName("label__2")

        
        self.label__3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label__3.setGeometry(QtCore.QRect(835, 3, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label__3.setFont(font)
        self.label__3.setObjectName("label__3")
        
        
        self.label__4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label__4.setGeometry(QtCore.QRect(820, 20, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label__4.setFont(font)
        self.label__4.setObjectName("label__4")
        
        
        
        self.label_image = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_image.setGeometry(QtCore.QRect(30, 160, 290, 350))  # Đặt vị trí và kích thước cho label hình ảnh

        # Định nghĩa thư mục chứa kết quả
        results_dir = "E:/NLCS/results"

        # Lấy danh sách tất cả các thư mục trong thư mục kết quả
        dirs = glob.glob(os.path.join(results_dir, "*"))

        # Sắp xếp các thư mục theo thời gian sửa đổi
        dirs.sort(key=os.path.getmtime)

        # Lấy thư mục mới nhất
        latest_dir = dirs[-1]

        # Lấy danh sách tất cả các tệp hình ảnh trong thư mục mới nhất
        image_files = glob.glob(os.path.join(latest_dir, "*"))

        # Sắp xếp các tệp theo thời gian sửa đổi
        image_files.sort(key=os.path.getmtime)

        # Lấy tệp hình ảnh mới nhất
        latest_image_file = image_files[-1]

        pixmap = QtGui.QPixmap(latest_image_file)  # Sử dụng hình ảnh mới nhất
        self.label_image.setPixmap(pixmap)
        self.label_image.setScaledContents(True)  # Đặt hình ảnh co giãn theo kích thước của QLabel
    
        
        
        
        
        self.label_link = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_link.setGeometry(QtCore.QRect(450, 400, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_link.setFont(font)
        self.label_link.setText('<a href="https://vietthanghanoi.vn/benh-dom-la-tren-cay-sau-rieng/#:~:text=C%C3%A1c%20bi%E1%BB%87n%20ph%C3%A1p%20ph%C3%B2ng%20tr%E1%BB%AB%20b%E1%BB%87nh%20%C4%91%E1%BB%91m%20l%C3%A1%20g%C3%A2y%20h%E1%BA%A1i%20tr%C3%AAn%20s%E1%BA%A7u%20ri%C3%AAng&text=%E2%80%93%20B%E1%BB%95%20sung%20dinh%20d%C6%B0%E1%BB%A1ng%20c%C3%A2n,s%C3%A1t%20%C4%91%E1%BA%A5t%2C%20c%C3%A0nh%20giao%20t%C3%A1n." style="text-decoration: none">Tham khảo thêm cách phòng tránh tại đây.</a>')
        self.label_link.setOpenExternalLinks(True)
        self.label_link.setObjectName("label_link")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 891, 26))
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
        self.label.setText(_translate("MainWindow", "Hình ảnh nhận dạng được:"))
        self.label_2.setText(_translate("MainWindow", "Phương pháp điều trị:"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">Bệnh đốm lá</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">1</span><span style=\" font-size:12pt;\">. Nên dùng thuốc chứa các loại hoạt chất như Mancozed + Metalaxyl (Rorigold 720WP) phun ướt đều 2 mặt lá. Phun 2 lần cách nhau từ 7-5 ngày để trị bệnh cho cây.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">2</span><span style=\" font-size:12pt;\">. Tăng cường bón phân hữu cơ vi sinh (Trichomix-CTD, Trimix-N1, ...) đặc biệt trong giai đoạn mùa mưa để tăng sức đề kháng cho cây.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">3</span><span style=\" font-size:12pt;\">. Cắt tỉa cành thông thoáng, đặc biệt là cành sát đất đối với cây từ 1-2 năm.</span></p></body></html>"))
        
        self.label__1.setText(_translate("MainWindow", "NIÊN LUẬN CƠ SỞ"))
        self.label__2.setText(_translate("MainWindow", "DỰ ĐOÁN BỆNH TRÊN CÂY SẦU RIÊNG"))
        self.label__3.setText(_translate("MainWindow", "B2107182"))
        self.label__4.setText(_translate("MainWindow", "Hồ Hữu Thuận"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setFixedSize(910, 600)
    MainWindow.show()
    sys.exit(app.exec())
