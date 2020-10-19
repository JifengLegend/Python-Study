import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from functools import partial

import hello_world
def click_success():
    print('我成功啦')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = hello_world.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.pushButton.clicked.connect(partial(convert,ui))
    MainWindow.show()
    sys.exit(app.exec_())