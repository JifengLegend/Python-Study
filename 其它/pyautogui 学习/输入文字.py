import pyautogui
import time

def tips(str,times=5):
    for eachsecond in range(times):
        print(f'{str} left time :: {times-eachsecond}s')
        time.sleep(1)

def findTextWindow():
    a=pyautogui.locateCenterOnScreen(r"C:\Users\m3\Desktop\Working\python 学习\其它\pyautogui 学习\text.png",region=(0,850,1600,50))
    if a==None:
        print('Text window not found')
        # pyautogui.alert('Text window not found',button='OK')
        return None
    else:
        print(a)
        pyautogui.click(a.x,a.y)
        return True
    
def clearAll():
    pyautogui.hotkey('ctrl','a')
    pyautogui.press('delete')
if __name__ == "__main__":
    tips('ready--',3)

    actives=findTextWindow()
    if actives==True:
        clearAll()
        pyautogui.press('shift')
        pyautogui.typewrite("i love python\n"*10,0.05)
        pyautogui.hotkey('ctrl','a')
        pyautogui.hotkey('ctrl','c')
        # pyautogui.click()y
        # time.sleep(1)
        pyautogui.hotkey("ctrl","v")
        pyautogui.hotkey("ctrl","v")
        pyautogui.hotkey("ctrl","v")
        # pyautogui.typewrite(['g','left','left','left','left','backspace',' G','end','.'],0.25)
    else:
        pass