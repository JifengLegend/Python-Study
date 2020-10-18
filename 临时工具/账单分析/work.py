import re
import xlrd
import os
from tkinter import *
import csv

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
        # print(self.money,self.l[6],self.l[payObj],self.l[payTime])
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
    fselect=listbox1.get(ACTIVE)
    print(fselect)

    with open(fselect,'r',encoding='utf-8')as f:
        reader=csv.reader(f)
        sheet=list(reader)
        name='账单持有人：'+re.search(r'\[.*\]',sheet[1][0]).group()
        Pname.set(name)

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
        def_money=ConList(listDef,'零钱(默认)')
        result=f'分析结果：{def_money.money:.2f}'
        Presult1.set(result)
        other_money=ConList(listSelf,'其它')
        in_money=inMoney(listIn)
        Presult2.set(f'其它结余：{other_money.money+in_money:.2f}')


if __name__ == "__main__":
    root=Tk()
    root.title('账单分析器')
    root.geometry('400x516+10+10')

    Pname=StringVar()
    Presult1=StringVar()
    Presult1.set('读取文件后，分析结果在这里呈现哦~')
    Presult2=StringVar()

    frame1=LabelFrame(root,text='请选择文件：',padx=10, pady=10)
    frame1.pack(side=TOP,padx=5,pady=5)

    listbox1=Listbox(frame1,width=50)
    listbox1.pack(side=TOP, padx=5, pady=5,expand=1,fill=BOTH)

    chRec()
    fileList=chTypeFile('csv')
    for each in fileList:
        listbox1.insert(END,each)
    
    btn1=Button(frame1,text='读取',command=read,width=80)
    btn1.pack(side=BOTTOM,padx=5,pady=5)

    frame2=Frame(root,padx=10,pady=0)
    frame2.pack(side=BOTTOM,padx=10,pady=10)



    lable1=Label(frame2,textvariable=Pname,padx=10,pady=5,anchor=E,fg='#2a2739',font=("微软雅黑", 15))
    lable1.grid(row=0,column=0,padx=10,pady=10)
    lable2=Label(frame2,textvariable=Presult1,padx=10,pady=5,anchor=E,fg='#222222',font=("微软雅黑", 13))
    lable2.grid(row=1,column=0,padx=10,pady=10)
    lable3=Label(frame2,textvariable=Presult2,padx=10,pady=5,anchor=E,fg='#222222',font=("微软雅黑", 13))
    lable3.grid(row=3,column=0,padx=10,pady=10)



    root.mainloop()
