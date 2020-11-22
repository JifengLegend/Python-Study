import re
import os

def chRec():
    recPath=__file__
    recPath=re.sub(r'[A-z_]+\.py','',recPath)
    print(recPath)
    os.chdir(recPath)
class KeyInfo():
    def __init__(self,strs):
        self.infoList=strs.split('\n')
        self.name=self.infoList[0]
        self.name=self.name[1:-1]
        self.infoTable={}
        for num,each in enumerate(self.infoList[1:]):
            if each!='':
                c=each.split('=')
                self.infoTable[c[0]]=c[1]
        self.delInfo('up')
        self.delInfo('down')
        self.delInfo('left')
        self.delInfo('right')
        self.delInfo('center')
    # def readInfo(self,tarStr):
    #     count=0
    #     cache=''
    #     for each,num in enumerate(self.infoList):
    #         if re.search(tarStr,each)!=None:
    #             cache=each
    #             count+=1
    #     if count==0:
    #         print('无匹配')
            
    #     else:
    #         print(each)
    def readInfo(self,tarSts):
        tarSts=tarSts.upper()
        if tarSts in self.infoTable:
            # print(tarSts+'='+self.infoTable[tarSts])
            return 1
        else:
            return 0
    def changeInfo(self,tar,val):
        tar=tar.upper()
        if len(val)>=2:
            val=val.upper()
        if self.readInfo(tar):
            self.infoTable[tar]=val
        else:
            self.infoTable[tar]=val
        # self.com()
    def delInfo(self,tar):
        tar=tar.upper()
        if tar in self.infoTable:
            self.infoTable.pop(tar)
    def com(self):
        self.text=f'[{self.name}]\n'
        for each in self.infoTable:
            self.text+=(each+'='+self.infoTable[each]+'\n')
        self.text=self.text[:-1]
        # print(self.text)
        return self.text


def getSen(strs,target):
    if len(target)>=2:
        target=target.upper()
    target='CENTER='+target

    cache=re.search(target,strs)
    area=cache.span()
    tarAreaRaw=strs[area[0]-200:area[1]+80]
    tarArea=re.search('\[.*\](\n|.)*?\[',tarAreaRaw).group()[:-3]
    # print(re.search(tarArea,tarAreaRaw))
    
    # print(tarArea)
    return tarArea
    # print(tarAreaRaw)
def getArea(strs):
    global raw
    cache=strs.split('KEY')
    cache='KEY'+str(int(cache[1])+1)
    return (re.search(strs,raw).span()[0]-1,re.search(cache,raw).span()[0]-3)
def keyModel(keyFcn):
    def inner(a):
        global raw,key
        key=KeyInfo(getSen(raw,a))
        area=getArea(key.name)
        ret =keyFcn(a)
        key.changeInfo('center',a)
        raw=raw[:area[0]]+key.com()+raw[area[1]:]
        print(key.com())
        return ret
    return inner
def keyModelp(keyFcn):
    def inner(a):
        global raw,key
        key=KeyInfo(getSen(raw,a))
        area=getArea(key.name)
        ret =keyFcn(a)
        raw=raw[:area[0]]+key.com()+raw[area[1]:]
        print(key.com())
        return ret
    return inner

@keyModel
def keyA(a):
    key.changeInfo('up','f47')
    key.changeInfo('left','~')
    key.changeInfo('down','A')
@keyModel
def keyH(a):
    key.changeInfo('up','&')
    key.changeInfo('left','f51')
    key.changeInfo('right','f52')
@keyModel
def keyJ(a):
    key.changeInfo('up','*')
    key.changeInfo('left','f51')
    key.changeInfo('right','f52')
@keyModel
def keyK(a):
    global lan
    key.changeInfo('left','f51')
    key.changeInfo('right','f52')
    if lan=='en':
        key.changeInfo('up','(')
    else:
        key.changeInfo('up','（')

    
@keyModel
def keyL(a):
    global lan
    key.changeInfo('left','f51')
    key.changeInfo('right','f52')
    if lan=='en':
        key.changeInfo('up',')')
    else:
        key.changeInfo('up','）')
