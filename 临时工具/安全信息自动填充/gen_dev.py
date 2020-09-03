import xlrd
import xlwt
import os
from os import path
import random

def addSheet(wb01):
    s01=wb01.add_sheet('张宝中')
    s02=wb01.add_sheet('张晋豪')
    s03=wb01.add_sheet('张川')
    s04=wb01.add_sheet('张方实')
    s05=wb01.add_sheet('张煚森')
def tem()->float:
    a=35.5+random.randint(0,10)*0.12
    a=round(a,1)
    return a
def writeTem(sheet,n):
    for i in range(3):
        sheet.write(n,i+1,tem())

def writeInfo(sheet,n,d00,d01):
    sheet.write(n,4,'全天' if random.randint(0,10)>5 else '上午')
    sheet.write(n,5,'否')
    sheet.write(n,6,'无')
    sheet.write(n,7,getPlace(d00))
    sheet.write(n,8,getWord(d01))

def getWord(data):
    dlen=random.randint(1,4)
    dataR=random.sample(data,dlen)
    dataS=''
    for each in dataR:
        dataS+=each+'，'

    return dataS[0:-1]
def getPlace(data):
    dlen=random.randint(0,3)
    dataList=[data[0]]
    if random.random()<=0.7 :
        dataList.append(data[1])
    
    dataR=random.sample(data[2:],dlen)
    dataList=dataList+dataR
    dataList=random.sample(dataList,len(dataList))
    dataS=''
    for each in dataList:
        dataS+=each+'，'

    return dataS[0:-1]
def pinRow(sheet):
    rows=sheet.nrows
    for num in range(rows):
        if sheet.cell(num,6).value=='':
            return num
        
if __name__ == "__main__":
    # realPath=path.abspath('.')
    # os.chdir(path.join(realPath,'临时工具\安全信息自动填充'))
    wb01=xlwt.Workbook()
    # addSheet(wb01)
    ss1=wb01.add_sheet('张宝中')
    ss2=wb01.add_sheet('张晋豪')
    

    d00=['文化1A','远航二区204','中心食堂','心海餐厅','第四餐厅']
    d01=['张晋豪','张川','钟振宇','王关杰','李文正','杨国涛']

    d10=['文化1A','远航二区204','中心食堂','心海餐厅','第四餐厅']
    d11=['张宝中','张川','张方实','王关杰','李文正']

    # for i in range(10):

    #     writeTem(ss1,i)
    #     writeInfo(ss1,i,d00,d01)

    #     writeTem(ss2,i)
    #     writeInfo(ss2,i,d10,d11)
    



    # wb01.save('workBook.xls')
    wb01=xlrd.open_workbook('workBook.xls')
    sheetName=wb01.sheet_names()
    for num,eachSheet in enumerate(sheetName):
        s01=wb01.sheet_by_index(num)

        # for each in range(s01.nrows):
        #     print(s01.row_values(each))
        print('_'*50)
        print(pinRow(s01))
    

    

    