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
        sheet.write(n,i+1,tem(),setStyle())

def writeInfo(sheet,n,index):
    sheet.write(n,4,'全天' if random.randint(0,10)>5 else '上午',setStyle())
    sheet.write(n,5,'否',setStyle())
    sheet.write(n,6,'无',setStyle())
    if index==0:
        data0=d00
        data1=d01
    elif index==1:
        data0=d10
        data1=d11
    sheet.write(n,7,getPlace(data0),setStyle())
    sheet.write(n,8,getWord(data1),setStyle())

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
def setStyle(horalign=2,veralign=2):
    style=xlwt.XFStyle()    
    # style.font.name=name
    style.alignment.horz=horalign
    style.alignment.vert=veralign
    return style
    
if __name__ == "__main__":
    realPath=path.abspath('.')
    os.chdir(path.join(realPath,'临时工具\安全信息自动填充'))

    global d00,d01,d10,d11
    d00=['文化1A','远航二区204','中心食堂','心海餐厅','第四餐厅']
    d01=['张晋豪','张川','钟振宇','王关杰','李文正','杨国涛']

    d10=['文化1A','远航二区204','中心食堂','心海餐厅','第四餐厅']
    d11=['张宝中','张川','张方实','王关杰','李文正']

    # 带格式的读取整个表格
    rb=xlrd.open_workbook('workBook.xls',formatting_info=True)
    rbS=rb.sheet_names()


    rb01=rb.sheets()[0]
    # 把读取的表格复制成可编辑的格式
    wb=copy(rb)


    # 获取可读写的sheet
    wb01=wb.get_sheet(0)
    # writeTem(wb01,12)
    
    for index ,name in enumerate(rbS):
        wbcache=wb.get_sheet(index)
        rbcache=rb.sheet_by_index(index)
        
        print(pinRow(rbcache))
        writeTem(wbcache,pinRow(rbcache)+0)
        writeInfo(wbcache,pinRow(rbcache)+0,index)
        xflist=rb.xf_list
        cell01=rbcache.cell_xf_index(4,3)
        cellXF=xflist[cell01]



    wb.save('workBook.xls')

    