@keyModel
def keyZ(a):
    global lan
    if lan=='en':
        key.changeInfo('up','!')
        key.changeInfo('down','f47')
    else:
        key.changeInfo('up','！')
        key.changeInfo('down','f47')
@keyModel
def keyX(a):
    key.changeInfo('up','f44')
    key.changeInfo('down','/')
@keyModel
def keyC(a):
    global lan
    if lan=='en':
        key.changeInfo('up','f45')
        key.changeInfo('down','-')
    else:
        key.changeInfo('up','f47')
        key.changeInfo('down','-')
@keyModel
def keyV(a):
    key.changeInfo('up','f46')
    key.changeInfo('left','_')
    key.changeInfo('down','f76')

@keyModel
def keyB(a):
    global lan
    key.changeInfo('left','f51')
    key.changeInfo('right','f52')
    key.changeInfo('down','f47')
    if lan=='en':
        key.changeInfo('up',':')
    else:
        key.changeInfo('up','：')
@keyModel
def keyN(a):
    global lan
    key.changeInfo('up','f42')
    key.changeInfo('left','f51')
    key.changeInfo('right','f52')
    if lan=='en':
        key.changeInfo('down',';')
    else:
        key.changeInfo('down','；')
@keyModel
def keyM(a):
    global lan
    key.changeInfo('left','f51')
    key.changeInfo('right','f52')
    key.changeInfo('down','f43')
    if lan=='en':
        key.changeInfo('up','?')

    else:
        key.changeInfo('up','？')
@keyModel
def keySpace(a):
    global lan
    key.changeInfo('left','f51')
    key.changeInfo('right','f52')
    key.changeInfo('hold','f72')
    if lan=='en':
        key.changeInfo('up','f15')
    else:
        key.changeInfo('up','f16')
@keyModel
def keyDel(a):
    key.changeInfo('left','f40')
    key.changeInfo('up','f48')
    key.changeInfo('down','f37')
@keyModel
def keyNum(a):
    key.changeInfo('up','f1')
@keyModelp
def keyEmj(a):
    key.changeInfo('up','f7')
    key.changeInfo('center','\'')
    key.delInfo('hold')

@keyModelp
def keyLeft(a):
    global lan
    key.changeInfo('hold','f77')
    key.changeInfo('center','\'')
    if lan=='en':
        key.changeInfo('up',',')
    else:
        key.changeInfo('up','，')
@keyModelp
def keyRight(a):
    global lan
    if lan=='en':
        key.changeInfo('up',',')
        key.changeInfo('center','.')
    else:
        key.changeInfo('up','，')
        key.changeInfo('center','。')

# 单独配置
@keyModel
def adA(a):
    key.changeInfo('fore_style','611,411,501')
    key.changeInfo('pos_type','1,2,3')
@keyModel
def adZ(a):
    key.changeInfo('fore_style','620,428')
@keyModel
def adB(a):
    key.changeInfo('fore_style','624,424')
@keyModel
def adEmj(a):
    key.changeInfo('fore_style','1704')
@keyModel
def adLeft(a):
    global lan
    if lan=='en':
        key.changeInfo('fore_style','1710')
    else:
        key.changeInfo('fore_style','1711')
if __name__ == "__main__":
    chRec()
    global lan
    lan=input('请输入该皮肤文件为 英文（1） 还是 中文（2）？\n')
    lan='en' if lan!='2' else 'zh'
    with open('raw.ini','r',encoding='utf-8')as f:
        # print(f.read())
        global raw
        raw=f.read()
        raw=re.sub('INFO=微信公众号.*','INFO=微信公众号',raw)
        # 自定义段
        if lan=='en':
            adA('a')
            adB('b')
            adZ('z')

        # 基本段
        keyA('a')
        keyH('h')
        keyJ('j')
        keyK('k')
        keyL('l')
        keyZ('z')
        keyX('x')
        keyC('c')
        keyV('v')
        keyB('b')
        keyN('n')
        keyM('m')

        keySpace('f38')
        keyDel('f36')
        keyNum('f6')




        # print(re.search('KEY38',raw).span()[0]-1,re.search("KEY39",raw).span()[0]-31)
    with open('result.ini','w',encoding='utf-8')as f:
        f.write(raw)