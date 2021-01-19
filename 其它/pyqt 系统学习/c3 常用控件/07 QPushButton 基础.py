import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QRegExp,Qt


def chRec():
    absPath=__file__
    recPath=absPath[:absPath.rfind("\\")]
    os.chdir(recPath)
class QPushBtDemo(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("QPushButton 示例")
        self.resize(300,300)

        mainLay=QVBoxLayout()
        self.bt1=QPushButton("按钮1")
        self.bt1.setCheckable(True)
        self.bt1.toggle()
        self.bt1.clicked.connect(lambda : self.whichButton(self.bt1))

        self.bt2=QPushButton("按钮2",icon=QIcon(QPixmap("./卷蛋糕.png")))
        self.bt2.clicked.connect(lambda : self.whichButton(self.bt2))

        self.bt3=QPushButton("不可用的按钮")
        self.bt3.setEnabled(False)
        self.bt3.clicked.connect(lambda : self.whichButton(self.bt3))

        self.bt4=QPushButton("&M 我的按钮")
        self.bt4.setDefault(True)
        self.bt4.clicked.connect(lambda : self.whichButton(self.bt4))



        mainLay.addWidget(self.bt1)
        mainLay.addWidget(self.bt2)
        mainLay.addWidget(self.bt3)
        mainLay.addWidget(self.bt4)
        self.setLayout(mainLay)
    def whichButton(self,btn):
        print("被单击的按钮是 "+btn.text())


if  __name__ == "__main__":
    chRec()
    app=QApplication(sys.argv)
    main=QPushBtDemo()
    main.show()

    sys.exit(app.exec_())