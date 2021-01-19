import sys
import os
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
def chRec():
    absPath=__file__
    recPath=absPath[:absPath.rfind("\\")]
    os.chdir(recPath)

class MyTypeSignal(QObject):
    sendMsg=pyqtSignal(object)
    def run(self):
        self.sendMsg.emit('Hello Pyqt5')

    altMsg=pyqtSignal(str,int,int)
    def start(self):
        self.altMsg.emit('111',1,2)

class MySlot(QObject):
    def get(self,msg):
        print(f'信息{msg}')
    def printMsg(self,strs,a,b):
        print(strs)
        print(a+b)




if __name__ == "__main__":
    chRec()
    send=MyTypeSignal()
    slot=MySlot()

    send.sendMsg.connect(slot.get)
    send.run()

    send.altMsg.connect(slot.printMsg)
    send.start()

    