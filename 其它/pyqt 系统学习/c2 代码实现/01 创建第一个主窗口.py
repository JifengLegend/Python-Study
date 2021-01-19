import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QIcon
import os
def chRec():
    absPath=__file__
    recPath=absPath[:absPath.rfind("\\")]
    os.chdir(recPath)
class FirstMainWindow(QMainWindow):
    def __init__(self,parent=None):
        super(FirstMainWindow,self).__init__(parent)

        self.setWindowTitle("代码实现的第一个主窗口")
        self.resize(400,300)
        self.status=self.statusBar()
        self.status.showMessage('11111',5000)

if  __name__ == "__main__":
    chRec()
    app=QApplication(sys.argv)
    app.setWindowIcon(QIcon("./心2.ico"))

    main=FirstMainWindow()
    main.show()

    sys.exit(app.exec_())