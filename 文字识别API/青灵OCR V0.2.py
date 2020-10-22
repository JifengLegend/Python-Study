import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from functools import partial
import requests
import base64
from PIL import ImageGrab
import time
import json
import os
import webbrowser as web
import window
import re
# def click_success():
    # print('我成功啦')
def pre():
    # 保存剪贴板截图
    ui.statusbar.showMessage('正在努力识别中')
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
    # ui.statusbar.showMessage('获取 token 中...')
    if response:
        global access_token
        access_token = response.json()['access_token']
        print(access_token)
def gen():
    pre()
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
    request_url = request_url + "?access_token=" + access_token
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print(response.json())
        text = ''
        for each in response.json()['words_result']:
            text += each["words"] + '\n'
        print(text)
        ui.textShow.setText(text)
        ui.statusbar.showMessage('ready')

def formula():
    pre()
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/formula"
    request_url = request_url + "?access_token=" + access_token
    params['disp_formula']='true'
    response = requests.post(request_url, data=params, headers=headers)

    if response:
        a=response.json()['formula_result'][0]['words']
        print(a)
        ui.textShow.setText(a)
        ui.statusbar.showMessage('ready')
def table():
    pre()
    request_url = "https://aip.baidubce.com/rest/2.0/solution/v1/form_ocr/request"
    request_url = request_url + "?access_token=" + access_token
    response = requests.post(request_url, data=params, headers=headers)

    if response:
        print(response.json())

    ids = {'request_id': response.json()['result'][0]['request_id']}
    getFormUrl = 'https://aip.baidubce.com/rest/2.0/solution/v1/form_ocr/get_request_result'
    getFormUrl = getFormUrl + "?access_token=" + access_token

    time.sleep(3)
    response2 = requests.post(getFormUrl, data=ids, headers=headers)
    if response2:
        global downloadUrl
        downloadUrl=response2.json()['result']['result_data']
        print(downloadUrl)
        ui.textShow.setText(downloadUrl)
        ui.statusbar.showMessage('ready')
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
    ui.textShow.setText(mathPure)
    ui.statusbar.showMessage('ready')
def copy():
    ui.textShow.selectAll()
    ui.textShow.copy()
    ui.statusbar.showMessage('ready')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = window.Ui_MainWindow()
    ui.setupUi(MainWindow)
    # ui.pushButton.clicked.connect(partial(convert,ui))
    MainWindow.show()

    ui.genBtn.clicked.connect(gen)
    ui.formulaBtn.clicked.connect(formula)
    ui.tableBtn.clicked.connect(table)
    ui.openTableBtn.clicked.connect(openTable)
    ui.mathpixBtn.clicked.connect(mathpix)
    ui.copyBtn.clicked.connect(copy)
    ui.textShow.documentTitle()
    ui.statusbar.showMessage('ready')



    sys.exit(app.exec_())