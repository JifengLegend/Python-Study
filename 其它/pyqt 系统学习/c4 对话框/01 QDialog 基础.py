'''
对话框 QDialog

QMessageBox
QColorDialog
QFileDialog
QFontDialog
QinputDialog
'''

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class QDialogDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QDialog 案例")
        self.resize(200,200)
        self.initUi()
    def initUi(self):
        self.bt1=QPushButton("弹出对话框",self)
        self.bt1.clicked.connect(self.showDialog)

    def showDialog(self):
        dialog=QDialog()
        bt2=QPushButton("确定",dialog)
        bt2.clicked.connect(dialog.close)

        dialog.setWindowTitle("这是一个对话框")
        # 设置模式
        dialog.setWindowModality(Qt.ApplicationModal)

        dialog.exec()

if __name__ == "__main__":
    app=QApplication(sys.argv)
    main=QDialogDemo()
    main.show()
    sys.exit(app.exec_())

