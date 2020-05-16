import urllib.request
import random

url = 'http://www.4399.com'
iplist=['58.52.201.117:8080','36.248.132.23:9999','1.197.204.8:9999']
prosy_support = urllib.request.ProxyHandler({'http': random.choice(iplist)})

opener = urllib.request.build_opener(prosy_support)
opener.add_handler=[('User-Agent',
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36')]

urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')
print(html)
