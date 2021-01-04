from PyQt5 import QtCore, QtGui, QtWidgets
class ClickLabel(QtWidgets.QLabel):
    clicked=QtCore.pyqtSignal()
    def __init__(self,parent=None):
        super(ClickLabel,self).__init__(parent)
    def mouseReleaseEvent(self,QmouseEvent):
        self.clicked.emit()
    def connect_customized_slot(self,func):
        self.clicked.connect(func)