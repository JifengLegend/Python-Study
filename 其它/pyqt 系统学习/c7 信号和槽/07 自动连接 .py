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

class AutoSignal(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('多线程ui')
        self.resize(200,200)        
        self.initUI()
        self.setLayout(self.layout)
    def initUI(self):
        self.bt1=QPushButton('OK',self)
        self.bt2=QPushButton('Cancel',self)
        
        self.layout=QVBoxLayout()
        self.layout.addWidget(self.bt1)
        self.layout.addWidget(self.bt2)

        self.bt1.setObjectName('OkBtn')
        self.bt2.setObjectName('CancelBtn')

        QMetaObject.connectSlotsByName(self)
    @pyqtSlot()
    def on_OkBtn_clicked(self):
        print('OK')
    @pyqtSlot()
    def on_CancelBtn_clicked(self):
        print('Cancel')

if __name__ == "__main__":
    app=QApplication(sys.argv)
    main=AutoSignal()
    main.show()
    sys.exit(app.exec_())

