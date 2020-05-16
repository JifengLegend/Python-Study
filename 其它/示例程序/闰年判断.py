a = input('请输入要判断的年份')
while not a.isdigit():
    a = input('抱歉，您输入的年份有误，请重新输入：')
year = int(a)
if year / 400 == (year / 400):  # 判断是否有余数
    print(a + '是闰年')
else:
    if (year / 4 == int(year / 4)) and (year / 100 != int(year / 100)):
        print(a + '是闰年')
    else:
        print(a + '不是闰年')
