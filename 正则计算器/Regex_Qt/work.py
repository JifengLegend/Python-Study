import sys
import PyQt5.sip
from PyQt5.QtWidgets import QApplication, QMainWindow,QListWidgetItem,QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
import re
import os
import json


from window import Ui_RegexQt
from subWindow import Ui_Warehouse
import Ui_ReHouseWindow
# 界面段
def chRec():
    absPath=__file__ 
    recPath=absPath[:absPath.rfind("\\")]
    os.chdir(recPath)
def copyRaw():    
    if mainWin.rawText.toPlainText()=='':
        mainWin.statusbar.showMessage(f"▶ 点击此处进行复制",3000)
    else:
        mainWin.rawText.selectAll()
        mainWin.rawText.copy()    
        cache=mainWin.rawText.toPlainText()[0:20]
        mainWin.statusbar.showMessage(f"▶ 原文本已复制  {cache}...",5000)
def copyRes():    
    if mainWin.resultText.toPlainText()=='':
        mainWin.statusbar.showMessage(f"▶ 点击此处进行复制",3000)
    else:
        mainWin.resultText.selectAll()
        mainWin.resultText.copy()
        cache=mainWin.resultText.toPlainText()[0:20]
        mainWin.statusbar.showMessage(f"▶ 结果文本已复制  {cache}...",5000)
def fontAddAction():
    global fontSize
    fontSize+=1
    font = QtGui.QFont()
    font.setFamily("微软雅黑 Light") #括号里可以设置成自己想要的其它字体
    font.setPointSize(fontSize) 
    mainWin.rawText.setFont(font)
    mainWin.resultText.setFont(font)
    mainWin.statusbar.showMessage(f'▶ 当前字体大小调整为：{fontSize}',5000)

def fontDecAction():
    global fontSize
    fontSize-=1
    fontSize=fontSize if fontSize>2 else 2
    font = QtGui.QFont()
    font.setFamily("微软雅黑 Light") #括号里可以设置成自己想要的其它字体
    font.setPointSize(fontSize) 
    mainWin.rawText.setFont(font)
    mainWin.resultText.setFont(font)
    mainWin.statusbar.showMessage(f'▶ 当前字体大小调整为：{fontSize}',5000)
def onTop():
    _translate = QtCore.QCoreApplication.translate
    if not mainWin.PinWindow.isChecked():
        MainWindow.setWindowFlags(QtCore.Qt.Widget)# 取消置顶
        MainWindow.show()
        mainWin.statusbar.showMessage('▶ 窗口置顶 已取消',5000)
        MainWindow.setWindowTitle(_translate("RegexQt", "正则计算器-Qt"))
    else:
        MainWindow.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint) # 打开置顶
        MainWindow.show()
        MainWindow.setWindowTitle(_translate("RegexQt", "正则计算器-Qt (置顶模式)"))
        mainWin.statusbar.showMessage('▶ 窗口置顶 已启动',5000)

def regex(rule, a):
    a = re.sub(rule[0], rule[1], a, flags=re.M)
    return a
def RegexStart():
    global a
    rule = [mainWin.regexText.text(), mainWin.replaceText.text()]
    a = mainWin.rawText.toPlainText()
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
    mainWin.resultText.setPlainText(a)
    mainWin.statusbar.showMessage("▶ 已完成正则处理",5000)


def save2Json(obj,path='./save.json'):
    with open(path,'w',encoding='utf-8')as f:
        f.write(json.dumps(obj,ensure_ascii=False))

class MainWindowClass(QMainWindow,Ui_RegexQt):
    openSub=QtCore.pyqtSignal()
    refresh=QtCore.pyqtSignal()
    closed=QtCore.pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()
    def initUi(self):
        global fontSize
        fontSize=11
        # 绑定段
        self.rawLabel.clicked.connect(lambda:self.rawText.selectAll())


        self.rawLabel.doubleClicked.connect(copyRaw)
        self.rawLabel.hover.connect(lambda : self.statusbar.showMessage('▶  此处单击全选/双击复制',5000))
        self.rawLabel.leave.connect(lambda : self.statusbar.showMessage(''))

        self.resultLabel.clicked.connect(lambda:self.resultText.selectAll())
        self.resultLabel.doubleClicked.connect(copyRes)
        self.resultLabel.hover.connect(lambda : self.statusbar.showMessage('▶  此处单击全选/双击复制',5000))
        self.resultLabel.leave.connect(lambda : self.statusbar.showMessage(''))
        self.RunBtn.clicked.connect(RegexStart)
        self.FontAdd.triggered.connect(fontAddAction)
        self.FontDec.triggered.connect(fontDecAction)
        self.PinWindow.triggered.connect(onTop)
        self.proBtn.clicked.connect(lambda : self.openSub.emit())
        self.label_3.doubleClicked.connect(lambda:self.regexText.setText(''))
        self.label_4.doubleClicked.connect(lambda:self.replaceText.setText(''))
        self.saveAction.triggered.connect(self.saveReg)
    def saveReg(self):
        with open ('./save.json','r',encoding='utf-8')as f:
            rawJson=json.loads(f.read())
        cache=  { "name": "Nothing", "match": self.regexText.text(), "replace": self.replaceText.text() }
        rawJson.append(cache)        
        save2Json(rawJson)
        self.refresh.emit()
    def closeEvent(self,e):
        self.closed.emit()

