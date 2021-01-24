import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MenuDemo(QMainWindow):
    def __init__(self):
        super(MenuDemo, self).__init__()
        bar=self.menuBar()

        file=bar.addMenu('文件')

        file.addAction('新建')

        save=QAction("保存",self)
        save.setShortcut('Ctrl+S')
        file.addAction(save)

        edit=bar.addMenu('Edit')
        edit.addAction('copy')
        edit.addAction("paste")
        # edit.addAction('quit')
        quitAction=QAction("退出",self)
        bar.addAction(quitAction)

        save.triggered.connect(self.process)
        quitAction.triggered.connect(self.quit)
    def process(self,a):
        print(self.sender().text())
    def quit(self,e):
        print('QUIT')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MenuDemo()
    main.show()
    sys.exit(app.exec_())
