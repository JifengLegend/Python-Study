import urllib.request   
import re
import os
import shutil

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
    title=f'./{folderName}/{title}.jpg'
    with open(title,'wb')as f:
        f.write(src)










if __name__ == "__main__":
    while 1:
        indexName = input('请输入网址：')
        #indexName='YomTNwFNmgKEWXtHT2nYSA'
        urlin=f'{indexName}'
        webtext=openWeb(urlin)
        webtext=decodeWeb(webtext)

        titleName=re.findall(r'<h2.*>((.|\n)*)</h2>',webtext)
        titleName=re.sub(r'( |\n)', '', titleName[0][0])
        # 创建保存目录
        folderName = titleName
        folderName=re.sub(r' $','',folderName)
        folderName=re.sub(r'\|','-',folderName)
        try:
            shutil.rmtree(folderName)
            print('原始文件已经清除')
        except FileNotFoundError:
            pass
        os.mkdir(folderName)
        print('--'+folderName)

        #获取连接
        #
        srcText=re.search(r'<p style="text-align(.|\n)*?</div>',webtext)
        srcList=re.findall(r'src="(.*?)"',srcText.group())
        n=len(srcList)
        i=1
        for each in range(0,n):
            print(f'{i}/{each+1}/{n}')
            newSrc=srcList[each]
            title=indexName+'-'+str(each+1)
            try:
                newSrc=openWeb(newSrc)
                saveImg(str(each+1),newSrc)
            except(urllib.error.HTTPError)as reason:
                print('----图片访问失败')
                continue
            i+=1
        print(f'--获取完成,图片存放在"{folderName}"文件夹')
        