class SubWinClass(QtWidgets.QWidget,Ui_Warehouse):
    render=QtCore.pyqtSignal(str,str)
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.addRegItem()
        self.setWindowTitle('正则仓库')
        self.resize(600,450)
        self.initUi()
        self.band()
    def band(self):
        self.delBtn.clicked.connect(self.removeItem)
        self.reBtn.clicked.connect(self.rename)
        self.cancelBtn.clicked.connect(self.close)
        self.okBtn.clicked.connect(lambda : self.renderStrs(self.lv1.currentRow()))        
        self.lv1.currentRowChanged.connect(self.putIn)

    def initUi(self):
        self.delBtn.setStyleSheet('background:#ff4d4d;color:white')
        self.okBtn.setStyleSheet('background:#4662d9;color:white')

    def putIn(self):
        self.le1.setText(self.rawJson[self.lv1.currentRow()]['match'])
        self.le2.setText(self.rawJson[self.lv1.currentRow()]['replace'])
        self.le2.setAlignment(QtCore.Qt.AlignLeft)
    def renderStrs(self,index):
        if index==-1:
            pass
        else:
            cmatch,creplace=self.rawJson[index]['match'],self.rawJson[index]['replace']
            self.render.emit(cmatch,creplace)
    def creatItem(self,index,data):
        name=data['name']
        match=data['match']
        replace=data['replace']

        wd=QtWidgets.QWidget()
        QtWidgets
        lay00=QtWidgets.QHBoxLayout()
        lay10=QtWidgets.QVBoxLayout()
        lay11=QtWidgets.QHBoxLayout()
        lay12=QtWidgets.QHBoxLayout()

        lb1=QtWidgets.QLabel(str(index))
        lb1.setMaximumWidth(50)
        lb1.setAlignment(QtCore.Qt.AlignCenter)
        lb1.setFont(QtGui.QFont('微软雅黑',16))
        lb1.setStyleSheet('border:2px solid #4e6ef2;border-top:0px;border-left:0px;border-bottom:0px;')

        lb2=QtWidgets.QLabel(name)
        lb2.setFont(QtGui.QFont('微软雅黑',10))
        lb2.setAlignment(QtCore.Qt.AlignLeft)

        lb3=QtWidgets.QLabel(match)
        lb3.setFont(QtGui.QFont('微软雅黑',10))
        lb3.setStyleSheet('margin-left:5px;padding-left:10px;border:5px solid #4e6ef2;border-top:0px;border-right:0px;border-bottom:0px')
        lb4=QtWidgets.QLabel(replace)
        lb4.setFont(QtGui.QFont('微软雅黑',10))
        lb4.setStyleSheet('margin-left:5px;padding-left:10px;border:5px solid #4e6ef2;border-top:0px;border-right:0px;border-bottom:0px')    

        lay12.addWidget(lb3)
        lay12.addWidget(lb4)

        lay10.addWidget(lb2)
        lay10.addLayout(lay12)

        lay00.addWidget(lb1)
        lay00.addLayout(lay10)

        wd.setLayout(lay00)      
        return wd 
    def refresh(self):
        self.lv1.clear()
        self.addRegItem()
    def rename(self):
        index=self.lv1.currentRow()
        name=self.le1.text()
        self.rawJson[index]['name']=name
        save2Json(self.rawJson)
        self.refresh()
        self.lv1.setCurrentRow(index)
        
    def removeItem(self):
        index=self.lv1.currentRow()
        self.lv1.takeItem(index)
        self.rawJson.pop(index)
        save2Json(self.rawJson)
    def addRegItem(self):
        with open('./save.json','r',encoding='utf-8')as f:
            self.rawJson=json.loads(f.read())
        for index,eachData in enumerate(self.rawJson):
            wd=self.creatItem(index,eachData)
            item=QListWidgetItem()
            item.setSizeHint(QtCore.QSize(200,70))        
            self.lv1.addItem(item)
            self.lv1.setItemWidget(item,wd)

if __name__ == '__main__':
    chRec()
    app = QApplication(sys.argv)

    mainWin=MainWindowClass()

    subWin=SubWinClass()    
    subWin.render.connect(lambda str1,str2: mainWin.regexText.setText(str1))
    subWin.render.connect(lambda str1,str2: mainWin.replaceText.setText(str2))
 
    mainWin.openSub.connect(subWin.show)
    mainWin.refresh.connect(subWin.refresh)
    mainWin.closed.connect(subWin.close)

    mainWin.show()
    sys.exit(app.exec_())