'''

'''

import sys
import os
from PyQt5.QtGui import QPainter,QFont,QColor
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
def chRec():
    absPath=__file__
    recPath=absPath[:absPath.rfind("\\")]
    os.chdir(recPath)
class QDrawTextDemo(QWidget):
    def __init__(self):
        super().__init__() 
        self.setWindowTitle("文件对话框 案例")
        self.resize(200,300)
        self.initUi()
    def initUi(self):      
        # self.bt1=QPushButton("加载图片",self)
        # self.bt1.clicked.connect(self.loadImage)
        # self.bt2=QPushButton("加载txt",self)
        # self.bt2.clicked.connect(self.loadTxt)

        self.text='三只松鼠 2333'


        lay1=QVBoxLayout()
        # lay1.addWidget(self.bt1)
        # lay1.addWidget(self.bt2)
        # lay1.addWidget(self.lb1)
        # lay1.addWidget(self.te1)


        self.setLayout(lay1)

    def paintEvent(self,event):
        painter=QPainter(self)
        painter.begin(self)

        painter.setPen(QColor(12,44,150))
        painter.setFont(QFont('SimSun',18))

        painter.drawText(event.rect(),Qt.AlignCenter,self.text)
        painter.end()

if __name__ == "__main__":
    chRec()
    app=QApplication(sys.argv)
    main=QDrawTextDemo()
    main.show()
    sys.exit(app.exec_())

