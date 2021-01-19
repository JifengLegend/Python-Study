'''
对话框 QInputDialog

1. getItem
2. getText
3. getInt
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
        self.bt1=QPushButton("加载图片",self)
        self.bt1.clicked.connect(self.loadImage)
        self.bt2=QPushButton("加载txt",self)
        self.bt2.clicked.connect(self.loadTxt)

        self.lb1=QLabel('□',self)
        self.lb1.setMaximumSize(200,200)

        self.te1=QTextEdit(self)
        self.te1.setAlignment(Qt.AlignCenter)


        lay1=QVBoxLayout()
        lay1.addWidget(self.bt1)
        lay1.addWidget(self.bt2)
        lay1.addWidget(self.lb1)
        lay1.addWidget(self.te1)


        self.setLayout(lay1)

    def loadImage(self):
        fName,_=QFileDialog.getOpenFileName(self,'打开文件','.','图像文件(*.jpg *.png)')
        self.lb1.setPixmap(QPixmap(fName))
    def loadTxt(self):
        dg1=QFileDialog()
        dg1.setFilter(QDir.Files)

        if dg1.exec():
            fileName=dg1.selectedFiles()
            with open(fileName[0],'r',encoding='utf-8')as f:
                data=f.read()
                self.te1.setText(data)

if __name__ == "__main__":
    chRec()
    app=QApplication(sys.argv)
    main=QDrawTextDemo()
    main.show()
    sys.exit(app.exec_())

