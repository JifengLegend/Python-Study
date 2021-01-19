import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QRegExp,Qt


def chRec():
    absPath=__file__
    recPath=absPath[:absPath.rfind("\\")]
    os.chdir(recPath)
class QComboBoxDemo(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("QComboBox 示例")
        self.resize(300,200)
        mainLay=QVBoxLayout()
        lay1=QHBoxLayout()

        self.label=QLabel("请选择一个编程语言")

        self.combo=QComboBox()
        self.combo.addItem('Python')
        self.combo.addItems(['Java','C#',"F#","Ruby"])
        self.combo.currentIndexChanged.connect(self.comboNow)



        lay1.addWidget(self.label)
        lay1.addWidget(self.combo)
        

        mainLay.addLayout(lay1)
        self.setLayout(mainLay)
    # comboBox 也会把索引传进来
    def comboNow(self,index):
        self.label.setText(self.combo.currentText())
        self.label.adjustSize()
        print(f'当前选中了{self.combo.itemText(index)}，序号为{index}')

        




if  __name__ == "__main__":
    chRec()
    app=QApplication(sys.argv)
    main=QComboBoxDemo()
    main.show()

    sys.exit(app.exec_())