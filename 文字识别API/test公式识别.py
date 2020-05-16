# encoding:utf-8

import requests
import base64

'''
通用文字识别
'''

request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/formula"
# 二进制方式打开图片文件
f = open('cache.png', 'rb')
img = base64.b64encode(f.read())

params = {"image":img,'disp_formula':True}

# 获取token
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=YE8XoIIXzN3Z4NGsl8DV5c2r&client_secret=rojyCx5SKy9FRVtCwHwSKkznUBtHlt0v'
response = requests.get(host)
if response:
    access_token = response.json()['access_token']
    print(access_token)


request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print(response.json())
    text=''
    for each in response.json()['words_result']:
        text+=each["words"]+'\n'
    print(text)
    
    # print(response.json()['+words'])
    
