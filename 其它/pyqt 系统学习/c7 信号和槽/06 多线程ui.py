import sys
import os
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import time
def chRec():
    absPath=__file__
    recPath=absPath[:absPath.rfind("\\")]
    os.chdir(recPath)

class Therad2(QThread):
    s1=pyqtSignal(str)
    def run(self):
        while 1:
            data=QDateTime.currentDateTime()
            current=data.toString('yyyy-MM-dd hh:mm:ss')
            self.s1.emit(current)
            time.sleep(1)

class WindowMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('多线程ui')
        self.resize(200,200)
        self.le1=QLineEdit(self)
        self.le1.resize(200,100)
        self.initUI()
    def initUI(self):
        self.thread2=Therad2()
        self.thread2.s1.connect(self.handleDisplay)
        self.thread2.start()

    def handleDisplay(self,data):
        self.le1.setText(data)


if __name__ == "__main__":
    app=QApplication(sys.argv)
    main=WindowMain()
    main.show()
    sys.exit(app.exec_())

