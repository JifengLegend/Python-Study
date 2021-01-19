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
class QColorDialogDemo(QWidget):
    def __init__(self):
        super().__init__() 
        self.setWindowTitle("输入对话框 案例")
        self.resize(200,200)
        self.initUi()
    def initUi(self):      
        self.bt1=QPushButton("选择前景颜色",self)
        self.bt1.clicked.connect(self.getColor)
        self.bt2=QPushButton("选择背景颜色",self)
        self.bt2.clicked.connect(self.getBgColor)


        self.lb1=QLabel('Color Show')
        self.lb1.setAlignment(Qt.AlignCenter)


        lay1=QVBoxLayout()
        lay1.addWidget(self.bt1)
        lay1.addWidget(self.bt2)
        lay1.addWidget(self.lb1)


        self.setLayout(lay1)

    def getColor(self):
        color=QColorDialog.getColor()
        if color:
            fore=QPalette()
            fore.setColor(QPalette.WindowText,color)
            self.lb1.setPalette(fore)
    def getBgColor(self):
        color=QColorDialog.getColor()
        if color:
            bg=QPalette()
            bg.setColor(QPalette.Window,color)
            self.lb1.setAutoFillBackground(1)

            self.lb1.setPalette(bg)

if __name__ == "__main__":
    chRec()
    app=QApplication(sys.argv)
    main=QColorDialogDemo()
    main.show()
    sys.exit(app.exec_())

