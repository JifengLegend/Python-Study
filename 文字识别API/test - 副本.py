# encoding:utf-8
import requests

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=YE8XoIIXzN3Z4NGsl8DV5c2r&client_secret=rojyCx5SKy9FRVtCwHwSKkznUBtHlt0v'

response = requests.get(host)
if response:
    print(response.json()['access_token'])
