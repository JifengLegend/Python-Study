import pyautogui
import pygetwindow as gw
import random

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
def getPosition(x:float,y:float):
    x1=x if x>1 else 0
    x2=x if x<1 else 0
    y1=y if y>1 else 0
    y2=y if y<1 else 0
    x=tarPos[0]+x1+tarPos[2]*x2
    y=tarPos[1]+y1+tarPos[3]*y2
    pyautogui.moveTo(x,y,tween=pyautogui.easeInOutQuad,duration=1)
def typeWords(strs,time=0.2):
    pyautogui.click()
    pyautogui.hotkey('ctrl','a')
    pyautogui.press('backspace')
    pyautogui.typewrite(message=strs,interval=time)

def getTem()->float:
    a=35.5+random.randint(0,10)*0.12
    a=round(a,1)
    a=str(a)
    return a
if __name__ == "__main__":
    tarWin=findWindow('群精选接龙')
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
        getPosition(0.5,0.45)
        pyautogui.click()
        
        getPosition(0.5,375-158)
        typeWords('vhjnhk')
        pyautogui.press('space')

        getPosition(0.5,506-158)
        typeWords(getTem())

        getPosition(0.5,640-158)
        typeWords(getTem())

        getPosition(0.5,779-158)
        typeWords(getTem())

        pyautogui.scroll(-1000)

        getPosition(0.5,578-158)
        pyautogui.click()

        getPosition(0.5,720-158)
        # pyautogui.click()