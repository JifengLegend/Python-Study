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




#保存文件
def saveImg(title,src):
    title=f'./{folderName}/'+title+'.jpg'
    with open(title,'wb')as f:
        f.write(src)










if __name__ == "__main__":
    homePageIndex='shenmengyao'
    #8/8 10346失败
    urlin = f'https://www.meitulu.com/t/{homePageIndex}/'
    webtext=openWeb(urlin)
    webtext=decodeWeb(webtext)
    #创建主目录
    moderName0=re.search(r'模特：.*</a>',webtext)
    moderName=re.findall(r'>(.*?)<',moderName0.group())
    moderName=moderName[0]+'合集'
    moderName=re.sub(r'\\',r'-',moderName)
    os.mkdir(moderName)
    os.chdir(moderName)
    IndexNameList=[]
    IndexTextList = re.findall(r'<li>\n.*', webtext)
    for each in IndexTextList:
        IndexName=re.findall(r'href="https://www.meitulu.com/item/(\d+).html"',each)
        IndexNameList.append(IndexName[0])
    IndexNum=len(IndexNameList)
    IndexNumNow=1
    for each in IndexNameList:
        print(f'{IndexNumNow}/{IndexNum}\t{each}')
        IndexNumNow+=1
        indexName = each
        urlin=f'https://www.meitulu.com/item/{indexName}.html'
        webtext=openWeb(urlin)
        webtext=decodeWeb(webtext)

        titleName=re.findall(r'<h1>(.*)</h1>',webtext)
        # 创建保存目录
        folderName = titleName[0]
        folderName =re.sub(r'\/', r'-', folderName)
        folderName = re.sub(r' $', '', folderName)
        if os.path.exists(folderName)==1:
            continue
        else:
            os.mkdir(folderName)

        a0=re.findall(r'content_img.*',webtext)
        matchtext=re.finditer(r'content_img.*',webtext)

        a1=re.findall(r'图片数量： (\d+) 张',webtext)
        try:
            n = int(a1[0])
        except IndexError:
            print(f'--{indexName} 匹配失败')
            continue

        x = 1
        i=1
        for each in range(1,n+1):
            print(f'\t{i}/{each}/{n}')
            newSrc=f'https://mtl.gzhuibei.com/images/img/{indexName}/{x}.jpg'

            title=indexName+'-'+str(x)
            x += 1
            try:
                newSrc=openWeb(newSrc)
                saveImg(title,newSrc)
            except(urllib.error.HTTPError)as reason:
                print('----图片访问失败')
                continue
            i+=1
        print(f'--获取完成,图片存放在{moderName}')


