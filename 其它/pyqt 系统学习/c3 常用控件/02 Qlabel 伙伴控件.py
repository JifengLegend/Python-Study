import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import os
def chRec():
    absPath=__file__
    recPath=absPath[:absPath.rfind("\\")]
    os.chdir(recPath)
class QlabelBuddy(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)

        self.setWindowTitle("设置伙伴控件")
        # self.setGeometry(300,300,350,250)

        nameLabel=QLabel('&Name',self)
        nameLineEdit=QLineEdit(self)

        nameLabel.setBuddy(nameLineEdit)

        passLabel=QLabel('&pass',self)
        passLineEdit=QLineEdit(self)

        passLabel.setBuddy(passLineEdit)

        bt1=QPushButton("&OK")
        bt2=QPushButton("&Cancel")

        mainLayout=QGridLayout(self)
        mainLayout.addWidget(nameLabel,0,0)
        mainLayout.addWidget(nameLineEdit,0,1,1,2)

        mainLayout.addWidget(passLabel,1,0)
        mainLayout.addWidget(passLineEdit,1,1,1,2)

        mainLayout.addWidget(bt1,2,1)
        mainLayout.addWidget(bt2,2,2)

        self.setLayout(mainLayout)





if  __name__ == "__main__":
    chRec()
    app=QApplication(sys.argv)
    # app.setWindowIcon(QIcon("./心2.ico"))

    main=QlabelBuddy()
    main.show()

    sys.exit(app.exec_())