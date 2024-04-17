from PyQt6 import QtCore, QtGui, QtWidgets
import os
import glob
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(891, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 110, 271, 51)) 
        
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
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
        self.textEdit.setGeometry(QtCore.QRect(320, 170, 571, 211))
        self.textEdit.setObjectName("textEdit")
        
        
        # Logo
        self.logoLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.logoLabel.setGeometry(QtCore.QRect(10, 10, 200, 100))  # Điều chỉnh vị trí và kích thước theo ý muốn
        # Tải hình ảnh logo và đặt nó cho QLabel
        logo = QtGui.QPixmap("C:/Users/hohuu/Pictures/lá.png")
        logo = logo.scaled(200, 100, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
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
        self.label_link.setGeometry(QtCore.QRect(450, 380, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_link.setFont(font)
        self.label_link.setText('<a href="https://nongnghiepthuanthien.vn/cach-xu-ly-va-phong-ngua-benh-dom-rong-tren-cay-sau-rieng/#3_Cach_xu_ly_va_phong_ngua_benh_dom_rong_tren_sau_rieng" style="text-decoration: none">Tham khảo thêm cách phòng tránh tại đây.</a>')
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
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">Bệnh đốm rong</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">1</span><span style=\" font-size:12pt;\">. Nhà vườn sử dụng chế phẩm vaccin kết hợp với siêu đồng phun kép 2 lần cách nhau 2-3 ngày.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">2</span><span style=\" font-size:12pt;\">. Phun ướt đấm thân cành và hai mặt lá để tẩy rửa mảng rong và diệt tảo gây hại, đồng thời diệt các loại nấm khuẩn và kích kháng cho cây. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">3</span><span style=\" font-size:12pt;\">. Nếu bệnh trên thân, cành thì pha đậm đặc dung dịch vaccin và siêu đồng rồi quét đậm lên thân, cành.</span></p></body></html>"))
        
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
    MainWindow.setFixedSize(900, 600)
    MainWindow.show()
    sys.exit(app.exec())