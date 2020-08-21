import re
import os
from itertools import compress
import shutil

def getRealName(raw,delStr):
    realWord,realType=raw.split(".")
    realName=re.sub(delStr,'',realWord)
    return f'{realName}.{realType}'
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
def sortAndMove(fileList):
    newFolder=input('请输入新文件夹名，默认为 “笔记”：')
    if newFolder == '':
        newFolder='笔记'
    try:
        os.mkdir(newFolder)
    except FileExistsError:
        pass
    for each in fileList:
        fullPath=os.path.join(newFolder,each)
        shutil.move(each,fullPath)
def printList(list):
    for each in range(len(list)):
        print(f'{each+1}:{list[each]}')
if __name__ == "__main__":    
    fileList=os.listdir()

    for each in range(len(fileList)):
        print(f"{each+1}:{fileList[each]}")

    keyWords=input("请输入关键字，使用[]分隔：").split("[]")
    selMode=selectFile(fileList,*keyWords)
    print(selMode)
    fileListNew= list(compress(fileList,selMode))
    printList(fileListNew)
    sortAndMove(fileListNew)


