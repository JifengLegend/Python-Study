import webbrowser
import os,re,time
import pyautogui
import py7zr

import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFormLayout,QLineEdit,QLabel,QPushButton,QWidget,QVBoxLayout,QHBoxLayout
from PyQt5.QtCore import Qt

def chRec():
    absPath=__file__
    recPath=absPath[:absPath.rfind("\\")]
    os.chdir(recPath)

def easyMove(x,y):
    pyautogui.moveTo(x,y,duration=2.0,tween=pyautogui.easeInOutQuad)
def easyMoveRel(x,y):
    pyautogui.moveRel(x,y,duration=2.0,tween=pyautogui.easeInOutQuad)
def findMove(filename,x,y,w,h):
    aaa=pyautogui.locateCenterOnScreen(filename,region=(x,y,w,h))
    if aaa==None:
        print('404')
    else:
        easyMove(aaa.x,aaa.y)

def find_new_file(dir):
    '''查找目录下最新的文件'''
    file_lists = os.listdir(dir)
    file_lists.sort(key=lambda fn: os.path.getmtime(dir + "\\" + fn)
                    if not os.path.isdir(dir + "\\" + fn) else 0)
    print('最新的文件为： ' + file_lists[-1])
    file = os.path.join(dir, file_lists[-1])
    print('完整路径：', file)
    return file_lists[-1],file

class MainWindowClass(QMainWindow):
    def __init__(self,parent=None):
        pyautogui.PAUSE=0.5
        super().__init__(parent)
        self.setWindowTitle("获取下载文件")


        self.resize(700,500)
        self.initUi()
        self.task()
        # self.status=self.statusBar()
        # self.status.showMessage('11111',5000)
    def initUi(self):
        self.status=self.statusBar()
        formLayout=QFormLayout()
        vbox=QVBoxLayout()
        vbox2=QVBoxLayout()
        hbox=QHBoxLayout()
        self.edit1=QLineEdit()
        self.edit2=QLineEdit()
        self.edit3=QLineEdit()
        self.edit3.setText(r'C:\Users\JIfeng-X\Downloads')

        self.lb1=QLabel('最新的文件名为：')
        self.lb2=QLabel('')
        self.lb2.setAlignment(Qt.AlignCenter)

        self.bt1=QPushButton("下载")
        self.bt2=QPushButton("解密")


        formLayout.addRow('邮箱网址：',self.edit1)
        formLayout.addRow('解压密码：',self.edit2)
        formLayout.addRow('下载位置：',self.edit3)

        vbox.addLayout(formLayout)
        hbox.addWidget(self.bt1)
        hbox.addWidget(self.bt2)

        
        vbox2.addWidget(self.lb1)
        vbox2.addWidget(self.lb2)

        vbox.addLayout(vbox2)
        vbox.addLayout(hbox)


        mainFrame=QWidget()        
        mainFrame.setLayout(vbox)

        self.setCentralWidget(mainFrame)
    def task(self):
        self.bt1.clicked.connect(self.downFile)
        self.bt2.clicked.connect(self.upPack)

    def downFile(self):
        self.dir=self.edit3.text()
        # 载入网页
        webbrowser.open(self.edit1.text())
        # 点击收件箱
        time.sleep(3)
        findMove('./收件箱.png',0,200,600,900)
        pyautogui.click()
        # 点击最新邮件
        findMove('./今天.png',400,520,800,400)
        easyMoveRel(200,70)
        pyautogui.click()
        # 点击下载
        time.sleep(0.5)
        findMove('./下载.png',570,1600,800,220)
        pyautogui.click()

        time.sleep(2)




    def upPack(self):
        # 查找本地最新文件
        name,self.address=find_new_file(self.dir)
        self.lb2.setText(name)

        self.dir=self.edit3.text()
        self.passWord=self.edit2.text()
        if not os.path.exists(r'D:\cache'):
            os.mkdir(r'D:\cache')
        try:
            with py7zr.SevenZipFile(self.address,mode='r',password=self.passWord) as z:
                z.extractall(r'D:\cache')
                self.status.showMessage(r'解压成功，文件保存在 D:\cache 目录',5000)
        except:
            self.status.showMessage('解压失败',5000)


if __name__ == '__main__':
    chRec()
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./网络.png'))

    mainWin=MainWindowClass()
    mainWin.show()
    sys.exit(app.exec_())