import re
while 1:
    patten=input('正则匹配开始啦，输入0退出\n\t请输入正则表达式匹配模式')
    if patten=='0':
        print('----程序已经终止了哦----')
        break
    replace=input('\t请输入要替换的内容')
    text=input('\t请输入需要匹配的文本')
    a=re.sub(r'%s'%patten,r'%s'%replace,text)
    print(a)