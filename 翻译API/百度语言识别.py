import http.client
import hashlib
import urllib
import random
import json

def getLanguage(raw='apple',\
    app_id='20200406000412945',secret_Key = 'pZCsP6EUTkXG0lLwOYAS',\
       ):
    '''
    返回一个翻译后的字符串\n
    raw:原文本\n
    to_lang:目标翻译语言，默认为 翻译为中文\n
    from_lang:指定原文本语言，默认为 自动检测\n
    appid/key:我本人的账号密码\n
    '''

    appid = app_id # appid
    secretKey = secret_Key  # 密码

    httpClient = None
    myurl = '/api/trans/vip/language'


    salt = random.randint(32768, 65536)
    q= raw
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&salt=' + str(
    salt) + '&sign=' + sign

    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)

        # response是HTTPResponse对象
        response = httpClient.getresponse()
        result_all = response.read().decode("utf-8")
        result = json.loads(result_all)

        return result['data']['src']
    except Exception as e:
        print (e)
    finally:
        if httpClient:
            httpClient.close()

if __name__ == "__main__":
    print(getLanguage('我的'))