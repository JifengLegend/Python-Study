import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import os
def chRec():
    absPath=__file__
    recPath=absPath[:absPath.rfind("\\")]
    os.chdir(recPath)
class ToolBarDemo(QMainWindow):
    def __init__(self):
        super(ToolBarDemo, self).__init__()
        self.initUi()
    def initUi(self):
        self.setWindowTitle('ToolBar')
        self.resize(200,300)
        tb1=self.addToolBar('file')

        new=QAction(QIcon('./images/new.png'),'new',self)
        tb1.addAction(new)

        openAction=QAction(QIcon('./images/open.png'),'openAction',self)
        tb1.addAction(openAction)
        tb1.actionTriggered.connect(self.open)

        saveAction=QAction(QIcon('./images/save.png'),'saveAction',self)
        tb1.addAction(saveAction)

        tb1.setToolButtonStyle(Qt.ToolButtonFollowStyle)
        '''
        Qt.ToolButtonTextOnly
        Qt.ToolButtonIconOnly
        Qt.ToolButtonTextUnderIcon
        Qt.ToolButtonTextBesideIcon
        Qt.ToolButtonFollowStyle
        '''
    def open(self,a):
        print('111',a.text())




if __name__ == '__main__':
    chRec()
    app = QApplication(sys.argv)
    main = ToolBarDemo()
    main.show()
    sys.exit(app.exec_())