'''
对话框 QMessgegBox

1. 关于
2. 错误
3. 警告
4. 提问
5. 消息
'''

import sys
import os
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
def chRec():
    absPath=__file__
    recPath=absPath[:absPath.rfind("\\")]
    os.chdir(recPath)
class QMessegeBoxDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QDialog 案例")
        self.resize(200,200)
        self.initUi()
    def initUi(self):
        

        self.bt1=QPushButton("关于对话框",self)
        self.bt1.clicked.connect(self.showDialog)

        self.bt2=QPushButton('消息对话框',self)
        self.bt2.clicked.connect(self.showDialog)

        self.bt3=QPushButton('警告对话框',self)
        self.bt3.clicked.connect(self.showDialog)

        self.bt4=QPushButton('错误对话框',self)
        self.bt4.clicked.connect(self.showDialog)

        self.bt5=QPushButton('提问对话框',self)
        self.bt5.clicked.connect(self.showDialog)

        lay1=QVBoxLayout()
        lay1.addWidget(self.bt1)
        lay1.addWidget(self.bt2)
        lay1.addWidget(self.bt3)
        lay1.addWidget(self.bt4)
        lay1.addWidget(self.bt5)

        self.setLayout(lay1)
    def showDialog(self):
        text=self.sender().text()
        if text=='关于对话框':
            QMessageBox.about(self,'关于','这是一个关于对话框')
        elif text=='消息对话框':
            reply=QMessageBox.information(self,'消息','这是一个消息对话框',QMessageBox.Yes|QMessageBox.No|QMessageBox.Cancel)
            print(reply)
        elif text=='警告对话框':
            QMessageBox.warning(self,'警告','这是一个警告对话框',QMessageBox.Yes|QMessageBox.Retry)
        elif text=='错误对话框':
            QMessageBox.critical(self,'关于','这是一个关于对话框')
        elif text=='提问对话框':
            QMessageBox.question(self,'关于','这是一个关于对话框')

if __name__ == "__main__":
    chRec()
    app=QApplication(sys.argv)
    main=QMessegeBoxDemo()
    main.show()
    sys.exit(app.exec_())

