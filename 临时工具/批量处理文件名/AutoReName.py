import re
import os
from itertools import compress

def getRealNameback(raw,delStr):
    nameList=raw.split(".")
    realType='.'+nameList[-1]
    realWord=re.sub(realType,'',raw)
    realName=re.sub(delStr,'',realWord)
    return f'{realName}.{realType}'
def getRealName(raw,delStr,rep):
    realName=re.sub(delStr,rep,raw)
    return f'{realName}'
def selectFile(fileList,*args):
    selcache=[]
    for eachName in fileList:
        selcachesub=0
        for eachMatch in args:
            if re.search(eachMatch,eachName)==None:
                pass
            else:
                selcachesub+=1
        if selcachesub==len(args):
            selcache.append('1')
        else:
            selcache.append('')
        
    return selcache 
def printList(list):
    for each in range(len(list)):
        print(f'{each+1}:{list[each]}')
def processing(realPath,path,strs,rep):
    print('-'*50)
    os.chdir(os.path.join(realPath,path))
    print(f"当前目录'{path}' 文件如下：")
    fileList=os.listdir()

    for each in range(len(fileList)):
        print(f"{each+1}:{fileList[each]}")

    print('-'*50)
    print(f"-- 目录'{path}' 选择状态：")
    selMode=selectFile(fileList,delWord)
    print(selMode)

    fileListNew= list(compress(fileList,selMode))
    printList(fileListNew)
    print('-'*50)

    for each in fileListNew:
        realName=getRealName(each,strs,rep)
        os.rename(each,realName)
    os.chdir(os.pardir)
if __name__ == "__main__":
    realPath=os.path.abspath('.')
    delWords=input("--请输入要文件名中要替换的字,按[]分隔：").split("[]")
    repWords=input("--请输入要换成的文字：")
    for each in list(os.walk('.')):
        path,content,files=each[0],each[1],each[2]
        # printList(content+files)
        for delWord in delWords:
            processing(realPath,path,delWord,repWords)

    print('-'*50) 