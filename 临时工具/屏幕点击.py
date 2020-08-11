import pyautogui
import time

def getPosition():
    print("请在五秒后，把鼠标放到预点击位置\n")
    for s in range(5):

        print(5-s)
        time.sleep(1)
    try:
        for i in range(2):
        # Get and print the mouse coordinates.
            x, y = pyautogui.position()
            X,Y=str(x).rjust(4),str(y).rjust(4)
            positionStr = f'鼠标坐标点（X,Y）为：{X},{Y}'
            pix = pyautogui.screenshot().getpixel((x, y)) # 获取鼠标所在屏幕点的RGB颜色
            positionStr += ' RGB:(' + str(pix[0]).rjust(3) + ',' + str(pix[1]).rjust(3) + ',' + str(pix[2]).rjust(
                3) + ')'
            print(positionStr)
            time.sleep(0.5) # 停顿时间
    except:
        print('获取鼠标位置失败')
    return X,Y

# 获取鼠标位置


# pyautogui.click(638,31)

if __name__ == "__main__":
    print('start')
    startJudge=1
    while startJudge==1:
        setTimeRaw=input('--请输入要设定时间（xx.xx分钟后）：\n')
        setTime=setTimeRaw.split('.')
        if len(setTime)==1 and setTime[0].isdigit():
            setTime=int(setTime[0])*60
            startJudge=0
        elif len(setTime)==2:
            setTime=int(setTime[0])*60+int(setTime[1])        
            startJudge=0
        else:
            print("--输入的值有误，请重新输入")
            
    print(setTime)
    x,y=getPosition()
    time.sleep(setTime)
    print('111')
    pyautogui.click(int(x),int(y))

    
            