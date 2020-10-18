import re
import xlrd
import os
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

if __name__ == "__main__":
    chRec()
    # fileName=chFile()

    with open('微信支付账单(20200917-20201017).csv','r',encoding='utf-8')as f:
        reader=csv.reader(f)
        sheet=list(reader)
        name=re.search(r'\[.*\]',sheet[1][0]).group()


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
        other_money=ConList(listSelf,'其它')
        in_money=inMoney(listIn)

        print(f'零钱通最终结余：\n\t{other_money.money+in_money:.2f}')
        









