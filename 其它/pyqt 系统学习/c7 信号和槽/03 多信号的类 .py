import sys
import os
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
def chRec():
    absPath=__file__
    recPath=absPath[:absPath.rfind("\\")]
    os.chdir(recPath)

class MulSignal(QObject):
    signal1=pyqtSignal()
    signal2=pyqtSignal(int)
    signal3=pyqtSignal(int,str)
    signal4=pyqtSignal(list)
    signal5=pyqtSignal(dict)
    signal6=pyqtSignal([int,str],[str])

    def __init__(self):
        super().__init__()
        self.signal1.connect(self.call1)
        self.signal2.connect(self.call2)
        self.signal3.connect(self.call3)
        self.signal4.connect(self.call4)
        self.signal5.connect(self.call5)
        self.signal6[int,str].connect(self.call6)
        self.signal6[str].connect(self.call6p)
        self.signal1.emit()
        self.signal2.emit(10)
        self.signal3.emit(10,'aaa')
        self.signal4.emit([1,2,5,7,9,12])
        self.signal5.emit({'name':"Dio","stand":"The World"})
        self.signal6[str].emit('bbb')
        self.signal6[int,str].emit(20,'bbb')
    def call1(self):
        print('signal 1 emit')
    def call2(self,val):
        print('signal 2 emit',val)
    def call3(self,val,strs):
        print('signal 3 emit',val,strs)
    def call4(self,val):
        print('siganl 4 emit',val)
    def call5(self,val):
        print('siganl 5 emit',val)
    def call6(self,val,strs):
        print('siganl 6 emit 01',val,strs)
    def call6p(self,strs):
        print('siganl 6 emit 02',strs)
if __name__ == "__main__":
    chRec()
    MulSignal()
    

    