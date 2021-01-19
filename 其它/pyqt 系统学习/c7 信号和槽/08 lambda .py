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

class LambdaSignalDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('lambda Demo')
        self.resize(200,200)        
        self.initUI()
        
    def initUI(self):
        self.bt1=QPushButton('1')
        self.bt1.clicked.connect(lambda : self.bt1_clicked(10,20))
        self.bt2=QPushButton('2')
        # self.bt2.clicked.connect(self.bt2_clicked)

        
        
        layout=QHBoxLayout()
        layout.addWidget(self.bt1)
        layout.addWidget(self.bt2)

        mainFrame=QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

    def bt1_clicked(self,m,n):
        print(m+n)
        QMessageBox.information(self,'结果',str(n+m))
    def bt2_clicked(self):
        pass


if __name__ == "__main__":
    app=QApplication(sys.argv)
    main=LambdaSignalDemo()
    main.show()
    sys.exit(app.exec_())

