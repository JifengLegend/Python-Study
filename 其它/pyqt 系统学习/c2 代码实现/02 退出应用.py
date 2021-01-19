import sys
import os
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtWidgets import QHBoxLayout,QWidget,QPushButton


def chRec():
    absPath=__file__
    recPath=absPath[:absPath.rfind("\\")]
    os.chdir(recPath)

class QuitApplication(QMainWindow):
    def __init__(self,parent=None):
        super().__init__()
        self.setWindowTitle("测试-退出应用")
        self.resize(400,300)

        self.bt1=QPushButton("退出")
        self.bt1.clicked.connect(self.onClick_Button)

        layout=QHBoxLayout()
        layout.addWidget(self.bt1)

        mainFrame=QWidget()
        mainFrame.setLayout(layout)

        self.setCentralWidget(mainFrame)

    def onClick_Button(self):
        sender=self.sender()
        print(sender.text()+'按钮被按下')
        appNow=QApplication.instance()
        appNow.quit()
        


if __name__ == "__main__":
    app=QApplication(sys.argv)
    win00=QuitApplication()
    win00.show()

    sys.exit(app.exec_())
