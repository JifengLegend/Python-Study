def huiJ(string):
    length=len(string)
    last=length-1
    length//=2
    flag=1
    for each in range(length):
        if string[each]!=string[last]:
            flag=0
        last-=1

    if flag==1:
        print('是哦')
    else:
        print('不是')
word=input('请输入一个回文联：')
huiJ(word)


