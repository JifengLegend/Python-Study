import easygui as g
import sys

while 1:
    g.msgbox('嗨，欢迎来到我们第一个小程序')
    msg = '请问你希望从这里获得什么呢'
    title = '小游戏互动'
    choices = ['谈恋爱', '编程', '搞事情', '琴棋书画']

    choice_window = g.choicebox(msg, title, choices)

    g.msgbox('你的选择是：' + str(choice_window), '结果')

    msg = '你希望重新开始小游戏么'
    title = '请选择'

    if g.ccbox(msg, title):
        pass
    else:
        sys.exit(0)
