import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QIcon
import os
def chRec():
    absPath=__file__
    recPath=absPath[:absPath.rfind("\\")]
    os.chdir(recPath)
class IconWindow(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)

        self.setWindowTitle("设置窗口图标")
        self.setGeometry(300,300,350,250)

        self.setWindowIcon(QIcon("./心2.ico"))


if  __name__ == "__main__":
    chRec()
    app=QApplication(sys.argv)
    # app.setWindowIcon(QIcon("./心2.ico"))

    main=IconWindow()
    main.show()

    sys.exit(app.exec_())