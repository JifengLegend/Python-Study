import pygetwindow as gw
import pyautogui
import time
import threading

class MyTimer(threading.Thread):
    def __init__(self,thID,times):
        threading.Thread.__init__(self)
        self.thID=thID
        self.times=times
        self.setDaemon(True)
    def run(self):
        print(f'start thread {self.thID}')
        timeShow(self.times)
        
def timeShow(times):
    """时间进度条的展示面板"""
    if times>=10:
        sec=times/10
        for eachsec in range(10):
            eachsec+=1
            print(f'{str(eachsec*10).rjust(3)}%:|{"="*eachsec}{"-"*(10-eachsec)}|')
            time.sleep(sec)
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
def activateWin(tarWin):
    if tarWin.isMinimized:
        tarWin.restore()
    else:
        tarWin.minimize()
        tarWin.restore()

if __name__ == "__main__":
    # timeShow()
    flags=1
    flagsWord=0
    while flags:
        tarWin=findWindow(input(f'--请{"重新"*flagsWord}输入要定位的窗口标题：\n'))
        if tarWin==None:
            flagsWord=1
        else:
            flags=0
            activateWin(tarWin)


            t1=MyTimer('t1',8)
            # t1.start()
            time.sleep(3)
            tarPos=[tarWin.topleft.x,tarWin.topleft.y,tarWin.size.width,tarWin.size.height]
            print(f'--窗体位置信息为：{tarPos}')
            pyautogui.moveTo(tarPos[0]+tarPos[2]/2,tarPos[1]+20,tween=pyautogui.easeInOutQuad,duration=1)
            pyautogui.dragRel(None,-40,button='left',duration=2)