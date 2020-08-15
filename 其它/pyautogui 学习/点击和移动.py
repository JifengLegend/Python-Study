import pyautogui
import time

def tips(str,times=5):
    for eachsecond in range(times):
        print(f'{str} left time :: {times-eachsecond}s')
        time.sleep(1)

if __name__ == "__main__":
    # pyautogui.moveRel(-500,200,duration=1,tween=pyautogui.easeInOutQuad)
    # pyautogui.doubleClick()
    # get position
    tips("get postion",3)
    x,y=pyautogui.position()
    print(x,y)

    time.sleep(3)
    # pyautogui.click(x,y)

    # pyautogui.mouseDown(x+200,y,button="left",duration=5)
    # pyautogui.mouseUp(x-200,y-20,button="left",duration=5)
    # pyautogui.moveTo(x,y)
    # # pyautogui.click()
    # pyautogui.dragRel(100,100,mouseDownUp=True,duration=2)

    # 滚动

    # pyautogui.scroll(10)

