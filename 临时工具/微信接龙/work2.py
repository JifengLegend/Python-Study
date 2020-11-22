import pyautogui
import pygetwindow as gw
import random
import re
import os
import time

def findWindow(tarWord):
    """通过给出的tarWord关键字，来查询当前窗口，并返回窗体对象\n
    若只存在一个，即定位成功\n
    若存在多个匹配，需要手动选择所需窗口\n
    若不存在，返回None"""
    tarWin=gw.getWindowsWithTitle(tarWord)
    if len(tarWin)==1:
        tarWin=tarWin[0]
    elif len(tarWin)==0:
        print("没有找到含有所输入关键字的窗口")
        return None
    else:
        print("--检索到多个窗口，请选择要定位的窗口名称")
        for num in range(len(tarWin)):
            print(f'{num+1}:{tarWin[num].title}')
        tarNum=int(input("--请选择目标窗口的序号:"))
        tarWin=tarWin[tarNum-1]
    print('--窗口定位成功!')
    return tarWin
def getPosition(x:float,y:float,t=0.2):
    x1=x if x>1 else 0
    x2=x if x<1 else 0
    y1=y if y>1 else 0
    y2=y if y<1 else 0
    x=tarPos[0]+x1+tarPos[2]*x2
    y=tarPos[1]+y1+tarPos[3]*y2
    pyautogui.moveTo(x,y,tween=pyautogui.easeInOutQuad,duration=t)
def typeWords(strs,time=0.1):
    pyautogui.click()
    pyautogui.hotkey('ctrl','a')
    pyautogui.press('backspace')
    pyautogui.typewrite(message=strs,interval=time)

def getTem()->float:
    """
    获取随机温度
    """
    a=35.7+random.randint(0,10)*0.09
    a=round(a,1)
    a=str(a)
    return a
def chRec():
    """
    获取当前python脚本的工作目录
    """
    pyPath=__file__
    recPath=re.sub(r'\/work.*?\.py','',pyPath)
    print(f'当前工作目录为： {recPath}')
    os.chdir(recPath)
if __name__ == "__main__":
    pyautogui.PAUSE=0.2
    tarWin=findWindow('报名接龙')
    chRec()
    if tarWin==None:
        print("未找到指定应用")
        exit()
    else:
        if tarWin.isMinimized:
            tarWin.restore()
            print(tarWin.isMinimized)
        else:
            tarWin.activate()
            tarWin.minimize()
            tarWin.restore()
        print(tarWin.title)
        global tarPos
        tarPos=[tarWin.topleft.x,tarWin.topleft.y,tarWin.size.width,tarWin.size.height]
        print(f'--窗体位置信息为：{tarPos}')
        
        # 跳过提示
        getPosition(0.5,0.59)
        pyautogui.click()

        # 转发文件
        # getPosition(70,698)
        # pyautogui.click()
        # getPosition(0.5,31 3)
        # pyautogui.click()
        # pyautogui.click(847,329)
        # typeWords('233')
        # pyautogui.press('space')
        # pyautogui.click(818,421)


        # 选中自己
        getPosition(0.5,0.59)
        pyautogui.scroll(-800)
        try:
            pocache=pyautogui.locateOnScreen('target2.png',region=(tarWin.topleft.x,tarWin.topleft.y,tarWin.size.width,tarWin.size.height))
            bx,by=pyautogui.center(pocache)
            print(bx-tarPos[0],by-tarPos[1])
            pyautogui.moveTo(bx+300,by,duration=1)
            # getPosition(bx-tarPos[0]+310,by-tarPos[1])
        except TypeError:
            pyautogui.scroll(1600)
            pyautogui.scroll(-800)
            pocache=pyautogui.locateOnScreen('target2.png',region=(tarWin.topleft.x,tarWin.topleft.y,tarWin.size.width,tarWin.size.height))
            bx,by=pyautogui.center(pocache)
            print(bx,by)
            print(bx-tarPos[0],by-tarPos[1])
            pyautogui.moveTo(bx+300,by,duration=1)
            # getPosition(bx-tarPos[0]+250,by-tarPos[1])
        pyautogui.click()
        time.sleep(5)

        # 填写信息

        getPosition(0.5,209)
        typeWords('vhjnhk')
        pyautogui.press('space')
        
        getPosition(0.5,287)
        typeWords(getTem())

        getPosition(0.5,369)
        typeWords(getTem())

        getPosition(0.5,445)
        typeWords(getTem())

        getPosition(0.5,515)
        pyautogui.click()

        getPosition(0.5,705)
        pyautogui.click()

        time.sleep(2)

        # 转发
        getPosition(0.5,226)
        pyautogui.click()

        getPosition(70,698)
        pyautogui.click()

        time.sleep(2)
        getPosition(0.5,237)
        pyautogui.click()
        pyautogui.click(847,329)
        typeWords('4')
        pyautogui.click(822,743)
