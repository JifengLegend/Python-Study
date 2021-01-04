import json,requests,time

cid = "4230532"
sign = "THU08081000447"

# 请求头 仅供参考
headers = { "xtbz": "xt" }
cookies = { "sessionid": "je1mjha9g5bhvrrfhshautbroy1m4vs8" }

# 章节信息
url_chapter = "https://www.xuetangx.com/api/v1/lms/learn/course/chapter?cid={}&sign={}".format(cid, sign)
time.sleep(0.2)
chapter = json.loads(requests.get(url_chapter,headers=headers,cookies=cookies).content)
print(chapter)
## 第一章的第一节的所有小节
leaf_list = chapter['data']['course_chapter'][0]['section_leaf_list'][0]['leaf_list']
## 第一章的第一节的所有视频小节
video_leaf_list = list(filter(lambda item:item['leaf_type']==0, leaf_list))
## 第一章的第一节的第一个视频小节的id
vid = video_leaf_list[0]['id']

# 视频小节信息
url_leaf = "https://www.xuetangx.com/api/v1/lms/learn/leaf_info/{}/{}/?sign={}".format(cid, vid, sign)
time.sleep(0.2)
video = json.loads(requests.get(url_leaf,headers=headers,cookies=cookies).content)

## ppt等附件
# url_file = video['data']['content_info']['download'][0]['file_url']
# time.sleep(0.2)
# file = requests.get(url_file).content
# with open('1.pptx','wb') as f:
#   f.write(file)

ccid = video['data']['content_info']['media']['ccid']
## 视频
time.sleep(0.2)
url_video = json.loads(requests.get("https://www.xuetangx.com/api/v1/lms/service/playurl/{}/?appid=10000".format(ccid)).content)['data']['sources']['quality10'][0]
time.sleep(0.2)
content_video = requests.get(url_video).content
with open('2.mp4','wb') as f:
  f.write(content_video)
## 字幕
time.sleep(0.2)
url_subtitle = json.loads(requests.post("https://www.xuetangx.com/api/v1/lms/service/s_t_g_p/",data={"c_d": ccid},headers=headers).content)['data'][0]['data']
time.sleep(0.2)
content_subtitle = requests.get(url_subtitle).text
with open('2.txt','w') as f:
  f.write(content_subtitle)