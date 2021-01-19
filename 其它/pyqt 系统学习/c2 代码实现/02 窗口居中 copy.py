import sys
import os
from PyQt5.QtWidgets import QMainWindow,QApplication,QDesktopWidget


def chRec():
    absPath=__file__
    recPath=absPath[:absPath.rfind("\\")]
    os.chdir(recPath)

class CenterForm(QMainWindow):
    def __init__(self,parent=None):
        super().__init__()
        self.setWindowTitle("绝对居中窗口")
        self.resize(400,300)
        self.move(100,100)
        self.center()
    def center(self):
        # 获得屏幕几何信息
        screen=QDesktopWidget().screenGeometry()
        # 获得窗体几何信息
        size=self.geometry()
        newLeft=(screen.width()-size.width())/2
        newTop=(screen.height()-size.height())/2
        self.move(newLeft,newTop)


if __name__ == "__main__":
    app=QApplication(sys.argv)
    win00=CenterForm()
    win00.show()

    sys.exit(app.exec_())
