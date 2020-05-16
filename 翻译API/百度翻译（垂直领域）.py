#鐧惧害閫氱敤缈昏瘧API,涓嶅寘鍚瘝鍏搞€乼ts璇煶鍚堟垚绛夎祫婧愶紝濡傛湁鐩稿叧闇€姹傝鑱旂郴translate_api@baidu.com
# coding=utf-8

import http.client
import hashlib
import urllib
import random
import json

appid = '20200406000412945'  # 濉啓浣犵殑appid
secretKey = 'pZCsP6EUTkXG0lLwOYAS'  # 濉啓浣犵殑瀵嗛挜

httpClient = None
myurl = '/api/trans/vip/fieldtranslate'

fromLang = 'zh'   #鍘熸枃璇
toLang = 'en'   #璇戞枃璇
salt = random.randint(32768, 65536)
q= '电源接地'
domain = 'medicine' # electronics mechanics medicine
sign = appid + q + str(salt) + domain + secretKey
sign = hashlib.md5(sign.encode()).hexdigest()
myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + '&domain=' + domain + str(
salt) + '&sign=' + sign

try:
    httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
    httpClient.request('GET', myurl)

    # response鏄疕TTPResponse瀵硅薄
    response = httpClient.getresponse()
    result_all = response.read().decode("utf-8")
    result = json.loads(result_all)

    print (result)

except Exception as e:
    print (e)
finally:
    if httpClient:
        httpClient.close()