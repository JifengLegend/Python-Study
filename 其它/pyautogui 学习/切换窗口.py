import pyautogui
import time

def tips(str,times=5):
    for eachsecond in range(times):
        print(f'{str} left time :: {times-eachsecond}s')
        time.sleep(1)

if __name__ == "__main__":
    tips('ready',3)
    pyautogui.hotkey('winleft','tab')