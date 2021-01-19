'''
对话框 QInputDialog

1. getItem
2. getText
3. getInt
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
class QInputDialogDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("输入对话框 案例")
        self.resize(200,200)
        self.initUi()
    def initUi(self):      
        self.bt1=QPushButton("获取列表中的选项",self)
        self.bt1.clicked.connect(self.getItem)
        self.le1=QLineEdit()


        self.bt2=QPushButton('过去字符串',self)
        self.bt2.clicked.connect(self.getText)
        self.le2=QLineEdit()


        self.bt3=QPushButton('获取整数',self)
        self.bt3.clicked.connect(self.getInt)
        self.le3=QLineEdit()

        lay1=QFormLayout()
        lay1.addRow(self.bt1,self.le1)
        lay1.addRow(self.bt2,self.le2)
        lay1.addRow(self.bt3,self.le3)

        self.setLayout(lay1)

    def getItem(self):
        items = ('C','C++','Ruby','Python','Java')
        item, ok =QInputDialog.getItem(self,'请选择编程语言','语言列表',items)
        if ok and item:
            self.le1.setText(item)
    def getText(self):
        text, ok =QInputDialog.getText(self,'文本输入框','输入姓名')
        if ok and text:
            self.le2.setText(text)
    def getInt(self):
        intNum,ok=QInputDialog.getText(self,'输入对话框','输入年龄')
        if ok and intNum:
            self.le3.setText(str(intNum))

if __name__ == "__main__":
    chRec()
    app=QApplication(sys.argv)
    main=QInputDialogDemo()
    main.show()
    sys.exit(app.exec_())

