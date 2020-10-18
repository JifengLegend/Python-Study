import zipfile
import re
import os
import csv
import shutil


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
    fileNum=int(input("请输入要选择的文件：\n"))-1
    print(f"目前选择的文件是：{appList[fileNum]}")
    return appList[fileNum]
        
if __name__ == "__main__":
    
    chRec()
    # fileName=chFile()
    fileName=chTypeFile('zip')
    passWord=input('请输入该文件的密码：\n')

    zip_file=zipfile.ZipFile(fileName)

    zip_list=zip_file.namelist()

    # print(zip_file)
    # print(zip_list)
    zip_file.extract(zip_list[1],'./folder',pwd=passWord.encode('utf-8'))



    rawName=re.sub(r'.*\/','',zip_list[1])  
    # print(rawName)
    realName=re.sub(r'.csv','',rawName)
    cfile=os.path.join('./folder/',realName,rawName)
    rfile=os.path.join('./folder/',rawName)
    sfile=os.path.join('./folder/',realName)



    # print(cfile)

    with open (cfile,'r',encoding='utf-8')as f:
        reader =csv.reader(f)
        sheet=list(reader)
        name=re.search(r'\[.*\]',sheet[1][0]).group()
        print(name)

    rename=name+rawName[4:]
    refile=os.path.join('./folder/',rename)
    # print(cfile,rfile)
    shutil.move(cfile,rfile)

    os.rename(rfile,refile)
    os.rmdir(sfile)

