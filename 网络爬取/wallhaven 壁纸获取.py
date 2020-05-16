import urllib.request   
import re
import os

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
folderName='img2'
#os.mkdir(folderName)

#保存文件
def saveImg(title,src):
    title=f'./{folderName}/'+title+'.jpg'
    with open(title,'wb')as f:
        f.write(src)










if __name__ == "__main__":
    urlin='https://588ku.com/sheyingtu/0-82-default-0-1/?hd=85'
    urlin1='http://placekitten.com/g/500/600'
    urlin2='http://bpic.588ku.com/back_list_pic/19/10/22/0be968e6d311a49e4abeabc43ca0e111.jpg!/fh/300/quality/90/unsharp/true/compress/true'
    urlin3='https://wallhaven.cc/toplist'
    urlin4='https://wallhaven.cc/random'
    urlin5='https://wallhaven.cc/search?categories=001&purity=100&sorting=random&order=desc'
    
    urlin6='https://wallhaven.cc/search?categories=001&purity=010&sorting=random&order=desc'
    webtext=openWeb(urlin6)
    webtext=decodeWeb(webtext)
    


    matchtext=re.finditer(r'class="preview".*?</a>',webtext)
    
    
    a=[]
    for each in matchtext:     
        keyword=re.sub(r'.*\/(.+?)".*',r'\1',each.group())
        keystart=keyword[0:2]
        
        title=keyword
        
        a.append([keystart,keyword])
        
        
    
    x=1
    i=1
    n=len(a)
    for each in a:        
        print(f'{i}/{x}/{n}\t\t{each[0]}\t{each[1]}')
        newSrc=f'https://w.wallhaven.cc/full/{each[0]}/wallhaven-{each[1]}.jpg'
        x+=1
        try:
            newSrc=openWeb(newSrc)
            saveImg(each[1],newSrc)
        except(urllib.error.HTTPError)as reason:
            print('----图片访问失败')
            continue
        i+=1


