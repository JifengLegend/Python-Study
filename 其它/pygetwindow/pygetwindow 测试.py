import pygetwindow as gw

gw.getActiveWindow().title

for each in gw.getWindowsAt(10,10):
    print(each.title)

gw.getAllTitles()
gw.getAllWindows()
gw.getWindowsWithTitle('python')
gw.getActiveWindow()
gw.getActiveWindowTitle()

rewin=gw.getWindowsWithTitle('正则计算器')[0]
rewin.visible
rewin.title
rewin.isMinimized
rewin.isActive
rewin.isMaximized
rewin.isMinimized
rewin.size
rewin.box
rewin.area
rewin.width
rewin.height
rewin.center
rewin.top
rewin.right
rewin.bottomleft
rewin.topright
rewin.midleft



rewin=gw.getWindowsWithTitle('笔记')[0]

rewin.activate()
rewin.maximize()
rewin.minimize()
rewin.restore()
rewin.close()
rewin.resize(-10,-10)
rewin.resizeTo(600,700)
rewin.resizeRel(-50,-50)
rewin.move(10,10)
rewin.moveTo(100,10)
rewin.moveRel(10,10)
