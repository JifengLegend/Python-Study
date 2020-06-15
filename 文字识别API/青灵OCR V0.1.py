from tkinter import *  # 导入 tkinter 模块
import requests
import base64
from PIL import ImageGrab
import time
import json
import os
import webbrowser as web

class TextPlus:
    def __init__(self, window, wide=30, high=9):
        self.window = window
        self.frame = Frame(self.window, padx=10, pady=10)
        self.frame.pack(padx=10, pady=10)
        self.scroll = Scrollbar(self.frame)
        self.scroll.pack(side=RIGHT, fill=Y)
        self.text = Text(self.frame, width=wide, height=high,
                         yscrollcommand=self.scroll.set)
        self.text.pack(fill=BOTH, expand=YES)
        self.scroll.config(command=self.text.yview)

        self.mm = Menu(self.frame, tearoff=False)
        self.mm.add_command(label='全选', command=self.selectAll)
        self.mm.add_command(label='复制', command=self.copy)
        self.mm.add_command(label='粘贴', command=self.paste)
        self.mm.add_separator()
        self.mm.add_command(label='复制+', command=self.copyAll)
        self.mm.add_command(label='清空', command=self.clear)
        self.text.bind('<Button-3>', self.popMenu)

    def get(self):
        return self.text.get(1.0, END)

    def write(self, a):
        self.text.delete(1.0, END)
        self.text.insert(INSERT, a)

    def copy(self):
        self.text.event_generate("<<Copy>>")

    def paste(self):
        self.text.event_generate("<<Paste>>")

    def selectAll(self):
        self.text.tag_add('sel', '1.0', END)

    def copyAll(self):
        self.text.tag_add('sel', '1.0', END)
        self.text.event_generate("<<Copy>>")

    def clear(self):
        self.text.delete(1.0, END)

    def popMenu(self, event):
        self.mm.post(event.x_root, event.y_root)
def pre():
    # 保存剪贴板截图
    try:
        im = ImageGrab.grabclipboard()
        im.save('cache.png', 'PNG')
    except AttributeError as reason:
        pass

    # 打开图片
    f = open('cache.png', 'rb')
    img = base64.b64encode(f.read())
    global params
    params = {"image": img}

    # 获取token
    aid = 'YE8XoIIXzN3Z4NGsl8DV5c2r'
    asd = 'rojyCx5SKy9FRVtCwHwSKkznUBtHlt0v'
    host = f'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={aid}&client_secret={asd}'
    response = requests.get(host)
    global  headers
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    textShow.write('|----______|\n获取 token 中...')
    if response:
        global access_token
        access_token = response.json()['access_token']
        print(access_token)


def gen():
    pre()
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
    request_url = request_url + "?access_token=" + access_token
    response = requests.post(request_url, data=params, headers=headers)
    textShow.write('|--------__|\n正在努力识别中...')
    if response:
        print(response.json())
        text = ''
        for each in response.json()['words_result']:
            text += each["words"] + '\n'
        print(text)
        textShow.write(text)
def formula():
    pre()
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/formula"
    request_url = request_url + "?access_token=" + access_token
    params['disp_formula']='true'
    response = requests.post(request_url, data=params, headers=headers)
    textShow.write('|--------__|\n正在努力识别中...')
    if response:
        a=response.json()['formula_result'][0]['words']
        print(a)
        textShow.write(a)

def table():
    pre()
    request_url = "https://aip.baidubce.com/rest/2.0/solution/v1/form_ocr/request"
    request_url = request_url + "?access_token=" + access_token
    response = requests.post(request_url, data=params, headers=headers)
    textShow.write('|----______|\n生成表格ing...')
    if response:
        print(response.json())

    ids = {'request_id': response.json()['result'][0]['request_id']}
    getFormUrl = 'https://aip.baidubce.com/rest/2.0/solution/v1/form_ocr/get_request_result'
    getFormUrl = getFormUrl + "?access_token=" + access_token
    textShow.write('|--------__|\n获取表格ing...')
    time.sleep(3)
    response2 = requests.post(getFormUrl, data=ids, headers=headers)
    if response2:
        global downloadUrl
        downloadUrl=response2.json()['result']['result_data']
        print(downloadUrl)
        textShow.write(downloadUrl)
def openTable():
     web.open(downloadUrl)
def latex(args, headers,timeout=30):
    service = 'https://api.mathpix.com/v3/latex'
    r = requests.post(service,
                      data=json.dumps(args), headers=headers, timeout=timeout)
    return json.loads(r.text)
def mathpix():
    env = os.environ

    default_headers = {
        'app_id': env.get('APP_ID', '2996710293_qq_com_864f30'),
        'app_key': env.get('APP_KEY', '8664e98ebe9bd0008fd0'),
        'Content-type': 'application/json'
    }

    im = ImageGrab.grabclipboard()
    im.save('equa.png', 'PNG')
    image_data=open('equa.png',"rb").read()
    image_code="data:image/jpg;base64," + base64.b64encode(image_data).decode()
    r = latex({
        'src': image_code,
        'formats': ['latex_simplified']
    },default_headers)
    mathPure=re.sub(' ','',r['latex_simplified'])
    print(mathPure)
    textShow.write(mathPure)
def copyAll():
    textShow.copyAll()

root = Tk()
root.title('青灵OCR V0.1')

frame = LabelFrame(root, text='执行：', padx=10, pady=10)
frame.pack(padx=10, pady=10)


Button(frame, text='通用识别', command=gen, width=10).grid(row=1,column=1,padx=10,pady=10)
Button(frame, text='公式识别', command=formula, width=10).grid(row=1,column=2,padx=10,pady=10)
Button(frame, text='表格识别', command=table, width=10).grid(row=2,column=1,padx=10,pady=10)
Button(frame, text='表格下载', command=openTable, width=10).grid(row=2,column=2,padx=10,pady=10)
Button(frame, text='MathPix', command=mathpix, width=10).grid(row=3,column=1,padx=10,pady=10)
Button(frame, text='复制', command=copyAll, width=10).grid(row=3,column=2,padx=10,pady=10)
# Button(root, text='退出', command=root.quit, width=10).pack(side=RIGHT,padx=20,pady=20)
textShow = TextPlus(root)
root.mainloop()

