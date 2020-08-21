import pyautogui
import time


time.sleep(2)
times=50
try:
    while(times>=0):
        time.sleep(0.5)
        pyautogui.scroll(-100)
        times-=1
except KeyboardInterrupt:
    print("已退出")

