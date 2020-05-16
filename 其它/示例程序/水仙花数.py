
for num in range(100,1000):
    si,di,hi=num%10,(num//10)%10,num//100
    if num==(si**3+di**3+hi**3):
        print('%d是一个水仙花数，其中：\n%d+%d+%d=%d'%(num,hi**3,di**3,si**3,num))

