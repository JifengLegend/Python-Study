from subWindow import Ui_Warehouse
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
class SubWinDemo(QtWidgets.QWidget,Ui_Warehouse):
    
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi(self)

if __name__ == "__main__":
    # app=QtWidgets.QApplication(sys.argv)
    # win=QtWidgets.QWidget()
    # ui=subWindow.Ui_Warehouse()
    # ui.setupUi(win)
    # win.show()
    # sys.exit(app.exec_())
    app=QtWidgets.QApplication(sys.argv)
    win=SubWinDemo()
    win.show()
    sys.exit(app.exec_())