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
    # homePageIndex='sugar-xiaotianxincc'
    # urlin = f'https://www.meitulu.com/t/{homePageIndex}/'
    # webtext=openWeb(urlin)
    # webtext=decodeWeb(webtext)
    # #创建主目录
    # moderName0=re.search(r'模特：.*</a>',webtext)
    # moderName=re.findall(r'>(.*)<',moderName0.group())
    # moderName=moderName[0]+'合集'
    # os.mkdir(moderName)
    # os.chdir('杨晨晨合集')

    # IndexTextList = re.findall(r'<li>\n.*', webtext)
    # for each in IndexTextList:
    #     IndexName=re.findall(r'href="https://www.meitulu.com/item/(\d+).html"',each)
    #     IndexNameList.append(IndexName[0])
    IndexNameList = ["18397","19392","19395","19460","20671","20654","9686","15041","11548","14305","7949","14485","14695","15258","18993","18755","18899","16154","14666","19734","15906","18225","21020","20533","20654","20646","20784","19505"]
    #IndexNameList=['18444', '18439', '18436', '18431', '18175', '18147', '18144', '18140', '18136', '18132', '18128', '18122', '18117', '18110', '18109', '18107', '18102', '17956', '17757', '17753', '17661', '17650', '17279', '17278', '17264', '17250', '17242', '17161', '16813', '16759', '16603', '16597', '16586', '16581', '16461', '16449', '16443', '16274', '16070', '16064', '15963', '15953', '15892', '15783', '15775', '15582', '15563', '15552', '15534', '15376', '15239', '15233', '15227', '15222', '15216', '14686', '14480', '14363', '14325', '14186','14110', '13781', '13732', '13660', '13560', '13491', '12967', '12921', '12854', '12804', '12719', '12716', '12617', '12212', '12210', '12208', '11825', '11738', '11539', '11523', '11448', '11298', '10683', '10573', '10548', '10477', '10424', '10418', '10386', '10355', '10182', '10175', '10136', '10085', '10049', '9792', '9699', '9692', '9664', '9396', '9388', '9366', '9364', '9363', '9168', '9015', '8950', '8931', '8911', '8739', '8700', '8661', '8652', '8650', '8255', '8115', '8097', '8096', '8094', '7962','7923', '7918', '7911', '7910', '7702', '7456', '7259', '6712', '6694', '6691']
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
        folderName = re.sub(r'\/', r'-', folderName)
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
        print(f'--获取完成')


