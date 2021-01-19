import sys
import os
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MyLabel(QLabel):
    def __init__(self,text=None,parent=None):
        super().__init__(text,parent)
    # 
    def mousePressEvent(self,e):
        if e.buttons()==Qt.LeftButton:
            print('单击左键')
        elif e.buttons()==Qt.RightButton:
            print('单击右键')
        elif e.buttons()==Qt.MidButton:
            print('单击中键')
        elif e.buttons()==Qt.LeftButton|Qt.RightButton:
            print('单击左右键')
    def wheelEvent(self,e):
        angle=e.angleDelta()/8
        # angleX=angle.x()
        angleY=angle.y()
        if angleY>0:
            print('up')
        else:
            print('down')

    def mouseDoubleClickEvent(self,e):
        print(e.buttons()==Qt.RightButton)
        print('双击')
    def mouseMoveEvent(self,e):
        print('移动')

class MainWindowDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.lb1=MyLabel('Island',self)

if __name__ == "__main__":
    app=QApplication(sys.argv)
    main=MainWindowDemo()
    main.show()
    sys.exit(app.exec_())
