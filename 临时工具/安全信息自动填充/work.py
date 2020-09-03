import xlrd
import xlwt
import os
from os import path
import random
from xlutils.copy import copy
from datetime import datetime

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
        sheet.write(n,i+2,tem(),setStyle())

def writeInfo(sheet,n,index):
    # sheet.write(n,4,'全天' if random.randint(0,10)>5 else '上午',setStyle())
    sheet.write(n,5,'否',setStyle())
    sheet.write(n,7,'无',setStyle())
    # if index==0:
    #     data0=d00
    #     data1=d01
    # elif index==1:
    #     data0=d10
    #     data1=d11
    # sheet.write(n,7,getPlace(data0),setStyle())
    # sheet.write(n,8,getWord(data1),setStyle())

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
    for num in range(8,rows):
        if sheet.cell(num,5).value=='':
            # print(sheet.row_values(num))
            return num
        
def setStyle(horalign=2,veralign=1):
    style=xlwt.XFStyle()    
    style.font.name='宋体'
    style.font.height = 20*12
    style.alignment.horz=horalign
    style.alignment.vert=veralign
    style.borders.left=1
    style.borders.right=1
    style.borders.top=1
    style.borders.b =1
    return style
def changeDate(row):
    dataRaw=rbcache.cell(row,1).value
    dataRaw = datetime(*xlrd.xldate_as_tuple(dataRaw
    ,0))
    date01=dataRaw.strftime('%m')
    date02=dataRaw.strftime('%d')
    date=f'{int(date01)}月{int(date02)}日'
    wbcache.write(row,1,date,setStyle())
    
if __name__ == "__main__":
    # realPath=path.abspath('.')
    # os.chdir(path.join(realPath,'临时工具\安全信息自动填充'))


    # 带格式的读取整个表格
    rb=xlrd.open_workbook('学硕二班_网格4组“一人一册”健康状况记录表.xls',formatting_info=True)
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
        # print(rbcache.row_values(pinRow(rbcache)-1))

        writeTem(wbcache,pinRow(rbcache)+0)
        writeInfo(wbcache,pinRow(rbcache)+0,index)
        for row in range(8,43):
            changeDate(row)


        



    try:
        wb.save('01.xls')
    except PermissionError:
        print('\n--文件已存在，写入失败--')

    