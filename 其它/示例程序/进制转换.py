# 进制转换
q = True
while q:
    num = input('请输入一个整数（输入q程序结束）')
    if num != 'Q':
        num = int(num)
        print('十六进制形式：%d -> 0x%x' % (num, num))
        print('八进制形式：%d -> 0o%o' % (num, num))
        print('二进制形式：%d -> ' % num,bin(num))
    else:
        q = False
