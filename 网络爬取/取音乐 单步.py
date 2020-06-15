import urllib.request   
import re
import os
import shutil

#打开网页链接
def openWeb(urlin):
    #获取链接请求
    req=urllib.request.Request(urlin)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36 Edg/81.0.416.45')
    response=urllib.request.urlopen(req)
        #response此时可以执行的操作
            #response.geturl()    获取当前链接
            #response.info()    获取链接head信息
            #response.getcode()    获取http状态
    htmlbyte=response.read()
    #读取二进制网页
    return htmlbyte
    #按着meta中说明的utf-8格式进行解码
def decodeWeb(htmlbyte):
    htmlmain=htmlbyte.decode('utf-8')
    return htmlmain




#保存文件
def saveImg(title,src):
    title=f'./{folderName}/{title}.jpg'
    with open(title,'wb')as f:
        f.write(src)

def saveMusic(Link,Name):
    Link=openWeb(Link)
    title=f'./{folderName}/{Name}.mp3'
    with open(title,'wb')as f:
        f.write(Link)

def Word2List(word):
    cache=re.sub(r' ','',word)
    return cache.split('\n')










if __name__ == "__main__":
    while 1:
        WebContent = input('请输入网址：')

        
        # Link=re.sub(r'.*href="(.*?)".*',r'\1',WebContent)
        # Name=re.sub(r'.*download="(.*?)".*',r'\1',WebContent)

        LinkWord='''http://mobileoc.music.tc.qq.com/M800001a8tgu4DggDy.mp3?guid=ghmusic&vkey=E43D98D501FF1B888BF86AFE52F9931DF93C5518276A8E8B2E506C010F917F4078B3943D54F0102FDA87E6FA125F65CD04332C94455E9A7C&uin=0&fromtag=143
        http://mobileoc.music.tc.qq.com/M80000140o6q3Jvfzr.mp3?guid=ghmusic&vkey=2933CBC281741847250DFB7279D8620EFC48BB283D82B183FCA83BE3D39F8D4B39BAD100F7E3BE36133C36EC63CDD06D3839197B4DFC9E09&uin=0&fromtag=143
        http://mobileoc.music.tc.qq.com/M800000jSDYe2njuWS.mp3?guid=ghmusic&vkey=083BEFD4BF091F2861444AE43C32AA4D5DE30D596BDBBFBABE121F37DEF232C3D30FE741D90B6179F0120E30B4BA0A4FD0D3F54380F6F60B&uin=0&fromtag=143
        http://mobileoc.music.tc.qq.com/M8000024HIjs2EwxYA.mp3?guid=ghmusic&vkey=FBB21E4B026AE38EFC1C0D20188DA77EC7CDDDCA848CD7AB4A8ADE4106DD1C6A5ED7396EB1B283F2DE62EDBECA2B79A3EA7B0E4F90FEC31F&uin=0&fromtag=143
        http://mobileoc.music.tc.qq.com/M8000024HIjs2EwxYA.mp3?guid=ghmusic&vkey=FBB21E4B026AE38EFC1C0D20188DA77EC7CDDDCA848CD7AB4A8ADE4106DD1C6A5ED7396EB1B283F2DE62EDBECA2B79A3EA7B0E4F90FEC31F&uin=0&fromtag=143
        http://mobileoc.music.tc.qq.com/M800002qDomq4crsKv.mp3?guid=ghmusic&vkey=AFEF3EA608E4932BED7CCEB3D7B65B76DCEF79C2C55953BC85496B51E2F7E7A0A1E47A578B29C3A378BCA91888864984461DFB8CDE4274DA&uin=0&fromtag=143
        http://mobileoc.music.tc.qq.com/M800000d5VXa1mFK4G.mp3?guid=ghmusic&vkey=6DD984ABFF982559F58578CBA943913C87E24713E622B591C116743A568CFA6ACDD49038C239BFDFA7BCD2A32EB8392B69FE62E4207850A2&uin=0&fromtag=143
        http://mobileoc.music.tc.qq.com/M800000gkeah1yMIAL.mp3?guid=ghmusic&vkey=EEA8E29770FDB98A8D189552696C4B07A8F032F25C8090D41ED8079A473B2507C3104B63A2044D4D7F0A4B80881AEEB204D011BAA4B74D49&uin=0&fromtag=143
        http://mobileoc.music.tc.qq.com/M8000021XVFE34Wsbw.mp3?guid=ghmusic&vkey=C31CC4C57E42E726F7C538CEF7EA2BBFBDDDDAC51293EAA04D4446633B70F135CA89ABC26EDE2B63498B913304D64AE564A17A04F135D941&uin=0&fromtag=143
        http://mobileoc.music.tc.qq.com/M8000021XVFE34Wsbw.mp3?guid=ghmusic&vkey=C31CC4C57E42E726F7C538CEF7EA2BBFBDDDDAC51293EAA04D4446633B70F135CA89ABC26EDE2B63498B913304D64AE564A17A04F135D941&uin=0&fromtag=143
        http://mobileoc.music.tc.qq.com/M800002RQhEf3ZzXue.mp3?guid=ghmusic&vkey=A3DA2C611DA723CB113C58DE9DE8B8311BFFAE079B44E841EED3ABDDBF848371223ABE9116B0E54ED48D74F64920BA7D7965547C6957B1CE&uin=0&fromtag=143
        http://mobileoc.music.tc.qq.com/M800000uSJdv1nG6w2.mp3?guid=ghmusic&vkey=C6696D7F64201CD894FE31A39ADA934312FA4401D61ECC445A140C454030A6BAD9C415F4C6B79AC904953CD822ED827B3C8868FC2BAFC1CC&uin=0&fromtag=143
        http://mobileoc.music.tc.qq.com/M800003Go5er469cM9.mp3?guid=ghmusic&vkey=7ECF1F68524B4CB6DFA0202EBB92D5F4E92B655866816FF574B123FFC41FC02D5DFD8C4C5197404031C89C442BDC2E23B3BB2AEEF5A8ADC1&uin=0&fromtag=143
        http://mobileoc.music.tc.qq.com/M800000Y49jL10qwEF.mp3?guid=ghmusic&vkey=2EBD11E0B8CE3609D63AC7EB0DB3CF7085E8451C7475FB020224A8C8B99F22A1F82CE8687E5B187DFABB14BC1154FA23F356AE9421F2AEF6&uin=0&fromtag=143
        http://mobileoc.music.tc.qq.com/M8000035XlFi0CdbyK.mp3?guid=ghmusic&vkey=4595A227DDC36BF066B882C0441F97E46077238A53B7F8644206B499E844AECA171B096C162D5440216D852DC02F78BAA03A8E3BB2CF6337&uin=0&fromtag=143
        http://mobileoc.music.tc.qq.com/M800002sgfkg2UKdQZ.mp3?guid=ghmusic&vkey=A43D8448F56047A337FEAEA432E8B886E296A975AD8AE3A84CF371CAB252027B4E6F48F5C7EC831E0600B8CDF827D155B36CAA1750B604FC&uin=0&fromtag=143
        http://mobileoc.music.tc.qq.com/M800000uy1Dg3wxs29.mp3?guid=ghmusic&vkey=6AA5C15DF4C0A4F2C6E3191491365C85B82B3E483361A9D9F31E254D5B424572271E41D5818D9B9B31FA2F64D7A82D913E3888E9E36F8876&uin=0&fromtag=143
        http://mobileoc.music.tc.qq.com/M80000282pUH3hzqBr.mp3?guid=ghmusic&vkey=FE8A0B394AEB5877F03F8A5F689A1FC4E44684623E43C89BD31E860E8378EC86CA448927901801108834099BBD4C415D35FF492548097869&uin=0&fromtag=143
        http://mobileoc.music.tc.qq.com/M800002SuEwu3l2bsf.mp3?guid=ghmusic&vkey=340D5DF222491743391BCDF1462EA378B766F6D59A7709B4A606D9D3DCC94C1F50796B603BD1446CBFC1C3137E54885EB791CC5C63744D29&uin=0&fromtag=143        '''   
        
        NameWord='''说好的幸福呢
蒲公英的约定
心中的日月
逆光
惊叹号
天涯过客
红尘客栈
忍者
轨迹
公公偏头痛
手写的从前
给我一首歌的时间
画沙
阳光宅男
她的睫毛
心跳
说散就散（前任3：再见前E电影主题曲）
你听得到
你好吗'''
        LinkList=Word2List(LinkWord)
        NameList=Word2List(NameWord)



        # 创建保存目录
        folderName = "Music cache"

        try:
            shutil.rmtree(folderName)
            print('原始文件已经清除')
        except FileNotFoundError:
            pass
        os.mkdir(folderName)
        print('--'+folderName)

        for num in range(len(NameList)):
            saveMusic(LinkList[num],NameList[num])
            print(f'--{NameList[num]}已下载，当前进度{num+1}/{len(NameList)}')
 
