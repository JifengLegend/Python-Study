import sys,math
import os
from PyQt5.QtGui import QPainter,QFont,QColor,QPen
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
def chRec():
    absPath=__file__
    recPath=absPath[:absPath.rfind("\\")]
    os.chdir(recPath)

class DrawLine(QWidget):
    def __init__(self):
        super(DrawLine, self).__init__()
        self.resize(400,400)
        self.setWindowTitle("Draw")
    def paintEvent(self, event):
        painter=QPainter()
        painter.begin(self)
        
        size=self.size()

        pen=QPen(Qt.red,2,Qt.SolidLine)
        painter.setPen(pen)
        painter.drawLine(20,40,250,40)

        pen.setStyle(Qt.DashLine)
        painter.setPen(pen)
        painter.drawLine(20,80,250,80)

        pen.setStyle(Qt.DashDotDotLine)
        painter.setPen(pen)
        painter.drawLine(20,120,250,120)

        pen.setStyle(Qt.DotLine)
        painter.setPen(pen)
        painter.drawLine(20,160,250,160)

        pen.setStyle(Qt.CustomDashLine)
        pen.setDashPattern([1,2,3,15])
        painter.setPen(pen)
        painter.drawLine(20,200,250,200)

        painter.end()

if __name__ == "__main__":
    chRec()
    app=QApplication(sys.argv)
    main=DrawLine()
    main.show()
    sys.exit(app.exec_())