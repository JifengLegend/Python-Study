import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QListWidgetItem,QFileDialog
from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets
import re
import os
from tkinter import *
import csv


import window
import Ui_ReHouseWindow
# 界面段
def chRec():
    recPath=__file__
    recPath=re.sub(r'[a-z_]+\.py','',recPath)
    print(recPath)
    os.chdir(recPath)
def copyRaw():    
    if ui.rawText.toPlainText()=='':
        ui.statusbar.showMessage(f"▶ 点击此处进行复制",3000)
    else:
        ui.rawText.selectAll()
        ui.rawText.copy()    
        cache=ui.rawText.toPlainText()[0:20]
        ui.statusbar.showMessage(f"▶ 原文本已复制  {cache}...",5000)
def copyRes():    
    if ui.resultText.toPlainText()=='':
        ui.statusbar.showMessage(f"▶ 点击此处进行复制",3000)
    else:
        ui.resultText.selectAll()
        ui.resultText.copy()
        cache=ui.resultText.toPlainText()[0:20]
        ui.statusbar.showMessage(f"▶ 结果文本已复制  {cache}...",5000)
def fontAddAction():
    global fontSize
    fontSize+=1
    font = QtGui.QFont()
    font.setFamily("微软雅黑 Light") #括号里可以设置成自己想要的其它字体
    font.setPointSize(fontSize) 
    ui.rawText.setFont(font)
    ui.resultText.setFont(font)
    ui.statusbar.showMessage(f'▶ 当前字体大小调整为：{fontSize}',5000)

def fontDecAction():
    global fontSize
    fontSize-=1
    fontSize=fontSize if fontSize>2 else 2
    font = QtGui.QFont()
    font.setFamily("微软雅黑 Light") #括号里可以设置成自己想要的其它字体
    font.setPointSize(fontSize) 
    ui.rawText.setFont(font)
    ui.resultText.setFont(font)
    ui.statusbar.showMessage(f'▶ 当前字体大小调整为：{fontSize}',5000)
def onTop():
    _translate = QtCore.QCoreApplication.translate
    if not ui.PinWindow.isChecked():
        MainWindow.setWindowFlags(QtCore.Qt.Widget)# 取消置顶
        MainWindow.show()
        ui.statusbar.showMessage('▶ 窗口置顶 已取消',5000)
        MainWindow.setWindowTitle(_translate("RegexQt", "正则计算器-Qt"))
    else:
        MainWindow.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint) # 打开置顶
        MainWindow.show()
        MainWindow.setWindowTitle(_translate("RegexQt", "正则计算器-Qt (置顶模式)"))
        ui.statusbar.showMessage('▶ 窗口置顶 已启动',5000)
class Child(QMainWindow,Ui_ReHouseWindow.Ui_ReHouseWindow):
    def __init__(self):
        super(Child,self).__init__()
        self.setupUi(self)
        
    def open(self):
        self.show()
def openHouse():
    ch=Ui_ReHouseWindow.Ui_ReHouseWindow()
    ch.show()
# 功能段
def regex(rule, a):
    a = re.sub(rule[0], rule[1], a, flags=re.M)
    return a
def RegexStart():
    global a
    rule = [ui.regexText.text(), ui.replaceText.text()]
    a = ui.rawText.toPlainText()
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
    ui.resultText.setPlainText(a)
    ui.statusbar.showMessage("▶ 已完成正则处理",5000)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = window.Ui_RegexQt()
    ui.setupUi(MainWindow)

    global fontSize
    fontSize=11
    ch=Child()
    # 绑定段
    ui.rawLabel.clicked.connect(copyRaw)
    ui.resultLabel.clicked.connect(copyRes)
    ui.RunBtn.clicked.connect(RegexStart)
    ui.FontAdd.triggered.connect(fontAddAction)
    ui.FontDec.triggered.connect(fontDecAction)
    ui.PinWindow.triggered.connect(onTop)
    ui.proBtn.clicked.connect(ch.open)

    MainWindow.show()
    sys.exit(app.exec_())