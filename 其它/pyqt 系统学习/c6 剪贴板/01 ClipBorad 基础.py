import sys
import os
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
def chRec():
    absPath=__file__
    recPath=absPath[:absPath.rfind("\\")]
    os.chdir(recPath)

class QClipBoardDemo(QDialog):
    def __init__(self):
        super().__init__()

        self.bt1=QPushButton('复制文本')
        self.bt2=QPushButton('粘贴文本')

        self.bt3=QPushButton('复制Html')
        self.bt4=QPushButton('粘贴Html')

        self.bt5=QPushButton('复制图像')
        self.bt6=QPushButton('粘贴图像')

        self.bt1.clicked.connect(self.copyText)
        self.bt2.clicked.connect(self.pasteText)
        self.bt3.clicked.connect(self.copyHtml)
        self.bt4.clicked.connect(self.pasteHtml)
        self.bt5.clicked.connect(self.copyImage)
        self.bt6.clicked.connect(self.pasteImage)

        self.lb1=QLabel('初始文本')
        self.lb2=QLabel('初始图像')
        self.lb2.setPixmap(QPixmap('./卷蛋糕.png'))

        self.lb1.setAlignment(Qt.AlignCenter)
        self.lb2.setAlignment(Qt.AlignCenter)








        lay1=QGridLayout()
        lay1.addWidget(self.bt1,0,0)
        lay1.addWidget(self.bt2,0,1)
        lay1.addWidget(self.bt3,1,0)
        lay1.addWidget(self.bt4,1,1)
        lay1.addWidget(self.bt5,2,0)
        lay1.addWidget(self.bt6,2,1)
        lay1.addWidget(self.lb1,3,0,1,2)
        lay1.addWidget(self.lb2,4,0,1,2)

        self.setLayout(lay1)

    def copyText(self):
        cp=QApplication.clipboard()
        cp.setText('The World')
    def copyHtml(self):
        cp=QApplication.clipboard()
        mimeData=QMimeData()
        mimeData.setHtml('<b>Bold and font color=red>Red</font></b>')
        cp.setMimeData(mimeData)
    def copyImage(self):
        cp=QApplication.clipboard()
        cp.setPixmap(QPixmap('./卷蛋糕.png'))
    def pasteText(self):
        cp=QApplication.clipboard()  
        self.lb1.setText(cp.text())
    def pasteHtml(self):
        cp=QApplication.clipboard()
        mimeData=cp.mimeData()
        if mimeData.hasHtml():
            self.lb1.setText(mimeData.html())
    def pasteImage(self):
        cp=QApplication.clipboard()
        self.lb2.setPixmap(cp.pixmap())

    



if __name__ == "__main__":
    chRec()
    app=QApplication(sys.argv)
    main=QClipBoardDemo()
    main.show()
    sys.exit(app.exec_())
