# coding=utf-8
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QShortcut
from PyQt5 import QtGui,QtCore
from functools import partial
import requests
import base64
from PIL import ImageGrab
import time
import json
import os
import webbrowser as web
import window
import rec_rc
import re
import http.client
import hashlib
import urllib
import random
import json
# def clicked():
    # print('我成功啦')
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
    ui.rawText.setText('|----______|\n获取 token 中...')
    if response:
        global access_token
        access_token = response.json()['access_token']
        print(access_token)
def latex(args, headers,timeout=30):
    service = 'https://api.mathpix.com/v3/latex'
    r = requests.post(service,
                      data=json.dumps(args), headers=headers, timeout=timeout)
    return json.loads(r.text)
def mathMode():
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
    ui.rawText.setText(mathPure)
    ui.statusbar.showMessage('ready')
def gen():
    if ui.c02.checkState()==2:
        mathMode()
    else:
        genMode()
def genMode():
    pre()
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
    request_url = request_url + "?access_token=" + access_token
    response = requests.post(request_url, data=params, headers=headers)
    ui.statusbar.showMessage('正在努力识别中...')
    if response:
        print(response.json())
        text = ''
        for each in response.json()['words_result']:
            text += each["words"] + '\n'
        if ui.c01.checkState()==2:
            text=textClean(text)
            ui.statusbar.showMessage('文字识别/净化 已完成')
        else:
            ui.statusbar.showMessage('文字识别 已完成')
       

        print(text)
        ui.tabCtrl.setCurrentIndex(0)
        ui.rawText.setText(text)
def textClean(strs,addtionRex=r'Fault Tree Handbook with .*Ver.*\nChapter.*'):
    if addtionRex=='':
        pass
    else:
        strs=re.sub(addtionRex,'\n',strs)
    strs=re.sub(r'(?<!\.|。)\n(?![A-Z])',' ',strs)
    return strs
