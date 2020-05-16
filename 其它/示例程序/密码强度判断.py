# 密码安全性检查代码
#
# 低级密码要求：
#   1. 密码由单纯的数字或字母组成
#   2. 密码长度小于等于8位
#
# 中级密码要求：
#   1. 密码必须由数字、字母或特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）任意两种组合
#   2. 密码长度不能低于8位
#
# 高级密码要求：
#   1. 密码必须由数字、字母及特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）三种组合
#   2. 密码只能由字母开头
#   3. 密码长度不能低于16位
symbol = '~!@#$%^&*()_=-/,.?<>;:[]{}|\\'
char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '0123456789'

passIn = input('请输入要判别的密码：')
lenth = len(passIn)
while (passIn.isspace() or lenth == 0):
    passIn = input('您输入的密码为空，请重新输入')
    lenth = len(passIn)

if lenth <= 8:
    flagLen = 1
elif 8 < lenth <= 16:
    flagLen = 2
elif 16 < lenth:
    flagLen = 3

flagCon = 0


def count(l):
    global flagCon
    for each in passIn:
        if each in l:
            flagCon += 1
            break


count(symbol)
count(char)
count(num)

while 1:
    print('您的密码评级为：', end=' ')
    if flagLen == 1 or flagCon == 1:
        print('低')
    elif flagLen == 3 and flagCon == 3 and (passIn[0] in char):
        print('高\t\t请继续保持')
        break
    else:
        print('中')
    print('请提升密码强度哦')
    break
