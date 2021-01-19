import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import os

"""
1. Normal

2. NoEcho

3. Password

4. PasswordEchoOnEdit
"""
def chRec():
    absPath=__file__
    recPath=absPath[:absPath.rfind("\\")]
    os.chdir(recPath)
class QlineEditEcho(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("设置按键回显模式")
        formLayout=QFormLayout()

        echo1=QLineEdit()
        echo2=QLineEdit()
        echo3=QLineEdit()
        echo4=QLineEdit()

        formLayout.addRow("正常",echo1)
        formLayout.addRow("不回显",echo2)
        formLayout.addRow("密码模式",echo3)
        formLayout.addRow("动态密码模式",echo4)

        #placeHoldertext

        echo1.setPlaceholderText("正常")
        echo2.setPlaceholderText("不回显")
        echo3.setPlaceholderText("密码模式")
        echo4.setPlaceholderText("动态密码模式")

        echo1.setEchoMode(QLineEdit.Normal)
        echo2.setEchoMode(QLineEdit.NoEcho)
        echo3.setEchoMode(QLineEdit.Password)
        echo4.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.setLayout(formLayout)








if  __name__ == "__main__":
    chRec()
    app=QApplication(sys.argv)
    main=QlineEditEcho()
    main.show()

    sys.exit(app.exec_())