def count(*parm):
    length = len(parm)
    for each in range(length):
        letters, space, others, digit = 0, 0, 0, 0
        for eachSub in parm[each]:
            if eachSub.isalpha():
                letters += 1
            elif eachSub.isdigit():
                digit += 1
            elif eachSub == ' ':
                space += 1
            else:
                others += 1
        print('第%d个字符串共有：\n英文：%d\t数字：%d\t空格：%d\t其它：%d' % (each, letters, digit, space, others))

count('I love fishc.com.', 'I love you, you love me.')