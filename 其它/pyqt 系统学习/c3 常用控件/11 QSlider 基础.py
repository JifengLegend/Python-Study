import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QRegExp,Qt


def chRec():
    absPath=__file__
    recPath=absPath[:absPath.rfind("\\")]
    os.chdir(recPath)
class QSliderDemo(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("QComboBox 示例")
        self.resize(300,200)
        mainLay=QVBoxLayout()
        lay1=QHBoxLayout()

        self.label=QLabel("你好，Python")
        self.label.setAlignment(Qt.AlignCenter)

        self.s1=QSlider(Qt.Horizontal)
        self.s1.setMinimum(12)
        self.s1.setMaximum(48)
        self.s1.setSingleStep(3)
        self.s1.setValue(18)
        self.s1.setTickPosition(QSlider.TicksBelow)
        self.s1.setTickInterval(5)

        self.s1.valueChanged.connect(self.valueChange)
        
        self.s2=QSlider(Qt.Vertical)
        self.s2.setMinimum(5)
        self.s2.setMaximum(60)
        self.s2.setSingleStep(3)
        self.s2.setValue(18)
        self.s2.setTickPosition(QSlider.TicksBelow)
        self.s2.setTickInterval(5)

        self.s2.valueChanged.connect(self.valueChange)


 
        
        mainLay.addWidget(self.label)
        mainLay.addWidget(self.s2)
        lay1.addWidget(self.s1)
        mainLay.addLayout(lay1)
        
        self.setLayout(mainLay)

    def valueChange(self):
        size=self.sender().value()
        print(f'当前值为：{size}')
        self.label.setFont(QFont('Arial',size))
        




if  __name__ == "__main__":
    chRec()
    app=QApplication(sys.argv)
    main=QSliderDemo()
    main.show()

    sys.exit(app.exec_())