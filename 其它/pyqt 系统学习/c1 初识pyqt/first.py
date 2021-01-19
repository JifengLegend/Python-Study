import sys

from PyQt5.QtWidgets import QApplication,QWidget
if __name__ == "__main__":
    # 创建QApplication类的实例
    app=QApplication(sys.argv)
    # 创建一个窗口
    window=QWidget()
    # 设置尺寸
    window.resize(300,150)
    # 移动窗口
    window.move(100,200)
    # 设置窗口标题
    window.setWindowTitle("初识pyqt")
    # 显示窗口
    window.show()

    # 进入程序的主循环，并通过exit函数确保主循环安全结束
    sys.exit(app.exec_())
    