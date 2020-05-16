# encoding:utf-8

import requests
import base64
import time

'''
通用文字识别
'''

request_url = "https://aip.baidubce.com/rest/2.0/solution/v1/form_ocr/request"
# 二进制方式打开图片文件
f = open('cache.png', 'rb')
img = base64.b64encode(f.read())

params = {"image":img}

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
    print (response.json())


ids={'request_id':response.json()['result'][0]['request_id']}
getFormUrl='https://aip.baidubce.com/rest/2.0/solution/v1/form_ocr/get_request_result'
getFormUrl = getFormUrl + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}

time.sleep(3)
response2 = requests.post(getFormUrl, data=ids, headers=headers)
if response2:
    print (response2.json()['result']['result_data'])
