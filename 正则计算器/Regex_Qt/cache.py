from PyQt5 import QtCore, QtGui, QtWidgets
# class ClickLabel1(QtWidgets.QLabel):
#     clicked=QtCore.pyqtSignal()

#     def __init__(self,parent=None):
#         super(ClickLabel,self).__init__(parent)
#     def mouseReleaseEvent(self,QmouseEvent):
#         self.clicked.emit()
#     def connect_customized_slot(self,func):
#         self.clicked.connect(func)

class ClickLabel(QtWidgets.QLabel):
    clicked=QtCore.pyqtSignal()
    doubleClicked=QtCore.pyqtSignal()
    hover=QtCore.pyqtSignal()
    leave=QtCore.pyqtSignal()
    def __init__(self,text=None,parent=None):
        super().__init__(parent,text)
    def mouseReleaseEvent(self,e):
        self.clicked.emit()
    def mouseDoubleClickEvent(self,e):
        self.doubleClicked.emit()
    def enterEvent(self,e):
        self.hover.emit()
    def leaveEvent(self,e):
        self.leave.emit()

