import urllib.request
import urllib.parse
import json
import time

while 1:
    inputWord = input('——请输入要翻译的文本：')
    if inputWord == '0':
        break

    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    data = {}
    data['i'] = inputWord
    data['from'] = 'AUTO'
    data['to'] = 'AUTO'
    data['smartresult'] = 'dict'
    data['client'] = 'fanyideskweb'
    data['salt'] = '15811605959637'
    data['sign'] = '2b3d3c8b01002be2faf7f08a5eb95dab'
    data['ts'] = '1581160595963'
    data['bv'] = '7bcd9ea3ff9b319782c2a557acee9179'
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'FY_BY_REALTlME'
    data = urllib.parse.urlencode(data).encode('utf-8')

    req = urllib.request.Request(url, data)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36')

    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    target = json.loads(html)
    result = target['translateResult'][0][0]['tgt']

    print('——翻译结果为：' + result + '\n进入下一次翻译了哦')
    time.sleep(3)
