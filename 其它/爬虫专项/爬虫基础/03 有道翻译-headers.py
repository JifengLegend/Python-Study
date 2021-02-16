import urllib.request
import urllib.parse

url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
# 重新编写data
data={}

data['type']='AUTO'
data['i']='i am a cat'
data['doctype']='json'
data['xmlVersion']='1.6'
data['keyfrom']='fanyi.web'
data['ue']='UTF-8'
data['typoResult']='true'
# 使用urlencode 编码 data
data=urllib.parse.urlencode(data).encode('utf-8')

# Method 1

# head={}
# head['User-Agent'] ='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.53'
# req=urllib.request.Request(url,data,head)

# Method 2

req=urllib.request.Request(url,data)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.53')

response = urllib.request.urlopen(req)
html=response.read().decode('utf-8')

print(html)

