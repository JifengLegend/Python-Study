import sys
import os
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtWidgets import QHBoxLayout,QWidget,QPushButton,QToolTip
from PyQt5.QtGui import QFont


def chRec():
    absPath=__file__
    recPath=absPath[:absPath.rfind("\\")]
    os.chdir(recPath)

class ToolWindow(QMainWindow):
    def __init__(self,parent=None):
        super().__init__()
        self.setWindowTitle("提示信息")
        self.resize(400,300)

        QToolTip.setFont(QFont('微软雅黑',12))
        self.setToolTip('今天是<b>星期五</b>')

        self.bt1=QPushButton('I can Tipable')
        self.bt1.setToolTip("这是一个按钮")

        layout=QHBoxLayout()
        layout.addWidget(self.bt1)

        mainFrame=QWidget()
        mainFrame.setLayout(layout)

        self.setCentralWidget(mainFrame)


if __name__ == "__main__":
    app=QApplication(sys.argv)
    win00=ToolWindow()
    win00.show()

    sys.exit(app.exec_())
