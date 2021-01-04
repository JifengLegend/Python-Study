import json,requests,time,math

def timePro(t1):
    t1/=1000
    hour=math.floor(t1)//3600
    minute=(math.floor(t1)-hour*3600)//60
    sec=math.floor(t1)-hour*3600-minute*60
    miniSec=int(math.modf(t1)[0]*100)
    return f'{hour}:{minute}:{sec}.{miniSec}'

cid = "4230532"
sign = "THU08081000447"

# 请求头 仅供参考
headers = { "xtbz": "xt" }
cookies = { "sessionid": "je1mjha9g5bhvrrfhshautbroy1m4vs8" }

# 章节信息
url_chapter = "https://www.xuetangx.com/api/v1/lms/learn/course/chapter?cid={}&sign={}".format(cid, sign)
time.sleep(0.2)
chapter = json.loads(requests.get(url_chapter,headers=headers,cookies=cookies).content)
# print(chapter)
## 第一章的第一节的所有小节
leaf_list = chapter['data']['course_chapter'][0]['section_leaf_list'][0]['leaf_list']
week_list=chapter['data']['course_chapter']
v_list=[]
v_name={}

for weekNum,eachWeek in enumerate(week_list):
    print(eachWeek['id'],eachWeek['name'])
    for sectionNum,eachSection in enumerate(eachWeek['section_leaf_list']):
        try:
            v_name={'link':eachSection['leaf_list'][0]['id'],'index':f'{weekNum+1}-{sectionNum+1}','name':eachSection['name']}
            v_list.append(v_name)
            # print(f"\t{eachSection['leaf_list'][0]['id']}\t{weekNum+1}-{sectionNum+1}\t{eachSection['name']}")
            
        except:
            pass
# 打印列表
for each in v_list:
    print(f"\t{each['link']}\t{each['index']}\t{each['name']}")


# 视频+字幕下载
for index,each in enumerate(v_list):
    vid=each['link']
    # 视频小节信息
    url_leaf = "https://www.xuetangx.com/api/v1/lms/learn/leaf_info/{}/{}/?sign={}".format(cid, vid, sign)
    time.sleep(0.2)
    video = json.loads(requests.get(url_leaf,headers=headers,cookies=cookies).content)


    ccid = video['data']['content_info']['media']['ccid']
    ## 视频
    print(f"--视频 {each['index']} {each['name']}正在下载...")
    time.sleep(0.2)
    url_video = json.loads(requests.get("https://www.xuetangx.com/api/v1/lms/service/playurl/{}/?appid=10000".format(ccid)).content)['data']['sources']['quality10'][0]
    time.sleep(0.2)
    content_video = requests.get(url_video).content
    with open(f"{each['index']} {each['name']}.mp4",'wb') as f:
        f.write(content_video)

    ## 字幕
    time.sleep(0.2)
    url_subtitle = json.loads(requests.post("https://www.xuetangx.com/api/v1/lms/service/s_t_g_p/",data={"c_d": ccid},headers=headers).content)['data'][0]['data']
    time.sleep(0.2)
    raw = requests.get(url_subtitle).text
    a=json.loads(raw)
    with open(f"{each['index']} {each['name']}.srt",'w') as f:
        result=''
        for num,content in enumerate(a['start']):
            result+=f"{num}\n{timePro(a['start'][num])}-->{timePro(a['end'][num])}\n{a['text'][num]}\n\n"
        f.write(result)

    print(f"  --视频+字幕 {each['index']} {each['name']}下载完成...")