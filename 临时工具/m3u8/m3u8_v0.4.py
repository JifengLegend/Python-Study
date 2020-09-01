import re
import os
from os import path
import m3u8
from Crypto.Cipher import AES
from glob import glob

class Mfile:
    def __init__(self,mfileName):
        self.mfileName=mfileName
        self.reLink()        
        if self.newMFile:
            self.getLinks()
            if self.tor:                
                self.getTsfile()
            else:
                self.easyTsfile()

    def reLink(self):
        self.fileName=re.sub(' .*\.','.',self.mfileName)
        self.outName=self.fileName[:-4]+'mp4'
        newMfileName=self.fileName[:-5]+'N.m3u8'
        with open(self.mfileName)as f:
            strRaw=f.read()
            cachePath=re.sub(r'\\','/',realPath)        
            strChange=re.sub("/storage/emulated/0/Quark/Download",cachePath,strRaw)
            self.tor=self.getKey(strChange)

            self.newMFile=path.join(mfilesPath,newMfileName)
            if self.mfileName[-6]=='N'or path.exists(self.newMFile):
                self.newMFile=False
                print(f'已存在重定向文件{newMfileName}')
            else:
                with open(self.newMFile,'w',encoding='utf-8')as fn:
                    fn.write(strChange)
                    print(f'重定向的m文件已创建{newMfileName}')
    def getLinks(self):
        m_obj=m3u8.load(self.newMFile)
        self.tsLists=[]
        for i,seg in enumerate(m_obj.segments):
            self.tsLists.append(seg.uri)
        print(self.tsLists)
    def getTsfile(self):
        for tsLink in self.tsLists:
            tsName=tsLink.split("/")[-1]+'.ts'
            if path.exists(tsLink):
                with open(tsLink,'rb')as tsfile:
                    tsCon=tsfile.read()
                while len(tsCon) % 16 != 0:
                    tsCon+= b"0"
                print('正在解密： '+tsName)
                outfile=path.join(VideosPath,self.outName)
                with open(outfile,'ab')as fv:
                    fv.write(self.tor.decrypt(tsCon))
            else:
                print(f'找不到链接,{self.outName} 视频生成已终止')
                break
    def easyTsfile(self):
        for tsLink in self.tsLists:
            tsName=tsLink.split("/")[-1]+'.ts'
            if path.exists(tsLink):
                with open(tsLink,'rb')as tsfile:
                    tsCon=tsfile.read()
                
                print('正在合成： '+tsName)
                outfile=path.join(VideosPath,self.outName)
                with open(outfile,'ab')as fv:
                    fv.write(tsCon)
            else:
                print(f'找不到链接,{self.outName} 视频生成已终止')
                break    
    def getKey(self,strs):
        # 获得解密
        try:
            kPath = re.findall(r'URI="(.*)"', strs)[0]
            with open(kPath,'rb')as f:
                k0=f.read()
            print(k0)
            tor=AES.new(k0,AES.MODE_CBC)
        except:
            tor=False
        return tor

def creatDirs(*args):
    for each in args:
        try:
            os.mkdir(each)
        except:
            pass

if __name__ == "__main__":
    global realPath,mfilesPath,VideosPath
    realPath=path.abspath('.')
    # realPath=path.join(realPath,'临时工具\m3u8')
    os.chdir(realPath)
    creatDirs('mfiles','Videos')
    mfilesPath=path.join(realPath,'mfiles')
    VideosPath=path.join(realPath,'Videos')
    # print(mfilesPath,VideosPath)
    mflists=glob('*.m3u8')
    for mfileName in mflists:
        mfileNow=Mfile(mfileName)

    

