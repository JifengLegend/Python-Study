import re
import os
import os.path

def readM3u8(mFile):
    with open(mFile,"r")as f:
        pathRaw=f.readlines()[-2]
        a=pathRaw.split('/')
        dirs,files=a[-2],a[-1]

        fileRaw=files.split('\n')[0]
        nums=re.search('\d+$',fileRaw).group()
        files=re.sub(nums,'',fileRaw)
        # print(a)
        print(dirs,files,nums)
        return dirs,files,int(nums)
if __name__ == "__main__":
    fileName='222.m3u8'
    dirs,files,nums=readM3u8(fileName)
    if os.path.exists(dirs):
        os.chdir(dirs)
        cmdStr=''
        for each in range(nums+1):
            cmdStr+=files+str(each)+"+"
        cmdStr=cmdStr[:-1]

        outName=fileName[:-4]+"ts"
        outName=re.sub(' .*\.','.',outName)
        execStr="copy /b "+cmdStr+" "+outName
        print(execStr)
        # os.system(execStr)