import re
import os
from os import path
import m3u8
from Crypto.Cipher import AES

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

def changeM3u8(mfiles,realPath):
    with open(mfiles,'r')as f:
        strRaw=f.read()   
        print(strRaw)     
        # strChange=re.sub(r'/storage/emulated/0/Quark/Download',realPath,strRaw)
        print(strChange)
if __name__ == "__main__":
    mfiles='222.m3u8'
    realPath=os.path.abspath('.')
    print("_"*50)
    print(realPath)
    realPath=os.path.join(realPath,"临时工具\m3u8")
    print(realPath)
    os.chdir(realPath)
    dirPath,files,nums=readM3u8("222.m3u8")
    
    with open(mfiles,'r')as f:
        strRaw=f.read()   
        print(strRaw)
        cachePath=re.sub(r"\\",'/',realPath)
        strChange=re.sub("/storage/emulated/0/Quark/Download",cachePath,strRaw)
        kPath = re.findall(r'URI="(.*)"', strChange)[0]
        print(kPath)
        with open(kPath,'rb')as fk:
            print(fk.read())
            k0=fk.read()
        print('-'*50)
        with open("333.m3u8",'w',encoding="utf-8")as fn:
            fn.write(strChange)
    
    # mObj=m3u8.load('333.m3u8')
    # for seg in mObj.segments:
    #     pass
    #     # print(seg.uri)
    m3u8_obj = m3u8.load("333.m3u8")
    ts_urls = []
    for i, seg in enumerate(m3u8_obj.segments):
        ts_urls.append(seg.uri)
    print(ts_urls)

    for ts in ts_urls:
        tsName=ts.split("/")[-1]+'.ts'
        print(tsName)
        print('_'*50)
        k0="f3df42e38c9e8fae".encode("utf-8")
        sprytor=AES.new(k0,AES.MODE_CBC)
        print(sprytor)

        print("正在下载：" + tsName)
        with open(ts,'rb')as tsfile:
            tsCon=tsfile.read()
        # tsCon = requests.get(ts).content
        # 密文长度不为16的倍数，则添加b"0"直到长度为16的倍数
        while len(tsCon) % 16 != 0:
            tsCon += b"0"

        print("正在解密：" + tsName)
        

        with open('111.mp4','ab')as vf:
            vf.write(sprytor.decrypt(tsCon))


