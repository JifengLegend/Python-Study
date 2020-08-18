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
# def filterFile(fileList):
#     return bool(x) for x in selMode
if __name__ == "__main__":    
    fileList=os.listdir()

    for each in range(len(fileList)):
        print(f"{each+1}:{fileList[each]}")

    # fileNum=int(input("请输入要选择的文件：\n"))-1
    # print(f"目前选择的文件是：{fileList[fileNum]}")
    # realName=getRealName(fileList[fileNum],'【后续完整课程必加微信：kaoyan800，完整课程福利更新QQ群：651077908】')
    # os.rename(fileList[fileNum],realName)
    selMode=selectFile(fileList,'2020.')
    print(selMode)
    for each in selMode:
        # print(bool(each))
        pass
    # print(list(bool(i) for i in selMode))
    # print(filter(filterFile,fileList))
    fileListNew= list(compress(fileList,selMode))
    print(fileListNew)
    sortAndMove(fileListNew)

    # for each in fileListNew:
    #     realName=getRealName(each,'【后续完整课程必加微信：kaoyan800，完整课程福利更新QQ群：651077908】')
    #     os.rename(each,realName)
