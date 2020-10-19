import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QListWidgetItem,QFileDialog
from functools import partial
import re
import os
from tkinter import *
import csv



import window

def click_success():
    m01('233')
    print('我成功啦')
def chRec():
    recPath=__file__
    recPath=re.sub(r'[a-z_]+\.py','',recPath)
    print(recPath)
    os.chdir(recPath)
def chFile():
    fileList=os.listdir()

    for each in range(len(fileList)):
        print(f"{each+1}:{fileList[each]}")
    fileNum=int(input("请输入要选择的文件：\n"))-1
    print(f"目前选择的文件是：{fileList[fileNum]}")
    return fileList[fileNum]
def chTypeFile(type):
    fileList=os.listdir()
    appList=[]
    for each in fileList:
        if re.search(f'\.{type}',each):
            appList.append(each)
    for each in range(len(appList)):
        print(f"{each+1}:{appList[each]}")
    return appList
global payTime,payWay,payObj,payGood,payType,payMoney,payCard,payState,payID,payCD,payText
payTime=0
payWay=1
payObj=2
payGood=3
payType=4
payMoney=5
payCard=6
payState=7
payID=8
payCD=9
payText=10
class PayMess:
    def __init__(self,l):
        self.l=l
        self.k=self.l[payType]
        self.k=1 if self.k=="收入" else -1
        self.money= float(self.l[payMoney][1:])*self.k
    def calc(self):
        print(self.money,self.l[6],self.l[payObj],self.l[payTime])
        return self.money
class ConList():
    def __init__(self,payList,text):
        self.payList=payList
        self.money=0
        for each in self.payList:
            self.cache=PayMess(each)
            self.money+=self.cache.calc()
        judge='+' if self.money>0 else ''
        print(f'{text}的收支计算结果为：\n\t{judge}{self.money:.2f}')
        
    def get(self):
        return self.money
def inMoney(l):
    money=0
    for each in l:
        money+=float(each[payMoney][1:])
    print(f'从零钱里面转入零钱通共：\n\t{money}')
    return money

def read():
    fselect=ui.l01.selectedItems()[0].text()
    with open(fselect,'r',encoding='utf-8')as f:
        reader=csv.reader(f)
        sheet=list(reader)
        name='账单持有人：'+re.search(r'\[.*\]',sheet[1][0]).group()
        

        listDef=[]
        listSelf=[]
        listIn=[]

        for row in sheet:
            if (len(row)==11) and (len(row[0])!=4):
                # print(row)
                if (row[6]!='零钱') and (row[6]!='/'):
                    listSelf.append(row)
                else:
                    listDef.append(row)
                if (row[4]=='/'):
                    listIn.append(row)
        # print(listSelf)
        print(f'账单归属人：{name}')
        pname.setText(re.search(r'\[.*\]',sheet[1][0]).group())


        def_money=ConList(listDef,'零钱(默认)')
        flag='+' if def_money.money>0 else ''
        result=f'分析结果：{flag}{def_money.money:.2f}'
        print(result)
        m01(f'{flag}{def_money.money:.2f}')

        
        other_money=ConList(listSelf,'其它')
        in_money=inMoney(listIn)
        print(f'其它结余：{other_money.money+in_money:.2f}')
        flag='+' if other_money.money+in_money>0 else ''
        m02(f'{flag}{other_money.money+in_money:.2f}')

        ui.decText02.setText(f'{flag}{def_money.money:.2f}')
        ui.addText02.setText(f'{flag}{def_money.money:.2f}')
def setRec():
    dir_choose=QFileDialog.getExistingDirectory(None,'选取文件夹','.')
    print(f'当前目录为：{dir_choose}')
    os.chdir(dir_choose)
    init()

def init():
    ui.l01.clear()
    fileList=chTypeFile('csv')
    print(fileList)
    for each in fileList:
        ui.l01.addItem(each)
        ui.l01.setCurrentRow(0)
def adding():
    t01=float(ui.addText01.text())
    t02=float(ui.addText02.text())
    ui.addText03.setText(f'{(t01+t02):.2f}')

def decing():
    t01=float(ui.decText01.text())
    t02=float(ui.decText02.text())
    ui.decText03.setText(f'{(t01-t02):.2f}')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = window.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.b01.clicked.connect(read)
    pname=ui.pname
    pname.setText('')
    m01=ui.m01.display
    m02=ui.m02.display
    chRec()
    init()
    

    ui.l01.setSpacing(3)
    ui.setRec.triggered.connect(setRec)

    ui.addAction.clicked.connect(adding)
    ui.decAction.clicked.connect(decing)
    MainWindow.show()
    sys.exit(app.exec_())