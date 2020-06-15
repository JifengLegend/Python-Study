#百度通用翻译API,不包含词典、tts语音合成等资源，如有相关需求请联系translate_api@baidu.com
# coding=utf-8

import http.client
import hashlib
import urllib
import random
import json
def BaiduTrans(source):
    appid = '20200406000412945'  # 填写你的appid
    secretKey = 'pZCsP6EUTkXG0lLwOYAS'  # 填写你的密钥

    httpClient = None
    # myurl = '/api/trans/vip/translate/fieldtranslate'
    myurl ='/api/trans/vip/fieldtranslate'

    fromLang = 'zh'   #原文语种
    toLang = 'en'   #译文语种
    salt = random.randint(32768, 65536)
    q= source
    domain = 'medicine' # electronics mechanics medicine
    sign = appid + q + str(salt) + domain +secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
    salt) + '&sign=' + sign

    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)

        # response是HTTPResponse对象
        response = httpClient.getresponse()
        result_all = response.read().decode("utf-8")
        result = json.loads(result_all)
        print(result)
        # print (result['trans_result'][0]["dst"])

    except Exception as e:
        print (e)
    finally:
        if httpClient:
            httpClient.close()
    print(result)
    return result['trans_result'][0]["dst"]
if __name__ == "__main__":
    a=BaiduTrans("苹果")
    print(a)