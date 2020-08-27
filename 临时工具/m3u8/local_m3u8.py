import re
import os
from os import path
import m3u8
from Crypto.Cipher import AES
from glob import glob

def readM3u8(mFile):
    # 读取相对文件夹地址，文件名，文件数量
    with open(mFile,"r")as f:
        pathRaw=f.readlines()[-2]
        a=pathRaw.split('/')
        dirs,files=a[-2],a[-1]

        fileRaw=files.split('\n')[0]
        nums=re.search('\d+$',fileRaw).group()
        files=re.sub(nums,'',fileRaw)
        # print(a)
        print(dirs,files,nums)
def getKey(kPath):
    with open(kPath,'r')as f:
        k0=f.read().encode('utf-8')
        print(k0)
        return k0

def getSprtor(key,mode=AES.MODE_CBC):
    sprytor=AES.new(key,mode)
    return sprytor
def reLink(mfile):
    # 返回密匙路径，输出文件名，重定向的文件名
    fileName=re.sub(' .*\.','.',mfile)
    outName=fileName[:-4]+'mp4'
    newMfileName=fileName[:-5]+'N.m3u8'
    with open(mfile,'r')as f:
        strRaw=f.read()   
        print(strRaw)
        cachePath=re.sub(r"\\",'/',realPath)
        strChange=re.sub("/storage/emulated/0/Quark/Download",cachePath,strRaw)
        kPath = re.findall(r'URI="(.*)"', strChange)[0]
        newMfile=os.path.join('mFiles/',newMfileName)
        
        if mfile[-6]=='N'or path.exists(newMfile):

            newMfile=False
            print("已存在重定向文件")
        else:
            with open(newMfile,'w',encoding='utf-8')as fn:
                fn.write(strChange)
            print("重定向的.m3u8文件已创建")
        return kPath,outName,newMfile
def creatDirs(*args):
    for each in args:
        try:
            os.mkdir(each)
        except:
            pass
if __name__ == "__main__":
    mfileName='222.m3u8'

    realPath=os.path.abspath(".")
    # realPath=os.path.join(realPath,"临时工具\m3u8")
    os.chdir(realPath)
    creatDirs('mFiles','Videos')
    mflists=glob(os.path.join(realPath,'*.m3u8'))
    for mfileName in mflists:
        
        kPath,outName,newM=reLink(mfileName)
        if newM==False:
            continue
        else:
        
            # 获得解密密匙
            k0=getKey(kPath)
            sprytor=getSprtor(k0)
            # 获得ts链接
            m_obj=m3u8.load(newM)
            tsLists=[]
            for i,seg in enumerate(m_obj.segments):
                tsLists.append(seg.uri)
            print(tsLists)

            for tsLink in tsLists:
                tsName=tsLink.split("/")[-1]+'.ts'
                print("正在下载：" + tsName)
                if os.path.exists(tsLink):
                    with open(tsLink,'rb')as tsfile:
                        tsCon=tsfile.read()
                    # tsCon = requests.get(ts).content
                    # 密文长度不为16的倍数，则添加b"0"直到长度为16的倍数
                    while len(tsCon) % 16 != 0:
                        tsCon += b"0"
                    print("正在解密：" + tsName)
                    outFile=os.path.join('Videos/',outName)

                    with open(outFile,'ab')as vf:
                        vf.write(sprytor.decrypt(tsCon))
                else:
                    print(f'找不到链接,{outName} 视频生成已终止')
                    continue
