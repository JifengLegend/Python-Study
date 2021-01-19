import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QRegExp,Qt


def chRec():
    absPath=__file__
    recPath=absPath[:absPath.rfind("\\")]
    os.chdir(recPath)
class QPinBoxDemo(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("QComboBox 示例")
        self.resize(300,100)  
        mainLay=QVBoxLayout()
        lay1=QHBoxLayout()


        self.l1=QLabel('当前值：')
        self.l1.setAlignment(Qt.AlignCenter)

        self.spin=QSpinBox()
        self.spin.valueChanged.connect(self.valueChange)
        self.spin.setSingleStep(2)


        mainLay.addWidget(self.l1)
        lay1.addWidget(self.spin)      

        mainLay.addLayout(lay1)
        self.setLayout(mainLay)

    def valueChange(self):
        self.l1.setText(f'当前值：{self.spin.value()}')
        




if  __name__ == "__main__":
    chRec()
    app=QApplication(sys.argv)
    main=QPinBoxDemo()
    main.show()

    sys.exit(app.exec_())