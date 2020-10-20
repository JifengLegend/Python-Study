import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QListWidgetItem,QFileDialog,QMessageBox
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
def judgeNmae(l):
    
    return re.search(r'(珊珊|瀮风|偈妮)',l[2])
def judgeRed(l):
    return re.search(r'(群红|退款)',l[1])
def printList(l):
            # print(self.money,self.l[6],self.l[payObj])
        for each in l:
            k=l[payType]
            k=1 if k=='收入' else -1
            mm=float(each[payMoney][1:])*k
            print(f'{mm}\t{each[6]}\t{each[payObj]}\t{each[payTime]}')
def printData(csv_writer,l,str,name):
    '''
    csv_writer:要写入的文件\n
    l:要写入的数据列表\n
    str:情况分类\n
    name:持有人\n
    '''
    csv_writer.writerow([''])
    csv_writer.writerow(['特殊情况','','',str])
    csv_writer.writerow(['持有人',name])
    csv_writer.writerow([''])
    csv_writer.writerow(['交易时间','交易类型','交易对方','商品','收/支','金额(元)','支付方式','当前状态','交易单号','商户单号','备注'])
    for each in l:
        csv_writer.writerow(each)

        
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
        listDanger=[]
        listTongTo=[]
        listToTong=[]
        listToCard=[]
        listCardTo=[]
        listCash=[]
        listTan=[]
        



        for row in sheet:
            if (len(row)==11) and (len(row[0])!=4):
                # print(row)
                if (row[6]!='零钱') and (row[6]!='/'):
                    listSelf.append(row)
                else:
                    listDef.append(row)
                # if (row[4]=='/'):
                #     listIn.append(row)
                if (judgeNmae(row)) and (judgeUp(row)):
                    listAdd.append(row)
                if(row[2]=="发出群红包")or(row[1]=='微信红包（单发）'and not((row[payMoney]!='¥0.30')and(row[payMoney]!='¥0.10')and(row[payMoney]!='¥0.01'))) :
                    listRed.append(row)
                    if (row[payState][0:2]=='已退'):
                        listRedBack.append(row)
                if name=='[偈妮]':
                    if (row[payMoney]=='¥80.00')or (row[payMoney]=='¥40.00'):
                        listDec.append(row)
                if (row[payCard]=='零钱')and (row[4]=='支出'or row[4]=='/'):
                    if not(judgeRed(row)) :
                        if (row[payMoney]!='¥0.30')and(row[payMoney]!='¥0.10')and(row[payMoney]!='¥0.01'):
                            listDanger.append(row) 
                # if(row)
                if(row[payCard]=='零钱通')and(row[1]=='零钱通转出-到零钱'):
                    listTongTo.append(row)
                if(row[1]=='零钱提现'):
                    listToCard.append(row)
                if(row[1]=='转入零钱通-来自零钱'):
                    listToTong.append(row)
                if(row[1]=='零钱充值'):
                    listCardTo.append(row)
                # if(row[payCard]=='零钱')
                
        # print(listSelf)
        print(f'账单归属人：{name}')
        # name='[四组]'
        pname.setText(name)
        
        if name!='[偈妮]':
            pname.setStyleSheet('color:green;')

        # print(listRed)
        def_money=ConList(listDef,'零钱(默认)')
        flag='+' if def_money.money>0 else ''
        result=f'分析结果：{flag}{def_money.money:.2f}'
        print(result)
        ui.m02.setText(f'{flag}{def_money.money:.2f}')

        print(f"{name}危险操作：")
        for each in listDanger:
            print(each[0:7])
        try:
            with open('Danger Action List.csv','w',encoding='utf-8-sig',newline='')as f:
                csv_writer=csv.writer(f)
                csv_writer.writerow(['危险操作汇总列表'])
                csv_writer.writerow(['持有人',name])
                csv_writer.writerow([''])
                csv_writer.writerow(['交易时间','交易类型','交易对方','商品','收/支','金额(元)','支付方式','当前状态','交易单号','商户单号','备注'])
                for each in listDanger:
                    csv_writer.writerow(each)
        except PermissionError:
            alertBox=QMessageBox.information(None,'注意','文件目前被占用')








        print(name)

        other_money=ConList(listSelf,'其它结余')
        def_money=ConList(listDef,'综合分析(默认)')
        money_In=ConList(listAdd,'公司转入')
        money_Dec=ConList(listDec,"转账支出")
        red_Money=ConList(listRed,'群发红包')
        back_Money=redBackMoney(listRedBack)

        tongTo_money=ConList(listTongTo,'零钱通 转入 零钱').money
        toTong_money=ConList(listToTong,'零钱 转入 零钱通').money

        toCard_money=ConList(listToCard,'零钱 转到 银行卡').money
        cardTo_money=ConList(listCardTo,'银行卡 转到 零钱').money

        danger_money=ConList(listDanger,f'{name}危险操作').money

        tongIn_money=toTong_money-tongTo_money
        cardIn_money=toCard_money-cardTo_money




        finMoney=f2s(moneyAdd(money_In,money_Dec,red_Money)+back_Money)
        print(f'公司出入账\n\t{finMoney}')

        try:
            with open(f'Result.csv','w',encoding='utf-8-sig',newline='')as f:
                csv_writer=csv.writer(f)
                csv_writer.writerow(['特殊情况汇总列表'])
                printData(csv_writer,listToCard,'零钱 转到 银行卡',name)
                printData(csv_writer,listCardTo,'银行卡 转到 零钱',name)
                printData(csv_writer,listToTong,'零钱 转入 零钱通',name)
                printData(csv_writer,listTongTo,'零钱通 转入 零钱',name)
        except PermissionError:
            alertBox=QMessageBox.information(None,'注意','文件目前被占用')

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
