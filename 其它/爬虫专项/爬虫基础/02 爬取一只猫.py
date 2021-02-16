# paacekitten.com
import urllib.request
import os
# Method 1

# response = urllib.request.urlopen('http://placekitten.com/g/500/600')
# cat_image = response.read()

# Method 2
req=urllib.request.Request('http://placekitten.com/g/600/600')
response=urllib.request.urlopen(req)
cat_image = response.read()

'''
其中，response对象，有几个方法
response.geturl() 获取url地址
response.info（） 获取响应信息
response.getcode() 获取响应状态
'''


def chRec():
    absPath=__file__
    recPath=absPath[:absPath.rfind("\\")]
    os.chdir(recPath)
chRec()
 
with open('./cat.jpg','wb')as f:
    f.write(cat_image)