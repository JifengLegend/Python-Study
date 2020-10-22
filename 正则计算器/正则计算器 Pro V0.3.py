import sys

from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget
from functools import partial
import re
import pickle

import Ui_window
import Ui_ReHouseWindow
def click_success():
    print('我成功啦')
def regex(rule, a):
    a = re.sub(rule[0], rule[1], a, flags=re.M)
    return a
def save():
    rule = [ui.e1.text(), ui.e2.text()]
    cache = []
    try:
        f = open('regex history.pkl', 'rb')
        cache.extend(pickle.load(f))
        print(cache)
        f.close()
    except (FileNotFoundError, EOFError) as reason:
        pass
    if rule[0] == '':
        ui.textResult.setText('还没输入匹配呢，无法保存')
    else:
        cache.append(rule)
        print(cache)
        f = open('regex history.pkl', 'wb')
        pickle.dump(cache, f)
        f.close()
def read():
    f = open('regex history.pkl', 'rb')
    read = pickle.load(f)
    print(read)
    f.close()
def RegexStart():
    global a
    rule = [ui.e1.text(), ui.e2.text()]
    a = ui.textGet.toPlainText()
    print(f'原始文本\n{a}\n')
    print(rule)
    if a == '\n'or a=='':
        a = '还没输入文本呢'
    else:
        if rule[0] == '':
            a = '还没输入匹配呢'
        else:
            a = regex(rule, a)
    print(a)
    # ui.textResult.setText(a)
    ui.statusbar.showMessage(a)
class Child(QMainWindow,Ui_ReHouseWindow.Ui_ReHouseWindow):
    def __init__(self):
        super(Child,self).__init__()
        self.setupUi(self)
    def open(self):
        self.show()

def openHouse():
    ch=Ui_ReHouseWindow.Ui_ReHouseWindow()
    ch.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_window.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.textGet.setPlaceholderText('在这里输入原始文本哦')
    ui.textResult.setPlaceholderText('处理/翻译后的文本会出现在这里')
    # ch=Ui_ReHouseWindow.Ui_ReHouseWindow()
    ch=Child()

    ui.startBtn.clicked.connect(RegexStart)
    ui.proBtn.clicked.connect(ch.open)


    MainWindow.show()
    sys.exit(app.exec_())