def Trans(raw='apple',to_lang='zh',from_lang='auto',\
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
    myurl = '/api/trans/vip/translate'

    fromLang = from_lang   #原文语种
    toLang = to_lang   #译文语种
    salt = random.randint(32768, 65536)
    q= raw
    sign = appid + q + str(salt) + secretKey
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

        strs=''
        # print (result['trans_result'])
        for each in result['trans_result']:
            strs+=each['dst']+'\n'
            
        strs=strs.strip('\n')
        return strs

    except Exception as e:
        print (e)
    finally:
        if httpClient:
            httpClient.close()
def autoRun():
    if ui.autoR.isChecked()==True:
        ui.defTo.setStyleSheet('color:black;font-weight:normal;')
        ui.defBtn.setStyleSheet('color:black;text-align:center;padding:3px 0px')
        ui.defR.setStyleSheet('color:black;font-weight:normal;')

        ui.autoTo.setStyleSheet('color:#1884d9;font-weight:700;')
        ui.autoBtn.setStyleSheet('color:#1884d9;text-align:center;padding:3px 0px;')
        ui.autoR.setStyleSheet('color:#1884d9;font-weight:700;')

    else:
        ui.defTo.setStyleSheet('color:#1884d9;font-weight:700;')
        ui.defBtn.setStyleSheet('color:#1884d9;text-align:center;padding:3px 0px;')
        ui.defR.setStyleSheet('color:#1884d9;font-weight:700;')

        ui.autoTo.setStyleSheet('color:black;font-weight:normal;')
        ui.autoBtn.setStyleSheet('color:black;text-align:center;padding:3px 0px;')
        ui.autoR.setStyleSheet('color:black;font-weight:normal;')
    ui.statusbar.showMessage('当前状态为：'+search())


def autoChange():
    global autoBing,defBing
    autoBing=not autoBing
    if(autoBing):
        ui.autoTo.setText('En')
    else:
        ui.autoTo.setText('Zh')
    ui.statusbar.showMessage('当前状态为：'+search())

def defChange():
    global autoBing,defBing
    defBing=not defBing
    if(defBing):
        ui.defBtn.setText('<--')
    else:
        ui.defBtn.setText('-->')
    ui.statusbar.showMessage('当前状态为：'+search())

def preLoad():
    ui.autoTo.setStyleSheet('color:#1884d9;font-weight:700;')
    ui.autoBtn.setStyleSheet('color:#1884d9;text-align:center;padding:3px 0px')
    ui.autoR.setStyleSheet('color:#1884d9;font-weight:700;')
    ui.tabCtrl.setCurrentIndex(0)
    ui.statusbar.showMessage('Ready')
def search():
    strs=''
    if(ui.autoR.isChecked()==True):
        strs+='Auto To '
        if autoBing==False:
            strs+='Zh'
        else:
            strs+='En'
    else:
        if defBing==False:
            strs='Zh To En'
        else:
            strs='En To Zh'
    return strs
def getType():
    cache=search().lower()
    cache=cache.split(' ')
    return cache[0],cache[2]
def transMode():
    if ui.c01.checkState()==2:
        raw=ui.rawText.toPlainText()
        raw=textClean(raw)
        ui.rawText.setText(raw)
    cache=getType()
    print(cache)
    strs=Trans(ui.rawText.toPlainText(),cache[1],cache[0],\
        app_id='20201027000600376',secret_Key='5wiYK3JixYvFggKoGefp'
        )
    print(strs)

    ui.transText.setText(strs)
    ui.tabCtrl.setCurrentIndex(1)
    ui.statusbar.showMessage('翻译完成~')
def copyAction():
    if ui.tabCtrl.currentIndex()==0:
        ui.rawText.selectAll()
        ui.rawText.copy()
        ui.statusbar.showMessage('源文本已复制到剪贴板啦')
    else:
        ui.transText.selectAll()
        ui.transText.copy()
        ui.statusbar.showMessage('翻译结果已复制到剪贴板啦')
def delAction():
    if ui.tabCtrl.currentIndex()==0:
        ui.rawText.selectAll()
        ui.rawText.clear()
        ui.statusbar.showMessage('源文本窗口已清空')
    else:
        ui.transText.selectAll()
        ui.transText.clear()
        ui.statusbar.showMessage('翻译窗口已清空')
def regMes():
    if ui.c01.checkState()==2:
        ui.statusbar.showMessage('开启文本净化')
    else:
        ui.statusbar.showMessage('关闭文本净化')
def mathMes():
    if ui.c02.checkState()==2:
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/ico/公式.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ui.statusbar.showMessage('公式识别模式已启动~')
        ui.genBtn.setText('公式识别')
        ui.genBtn.setIcon(icon1)
    else:
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/ico/scanning.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ui.statusbar.showMessage('公式识别模式关闭，当前为通用识别')
        ui.genBtn.setText('文本识别')
        ui.genBtn.setIcon(icon1)
def onePress():
    ui.rawText.selectAll()
    ui.rawText.clear()
    ui.rawText.paste()

    if ui.c01.checkState()==2:
        raw=ui.rawText.toPlainText()
        raw=textClean(raw)
        ui.rawText.setText(raw)
    cache=getType()
    print(cache)
    strs=Trans(ui.rawText.toPlainText(),cache[1],cache[0],\
        app_id='20201027000600376',secret_Key='5wiYK3JixYvFggKoGefp')
    print(strs)
    ui.transText.setText(strs)
    ui.tabCtrl.setCurrentIndex(1)
    ui.statusbar.showMessage('翻译完成~')

    ui.statusbar.showMessage('一键翻译 已完成')
def onTop():

    _translate = QtCore.QCoreApplication.translate
    if not ui.topAction.isChecked():
        MainWindow.setWindowFlags(QtCore.Qt.Widget)# 取消置顶
        MainWindow.show()
        ui.statusbar.showMessage('窗口置顶 已取消')
        MainWindow.setWindowTitle(_translate("MainWindow", "可可 OCR"))
    else:
        MainWindow.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint) # 打开置顶
        MainWindow.show()
        MainWindow.setWindowTitle(_translate("MainWindow", "可可 OCR - 置顶模式"))
        ui.statusbar.showMessage('窗口置顶 已启动')
