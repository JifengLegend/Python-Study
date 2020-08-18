import re
import os
from itertools import compress

def getRealName(raw,delStr):
    nameList=raw.split(".")
    realType='.'+nameList[-1]
    realWord=re.sub(realType,'',raw)
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
def printList(list):
    for each in range(len(list)):
        print(f'{each+1}:{list[each]}')
def processing(realPath,path):
    print('-'*50)
    os.chdir(os.path.join(realPath,path))
    print(f"当前目录'{path}' 文件如下：")
    fileList=os.listdir()

    for each in range(len(fileList)):
        print(f"{each+1}:{fileList[each]}")

    print('-'*50)
    print(f"-- 目录'{path}' 选择状态：")
    selMode=selectFile(fileList,'【后续完整课程')
    print(selMode)

    fileListNew= list(compress(fileList,selMode))
    printList(fileListNew)
    print('-'*50)

    for each in fileListNew:
        realName=getRealName(each,'【后续完整课程必加微信：kaoyan800，完整课程福利更新QQ群：651077908】')
        os.rename(each,realName)
    os.chdir(os.pardir)
def autoClear(realPath,path,strs):
    os.chdir(os.path.join(realPath,path))
    print(f"当前目录'{path}' 文件如下：")
    fileList=os.listdir()

    for each in range(len(fileList)):
        print(f"{each+1}:{fileList[each]}")

    print('-'*50)
    print(f"-- 目录'{path}' 选择状态：")
    selMode=selectFile(fileList,strs)
    print(selMode)

    fileListNew= list(compress(fileList,selMode))
    printList(fileListNew)
    print('-'*50)

    for each in fileListNew:
        realName=getRealName(each,'【后续完整课程必加微信：kaoyan800，完整课程福利更新QQ群：651077908】')
        os.remove(each)


if __name__ == "__main__":
    realPath=os.path.abspath('.')
    for each in list(os.walk('.')):
        path,content,files=each[0],each[1],each[2]
        # printList(content+files)
        # processing(realPath,path)
        autoClear(realPath,path,'Auto')
    print('-'*50) 