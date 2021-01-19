import sys
import window

from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow
if __name__ == "__main__":
    # 根据输入参数，创建应用实例
    app=QApplication(sys.argv)
    # 创建应用中的主窗口QMainWindow对象win
    win=QMainWindow()
    # 根据导入的window.py，实例化它的Ui_MainWindow，命名为ui
    ui=window.Ui_MainWindow()
    # 调用ui的函数，和主窗口win绑定
    ui.setupUi(win)
    win.show()
    sys.exit(app.exec_())