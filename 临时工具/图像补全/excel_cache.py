import re
import xlrd
import xlwt
import os

realPath=r'C:\Users\Administrator\Desktop\python 学习\临时工具\图像补全'
os.chdir(realPath)

# xlfile=xlrd.open_workbook(r'dataBase.xls')

# sheetList=xlfile.sheet_names()[0]
# sheet0=xlfile.sheet_by_index(0)
# sheet1=xlfile.sheet_by_name('d60')

# con0=sheet0.cell_value(1,1)
def writeList(sheet,adress,list):
    for num in range(len(list)):
        sheet.write(num,adress,list[num])


myfile=xlwt.Workbook()
mySheet=myfile.add_sheet('d50')
myStyle=xlwt.easyxf("font:name Times New Roman,color-index red,bold on", num_format_str='#,##0.00')
a=[1,2,3,4,5]
writeList(mySheet,0,a)
myfile.save('dataBase.xls')
# print(con0)