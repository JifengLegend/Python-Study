password = '22223333'
count = 3

while count:
    in_word = input('请输入密码')
    if password == in_word:
        print('暗号验证成功，欢迎~')
        break
    elif '*' in in_word:
        print('暗号中可没有 * 哦')
        continue
    else:
        count -= 1
        if count:
            print('密码输入错误，请重新输入\t提示：还剩%d次机会' % count)
        else:
            print('您已经用完所有机会，噫，看来你缘分未到')


