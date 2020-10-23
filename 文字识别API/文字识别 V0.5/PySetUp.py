import os
import sys
import re

def chRec():
    recPath=__file__
    recPath=re.sub(r'[A-z_]+\.py','',recPath)
    print(recPath)
    os.chdir(recPath)
if __name__ == "__main__":
    chRec()
    rawName=input('请输入 ***.ui 文件的名称：\n')
    uiName=rawName+'.ui'
    pyName=rawName+'.py'

    command=f'pyuic5 -o {pyName} {uiName}'
    os.system(command)
    print(f'{pyName} 文件已生成~')

    mainText=f'''import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from functools import partial

import {rawName}
# def click_success():
    # print('我成功啦')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = {rawName}.Ui_MainWindow()
    ui.setupUi(MainWindow)
    # ui.pushButton.clicked.connect(partial(convert,ui))
    MainWindow.show()
    sys.exit(app.exec_())'''


    with open ('main.py','w',encoding='utf-8')as f:
        f.write(mainText)
        print("主函数 main.py 已生成~")