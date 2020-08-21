
from pynput import keyboard


def on_press1(key):
    # 如果按下了 <Esc> 键
    if key == keyboard.Key.esc:
        global is_stopped
        is_stopped = True

        # 停止监听
        listener.stop()


is_stopped = False

listener = keyboard.Listener(on_press=on_press1)
listener.start()

print("按下 <Esc> 键退出程序~")
while True:
    # 如果停止了监听则退出死循环
    if is_stopped:
        print("程序已退出")
        break