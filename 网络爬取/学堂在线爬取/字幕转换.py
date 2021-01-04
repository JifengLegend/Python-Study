import json
import math
def timePro(t1):
    t1/=1000
    hour=math.floor(t1)//3600
    minute=(math.floor(t1)-hour*3600)//60
    sec=math.floor(t1)-hour*3600-minute*60
    miniSec=int(math.modf(t1)[0]*100)
    return f'{hour}:{minute}:{sec}.{miniSec}'

with open('./学堂在线爬取/2.txt','r')as f:
    raw=f.read()
    a=json.loads(raw)
    # print(a['start'],a['end'],a['text'])
    result=''
    for num,content in enumerate(a['start']):
        result+=f"{num}\n{timePro(a['start'][num])}-->{timePro(a['end'][num])}\n{a['text'][num]}\n\n"
    print(result)

with open('./学堂在线爬取/2.srt','w',encoding='utf-8')as f:
    f.write(result)

