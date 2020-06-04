import re
import time
import matplotlib.pyplot as plt
#时间检查器
def TimeGeter():
    now=time.strftime('%H')
    now=int(now)
    if now<=4:
        now='凌晨好'
    elif now<=9:
        now='早上好'
    elif now<=13:
        now='中午好'
    elif now<=18:
        now='下午好'
    elif now<=22:
        now='晚上好'
    elif now<=24:
        now='深夜好'
    return now
#括号检查器
def check(s):
    SL, SR = '(', ')'
    arr=[]
    after=''
    for c in s:
        if c in SL:
            # 左符号入栈
            arr.append(c)                  
        elif c in SR:
            if arr[-1]==SL:
                arr.pop()
            else:
                return False         
            if arr==[]:
                after=after+c
                break
        after=after+c        
    return after

#乘幂
def power(a):    
    le=len(re.findall(r'power',a))
    if le==1:
        kuo=re.search(r'power\(.*',a).group()
        kuo=check(kuo)
        cache=re.search(r'power\(.*,.*\)',kuo).group()
        cache1=re.search(r'(?<=power\().*(?=\,)',cache).group()
        cache2=re.search(r'(?<=,).*(?=\))',cache).group()
        cache='{('+cache1+')}^{'+cache2+'}'
        kuo=re.sub(r'(?=[\-|\(|\)|\+|\*|\/|\{|\}|\^])',r'\\',kuo)
        #print('cache:\t',cache,cache1,cache2,'\nkuo:\t',kuo)
        return re.sub(kuo,cache,a)
    elif le==0:
        return a
    else:
        print('提示：该公式中含有多个Power()函数')
    print('已完成Sqrt()的转换,目标公示中Power()的个数为：\t',le,'个')
def numx(a):        #获取有多少个元素
    if re.findall(r'(?<=u\()\d*(?=\))',a)!=[]:
        numx=int(max(re.findall(r'(?<=u\()\d*(?=\))',a)))
        return numx
    else:
        return 1
    print(num)

def sqrt(a):        #开根号
    le=len(re.findall(r'sqrt',a))
    if le==1:
        kuo=re.search(r'sqrt\(.*',a).group()
        kuo=check(kuo)
        cache=re.search(r'sqrt\(.*.*\)',kuo).group()
        cache=re.sub('sqrt\(','',cache)
        cache=cache[:-1]
        cache=r'\\'+r'sqrt{'+cache+'}'        
        kuo=re.sub(r'(?=[\-|\(|\)|\+|\*|\/|\{|\}|\^])',r'\\',kuo)
        #print('cache:\t',cache,'\nkuo:\t',kuo)
        return re.sub(kuo,cache,a)
    elif le==0:
        return a
    else:
        print('提示：该公式中含有多个Sqrt()函数')
    print('已完成Sqrt()的转换目标公示中Sqrt()的个数为：\t',le,'个')

#Main Code
now=TimeGeter()
while 1 :
    mode=int(input(now+',请选择运行模式:\n（0:公式转换）\n（1：公式绘制）：'))      
    a=r'(u(1)-u(2)*u(4)*u(5)-u(3)-u(7))/(u(4)*u(6)+power(u(2),9u(8))))+12)'
    a=input('——请输入公式：')
    if mode==0:
        num=numx(a)+1
        a=power(a)
        a=sqrt(a)
        
        #print('After power(a)',a)
        u=[''for c in range(num)]
        num_i=1
        while num-num_i>=1: #依次输入u()元素值并对原公式进行替换
            u[num_i]=input("——请输入u(%d）的值："%(num_i))
            if num >2:
                a=re.sub(r"u\(%d\)"%(num_i),u[num_i],a)
            else:
                a=re.sub(r"u",u[num_i],a)
            print('——',u)
            num_i=1+num_i

        print('您好，'+now,'，转化后的Latex公式为：')
        print(a)
    else:
        a=a
    ax=plt.figure()
    ax.text(0.1,0.8,r"$%s$"%(a),fontsize=30)
    print('您好，正在为您绘制目标公式')
    plt.show()
