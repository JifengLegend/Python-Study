'''
让控件支持拖拽
setDragEnabled(1)
setAcceptDrops(1)

dragEnterEvent 
dropEvent
'''

import sys
import os
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
def chRec():
    absPath=__file__
    recPath=absPath[:absPath.rfind("\\")]
    os.chdir(recPath)

class MyCombo(QComboBox):
    def __init__(self):
        super(MyCombo, self).__init__()
        self.setAcceptDrops(True)
    def dragEnterEvent(self,e):
        print(e)
        if e.mimeData().hasText():
            e.accept()
        else:
            e.ignore()
    def dropEvent(self,e):
        self.addItem(e.mimeData().text())
    
class DrapDemo(QWidget):
    def __init__(self):
        super().__init__()
        formLayout=QFormLayout()
        formLayout.addRow(QLabel('请将左边文本拖到右边'))
        le1=QLineEdit()
        le1.setDragEnabled(1)

        combo=MyCombo()
        formLayout.addRow(le1,combo)

        self.setLayout(formLayout)

        self.setWindowTitle("拖拽")
        

if __name__ == "__main__":
    chRec()
    app=QApplication(sys.argv)
    main=DrapDemo()
    main.show()
    sys.exit(app.exec_())
