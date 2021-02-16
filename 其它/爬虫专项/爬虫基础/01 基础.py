import urllib.request
# 访问url链接，并存储为response对象
response = urllib.request.urlopen("http://www.baidu.com")
# 读取respose对象为二进制文本
html=response.read()
# 解码为utf-8格式
html=html.decode('utf-8')
print(html)