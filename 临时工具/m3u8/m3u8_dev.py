import sys
import os
from glob import glob

def getPath(arg_dir):
    if os.path.isdir(arg_dir):
        return arg_dir
    elif os.path.isabs(arg_dir):
        return arg_dir
    else:
        return False
def getSortTs(userPath):
    tsList=glob(os.path.join(userPath,'.*ts'))
    print(tsList)
    boxer=[]
    for ts in tsList:
        if os.path.exists(ts):
            file=os.path.splitext(os.path.basename(ts))
            boxer.append(int(file))
    boxer.sort()
    print(boxer)
    return boxer

def convertVideo(boxer,fileName):
    tem=[]
    for ts in boxer:
        tem.append(str(ts)+".ts")
    cmdStr='+'.jion(tem)
    execStr="copy /b"+cmdStr+" "+fileName
    print(execStr)
    # os.system(ex)
if __name__ == "__main__":
    argvLen=len(sys.argv)
    if argvLen==3:
        oDir,fileName=sys.argv[1:]
        print(oDir,fileName)
        userPath=getPath(oDir)
        if not userPath:
            print('当前地址不正确')
        else:
            if os.path.exists(os.path.join(userPath,fileName)):
                print("目标已存在，程序停止")
                exit(0)
            os.chdir(userPath)
            boxer=getSortTs(userPath)
            # convertVideo(boxer,fileName)
    else:
        print("参数个数有误")
        
