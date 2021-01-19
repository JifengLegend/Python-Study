import sys
import os
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
def chRec():
    absPath=__file__
    recPath=absPath[:absPath.rfind("\\")]
    os.chdir(recPath)

class NNSiganl(QObject):
    s1=pyqtSignal()
    s2=pyqtSignal(int)
    
    def __init__(self):
        super().__init__()

        self.s1.connect(self.call1)
        self.s1.connect(self.call1p)
        self.s2.connect(self.call1)

        self.s1.emit()
        self.s2.emit(10)
    def call1(self):
        print('call 1')
    def call1p(self):
        print('call 1p')
    def call2(self,val):
        print('call 2',val)
if __name__ == "__main__":
    NNSiganl()