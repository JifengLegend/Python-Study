import sys
import os
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
class MainWindowDemo(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('主窗口')
        self.resize(400,400)
        self.bt1=QPushButton('打开子窗口1',self)
        self.bt2=QPushButton('打开子窗口2',self)
        self.bt1.clicked.connect(self.bt1_clicked)
        self.bt2.clicked.connect(self.bt2_clicked)
        self.le1=QLineEdit(self)

        lay1=QVBoxLayout()
        lay1.addWidget(self.le1)
        lay1.addWidget(self.bt1)
        lay1.addWidget(self.bt2)
        
        mainFrame=QWidget()
        mainFrame.setLayout(lay1)
        self.setCentralWidget(mainFrame)

    def bt1_clicked(self):
        self.sub1=Sub1()
        self.sub1.s1.connect(self.update1)
        self.sub1.show()
    def update1(self,strs):
        self.le1.setText(strs)
    def bt2_clicked(self):
        pass
class Sub1(QWidget):
    s1=pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.le1=QLineEdit(self)
        self.bts=QDialogButtonBox(QDialogButtonBox.Ok|QDialogButtonBox.Cancel,Qt.Horizontal,self)
        self.bts.accepted.connect(lambda : self.s1_emit(self.le1.text()))
        self.bts.rejected.connect(self.close)
        
        lay1=QVBoxLayout()
        lay1.addWidget(self.le1)
        lay1.addWidget(self.bts)
        self.setLayout(lay1)

    def s1_emit(self,strs):
        print(strs)
        self.s1.emit(strs)


if __name__ == "__main__":
    app=QApplication(sys.argv)
    main=MainWindowDemo()
    main.show()
    sys.exit(app.exec_())
