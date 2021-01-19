import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QRegExp,Qt


def chRec():
    absPath=__file__
    recPath=absPath[:absPath.rfind("\\")]
    os.chdir(recPath)
class QRadioButtonDemo(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("QRadioButton 示例")
        self.resize(300,300)

        mainLay=QVBoxLayout()
        lay1=QHBoxLayout()

        self.rb1=QRadioButton("1")
        self.rb2=QRadioButton("2")
        self.rb1.setChecked(True)

        self.rb1.toggled.connect(self.buttonState)
        # self.rb2.toggled.connect(self.buttonState)

        lay1.addWidget(self.rb1)
        lay1.addWidget(self.rb2)
        mainLay.addLayout(lay1)
        self.setLayout(mainLay)
    def buttonState(self):
        radioButton=self.sender()
        if radioButton.text()=="1":
            if radioButton.isChecked()==1:
                print(f'<{radioButton.text()}被选中>')
            else:
                print(f'<{radioButton.text()}未被选中>')
 



if  __name__ == "__main__":
    chRec()
    app=QApplication(sys.argv)
    main=QRadioButtonDemo()
    main.show()

    sys.exit(app.exec_())