import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QListWidgetItem,QFileDialog
from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets
import re
import os
from tkinter import *
import csv




import window

def chRec():
    recPath=__file__
    recPath=re.sub(r'[a-z_]+\.py','',recPath)
    print(recPath)
    os.chdir(recPath)
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
        # print(self.money,self.l[6],self.l[payObj])
        return self.money
class ConList():
    def __init__(self,payList,text):
        self.payList=payList
        self.money=0
        for each in self.payList:
            self.cache=PayMess(each)
            self.money+=self.cache.calc()
        judge='+' if self.money>0 else ''
        print(f'{text}共：\n\t{judge}{self.get()}')
        
    def get(self):
        return f2f(self.money)

def f2f(num):
    cache=f'{num:.2f}'
    return float(cache)
def f2s(num):
    flag='+' if num>0 else ''
    cache=f'{flag}{num:.2f}'
    return cache
def moneyAdd(*l):
    money=0

    for each in l:
        money+=each.money
    return f2f(money)
def inMoney(l):
    money=0
    for each in l:
        money+=float(each[payMoney][1:])
    print(f'从零钱里面转入零钱通共：\n\t{f2f(money)}')
    return f2f(money)
def redMoney(l):
    money=0
    for each in l:
        money-=float(each[payMoney][1:])
    print(f'群发红包共：\n\t{f2f(money)}')
    return f2f(money)
def redBackMoney(l):
    money=0
    for each in l:
        money+=float(re.search(r'\d+\.\d+',each[payState]).group())
    print(f'从红包中退款共：\n\t{f2f(money)}')
    return f2f(money)
def judgeUp(l):    
    '''
    分析是否为来自上级的转账
    从 支付方式 和 收入金额 判断
    '''
    cache=float(l[payMoney][1:])%40
    result=1 if (l[6]=='/')and(cache==0) else 0
    return result

def read():
    fselect=ui.l01.selectedItems()[0].text()
    with open(fselect,'r',encoding='utf-8')as f:
        reader=csv.reader(f)
        sheet=list(reader)
        name=re.search(r'\[.*\]',sheet[1][0]).group()
        names='账单持有人：'+name
        

        listDef=[]
        listSelf=[]
        listIn=[]
        listAdd=[]
        listDec=[]
        listRed=[]
        listRedBack=[]



        for row in sheet:
            if (len(row)==11) and (len(row[0])!=4):
                # print(row)
                if (row[6]!='零钱') and (row[6]!='/'):
                    listSelf.append(row)
                else:
                    listDef.append(row)
                if (row[4]=='/'):
                    listIn.append(row)
                if ((row[2]=='瀮风')or (row[2]=='偈妮')) and (judgeUp(row)):
                    listAdd.append(row)
                if(row[2]=="发出群红包") :
                    listRed.append(row)
                    if (row[payState][0:2]=='已退'):
                        listRedBack.append(row)
                if (row[payMoney]=='¥80.00')or (row[payMoney]=='¥40.00'):
                    listDec.append(row)
        # print(listSelf)
        print(f'账单归属人：{name}')
        # name='[四组]'
        pname.setText(name)
        
        if name!='[偈妮]':
            pname.setStyleSheet('color:green;')


        def_money=ConList(listDef,'零钱(默认)')
        flag='+' if def_money.money>0 else ''
        result=f'分析结果：{flag}{def_money.money:.2f}'
        print(result)
        ui.m02.setText(f'{flag}{def_money.money:.2f}')


        other_money=ConList(listSelf,'其它')
        def_money=ConList(listDef,'综合分析(默认)')
        money_In=ConList(listAdd,'瀮风转入')
        money_Dec=ConList(listDec,"转账支出")
        red_Money=ConList(listRed,'群发红包')
        back_Money=redBackMoney(listRedBack)

        finMoney=f2s(moneyAdd(money_In,money_Dec,red_Money)+back_Money)



        ui.x01.setText(f2s(money_In.money))
        ui.x02.setText(f2s(moneyAdd(money_Dec,red_Money)))
        ui.x03.setText(f2s(back_Money))

        ui.m01.setText(finMoney)
        ui.m02.setText(f2s(def_money.money))
        ui.m03.setText(f2s(other_money.money))

        ui.decText02.setText(finMoney)
        ui.addText02.setText(finMoney)


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

    chRec()
    init()

    ui.l01.setSpacing(3)
    ui.setRec.triggered.connect(setRec)

    ui.addAction.clicked.connect(adding)
    ui.decAction.clicked.connect(decing)
    MainWindow.show()
    sys.exit(app.exec_())