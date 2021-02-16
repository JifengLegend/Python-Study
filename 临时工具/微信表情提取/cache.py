# import urllib.request   
# import re
# import os
# import shutil

# def chRec():
#     absPath=__file__ 
#     recPath=absPath[:absPath.rfind("\\")]
#     os.chdir(recPath)

# #打开网页链接
# def openWeb(urlin):
#     #获取链接请求
#     req=urllib.request.Request(urlin)
#     req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36 Edg/81.0.416.45')
#     response=urllib.request.urlopen(req)
#         #response此时可以执行的操作
#             #response.geturl()    获取当前链接
#             #response.info()    获取链接head信息
#             #response.getcode()    获取http状态
#     htmlbyte=response.read()
#     #读取二进制网页
#     return htmlbyte
#     #按着meta中说明的utf-8格式进行解码
# def decodeWeb(htmlbyte):
#     htmlmain=htmlbyte.decode('utf-8')
#     return htmlmain




# #保存文件
# def saveImg(title,src):
#     title=f'./Pics/{title}.gif'
#     with open(title,'wb')as f:
#         f.write(src)

# if __name__ == "__main__":
#     chRec()

#     urlin='https://mp.weixin.qq.com/cgi-bin/getimgdata?token=928669827&msgid=500000032&mode=small&source=&fileId=0&ow=-1'
#     src=openWeb(urlin)
#     print(src)
#     webtext=decodeWeb(src)

#     saveImg('真棒',src)

