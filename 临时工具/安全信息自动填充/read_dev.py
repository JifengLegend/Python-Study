import xlrd
import xlwt
import os
from os import path
import random
from xlutils.copy import copy

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

def writeInfo(sheet,n,index):
    sheet.write(n,4,'全天' if random.randint(0,10)>5 else '上午')
    sheet.write(n,5,'否')
    sheet.write(n,6,'无')
    if index==0:
        data0=d00
        data1=d01
    elif index==1:
        data0=d10
        data1=d11
    sheet.write(n,7,getPlace(data0))
    sheet.write(n,8,getWord(data1))

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
    realPath=path.abspath('.')
    os.chdir(path.join(realPath,'临时工具\安全信息自动填充'))

    # 带格式的读取整个表格
    rb=xlrd.open_workbook('workBook.xls',formatting_info=True)
    rbS=rb.sheet_names()
    rb01=rb.sheet_by_index(0)
    xflist=rb.xf_list
    print(xflist)
    cell01=rb01.cell_xf_index(4,3)
    cell02=rb01.cell_xf_index(5,0)
    print(cell01,cell02)



    cellXf=xflist[cell01]
    print(cellXf.protection.cell_locked)
    print(cellXf.background.fill_pattern,\
        cellXf.background.background_colour_index)
    print(cellXf.alignment.hor_align)

    