import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QRegExpValidator
from PyQt5.QtCore import QRegExp,Qt


def chRec():
    absPath=__file__
    recPath=absPath[:absPath.rfind("\\")]
    os.chdir(recPath)
class QTextEditDemo(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("QTextEdit 示例")
        self.resize(500,400)

        self.text1=QTextEdit()
        self.bt1=QPushButton("显示文本")
        self.bt2=QPushButton("显示HTML")
        self.bt3=QPushButton("获取文本")
        self.bt4=QPushButton("获取HTML")

        layout=QVBoxLayout()
        layout.addWidget(self.text1)
        layout.addWidget(self.bt1)
        layout.addWidget(self.bt2)
        layout.addWidget(self.bt3)
        layout.addWidget(self.bt4)

        self.bt1.clicked.connect(self.onClink_bt1)
        self.bt2.clicked.connect(self.onClick_bt2)
        self.bt3.clicked.connect(self.onClink_bt3)
        self.bt4.clicked.connect(self.onClick_bt4)
        self.setLayout(layout)

    def onClink_bt1(self):
        self.text1.setPlainText("Hello World")
    def onClick_bt2(self):
        self.text1.setHtml('<font color=blue>Hello World<font>')
    def onClink_bt3(self):
        print(self.text1.toPlainText())
    def onClick_bt4(self):
        print(self.text1.toHtml())


if  __name__ == "__main__":
    chRec()
    app=QApplication(sys.argv)
    main=QTextEditDemo()
    main.show()

    sys.exit(app.exec_())