import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QRegExpValidator
from PyQt5.QtCore import QRegExp
import os


def chRec():
    absPath=__file__
    recPath=absPath[:absPath.rfind("\\")]
    os.chdir(recPath)
class QLineEditCheck(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("QlineEdit 检验器")
        formLayout=QFormLayout()
        
        edit1=QLineEdit()
        edit2=QLineEdit()
        edit3=QLineEdit()

        formLayout.addRow('整数',edit1)
        formLayout.addRow('浮点',edit2)
        formLayout.addRow('正则',edit3)

        # 整数校验器
        intValid=QIntValidator(self)
        intValid.setRange(1,99)
        # 浮点校验器
        doubleValid=QDoubleValidator(self)
        doubleValid.setRange(-360,360)
        doubleValid.setNotation(QDoubleValidator.StandardNotation)
        doubleValid.setDecimals(2)
        # 正则校验器
        reg=QRegExp('[A-z0-9]+')
        regValid=QRegExpValidator(self)
        regValid.setRegExp(reg)

        edit1.setValidator(intValid)
        edit2.setValidator(doubleValid)
        edit3.setValidator(regValid)

        self.setLayout(formLayout)




if  __name__ == "__main__":
    chRec()
    app=QApplication(sys.argv)
    main=QLineEditCheck()
    main.show()

    sys.exit(app.exec_())