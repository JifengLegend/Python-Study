import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QRegExpValidator
from PyQt5.QtCore import QRegExp,Qt


def chRec():
    absPath=__file__
    recPath=absPath[:absPath.rfind("\\")]
    os.chdir(recPath)
class QLineEditCon(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("QlineEdit 检验器")
        formLayout=QFormLayout()
        
        edit1=QLineEdit()
        edit2=QLineEdit()
        edit3=QLineEdit()
        edit4=QLineEdit()
        edit5=QLineEdit()
        edit6=QLineEdit('Hello Python')

        formLayout.addRow('整数校验',edit1)
        formLayout.addRow('浮点',edit2)
        formLayout.addRow('掩码',edit3)
        formLayout.addRow("文本变化",edit4)
        formLayout.addRow("回显",edit5)
        formLayout.addRow("只读",edit6)

        self.setLayout(formLayout)

        # 整数校验器
        edit1.setValidator(QIntValidator())
        edit1.setMaxLength(4)
        edit1.setAlignment(Qt.AlignRight)

        # 浮点校验器
        edit2.setValidator(QDoubleValidator(0.99,99.99,2))

        # 掩码
        edit3.setInputMask('99_9999_99999;\\')

        # 
        edit4.textChanged.connect(self.texChanged)

        # 
        edit5.setEchoMode(QLineEdit.Password)
        edit5.editingFinished.connect(self.enterPress)
        # 
        edit6.setReadOnly(True)
    def texChanged(self,text):
        print('输入的内容'+text)

    def enterPress(self):
        print('输入的内容')





if  __name__ == "__main__":
    chRec()
    app=QApplication(sys.argv)
    main=QLineEditCon()
    main.show()

    sys.exit(app.exec_())