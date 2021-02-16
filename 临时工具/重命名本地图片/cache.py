import sys
from window import Ui_ReNameForm

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QStatusBar
import threading
import time,os


def chRec():
    absPath=__file__
    recPath=absPath[:absPath.rfind("\\")]
    os.chdir(recPath)
class MyTherad(QtCore.QThread):
    s1=QtCore.pyqtSignal(bool)
    def run(self):
        while 1:
            flist=os.listdir('.')
            if 'download.gif' in flist:
                self.s1.emit(1)       
            else:
                self.s1.emit(0)    
            time.sleep(1)
class ReWindow(QtWidgets.QWidget,Ui_ReNameForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()
    def initUi(self):
        self.t1=MyTherad()
        self.t1.start()
        self.t1.s1.connect(self.loadPic)
        self.bt1.clicked.connect(self.rename)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    def loadPic(self,flag):
        if flag==1:
            self.gif=QtGui.QMovie('download.gif')
            self.lb1.setMovie(self.gif)
            self.gif.start()
        else:
            self.lb2.setText('暂无 download.gif 文件')
            pass
    def rename(self):
        fraw=self.le1.text()
        ftype=self.cb1.currentText()
        fname=fraw+ftype
        self.gif=QtGui.QMovie(fname)
        self.lb1.setMovie(self.gif)
        
            os.rename('download.gif',fname)
        

        self.gif=QtGui.QMovie('11.gif')
        self.lb1.setMovie(self.gif)
        self.gif.start()
        self.lb2.setText('重命名成功')
if __name__ == "__main__":

    chRec()
    app=QApplication(sys.argv)
    win=ReWindow()
    win.show()

    sys.exit(app.exec_())
    