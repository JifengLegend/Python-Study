import pyautogui
import time

def tips(str,times=5):
    for eachsecond in range(times):
        print(f'{str} left time :: {times-eachsecond}s')
        time.sleep(1)

if __name__ == "__main__":
    tips('ready--',3)
    # a=pyautogui.locateCenterOnScreen(r"C:\Users\m3\Desktop\Working\python 学习\其它\pyautogui 学习\text.png",region=(0,600,1200,300))
    a=pyautogui.locateCenterOnScreen(r"C:\Users\m3\Desktop\Working\python 学习\其它\pyautogui 学习\text.png",region=(0,850,1600,50))

    if a==None:
        print('not found')
    else:
        print(a)
        pyautogui.click(a.x,a.y)
    pyautogui.moveTo(800,450)
    # # pyautogui.mouseDown(button='right')
    pyautogui.dragRel(-100,100,button='right',duration=2,mouseDownUp=True)
