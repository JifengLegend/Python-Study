import sys,math
import os
from PyQt5.QtGui import QPainter,QFont,QColor
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
def chRec():
    absPath=__file__
    recPath=absPath[:absPath.rfind("\\")]
    os.chdir(recPath)

class DrawLine(QWidget):
    def __init__(self):
        super(DrawLine, self).__init__()
        self.resize(200,200)
        self.setWindowTitle("Draw")
    def paintEvent(self, event):
        painter=QPainter()
        painter.begin(self)
        painter.setPen(Qt.blue)
        size=self.size()

        for i in range(1000):
           x=100*(-1+2.0*i/1000)+size.width()/2.0 
           y=-50* math.sin((x-size.width()/2.0)*math.pi/50)+size.height()/2.0
           painter.drawPoint(x,y)

if __name__ == "__main__":
    chRec()
    app=QApplication(sys.argv)
    main=DrawLine()
    main.show()
    sys.exit(app.exec_())