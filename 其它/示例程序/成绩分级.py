score = int(input('请输入要判别的成绩：'))
a, b, c, d, e = '成绩为A', '成绩为B', '成绩为C', '成绩为D', '成绩不合格'
if 90 <= score < 100:
    print(a)
elif 80 <= score < 90:
    print(b)
elif 70 <= score < 80:
    print(c)
elif 60 <= score < 70:
    print(c)
elif score <= 60:
    print(e)
