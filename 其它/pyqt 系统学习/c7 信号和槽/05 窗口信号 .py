import sys
import os
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
def chRec():
    absPath=__file__
    recPath=absPath[:absPath.rfind("\\")]
    os.chdir(recPath)

class WinSignal(QWidget):
    s1=pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle('窗口信号')
        self.resize(300,400)

        self.bt1=QPushButton('关闭',self)
        self.bt1.clicked.connect(self.bt1_clicked)
        

        self.s1.connect(self.bt_closed)

    def bt_closed(self):
        self.close()
    def bt1_clicked(self):
       self.s1.emit() 


if __name__ == "__main__":
    app=QApplication(sys.argv)
    main=WinSignal()
    main.show()
    sys.exit(app.exec_())

