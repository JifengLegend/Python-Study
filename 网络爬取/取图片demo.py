import urllib.request   
import re
import os
def chRec():
    absPath=__file__ 
    recPath=absPath[:absPath.rfind("\\")]
    os.chdir(recPath)
#打开网页链接
def openWeb(urlin):
    #获取链接请求
    req=urllib.request.Request(urlin)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36 Edg/81.0.416.45')
    response=urllib.request.urlopen(req)
        #response此时可以执行的操作
            #response.geturl()    获取当前链接
            #response.info()    获取链接head信息
            #response.getcode()    获取http状态
    htmlbyte=response.read()
    #读取二进制网页
    return htmlbyte
    #按着meta中说明的utf-8格式进行解码
def decodeWeb(htmlbyte):
    htmlmain=htmlbyte.decode('utf-8')
    return htmlmain


#创建保存目录
# os.mkdir('imgcache')
#保存文件
def saveImg(title,src):
    title='./imgcache/'+title+'.jpg'
    with open(title,'wb')as f:
        f.write(src)

def getDirect():
    








if __name__ == "__main__":
    chRec()
    urlin='https://588ku.com/sheyingtu/0-82-default-0-1/?hd=85'
    urlin1='http://placekitten.com/g/500/600'
    urlin2='http://bpic.588ku.com/back_list_pic/19/10/22/0be968e6d311a49e4abeabc43ca0e111.jpg!/fh/300/quality/90/unsharp/true/compress/true'
    urlin3='https://mp.weixin.qq.com/cgi-bin/getimgdata?token=928669827&msgid=500000031&mode=small&source=&fileId=0&ow=-1'
    
    webtext=openWeb(urlin3)
    webtext=decodeWeb(webtext)
    matchtext=re.finditer(r'class="lazy".*?</div>',webtext)
    for each in matchtext:
        title=re.sub(r'.*title="(.+)".*',r'\1',each.group())
        src=re.sub(r'.*data-original="(.+?)".*',r'\1',each.group())
        src='http:'+src
        if len(src)>200:
            break
        print(title)
        print(src)
        src=openWeb(src)
        os.mkdir('imgcache')
        saveImg(title,src)
    # saveImg('cat',webtext)

