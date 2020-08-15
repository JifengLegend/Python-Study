import pyautogui
import time

time.sleep(3)
pyautogui.PAUSE=0.2

pyautogui.moveRel(-100,0,duration=2,tween=pyautogui.easeInOutQuad)


pyautogui.scroll(200)
pyautogui.scroll(200)
pyautogui.scroll(200)
# try:
#     while True:
#         print('I am a big boy')
#         time.sleep(1)
# except KeyboardInterrupt:
#     print("\nExit")