from pynput import keyboard
import time

def on_press(key):
    if key==keyboard.Key.esc:
        global stopFlag
        stopFlag=1
        print("就是这个键")
        return False

listener = keyboard.Listener(on_press=on_press)
listener.setDaemon(True)
listener.start()

stopFlag=0

while True:
    if stopFlag==1:
        break
    else:
        time.sleep(1)
        print(233)