import requests
import base64
import webbrowser as web
# 获取token
aid='YE8XoIIXzN3Z4NGsl8DV5c2r'
asd='rojyCx5SKy9FRVtCwHwSKkznUBtHlt0v'
host = f'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={aid}&client_secret={asd}'
response = requests.get(host)
if response:
    access_token = response.json()['access_token']
    print(access_token)

ids={'request_id':'19698398_1731526','request_type':'json'}
getFormUrl='https://aip.baidubce.com/rest/2.0/solution/v1/form_ocr/get_request_result'
getFormUrl = getFormUrl + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response2 = requests.post(getFormUrl, data=ids, headers=headers)
if response2:
    downloadUrl=response2.json()['result']['result_data']
    print (downloadUrl)
    web.open(downloadUrl)
