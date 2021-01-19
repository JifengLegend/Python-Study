import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QRegExp,Qt


def chRec():
    absPath=__file__
    recPath=absPath[:absPath.rfind("\\")]
    os.chdir(recPath)
class QCheckBoxDemo(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("QCheckBox 示例")
        self.resize(300,300)
        mainLay=QVBoxLayout()
        lay1=QHBoxLayout()

        self.cb1=QCheckBox("1")
        self.cb1.setChecked(1)
        self.cb2=QCheckBox("2")
        self.cb3=QCheckBox("3")

        # 半选中的设置方法
        self.cb3.setTristate(1)
        self.cb3.setCheckState(Qt.PartiallyChecked)

        self.cb1.stateChanged.connect(lambda:self.checkBoxState(self.cb1))
        # self.cb1.stateChanged.connect(lambda:self.checkBoxState(self.cb2))
        # self.cb1.stateChanged.connect(lambda:self.checkBoxState(self.cb3))






        lay1.addWidget(self.cb1)
        lay1.addWidget(self.cb2)
        lay1.addWidget(self.cb3)
        mainLay.addLayout(lay1)
        self.setLayout(mainLay)

    def checkBoxState(self,cb):
        cache1=f'{self.cb1.text()}isChecked={self.cb1.isChecked()},checkState={self.cb1.checkState()}\n'
        cache2=f'{self.cb2.text()}isChecked={self.cb2.isChecked()},checkState={self.cb2.checkState()}\n'
        cache3=f'{self.cb3.text()}isChecked={self.cb3.isChecked()},checkState={self.cb3.checkState()}\n'

        print(cache1+cache2+cache3)




if  __name__ == "__main__":
    chRec()
    app=QApplication(sys.argv)
    main=QCheckBoxDemo()
    main.show()

    sys.exit(app.exec_())