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

def saveMusic(recLink,recName):
    title=f'./{folderName}/{recName}'
    with open(title,'wb')as f:
        f.write(recLink)










if __name__ == "__main__":
    while 1:
        WebContent = input('请输入网址：')
        #indexName='YomTNwFNmgKEWXtHT2nYSA'
        # <a href="http://mobileoc.music.tc.qq.com/M800004ANAbn4Og7jd.mp3?guid=ghmusic&amp;vkey=8D3D95B87BC614A4D9356BCDC94F693199E357CF52A0338B8F55D9D50B3FB2319C570BD6868FB2FBD76A7D6ED3DF3FD636A35981D395078B&amp;uin=0&amp;fromtag=143" id="down_a" download="对不起 我只是个宅男 - 封茗囧菌.mp3" target="_blank" style="margin-left: 16px;">右键另存为或者点击我</a>
        # recLink="http://mobileoc.music.tc.qq.com/M800004ANAbn4Og7jd.mp3?guid=ghmusic&amp;vkey=8D3D95B87BC614A4D9356BCDC94F693199E357CF52A0338B8F55D9D50B3FB2319C570BD6868FB2FBD76A7D6ED3DF3FD636A35981D395078B&amp;uin=0&amp;fromtag=143"
        # recName="对不起 我只是个宅男 - 封茗囧菌.mp3"
        
        recLink=re.sub(r'.*href="(.*?)".*',r'\1',WebContent)
        recName=re.sub(r'.*download="(.*?)".*',r'\1',WebContent)



        # urlin=f'{recLink}'
        # webtext=openWeb(urlin)
        # webtext=decodeWeb(webtext)

        # 创建保存目录
        folderName = "Music cache"

        try:
            shutil.rmtree(folderName)
            print('原始文件已经清除')
        except FileNotFoundError:
            pass
        os.mkdir(folderName)
        print('--'+folderName)

        #获取连接
        src=openWeb(recLink)
        saveMusic(src,recName)
        print(f'--获取音乐完成,图片存放在文件夹')
        
