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
class QFontDialogDemo(QWidget):
    def __init__(self):
        super().__init__() 
        self.setWindowTitle("输入对话框 案例")
        self.resize(200,200)
        self.initUi()
    def initUi(self):      
        self.bt1=QPushButton("选择字体",self)
        self.bt1.clicked.connect(self.getFont)


        self.lb1=QLabel('Font Show')
        self.lb1.setAlignment(Qt.AlignCenter)


        lay1=QVBoxLayout()
        lay1.addWidget(self.bt1)
        lay1.addWidget(self.lb1)


        self.setLayout(lay1)

    def getFont(self):
        font,ok =QFontDialog.getFont()
        if font and ok :
            self.lb1.setFont(font)

if __name__ == "__main__":
    chRec()
    app=QApplication(sys.argv)
    main=QFontDialogDemo()
    main.show()
    sys.exit(app.exec_())

