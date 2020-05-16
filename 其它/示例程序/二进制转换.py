def d2b(d):
    temp=[]
    result=''
    while d:
        yu=d%2
        d=d//2
        print('d目前为： '+str(d),'余数目前为： '+str(yu))
        temp.append(yu)
    while temp:
        result+=str(temp.pop())
    return result

print(d2b(56))