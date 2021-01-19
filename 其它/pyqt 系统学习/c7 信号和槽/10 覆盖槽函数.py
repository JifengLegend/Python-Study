import sys
import os
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from functools import partial
def chRec():
    absPath=__file__
    recPath=absPath[:absPath.rfind("\\")]
    os.chdir(recPath)

class OverrideSignal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('覆盖 Demo')
        self.resize(200,200)        
        self.initUI()
        
    def initUI(self):
        pass
    def keyPressEvent(self,e):
        if e.key()==Qt.Key_Escape:
            self.close()
        if e.key()==Qt.Key_1:
            self.resize(300,200)

if __name__ == "__main__":
    app=QApplication(sys.argv)
    main=OverrideSignal()
    main.show()
    sys.exit(app.exec_())