def activeAutoCatch():
    if ui.autoCatch.isChecked():
        ui.statusbar.showMessage('自动捕获模式 已启动')
        ui.autoMBtn.setChecked(1)
        ui.autoCatch.setChecked(1)

    else:
        ui.statusbar.showMessage('自动捕获模式 已关闭')
        ui.autoMBtn.setChecked(0)
        ui.autoCatch.setChecked(0)
    pass
def activeMAutoCatch():
    if  ui.autoMBtn.isChecked():
        ui.statusbar.showMessage('自动捕获模式 已启动')
        ui.autoCatch.setChecked(1)

    else:
        ui.statusbar.showMessage('自动捕获模式 已关闭')
        ui.autoCatch.setChecked(0)
    pass

def runAutoCatch():
    global runTimes
    if cp.text()==ui.transText.toPlainText():
        print('检测到刚复制的内容为刚才的翻译结果，跳过')
        pass
    else:        
        if runTimes%2==0:
            if ui.autoCatch.isChecked():
                onePress()        
            else:
                pass
    runTimes+=1

def fontAddAction():
    global fontSize
    fontSize+=1
    font = QtGui.QFont()
    font.setFamily("微软雅黑 Light") #括号里可以设置成自己想要的其它字体
    font.setPointSize(fontSize) 
    ui.rawText.setFont(font)
    ui.transText.setFont(font)
    ui.statusbar.showMessage(f'当前字体大小调整为：{fontSize}')

def fontDecAction():
    global fontSize
    fontSize-=1
    fontSize=fontSize if fontSize>2 else 2
    font = QtGui.QFont()
    font.setFamily("微软雅黑 Light") #括号里可以设置成自己想要的其它字体
    font.setPointSize(fontSize) 
    ui.rawText.setFont(font)
    ui.transText.setFont(font)
    ui.statusbar.showMessage(f'当前字体大小调整为：{fontSize}')
def printVer():
    ver=0.5
    ui.statusbar.showMessage(f'当前`可可 OCR`的版本为 V{ver}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = window.Ui_MainWindow()
    ui.setupUi(MainWindow)
    # ui.pushButton.clicked.connect(partial(convert,ui))
    cp=app.clipboard()
    cp.dataChanged.connect(runAutoCatch)
    ui.genBtn.clicked.connect(gen)
    ui.autoR.toggled.connect(autoRun)
    global autoBing,defBing,topBing,fontSize,runTimes
    autoBing,defBing,topBing=False,False,False
    fontSize,runTimes=14,0
    preLoad()
    ui.autoBtn.clicked.connect(autoChange)
    ui.defBtn.clicked.connect(defChange)
    ui.transBtn.clicked.connect(transMode)
    ui.copyBtn.clicked.connect(copyAction)
    ui.delBtn.clicked.connect(delAction)
    ui.c02.toggled.connect(regMes)
    ui.c02.toggled.connect(mathMes)
    # QShortcut(QtGui.QKeySequence(MainWindow.tr('Ctrl+B')),MainWindow,onePress)
    # QShortcut(QtGui.QKeySequence(MainWindow.tr('Ctrl+Q')),MainWindow,onTop)
    ui.oneAction.triggered.connect(onePress)
    ui.topAction.triggered.connect(onTop)
    ui.fontAdd.triggered.connect(fontAddAction)
    ui.fontDec.triggered.connect(fontDecAction)
    ui.autoCatch.triggered.connect(activeAutoCatch)
    ui.verBtn.triggered.connect(printVer)
    ui.autoMBtn.clicked.connect(activeMAutoCatch)
    ui.oneMBtn.clicked.connect(onePress)


    MainWindow.show()
    sys.exit(app.exec_())